
from typing import TypeVar

Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_dozenal, validate_clean_decimal
from .digit_conversion import dozenal_digits_to_letters


def dozenal_to_decimal(number: int | float | Decimal | str | Dozenal | DozenalInteger | DozenalFraction, decimal_precision: int = None) -> str:
    if type(number) == Decimal:
        return validate_clean_decimal(str(number))

    if type(number).__name__ in ('Dozenal', 'DozenalInteger', 'DozenalFraction'):
        decimal = number.decimal

        if decimal_precision is not None:
            with localcontext() as context:
                context.prec = decimal_precision
                decimal = round(decimal, decimal_precision)

        return validate_clean_decimal(str(decimal))

    number = validate_clean_dozenal(str(number))

    number = dozenal_digits_to_letters(number)

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

    decimal_integer, decimal_fraction = _dozenal_fraction_to_decimal(fraction, decimal_precision)
    decimal_integer = str(int(integer, 12) + int(decimal_integer or '0'))
    # decimal_integer = _dozenal_integer_to_decimal(integer)

    decimal = decimal_integer

    if decimal_fraction:
        decimal += '.' + decimal_fraction

    if negative:
        decimal = '-' + decimal

    return decimal


def _dozenal_integer_to_decimal(integer: str) -> str:
    if not integer:
        return ''

    decimal_integer = Decimal(0)
    integer = integer[::-1]

    i = 0
    for d in integer:
        decimal_integer += int(d, 12) * (Decimal('12') ** i)
        i += 1

    decimal_integer = validate_clean_decimal(decimal_integer)

    return decimal_integer


def _dozenal_fraction_to_decimal(fraction: str, decimal_precision: int = None) -> tuple[str, str]:
    if not fraction:
        return '', ''

    if decimal_precision is None:
        decimal_precision = getcontext().prec

    with localcontext() as context:
        # context.prec = decimal_precision * 2

        decimal_fraction = Decimal('0')

        i = -1
        for d in fraction:
            decimal_fraction += int(d, 12) * (Decimal('12') ** i)
            i -= 1

    decimal_fraction = validate_clean_decimal(decimal_fraction)
    decimal_integer, decimal_fraction = decimal_fraction.split('.')

    if len(decimal_fraction) > decimal_precision:
        decimal_fraction = decimal_fraction[:decimal_precision]

    while decimal_fraction.endswith('9999') \
        or decimal_fraction.endswith('9998') \
        or decimal_fraction.endswith('9997') \
        or decimal_fraction.endswith('9996') \
        or decimal_fraction.endswith('9995'):
        decimal_fraction = decimal_fraction[:-4]

        if decimal_fraction.replace('9', '') == '':
            decimal_integer = str(int(decimal_integer) + 1)
            decimal_fraction = '0'
            break

        size = len(decimal_fraction)
        decimal_fraction = str(int(decimal_fraction) + 1)
        decimal_fraction = decimal_fraction.zfill(size)

    return decimal_integer, decimal_fraction
