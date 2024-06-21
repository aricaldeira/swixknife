

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

_OPERATION = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__PERCENT__': "/Sezimal('100')",
    '__PERMILLE__': "/Sezimal('1_000')",
    '__PERMYRIAD__': "/Sezimal('10_000')",
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

_OPERATION_DECIMAL  = {
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

_ALLWAYS_NICE_OPERATIONS = ('__PERCENT__', '__PERMILLE__', '__PERMYRIAD__', '__PERSIX__', '__PERNIF__', '__PERARDA__', '__PERSIXARDA__', '__PERNIFARDA__', '__PERSHADARA__', '__PERSIXSHADARA__', '__PERNIFSHADARA__', '__PERARDASHADARA__', '__PERSIXARDASHADARA__', '__PERNIFARDASHADARA__', '__PERDISHADARA__', '__PERTRISHADARA__', '__PERCHARSHADARA__', '__PERPANSHADARA__', '__PERSHASHADARA__')

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
        if suffix in ('%', '‰', '‱', '󱺈', '󱺉', '󱺊', '󱺋', '󱺌', '󱺍', '󱺎', '󱺏', '󱺐', '󱺑', '󱺒', '󱺓', '󱺔', '󱺕', '󱺖', '󱺗', '󱹷', '󱹸', '󱹹', '󱹺', '󱹻', '󱹼', '󱹽', '󱹾', '󱹿', '󱺀', '󱺁', '󱺂', '󱺃', '󱺄', '󱺅', '󱺆', '󱺇'):
            display = display[0:len(suffix) * -1]
        elif suffix:
            display = display[0:(len(suffix) + 1) * -1]

        display += separator

        if suffix in ('%', '‰', '‱', '󱺈', '󱺉', '󱺊', '󱺋', '󱺌', '󱺍', '󱺎', '󱺏', '󱺐', '󱺑', '󱺒', '󱺓', '󱺔', '󱺕', '󱺖', '󱺗', '󱹷', '󱹸', '󱹹', '󱹺', '󱹻', '󱹼', '󱹽', '󱹾', '󱹿', '󱺀', '󱺁', '󱺂', '󱺃', '󱺄', '󱺅', '󱺆', '󱺇'):
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

        if self.expression == '0':
            if self.sezimal_digits:
                self._display = '󱸀'
            else:
                self._display = '0'

            self._decimal_display = '0'

            if self.decimal:
                self._prepared_expression = "Decimal('0')"
            else:
                self._prepared_expression = "Sezimal('0')"

            self._sezimal_expression = "0"
            self._decimal_expression = "0"

            return

        exp = self.expression

        print('expressão', exp)

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

                    if part in _ALLWAYS_NICE_OPERATIONS:
                        decimal_expression += f'{_NICE_OPERATION[part]} '
                    else:
                        decimal_expression += f' {_OPERATION_DECIMAL[part]} '

                else:
                    prepared_expression += _OPERATION[part]

                    if part in _ALLWAYS_NICE_OPERATIONS:
                        sezimal_expression +=  f'{_NICE_OPERATION[part]} '
                    else:
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
                        if previous_part.strip() in _ALLWAYS_NICE_OPERATIONS:
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
                    for symbol, display_text, expression_text in (
                        ('%', ' ÷ 244', ' / 244'),
                        ('‰', f' ÷ 4{self.locale.GROUP_SEPARATOR}344', ' / 4_344'),
                        ('‱', f' ÷ 114{self.locale.GROUP_SEPARATOR}144', ' / 114_144'),
                    ):
                        display = display.replace(symbol, display_text)
                        exp = exp.replace(symbol, expression_text)

                else:
                    for symbol, display_text, expression_text in (
                        ('%', ' ÷ 36', ' / 36'),
                        ('‰', ' ÷ 216', ' / 216'),
                        ('‱', f' ÷ 1{self.locale.GROUP_SEPARATOR}296', ' / 1_296'),
                        ('󱺈', ' ÷ 6', ' / 6'),
                        ('󱺉', ' ÷ 36', ' / 36'),
                        ('󱺊', ' ÷ 216', ' / 216'),
                        ('󱺋', f' ÷ 1{self.locale.GROUP_SEPARATOR}296', ' / 1_296'),
                        ('󱺌', f' ÷ 7{self.locale.GROUP_SEPARATOR}776', ' / 7_776'),
                        ('󱺍', f' ÷ 46{self.locale.GROUP_SEPARATOR}656', ' / 46_656'),
                        ('󱺎', f' ÷ 279{self.locale.GROUP_SEPARATOR}936', ' / 279_936'),
                        ('󱺏', f' ÷ 1{self.locale.GROUP_SEPARATOR}679{self.locale.GROUP_SEPARATOR}616', ' / 1_679_616'),
                        ('󱺐', f' ÷ 10{self.locale.GROUP_SEPARATOR}077{self.locale.GROUP_SEPARATOR}696', ' / 10_077_696'),
                        ('󱺑', f' ÷ 60{self.locale.GROUP_SEPARATOR}466{self.locale.GROUP_SEPARATOR}176', ' / 60_466_176'),
                        ('󱺒', f' ÷ 362{self.locale.GROUP_SEPARATOR}797{self.locale.GROUP_SEPARATOR}056', ' / 362_797_056'),
                        ('󱺓', f' ÷ 2{self.locale.GROUP_SEPARATOR}176{self.locale.GROUP_SEPARATOR}782{self.locale.GROUP_SEPARATOR}336', ' / 2_176_782_336'),
                        ('󱺔', f' ÷ 101{self.locale.GROUP_SEPARATOR}559{self.locale.GROUP_SEPARATOR}956{self.locale.GROUP_SEPARATOR}668{self.locale.GROUP_SEPARATOR}416', ' / 101_559_956_668_416'),
                        ('󱺕', f' ÷ 4{self.locale.GROUP_SEPARATOR}738{self.locale.GROUP_SEPARATOR}381{self.locale.GROUP_SEPARATOR}338{self.locale.GROUP_SEPARATOR}321{self.locale.GROUP_SEPARATOR}616{self.locale.GROUP_SEPARATOR}896', ' / 4_738_381_338_321_616_896'),
                        ('󱺖', f' ÷ 221{self.locale.GROUP_SEPARATOR}073{self.locale.GROUP_SEPARATOR}919{self.locale.GROUP_SEPARATOR}720{self.locale.GROUP_SEPARATOR}733{self.locale.GROUP_SEPARATOR}357{self.locale.GROUP_SEPARATOR}899{self.locale.GROUP_SEPARATOR}776', ' / 221_073_919_720_733_357_899_776'),
                        ('󱺗', f' ÷ 10{self.locale.GROUP_SEPARATOR}314{self.locale.GROUP_SEPARATOR}424{self.locale.GROUP_SEPARATOR}798{self.locale.GROUP_SEPARATOR}490{self.locale.GROUP_SEPARATOR}535{self.locale.GROUP_SEPARATOR}546{self.locale.GROUP_SEPARATOR}171{self.locale.GROUP_SEPARATOR}949{self.locale.GROUP_SEPARATOR}056', ' / 10_314_424_798_490_535_546_171_949_056'),
                    ):
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
