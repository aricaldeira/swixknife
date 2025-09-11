
#
# This is the base functions for the Sezimal classes and functions;
# All functions in here explicit don’t use the Sezimal classes,
# using only strings or indirect methods for converting, validating etc.
#

from .validation import (
    validate_clean_sezimal,
    validate_clean_decimal,
    validate_clean_niftimal,
    validate_clean_dozenal,
)
from .context import sezimal_context, SezimalContext
from .decimal_sezimal_conversion import decimal_to_sezimal
from .sezimal_decimal_conversion import sezimal_to_decimal
from .sezimal_niftimal_conversion import sezimal_to_niftimal, niftimal_to_sezimal
from .sezimal_dozenal_conversion import sezimal_to_dozenal, dozenal_to_sezimal
from .decimal_dozenal_conversion import decimal_to_dozenal
from .dozenal_decimal_conversion import dozenal_to_decimal
from .digit_conversion import (
    default_to_sezimal_digits, default_niftimal_to_sezimal_digits,
    default_niftimal_to_regularized_digits, default_niftimal_to_niftimal_digits,
    default_niftimal_to_financial_digits, default_niftimal_to_financial_sezimal_digits,
    sezimal_to_default_digits, dedicated_niftimal_to_default_digits,
    default_to_numerator_digits, default_to_denominator_digits,
    sezimal_to_numerator_digits, sezimal_to_denominator_digits,
    default_to_dedicated_numerator_digits, default_to_dedicated_denominator_digits,
    sezimal_to_default_numerator_digits, sezimal_to_default_denominator_digits,
    dozenal_letters_to_digits, dozenal_digits_to_letters,
    default_niftimal_to_letter_digits,
    default_niftimal_to_domino,
)
from .formatting import (
    sezimal_format, sezimal_format_fraction,
    decimal_format, dozenal_format, niftimal_format,
    SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_UNDERSCORE,
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_NOBREAK_SPACE, SEPARATOR_HAIR_SPACE,
    SEPARATOR_DOT_ABOVE, SEPARATOR_ZERO_WIDTH_JOINER,
    SEPARATOR_HIGH_VERTICAL_LINE, SEPARATOR_LOW_VERTICAL_LINE,
    SEPARATOR_MIDDLE_DOT, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT,
    SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT,
    SEPARATOR_COMBINING_RING_ABOVE,
    RECURRING_DIGITS_NOTATION_NONE,
    RECURRING_DIGITS_NOTATION_SIMPLE,
    RECURRING_DIGITS_NOTATION_WITH_ELLIPSIS,
    RECURRING_DIGITS_NOTATION_WITH_TYPOGRAPHICAL_ELLIPSIS,
    RECURRING_DIGITS_NOTATION_OVERLINE,
    RECURRING_DIGITS_NOTATION_DOT_ABOVE,
    SEPARATOR_SHADARA, SEPARATOR_ARDA,
    SEPARATOR_WEDGE, SEPARATOR_REPEATING,
    SEPARATOR_DECIMAL_CURRENCY,
)
