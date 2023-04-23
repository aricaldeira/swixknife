
from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_decimal


def decimal_to_sezimal(number: int | float | Decimal | str | Sezimal, sezimal_precision: int = None) -> str:
    if str(type(number)) == 'Sezimal':
        return str(number)

    number = validate_clean_decimal(str(number))

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

    sezimal_integer = _decimal_integer_to_sezimal(integer)
    sezimal_fraction = _decimal_fraction_to_sezimal(fraction, sezimal_precision)

    sezimal = sezimal_integer

    if sezimal_fraction:
        sezimal += '.' + sezimal_fraction

    if negative:
        sezimal = '-' + sezimal

    return sezimal


def _decimal_integer_to_sezimal(integer: int | str) -> str:
    integer = int(integer)
    sezimal = ''

    while integer:
        sezimal += str(integer % 6)
        integer //= 6

    sezimal = sezimal[::-1]
    return sezimal


def _decimal_fraction_to_sezimal(fraction: str, sezimal_precision: int = None) -> str:
    if not fraction:
        return ''

    decimal_precision = len(fraction)

    if sezimal_precision is None:
        # sezimal_precision = decimal_exponent_to_sezimal(decimal_precision * -1) * -1
        sezimal_precision = decimal_exponent_to_sezimal(getcontext().prec)

    fraction = Decimal('0.' + fraction)
    sezimal_fraction = ''

    with localcontext() as context:
        # context.prec = sezimal_precision * 2

        for i in range(sezimal_precision):
            fraction = fraction * 6
            digit = int(fraction % 10)
            sezimal_fraction += str(digit)
            fraction -= digit

            if fraction <= 0:
                break

    #
    # Let’s adjust for recurring 5s at the end of fractional parts
    #
    while sezimal_fraction.endswith('5555'):
        sezimal_fraction = sezimal_fraction[:-4]
        size = len(sezimal_fraction)
        sezimal_fraction = _decimal_integer_to_sezimal(int(sezimal_fraction, 6) + 1)
        sezimal_fraction = sezimal_fraction.zfill(size)

    #
    # Remove trailing zeroes
    #
    sezimal_fraction = sezimal_fraction[::-1]

    while sezimal_fraction[0] == '0':
        sezimal_fraction = sezimal_fraction[1:]

    sezimal_fraction = sezimal_fraction[::-1]

    return sezimal_fraction


def decimal_exponent_to_sezimal(exponent: int) -> int:
    if exponent == 0:
        return 0

    exponent_10 = Decimal(10) ** Decimal(exponent)

    if exponent > 0:
        start = 1
        finish = exponent * 3
        step = 1
    else:
        start = -1
        finish = exponent * 3
        step = -1

    for i in range(start, finish, step):
        exponent_6 = Decimal(6) ** Decimal(i)

        if exponent > 0:
            if exponent_6 >= exponent_10:
                return i

        else:
            if exponent_6 <= exponent_10:
                return i

    return 0


def decimal_exponent_to_sezimal_factor(decimal_exponent: int, sezimal_exponent: int = None, precision: int = None) -> Decimal:
    if sezimal_exponent is None:
        sezimal_exponent = decimal_exponent_to_sezimal(decimal_exponent)

    if precision is None:
        precision = getcontext().prec

    with localcontext() as context:
        context.prec = precision
        conversion = (Decimal(10) ** decimal_exponent) / (Decimal(6) ** sezimal_exponent)

    return conversion
