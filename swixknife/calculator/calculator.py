

__all__ = ('SezimalCalculator',)

from decimal import Decimal
from fractions import Fraction as DecimalFraction

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..constants import E, PI, TAU, GOLDEN_RATIO
from ..base import default_to_sezimal_digits, decimal_to_sezimal, \
    validate_clean_sezimal, validate_clean_decimal, \
    sezimal_format, decimal_format, \
    RECURRING_DIGITS_NOTATION_NONE, \
    RECURRING_DIGITS_NOTATION_SIMPLE
from ..exponents import sezimal_exponent_to_decimal_exponent, decimal_exponent_to_sezimal_exponent
from ..units import sezimal_to_decimal_unit, decimal_to_sezimal_unit
from ..text import sezimal_spellout

from ..localization import SezimalLocale, sezimal_locale

_PERARDA = '‰'
_PERSIXARDA = '‱'

_OPERATOR = {
    #
    # Operators
    #
    '+': ' __ADD__ ',
    '−': ' __SUBTRACT__ ',
    '-': ' __SUBTRACT__ ',
    '÷': ' __DIVIDE__ ',
    '/': ' __DIVIDE__ ',
    '^': ' __POWER__ ',
    '**': ' __POWER__ ',
    '×': ' __MULTIPLY__ ',
    '*': ' __MULTIPLY__ ',
    '%': ' __PERNIF__ ',
    '‰': ' __PERARDA__ ',
    '‱': ' __PERSIXARDA__ ',
    '²': ' __SQUARE__ ',
    '³': ' __CUBE__ ',
    '±': ' __PLUS_MINUS__ ',

    #
    # Constants and “punctuation”
    #
    'ln': ' __NATURAL_LOGARITHM__ ',
    '(': ' __LEFT_PARENTHESIS__ ',
    ')': ' __RIGHT_PARENTHESIS__ ',
    '|o': '__MOD_OPEN__',
    'c|': '__MOD_CLOSE__',
}

_OPERATION = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__PERNIF__': "/Sezimal('100')",
    '__PERARDA__': "/Sezimal('1_000')",
    '__PERSIXARDA__': "/Sezimal('10_000')",
    '__SQUARE__': "**Sezimal('2')",
    '__CUBE__': "**Sezimal('3')",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__MOD__': '|',
}

_OPERATION_DECIMAL  = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__PERNIF__': "/Sezimal('244')",
    '__PERARDA__': "/Sezimal('4_344')",
    '__PERSIXARDA__': "/Sezimal('114_144')",
    '__SQUARE__': "**Sezimal('2')",
    '__CUBE__': "**Sezimal('3')",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__MOD__': '|',
}

_NICE_OPERATION = {
    '__ADD__': ' + ',
    '__SUBTRACT__': ' − ',
    '__DIVIDE__': ' ÷ ',
    '__MULTIPLY__': ' × ',
    '__POWER__': ' ^ ',
    '__PERNIF__': '%',
    '__PERARDA__': '‰',
    '__PERSIXARDA__': '‱',
    '__SQUARE__': "²",
    '__CUBE__': "³",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
}

e = E
π = PI
τ = TAU
φ = GOLDEN_RATIO


class SezimalCalculator:
    def __init__(self, expression: str = '0', locale: str | SezimalLocale = None):
        self.sezimal_digits = False
        self.decimal = False
        self.precision = 3
        self.locale = locale
        self.grouping_digits = 3
        self.suffix = ''
        self.decimal_suffix = ''
        self.factor = Sezimal(1)
        self.unit = ''
        self.decimal_unit = ''
        self.debug = False
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
            return default_to_sezimal_digits(self._display)
        else:
            return self._display

    @property
    def decimal_display(self):
        return self._decimal_display

    @property
    def spellout(self):
        if self.locale:
            lang = self.locale.LANG
        else:
            lang = 'en'

        if lang == 'en' and self.grouping_digits == 4:
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
                print(f'SH-{self.unit} {part}', lang)
                spellout += sezimal_spellout(f'SH-{self.unit} {part}', lang) + ' '
            elif self.unit and part.replace('/', '').replace('⁄', '').isdigit():
                print(f'SH-{self.unit} {part}', lang)
                spellout += sezimal_spellout(f'SH-{self.unit} {part}', lang) + ' '
            else:
                spellout += sezimal_spellout(part, lang) + ' '

        return spellout.strip()

    def _determine_precision(self, number: str, max_precision: SezimalInteger, result: bool = False) -> SezimalInteger:
        number = str(number)

        if '.' in number and number[-1] != '.':
            precision = SezimalInteger(Decimal(len(number.split('.')[1])))

            if result:
                while number and number.endswith('0'):
                    precision -= 1
                    number = number[:-1]

        else:
            precision = SezimalInteger(0)

        return min(precision, max_precision)

    def _format_sezimal(self, number, display: bool = False, result: bool = False, part: str = '', keep_original_aspect=True):
        if part and type(part) == str and '⁄' in part:
            numerator, denominator = part.split('⁄')

            numerator = self._format_sezimal(numerator, display, result, numerator, keep_original_aspect)

            if denominator:
                denominator = self._format_sezimal(denominator, display, result, denominator, keep_original_aspect)
                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif not part and type(number) == SezimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = self._format_sezimal(numerator, display, result, numerator, keep_original_aspect)
            denominator = self._format_sezimal(denominator, display, result, numerator, keep_original_aspect)
            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._sezimal_precision, result)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'sezimal_places': precision,
            'sezimal_digits': self.sezimal_digits,
            'recurring_digits_notation': recurring_digits_notation,
            'keep_original_aspect': keep_original_aspect and not result,
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
            params['typographical_negative'] = False

        if not keep_original_aspect:
            if not recurring_digits_notation:
                number = round(number, precision)

        if display:
            return self.locale.format_number(number, **params)

        return sezimal_format(number, **params)

    def _format_decimal(self, number, display: bool = False, result: bool = False, part: str = '', keep_original_aspect: bool = True):
        if part and type(part) == str and '⁄' in part:
            numerator, denominator = part.split('⁄')

            numerator = self._format_decimal(numerator, display, result, numerator, keep_original_aspect)

            if denominator:
                denominator = self._format_decimal(denominator, display, result, denominator, keep_original_aspect)
                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif not part and type(number) == DecimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = Decimal(numerator)
            denominator = Decimal(denominator)
            numerator = self._format_decimal(numerator, display, result, numerator, keep_original_aspect)
            denominator = self._format_decimal(denominator, display, result, numerator, keep_original_aspect)
            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._decimal_precision, result)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'decimal_places': precision,
            'recurring_digits_notation': recurring_digits_notation,
            'keep_original_aspect': keep_original_aspect and not result,
            'lakh_crore_grouping': self.locale and (self.locale.LANG in ('hi', 'ur', 'mr', 'bn', 'or', 'ta', 'te', 'kn', 'ml') or 'Indian ' in self.locale.LANGUAGE),
            'wan_man_van_grouping': self.locale and self.locale.LANG in ('zh', 'ja', 'ko', 'vi'),
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

    def _apply_sezimal_or_recurring_mark(self, display: str, separator: str, suffix: str) -> str:
        if suffix in ('%', '‰', '‱', '󱹷', '󱹸', '󱹹', '󱹺', '󱹻', '󱹼', '󱹽', '󱹾', '󱹿', '󱺀', '󱺁', '󱺂', '󱺃', '󱺄', '󱺅', '󱺆', '󱺇'):
            display = display[0:len(suffix) * -1]
        elif suffix:
            display = display[0:(len(suffix) + 1) * -1]

        display += separator

        if suffix in ('%', '‰', '‱', '󱹷', '󱹸', '󱹹', '󱹺', '󱹻', '󱹼', '󱹽', '󱹾', '󱹿', '󱺀', '󱺁', '󱺂', '󱺃', '󱺄', '󱺅', '󱺆', '󱺇'):
            display += suffix
        elif suffix:
            display += ' ' + suffix

        return display

    def _prepare_expression(self):
        if not self.expression:
            self._display = ''
            self._decimal_display = ''
            self._prepared_expression = ''
            self._sezimal_expression = ''
            self._decimal_expression = ''
            return

        exp = self.expression

        #
        # Replace operators first
        #
        for o in _OPERATOR:
            text = _OPERATOR[o]
            exp = exp.replace(o, text)

        parenthesis_opened = 0

        prepared_expression = ''
        display = ''
        decimal_display = ''
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

            if part in _OPERATION:
                if self.decimal:
                    prepared_expression += _OPERATION_DECIMAL[part]
                    sezimal_expression += f' {_OPERATION_DECIMAL[part]} '
                    decimal_expression += f' {_OPERATION_DECIMAL[part]} '
                else:
                    prepared_expression += _OPERATION[part]
                    sezimal_expression +=  f' {_OPERATION[part]} '
                    decimal_expression += f' {_OPERATION[part]} '

                #
                # Deals with negative numbers
                #
                if part == '__SUBTRACT__':
                    if previous_part == '':
                        display += ' −'
                        decimal_display += ' −'

                    elif previous_part in _OPERATION:
                        if previous_part in (' __PERNIF__ ', ' __PERARDA__ ', ' __PERSIXARDA__ '):
                            display += _NICE_OPERATION[part]
                            decimal_display += _NICE_OPERATION[part]
                        else:
                            display += ' −'
                            decimal_display += ' −'

                    else:
                        display += _NICE_OPERATION[part]
                        decimal_display += _NICE_OPERATION[part]

                else:
                    display += _NICE_OPERATION[part]
                    decimal_display += _NICE_OPERATION[part]

                previous_part = part

                if self.decimal:
                    display = display.replace('%', ' ÷ 244')
                    display = display.replace('‰', f' ÷ 4{self.locale.GROUP_SEPARATOR}344')
                    display = display.replace('‱', f' ÷ 114{self.locale.GROUP_SEPARATOR}144')

                    exp = exp.replace('%', ' / 100')
                    exp = exp.replace('‰', ' / 1_000')
                    exp = exp.replace('‱', ' / 10_000')

                else:
                    decimal_display = decimal_display.replace('%', ' ÷ 36')
                    decimal_display = decimal_display.replace('‰', ' ÷ 216')
                    decimal_display = decimal_display.replace('‱', f' ÷ 1{self.locale.GROUP_SEPARATOR}296')

                    decimal_expression = decimal_expression.replace('%', ' / 36')
                    decimal_expression = decimal_expression.replace('‰', ' / 216')
                    decimal_expression = decimal_expression.replace('‱', ' / 1_296')

                if (not parenthesis_opened) and part == '__LEFT_PARENTHESIS__':
                    parenthesis_opened += 1
                elif parenthesis_opened and part == '__RIGHT_PARENTHESIS__':
                    parenthesis_opened -= 1

                continue

            if part == '.':
                continue

            previous_part = part

            if part in ('e', 'π', 'τ', 'φ'):
                prepared_expression += part
                display += part
                decimal_display += part
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
                else:
                    number = Decimal(validate_clean_decimal(part))
                    prepared_expression += f"Decimal('{number}')"

                decimal_display += self._format_decimal(part, display=True, part=part)
                decimal_expression += self._format_decimal(part, part=part)

                if self.unit and self.decimal_unit:
                    number = decimal_to_sezimal_unit(number, self.decimal_unit, self.unit)
                    number = round(number, self._sezimal_precision)
                elif self.factor:
                    number *= self.factor
                    number = round(number, self._sezimal_precision)
                else:
                    number = Sezimal(number)

                display += self._format_sezimal(number, display=True)
                sezimal_expression += self._format_sezimal(number)

            else:
                if '⁄' in part:
                    if part.endswith('⁄'):
                        number = Sezimal(part[:-1])
                        prepared_expression += f"Sezimal('{number}')"
                    else:
                        number = SezimalFraction(part)
                        prepared_expression += f"SezimalFraction('{number}')"
                elif part.endswith('..'):
                    number = Sezimal(part[:-2])
                    prepared_expression += f"Sezimal('{number}')"
                elif part.endswith('.'):
                    number = Sezimal(part[:-1])
                    prepared_expression += f"Sezimal('{number}')"
                else:
                    number = Sezimal(part)
                    prepared_expression += f"Sezimal('{number}')"

                display += self._format_sezimal(part, display=True, part=part)
                sezimal_expression += self._format_sezimal(part, part=part)

                if self.unit and self.decimal_unit:
                    number = sezimal_to_decimal_unit(number, self.unit, self.decimal_unit)
                    number = round(number.decimal, int(self._decimal_precision))
                elif self.factor:
                    number /= self.factor
                    number = round(number.decimal, int(self._decimal_precision))
                else:
                    number = number.decimal

                decimal_display += self._format_decimal(number, display=True)
                decimal_expression += self._format_decimal(number)

        for i in range(parenthesis_opened):
            prepared_expression += ')'

        self._prepared_expression = prepared_expression
        self._display = display
        self._decimal_display = decimal_display

        sezimal_expression = sezimal_expression.replace('**', '^')
        decimal_expression = decimal_expression.replace('**', '^')
        sezimal_expression = sezimal_expression.replace('* *', '^')
        decimal_expression = decimal_expression.replace('* *', '^')

        if self.decimal:
            sezimal_expression = sezimal_expression.replace(" /Sezimal('244')", ' / 244')
            sezimal_expression = sezimal_expression.replace(" /Sezimal('4_344')", ' / 4_344')
            sezimal_expression = sezimal_expression.replace(" /Sezimal('114_144')", ' / 114_144')

            decimal_expression = decimal_expression.replace(" /Sezimal('244')", '%')
            decimal_expression = decimal_expression.replace(" /Sezimal('4_344')", '‰')
            decimal_expression = decimal_expression.replace(" /Sezimal('114_144')", '‱')

        else:
            sezimal_expression = sezimal_expression.replace(" /Sezimal('100')", '%')
            sezimal_expression = sezimal_expression.replace(" /Sezimal('1_000')", '‰')
            sezimal_expression = sezimal_expression.replace(" /Sezimal('10_000')", '‱')

            decimal_expression = decimal_expression.replace(" /Sezimal('100')", ' / 36')
            decimal_expression = decimal_expression.replace(" /Sezimal('1_000')", ' / 216')
            decimal_expression = decimal_expression.replace(" /Sezimal('10_000')", ' / 1_296')

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
            response = eval(self._prepared_expression)

            if self.decimal:
                if type(response) != DecimalFraction:
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
            self._display = self.locale.ERROR.upper()
            self._decimal_display = self.locale.ERROR.upper()
        else:
            self._display = 'ERROR'
            self._decimal_display = 'ERROR'
