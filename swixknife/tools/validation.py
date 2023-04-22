

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

import re
from .digit_conversion import dedicated_to_default_digits, dedicated_compressed_to_default_digits


def _exponent_to_full_form(number: str, base: int = 6) -> str:
    number = number.upper()

    if 'E-' not in number and 'E+' not in number and 'E' not in number:
        return number

    if '.' in number:
        integer, fraction = number.split('.')
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

    return number


_SPACES = re.compile('[\u0020\u00a0\u2000-\u206f]')


def _clean_separators(number: str) -> str:
    number = number.replace('_', '')
    number = number.replace(',', '.')
    number = number.replace('\u02d9', '')
    number = _SPACES.sub('', number)
    return number


_VALID_SEZIMAL_FORMAT = re.compile(r'^[+\-]?[0-5]+\.?$|^[+\-]?[0-5]*\.[0-5]+$|^[+\-]?[0-5]+\.?[Ee][+\-]?[0-5]*$|^[+\-]?[0-5]*\.[0-5]+[Ee][+\-]?[0-5]*$')


def validate_clean_sezimal(number: int | float | str | Decimal | Sezimal | SezimalInteger) -> str:
    number = str(number)

    if not number:
        raise ValueError(f'An empty string is not a valid sezimal number')

    cleaned_number = dedicated_to_default_digits(number)
    cleaned_number = _clean_separators(cleaned_number)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    while cleaned_number.startswith('-00'):
        cleaned_number = '-0' + cleaned_number[3:]

    if len(cleaned_number) > 1:
        while cleaned_number.startswith('0'):
            cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('.'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    invalid = _VALID_SEZIMAL_FORMAT.sub('', cleaned_number)

    if invalid != '':
        raise ValueError(f'The number {number} has an invalid format for a sezimal number')

    cleaned_number = _exponent_to_full_form(cleaned_number, 6)

    return cleaned_number


_VALID_DECIMAL_FORMAT = re.compile(r'^[+\-]?[0-9]+\.?$|^[+\-]?[0-9]*\.[0-9]+$|^[+\-]?[0-9]+\.?[Ee][+\-]?[0-9]*$|^[+\-]?[0-9]*\.[0-9]+[Ee][+\-]?[0-9]*$')


def validate_clean_decimal(number: int | float | str | Decimal | Sezimal) -> str:
    number = str(number)

    if not number:
        raise ValueError(f'An empty string is not a valid decimal number')

    cleaned_number = _clean_separators(number)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    while cleaned_number.startswith('-00'):
        cleaned_number = '-0' + cleaned_number[3:]

    if len(cleaned_number) > 1:
        while cleaned_number.startswith('0'):
            cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('.'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    invalid = _VALID_DECIMAL_FORMAT.sub('', cleaned_number)

    if invalid != '':
        raise ValueError(f'The number {number} has an invalid format for a decimal number')

    cleaned_number = _exponent_to_full_form(cleaned_number, 10)

    return cleaned_number


#
# Compressed sezimal numbers,
# when using engineering notation (E+, E-),
# always have to specify the exponent sign;
# when regular sezimal numbers don’t specify a sign,
# a positive sign + is assumed
#
_VALID_COMPRESSED_SEZIMAL_FORMAT = re.compile(r'^[+\-]?[0-9A-Z]+\.?$|^[+\-]?[0-9A-Z]*\.[0-9A-Z]+$|^[+\-]?[0-9A-Z]+\.?[Ee][+\-][0-9A-Z]*$|^[+\-]?[0-9A-Z]*\.[0-9A-Z]+[Ee][+\-][0-9A-Z]*$')


def validate_clean_compressed_sezimal(number: int | float | str | Decimal | Sezimal) -> str:
    number = str(number).upper()

    if not number:
        raise ValueError(f'An empty string is not a valid compressed sezimal number')

    cleaned_number = dedicated_compressed_to_default_digits(number)
    cleaned_number = _clean_separators(cleaned_number)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    while cleaned_number.startswith('-00'):
        cleaned_number = '-0' + cleaned_number[3:]

    if len(cleaned_number) > 1:
        while cleaned_number.startswith('0'):
            cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('.'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    invalid = _VALID_COMPRESSED_SEZIMAL_FORMAT.sub('', cleaned_number)

    if invalid != '':
        raise ValueError(f'The number {number} has an invalid format for a compressed sezimal number')

    cleaned_number = _exponent_to_full_form(cleaned_number, 6)

    return cleaned_number
