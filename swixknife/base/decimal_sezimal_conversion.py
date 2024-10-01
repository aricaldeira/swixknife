
from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')

from decimal import Decimal, localcontext, getcontext

from .validation import validate_clean_decimal
from .context import sezimal_context


def decimal_to_sezimal(number: int | float | Decimal | str | Sezimal | SezimalInteger | SezimalFraction, sezimal_precision: int | str | SezimalInteger = None) -> str:
    if type(number).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        return str(number.decimal)

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


_HUNDRETHS_TO_SEZIMAL = {
    '01': '00..20543',
    '02': '00..41530',
    '03': '01..02514',
    '04': '01..23501',
    '05': '01..44444',
    '06': '02..05432',
    '07': '02..30415',
    '08': '02..51402',
    '09': '03..12350',
    '10': '03..33333',
    '1':  '03..33333',
    '11': '03..54320',
    '12': '04..15304',
    '13': '04..40251',
    '14': '05..01235',
    '15': '05..22222',
    '16': '05..43205',
    '17': '10..04153',
    '18': '10..25140',
    '19': '10..50123',
    '20': '11..11111',
    '2':  '11..11111',
    '21': '11..32054',
    '22': '11..53041',
    '23': '12..14025',
    '24': '12..35012',
    '25': '13..00000',
    '26': '13..20543',
    '27': '13..41530',
    '28': '14..02514',
    '29': '14..23501',
    '30': '14..44444',
    '3':  '14..44444',
    '31': '15..05432',
    '32': '15..30415',
    '33': '15..51402',
    '34': '20..12350',
    '35': '20..33333',
    '36': '20..54320',
    '37': '21..15304',
    '38': '21..40251',
    '39': '22..01235',
    '40': '22..22222',
    '4':  '22..22222',
    '41': '22..43205',
    '42': '23..04153',
    '43': '23..25140',
    '44': '23..50123',
    '45': '24..11111',
    '46': '24..32054',
    '47': '24..53041',
    '48': '25..14025',
    '49': '25..35012',
    '50': '30..00000',
    '5':  '30..00000',
    '51': '30..20543',
    '52': '30..41530',
    '53': '31..02514',
    '54': '31..23501',
    '55': '31..44444',
    '56': '32..05432',
    '57': '32..30415',
    '58': '32..51402',
    '59': '33..12350',
    '60': '33..33333',
    '6':  '33..33333',
    '61': '33..54320',
    '62': '34..15304',
    '63': '34..40251',
    '64': '35..01235',
    '65': '35..22222',
    '66': '35..43205',
    '67': '40..04153',
    '68': '40..25140',
    '69': '40..50123',
    '70': '41..11111',
    '7':  '41..11111',
    '71': '41..32054',
    '72': '41..53041',
    '73': '42..14025',
    '74': '42..35012',
    '75': '43..00000',
    '76': '43..20543',
    '77': '43..41530',
    '78': '44..02514',
    '79': '44..23501',
    '80': '44..44444',
    '8':  '44..44444',
    '81': '45..05432',
    '82': '45..30415',
    '83': '45..51402',
    '84': '50..12350',
    '85': '50..33333',
    '86': '50..54320',
    '87': '51..15304',
    '88': '51..40251',
    '89': '52..01235',
    '90': '52..22222',
    '9':  '52..22222',
    '91': '52..43205',
    '92': '53..04153',
    '93': '53..25140',
    '94': '53..50123',
    '95': '54..11111',
    '96': '54..32054',
    '97': '54..53041',
    '98': '55..14025',
    '99': '55..35012',
}

def _decimal_fraction_to_sezimal(fraction: str | Decimal, sezimal_precision: int = None) -> tuple[str, str]:
    if not fraction:
        return '0', ''

    decimal_precision = len(str(fraction))

    fraction = str(fraction)[::-1]

    while fraction[0] == '0':
        fraction = fraction[1:]

    if not fraction:
        return '0', '0' * decimal_precision

    fraction = fraction[::-1]

    if fraction in _HUNDRETHS_TO_SEZIMAL:
        return '0', _HUNDRETHS_TO_SEZIMAL[fraction]

    if sezimal_precision is None:
        sezimal_precision = _decimal_exponent_to_sezimal(getcontext().prec)

    fraction = Decimal('0.' + fraction)
    sezimal_integer = '0'
    sezimal_fraction = ''

    with localcontext() as context:
        context.prec = sezimal_precision * 2

        nines = '.' + '9' * ((context.prec // 4) + 1)

        for i in range(sezimal_precision):
            fraction = fraction * 6

            if nines in str(fraction):
                fraction = round(fraction, 0)

            if fraction == 6:
                sezimal_integer = '1'
                break

            digit = int(fraction % 10)
            sezimal_fraction += str(digit)
            fraction -= digit

            if fraction <= 0:
                break

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
