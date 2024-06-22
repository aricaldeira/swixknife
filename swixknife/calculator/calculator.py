

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
from ..base.digit_conversion import PER_SYMBOLS
from ..exponents import sezimal_exponent_to_decimal_exponent, decimal_exponent_to_sezimal_exponent
from ..units import sezimal_to_decimal_unit, decimal_to_sezimal_unit
from ..text import sezimal_spellout

from ..localization import SezimalLocale, sezimal_locale


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
    '%': ' __PERCENT__ ',
    '‰': ' __PERMILLE__ ',
    '‱': ' __PERMYRIAD__ ',
    '󱺈': ' __PERSIX__ ',
    '󱺉': ' __PERNIF__ ',
    '󱺊': ' __PERARDA__ ',
    '󱺋': ' __PERSIXARDA__ ',
    '󱺌': ' __PERNIFARDA__ ',
    '󱺍': ' __PERSHADARA__ ',
    '󱺎': ' __PERSIXSHADARA__ ',
    '󱺏': ' __PERNIFSHADARA__ ',
    '󱺐': ' __PERARDASHADARA__ ',
    '󱺑': ' __PERSIXARDASHADARA__ ',
    '󱺒': ' __PERNIFARDASHADARA__ ',
    '󱺓': ' __PERDISHADARA__ ',
    '󱺔': ' __PERTRISHADARA__ ',
    '󱺕': ' __PERCHARSHADARA__ ',
    '󱺖': ' __PERPANSHADARA__ ',
    '󱺗': ' __PERSHASHADARA__ ',
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

_IN_PREPARED_EXPRESSION_OPERATION = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__PERCENT__': "/Sezimal('244')",
    '__PERMILLE__': "/Sezimal('4_344')",
    '__PERMYRIAD__': "/Sezimal('114_144')",
    '__PERSIX__': "/Sezimal('10')",
    '__PERNIF__': "/Sezimal('100')",
    '__PERARDA__': "/Sezimal('1_000')",
    '__PERSIXARDA__': "/Sezimal('10_000')",
    '__PERNIFARDA__': "/Sezimal('100_000')",
    '__PERSHADARA__': "/Sezimal('1_000_000')",
    '__PERSIXSHADARA__': "/Sezimal('1e11')",
    '__PERNIFSHADARA__': "/Sezimal('1e12')",
    '__PERARDASHADARA__': "/Sezimal('1e13')",
    '__PERSIXARDASHADARA__': "/Sezimal('1e14')",
    '__PERNIFARDASHADARA__': "/Sezimal('1e15')",
    '__PERDISHADARA__': "/Sezimal('1e20')",
    '__PERTRISHADARA__': "/Sezimal('1e30')",
    '__PERCHARSHADARA__': "/Sezimal('1e40')",
    '__PERPANSHADARA__': "/Sezimal('1e50')",
    '__PERSHASHADARA__': "/Sezimal('1e100')",
    '__SQUARE__': "**Sezimal('2')",
    '__CUBE__': "**Sezimal('3')",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__MOD__': '|',
}

_IN_EXPRESSION_OPERATION  = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    # '__PERCENT__': '/ 244',
    # '__PERMILLE__': '/ 4_344',
    # '__PERMYRIAD__': '/ 114_144',
    # '__PERSIX__': '/ 10',
    # '__PERNIF__': '/ 100',
    # '__PERARDA__': '/ 1_000',
    # '__PERSIXARDA__': '/ 10_000',
    # '__PERNIFARDA__': '/ 100_000',
    # '__PERSHADARA__': '/ 1_000_000',
    # '__PERSIXSHADARA__': '/ 10_000_000',
    # '__PERNIFSHADARA__': '/ 100_000_000',
    # '__PERARDASHADARA__': '/ 1_000_000_000',
    # '__PERSIXARDASHADARA__': '/ 10_000_000_000',
    # '__PERNIFARDASHADARA__': '/ 100_000_000_000',
    # '__PERDISHADARA__': '/ 1_000_000_000_000',
    # '__PERTRISHADARA__': '/ 1_000_000_000_000_000_000',
    # '__PERCHARSHADARA__': '/ 1_000_000_000_000_000_000_000_000',
    # '__PERPANSHADARA__': '/ 1_000_000_000_000_000_000_000_000_000_000',
    # '__PERSHASHADARA__': '/ 1_000_000_000_000_000_000_000_000_000_000_000_000',
    '__SQUARE__': "^ 2",
    '__CUBE__': "^ 3",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__MOD__': '|',
    # '__PERCENT_DECIMAL__': '/ 100',
    # '__PERMILLE_DECIMAL__': '/ 1_000',
    # '__PERMYRIAD_DECIMAL__': '/ 10_000',
    # '__PERSIX_DECIMAL__': '/ 6',
    # '__PERNIF_DECIMAL__': '/ 36',
    # '__PERARDA_DECIMAL__': '/ 216',
    # '__PERSIXARDA_DECIMAL__': '/ 1_296',
    # '__PERNIFARDA_DECIMAL__': '/ 7_776',
    # '__PERSHADARA_DECIMAL__': '/ 46_656',
    # '__PERSIXSHADARA_DECIMAL__': '/ 279_936',
    # '__PERNIFSHADARA_DECIMAL__': '/ 1_679_616',
    # '__PERARDASHADARA_DECIMAL__': '/ 10_077_696',
    # '__PERSIXARDASHADARA_DECIMAL__':'/ 60_466_176',
    # '__PERNIFARDASHADARA_DECIMAL__':'/ 362_797_056',
    # '__PERDISHADARA_DECIMAL__': '/ 2_176_782_336',
    # '__PERTRISHADARA_DECIMAL__': '/ 101_559_956_668_416',
    # '__PERCHARSHADARA_DECIMAL__': '/ 4_738_381_338_321_616_896',
    # '__PERPANSHADARA_DECIMAL__': '/ 221_073_919_720_733_357_899_776',
    # '__PERSHASHADARA_DECIMAL__': '/ 10_314_424_798_490_535_546_171_949_056',
}

_NICE_OPERATION = {
    '__ADD__': ' + ',
    '__SUBTRACT__': ' − ',
    '__DIVIDE__': ' ÷ ',
    '__MULTIPLY__': ' × ',
    '__POWER__': ' ^ ',
    '__PERCENT__': '%',
    '__PERMILLE__': '‰',
    '__PERMYRIAD__': '‱',
    '__PERSIX__': '󱺈',
    '__PERNIF__': '󱺉',
    '__PERARDA__': '󱺊',
    '__PERSIXARDA__': '󱺋',
    '__PERNIFARDA__': '󱺌',
    '__PERSHADARA__': '󱺍',
    '__PERSIXSHADARA__': '󱺎',
    '__PERNIFSHADARA__': '󱺏',
    '__PERARDASHADARA__': '󱺐',
    '__PERSIXARDASHADARA__': '󱺑',
    '__PERNIFARDASHADARA__': '󱺒',
    '__PERDISHADARA__': '󱺓',
    '__PERTRISHADARA__': '󱺔',
    '__PERCHARSHADARA__': '󱺕',
    '__PERPANSHADARA__': '󱺖',
    '__PERSHASHADARA__': '󱺗',
    '__SQUARE__': "²",
    '__CUBE__': "³",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
}

_PER_OPERATIONS = ('__PERCENT__', '__PERMILLE__', '__PERMYRIAD__', '__PERSIX__', '__PERNIF__', '__PERARDA__', '__PERSIXARDA__', '__PERNIFARDA__', '__PERSHADARA__', '__PERSIXSHADARA__', '__PERNIFSHADARA__', '__PERARDASHADARA__', '__PERSIXARDASHADARA__', '__PERNIFARDASHADARA__', '__PERDISHADARA__', '__PERTRISHADARA__', '__PERCHARSHADARA__', '__PERPANSHADARA__', '__PERSHASHADARA__')

_PER_OPERATIONS_DECIMAL_TO_SEZIMAL = (
    ('%', ' / 244', ' ÷ 24̄', ' ÷ 󱸂󱸜'),
    ('‰', ' / 4_344', ' ÷ 3̄4̄', ' ÷ 󱸛󱸜'),
    ('‱', ' / 114_144', ' ÷ 1̇1̄4̄', ' ÷ 󱸇󱸙󱸜'),
)

_PER_OPERATIONS_SEZIMAL_TO_DECIMAL = (
    ('%', ' / 36'),
    ('‰', ' / 216'),
    ('‱', ' / 1_296'),
    ('󱺈', ' / 6'),
    ('󱺉', ' / 36'),
    ('󱺊', ' / 216'),
    ('󱺋', ' / 1_296'),
    ('󱺌', ' / 7_776'),
    ('󱺍', ' / 46_656'),
    ('󱺎', ' / 279_936'),
    ('󱺏', ' / 1_679_616'),
    ('󱺐', ' / 10_077_696'),
    ('󱺑', ' / 60_466_176'),
    ('󱺒', ' / 362_797_056'),
    ('󱺓', ' / 2_176_782_336'),
    ('󱺔', ' / 101_559_956_668_416'),
    ('󱺕', ' / 4_738_381_338_321_616_896'),
    ('󱺖', ' / 221_073_919_720_733_357_899_776'),
    ('󱺗', ' / 10_314_424_798_490_535_546_171_949_056'),
)

e = E
π = PI
τ = TAU
φ = GOLDEN_RATIO


class SezimalCalculator:
    def __init__(self, expression: str = '0', locale: str | SezimalLocale = None):
        self.sezimal_digits = False
        self.regularized_digits = True
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
    def niftimal_display(self):
        return self._niftimal_display

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
                spellout += sezimal_spellout(f'SH-{self.unit} {part}', lang) + ' '
            elif self.unit and part.replace('/', '').replace('⁄', '').isdigit():
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

    def _format_sezimal(self, number, display: bool = False, part: str = '', keep_original_aspect=True):
        if part and type(part) == str and '⁄' in part:
            numerator, denominator = part.split('⁄')

            numerator = self._format_sezimal(numerator, display, numerator, keep_original_aspect)

            if denominator:
                denominator = self._format_sezimal(denominator, display, denominator, keep_original_aspect)
                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif not part and type(number) == SezimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = self._format_sezimal(numerator, display, numerator, keep_original_aspect)
            denominator = self._format_sezimal(denominator, display, numerator, keep_original_aspect)
            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._sezimal_precision)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'sezimal_places': precision,
            'sezimal_digits': self.sezimal_digits,
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
            params['typographical_negative'] = False

        if not keep_original_aspect:
            if not recurring_digits_notation:
                number = round(number, precision)

        if display:
            return self.locale.format_number(number, **params)

        return sezimal_format(number, **params)

    def _format_decimal(self, number, display: bool = False, part: str = '', keep_original_aspect: bool = True):
        if part and type(part) == str and '⁄' in part:
            numerator, denominator = part.split('⁄')

            numerator = self._format_decimal(numerator, display, numerator, keep_original_aspect)

            if denominator:
                denominator = self._format_decimal(denominator, display, denominator, keep_original_aspect)
                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif not part and type(number) == DecimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = Decimal(numerator)
            denominator = Decimal(denominator)
            numerator = self._format_decimal(numerator, display, numerator, keep_original_aspect)
            denominator = self._format_decimal(denominator, display, numerator, keep_original_aspect)
            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._decimal_precision)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'decimal_places': precision,
            'recurring_digits_notation': recurring_digits_notation,
            'keep_original_aspect': keep_original_aspect,
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

    def _format_niftimal(self, number, part: str = ''):
        if part and type(part) == str and '⁄' in part:
            numerator, denominator = part.split('⁄')

            numerator = self._format_niftimal(Sezimal(numerator), numerator)

            if denominator:
                denominator = self._format_niftimal(Sezimal(denominator), denominator)
                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif not part and type(number) == SezimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = self._format_niftimal(numerator, str(numerator))
            denominator = self._format_niftimal(denominator, str(numerator))
            return numerator + '⁄' + denominator

        precision = self._determine_precision(number, self._sezimal_precision)
        recurring_digits_notation = '..' in part if type(part) == str else False

        params = {
            'niftimal_places': precision // 2 if precision % 2 == 0 else (precision // 2) + 1,
            'sezimal_digits': self.sezimal_digits,
            'recurring_digits_notation': recurring_digits_notation,
            'use_fraction_group_separator': True,
            'suffix': self.suffix,
            'regularized_digits': self.regularized_digits,
        }

        if type(number) == str:
            number = Sezimal(number)

        return self.locale.format_niftimal_number(number, **params)

    def _apply_sezimal_or_recurring_mark(self, display: str, separator: str, suffix: str) -> str:
        if suffix in PER_SYMBOLS:
            display = display[0:len(suffix) * -1]
        elif suffix:
            display = display[0:(len(suffix) + 1) * -1]

        display += separator

        if suffix in PER_SYMBOLS:
            display += suffix
        elif suffix:
            display += ' ' + suffix

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
                niftimal_display += self._format_niftimal(number)
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
                niftimal_display += self._format_niftimal(part, part=part)
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
            self._niftimal_display = self.locale.ERROR.upper()
        else:
            self._display = 'ERROR'
            self._decimal_display = 'ERROR'
            self._niftimal_display = 'ERROR'
