

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')
Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

import re
from .validation import validate_clean_sezimal, validate_clean_decimal, \
    validate_clean_niftimal, validate_clean_dozenal, \
    _MAX_SEZIMAL_PRECISION_DECIMAL, MAX_DECIMAL_PRECISION, \
    _MAX_DOZENAL_PRECISION_DECIMAL
from .decimal_sezimal_conversion import decimal_to_sezimal
from .sezimal_decimal_conversion import sezimal_to_decimal
from .sezimal_niftimal_conversion import sezimal_to_niftimal, niftimal_to_sezimal
from .sezimal_dozenal_conversion import sezimal_to_dozenal, dozenal_to_sezimal
from .dozenal_decimal_conversion import dozenal_to_decimal
from .digit_conversion import (
    default_to_dedicated_digits,
    default_to_numerator_digits, default_to_denominator_digits,
    default_to_dedicated_numerator_digits, default_to_dedicated_denominator_digits,
    default_niftimal_to_regularized_digits, default_niftimal_to_financial_digits,
    default_niftimal_to_regularized_dedicated_digits, default_niftimal_to_financial_dedicated_digits,
    dozenal_letters_to_digits,
)

_TWO_DIGITS_GROUP_FORMAT = re.compile('([0-9↊↋A-Z]{2})')
_THREE_DIGITS_GROUP_FORMAT = re.compile('([0-9↊↋A-Z]{3})')
_FOUR_DIGITS_GROUP_FORMAT = re.compile('([0-9↊↋A-Z]{4})')

_ONE_DIGIT = re.compile('([0-9↊↋A-Z]{1})')
_RECURRING_DIGITS_COMBINING_OVERLINE = '\u0305'

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


def sezimal_format(
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        sezimal_places: str | int | Decimal | Sezimal | SezimalInteger | SezimalFraction = 4,
        sezimal_separator: str = SEPARATOR_DOT,
        group_separator: str = SEPARATOR_UNDERSCORE,
        subgroup_separator: str = '',
        fraction_group_separator: str = SEPARATOR_UNDERSCORE,
        fraction_subgroup_separator: str = '',
        dedicated_digits: bool = False,
        typographical_negative: bool = False,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        mark_recurring_digits: bool = False,
        p_recurring_notation: bool = False,
    ) -> str:
    if type(number).__name__ == 'Decimal':
        number = decimal_to_sezimal(number)

    if type(sezimal_places).__name__ == 'Decimal':
        sezimal_places = decimal_to_sezimal(sezimal_places)

    if type(minimum_size).__name__ == 'Decimal':
        minimum_size = decimal_to_sezimal(minimum_size)

    if type(number).__name__ == 'SezimalFraction':
        number = number.sezimal

    number = validate_clean_sezimal(str(number))
    sezimal_places = validate_clean_sezimal(sezimal_places)
    minimum_size = validate_clean_sezimal(minimum_size)

    sezimal_places = int(sezimal_to_decimal(sezimal_places))
    minimum_size = int(sezimal_to_decimal(minimum_size))

    recurring: str = ''

    if '.' in number:
        integer, fraction = number.split('.')

        if mark_recurring_digits and fraction:
            fixed_part, recurring = _identify_recurring_digits(fraction[:_MAX_SEZIMAL_PRECISION_DECIMAL], max_fraction_size=_MAX_SEZIMAL_PRECISION_DECIMAL)

            if recurring:
                fraction = fixed_part + recurring

    else:
        integer, fraction = number, ''

    if not mark_recurring_digits:
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

        if mark_recurring_digits and recurring:
            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                p_recurring_notation or fraction_group_separator == '_',
                _FOUR_DIGITS_GROUP_FORMAT,
                fraction_group_separator,
            )
        else:
            formatted_number += fraction

    if dedicated_digits:
        formatted_number = default_to_dedicated_digits(formatted_number)

    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    return formatted_number


def _apply_format(number: str, separator: str, format_pattern: re.Pattern) -> str:
    is_negative = number[0] in '-−⁻₋'

    if is_negative:
        number = number[1:]

    formatted_number = number[::-1]
    parts = re.split(format_pattern, formatted_number)
    parts = list(filter(bool, parts))
    formatted_number = separator.join(parts)
    formatted_number = formatted_number[::-1]

    if is_negative:
        formatted_number = '-' + formatted_number

    return formatted_number


def _finish_formatting(formatted_number: str, prefix: str, suffix: str, positive_format: str, negative_format: str, typographical_negative: bool) -> str:
    if prefix:
        prefix += ' '

    if suffix and suffix[-1] not in '%‰‱':
        suffix = ' ' + suffix

    if formatted_number[0] != '-':
        formatted_number = positive_format.format(prefix=prefix, value=formatted_number, suffix=suffix)
    else:
        formatted_number = negative_format.format(prefix=prefix, value=formatted_number[1:], suffix=suffix)

        if typographical_negative:
            formatted_number = TYPOGRAPHICAL_NEGATIVE + formatted_number[1:]

    return formatted_number


def sezimal_format_fraction(numerator: str | int | float | Decimal | Sezimal | SezimalInteger, denominator: str | int | float | Decimal | Sezimal | SezimalInteger, dedicated_digits: bool = False) -> str:
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


def decimal_format(
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        decimal_places: str | int | Decimal | SezimalInteger = 2,
        decimal_separator: str = SEPARATOR_DOT,
        group_separator: str = SEPARATOR_UNDERSCORE,
        fraction_group_separator: str = SEPARATOR_UNDERSCORE,
        typographical_negative: bool = False,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        mark_recurring_digits: bool = False,
        p_recurring_notation: bool = False,
        #
        # Lakhs and crores are Indian names for powers of ten
        # https://en.wikipedia.org/wiki/Indian_numbering_system
        #
        lakh_crore_grouping: bool = False,
        #
        # 萬/万: Chinese wàn/ㄨㄢˋ, Japanese まん man, Korean 만 man, Vietnamese vạn
        # https://en.wikipedia.org/wiki/Japanese_numerals#Powers_of_10
        #
        wan_man_van_grouping: bool = False,
    ) -> str:
    if type(number).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        number = sezimal_to_decimal(number)

    if type(decimal_places).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        decimal_places = sezimal_to_decimal(decimal_places)

    if type(minimum_size).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        minimum_size = sezimal_to_decimal(minimum_size)

    number = validate_clean_decimal(str(number))
    decimal_places = int(validate_clean_decimal(str(decimal_places)))
    minimum_size = int(validate_clean_decimal(str(minimum_size)))

    recurring: str = ''

    if '.' in number:
        integer, fraction = number.split('.')

        if mark_recurring_digits and fraction:
            fixed_part, recurring = _identify_recurring_digits(fraction[:MAX_DECIMAL_PRECISION], max_fraction_size=MAX_DECIMAL_PRECISION)

            if recurring:
                fraction = fixed_part + recurring

    else:
        integer, fraction = number, ''

    if not mark_recurring_digits:
        if decimal_places:
            fraction = fraction.ljust(decimal_places, '0')[:decimal_places]
        else:
            fraction = ''

    if group_separator:
        if minimum_size > 0:
            integer = integer.rjust(minimum_size, '0')

        if wan_man_van_grouping:
            integer = _apply_format(integer, group_separator, _FOUR_DIGITS_GROUP_FORMAT)

        elif lakh_crore_grouping and len(integer) > 3:
            integer = _apply_format(integer[:-3], group_separator, _TWO_DIGITS_GROUP_FORMAT) + group_separator + integer[-3:]

        else:
            integer = _apply_format(integer, group_separator, _THREE_DIGITS_GROUP_FORMAT)

    if fraction_group_separator and fraction:
        if wan_man_van_grouping:
            fraction = _apply_format(fraction[::-1], fraction_group_separator, _FOUR_DIGITS_GROUP_FORMAT)[::-1]

        elif lakh_crore_grouping and len(fraction) > 3:
            fraction = fraction[0:3] + fraction_group_separator + _apply_format(fraction[::-1][:-3], fraction_group_separator, _TWO_DIGITS_GROUP_FORMAT)[::-1]

        else:
            fraction = _apply_format(fraction[::-1], fraction_group_separator, _THREE_DIGITS_GROUP_FORMAT)[::-1]

    formatted_number = integer

    if fraction:
        formatted_number += decimal_separator

        if mark_recurring_digits and recurring:
            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                p_recurring_notation or fraction_group_separator == '_',
                _THREE_DIGITS_GROUP_FORMAT,
                fraction_group_separator
            )
        else:
            formatted_number += fraction

    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    return formatted_number


def dozenal_format(
        number: str | int | float | Decimal | Dozenal | DozenalInteger | DozenalFraction | Sezimal | SezimalInteger | SezimalFraction,
        dozenal_places: str | int | Decimal | Dozenal | DozenalInteger | DozenalFraction | Sezimal | SezimalInteger | SezimalFraction = 2,
        dozenal_separator: str = SEPARATOR_DOT,
        group_separator: str = SEPARATOR_UNDERSCORE,
        subgroup_separator: str = '',
        fraction_group_separator: str = SEPARATOR_UNDERSCORE,
        fraction_subgroup_separator: str = '',
        typographical_negative: bool = False,
        minimum_size: str | int | Decimal | Dozenal | DozenalInteger | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        mark_recurring_digits: bool = False,
        p_recurring_notation: bool = False,
    ) -> str:
    if type(number) in (str, Dozenal, DozenalInteger, DozenalFraction):
        number = dozenal_letters_to_digits(str(number))
    else:
        number = sezimal_to_dozenal(number)

    if type(dozenal_places) in (str, Dozenal, DozenalInteger, DozenalFraction):
        dozenal_places = dozenal_letters_to_digits(str(dozenal_places))
    else:
        dozenal_places = sezimal_to_dozenal(dozenal_places)

    if type(minimum_size) in (str, Dozenal, DozenalInteger, DozenalFraction):
        minimum_size = dozenal_letters_to_digits(str(minimum_size))
    else:
        minimum_size = sezimal_to_dozenal(minimum_size)

    number = validate_clean_dozenal(str(number))
    dozenal_places = validate_clean_dozenal(dozenal_places)
    minimum_size = validate_clean_dozenal(minimum_size)

    dozenal_places = int(dozenal_to_decimal(dozenal_places))
    minimum_size = int(dozenal_to_decimal(minimum_size))

    recurring: str = ''

    if '.' in number:
        integer, fraction = number.split('.')

        if mark_recurring_digits and fraction:
            fixed_part, recurring = _identify_recurring_digits(fraction[:_MAX_DOZENAL_PRECISION_DECIMAL], max_fraction_size=_MAX_DOZENAL_PRECISION_DECIMAL)

            if recurring:
                fraction = fixed_part + recurring

    else:
        integer, fraction = number, ''

    if not mark_recurring_digits:
        if dozenal_places:
            fraction = fraction.ljust(dozenal_places, '0')[:dozenal_places]
        else:
            fraction = ''

    if group_separator:
        if minimum_size > 0:
            integer = integer.rjust(minimum_size, '0')

        integer = _apply_format(integer, group_separator, _THREE_DIGITS_GROUP_FORMAT)

        if subgroup_separator:
            integer = _apply_format(integer, subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)
            integer = integer.replace(subgroup_separator + group_separator, group_separator)
            integer = integer.replace(group_separator + subgroup_separator, group_separator)

    if fraction and fraction_group_separator:
        fraction = _apply_format(fraction[::-1], fraction_group_separator, _THREE_DIGITS_GROUP_FORMAT)[::-1]

        if fraction_subgroup_separator:
            fraction = _apply_format(fraction[::-1], fraction_subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)[::-1]
            fraction = fraction.replace(fraction_subgroup_separator + fraction_group_separator, fraction_group_separator)
            fraction = fraction.replace(fraction_group_separator + fraction_subgroup_separator, fraction_group_separator)

    formatted_number = integer

    if fraction:
        formatted_number += dozenal_separator

        if mark_recurring_digits and recurring:
            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                p_recurring_notation or fraction_group_separator == '_',
                _THREE_DIGITS_GROUP_FORMAT,
                fraction_group_separator
            )
        else:
            formatted_number += fraction

    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    return formatted_number


def niftimal_format(
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        niftimal_places: str | int | Decimal | Sezimal | SezimalInteger | SezimalFraction = 2,
        niftimal_separator: str = SEPARATOR_DOT,
        group_separator: str = SEPARATOR_UNDERSCORE,
        subgroup_separator: str = '',
        fraction_group_separator: str = SEPARATOR_UNDERSCORE,
        fraction_subgroup_separator: str = '',
        regularized_digits: bool = True,
        dedicated_digits: bool = False,
        financial_digits: bool = False,
        typographical_negative: bool = False,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        mark_recurring_digits: bool = False,
        p_recurring_notation: bool = False,
    ) -> str:
    if type(number).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        number = sezimal_to_niftimal(number)
    elif type(number).__name__ == 'Decimal':
        number = sezimal_to_niftimal(decimal_to_sezimal(number))

    if type(niftimal_places).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        niftimal_places = sezimal_to_niftimal(niftimal_places)
    elif type(niftimal_places).__name__ == 'Decimal':
        niftimal_places = sezimal_to_niftimal(decimal_to_sezimal(niftimal_places))

    if type(minimum_size).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        minimum_size = sezimal_to_niftimal(minimum_size)
    elif type(number).__name__ == 'Decimal':
        minimum_size = sezimal_to_niftimal(decimal_to_sezimal(minimum_size))

    number = validate_clean_niftimal(str(number))
    niftimal_places = validate_clean_niftimal(niftimal_places)
    minimum_size = validate_clean_niftimal(minimum_size)

    niftimal_places = int(sezimal_to_decimal(niftimal_to_sezimal(niftimal_places)))
    minimum_size = int(sezimal_to_decimal(niftimal_to_sezimal(minimum_size)))

    recurring: str = ''

    if '.' in number:
        integer, fraction = number.split('.')

        if mark_recurring_digits and fraction:
            fixed_part, recurring = _identify_recurring_digits(fraction[:_MAX_SEZIMAL_PRECISION_DECIMAL // 2], max_fraction_size=_MAX_SEZIMAL_PRECISION_DECIMAL // 2)

            if recurring:
                fraction = fixed_part + recurring

    else:
        integer, fraction = number, ''

    if not mark_recurring_digits:
        if niftimal_places:
            fraction = fraction.ljust(niftimal_places, '0')[:niftimal_places]
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
        formatted_number += niftimal_separator

        if mark_recurring_digits and recurring:
            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                p_recurring_notation or fraction_group_separator == '_',
                _FOUR_DIGITS_GROUP_FORMAT,
                fraction_group_separator
            )
        else:
            formatted_number += fraction

    if financial_digits:
        if dedicated_digits:
            formatted_number = default_niftimal_to_financial_dedicated_digits(formatted_number)
        else:
            formatted_number = default_niftimal_to_financial_digits(formatted_number)

    elif regularized_digits:
        if dedicated_digits:
            formatted_number = default_niftimal_to_regularized_dedicated_digits(formatted_number)
        else:
            formatted_number = default_niftimal_to_regularized_digits(formatted_number)

    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    return formatted_number


def _identify_recurring_digits(fraction: str, fixed_part: str = '', recurring_part: str = '', refining: bool = False, max_fraction_size: int = 48) -> tuple[str]:
    if (not refining) and ((not fraction) or (len(fraction) < max_fraction_size)):
        return fixed_part, recurring_part

    max_size = len(fraction)

    start = len(fixed_part)
    amount = len(recurring_part) + 1

    recurring_part = fraction[start:start + amount]

    max_repetitions = (max_size - start) // amount

    if max_repetitions <= 1:
        if len(fixed_part) >= max_size:
            return fixed_part, recurring_part

        fixed_part = fraction[0:len(fixed_part) + 1]
        recurring_part = ''

        return _identify_recurring_digits(fraction, fixed_part, recurring_part, max_fraction_size)

    test = fixed_part + recurring_part * max_repetitions

    if len(test) >= max_size:
        test = test[:max_size - 2]

    if fraction.startswith(test):
        #
        # Check if the recurring part is formed all by the same digit
        #
        if len(recurring_part) > 1 and (recurring_part[0] * len(recurring_part)) == recurring_part:
            recurring_part = recurring_part[0]

        #
        # Adjusts the last digit of the recurring part with the last digit of the fixed part
        #
        if fixed_part and fixed_part[-1] == recurring_part[-1]:
            recurring_part = fixed_part[-1] + recurring_part[:-1]
            fixed_part = fixed_part[:-1]

        return fixed_part, recurring_part

    return _identify_recurring_digits(fraction, fixed_part, recurring_part, max_fraction_size)


def _apply_recurring_mark(fraction: str, recurring: str, p_recurring_notation: bool = False, recurring_regrouping: re.Pattern = None, group_separator: str = '') -> str:
    if (not recurring) or (recurring == '0'):
        return fraction

    formatted_recurring = _apply_format(recurring.replace('_', '')[::-1], group_separator, recurring_regrouping)[::-1]

    if p_recurring_notation:
        if fraction and fraction != formatted_recurring:
            return fraction + '_p_' + formatted_recurring + '_p'
        else:
            return formatted_recurring + '_p'

    marked_fraction = fraction

    if fraction:
        marked_fraction += group_separator

    for c in formatted_recurring:
        fraction += c

        if c != group_separator and c != '_':
            fraction += _RECURRING_DIGITS_COMBINING_OVERLINE

    return marked_fraction
