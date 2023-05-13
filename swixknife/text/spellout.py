

__all__ = ('sezimal_spellout',)

import os

CURDIR = os.path.dirname(os.path.abspath(__file__))

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal
from .soros import run as soros_run


def sezimal_spellout(number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction, lang: str = 'en') -> str:
    number = str(number)

    try:
        lang_file = open(f'{CURDIR}/data/{lang}.sor', 'r').read()
        units_and_prefixes = open(f'{CURDIR}/data/{lang}_units_and_prefixes.sor', 'r').read()
    except:
        try:
            lang_file = open(f'{CURDIR}/data/{lang[:2]}.sor', 'r').read()
            units_and_prefixes = open(f'{CURDIR}/data/{lang[:2]}_units_and_prefixes.sor', 'r').read()
        except:
            lang_file = open(f'{CURDIR}/data/en.sor', 'r').read()
            units_and_prefixes = open(f'{CURDIR}/data/en_units_and_prefixes.sor', 'r').read()

    text = soros_run(lang_file.replace('### UNITS_AND_PREFIXES ###', units_and_prefixes), number, lang)

    return text
