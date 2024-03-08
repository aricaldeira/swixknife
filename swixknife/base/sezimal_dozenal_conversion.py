
from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')


from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_sezimal, validate_clean_dozenal, validate_clean_decimal
from .sezimal_decimal_conversion import sezimal_to_decimal
from .decimal_sezimal_conversion import decimal_to_sezimal
from .context import sezimal_context


DOZENAL_DIGITS = '0123456789↊↋'


def sezimal_to_dozenal(number: int | float | Decimal | str | Sezimal | SezimalInteger | SezimalFraction, dozenal_precision: int = None) -> str:
    if type(number) == Decimal:
        number = validate_clean_decimal(str(number))
    else:
        number = sezimal_to_decimal(number)

    if dozenal_precision is None:
        dozenal_precision = sezimal_context.dozenal_precision_decimal

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

    dozenal_integer = _decimal_integer_to_dozenal(integer)
    dozenal_fraction = _decimal_fraction_to_dozenal(fraction, dozenal_precision)

    dozenal = dozenal_integer

    if dozenal_fraction:
        dozenal += '.' + dozenal_fraction

    if negative:
        dozenal = '-' + dozenal

    return dozenal


def _decimal_integer_to_dozenal(integer: str | int) -> str:
    if not integer:
        return ''

    dozenal = []

    integer = int(integer)

    while integer:
        dozenal.append(DOZENAL_DIGITS[integer % 12])
        integer //= 12

    return ''.join(reversed(dozenal or '0'))


def _decimal_fraction_to_dozenal(fraction: str | Decimal, dozenal_precision: int = None) -> str:
    if not fraction:
        return ''

    decimal_precision = len(fraction)

    if dozenal_precision is None:
        dozenal_precision = 36

    fraction = Decimal('0.' + fraction)
    dozenal_fraction = ''

    with localcontext() as context:
        # context.prec = dozenal_precision * 2

        for i in range(dozenal_precision):
            fraction *= 12
            digit = int(fraction % 12)
            dozenal_fraction += DOZENAL_DIGITS[digit]
            fraction -= digit

            if fraction <= 0:
                break

    #
    # Let’s adjust for recurring ↋s at the end of fractional parts
    #
    while dozenal_fraction.endswith('↋↋↋)'):
        dozenal_fraction = dozenal_fraction[:-4]
        size = len(dozenal_fraction)
        dozenal_fraction = _decimal_integer_to_dozenal(int(dozenal_fraction.replace('↊', 'A').replace('↋', 'B'), 12) + 1)
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

    return dozenal_fraction


def dozenal_to_sezimal(number: str, sezimal_precision: int = None) -> str:
    number = validate_clean_dozenal(str(number))

    number = number.replace('↊', 'A').replace('↋', 'B')

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

    decimal_integer = str(int(integer, 12))
    decimal_fraction = _dozenal_fraction_to_decimal(fraction, 36)

    decimal = decimal_integer

    if decimal_fraction:
        decimal += '.' + decimal_fraction

    if negative:
        decimal = '-' + decimal

    sezimal = decimal_to_sezimal(decimal, sezimal_precision)

    return sezimal


def _dozenal_fraction_to_decimal(fraction: str, decimal_precision: int = None) -> str:
    if not fraction:
        return ''

    if decimal_precision is None:
        decimal_precision = getcontext().prec

    with localcontext() as context:
        context.prec = decimal_precision * 2

        decimal_fraction = Decimal('0')

        i = -1
        for d in fraction:
            decimal_fraction += int(d, 12) * (Decimal('12') ** i)
            i -= 1

    decimal_fraction = validate_clean_decimal(decimal_fraction)
    decimal_fraction = decimal_fraction.split('.')[-1]

    if len(decimal_fraction) > decimal_precision:
        decimal_fraction = decimal_fraction[:decimal_precision]

    return decimal_fraction
