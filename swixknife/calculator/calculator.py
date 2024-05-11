

__all__ = ('SezimalCalculator',)

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..constants import E, PI, TAU, GOLDEN_RATIO
from ..base import default_to_sezimal_digits, decimal_to_sezimal, \
    validate_clean_sezimal, validate_clean_decimal, \
    sezimal_format, decimal_format, \
    RECURRING_DIGITS_NOTATION_NONE, \
    RECURRING_DIGITS_NOTATION_SIMPLE

from ..localization import SezimalLocale, sezimal_locale

_PERSIXNIFF = '‰'
_PERUNEXIAN = '‱'

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
    '‰': ' __PERSIXNIF__ ',
    '‱': ' __PERUNEXIAN__ ',
    '²': ' __SQUARE__ ',
    '³': ' __CUBE__ ',
    '±': ' __PLUS_MINUS__ ',

    #
    # Constants and “punctuation”
    #
    'e': ' __CONSTANT_E__ ',
    'ln': ' __NATURAL_LOGARITHM__ ',
    '(': ' __LEFT_PARENTHESIS__ ',
    ')': ' __RIGHT_PARENTHESIS__ ',
    '|o': '__MOD_OPEN__',
    'c|': '__MOD_CLOSE__',
    'π': '__CONSTANT_PI__',
    'τ': '__CONSTANT_TAU__',
    'φ': '__CONSTANT_GOLDEN_RATIO__',
}

_OPERATION = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__PERNIF__': "/Sezimal('100')",
    '__PERSIXNIF__': "/Sezimal('1_000')",
    '__PERUNEXIAN__': "/Sezimal('10_000')",
    '__SQUARE__': "**Sezimal('2')",
    '__CUBE__': "**Sezimal('3')",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__MOD__': '|',
    '__CONSTANT_PI__': 'PI',
    '__CONSTANT_TAU__': 'TAU',
    '__CONSTANT_GOLDEN_RATIO__': 'GOLDEN_RATIO',
}

_OPERATION_DECIMAL  = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__PERNIF__': "/Sezimal('244')",
    '__PERSIXNIF__': "/Sezimal('4_344')",
    '__PERUNEXIAN__': "/Sezimal('114_144')",
    '__SQUARE__': "**Sezimal('2')",
    '__CUBE__': "**Sezimal('3')",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__MOD__': '|',
    '__CONSTANT_PI__': 'PI.decimal',
    '__CONSTANT_TAU__': 'TAU.decimal',
    '__CONSTANT_GOLDEN_RATIO__': 'GOLDEN_RATIO.decimal',
}

_NICE_OPERATION = {
    '__ADD__': ' + ',
    '__SUBTRACT__': ' − ',
    '__DIVIDE__': ' ÷ ',
    '__MULTIPLY__': ' × ',
    '__POWER__': ' ^ ',
    '__PERNIF__': '%',
    '__PERSIXNIF__': '‰',
    '__PERUNEXIAN__': '‱',
    '__SQUARE__': "²",
    '__CUBE__': "³",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__CONSTANT_PI__': ' π ',
    '__CONSTANT_TAU__': ' τ ',
    '__CONSTANT_GOLDEN_RATIO__': ' φ ',
}


class SezimalCalculator:
    def __init__(self, expression: str = '0', locale: str | SezimalLocale = None):
        self.sezimal_digits = False
        self.decimal = False
        self.p_notation = True
        self.precision = 3
        self.locale = locale
        self.expression = expression

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, text: str):
        self._expression = text
        self._prepare_expression()

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
            self._sezimal_precision = round(self._decimal_precision / 3 * 4, 0)

        else:
            self._sezimal_precision = precision
            self._decimal_precision = round(self._sezimal_precision / 4 * 3, 0)

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

    def _format_sezimal(self, number, precision: int = None, display: bool = False):
        params = {
            'sezimal_places': 0,
            'sezimal_digits': self.sezimal_digits,
            'recurring_digits_notation': 'p',
        }

        if not display:
            params['sezimal_separator'] = '.'
            params['group_separator'] = '_'
            params['fraction_group_separator'] = '_'
            params['sezimal_digits'] = False
            params['typographical_negative'] = False
            p_notation = sezimal_format(number, **params)

        else:
            params['use_fraction_group_separator'] = True
            p_notation = self.locale.format_number(number, **params)

        if 'p' in p_notation:
            if self.p_notation:
                if not p_notation.endswith('5p'):
                    return p_notation

                if display:
                    number = round(number, len(p_notation.split(self.locale.SEZIMAL_SEPARATOR)[1]) - 2)
                else:
                    number = round(number, len(p_notation.split('.')[1]) - 2)

            else:
                precision = None

        if (precision is None) or (precision == -1):
            number_precision = validate_clean_sezimal(str(number))

            if '.' not in number_precision:
                number_precision = 0
            else:
                number_precision = number_precision.split('.')[1]

                # if number_precision.replace('0', '') == '':
                #     number_precision = 0
                # else:
                number_precision = len(number_precision)

            if precision is None:
                precision = min(number_precision, int(self._sezimal_precision))
            else:
                precision = number_precision

        else:
            precision = Decimal(precision)

        params['sezimal_places'] = Decimal(precision)
        params['recurring_digits_notation'] = RECURRING_DIGITS_NOTATION_NONE

        if not display:
            return sezimal_format(
                round(number, params['sezimal_places']),
                **params
            )
        else:
            return self.locale.format_number(
                round(number, params['sezimal_places']),
                **params
            )

    def _format_decimal(self, number, precision: int = None, display: bool = False):
        params = {
            'decimal_places': 0,
            'recurring_digits_notation': RECURRING_DIGITS_NOTATION_NONE,
        }

        if not display:
            params['decimal_separator'] = '.'
            params['group_separator'] = '_'
            params['fraction_group_separator'] = '_'
            params['typographical_negative'] = False
            params['recurring_digits_notation'] = RECURRING_DIGITS_NOTATION_SIMPLE
            p_notation = decimal_format(number, **params)

        else:
            params['use_fraction_group_separator'] = True
            p_notation = self.locale.format_decimal_number(number, **params)

        if 'p' in p_notation:
            if self.p_notation:
                if not p_notation.endswith('9p'):
                    return p_notation

                if display:
                    number = round(number, len(p_notation.split(self.locale.SEZIMAL_SEPARATOR)[1]) - 2)
                else:
                    number = round(number, len(p_notation.split('.')[1]) - 2)

            else:
                precision = None

        if precision is None or precision == -1:
            number_precision = validate_clean_decimal(str(number))

            if '.' not in number_precision:
                number_precision = 0
            else:
                number_precision = number_precision.split('.')[1]

                # if number_precision.replace('0', '') == '':
                #     number_precision = 0
                # else:
                number_precision = len(number_precision)

            if precision is None:
                precision = min(number_precision, int(self._decimal_precision))
            else:
                precision = number_precision

        else:
            precision = Decimal(precision)

        params['decimal_places'] = precision
        params['recurring_digits_notation'] = RECURRING_DIGITS_NOTATION_NONE

        number = number.quantize(Decimal(f'1e{int(precision)}'))

        if not display:
            return decimal_format(
                number,
                **params
            )
        return self.locale.format_decimal_number(
                number,
                **params
            )

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
                        if previous_part in (' __PERNIF__ ', ' __PERSIXNIF__ ', ' __PERUNEXIAN__ '):
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

            number = eval(f"'{part}'")

            if self.decimal:
                number = Decimal(validate_clean_decimal(part))
                prepared_expression += f"Decimal('{number}')"

                display += self._format_sezimal(Sezimal(number), -1, display=True)
                decimal_display += self._format_decimal(number, -1, display=True)

                sezimal_expression += self._format_sezimal(Sezimal(number), -1)
                decimal_expression += self._format_decimal(number, -1)

            else:
                number = Sezimal(part)
                prepared_expression += f"Sezimal('{part}')"

                display += self._format_sezimal(number, -1, display=True)
                decimal_display += self._format_decimal(number.decimal, -1, display=True)

                sezimal_expression += self._format_sezimal(number, -1)
                decimal_expression += self._format_decimal(number.decimal, -1)

        if previous_part.endswith('.'):
            if self.decimal:
                decimal_display += self.locale.SEZIMAL_SEPARATOR
                decimal_expression += '.'
            else:
                display += self.locale.SEZIMAL_SEPARATOR
                sezimal_expression += '.'

        for i in range(parenthesis_opened):
            prepared_expression += ')'

        self._prepared_expression = prepared_expression
        self._display = display
        self._decimal_display = decimal_display

        sezimal_expression = sezimal_expression.replace('**', '^')
        decimal_expression = decimal_expression.replace('**', '^')

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

        if exp.endswith('_'):
            if self.decimal:
                self._decimal_display += '_'
                self._decimal_expression += '_'
            else:
                self._display += '_'
                self._sezimal_expression += '_'

        if self.decimal:
            self._expression = self._decimal_expression
        else:
            self._expression = self._sezimal_expression

    def eval_expression(self):
        if not self.expression:
            return

        try:
            response = eval(self._prepared_expression)

            if self.decimal:
                self.expression = self._format_decimal(response)
                self._sezimal_expression = self._format_sezimal(Sezimal(response))
                self._decimal_expression = self._format_decimal(response)

                self._display = self._format_sezimal(Sezimal(response), display=True)
                self._decimal_display = self._format_decimal(response, display=True)
            else:
                self.expression = self._format_sezimal(response)
                self._sezimal_expression = self._format_sezimal(response)
                self._decimal_expression = self._format_decimal(response.decimal)

                self._display = self._format_sezimal(response, display=True)
                self._decimal_display = self._format_decimal(response.decimal, display=True)

        except:
            self.expression = ''
            self._display = 'ERROR'
            self._decimal_display = 'ERROR'
