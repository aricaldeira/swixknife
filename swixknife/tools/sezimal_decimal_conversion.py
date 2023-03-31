
from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_sezimal


def sezimal_to_decimal(number: int | float | Decimal | str | Sezimal, decimal_precision: int = None) -> str:
    if type(number) == Decimal:
        return str(number)

    if str(type(number)) == 'Sezimal':
        return str(number.decimal)

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

    decimal_integer = str(int(integer, 6))
    decimal_fraction = _sezimal_fraction_to_decimal(fraction, decimal_precision)

    decimal = decimal_integer

    if decimal_fraction:
        decimal += '.' + decimal_fraction

    if negative:
        decimal = '-' + decimal

    return decimal


def _sezimal_fraction_to_decimal(fraction: str, decimal_precision: int = None) -> str:
    if not fraction:
        return ''

    sezimal_precision = len(fraction)

    if decimal_precision is None:
        # decimal_precision = sezimal_exponent_to_decimal(sezimal_precision * -1) * -1
        decimal_precision = getcontext().prec

    with localcontext() as context:
        context.prec = decimal_precision * 2
        decimal_fraction = Decimal(int(fraction, 6))
        decimal_fraction *= Decimal(1) / (Decimal(6) ** Decimal(sezimal_precision))
        decimal_fraction *= Decimal(10) ** decimal_precision

    decimal_fraction = str(int(decimal_fraction))

    return decimal_fraction


def sezimal_exponent_to_decimal(exponent: int) -> int:
    if exponent == 0:
        return 0

    exponent_6 = Decimal(6) ** Decimal(exponent)

    if exponent > 0:
        start = 1
        finish = exponent * 3
        step = 1
    else:
        start = -1
        finish = exponent * 3
        step = -1

    for i in range(start, finish, step):
        exponent_10 = Decimal(10) ** Decimal(i)

        if exponent > 0:
            if exponent_10 >= exponent_6:
                return i

        else:
            if exponent_10 <= exponent_6:
                return i

    return 0
