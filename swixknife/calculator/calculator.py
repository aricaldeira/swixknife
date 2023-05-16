

__all__ = ('SezimalCalculator',)

from ..sezimal import Sezimal, SezimalInteger
from decimal import Decimal
from ..units.conversions import  *
from ..base import decimal_format, sezimal_format, SEPARATOR_DOT, SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


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
    '__PERSIXNIF__': "/Sezimal('1000')",
    '__PERUNEXIAN__': "/Sezimal('1_0000')",
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
    '__PERSIXNIF__': '‰',
    '__PERUNEXIAN__': '‱',
    '__SQUARE__': "²",
    '__CUBE__': "³",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
}

_LOCALES_COMMA_SEPARATOR = [
    'az-AZ',
    'be-BY',
    'bg-BG',
    'bs-BA',
    'ca-ES',
    'crh-UA',
    'cs-CZ',
    'da-DK',
    'de-DE',
    'el-CY',
    'el-GR',
    'en-DK',
    'eo',
    'es-AR',
    'es-CR',
    'es-CU',
    'es-ES',
    'et-EE',
    'eu-ES',
    'ff-SN',
    'fi-FI',
    'fr-BE',
    'fr-FR',
    'fr-LU',
    'gl-ES',
    'hr-HR',
    'ht-HT',
    'hu-HU',
    'id-ID',
    'is-IS',
    'it-IT',
    'ka-GE',
    'kab-DZ',
    'kk-KZ',
    'ky-KG',
    'ln-CD',
    'lt-LT',
    'lv-LV',
    'mg-MG',
    'mk-MK',
    'mn-MN',
    'nb-NO',
    'nl-NL',
    'pap-AW',
    'pap-CW',
    'pl-PL',
    'pt-BR',
    'pt-PT',
    'pt-AO',
    'ro-RO',
    'ru-RU',
    'ru-UA',
    'rw-RW',
    'se-NO',
    'sk-SK',
    'sl-SI',
    'sq-AL',
    'sr-RS',
    'sv-SE',
    'tg-TJ',
    'tr-TR',
    'tt-RU',
    'uk-UA',
    'vi-VN',
    'wo-SN'
]

_LOCALES_SPACE_GROUP_SEPARATOR = [
    'cs-CZ',
    'de-CH',
    'eo',
    'es-CR',
    'es-MX',
    'et-EE',
    'fi-FI',
    'fr-FR',
    'fr-LU',
    'ht-HT',
    'kk-KZ',
    'ky-KG',
    'lv-LV',
    'mfe-MU',
    'mk-MK',
    'nb-NO',
    'pl-PL',
    'ps-AF',
    'ru-RU',
    'sk-SK',
    'sv-SE',
    'uk-UA',
    'unm-US',
]


class SezimalCalculator:
    def __init__(self, expression: str = '', lang: str = ''):
        self.expression = expression
        self.dedicated_digits = False
        self.sezimal_separator = SEPARATOR_DOT
        self.group_separator = SEPARATOR_COMMA
        self.fraction_group_separator = SEPARATOR_NARROW_NOBREAK_SPACE
        self.decimal = False
        self.precision = 4
        self.lang = lang

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, text: str):
        self._expression = text
        self._prepare_expression()

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
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang: str = ''):
        if not lang:
            self._lang = lang
            return

        #
        # Locales that use comma as the sezimal separador
        #
        if lang in _LOCALES_COMMA_SEPARATOR or lang.replace('_', '-') in _LOCALES_COMMA_SEPARATOR:
            self.sezimal_separator = SEPARATOR_COMMA
            self.group_separator = SEPARATOR_DOT

        if lang in _LOCALES_SPACE_GROUP_SEPARATOR or lang.replace('_', '-') in _LOCALES_SPACE_GROUP_SEPARATOR:
            self.group_separator = SEPARATOR_NARROW_NOBREAK_SPACE

    @property
    def display(self):
        return self._display

    @property
    def decimal_display(self):
        return self._decimal_display

    def calculate(self):
        final_exp, nice_exp, decimal_exp, sezimal_response, sezimal_formatted_response, decimal_response, decimal_formatted_response = calculator(self._expression)

        self.expression = str(sezimal_response)

    def _format_sezimal(self, number, precision=None):
        if precision is None:
            precision = self._sezimal_precision

        params = {
            'sezimal_places': precision,
            'sezimal_separator': self.sezimal_separator,
            'group_separator': self.group_separator,
            'fraction_group_separator': self.fraction_group_separator,
            'typographical_negative': True,
            'dedicated_digits': self.dedicated_digits,
        }

        return sezimal_format(number, **params)

    def _format_decimal(self, number, precision=None):
        if precision is None:
            precision = self._decimal_precision

        params = {
            'decimal_places': precision,
            'decimal_separator': self.sezimal_separator,
            'group_separator': self.group_separator,
            'fraction_group_separator': self.fraction_group_separator,
            'typographical_negative': True,
        }

        return decimal_format(number.quantize(Decimal(f'1e-{int(precision)}')), **params)

    def _prepare_expression(self):
        if not self.expression:
            self._display = ''
            self._decimal_display = ''
            self._prepared_expression = ''
            return

        exp = self.expression

        #
        # Replace operators first
        #
        for o in _OPERATOR:
            text = _OPERATOR[o]
            exp = exp.replace(o, text)

        parts = exp.split()

        parenthesis_opened = 0

        prepared_expression = ''
        display = ''
        decimal_display = ''

        for p in parts:
            p = p.strip()

            if not p:
                continue

            if p in _OPERATION:
                prepared_expression += _OPERATION[p]
                display += _NICE_OPERATION[p]
                decimal_display += _NICE_OPERATION[p]
                decimal_display = decimal_display.replace('%', ' ÷ 36')
                decimal_display = decimal_display.replace('‰', ' ÷ 216')
                decimal_display = decimal_display.replace('‱', ' ÷ 1296')

                if (not parenthesis_opened) and p == '__LEFT_PARENTHESIS__':
                    parenthesis_opened += 1
                elif parenthesis_opened and p == '__RIGHT_PARENTHESIS__':
                    parenthesis_opened -= 1

                continue

            if p == '.':
                continue

            n = eval(f"'{p}'")

            if type(n) != Sezimal:
                if self.decimal:
                    n = Sezimal(Decimal(p).quantize(Decimal(f'1e-{int(self._decimal_precision)}')))
                else:
                    n = Sezimal(p)

            # n = round(n, sezimal_precision)

            prepared_expression += f"Sezimal('{n}')"
            display += self._format_sezimal(n, SezimalInteger(Decimal(str(n._precision))))
            decimal_display += self._format_decimal(n.decimal)

        if exp[-1] == '.':
            display += self.sezimal_separator

        for i in range(parenthesis_opened):
            prepared_expression += ')'
            # display += ')'
            # decimal_display += ')'

        self._prepared_expression = prepared_expression
        self._display = display
        self._decimal_display = decimal_display

    def eval_expression(self):
        if not self.expression:
            return

        sezimal_response = eval(self._prepared_expression)
        self.expression = str(round(sezimal_response, self._sezimal_precision))
