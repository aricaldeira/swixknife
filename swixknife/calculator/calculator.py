

__all__ = ('SezimalCalculator',)

from decimal import Decimal, localcontext
from fractions import Fraction as DecimalFraction

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction, \
    SezimalDecimalUnit
from ..base import default_to_sezimal_digits, validate_clean_decimal, \
    sezimal_format, decimal_format, niftimal_format, sezimal_context
from ..base.formatting import PER_SYMBOLS
from ..exponents import sezimal_exponent_to_decimal_exponent, \
    decimal_exponent_to_sezimal_exponent
from ..units import sezimal_to_decimal_unit, decimal_to_sezimal_unit, \
    decimal_to_decimal_unit
from ..text import sezimal_spellout
from ..functions.trigonometry import *
from ..localization import SezimalLocale, sezimal_locale

from .operations import *


class SezimalCalculator:
    def __init__(self, expression: str = '0', locale: str | SezimalLocale = None):
        self.sezimal_digits = False
        self.sezimal_punctuation = True
        self.regularized_digits = True
        self.regularized_letter_digits = False
        self.decimal = False
        self.precision = 3
        self.locale = locale
        self.grouping_digits = 3
        self.suffix = ''
        self.decimal_suffix = ''
        self.factor = Sezimal(1)
        self.unit = ''
        self.decimal_unit = ''
        self.unit_as_fraction = False
        self.angle = 'mdl'
        self.decimal_angle = 'tau_rad'
        self.angle_as_fraction = False
        self.debug = False
        self.currency_mode = False
        self.expression = expression

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, text: str):
        self._expression = text.replace('E', 'e')
        self._expression = self._expression.replace('pi', 'π').replace('PI', 'π')
        self._expression = self._expression.replace('tau', 'τ').replace('TAU', 'τ')
        self._expression = self._expression.replace('phi', 'φ').replace('PHI', 'φ')
        self._expression = self._expression.replace('sqrt_2', '√2').replace('SQRT_2', '√2')
        self._expression = self._expression.replace('\u200b', '')
        self._expression = self._expression.replace('SeC', 'SEC')

        if self.debug:
            self._prepare_expression()
        else:
            try:
                self._prepare_expression()
                self.error = False
            except:
                self._set_error()

    @property
    def sezimal_expression(self):
        return self._sezimal_expression

    @property
    def decimal_expression(self):
        return self._decimal_expression

    @property
    def decimal(self):
        return self._decimal

    @decimal.setter
    def decimal(self, decimal: bool = False):
        self._decimal = decimal

    @property
    def precision(self):
        if self.decimal:
            return self._decimal_precision

        return self._sezimal_precision

    @precision.setter
    def precision(self, precision: int | str | Decimal | Sezimal | SezimalInteger):
        precision = SezimalInteger(precision)

        if self.decimal:
            self._decimal_precision = precision
            self._sezimal_precision = decimal_exponent_to_sezimal_exponent(precision * -1) * -1

        else:
            self._sezimal_precision = precision
            self._decimal_precision = sezimal_exponent_to_decimal_exponent(precision * -1) * -1

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale: str | SezimalLocale = None):
        self._locale = sezimal_locale(locale)

    @property
    def display(self):
        if self.sezimal_digits:
            res = default_to_sezimal_digits(self._display)
        else:
            res = self._display

        if self.locale and self.locale.RTL:
            return '\N{RLO}' + res + '\N{PDF}'

        return res

    @property
    def decimal_display(self):
        res = self._decimal_display

        if self.locale and self.locale.RTL:
            return '\N{RLO}' + res + '\N{PDF}'

        return res

    @property
    def niftimal_display(self):
        return self._niftimal_display

    @property
    def spellout(self):
        if self.locale:
            lang = self.locale.LANGUAGE_TAG
        else:
            lang = 'en'

        if self.grouping_digits == 4:
            lang = 'en_misali'

        expression = self._sezimal_expression.replace('_', '')

        if expression.endswith(' ^ 2'):
            expression = expression[0:-3] + '²'
        elif expression.endswith(' ^ 3'):
            expression = expression[0:-3] + '³'

        expression = expression.replace(' ^ 2 ',' ² ')
        expression = expression.replace(' ^ 3 ',' ³ ')

        spellout = ''

        for part in expression.split(' '):
            if not part:
                continue

            if self.unit and part.replace('.', '').isdigit():
                spellout += sezimal_spellout(f'SH-{self.unit} {part}', lang, self.sezimal_punctuation) + ' '
            elif self.unit and part.replace('/', '').replace('⁄', '').isdigit():
                spellout += sezimal_spellout(f'SH-{self.unit} {part}', lang, self.sezimal_punctuation) + ' '
            else:
                if self.currency_mode:
                    try:
                        part = SezimalDecimalUnit(part)
                        spellout += sezimal_spellout(part.unit, lang, self.sezimal_punctuation) + '; '
                        spellout += sezimal_spellout(part.subunit, lang, self.sezimal_punctuation) + ' '
                        continue
                    except:
                        pass

                spellout += sezimal_spellout(part, lang, self.sezimal_punctuation) + ' '

        return spellout.strip()

    def _determine_precision(self, number: str, max_precision: SezimalInteger, result: bool = False) -> SezimalInteger:
        number = str(number)

        if '.' in number and number[-1] != '.':
            precision = SezimalInteger(Decimal(len(number.split('.')[1])))

            if result:
                while number and number.endswith('0'):
                    precision -= 1
                    number = number[:-1]

        elif ';' in number and number[-1] != ';':
            precision = SezimalInteger(Decimal(len(number.split(';')[1])))

            if result:
                while number and number.endswith('0'):
                    precision -= 1
                    number = number[:-1]

        else:
            precision = SezimalInteger(0)

        return min(precision, max_precision)

    def _format_sezimal(self, number, display: bool = False, part: str = '', keep_original_aspect=True):
        if part and type(part) == str and '⁄' in part:
            numerator, denominator = part.split('⁄')

            numerator = self._format_sezimal(numerator, display, numerator, keep_original_aspect)

            if denominator:
                denominator = self._format_sezimal(denominator, display, denominator, keep_original_aspect)

                if display and denominator == '1':
                    return numerator

                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif type(number) == SezimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = self._format_sezimal(numerator, display, numerator, keep_original_aspect)
            denominator = self._format_sezimal(denominator, display, numerator, keep_original_aspect)

            if display and denominator == '1':
                return numerator

            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._sezimal_precision)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'sezimal_places': precision,
            'sezimal_digits': self.sezimal_digits,
            'sezimal_punctuation': self.sezimal_punctuation,
            'recurring_digits_notation': recurring_digits_notation,
            'keep_original_aspect': keep_original_aspect,
            'grouping_digits': self.grouping_digits,
        }

        if display:
            params['use_fraction_group_separator'] = True
            params['suffix'] = self.suffix
        else:
            params['sezimal_separator'] = '.'
            params['group_separator'] = '_'
            params['fraction_group_separator'] = '_'
            params['sezimal_digits'] = False
            params['sezimal_punctuation'] = False
            params['typographical_negative'] = False

        if not keep_original_aspect:
            if not recurring_digits_notation:
                number = round(number, precision)

        if display:
            if self.currency_mode and type(number) == SezimalDecimalUnit:
                del params['sezimal_places']
                return self.locale.format_currency(number, **params)

            return self.locale.format_number(number, **params)

        if self.currency_mode and type(number) == SezimalDecimalUnit:
            del params['sezimal_places']
            res = sezimal_format(number.unit, **params)

            if part and part[-1] == ';':
                res += ';'
            elif number.subunit:
                res += ';' + sezimal_format(number.subunit, **params)

            return res

        return sezimal_format(number, **params)

    def _format_decimal(self, number, display: bool = False, part: str = '', keep_original_aspect: bool = True):
        if (part and (type(part) == str and '⁄' in part)) or (type(number) == SezimalFraction):
            if type(number) == SezimalFraction:
                numerator = number.numerator.decimal
                denominator = number.denominator.decimal
            else:
                numerator, denominator = part.split('⁄')

            numerator = self._format_decimal(numerator, display, numerator, keep_original_aspect)

            if denominator:
                denominator = self._format_decimal(denominator, display, denominator, keep_original_aspect)

                if display and denominator == '1':
                    return numerator

                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif not part and type(number) == DecimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = Decimal(numerator)
            denominator = Decimal(denominator)
            numerator = self._format_decimal(numerator, display, numerator, keep_original_aspect)
            denominator = self._format_decimal(denominator, display, numerator, keep_original_aspect)

            if display and denominator == '1':
                return numerator

            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._decimal_precision)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'decimal_places': precision,
            'recurring_digits_notation': recurring_digits_notation,
            'keep_original_aspect': keep_original_aspect,
        }

        if display:
            params['use_fraction_group_separator'] = True
            params['suffix'] = self.decimal_suffix
        else:
            params['decimal_separator'] = '.'
            params['group_separator'] = '_'
            params['fraction_group_separator'] = '_'
            params['typographical_negative'] = False

        if not keep_original_aspect:
            if not recurring_digits_notation:
                number = round(number, precision.decimal)

        if display:
            return self.locale.format_decimal_number(number, **params)

        return decimal_format(number, **params)

    def _format_niftimal(self, number, part: str = ''):
        if part and type(part) == str and '⁄' in part:
            numerator, denominator = part.split('⁄')

            numerator = self._format_niftimal(Sezimal(numerator), numerator)

            if denominator:
                denominator = self._format_niftimal(Sezimal(denominator), denominator)

                if denominator == '1':
                    return numerator

                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif not part and type(number) == SezimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = self._format_niftimal(numerator, str(numerator))
            denominator = self._format_niftimal(denominator, str(numerator))

            if denominator == '1':
                return numerator

            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._sezimal_precision)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'niftimal_places': precision // 2 if precision % 2 == 0 else (precision // 2) + 1,
            'sezimal_digits': self.sezimal_digits,
            'sezimal_punctuation': self.sezimal_punctuation,
            'recurring_digits_notation': recurring_digits_notation,
            'use_fraction_group_separator': True,
            'suffix': self.suffix,
            'regularized_digits': self.regularized_digits,
            'regularized_letter_digits': self.regularized_letter_digits,
            # 'niftimal_separator': '󱹮',
            # 'group_separator': ' ',
            # 'fraction_group_separator': ' ',
        }

        if type(number) == str:
            number = Sezimal(number)

        return self.locale.format_niftimal_number(number, **params)
        # return niftimal_format(number, **params)

    def _apply_sezimal_or_recurring_mark(self, display: str, separator: str, suffix: str) -> str:
        if suffix in PER_SYMBOLS:
            display = display[0:len(suffix) * -1]
        elif suffix:
            display = display[0:(len(suffix) + 1) * -1]

        display += separator

        if suffix in PER_SYMBOLS:
            display += suffix
        elif suffix:
            display += '\u202f' + suffix

        return display

    def _prepare_expression(self):
        if not self.expression:
            self._display = ''
            self._decimal_display = ''
            self._niftimal_display = ''
            self._prepared_expression = ''
            self._sezimal_expression = ''
            self._decimal_expression = ''
            return

        if self.expression == '0':
            if self.sezimal_digits:
                self._display = '󱸀'
                self._niftimal_display = '󱸀'
            else:
                self._display = '0'
                self._niftimal_display = '0'

            self._decimal_display = '0'

            if self.decimal:
                self._prepared_expression = "Decimal('0')"
            else:
                self._prepared_expression = "Sezimal('0')"

            self._sezimal_expression = "0"
            self._decimal_expression = "0"

            return

        exp = self.expression

        #
        # Replace operators first
        #
        for o in _OPERATOR:
            text = _OPERATOR[o]
            exp = exp.replace(o, text)

        parenthesis_opened = 0
        trigonometry_opened = 0

        prepared_expression = ''
        display = ''
        decimal_display = ''
        niftimal_display = ''
        sezimal_expression = ''
        decimal_expression = ''

        parts = exp.split()

        if parts and parts[-1] == '__PLUS_MINUS__':
            parts = parts[:-1]

            if len(parts) >= 2:
                if parts[-2] == '__SUBTRACT__':
                    last_part = parts[-1]
                    parts = parts[0:-2]
                    parts.append(last_part)

                else:
                    parts[-1] = '-' + parts[-1]

            else:
                parts[-1] = '-' + parts[-1]

        previous_part = ''

        for part in parts:
            part = part.strip()

            if not part:
                continue

            if part in _IN_PREPARED_EXPRESSION_OPERATION:
                prepared_expression += _IN_PREPARED_EXPRESSION_OPERATION[part]

                if part in _PER_OPERATIONS:
                    sezimal_expression += f'{_NICE_OPERATION[part]} '
                    decimal_expression += f'{_NICE_OPERATION[part]} '
                elif part in _NO_SPACE_OPERATIONS:
                    sezimal_expression += f'{_IN_EXPRESSION_OPERATION[part]}'
                    decimal_expression += f'{_IN_EXPRESSION_OPERATION[part]}'
                else:
                    sezimal_expression += f' {_IN_EXPRESSION_OPERATION[part]} '
                    decimal_expression += f' {_IN_EXPRESSION_OPERATION[part]} '

                #
                # Deals with negative numbers
                #
                if part == '__SUBTRACT__':
                    if previous_part == '':
                        display += ' −'
                        decimal_display += ' −'
                        niftimal_display += ' −'

                    elif previous_part in _IN_PREPARED_EXPRESSION_OPERATION:
                        if previous_part.strip() in _PER_OPERATIONS:
                            display += _NICE_OPERATION[part]
                            decimal_display += _NICE_OPERATION[part]
                            niftimal_display += _NICE_OPERATION[part]
                        else:
                            display += ' −'
                            decimal_display += ' −'
                            niftimal_display += ' −'

                    else:
                        display += _NICE_OPERATION[part]
                        decimal_display += _NICE_OPERATION[part]
                        niftimal_display += _NICE_OPERATION[part]

                else:
                    display += _NICE_OPERATION[part]
                    decimal_display += _NICE_OPERATION[part]
                    niftimal_display += _NICE_OPERATION[part]

                previous_part = part

                if self.decimal:
                    for symbol, expression_text, niftimal_text, sd_niftimal_text in _PER_OPERATIONS_DECIMAL_TO_SEZIMAL:
                        display_text = expression_text.replace('/', '÷')
                        display_text = display_text.replace('_', self.locale.GROUP_SEPARATOR)

                        display = display.replace(symbol, display_text)
                        sezimal_expression = sezimal_expression.replace(symbol, expression_text)

                        if self.sezimal_digits:
                            niftimal_display = niftimal_display.replace(symbol, sd_niftimal_text)
                        else:
                            niftimal_display = niftimal_display.replace(symbol, niftimal_text)

                else:
                    for symbol, expression_text in _PER_OPERATIONS_SEZIMAL_TO_DECIMAL:
                        display_text = expression_text.replace('/', '÷')
                        display_text = display_text.replace('_', self.locale.GROUP_SEPARATOR)

                        decimal_display = decimal_display.replace(symbol, display_text)
                        decimal_expression = decimal_expression.replace(symbol, expression_text)

                if part in _TRIGONOMETRIC_FUNCTION:
                    trigonometry_opened += 1
                    parenthesis_opened += 1

                if (not parenthesis_opened) and part == '__LEFT_PARENTHESIS__':
                    parenthesis_opened += 1
                elif parenthesis_opened and part == '__RIGHT_PARENTHESIS__':
                    parenthesis_opened -= 1

                    if trigonometry_opened > 0:
                        trigonometry_opened -= 1

                continue

            if part == '.' or part == ';':
                continue

            previous_part = part

            if part in _CONSTANTS:
                prepared_expression += part
                display += part
                decimal_display += part
                niftimal_display += part
                sezimal_expression += part
                decimal_expression += part

            elif self.decimal:
                if '⁄' in part:
                    if part.endswith('⁄'):
                        number = Decimal(part[:-1])
                        prepared_expression += f"Decimal('{number}')"
                    else:
                        num, den = part.split('⁄')
                        number = Decimal(num) / Decimal(den)
                        prepared_expression += f"Decimal('{number}')"
                elif part.endswith('..'):
                    number = Decimal(validate_clean_decimal(part[:-2]))
                    prepared_expression += f"Decimal('{number}')"
                elif part.endswith('.'):
                    number = Decimal(validate_clean_decimal(part[:-1]))
                    prepared_expression += f"Decimal('{number}')"
                elif part.endswith(';'):
                    number = Decimal(validate_clean_decimal(part[:-1]))
                    prepared_expression += f"Decimal('{number}')"
                else:
                    number = Decimal(validate_clean_decimal(part))
                    prepared_expression += f"Decimal('{number}')"

                decimal_display += self._format_decimal(part, display=True, part=part)
                decimal_expression += self._format_decimal(part, part=part)

                if trigonometry_opened and self.angle and self.decimal_angle:
                    if self.angle.endswith('mdl'):
                        number = decimal_to_sezimal_unit(number, self.decimal_angle, self.angle, return_fraction=self.angle_as_fraction)
                    else:
                        number = decimal_to_decimal_unit(number, self.decimal_angle, self.angle, return_fraction=self.angle_as_fraction)

                    if not self.angle_as_fraction:
                        number = round(number, self._sezimal_precision)

                elif self.unit and self.decimal_unit:
                    number = decimal_to_sezimal_unit(number, self.decimal_unit, self.unit, return_fraction=self.unit_as_fraction)

                    if not self.unit_as_fraction:
                        number = round(number, self._sezimal_precision)

                elif self.currency_mode:
                    number = SezimalDecimalUnit(number)

                elif self.factor:
                    number *= self.factor
                    number = round(number, self._sezimal_precision)

                else:
                    number = Sezimal(number)

                display += self._format_sezimal(number, display=True)
                niftimal_display += self._format_niftimal(number)
                sezimal_expression += self._format_sezimal(number)

            else:
                cleaned_part = part

                if '⁄' in part:
                    if part.endswith('⁄'):
                        cleaned_part = part[:-1]
                        number = Sezimal(part[:-1])
                        prepared_expression += f"Sezimal('{number}')"
                    else:
                        number = SezimalFraction(part)
                        prepared_expression += f"SezimalFraction('{number}')"
                elif part.endswith('..'):
                    cleaned_part = part[:-2]
                    number = Sezimal(part[:-2])
                    prepared_expression += f"Sezimal('{number}')"
                elif part.endswith('.'):
                    cleaned_part = part[:-1]
                    number = Sezimal(part[:-1])
                    prepared_expression += f"Sezimal('{number}')"
                elif self.currency_mode:
                    number = SezimalDecimalUnit(part)

                    if part[-1] == ';':
                        prepared_expression += f"SezimalDecimalUnit('{number};')"
                    else:
                        prepared_expression += f"SezimalDecimalUnit('{number}')"

                    cleaned_part = str(number.sezimal)
                else:
                    number = Sezimal(part)
                    prepared_expression += f"Sezimal('{number}')"

                if self.currency_mode:
                    display += self._format_sezimal(number, display=True, part=part)
                    niftimal_display += self._format_niftimal(cleaned_part, part=part)
                    sezimal_expression += self._format_sezimal(number, part=part)
                else:
                    display += self._format_sezimal(part, display=True, part=part)
                    niftimal_display += self._format_niftimal(cleaned_part, part=part)
                    sezimal_expression += self._format_sezimal(part, part=part)

                if trigonometry_opened and self.angle and self.decimal_angle:
                    if self.angle.endswith('mdl'):
                        number = sezimal_to_decimal_unit(number, self.angle, self.decimal_angle, return_fraction=self.angle_as_fraction)
                    else:
                        number = decimal_to_decimal_unit(number, self.angle, self.decimal_angle, return_fraction=self.angle_as_fraction)

                    if not self.angle_as_fraction:
                        with localcontext() as context:
                            context.prec = int(self._decimal_precision)
                            number = round(number.decimal, int(self._decimal_precision))

                elif self.unit and self.decimal_unit:
                    number = sezimal_to_decimal_unit(number, self.unit, self.decimal_unit, return_fraction=self.unit_as_fraction)

                    if not self.unit_as_fraction:
                        try:
                            number = round(number.decimal, int(self._decimal_precision))
                        except:
                            number = number.decimal

                elif self.currency_mode:
                    number = number.decimal

                elif self.factor:
                    number /= self.factor

                    try:
                        number = round(number.decimal, int(self._decimal_precision))
                    except:
                        number = number.decimal

                else:
                    number = number.decimal

                decimal_display += self._format_decimal(number, display=True)
                decimal_expression += self._format_decimal(number)

        for i in range(parenthesis_opened):
            prepared_expression += ')'

        if self.sezimal_digits:
            display = display.replace('lbin', 'log󱹊')
            display = display.replace('lsez', 'log󱹉󱹈')
            display = display.replace('ldec', 'log󱹉󱹌')
        else:
            display = display.replace('lbin', 'log₂')
            display = display.replace('lsez', 'log₁₀')
            display = display.replace('ldec', 'log₁₄')

        display = display.replace('ln', 'logₑ')
        display = display.replace('sqrt', '√')
        display = display.replace('cbrt', '∛')

        decimal_display = decimal_display.replace('lbin', 'log₂')
        decimal_display = decimal_display.replace('ln', 'logₑ')
        decimal_display = decimal_display.replace('lsez', 'log₆')
        decimal_display = decimal_display.replace('ldec', 'log₁₀')
        decimal_display = decimal_display.replace('sqrt', '√')
        decimal_display = decimal_display.replace('cbrt', '∛')

        self._prepared_expression = prepared_expression
        self._display = display
        self._decimal_display = decimal_display
        self._niftimal_display = niftimal_display

        sezimal_expression = sezimal_expression.replace('**', '^')
        decimal_expression = decimal_expression.replace('**', '^')
        sezimal_expression = sezimal_expression.replace('* *', '^')
        decimal_expression = decimal_expression.replace('* *', '^')

        self._sezimal_expression = sezimal_expression
        self._decimal_expression = decimal_expression

        if self.decimal:
            self._expression = self._decimal_expression
        else:
            self._expression = self._sezimal_expression

    def eval_expression(self):
        if not self.expression:
            return

        if self.debug:
            #
            # Take care of the mod to % operator change
            #
            sezimal_context.use_ultra_precision()
            response = eval(self._prepared_expression.replace('mod', '%'))
            sezimal_context.back_to_regular_precision()

            if self.decimal:
                if type(response) == Sezimal:
                    response = round(round(response, self._sezimal_precision).decimal, int(self._decimal_precision))
                elif type(response) == Decimal:
                    response = round(response, int(self._decimal_precision))

                self.expression = self._format_decimal(response)
            else:
                if type(response) != SezimalFraction:
                    response = round(response, self._sezimal_precision)
                self.expression = self._format_sezimal(response)

        else:
            try:
                response = eval(self._prepared_expression)

                if self.decimal:
                    if type(response) != DecimalFraction:
                        response = round(response, int(self._decimal_precision))
                    self.expression = self._format_decimal(response)
                else:
                    if type(response) != SezimalFraction:
                        response = round(response, self._sezimal_precision)
                    self.expression = self._format_sezimal(response)

            except:
                self._set_error()

    def _set_error(self):
        self.expression = ''
        self.error = True

        if self.locale:
            self._display = self.locale.upper(self.locale.ERROR)
            self._decimal_display = self.locale.upper(self.locale.ERROR)
            self._niftimal_display = self.locale.upper(self.locale.ERROR)
        else:
            self._display = 'ERROR'
            self._decimal_display = 'ERROR'
            self._niftimal_display = 'ERROR'

    def ln(self, number):
        return number.ln()


    def lsez(self, number):
        if type(number) == Decimal:
            return number.ln() / Decimal(6).ln()

        return number.log()


    def ldec(self, number):
        if type(number) == Decimal:
            return number.log()

        return number.log14()


    def sqrt(self, number):
        return number.sqrt()


    def cbrt(self, number):
        if type(number) == Decimal:
            return number ** Decimal(validate_clean_decimal('0..3'))

        return number.cbrt()

    #
    # Trigonometric functions,
    # dealing with different angle units
    #
    def SIN(self, number):
        if self.decimal:
            res = sin(number, self.decimal_angle)
        else:
            res = sin(number, self.angle)
        return res


    def arcsin(self, number):
        if self.decimal:
            res = arcsin(number, self.decimal_angle)
        else:
            res = arcsin(number, self.angle)
        return res


    def asin(self, number):
        if self.decimal:
            res = asin(number, self.decimal_angle)
        else:
            res = asin(number, self.angle)
        return res


    def CSC(self, number):
        if self.decimal:
            res = csc(number, self.decimal_angle)
        else:
            res = csc(number, self.angle)
        return res


    def arccsc(self, number):
        if self.decimal:
            res = arccsc(number, self.decimal_angle)
        else:
            res = arccsc(number, self.angle)
        return res


    def acsc(self, number):
        if self.decimal:
            res = acsc(number, self.decimal_angle)
        else:
            res = acsc(number, self.angle)
        return res


    def COS(self, number):
        if self.decimal:
            res = cos(number, self.decimal_angle)
        else:
            res = cos(number, self.angle)
        return res


    def arccos(self, number):
        if self.decimal:
            res = arccos(number, self.decimal_angle)
        else:
            res = arccos(number, self.angle)
        return res


    def acos(self, number):
        if self.decimal:
            res = acos(number, self.decimal_angle)
        else:
            res = acos(number, self.angle)
        return res


    def SEC(self, number):
        if self.decimal:
            res = sec(number, self.decimal_angle)
        else:
            res = sec(number, self.angle)
        return res


    def arcsec(self, number):
        if self.decimal:
            res = arcsec(number, self.decimal_angle)
        else:
            res = arcsec(number, self.angle)
        return res


    def asec(self, number):
        if self.decimal:
            res = asec(number, self.decimal_angle)
        else:
            res = asec(number, self.angle)
        return res


    def TAN(self, number):
        if self.decimal:
            res = tan(number, self.decimal_angle)
        else:
            res = tan(number, self.angle)
        return res


    def arctan(self, number):
        if self.decimal:
            res = arctan(number, self.decimal_angle)
        else:
            res = arctan(number, self.angle)
        return res


    def atan(self, number):
        if self.decimal:
            res = atan(number, self.decimal_angle)
        else:
            res = atan(number, self.angle)
        return res


    def COT(self, number):
        if self.decimal:
            res = cot(number, self.decimal_angle)
        else:
            res = cot(number, self.angle)
        return res


    def arccot(self, number):
        if self.decimal:
            res = arccot(number, self.decimal_angle)
        else:
            res = arccot(number, self.angle)
        return res


    def acot(self, number):
        if self.decimal:
            res = acot(number, self.decimal_angle)
        else:
            res = acot(number, self.angle)
        return res


    def SINH(self, number):
        if self.decimal:
            res = sinh(number, self.decimal_angle)
        else:
            res = sinh(number, self.angle)
        return res


    def arcsinh(self, number):
        if self.decimal:
            res = arcsinh(number, self.decimal_angle)
        else:
            res = arcsinh(number, self.angle)
        return res


    def asinh(self, number):
        if self.decimal:
            res = asinh(number, self.decimal_angle)
        else:
            res = asinh(number, self.angle)
        return res


    def CSCH(self, number):
        if self.decimal:
            res = csch(number, self.decimal_angle)
        else:
            res = csch(number, self.angle)
        return res


    def arccsch(self, number):
        if self.decimal:
            res = arccsch(number, self.decimal_angle)
        else:
            res = arccsch(number, self.angle)
        return res


    def acsch(self, number):
        if self.decimal:
            res = acsch(number, self.decimal_angle)
        else:
            res = acsch(number, self.angle)
        return res


    def COSH(self, number):
        if self.decimal:
            res = cosh(number, self.decimal_angle)
        else:
            res = cosh(number, self.angle)
        return res


    def arccosh(self, number):
        if self.decimal:
            res = arccosh(number, self.decimal_angle)
        else:
            res = arccosh(number, self.angle)
        return res


    def acosh(self, number):
        if self.decimal:
            res = acosh(number, self.decimal_angle)
        else:
            res = acosh(number, self.angle)
        return res


    def SECH(self, number):
        if self.decimal:
            res = sech(number, self.decimal_angle)
        else:
            res = sech(number, self.angle)
        return res


    def arcsech(self, number):
        if self.decimal:
            res = arcsech(number, self.decimal_angle)
        else:
            res = arcsech(number, self.angle)
        return res


    def asech(self, number):
        if self.decimal:
            res = asech(number, self.decimal_angle)
        else:
            res = asech(number, self.angle)
        return res


    def TANH(self, number):
        if self.decimal:
            res = tanh(number, self.decimal_angle)
        else:
            res = tanh(number, self.angle)
        return res


    def arctanh(self, number):
        if self.decimal:
            res = arctanh(number, self.decimal_angle)
        else:
            res = arctanh(number, self.angle)
        return res


    def atanh(self, number):
        if self.decimal:
            res = atanh(number, self.decimal_angle)
        else:
            res = atanh(number, self.angle)
        return res


    def COTH(self, number):
        if self.decimal:
            res = coth(number, self.decimal_angle)
        else:
            res = coth(number, self.angle)
        return res


    def arccoth(self, number):
        if self.decimal:
            res = arccoth(number, self.decimal_angle)
        else:
            res = arccoth(number, self.angle)
        return res


    def acoth(self, number):
        if self.decimal:
            res = acoth(number, self.decimal_angle)
        else:
            res = acoth(number, self.angle)
        return res
