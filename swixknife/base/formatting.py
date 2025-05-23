

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
SezimalDecimalUnit = TypeVar('SezimalDecimalUnit', bound='SezimalDecimalUnit')
Decimal = TypeVar('Decimal', bound='Decimal')
Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

import re
from .validation import validate_clean_sezimal, validate_clean_decimal, \
    validate_clean_niftimal, validate_clean_dozenal
from .decimal_sezimal_conversion import decimal_to_sezimal
from .sezimal_decimal_conversion import sezimal_to_decimal
from .sezimal_niftimal_conversion import sezimal_to_niftimal, niftimal_to_sezimal
from .sezimal_dozenal_conversion import sezimal_to_dozenal, dozenal_to_sezimal
from .dozenal_decimal_conversion import dozenal_to_decimal
from .digit_conversion import (
    default_to_sezimal_digits,
    default_to_numerator_digits, default_to_denominator_digits,
    default_to_dedicated_numerator_digits, default_to_dedicated_denominator_digits,
    default_niftimal_to_regularized_digits, default_niftimal_to_financial_digits,
    default_niftimal_to_niftimal_digits, default_niftimal_to_financial_sezimal_digits,
    dozenal_letters_to_digits, default_niftimal_to_letter_digits,
)
from .context import sezimal_context


PER_SYMBOLS = ('%', '‰', '‱', '󱹰', '󱹱', '󱹲', '󱹳', '󱹴', '󱹵')

SEPARATOR_COMMA = ','
SEPARATOR_DOT = '.'
SEPARATOR_UNDERSCORE = '_'
SEPARATOR_NARROW_NOBREAK_SPACE = '\u202f'
SEPARATOR_NARROW_SPACE = '\u2006'
SEPARATOR_NOBREAK_SPACE = '\u00a0'
SEPARATOR_HAIR_SPACE = '\u200a'
SEPARATOR_DOT_ABOVE = '\u02d9'
SEPARATOR_ZERO_WIDTH_JOINER = '\u200d'
SEPARATOR_ZERO_WIDTH_SPACE = '\u200b'
SEPARATOR_HIGH_VERTICAL_LINE = 'ˈ'
SEPARATOR_LOW_VERTICAL_LINE = 'ˌ'
SEPARATOR_MIDDLE_DOT = '·'
SEPARATOR_COMBINING_DOT_ABOVE_RIGHT = '\u0358'
SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT = '\u0315'
SEPARATOR_COMBINING_RING_ABOVE = '\u030a'
SEPARATOR_SHADARA = '󱹬'  # '\U000f1e6c'  # 󱹬
SEPARATOR_ARDA = '󱹭'  # '\U000f1e6d'  # 󱹭
SEPARATOR_WEDGE = '󱹮'  # '\U000f1e6e'  # 󱹮
SEPARATOR_REPEATING = '󱹯'  # '\U000f1e6f'  # 󱹯
SEPARATOR_DECIMAL_CURRENCY = '󱹶'  # '\U000f1e76'  # 󱹶
SEPARATOR_SEZIMAL_TIME = '󱹷'  # '\U000f1e77'  # 󱹷

TYPOGRAPHICAL_NEGATIVE = '\u2212'
TYPOGRAPHICAL_FRACTION_SLASH = '\u2044'

RECURRING_DIGITS_NOTATION_NONE = False
RECURRING_DIGITS_NOTATION_SIMPLE = True
RECURRING_DIGITS_NOTATION_WITH_ELLIPSIS = '...'
RECURRING_DIGITS_NOTATION_WITH_TYPOGRAPHICAL_ELLIPSIS = 'typographical_ellipsis'
RECURRING_DIGITS_NOTATION_WITH_TYPOGRAPHICAL_ELLIPSIS_CHARACTER = '…'
RECURRING_DIGITS_NOTATION_OVERLINE = 'ol'  # Classical
RECURRING_DIGITS_NOTATION_DOT_ABOVE = 'da'  # Some locales

_TWO_DIGITS_GROUP_FORMAT = re.compile(r'([0-9↊↋A-Z]{2})')
_THREE_DIGITS_GROUP_FORMAT = re.compile(r'([0-9↊↋A-Z]{3})')
_FOUR_DIGITS_GROUP_FORMAT = re.compile(r'([0-9↊↋A-Z]{4})')
_ARDA_DIGITS_GROUP_FORMAT = re.compile(r'([0-9↊↋A-Z]{6})')
_SHADARA_DIGITS_GROUP_FORMAT = re.compile(rf'([0-9↊↋A-Z{SEPARATOR_ARDA}]{{7}})')

_ONE_DIGIT = re.compile('([0-9↊↋A-Z]{1})')
_RECURRING_DIGITS_COMBINING_OVERLINE = '\u0305'
_RECURRING_DIGITS_COMBINING_DOT_ABOVE = '\u0307'


def sezimal_format(
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | SezimalDecimalUnit,
        sezimal_places: str | int | Decimal | Sezimal | SezimalInteger | SezimalFraction = 2,
        sezimal_separator: str = SEPARATOR_DOT,
        group_separator: str = SEPARATOR_UNDERSCORE,
        subgroup_separator: str = '',
        fraction_group_separator: str = SEPARATOR_UNDERSCORE,
        fraction_subgroup_separator: str = '',
        sezimal_digits: bool = False,
        sezimal_punctuation: bool = False,
        typographical_negative: bool = False,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        recurring_digits_notation: bool | str | int | Decimal | Sezimal | SezimalInteger = RECURRING_DIGITS_NOTATION_NONE,
        grouping_digits: int = 3,
        keep_original_aspect: bool = False,
    ) -> str:
    if type(number).__name__ == 'Decimal':
        number = decimal_to_sezimal(number)

    if type(sezimal_places).__name__ == 'Decimal':
        sezimal_places = decimal_to_sezimal(sezimal_places)

    if type(minimum_size).__name__ == 'Decimal':
        minimum_size = decimal_to_sezimal(minimum_size)

    if type(number).__name__ == 'SezimalFraction':
        number = number.sezimal

    if type(number).__name__ == 'SezimalDecimalUnit':
        number = number.sezimal

    if grouping_digits < 2 or grouping_digits > 4:
        if grouping_digits == 1:
            raise ValueError(f'Invalid grouping digits by each {grouping_digits} digit')
        else:
            raise ValueError(f'Invalid grouping digits by groups of {grouping_digits} digits')

    if type(recurring_digits_notation).__name__ in ('int', 'Sezimal', 'SezimalInteger'):
        recurring_digits_notation = int(str(recurring_digits_notation), 6)
    elif type(recurring_digits_notation).__name__ == 'Decimal':
        recurring_digits_notation = int(recurring_digits_notation)

    if grouping_digits == 4:
        group_format = _FOUR_DIGITS_GROUP_FORMAT
    elif grouping_digits == 3:
        group_format = _THREE_DIGITS_GROUP_FORMAT
    elif grouping_digits == 2:
        group_format = _TWO_DIGITS_GROUP_FORMAT

    sezimal_places = validate_clean_sezimal(sezimal_places)
    sezimal_places = int(sezimal_to_decimal(sezimal_places))

    filling_character = ' '

    if type(minimum_size) == str:
        if 'X' in minimum_size.upper():
            filling_character = minimum_size[0]
            minimum_size = len(minimum_size) - 1
        else:
            minimum_size = validate_clean_sezimal(minimum_size)
            minimum_size = int(sezimal_to_decimal(minimum_size))

    else:
        minimum_size = int(sezimal_to_decimal(minimum_size))

    if keep_original_aspect:
        number = str(number).replace('_', '')

        integer, fraction, recurring = '', '', ''

        if number.endswith('..'):
            number = number[:-2]
            recurring_digits_notation = RECURRING_DIGITS_NOTATION_SIMPLE
            recurring = '?'

        elif number.endswith('.'):
            number = number[:-1]
            fraction = '?'

        validated_number = validate_clean_sezimal(number)

        if '..' in number:
            recurring_digits_notation = RECURRING_DIGITS_NOTATION_SIMPLE
            integer, recurring = number.split('..')

            if '.' in integer:
                integer, fraction = integer.split('.')

        elif '.' in number:
            integer, fraction = number.split('.')
        else:
            integer = number

        sezimal_places = len(fraction + recurring)

    else:
        number = validate_clean_sezimal(str(number))
        recurring: str = ''

        if '.' in number:
            integer, fraction = number.split('.')

            if recurring_digits_notation and fraction:
                if type(recurring_digits_notation) == int:
                    max_fraction_size = recurring_digits_notation
                else:
                    max_fraction_size = sezimal_context.sezimal_precision_decimal

                fixed_part, recurring = _identify_recurring_digits(fraction[:sezimal_context.sezimal_precision_decimal], max_fraction_size=max_fraction_size)

                if not recurring:
                    fixed_part, recurring = _identify_recurring_digits(fraction[:sezimal_context.sezimal_precision_decimal - 1], max_fraction_size=max_fraction_size - 1)

                if recurring == '0':
                    recurring = ''
                    fraction = fixed_part

                if recurring:
                    #
                    # Let’s check if we limit the size of the recurring notation
                    #
                    if type(recurring_digits_notation) == int:
                        if len(fixed_part + recurring) < recurring_digits_notation:
                            fraction = fixed_part
                        else:
                            recurring = ''

                    else:
                        fraction = fixed_part

        else:
            integer, fraction = number, ''

    if not recurring_digits_notation:
        if sezimal_places:
            fraction = fraction.ljust(sezimal_places, '0')[:sezimal_places]
        else:
            fraction = ''

    if group_separator:
        if sezimal_punctuation:
            integer = _apply_sezimal_punctuation(integer, False)
        else:
            integer = _apply_format(integer, group_separator, group_format, False)

        if subgroup_separator:
            integer = _apply_format(integer, subgroup_separator, _TWO_DIGITS_GROUP_FORMAT, False)
            integer = integer.replace(subgroup_separator + group_separator, group_separator)
            integer = integer.replace(group_separator + subgroup_separator, group_separator)

        if minimum_size > 0:
            integer = integer.rjust(minimum_size, filling_character)

    formatted_number = integer

    if recurring_digits_notation:
        if recurring:
            if fraction and fraction_group_separator:
                if sezimal_punctuation:
                    fraction = _apply_sezimal_punctuation(fraction, False)
                else:
                    fraction = _apply_format(fraction, fraction_group_separator, group_format)

                if fraction_subgroup_separator:
                    fraction = _apply_format(fraction, fraction_subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)
                    fraction = fraction.replace(fraction_subgroup_separator + fraction_group_separator, fraction_group_separator)
                    fraction = fraction.replace(fraction_group_separator + fraction_subgroup_separator, fraction_group_separator)

            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                recurring_digits_notation,
                group_format,
                SEPARATOR_WEDGE if sezimal_punctuation else sezimal_separator ,
                fraction_group_separator,
                keep_original_aspect,
            )
            fraction = ''

        else:
            fraction = fraction.rstrip('0')

    if fraction:
        if fraction_group_separator:
            if sezimal_punctuation:
                fraction = _apply_sezimal_punctuation(fraction, False)
            else:
                fraction = _apply_format(fraction, fraction_group_separator, group_format)

            if fraction_subgroup_separator:
                fraction = _apply_format(fraction, fraction_subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)
                fraction = fraction.replace(fraction_subgroup_separator + fraction_group_separator, fraction_group_separator)
                fraction = fraction.replace(fraction_group_separator + fraction_subgroup_separator, fraction_group_separator)

        if sezimal_punctuation:
            formatted_number += SEPARATOR_WEDGE
        else:
            formatted_number += sezimal_separator

        formatted_number += fraction

    if sezimal_digits:
        formatted_number = default_to_sezimal_digits(formatted_number)

    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    if keep_original_aspect:
        formatted_number = formatted_number.replace('?', '')

    return formatted_number


def _apply_sezimal_punctuation(number: str, is_fraction: bool = True, arda_shadara: bool = True) -> str:
    is_negative = number[0] in '-−⁻₋'

    if is_negative:
        number = number[1:]

    if is_fraction:
        number = number[::-1]

    if len(number) <= 3:
        formatted_number = number
    elif arda_shadara:
        formatted_number = _apply_format(number[:-3], SEPARATOR_ARDA, _ARDA_DIGITS_GROUP_FORMAT, False) + SEPARATOR_ARDA + number[-3:]
        formatted_number = _apply_format(formatted_number, SEPARATOR_SHADARA, _SHADARA_DIGITS_GROUP_FORMAT, False)
    else:
        formatted_number = _apply_format(number, SEPARATOR_SHADARA, _THREE_DIGITS_GROUP_FORMAT, False)

    if is_fraction:
        formatted_number = formatted_number[::-1]

    if is_negative:
        formatted_number = '-' + formatted_number

    return formatted_number


def _apply_format(number: str, separator: str, format_pattern: re.Pattern, is_fraction: bool = True) -> str:
    is_negative = number[0] in '-−⁻₋'

    if is_negative:
        number = number[1:]

    if is_fraction:
        number = number[::-1]

    if format_pattern == _THREE_DIGITS_GROUP_FORMAT and len(number) <= 3:
        formatted_number = number
    else:
        formatted_number = number[::-1]
        parts = re.split(format_pattern, formatted_number)
        parts = list(filter(bool, parts))
        formatted_number = separator.join(parts)
        formatted_number = formatted_number[::-1]

    if is_fraction:
        formatted_number = formatted_number[::-1]

    if is_negative:
        formatted_number = '-' + formatted_number

    return formatted_number


def _finish_formatting(formatted_number: str, prefix: str, suffix: str, positive_format: str, negative_format: str, typographical_negative: bool) -> str:
    if prefix:
        #
        # ISO standard suggests the use of the NNBSP
        # to separate the unit/prefix/sufix from the value
        #
        prefix += SEPARATOR_NARROW_NOBREAK_SPACE

    if suffix:
        if suffix[0] in ('π', 'τ'):
            #
            # Avoids mixing π and τ with fraction values
            #
            suffix = SEPARATOR_ZERO_WIDTH_SPACE + suffix
        elif suffix not in PER_SYMBOLS:
            #
            # ISO standard suggests the use of the NNBSP
            # to separate the unit/prefix/sufix from the value
            #
            suffix = SEPARATOR_NARROW_NOBREAK_SPACE + suffix

    if formatted_number[0] != '-':
        formatted_number = positive_format.format(prefix=prefix, value=formatted_number, suffix=suffix)
    else:
        formatted_number = negative_format.format(prefix=prefix, value=formatted_number[1:], suffix=suffix)

        if typographical_negative:
            formatted_number = TYPOGRAPHICAL_NEGATIVE + formatted_number[1:]

    return formatted_number


def sezimal_format_fraction(numerator: str | int | float | Decimal | Sezimal | SezimalInteger, denominator: str | int | float | Decimal | Sezimal | SezimalInteger, sezimal_digits: bool = False) -> str:
    if type(numerator).__name__ == 'Decimal':
        numerator = decimal_to_sezimal(numerator)

    numerator = validate_clean_sezimal(str(numerator))

    if type(denominator).__name__ == 'Decimal':
        denominator = decimal_to_sezimal(denominator)

    denominator = validate_clean_sezimal(str(denominator))

    if sezimal_digits:
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
        recurring_digits_notation: bool | str | int | Decimal | Sezimal | SezimalInteger = RECURRING_DIGITS_NOTATION_NONE,
        keep_original_aspect: bool = False,
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

    decimal_places = int(validate_clean_decimal(str(decimal_places)))
    minimum_size = int(validate_clean_decimal(str(minimum_size)))

    if keep_original_aspect:
        number = str(number).replace('_', '')

        integer, fraction, recurring = '', '', ''

        if number.endswith('..'):
            number = number[:-2]
            recurring_digits_notation = RECURRING_DIGITS_NOTATION_SIMPLE
            recurring = '?'

        elif number.endswith('.'):
            number = number[:-1]
            fraction = '?'

        validated_number = validate_clean_decimal(number)

        if '..' in number:
            recurring_digits_notation = RECURRING_DIGITS_NOTATION_SIMPLE
            integer, recurring = number.split('..')

            if '.' in integer:
                integer, fraction = integer.split('.')

        elif '.' in number:
            integer, fraction = number.split('.')
        else:
            integer = number

        decimal_places = len(fraction + recurring)

    else:
        number = validate_clean_decimal(str(number))

        if type(recurring_digits_notation).__name__ in ('Decimal', 'int', 'Sezimal', 'SezimalInteger'):
            recurring_digits_notation = int(recurring_digits_notation)

        recurring: str = ''

        if '.' in number:
            integer, fraction = number.split('.')

            if recurring_digits_notation and fraction:
                if type(recurring_digits_notation) == int:
                    max_fraction_size = recurring_digits_notation
                else:
                    max_fraction_size = sezimal_context.decimal_precision

                fixed_part, recurring = _identify_recurring_digits(fraction[:sezimal_context.decimal_precision], max_fraction_size=max_fraction_size)

                if recurring:
                    #
                    # Let’s check if we limit the size of the recurring notation
                    #
                    if type(recurring_digits_notation) == int:
                        if len(fixed_part + recurring) < recurring_digits_notation:
                            fraction = fixed_part
                        else:
                            recurring = ''

                    else:
                        fraction = fixed_part

        else:
            integer, fraction = number, ''

    if not recurring_digits_notation:
        if decimal_places:
            fraction = fraction.ljust(decimal_places, '0')[:decimal_places]
        else:
            fraction = ''

    if group_separator:
        if minimum_size > 0:
            integer = integer.rjust(minimum_size, '0')

        if wan_man_van_grouping:
            integer = _apply_format(integer, group_separator, _FOUR_DIGITS_GROUP_FORMAT, False)

        elif lakh_crore_grouping and len(integer) > 3:
            integer = _apply_format(integer[:-3], group_separator, _TWO_DIGITS_GROUP_FORMAT, False) + group_separator + integer[-3:]

        else:
            integer = _apply_format(integer, group_separator, _THREE_DIGITS_GROUP_FORMAT, False)

    formatted_number = integer

    if recurring_digits_notation:
        if recurring:
            if fraction and fraction_group_separator:
                if wan_man_van_grouping:
                    fraction = _apply_format(fraction, fraction_group_separator, _FOUR_DIGITS_GROUP_FORMAT)

                elif lakh_crore_grouping and len(fraction) > 3:
                    fraction = fraction[0:3] + fraction_group_separator + _apply_format(fraction[3:], fraction_group_separator, _TWO_DIGITS_GROUP_FORMAT)

                else:
                    fraction = _apply_format(fraction, fraction_group_separator, _THREE_DIGITS_GROUP_FORMAT)

            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                recurring_digits_notation,
                _THREE_DIGITS_GROUP_FORMAT,
                decimal_separator,
                fraction_group_separator,
                keep_original_aspect,
            )
            fraction = ''

        else:
            fraction = fraction.rstrip('0')

    if fraction:
        if fraction_group_separator:
            if wan_man_van_grouping:
                fraction = _apply_format(fraction, fraction_group_separator, _FOUR_DIGITS_GROUP_FORMAT)

            elif lakh_crore_grouping and len(fraction) > 3:
                fraction = fraction[0:3] + fraction_group_separator + _apply_format(fraction[3:], fraction_group_separator, _TWO_DIGITS_GROUP_FORMAT)

            else:
                fraction = _apply_format(fraction, fraction_group_separator, _THREE_DIGITS_GROUP_FORMAT)

        formatted_number += decimal_separator
        formatted_number += fraction

    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    if keep_original_aspect:
        formatted_number = formatted_number.replace('?', '')

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
        recurring_digits_notation: bool | str = RECURRING_DIGITS_NOTATION_NONE,
    ) -> str:
    if type(number).__name__ in ('str', 'Dozenal', 'DozenalInteger'):
        number = dozenal_letters_to_digits(str(number))
    elif type(number).__name__ == 'DozenalFraction':
        number = dozenal_letters_to_digits(str(number.dozenal))
    else:
        number = sezimal_to_dozenal(number)

    if type(dozenal_places).__name__ in ('str', 'Dozenal', 'DozenalInteger'):
        dozenal_places = dozenal_letters_to_digits(str(dozenal_places))
    else:
        dozenal_places = sezimal_to_dozenal(dozenal_places)

    if type(minimum_size).__name__ in ('str', 'Dozenal', 'DozenalInteger'):
        minimum_size = dozenal_letters_to_digits(str(minimum_size))
    else:
        minimum_size = sezimal_to_dozenal(minimum_size)

    number = validate_clean_dozenal(str(number))
    dozenal_places = validate_clean_dozenal(dozenal_places)
    minimum_size = validate_clean_dozenal(minimum_size)

    dozenal_places = int(dozenal_to_decimal(dozenal_places))
    minimum_size = int(dozenal_to_decimal(minimum_size))

    if type(recurring_digits_notation).__name__ in ('Sezimal', 'SezimalInteger'):
        recurring_digits_notation = int(str(recurring_digits_notation), 6)
    elif type(recurring_digits_notation).__name__ in ('int', 'Decimal'):
        recurring_digits_notation = int(recurring_digits_notation)
    elif type(recurring_digits_notation).__name__ in ('Dozenal', 'DozenalInteger'):
        recurring_digits_notation = int(dozenal_to_decimal(recurring_digits_notation))

    recurring: str = ''

    if '.' in number:
        integer, fraction = number.split('.')

        if recurring_digits_notation and fraction:
            if type(recurring_digits_notation) == int:
                max_fraction_size = recurring_digits_notation
            else:
                max_fraction_size = sezimal_context.dozenal_precision_decimal

            fixed_part, recurring = _identify_recurring_digits(fraction[:sezimal_context.dozenal_precision_decimal], max_fraction_size=max_fraction_size)

            if recurring:
                #
                # Let’s check if we limit the size of the recurring notation
                #
                if type(recurring_digits_notation) == int:
                    if len(fixed_part + recurring) < recurring_digits_notation:
                        fraction = fixed_part
                    else:
                        recurring = ''

                else:
                    fraction = fixed_part

    else:
        integer, fraction = number, ''

    if not recurring_digits_notation:
        if dozenal_places:
            fraction = fraction.ljust(dozenal_places, '0')[:dozenal_places]
        else:
            fraction = ''

    if group_separator:
        if minimum_size > 0:
            integer = integer.rjust(minimum_size, '0')

        integer = _apply_format(integer, group_separator, _THREE_DIGITS_GROUP_FORMAT, False)

        if subgroup_separator:
            integer = _apply_format(integer, subgroup_separator, _TWO_DIGITS_GROUP_FORMAT, False)
            integer = integer.replace(subgroup_separator + group_separator, group_separator)
            integer = integer.replace(group_separator + subgroup_separator, group_separator)

    formatted_number = integer

    if recurring_digits_notation:
        if recurring:
            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                recurring_digits_notation,
                _THREE_DIGITS_GROUP_FORMAT,
                dozenal_separator,
                fraction_group_separator,
            )
            fraction = ''

        else:
            fraction = fraction.rstrip('0')

    if fraction:
        if fraction_group_separator:
            fraction = _apply_format(fraction, fraction_group_separator, _THREE_DIGITS_GROUP_FORMAT)

            if fraction_subgroup_separator:
                fraction = _apply_format(fraction, fraction_subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)
                fraction = fraction.replace(fraction_subgroup_separator + fraction_group_separator, fraction_group_separator)
                fraction = fraction.replace(fraction_group_separator + fraction_subgroup_separator, fraction_group_separator)

        formatted_number += dozenal_separator
        formatted_number += fraction

    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    return formatted_number


def niftimal_format(
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | SezimalDecimalUnit,
        niftimal_places: str | int | Decimal | Sezimal | SezimalInteger | SezimalFraction = 2,
        niftimal_separator: str = SEPARATOR_DOT,
        group_separator: str = SEPARATOR_UNDERSCORE,
        subgroup_separator: str = '',
        fraction_group_separator: str = SEPARATOR_UNDERSCORE,
        fraction_subgroup_separator: str = '',
        regularized_digits: bool = True,
        regularized_letter_digits: bool = False,
        sezimal_digits: bool = False,
        sezimal_punctuation: bool = False,
        financial_digits: bool = False,
        typographical_negative: bool = False,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        recurring_digits_notation: bool | str = RECURRING_DIGITS_NOTATION_NONE,
        grouping_digits: int = 3,
        keep_original_aspect: bool = False,
    ) -> str:
    if type(number).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        number = sezimal_to_niftimal(number)
    elif type(number).__name__ == 'Decimal':
        number = sezimal_to_niftimal(decimal_to_sezimal(number))
    elif type(number).__name__ == 'SezimalDecimalUnit':
        number = sezimal_to_niftimal(number.sezimal)

    if type(niftimal_places).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        niftimal_places = sezimal_to_niftimal(niftimal_places)
    elif type(niftimal_places).__name__ == 'Decimal':
        niftimal_places = sezimal_to_niftimal(decimal_to_sezimal(niftimal_places))

    if type(minimum_size).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        minimum_size = sezimal_to_niftimal(minimum_size)
    elif type(number).__name__ == 'Decimal':
        minimum_size = sezimal_to_niftimal(decimal_to_sezimal(minimum_size))

    if grouping_digits < 2 or grouping_digits > 4:
        if grouping_digits == 1:
            raise ValueError(f'Invalid grouping digits by each {grouping_digits} digit')
        else:
            raise ValueError(f'Invalid grouping digits by groups of {grouping_digits} digits')

    if grouping_digits == 4:
        group_format = _FOUR_DIGITS_GROUP_FORMAT
    elif grouping_digits == 3:
        group_format = _THREE_DIGITS_GROUP_FORMAT
    elif grouping_digits == 2:
        group_format = _TWO_DIGITS_GROUP_FORMAT

    niftimal_places = validate_clean_niftimal(niftimal_places)
    minimum_size = validate_clean_niftimal(minimum_size)

    niftimal_places = int(sezimal_to_decimal(niftimal_to_sezimal(niftimal_places)))
    minimum_size = int(sezimal_to_decimal(niftimal_to_sezimal(minimum_size)))

    if keep_original_aspect:
        number = str(number).replace('_', '')

        integer, fraction, recurring = '', '', ''

        if number.endswith('..'):
            number = number[:-2]
            recurring_digits_notation = RECURRING_DIGITS_NOTATION_SIMPLE
            recurring = '?'

        elif number.endswith('.'):
            number = number[:-1]
            fraction = '?'

        validated_number = validate_clean_niftimal(number)

        if '..' in number:
            recurring_digits_notation = RECURRING_DIGITS_NOTATION_SIMPLE
            integer, recurring = number.split('..')

            if '.' in integer:
                integer, fraction = integer.split('.')

        elif '.' in number:
            integer, fraction = number.split('.')
        else:
            integer = number

        niftimal_places = len(fraction + recurring)

    else:
        number = validate_clean_niftimal(str(number))
        recurring: str = ''

        if '.' in number:
            integer, fraction = number.split('.')

            if recurring_digits_notation and fraction:
                if type(recurring_digits_notation) == int:
                    max_fraction_size = recurring_digits_notation
                else:
                    max_fraction_size = sezimal_context.sezimal_precision_decimal // 2

                fixed_part, recurring = _identify_recurring_digits(fraction[:sezimal_context.sezimal_precision_decimal // 2], max_fraction_size=max_fraction_size)

                if recurring:
                    #
                    # Let’s check if we limit the size of the recurring notation
                    #
                    if type(recurring_digits_notation) == int:
                        if len(fixed_part + recurring) < recurring_digits_notation:
                            fraction = fixed_part
                        else:
                            recurring = ''

                    else:
                        fraction = fixed_part

        else:
            integer, fraction = number, ''

    if not recurring_digits_notation:
        if niftimal_places:
            fraction = fraction.ljust(niftimal_places, '0')[:niftimal_places]
        else:
            fraction = ''

    if group_separator:
        if minimum_size > 0:
            integer = integer.rjust(minimum_size, '0')

        if sezimal_punctuation:
            integer = _apply_sezimal_punctuation(integer, False, arda_shadara=False)
        else:
            integer = _apply_format(integer, group_separator, group_format, False)

        if subgroup_separator:
            integer = _apply_format(integer, subgroup_separator, _TWO_DIGITS_GROUP_FORMAT, False)
            integer = integer.replace(subgroup_separator + group_separator, group_separator)
            integer = integer.replace(group_separator + subgroup_separator, group_separator)

    formatted_number = integer

    if recurring_digits_notation:
        if recurring:
            if fraction and fraction_group_separator:
                if sezimal_punctuation:
                    fraction = _apply_sezimal_punctuation(fraction, arda_shadara=False)
                else:
                    fraction = _apply_format(fraction, fraction_group_separator, group_format)

                if fraction_subgroup_separator:
                    fraction = _apply_format(fraction, fraction_subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)
                    fraction = fraction.replace(fraction_subgroup_separator + fraction_group_separator, fraction_group_separator)
                    fraction = fraction.replace(fraction_group_separator + fraction_subgroup_separator, fraction_group_separator)

            formatted_number += _apply_recurring_mark(
                fraction, recurring,
                recurring_digits_notation,
                group_format,
                SEPARATOR_WEDGE if sezimal_punctuation else niftimal_separator,
                fraction_group_separator
            )
            fraction = ''

        else:
            fraction = fraction.rstrip('0')

    if fraction:
        if fraction_group_separator:
            if sezimal_punctuation:
                fraction = _apply_sezimal_punctuation(fraction, arda_shadara=False)
            else:
                fraction = _apply_format(fraction, fraction_group_separator, group_format)

            if fraction_subgroup_separator:
                fraction = _apply_format(fraction, fraction_subgroup_separator, _TWO_DIGITS_GROUP_FORMAT)
                fraction = fraction.replace(fraction_subgroup_separator + fraction_group_separator, fraction_group_separator)
                fraction = fraction.replace(fraction_group_separator + fraction_subgroup_separator, fraction_group_separator)

        if sezimal_punctuation:
            formatted_number += SEPARATOR_WEDGE
        else:
            formatted_number += niftimal_separator

        formatted_number += fraction

    if financial_digits:
        if sezimal_digits:
            formatted_number = default_niftimal_to_financial_sezimal_digits(formatted_number)
        else:
            formatted_number = default_niftimal_to_financial_digits(formatted_number)

    elif regularized_digits or regularized_letter_digits:
        if regularized_letter_digits:
            formatted_number = default_niftimal_to_letter_digits(formatted_number)
        elif sezimal_digits:
            formatted_number = default_niftimal_to_niftimal_digits(formatted_number)
        else:
            formatted_number = default_niftimal_to_regularized_digits(formatted_number)


    formatted_number = _finish_formatting(
        formatted_number, prefix, suffix,
        positive_format, negative_format, typographical_negative,
    )

    return formatted_number


def _identify_recurring_digits(fraction: str, fixed_part: str = '', recurring_part: str = '', max_fraction_size: int = 48, refining: bool = False) -> tuple[str]:
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

        return _identify_recurring_digits(fraction, fixed_part, recurring_part, max_fraction_size, True)

    test = fixed_part + recurring_part * max_repetitions

    if len(test) >= max_size:
        test = test[:max_size - 2]

    if fraction.find(test) == 0:
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

    return _identify_recurring_digits(fraction, fixed_part, recurring_part, max_fraction_size, True)


def _apply_recurring_mark(
    fraction: str, recurring: str,
    recurring_digits_notation: bool | str = RECURRING_DIGITS_NOTATION_SIMPLE,
    recurring_regrouping: re.Pattern = None,
    fraction_separator: str = '.',
    group_separator: str = '',
    keep_original_aspect: bool = False,
) -> str:
    if not keep_original_aspect:
        if (not recurring) or (recurring == '0'):
            return fraction_separator + fraction

    if fraction_separator == SEPARATOR_WEDGE:
        formatted_recurring = _apply_sezimal_punctuation(recurring.replace('_', ''))
    else:
        formatted_recurring = _apply_format(recurring.replace('_', ''), group_separator, recurring_regrouping)

    if recurring_digits_notation == RECURRING_DIGITS_NOTATION_OVERLINE:
        if fraction and fraction != formatted_recurring:
            marked_fraction = fraction + group_separator
        else:
            marked_fraction = ''

        for c in formatted_recurring:
            marked_fraction += c

            if c != group_separator and c != '_':
                marked_fraction += _RECURRING_DIGITS_COMBINING_OVERLINE

        return fraction_separator + marked_fraction

    elif recurring_digits_notation == RECURRING_DIGITS_NOTATION_DOT_ABOVE:
        original_formatted_recurring = formatted_recurring

        if len(formatted_recurring) > 1:
            fr = formatted_recurring[0] + _RECURRING_DIGITS_COMBINING_DOT_ABOVE
            fr += formatted_recurring[1:-1]
            fr += formatted_recurring[-1] + _RECURRING_DIGITS_COMBINING_DOT_ABOVE
            formatted_recurring = fr
        else:
            formatted_recurring += _RECURRING_DIGITS_COMBINING_DOT_ABOVE

        if fraction and fraction != original_formatted_recurring:
            marked_fraction = fraction + group_separator + formatted_recurring
        else:
            marked_fraction = formatted_recurring

        return fraction_separator + marked_fraction

    if fraction_separator == SEPARATOR_WEDGE:
        recurring_marker = SEPARATOR_REPEATING
    else:
        recurring_marker = fraction_separator + fraction_separator

    if fraction and fraction != formatted_recurring:
        marked_fraction = fraction_separator + fraction + recurring_marker + formatted_recurring
    else:
        marked_fraction = recurring_marker + formatted_recurring

    if marked_fraction and marked_fraction[-1] == '0':
        if recurring_digits_notation == RECURRING_DIGITS_NOTATION_WITH_ELLIPSIS:
            marked_fraction += '...'
        elif recurring_digits_notation == RECURRING_DIGITS_NOTATION_WITH_TYPOGRAPHICAL_ELLIPSIS \
            or recurring_digits_notation == RECURRING_DIGITS_NOTATION_WITH_TYPOGRAPHICAL_ELLIPSIS_CHARACTER:
            marked_fraction += '…'

    return marked_fraction
