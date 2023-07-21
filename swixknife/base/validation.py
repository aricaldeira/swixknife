

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

import re
from .digit_conversion import dedicated_to_default_digits, dedicated_niftimal_to_default_digits


def _exponent_to_full_form(number: str, base: int = 6) -> str:
    number = number.upper()

    if base == 36:
        if 'E-' not in number and 'E+' not in number:
            return number
    else:
        if 'E-' not in number and 'E+' not in number and 'E' not in number:
            return number

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

    if cleaned_number.startswith('E') or cleaned_number.startswith('e'):
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

    if cleaned_number.startswith('E') or cleaned_number.startswith('e'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    invalid = _VALID_DECIMAL_FORMAT.sub('', cleaned_number)

    if invalid != '':
        raise ValueError(f'The number {number} has an invalid format for a decimal number')

    cleaned_number = _exponent_to_full_form(cleaned_number, 10)

    return cleaned_number


#
# Niftimal numbers,
# when using engineering notation (E+, E-),
# always have to specify the exponent sign;
# when sezimal numbers don’t specify a sign,
# a positive sign + is assumed
#
_VALID_NIFTIMAL_FORMAT = re.compile(r'^[+\-]?[0-9A-Z]+\.?$|^[+\-]?[0-9A-Z]*\.[0-9A-Z]+$|^[+\-]?[0-9A-Z]+\.?[Ee][+\-][0-9A-Z]*$|^[+\-]?[0-9A-Z]*\.[0-9A-Z]+[Ee][+\-][0-9A-Z]*$')


def validate_clean_niftimal(number: int | float | str | Decimal | Sezimal) -> str:
    number = str(number).upper()

    if not number:
        raise ValueError(f'An empty string is not a valid niftimal number')

    cleaned_number = dedicated_niftimal_to_default_digits(number)
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

    if cleaned_number.startswith('E+') or cleaned_number.startswith('e+'):
        cleaned_number = '0' + cleaned_number
    elif cleaned_number.startswith('E-') or cleaned_number.startswith('e-'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    invalid = _VALID_NIFTIMAL_FORMAT.sub('', cleaned_number)

    if invalid != '':
        raise ValueError(f'The number {number} has an invalid format for a niftimal number')

    cleaned_number = _exponent_to_full_form(cleaned_number, 36)

    return cleaned_number


_VALID_DOZENAL_FORMAT = re.compile(r'^[+\-]?[0-9↊↋]+\.?$|^[+\-]?[0-9↊↋]*\.[0-9↊↋]+$|^[+\-]?[0-9↊↋]+\.?[Ee][+\-]?[0-9↊↋]*$|^[+\-]?[0-9↊↋]*\.[0-9↊↋]+[Ee][+\-]?[0-9↊↋]*$')


def validate_clean_dozenal(number: str) -> str:
    number = str(number)

    if not number:
        raise ValueError(f'An empty string is not a valid dozenal number')

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

    if cleaned_number.startswith('E') or cleaned_number.startswith('e'):
        cleaned_number = '0' + cleaned_number

    if not cleaned_number:
        cleaned_number = '0'

    cleaned_number = cleaned_number.replace('A', '↊')
    cleaned_number = cleaned_number.replace('a', '↊')
    cleaned_number = cleaned_number.replace('B', '↋')
    cleaned_number = cleaned_number.replace('b', '↋')

    invalid = _VALID_DOZENAL_FORMAT.sub('', cleaned_number)

    if invalid != '':
        raise ValueError(f'The number {number} has an invalid format for a dozenal number')

    cleaned_number = _exponent_to_full_form(cleaned_number, 10)

    return cleaned_number
