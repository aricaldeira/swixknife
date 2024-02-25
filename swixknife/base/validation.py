

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

import re
from swixknife.base.digit_conversion import dedicated_to_default_digits, \
    dedicated_niftimal_to_default_digits, dozenal_digits_to_letters, \
    dozenal_letters_to_digits

from .context import sezimal_context


_CLEAN_SPACES = re.compile('[\u0020\u00a0\u2000-\u206f_]')
_FRACTION_SEPARATOR = '\\.'
_RECURRING_MARKER = re.compile(f'\\.\\.')
_CLOSING_RECURRING_MARKER = re.compile(f'\\.\\.\\.')


_VALID_SEZIMAL_FORMAT = re.compile(r'''^[+-]?[0-5]{1,}\.{0,2}([Ee][+-]?[0-5]{1,})?$|^[+-]?[0-5]*\.[0-5]{1,}([Ee][+-]?[0-5]{1,})?$|^[+-]?[0-5]*\.\.[0-5]{1,}(\.\.\.)?$|^[+-]?[0-5]*\.[0-5]{1,}\.\.[0-5]{1,}(\.\.\.)?$''')

_VALID_DECIMAL_FORMAT = re.compile(r'''^[+-]?[0-9]{1,}\.{0,2}([Ee][+-]?[0-9]{1,})?$|^[+-]?[0-9]*\.[0-9]{1,}([Ee][+-]?[0-9]{1,})?$|^[+-]?[0-9]*\.\.[0-9]{1,}(\.\.\.)?$|^[+-]?[0-9]*\.[0-9]{1,}\.\.[0-9]{1,}(\.\.\.)?$''')

_VALID_NIFTIMAL_FORMAT = re.compile(r'''^[+-]?[0-9A-Za-z]{1,}\.{0,2}([Ee][+-][0-9A-Za-z]{1,})?$|^[+-]?[0-9A-Za-z]*\.[0-9A-Za-z]{1,}([Ee][+-][0-9A-Za-z]{1,})?$|^[+-]?[0-9A-Za-z]*\.\.[0-9A-Za-z]{1,}(\.\.\.)?$|^[+-]?[0-9A-Za-z]*\.[0-9A-Za-z]{1,}\.\.[0-9A-Za-z]{1,}(\.\.\.)?$''')

_VALID_DOZENAL_FORMAT = re.compile(r'''^[+-]?[0-9↊↋ABab]{1,}\.{0,2}([Ee][+-]?[0-9↊↋ABab]{1,})?$|^[+-]?[0-9↊↋ABab]*\.[0-9↊↋ABab]{1,}([Ee][+-]?[0-9↊↋ABab]{1,})?$|^[+-]?[0-9↊↋ABab]*\.\.[0-9↊↋ABab]{1,}(\.\.\.)?$|^[+-]?[0-9↊↋ABab]*\.[0-9↊↋ABab]{1,}\.\.[0-9↊↋ABab]{1,}(\.\.\.)?$''')


def validate_clean_sezimal(number: int | float | str | Decimal | Sezimal | SezimalInteger | SezimalFraction, double_precision: bool = False) -> str:
    if type(number) == SezimalFraction:
        number = number.sezimal

    number = str(number)

    cleaned_number = _CLEAN_SPACES.sub('', number)
    cleaned_number = dedicated_to_default_digits(cleaned_number)

    if not _VALID_SEZIMAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a sezimal number')

    if double_precision:
        cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.sezimal_precision_decimal * 2)
    else:
        cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.sezimal_precision_decimal)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    while cleaned_number.startswith('-00'):
        cleaned_number = '-0' + cleaned_number[3:]

    if len(cleaned_number) > 1:
        while cleaned_number.startswith('0'):
            cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('.'):
        cleaned_number = '0' + cleaned_number

    if cleaned_number.startswith('E') or cleaned_number.startswith('e'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = _exponent_to_full_form(cleaned_number, 6)

    return cleaned_number


def validate_clean_decimal(number: int | float | str | Decimal) -> str:
    number = str(number)

    cleaned_number = _CLEAN_SPACES.sub('', number)

    if not _VALID_DECIMAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a decimal number')

    cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.decimal_precision)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    while cleaned_number.startswith('-00'):
        cleaned_number = '-0' + cleaned_number[3:]

    if len(cleaned_number) > 1:
        while cleaned_number.startswith('0'):
            cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('.'):
        cleaned_number = '0' + cleaned_number

    if cleaned_number.startswith('E') or cleaned_number.startswith('e'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = _exponent_to_full_form(cleaned_number, 10)

    return cleaned_number


def validate_clean_niftimal(number: int | float | str | Decimal | Sezimal) -> str:
    number = str(number)

    cleaned_number = _CLEAN_SPACES.sub('', number).upper()
    cleaned_number = dedicated_niftimal_to_default_digits(cleaned_number)

    if not _VALID_NIFTIMAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a niftimal number')

    cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.sezimal_precision_decimal // 2)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    while cleaned_number.startswith('-00'):
        cleaned_number = '-0' + cleaned_number[3:]

    if len(cleaned_number) > 1:
        while cleaned_number.startswith('0'):
            cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('.'):
        cleaned_number = '0' + cleaned_number

    if cleaned_number.startswith('E+') or cleaned_number.startswith('e+'):
        cleaned_number = '0' + cleaned_number
    elif cleaned_number.startswith('E-') or cleaned_number.startswith('e-'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = _exponent_to_full_form(cleaned_number, 36)

    return cleaned_number


def validate_clean_dozenal(number: str) -> str:
    number = str(number)

    cleaned_number = _CLEAN_SPACES.sub('', number).upper()

    if not _VALID_DOZENAL_FORMAT.match(cleaned_number):
        raise ValueError(f'The number {number} has an invalid format for a dozenal number')

    cleaned_number = _clean_recurring_digits(cleaned_number, sezimal_context.dozenal_precision)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    while cleaned_number.startswith('-00'):
        cleaned_number = '-0' + cleaned_number[3:]

    if len(cleaned_number) > 1:
        while cleaned_number.startswith('0'):
            cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('.'):
        cleaned_number = '0' + cleaned_number

    if cleaned_number.startswith('E') or cleaned_number.startswith('e'):
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

    if number.endswith('§'):
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

    negative = number.startswith('-')

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

    while integer.startswith('0'):
        integer = integer[1:]

    if not integer:
        integer = '0'

    number = integer + '.' + fraction

    if negative:
        number = '-' + number

    return number


def _make_validation_expression(all_digits='[0-5]') -> re.Pattern:
    fraction_separator = _FRACTION_SEPARATOR
    recurring_marker = f'{_RECURRING_MARKER.pattern}'
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

    all_pattern = f'^{integer}{exponent}$|^{common_fractional}{exponent}$|^{recurring_fractional}$|^{complex_recurring_fraction}$'

    return re.compile(all_pattern)


if __name__ == '__main__':
    print(f"_VALID_SEZIMAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-5]').pattern}''')")
    print()
    print(f"_VALID_DECIMAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-9]').pattern}''')")
    print()
    print(f"_VALID_NIFTIMAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-9A-Za-z]').pattern}''')")
    print()
    print(f"_VALID_DOZENAL_FORMAT = re.compile(r'''{_make_validation_expression('[0-9↊↋ABab]').pattern}''')")
