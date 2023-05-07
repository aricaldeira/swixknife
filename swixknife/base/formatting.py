

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
Decimal = TypeVar('Decimal', bound='Decimal')

import re
from .validation import validate_clean_sezimal, validate_clean_decimal
from .decimal_sezimal_conversion import decimal_to_sezimal
from .sezimal_decimal_conversion import sezimal_to_decimal
from .digit_conversion import (
    default_to_dedicated_digits,
    default_to_numerator_digits, default_to_denominator_digits,
    default_to_dedicated_numerator_digits, default_to_dedicated_denominator_digits,
)

_TWO_DIGITS_GROUP_FORMAT = re.compile('([0-5]{2})')
_THREE_DIGITS_GROUP_FORMAT = re.compile('([0-9]{3})')
_FOUR_DIGITS_GROUP_FORMAT = re.compile('([0-5]{4})')

SEPARATOR_COMMA = ','
SEPARATOR_DOT = '.'
SEPARATOR_UNDERSCORE = '_'
SEPARATOR_NARROW_NOBREAK_SPACE = '\u202f'
SEPARATOR_NOBREAK_SPACE = '\u00a0'
SEPARATOR_HAIR_SPACE = '\u200a'
SEPARATOR_DOT_ABOVE = '\u02d9'
SEPARATOR_ZERO_WIDTH_JOINER = '\u200d'
TYPOGRAPHICAL_NEGATIVE = '\u2212'
TYPOGRAPHICAL_FRACTION_SLASH = '\u2044'


def sezimal_format(number: str | int | float | Decimal | Sezimal | SezimalInteger,
                   sezimal_places: str | int | Decimal | SezimalInteger = 3,
                   sezimal_separator: str = SEPARATOR_DOT,
                   group_separator: str = SEPARATOR_UNDERSCORE,
                   subgroup_separator: str = '',
                   fraction_group_separator: str = SEPARATOR_UNDERSCORE,
                   fraction_subgroup_separator: str = '',
                   dedicated_digits: bool = False,
                   typographical_negative: bool = False,
                   minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0) -> str:
    if type(number).__name__ == 'Decimal':
        number = decimal_to_sezimal(number)

    if type(sezimal_places).__name__ == 'Decimal':
        sezimal_places = decimal_to_sezimal(sezimal_places)

    if type(minimum_size).__name__ == 'Decimal':
        minimum_size = decimal_to_sezimal(minimum_size)

    number = validate_clean_sezimal(str(number))
    sezimal_places = validate_clean_sezimal(sezimal_places)
    minimum_size = validate_clean_sezimal(minimum_size)

    sezimal_places = int(sezimal_to_decimal(sezimal_places))
    minimum_size = int(sezimal_to_decimal(minimum_size))

    if '.' in number:
        integer, fraction = number.split('.')
    else:
        integer, fraction = number, ''

    if sezimal_places:
        fraction = fraction.ljust(sezimal_places, '0')[:sezimal_places]
    else:
        fraction = ''

    if group_separator:
        if minimum_size > 0:
            integer = integer.rjust(minimum_size, '0')
        integer = _apply_format(integer, group_separator, _FOUR_DIGITS_GROUP_FORMAT)

        if subgroup_separator:
            integer = _apply_format(integer, subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)
            integer = integer.replace(subgroup_separator + group_separator, group_separator)
            integer = integer.replace(group_separator + subgroup_separator, group_separator)

    if fraction and fraction_group_separator:
        fraction = _apply_format(fraction[::-1], fraction_group_separator, _FOUR_DIGITS_GROUP_FORMAT)[::-1]

        if fraction_subgroup_separator:
            fraction = _apply_format(fraction[::-1], fraction_subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)[::-1]
            fraction = fraction.replace(fraction_subgroup_separator + fraction_group_separator, fraction_group_separator)
            fraction = fraction.replace(fraction_group_separator + fraction_subgroup_separator, fraction_group_separator)

    formatted_number = integer

    if fraction:
        formatted_number += sezimal_separator
        formatted_number += fraction

    if dedicated_digits:
        formatted_number = default_to_dedicated_digits(formatted_number)

    if formatted_number[0] == '-' and typographical_negative:
        formatted_number = TYPOGRAPHICAL_NEGATIVE + formatted_number[1:]

    return formatted_number


def _apply_format(number: str, separator: str, format_patter: re.Pattern) -> str:
    formatted_number = number[::-1]
    parts = re.split(format_patter, formatted_number)
    parts = list(filter(bool, parts))
    formatted_number = separator.join(parts)
    return formatted_number[::-1]


def sezimal_format_fraction(numerator: str | int | float | Decimal | Sezimal, denominator: str | int | float | Decimal | Sezimal, dedicated_digits: bool = False) -> str:
    if type(numerator).__name__ == 'Decimal':
        numerator = decimal_to_sezimal(numerator)

    numerator = validate_clean_sezimal(str(numerator))

    if type(denominator).__name__ == 'Decimal':
        denominator = decimal_to_sezimal(denominator)

    denominator = validate_clean_sezimal(str(denominator))

    if dedicated_digits:
        numerator = default_to_dedicated_numerator_digits(numerator)
        denominator = default_to_dedicated_denominator_digits(denominator)

    else:
        numerator = default_to_numerator_digits(numerator)
        denominator = default_to_denominator_digits(denominator)

    return numerator + TYPOGRAPHICAL_FRACTION_SLASH + denominator


def decimal_format(number: str | int | float | Decimal | Sezimal,
                   decimal_places: int = 2,
                   decimal_separator: str = SEPARATOR_DOT,
                   group_separator: str = SEPARATOR_UNDERSCORE,
                   fraction_group_separator: str = SEPARATOR_UNDERSCORE,
                   typographical_negative: bool = False) -> str:
    if type(number).__name__ == 'Sezimal':
        number = sezimal_to_decimal(number)

    number = validate_clean_decimal(str(number))

    if '.' in number:
        integer, fraction = number.split('.')
    else:
        integer, fraction = number, ''

    if decimal_places:
        fraction = fraction.ljust(decimal_places, '0')[:decimal_places]
    else:
        fraction = ''

    if group_separator:
        integer = _apply_format(integer, group_separator, _THREE_DIGITS_GROUP_FORMAT)

    if fraction_group_separator and fraction:
        fraction = _apply_format(fraction[::-1], fraction_group_separator, _THREE_DIGITS_GROUP_FORMAT)[::-1]

    formatted_number = integer

    if fraction:
        formatted_number += decimal_separator
        formatted_number += fraction

    if formatted_number[0] == '-' and typographical_negative:
        formatted_number = TYPOGRAPHICAL_NEGATIVE + formatted_number[1:]

    return formatted_number
