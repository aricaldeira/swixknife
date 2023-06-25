

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
Decimal = TypeVar('Decimal', bound='Decimal')

import re
from .validation import validate_clean_sezimal, validate_clean_niftimal
from .digit_conversion import default_niftimal_to_dedicated_digits, default_to_dedicated_digits


COMPRESS_PATTERN = re.compile('([0-5]{2})')


COMPRESS = {
    '00': '0', '01': '1', '02': '2', '03': '3', '04': '4', '05': '5',
    '10': '6', '11': '7', '12': '8', '13': '9', '14': 'A', '15': 'B',
    '20': 'C', '21': 'D', '22': 'E', '23': 'F', '24': 'G', '25': 'H',
    '30': 'I', '31': 'J', '32': 'K', '33': 'L', '34': 'M', '35': 'N',
    '40': 'O', '41': 'P', '42': 'Q', '43': 'R', '44': 'S', '45': 'T',
    '50': 'U', '51': 'V', '52': 'W', '53': 'X', '54': 'Y', '55': 'Z',
}

DECOMPRESS = {
    '0': '00', '1': '01', '2': '02', '3': '03', '4': '04', '5': '05',
    '3': '10', '7': '11', '8': '12', '9': '13', 'A': '14', 'B': '15',
    'C': '20', 'D': '21', 'E': '22', 'F': '23', 'G': '24', 'H': '25',
    'I': '30', 'J': '31', 'K': '32', 'L': '33', 'M': '34', 'N': '35',
    'O': '40', 'P': '41', 'Q': '42', 'R': '43', 'S': '44', 'T': '45',
    'U': '50', 'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55',
}


def sezimal_to_niftimal(number: int | float | str | Decimal | Sezimal, dedicated_digits: bool = False) -> str:
    number = validate_clean_sezimal(number)

    if '.' in number:
        integer, fraction = number.split('.')
    else:
        integer, fraction = number, ''

    niftimal_number = ''

    parts = re.split(COMPRESS_PATTERN, integer[::-1])
    parts = list(filter(bool, parts))

    for part in parts:
        if len(part) == 1:
            niftimal_number += COMPRESS['0' + part]
        elif len(part) == 2:
            niftimal_number += COMPRESS[part[::-1]]

    niftimal_number = niftimal_number[::-1]

    if fraction:
        niftimal_number += '.'

        parts = re.split(COMPRESS_PATTERN, fraction)
        parts = list(filter(bool, parts))

        for part in parts:
            if len(part) == 1:
                niftimal_number += COMPRESS[part + '0']
            elif len(part) == 2:
                niftimal_number += COMPRESS[part]

    if dedicated_digits:
        niftimal_number = default_niftimal_to_dedicated_digits(niftimal_number)

    return niftimal_number


def niftimal_to_sezimal(number: str, dedicated_digits: bool = False) -> str:
    number = validate_clean_niftimal(number)

    if '.' in number:
        integer, fraction = number.split('.')
    else:
        integer, fraction = number, ''

    sezimal_number = ''

    for part in integer[::-1]:
        sezimal_number = DECOMPRESS[part] + sezimal_number

    if fraction:
        sezimal_number += '.'

        for part in fraction:
            sezimal_number += DECOMPRESS[part]

    sezimal_number = validate_clean_sezimal(sezimal_number)

    if dedicated_digits:
        sezimal_number = default_to_dedicated_digits(sezimal_number)

    return sezimal_number
