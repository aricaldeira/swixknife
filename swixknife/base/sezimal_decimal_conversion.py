
from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_sezimal, validate_clean_decimal
from .context import sezimal_context


def sezimal_to_decimal(number: int | float | Decimal | str | Sezimal | SezimalInteger | SezimalFraction, decimal_precision: int = None) -> str:
    if type(number) == Decimal:
        return validate_clean_decimal(str(number))

    if type(number).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        decimal = number.decimal

        if decimal_precision is not None:
            with localcontext() as context:
                context.prec = decimal_precision * 2
                decimal = round(decimal, decimal_precision)

        return validate_clean_decimal(str(decimal))

    if decimal_precision is None:
        decimal_precision = sezimal_context.decimal_precision

    number = validate_clean_sezimal(str(number))

    if number.startswith('-'):
        negative = True
        number = number[1:]
    else:
        negative = False

    if '.' in number:
        integer, fraction = number.split('.')
    else:
        integer = number
        fraction = ''

    decimal_integer, decimal_fraction = _sezimal_fraction_to_decimal(fraction, decimal_precision)
    decimal_integer = str(int(integer, 6) + int(decimal_integer or '0'))
    # decimal_integer = _sezimal_integer_to_decimal(integer)

    decimal = decimal_integer

    if decimal_fraction:
        decimal += '.' + decimal_fraction

    if negative:
        decimal = '-' + decimal

    return decimal


def _sezimal_integer_to_decimal(integer: str) -> str:
    if not integer:
        return ''

    decimal_integer = Decimal(0)
    integer = integer[::-1]

    i = 0
    for d in integer:
        decimal_integer += int(d, 6) * (Decimal('6') ** i)
        i += 1

    decimal_integer = validate_clean_decimal(decimal_integer)

    return decimal_integer


def _sezimal_fraction_to_decimal(fraction: str, decimal_precision: int = None) -> tuple[str, str]:
    if not fraction:
        return '', ''

    if decimal_precision is None:
        decimal_precision = getcontext().prec

    with localcontext() as context:
        context.prec = decimal_precision * 2

        decimal_fraction = Decimal('0')

        i = -1
        for d in fraction:
            decimal_fraction += int(d, 6) * (Decimal('6') ** i)
            i -= 1

    with localcontext() as context:
        context.prec = decimal_precision * 2
        decimal_fraction = round(decimal_fraction, decimal_precision)

    decimal_fraction = validate_clean_decimal(decimal_fraction)
    decimal_integer, decimal_fraction = decimal_fraction.split('.')

    return decimal_integer, decimal_fraction
