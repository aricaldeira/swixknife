

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
Decimal = TypeVar('Decimal', bound='Decimal')

import re
from .validation import validate_clean_sezimal
from .decimal_sezimal_conversion import decimal_to_sezimal
from .digit_conversion import (
    default_to_dedicated_digits,
    default_to_numerator_digits, default_to_denominator_digits,
    default_to_dedicated_numerator_digits, default_to_dedicated_denominator_digits,
)

_GROUP_FORMAT = re.compile('([0-5]{4})')
_SUBGROUP_FORMAT = re.compile('([0-5]{2})')

SEPARATOR_COMMA = ','
SEPARATOR_DOT = '.'
SEPARATOR_NARROW_NOBREAK_SPACE = '\u202f'
SEPARATOR_NOBREAK_SPACE = '\u00a0'
SEPARATOR_HAIR_SPACE = '\u200a'
SEPARATOR_DOT_ABOVE = '\u02d9'
SEPARATOR_ZERO_WIDTH_JOINER = '\u200d'
TYPOGRAPHICAL_NEGATIVE = '\u2212'
TYPOGRAPHICAL_FRACTION_SLASH = '\u2044'


def sezimal_format(number: str | int | float | Decimal | Sezimal,
                   sezimal_places: int = 3,
                   sezimal_separator: str = SEPARATOR_DOT,
                   group_separator: str = SEPARATOR_NARROW_NOBREAK_SPACE,
                   subgroup_separator: str = '',
                   fraction_group_separator: str = SEPARATOR_NARROW_NOBREAK_SPACE,
                   fraction_subgroup_separator: str = '',
                   dedicated_digits: bool = False,
                   typographical_negative: bool = False) -> str:
    if str(type(number)) == 'Decimal':
        number = decimal_to_sezimal(number)

    number = validate_clean_sezimal(str(number))

    if '.' in number:
        integer, fraction = number.split('.')
    else:
        integer, fraction = number, ''

    if sezimal_places:
        fraction = fraction.zfill(sezimal_places)[:sezimal_places]
    else:
        fraction = ''

    if group_separator:
        integer = _apply_format(integer, group_separator, _GROUP_FORMAT)

        if subgroup_separator:
            integer = _apply_format(integer, subgroup_separator, _SUBGROUP_FORMAT)
            integer = integer.replace(subgroup_separator + group_separator, group_separator)
            integer = integer.replace(group_separator + subgroup_separator, group_separator)

    if fraction_group_separator and fraction:
        fraction = _apply_format(fraction[::-1], fraction_group_separator, _GROUP_FORMAT)[::-1]

        if fraction_subgroup_separator:
            fraction = _apply_format(fraction[::-1], fraction_subgroup_separator, _SUBGROUP_FORMAT)[::-1]
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
    if str(type(numerator)) == 'Decimal':
        numerator = decimal_to_sezimal(numerator)

    numerator = validate_clean_sezimal(str(numerator))

    if str(type(denominator)) == 'Decimal':
        denominator = decimal_to_sezimal(denominator)

    denominator = validate_clean_sezimal(str(denominator))

    if dedicated_digits:
        numerator = default_to_dedicated_numerator_digits(numerator)
        denominator = default_to_dedicated_denominator_digits(denominator)

    else:
        numerator = default_to_numerator_digits(numerator)
        denominator = default_to_denominator_digits(denominator)

    return numerator + TYPOGRAPHICAL_FRACTION_SLASH + denominator
