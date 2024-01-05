
from typing import TypeVar

Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_decimal
from .digit_conversion import dozenal_letters_to_digits


def decimal_to_dozenal(number: int | float | Decimal | str | Dozenal | DozenalInteger | DozenalFraction, dozenal_precision: int | str | DozenalInteger = None) -> str:
    if type(number).__name__ in ('Dozenal', 'DozenalInteger', 'DozenalFraction'):
        return str(number)

    number = validate_clean_decimal(str(number))

    if dozenal_precision is not None:
        dozenal_precision = int(dozenal_precision)

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

    integer = _decimal_integer_to_dozenal(integer)
    dozenal_integer, dozenal_fraction = _decimal_fraction_to_dozenal(fraction, dozenal_precision)

    dozenal = _decimal_integer_to_dozenal(int(integer or '0', 12) + int(dozenal_integer or '0', 12))

    if dozenal_fraction:
        dozenal += '.' + dozenal_fraction

    if negative:
        dozenal = '-' + dozenal

    dozenal = dozenal_letters_to_digits(dozenal)

    return dozenal


def _decimal_integer_to_dozenal(integer: int | str) -> str:
    integer = int(integer)
    dozenal = ''

    while integer:
        i = str(integer % 12)

        if i == '10':
            i = 'A'
        elif i == '11':
            i = 'B'

        dozenal += i

        integer //= 12

    dozenal = dozenal[::-1]
    return dozenal or '0'


def _decimal_fraction_to_dozenal(fraction: str | Decimal, dozenal_precision: int = None) -> tuple[str, str]:
    if not fraction:
        return '0', ''

    decimal_precision = len(fraction)

    if dozenal_precision is None:
        dozenal_precision = getcontext().prec

    fraction = Decimal('0.' + fraction)
    dozenal_integer = '0'
    dozenal_fraction = ''

    with localcontext() as context:
        # context.prec = dozenal_precision * 2

        for i in range(dozenal_precision):
            fraction = fraction * 12

            if fraction == 12:
                dozenal_integer = '1'
                break

            digit = int(fraction % 12)
            f = str(digit)

            if f == '10':
                f = 'A'
            elif f == '11':
                f = 'B'

            dozenal_fraction += f

            fraction -= digit

            if fraction <= 0:
                break

    while dozenal_fraction.endswith('BBBB') \
        or dozenal_fraction.endswith('BBBA') \
        or dozenal_fraction.endswith('BBB9') \
        or dozenal_fraction.endswith('BBB8') \
        or dozenal_fraction.endswith('BBB7') \
        or dozenal_fraction.endswith('BBB6'):
        dozenal_fraction = dozenal_fraction[:-4]

        if dozenal_fraction.replace('B', '') == '':
            dozenal_integer = _decimal_integer_to_dozenal(int(dozenal_integer, 12) + 1)
            dozenal_fraction = '0'
            break

        size = len(dozenal_fraction)
        dozenal_fraction = _decimal_integer_to_dozenal(int(dozenal_fraction, 12) + 1)
        dozenal_fraction = dozenal_fraction.zfill(size)

    #
    # Remove trailing zeroes
    #
    dozenal_fraction = dozenal_fraction[::-1]

    while dozenal_fraction and dozenal_fraction[0] == '0':
        dozenal_fraction = dozenal_fraction[1:]

    dozenal_fraction = dozenal_fraction[::-1]

    if not dozenal_fraction:
        dozenal_fraction = '0'

    return dozenal_integer, dozenal_fraction


def _decimal_exponent_to_dozenal(exponent: int) -> int:
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
        exponent_twelve = Decimal(12) ** i

        if exponent > 0:
            if exponent_twelve <= exponent_ten:
                return i + 1

        else:
            if exponent_twelve >= exponent_ten:
                return i - 1

    return 0
