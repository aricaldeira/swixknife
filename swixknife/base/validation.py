

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

import re
from swixknife.base.digit_conversion import sezimal_to_default_digits, \
    dedicated_niftimal_to_default_digits, dozenal_digits_to_letters, \
    dozenal_letters_to_digits

from swixknife.base.context import sezimal_context


_CLEAN_SPACES = {
    #
    # Sezimal Punctuation
    #
    ord('\U000f1e6c'): '',  # shadara separator 󱹬
    ord('\U000f1e6d'): '',  # arda separator 󱹭
    ord('\U000f1e6e'): '.',  # wedge separator 󱹮
    ord('\U000f1e6f'): '..',  # repeating separator 󱹯
    #
    # Common punctuation
    #
    ord('\u201e'): '..', # double comma „
    ord('\u2025'): '..', # double dot ‥
    ord('\u002c'): '.',  # comma is transformed into full stop
    ord('\u0020'): '',   # space
    ord('\u005f'): '',   # undescore
    ord('\u00a0'): '',   # non-break space
    ord('\u2000'): '',   # other spacing characters
    # ord('\u2001'): '',
    # ord('\u2002'): '',
    # ord('\u2003'): '',
    # ord('\u2004'): '',
    # ord('\u2005'): '',
    # ord('\u2006'): '',
    # ord('\u2007'): '',
    # ord('\u2008'): '',
    # ord('\u2009'): '',
    # ord('\u200a'): '',
    # ord('\u200b'): '',
    # ord('\u200c'): '',
    # ord('\u200d'): '',
    # ord('\u200e'): '',
    # ord('\u200f'): '',
    # ord('\u2010'): '',
    # ord('\u2011'): '',
    # ord('\u2012'): '',
    # ord('\u2013'): '',
    # ord('\u2014'): '',
    # ord('\u2015'): '',
    # ord('\u2016'): '',
    # ord('\u2017'): '',
    # ord('\u2018'): '',
    # ord('\u2019'): '',
    # ord('\u201a'): '',
    # ord('\u201b'): '',
    # ord('\u201c'): '',
    # ord('\u201d'): '',
    # ord('\u201e'): '',
    # ord('\u201f'): '',
    # ord('\u2020'): '',
    # ord('\u2021'): '',
    # ord('\u2022'): '',
    # ord('\u2023'): '',
    # ord('\u2024'): '',
    # ord('\u2025'): '',
    # ord('\u2026'): '',
    # ord('\u2027'): '',
    # ord('\u2028'): '',
    # ord('\u2029'): '',
    # ord('\u202a'): '',
    # ord('\u202b'): '',
    # ord('\u202c'): '',
    # ord('\u202d'): '',
    # ord('\u202e'): '',
    ord('\u202f'): '',   # narrow non-break space
    # ord('\u2030'): '',
    # ord('\u2031'): '',
    # ord('\u2032'): '',
    # ord('\u2033'): '',
    # ord('\u2034'): '',
    # ord('\u2035'): '',
    # ord('\u2036'): '',
    # ord('\u2037'): '',
    # ord('\u2038'): '',
    # ord('\u2039'): '',
    # ord('\u203a'): '',
    # ord('\u203b'): '',
    # ord('\u203c'): '',
    # ord('\u203d'): '',
    # ord('\u203e'): '',
    # ord('\u203f'): '',
    # ord('\u2040'): '',
    # ord('\u2041'): '',
    # ord('\u2042'): '',
    # ord('\u2043'): '',
    # ord('\u2044'): '',
    # ord('\u2045'): '',
    # ord('\u2046'): '',
    # ord('\u2047'): '',
    # ord('\u2048'): '',
    # ord('\u2049'): '',
    # ord('\u204a'): '',
    # ord('\u204b'): '',
    # ord('\u204c'): '',
    # ord('\u204d'): '',
    # ord('\u204e'): '',
    # ord('\u204f'): '',
    # ord('\u2050'): '',
    # ord('\u2051'): '',
    # ord('\u2052'): '',
    # ord('\u2053'): '',
    # ord('\u2054'): '',
    # ord('\u2055'): '',
    # ord('\u2056'): '',
    # ord('\u2057'): '',
    # ord('\u2058'): '',
    # ord('\u2059'): '',
    # ord('\u205a'): '',
    # ord('\u205b'): '',
    # ord('\u205c'): '',
    # ord('\u205d'): '',
    # ord('\u205e'): '',
    # ord('\u205f'): '',
    # ord('\u2060'): '',
    # ord('\u2061'): '',
    # ord('\u2062'): '',
    # ord('\u2063'): '',
    # ord('\u2064'): '',
    # ord('\u2065'): '',
    # ord('\u2066'): '',
    # ord('\u2067'): '',
    # ord('\u2068'): '',
    # ord('\u2069'): '',
    # ord('\u206a'): '',
    # ord('\u206b'): '',
    # ord('\u206c'): '',
    # ord('\u206d'): '',
    # ord('\u206e'): '',
    # ord('\u206f'): '',
}
_FRACTION_SEPARATOR = '\\.'
_RECURRING_MARKER = re.compile('\\.\\.')
_CLOSING_RECURRING_MARKER = re.compile('\\.\\.\\.$')

_VALID_SEZIMAL_FORMAT = re.compile(r'''^[+-]?[0-5]{1,}\.{0,2}([Ee][+-]?[0-5]{1,})?$|^[+-]?[0-5]*\.[0-5]{1,}([Ee][+-]?[0-5]{1,})?$|^[+-]?[0-5]*\.\.[0-5]{1,}(\.\.\.$)?$|^[+-]?[0-5]*\.[0-5]{1,}\.\.[0-5]{1,}(\.\.\.$)?$|^[ΦφΠπΤτ]$''')

_VALID_DECIMAL_FORMAT = re.compile(r'''^[+-]?[0-9]{1,}\.{0,2}([Ee][+-]?[0-9]{1,})?$|^[+-]?[0-9]*\.[0-9]{1,}([Ee][+-]?[0-9]{1,})?$|^[+-]?[0-9]*\.\.[0-9]{1,}(\.\.\.$)?$|^[+-]?[0-9]*\.[0-9]{1,}\.\.[0-9]{1,}(\.\.\.$)?$|^[ΦφΠπΤτ]$''')

_VALID_NIFTIMAL_FORMAT = re.compile(r'''^[+-]?[0-9A-Za-z]{1,}\.{0,2}([Ee][+-][0-9A-Za-z]{1,})?$|^[+-]?[0-9A-Za-z]*\.[0-9A-Za-z]{1,}([Ee][+-][0-9A-Za-z]{1,})?$|^[+-]?[0-9A-Za-z]*\.\.[0-9A-Za-z]{1,}(\.\.\.$)?$|^[+-]?[0-9A-Za-z]*\.[0-9A-Za-z]{1,}\.\.[0-9A-Za-z]{1,}(\.\.\.$)?$|^[ΦφΠπΤτ]$''')

_VALID_DOZENAL_FORMAT = re.compile(r'''^[+-]?[0-9↊↋ABab]{1,}\.{0,2}([Ee][+-]?[0-9↊↋ABab]{1,})?$|^[+-]?[0-9↊↋ABab]*\.[0-9↊↋ABab]{1,}([Ee][+-]?[0-9↊↋ABab]{1,})?$|^[+-]?[0-9↊↋ABab]*\.\.[0-9↊↋ABab]{1,}(\.\.\.$)?$|^[+-]?[0-9↊↋ABab]*\.[0-9↊↋ABab]{1,}\.\.[0-9↊↋ABab]{1,}(\.\.\.$)?$|^[ΦφΠπΤτ]$''')


def validate_clean_sezimal(number: int | float | str | Decimal | Sezimal | SezimalInteger | SezimalFraction, double_precision: bool = False) -> str:
    if type(number) == SezimalFraction:
        number = number.sezimal

    cleaned_number = str(number)

    # cleaned_number = sezimal_to_default_digits(cleaned_number)
    cleaned_number = cleaned_number.translate(_SEZIMAL_CONSTANTS)
    cleaned_number = cleaned_number.translate(_CLEAN_SPACES)

    if not _VALID_SEZIMAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a sezimal number')

    if double_precision or '..' in cleaned_number:
        cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.sezimal_precision_decimal * 2)
    else:
        cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.sezimal_precision_decimal)

    if cleaned_number and cleaned_number[0] == '+':
        cleaned_number = cleaned_number[1:]

    while len(cleaned_number) > 2 and cleaned_number[0:3] == '-00':
            cleaned_number = '-0' + cleaned_number[3:]

    while len(cleaned_number) > 1 and cleaned_number[0] == '0':
        cleaned_number = cleaned_number[1:]

    if cleaned_number and cleaned_number[0] == '.':
        cleaned_number = '0' + cleaned_number

    if cleaned_number and cleaned_number[0] in ('E', 'e'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = _exponent_to_full_form(cleaned_number, 6)

    return cleaned_number


def validate_clean_decimal(number: int | float | str | Decimal) -> str:
    number = str(number)

    cleaned_number = number.translate(_DECIMAL_CONSTANTS)
    cleaned_number = cleaned_number.translate(_CLEAN_SPACES)

    if not _VALID_DECIMAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a decimal number')

    cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.decimal_precision)

    if cleaned_number and cleaned_number[0] == '+':
        cleaned_number = cleaned_number[1:]

    while len(cleaned_number) > 2 and cleaned_number[0:3] == '-00':
            cleaned_number = '-0' + cleaned_number[3:]

    while len(cleaned_number) > 1 and cleaned_number[0] == '0':
        cleaned_number = cleaned_number[1:]

    if cleaned_number and cleaned_number[0] == '.':
        cleaned_number = '0' + cleaned_number

    if cleaned_number and cleaned_number[0] in ('E', 'e'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = _exponent_to_full_form(cleaned_number, 10)

    return cleaned_number


def validate_clean_niftimal(number: int | float | str | Decimal | Sezimal) -> str:
    number = str(number)

    cleaned_number = number.translate(_NIFTIMAL_CONSTANTS)
    cleaned_number = cleaned_number.translate(_CLEAN_SPACES).upper()
    cleaned_number = dedicated_niftimal_to_default_digits(cleaned_number)

    if not _VALID_NIFTIMAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a niftimal number')

    cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.sezimal_precision_decimal // 2)

    if cleaned_number and cleaned_number[0] == '+':
        cleaned_number = cleaned_number[1:]

    while len(cleaned_number) > 2 and cleaned_number[0:3] == '-00':
            cleaned_number = '-0' + cleaned_number[3:]

    while len(cleaned_number) > 1 and cleaned_number[0] == '0':
        cleaned_number = cleaned_number[1:]

    if cleaned_number and cleaned_number[0] == '.':
        cleaned_number = '0' + cleaned_number

    if cleaned_number and len(cleaned_number) >= 2 and cleaned_number[0:2] in ('E+', 'e+', 'E-', 'e-'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = _exponent_to_full_form(cleaned_number, 36)

    return cleaned_number


def validate_clean_dozenal(number: str) -> str:
    number = str(number)

    cleaned_number = number.translate(_DOZENAL_CONSTANTS)
    cleaned_number = cleaned_number.translate(_CLEAN_SPACES).upper()

    if not _VALID_DOZENAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a dozenal number')

    cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.dozenal_precision_decimal)

    if cleaned_number and cleaned_number[0] == '+':
        cleaned_number = cleaned_number[1:]

    while len(cleaned_number) > 2 and cleaned_number[0:3] == '-00':
            cleaned_number = '-0' + cleaned_number[3:]

    while len(cleaned_number) > 1 and cleaned_number[0] == '0':
        cleaned_number = cleaned_number[1:]

    if cleaned_number and cleaned_number[0] == '.':
        cleaned_number = '0' + cleaned_number

    if cleaned_number and cleaned_number[0] in ('E', 'e'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = dozenal_digits_to_letters(cleaned_number)

    cleaned_number = _exponent_to_full_form(cleaned_number, 12)

    cleaned_number = dozenal_letters_to_digits(cleaned_number)

    return cleaned_number


def _clean_recurring_digits(number: str, max_precision: int = 48) -> str:
    number = _CLOSING_RECURRING_MARKER.sub('§', number)
    number = _RECURRING_MARKER.sub('§', number)

    if '§' not in number:
        return number

    recurring = ''

    if number and number[-1] == '§':
        number = number[:-1]

    if '§' not in number:
        return number

    if '.' in number:
        integer, fraction = number.split('.')
        fraction, recurring = fraction.split('§')

    else:
        integer, recurring = number.split('§')
        fraction = ''

    #
    # How many times do we repeat (limit is 120 48_dec)?
    #
    repeating_max_size = max_precision - len(fraction)

    times = ((repeating_max_size) // len(recurring)) + 1

    recurring *= times
    recurring = recurring[:repeating_max_size]

    number = integer + '.' + fraction + recurring

    return number


def _exponent_to_full_form(number: str, base: int = 6) -> str:
    number = number.upper()

    if base == 36:
        if 'E-' not in number and 'E+' not in number:
            return number
    else:
        if 'E-' not in number and 'E+' not in number and 'E' not in number:
            return number

    negative = number and number[0] == '-'

    if negative:
        number = number[1:]

    if '.' in number:
        integer, fraction = number.split('.')
    else:
        if base == 36:
            if 'E+' in number:
                integer, fraction = number.split('E+')
                fraction = 'E+' + fraction
            else:
                integer, fraction = number.split('E-')
                fraction = 'E-' + fraction

        else:
            integer, fraction = number.split('E')
            fraction = 'E' + fraction

    if 'E-' in fraction:
        initial_fraction, exponent = fraction.split('E-')
        negative_exponent = True
    elif 'E+' in fraction:
        initial_fraction, exponent = fraction.split('E+')
        negative_exponent = False
    else:
        initial_fraction, exponent = fraction.split('E')
        negative_exponent = False

    exponent = abs(int(exponent, base))

    if negative_exponent:
        exponent += len(initial_fraction)

        number = integer + initial_fraction
        number = number.zfill(exponent)

        if len(number) > exponent:
            number = number[::-1]
            fraction = number[:exponent][::-1]
            integer = number[exponent:][::-1]

        else:
            integer = ''
            fraction = number

    else:
        number = initial_fraction[::-1].zfill(exponent)[::-1]

        if len(number) > exponent:
            integer += number[:exponent]
            fraction = number[exponent:]

        else:
            integer += number
            fraction = '0' * len(initial_fraction)

    while integer and integer[0] == '0':
        integer = integer[1:]

    if not integer:
        integer = '0'

    number = integer + '.' + fraction

    if negative:
        number = '-' + number

    return number


_SEZIMAL_CONSTANTS = {
    ord('Φ'):
        '1.341_254_554_353_431_451_342_235_140_150_120_045_250_124_044_114',
    ord('φ'):
        '1.341_254_554_353_431_451_342_235_140_150_120_045_250_124_044_114',
    ord('Π'):
        '3.050_330_051_415_124_105_234_414_053_125_321_102_301_214_442_004',
    ord('π'):
        '3.050_330_051_415_124_105_234_414_053_125_321_102_301_214_442_004',
    ord('Τ'):
        '10.141_100_143_234_252_214_513_232_150_255_042_205_002_433_324_012',
    ord('τ'):
        '10.141_100_143_234_252_214_513_232_150_255_042_205_002_433_324_012',
}

_DECIMAL_CONSTANTS = {
    ord('Φ'):
        '1.618_033_988_749_894_848_204_586_834_365_638_118',
    ord('φ'):
        '1.618_033_988_749_894_848_204_586_834_365_638_118',
    ord('Π'):
        '3.141_592_653_589_793_238_462_643_383_279_502_884',
    ord('π'):
        '3.141_592_653_589_793_238_462_643_383_279_502_884',
    ord('Τ'):
        '6.283_185_307_179_586_476_925_286_766_559_005_768',
    ord('τ'):
        '6.283_185_307_179_586_476_925_286_766_559_005_768',
}

_NIFTIMAL_CONSTANTS = {
    ord('Φ'): '1.M8YZRXRAVMENA1U80TH1G4PA',
    ord('φ'): '1.M8YZRXRAVMENA1U80TH1G4PA',
    ord('Π'): '3.53I5AB8P5FSA5JHK72I8ASC4',
    ord('π'): '3.53I5AB8P5FSA5JHK72I8ASC4',
    ord('Τ'): '6.A70AKMHEAVKKB2Z4E50GLKO8',
    ord('τ'): '6.A70AKMHEAVKKB2Z4E50GLKO8',
}

_DOZENAL_CONSTANTS = {
    ord('Φ'): '1.74↋↋6772802↊46↊6↊186530714908↊0912714↊',
    ord('φ'): '1.74↋↋6772802↊46↊6↊186530714908↊0912714↊',
    ord('Π'): '3.184809493↋918664573↊6211↋↋151551↊04708',
    ord('π'): '3.184809493↋918664573↊6211↋↋151551↊04708',
    ord('Τ'): '6.349416967↋635108↋2790423↋↊2↊2↊↊3809926',
    ord('τ'): '6.349416967↋635108↋2790423↋↊2↊2↊↊3809926',
}


def _make_validation_expression(
    all_digits='[0-5]',
    fraction_separator=_FRACTION_SEPARATOR,
    recurring_marker=_RECURRING_MARKER,
) -> re.Pattern:
    recurring_marker = f'{recurring_marker.pattern}'
    closing_recurring_marker = f'({_CLOSING_RECURRING_MARKER.pattern})?'

    required_digits = f'{all_digits}{{1,}}'
    optional_digits = f'{all_digits}*'

    integer = f'[+-]?{required_digits}{fraction_separator}{{0,2}}'

    common_fractional = f'[+-]?{optional_digits}{fraction_separator}{required_digits}'
    recurring_fractional = f'[+-]?{optional_digits}{recurring_marker}{required_digits}{closing_recurring_marker}'
    complex_recurring_fraction = f'[+-]?{optional_digits}{fraction_separator}{required_digits}{recurring_marker}{required_digits}{closing_recurring_marker}'

    #
    # If letters are used as digits, the use exponents
    # is only allowed when a mandatory sign +/- is
    # right next to E/e
    #
    if 'Z' in all_digits:
        exponent = f'([Ee][+-]{required_digits})?'
    else:
        exponent = f'([Ee][+-]?{required_digits})?'

    constants = '[ΦφΠπΤτ]'

    all_pattern = f'^{integer}{exponent}$|^{common_fractional}{exponent}$|^{recurring_fractional}$|^{complex_recurring_fraction}$|^{constants}$'

    return re.compile(all_pattern)


if __name__ == '__main__':
    print(f"_VALID_SEZIMAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-5]').pattern}''')")
    print()
    print(f"_VALID_DECIMAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-9]').pattern}''')")
    print()
    print(f"_VALID_NIFTIMAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-9A-Za-z]').pattern}''')")
    print()
    print(f"_VALID_DOZENAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-9↊↋ABab]').pattern}''')")
