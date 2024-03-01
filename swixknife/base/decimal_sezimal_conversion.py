
from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_decimal
from .context import sezimal_context


def decimal_to_sezimal(number: int | float | Decimal | str | Sezimal | SezimalInteger | SezimalFraction, sezimal_precision: int | str | SezimalInteger = None) -> str:
    if type(number).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        return str(number)

    number = validate_clean_decimal(str(number))

    if sezimal_precision is None:
        sezimal_precision = sezimal_context.sezimal_precision_decimal
    else:
        sezimal_precision = int(sezimal_precision)

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

    integer = _decimal_integer_to_sezimal(integer)
    sezimal_integer, sezimal_fraction = _decimal_fraction_to_sezimal(fraction, sezimal_precision)

    sezimal = _decimal_integer_to_sezimal(int(integer or '0', 6) + int(sezimal_integer or '0', 6))

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
    return sezimal or '0'


def _decimal_fraction_to_sezimal(fraction: str | Decimal, sezimal_precision: int = None) -> tuple[str, str]:
    if not fraction:
        return '0', ''

    decimal_precision = len(fraction)

    if sezimal_precision is None:
        sezimal_precision = _decimal_exponent_to_sezimal(getcontext().prec)

    fraction = Decimal('0.' + fraction)
    sezimal_integer = '0'
    sezimal_fraction = ''

    with localcontext() as context:
        context.prec = sezimal_precision * 2

        for i in range(sezimal_precision):
            fraction = fraction * 6

            if fraction == 6:
                sezimal_integer = '1'
                break

            digit = int(fraction % 10)
            sezimal_fraction += str(digit)
            fraction -= digit

            if fraction <= 0:
                break

    while sezimal_fraction.endswith('5555') \
        or sezimal_fraction.endswith('5554') \
        or sezimal_fraction.endswith('5553'):
        sezimal_fraction = sezimal_fraction[:-4]

        if sezimal_fraction.replace('5', '') == '':
            sezimal_integer = _decimal_integer_to_sezimal(int(sezimal_integer, 6) + 1)
            sezimal_fraction = '0'
            break

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

    return sezimal_integer, sezimal_fraction


def _decimal_exponent_to_sezimal(exponent: int) -> int:
    if exponent == 0:
        return 0

    exponent_ten = Decimal(10) ** exponent

    if exponent > 0:
        start = ((exponent // 3) * 4) + 4
        finish = 1
        step = -1
    else:
        start = ((exponent // 3) * 4) - 4
        finish = -1
        step = 1

    for i in range(start, finish, step):
        exponent_six = Decimal(6) ** i

        if exponent > 0:
            if exponent_six <= exponent_ten:
                return i + 1

        else:
            if exponent_six >= exponent_ten:
                return i - 1

    return 0
