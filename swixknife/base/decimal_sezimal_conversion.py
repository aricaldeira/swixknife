
from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_decimal


def decimal_to_sezimal(number: int | float | Decimal | str | Sezimal, sezimal_precision: int = None) -> str:
    if type(number).__name__ == 'Sezimal':
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

    while sezimal_fraction and sezimal_fraction[0] == '0':
        sezimal_fraction = sezimal_fraction[1:]

    sezimal_fraction = sezimal_fraction[::-1]

    if not sezimal_fraction:
        sezimal_fraction = '0'

    return sezimal_fraction
