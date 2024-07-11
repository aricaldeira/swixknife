

__all__ = ('SezimalCalculator',)

from decimal import Decimal
from fractions import Fraction as DecimalFraction

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..constants import E, PI, TAU, GOLDEN_RATIO, SQRT_2
from ..base import default_to_sezimal_digits, decimal_to_sezimal, \
    validate_clean_sezimal, validate_clean_decimal, \
    sezimal_format, decimal_format, niftimal_format, \
    RECURRING_DIGITS_NOTATION_NONE, \
    RECURRING_DIGITS_NOTATION_SIMPLE
from ..base.digit_conversion import PER_SYMBOLS
from ..exponents import sezimal_exponent_to_decimal_exponent, decimal_exponent_to_sezimal_exponent
from ..units import sezimal_to_decimal_unit, decimal_to_sezimal_unit
from ..text import sezimal_spellout
from ..functions.trigonometry import *

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
    '󱹰': ' __PERSIX__ ',
    '󱹱': ' __PERNIF__ ',
    '󱹲': ' __PERARDA__ ',
    '󱹳': ' __PERSIXARDA__ ',
    '󱹴': ' __PERNIFARDA__ ',
    '󱹵': ' __PERSHADARA__ ',
    '󱹶': ' __PERSIXSHADARA__ ',
    '󱹷': ' __PERNIFSHADARA__ ',
    '󱹸': ' __PERARDASHADARA__ ',
    '󱹹': ' __PERSIXARDASHADARA__ ',
    '󱹺': ' __PERNIFARDASHADARA__ ',
    '󱹻': ' __PERDISHADARA__ ',
    '󱹼': ' __PERTRISHADARA__ ',
    '󱹽': ' __PERCHARSHADARA__ ',
    '󱹾': ' __PERPANSHADARA__ ',
    '󱹿': ' __PERSHASHADARA__ ',
    '±': ' __PLUS_MINUS__ ',
    'mod': ' __MODULO__ ',
    '!': ' __FACTORIAL__ ',

    #
    # Functions and “punctuation”
    #
    'ln': ' __NATURAL_LOGARITHM__ ',
    'lsez': ' __SEZIMAL_LOGARITHM__ ',
    'ldec': ' __DECIMAL_LOGARITHM__ ',
    '²': ' __SQUARE__ ',
    '\u200b²': ' __SQUARE__ ',
    'sqrt': ' __SQUARE_ROOT__ ',
    '³': ' __CUBE__ ',
    '\u200b³': ' __CUBE__ ',
    'cbrt': ' __CUBIC_ROOT__ ',
    'SIN(': ' __SINE__ ',
    'arcsin(': ' __ARC_SINE__ ',
    'asin(': ' __A_SINE__ ',
    'CSC(': ' __COSECANT__ ',
    'arccsc(': ' __ARC_COSECANT__ ',
    'acsc(': ' __A_COSECANT__ ',
    'COS(': ' __COSINE__ ',
    'arccos(': ' __ARC_COSINE__ ',
    'acos(': ' __A_COSINE__ ',
    'SEC(': ' __SECANT__ ',
    'arcsec(': ' __ARC_SECANT__ ',
    'asec(': ' __A_SECANT__ ',
    'TAN(': ' __TANGENT__ ',
    'arctan(': ' __ARC_TANGENT__ ',
    'atan(': ' __A_TANGENT__ ',
    'COT(': ' __COTANGENT__ ',
    'arccot(': ' __ARC_COTANGENT__ ',
    'acot(': ' __A_COTANGENT__ ',
    'SINH(': ' __HYPERBOLIC_SINE__ ',
    'arcsinh(': ' __HYPERBOLIC_ARC_SINE__ ',
    'asinh(': ' __HYPERBOLIC_A_SINE__ ',
    'CSCH(': ' __HYPERBOLIC_COSECANT__ ',
    'arccsch(': ' __HYPERBOLIC_ARC_COSECANT__ ',
    'acsch(': ' __HYPERBOLIC_A_COSECANT__ ',
    'COSH(': ' __HYPERBOLIC_COSINE__ ',
    'arccosh(': ' __HYPERBOLIC_ARC_COSINE__ ',
    'acosh(': ' __HYPERBOLIC_A_COSINE__ ',
    'SECH(': ' __HYPERBOLIC_SECANT__ ',
    'arcsech(': ' __HYPERBOLIC_ARC_SECANT__ ',
    'asech(': ' __HYPERBOLIC_A_SECANT__ ',
    'TANH(': ' __HYPERBOLIC_TANGENT__ ',
    'arctanh(': ' __HYPERBOLIC_ARC_TANGENT__ ',
    'atanh(': ' __HYPERBOLIC_A_TANGENT__ ',
    'COTH(': ' __HYPERBOLIC_COTANGENT__ ',
    'arccoth(': ' __HYPERBOLIC_ARC_COTANGENT__ ',
    'acoth(': ' __HYPERBOLIC_A_COTANGENT__ ',
    '(': ' __LEFT_PARENTHESIS__ ',
    ')': ' __RIGHT_PARENTHESIS__ ',
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
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__MODULO__': 'mod',
    '__NATURAL_LOGARITHM__': 'self.ln',
    '__SEZIMAL_LOGARITHM__': 'self.lsez',
    '__DECIMAL_LOGARITHM__': 'self.ldec',
    '__SQUARE__': "**Sezimal('2')",
    '__SQUARE_ROOT__': 'self.sqrt',
    '__CUBE__': "**Sezimal('3')",
    '__CUBIC_ROOT__': 'self.cbrt',
    '__FACTORIAL__': '.factorial()',
    '__SINE__': 'self.SIN(',
    '__ARC_SINE__': 'self.arcsin(',
    '__A_SINE__': 'self.asin(',
    '__COSECANT__': 'self.CSC(',
    '__ARC_COSECANT__': 'self.arccsc(',
    '__A_COSECANT__': 'self.acsc(',
    '__COSINE__': 'self.COS(',
    '__ARC_COSINE__': 'self.arccos(',
    '__A_COSINE__': 'self.acos(',
    '__SECANT__': 'self.SEC(',
    '__ARC_SECANT__': 'self.arcsec(',
    '__A_SECANT__': 'self.asec(',
    '__TANGENT__': 'self.TAN(',
    '__ARC_TANGENT__': 'self.arctan(',
    '__A_TANGENT__': 'self.atan(',
    '__COTANGENT__': 'self.COT(',
    '__ARC_COTANGENT__': 'self.arccot(',
    '__A_COTANGENT__': 'self.acot(',
    '__HYPERBOLIC_SINE__': 'self.SINH(',
    '__HYPERBOLIC_ARC_SINE__': 'self.arcsinh(',
    '__HYPERBOLIC_A_SINE__': 'self.asinh(',
    '__HYPERBOLIC_COSECANT__': 'self.CSCH(',
    '__HYPERBOLIC_ARC_COSECANT__': 'self.arccsch(',
    '__HYPERBOLIC_A_COSECANT__': 'self.acsch(',
    '__HYPERBOLIC_COSINE__': 'self.COSH(',
    '__HYPERBOLIC_ARC_COSINE__': 'self.arccosh(',
    '__HYPERBOLIC_A_COSINE__': 'self.acosh(',
    '__HYPERBOLIC_SECANT__': 'self.SECH(',
    '__HYPERBOLIC_ARC_SECANT__': 'self.arcsech(',
    '__HYPERBOLIC_A_SECANT__': 'self.asech(',
    '__HYPERBOLIC_TANGENT__': 'self.TANH(',
    '__HYPERBOLIC_ARC_TANGENT__': 'self.arctanh(',
    '__HYPERBOLIC_A_TANGENT__': 'self.atanh(',
    '__HYPERBOLIC_COTANGENT__': 'self.COTH(',
    '__HYPERBOLIC_ARC_COTANGENT__': 'self.arccoth(',
    '__HYPERBOLIC_A_COTANGENT__': 'self.acoth(',
}

_IN_EXPRESSION_OPERATION  = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__NATURAL_LOGARITHM__': 'ln',
    '__SEZIMAL_LOGARITHM__': 'lsez',
    '__DECIMAL_LOGARITHM__': 'ldec',
    '__SQUARE__': '\u200b²',
    '__SQUARE_ROOT__': 'sqrt',
    '__CUBE__': '\u200b³',
    '__CUBIC_ROOT__': 'cbrt',
    '__MODULO__': ' mod ',
    '__FACTORIAL__': '!',
    '__SINE__': 'SIN(',
    '__ARC_SINE__': 'arcsin(',
    '__A_SINE__': 'asin(',
    '__COSECANT__': 'CSC(',
    '__ARC_COSECANT__': 'arccsc(',
    '__A_COSECANT__': 'acsc(',
    '__COSINE__': 'COS(',
    '__ARC_COSINE__': 'arccos(',
    '__A_COSINE__': 'acos(',
    '__SECANT__': 'SEC(',
    '__ARC_SECANT__': 'arcsec(',
    '__A_SECANT__': 'asec(',
    '__TANGENT__': 'TAN(',
    '__ARC_TANGENT__': 'arctan(',
    '__A_TANGENT__': 'atan(',
    '__COTANGENT__': 'COT(',
    '__ARC_COTANGENT__': 'arccot(',
    '__A_COTANGENT__': 'acot(',
    '__HYPERBOLIC_SINE__': 'SINH(',
    '__HYPERBOLIC_ARC_SINE__': 'arcsinh(',
    '__HYPERBOLIC_A_SINE__': 'asinh(',
    '__HYPERBOLIC_COSECANT__': 'CSCH(',
    '__HYPERBOLIC_ARC_COSECANT__': 'arccsch(',
    '__HYPERBOLIC_A_COSECANT__': 'acsch(',
    '__HYPERBOLIC_COSINE__': 'COSH(',
    '__HYPERBOLIC_ARC_COSINE__': 'arccosh(',
    '__HYPERBOLIC_A_COSINE__': 'acosh(',
    '__HYPERBOLIC_SECANT__': 'SECH(',
    '__HYPERBOLIC_ARC_SECANT__': 'arcsech(',
    '__HYPERBOLIC_A_SECANT__': 'asech(',
    '__HYPERBOLIC_TANGENT__': 'TANH(',
    '__HYPERBOLIC_ARC_TANGENT__': 'arctanh(',
    '__HYPERBOLIC_A_TANGENT__': 'atanh(',
    '__HYPERBOLIC_COTANGENT__': 'COTH(',
    '__HYPERBOLIC_ARC_COTANGENT__': 'arccoth(',
    '__HYPERBOLIC_A_COTANGENT__': 'acoth(',
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
    '__PERSIX__': '󱹰',
    '__PERNIF__': '󱹱',
    '__PERARDA__': '󱹲',
    '__PERSIXARDA__': '󱹳',
    '__PERNIFARDA__': '󱹴',
    '__PERSHADARA__': '󱹵',
    '__PERSIXSHADARA__': '󱹶',
    '__PERNIFSHADARA__': '󱹷',
    '__PERARDASHADARA__': '󱹸',
    '__PERSIXARDASHADARA__': '󱹹',
    '__PERNIFARDASHADARA__': '󱹺',
    '__PERDISHADARA__': '󱹻',
    '__PERTRISHADARA__': '󱹼',
    '__PERCHARSHADARA__': '󱹽',
    '__PERPANSHADARA__': '󱹾',
    '__PERSHASHADARA__': '󱹿',
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
    '__NATURAL_LOGARITHM__': 'ln',
    '__SEZIMAL_LOGARITHM__': 'lsez',
    '__DECIMAL_LOGARITHM__': 'ldec',
    '__SQUARE__': '\u200b²',
    '__SQUARE_ROOT__': 'sqrt',
    '__CUBE__': '\u200b³',
    '__CUBIC_ROOT__': 'cbrt',
    '__MODULO__': ' mod ',
    '__FACTORIAL__': '!',
    '__SINE__': 'sin(',
    '__ARC_SINE__': 'arcsin(',
    '__A_SINE__': 'asin(',
    '__COSECANT__': 'csc(',
    '__ARC_COSECANT__': 'arccsc(',
    '__A_COSECANT__': 'acsc(',
    '__COSINE__': 'cos(',
    '__ARC_COSINE__': 'arccos(',
    '__A_COSINE__': 'acos(',
    '__SECANT__': 'sec(',
    '__ARC_SECANT__': 'arcsec(',
    '__A_SECANT__': 'asec(',
    '__TANGENT__': 'tan(',
    '__ARC_TANGENT__': 'arctan(',
    '__A_TANGENT__': 'atan(',
    '__COTANGENT__': 'cot(',
    '__ARC_COTANGENT__': 'arccot(',
    '__A_COTANGENT__': 'acot(',
    '__HYPERBOLIC_SINE__': 'sinh(',
    '__HYPERBOLIC_ARC_SINE__': 'arcsinh(',
    '__HYPERBOLIC_A_SINE__': 'asinh(',
    '__HYPERBOLIC_COSECANT__': 'csch(',
    '__HYPERBOLIC_ARC_COSECANT__': 'arccsch(',
    '__HYPERBOLIC_A_COSECANT__': 'acsch(',
    '__HYPERBOLIC_COSINE__': 'cosh(',
    '__HYPERBOLIC_ARC_COSINE__': 'arccosh(',
    '__HYPERBOLIC_A_COSINE__': 'acosh(',
    '__HYPERBOLIC_SECANT__': 'sech(',
    '__HYPERBOLIC_ARC_SECANT__': 'arcsech(',
    '__HYPERBOLIC_A_SECANT__': 'asech(',
    '__HYPERBOLIC_TANGENT__': 'tanh(',
    '__HYPERBOLIC_ARC_TANGENT__': 'arctanh(',
    '__HYPERBOLIC_A_TANGENT__': 'atanh(',
    '__HYPERBOLIC_COTANGENT__': 'coth(',
    '__HYPERBOLIC_ARC_COTANGENT__': 'arccoth(',
    '__HYPERBOLIC_A_COTANGENT__': 'acoth(',
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
    ('󱹰', ' / 6'),
    ('󱹱', ' / 36'),
    ('󱹲', ' / 216'),
    ('󱹳', ' / 1_296'),
    ('󱹴', ' / 7_776'),
    ('󱹵', ' / 46_656'),
    ('󱹶', ' / 279_936'),
    ('󱹷', ' / 1_679_616'),
    ('󱹸', ' / 10_077_696'),
    ('󱹹', ' / 60_466_176'),
    ('󱹺', ' / 362_797_056'),
    ('󱹻', ' / 2_176_782_336'),
    ('󱹼', ' / 101_559_956_668_416'),
    ('󱹽', ' / 4_738_381_338_321_616_896'),
    ('󱹾', ' / 221_073_919_720_733_357_899_776'),
    ('󱹿', ' / 10_314_424_798_490_535_546_171_949_056'),
)

_NO_SPACE_OPERATIONS = (
    '__LEFT_PARENTHESIS__',
    '__RIGHT_PARENTHESIS__',
    '__NATURAL_LOGARITHM__',
    '__SEZIMAL_LOGARITHM__',
    '__DECIMAL_LOGARITHM__',
    '__SQUARE__',
    '__SQUARE_ROOT__',
    '__CUBE__',
    '__CUBIC_ROOT__',
    '__FACTORIAL__',
    '__SINE__',
    '__ARC_SINE__',
    '__A_SINE__',
    '__COSECANT__',
    '__ARC_COSECANT__',
    '__A_COSECANT__',
    '__COSINE__',
    '__ARC_COSINE__',
    '__A_COSINE__',
    '__SECANT__',
    '__ARC_SECANT__',
    '__A_SECANT__',
    '__TANGENT__',
    '__ARC_TANGENT__',
    '__A_TANGENT__',
    '__COTANGENT__',
    '__ARC_COTANGENT__',
    '__A_COTANGENT__',
)

_TRIGONOMETRIC_FUNCTION = (
    '__SINE__',
    '__ARC_SINE__',
    '__A_SINE__',
    '__COSECANT__',
    '__ARC_COSECANT__',
    '__A_COSECANT__',
    '__COSINE__',
    '__ARC_COSINE__',
    '__A_COSINE__',
    '__SECANT__',
    '__ARC_SECANT__',
    '__A_SECANT__',
    '__TANGENT__',
    '__ARC_TANGENT__',
    '__A_TANGENT__',
    '__COTANGENT__',
    '__ARC_COTANGENT__',
    '__A_COTANGENT__',
)


_CONSTANTS = ('e', 'π', 'τ', 'φ')

e = E
π = PI
τ = TAU
φ = GOLDEN_RATIO


class SezimalCalculator:
    def __init__(self, expression: str = '0', locale: str | SezimalLocale = None):
        self.sezimal_digits = False
        self.sezimal_punctuation = True
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
        self.unit_as_fraction = False
        self.angle = 'prd'
        self.decimal_angle = 'tau_rad'
        self.angle_as_fraction = True
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

                if denominator == '1':
                    return numerator

                return numerator + '⁄' + denominator

            return numerator + '⁄'

        elif type(number) == SezimalFraction:
            numerator, denominator = number.numerator, number.denominator
            numerator = self._format_sezimal(numerator, display, numerator, keep_original_aspect)
            denominator = self._format_sezimal(denominator, display, numerator, keep_original_aspect)

            if denominator == '1':
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
            # params['sezimal_separator'] = '󱹭'
            # params['group_separator'] = ' '
            # params['fraction_group_separator'] = ' '
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
            return self.locale.format_number(number, **params)

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

                if denominator == '1':
                    return numerator

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
            'sezimal_punctuation': self.sezimal_punctuation,
            'recurring_digits_notation': recurring_digits_notation,
            'use_fraction_group_separator': True,
            'suffix': self.suffix,
            'regularized_digits': self.regularized_digits,
            # 'niftimal_separator': '󱹭',
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
            display += '\N{NNBSP}' + suffix

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

            if part == '.':
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
                else:
                    number = Decimal(validate_clean_decimal(part))
                    prepared_expression += f"Decimal('{number}')"

                decimal_display += self._format_decimal(part, display=True, part=part)
                decimal_expression += self._format_decimal(part, part=part)

                if trigonometry_opened and self.angle and self.decimal_angle:
                    number = decimal_to_sezimal_unit(number, self.decimal_angle, self.angle, return_fraction=self.angle_as_fraction)

                    if not self.angle_as_fraction:
                        number = round(number, self._sezimal_precision)

                elif self.unit and self.decimal_unit:
                    number = decimal_to_sezimal_unit(number, self.decimal_unit, self.unit, return_fraction=self.unit_as_fraction)

                    if not self.unit_as_fraction:
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
                else:
                    number = Sezimal(part)
                    prepared_expression += f"Sezimal('{number}')"

                display += self._format_sezimal(part, display=True, part=part)
                niftimal_display += self._format_niftimal(cleaned_part, part=part)
                sezimal_expression += self._format_sezimal(part, part=part)

                if trigonometry_opened and self.angle and self.decimal_angle:
                    number = sezimal_to_decimal_unit(number, self.angle, self.decimal_angle, return_fraction=self.angle_as_fraction)

                    if not self.angle_as_fraction:
                        try:
                            number = round(number.decimal, int(self._decimal_precision))
                        except:
                            number = number.decimal

                elif self.unit and self.decimal_unit:
                    number = sezimal_to_decimal_unit(number, self.unit, self.decimal_unit, return_fraction=self.unit_as_fraction)

                    if not self.unit_as_fraction:
                        try:
                            number = round(number.decimal, int(self._decimal_precision))
                        except:
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
            response = eval(self._prepared_expression.replace('mod', '%'))

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
            self._display = self.locale.ERROR.upper()
            self._decimal_display = self.locale.ERROR.upper()
            self._niftimal_display = self.locale.ERROR.upper()
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
