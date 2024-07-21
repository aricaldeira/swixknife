

__all__ = ('sezimal_spellout',)

import os

CURDIR = os.path.dirname(os.path.abspath(__file__))

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal
from .soros import soros_compile


SPELLOUT_PROGRAMS = {}


def sezimal_spellout(number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction, lang: str = 'en') -> str:
    number = str(number).replace('_', '')

    if not number:
        return ''

    if '..' in number:
        number, recurring = number.split('..')
    elif ',,' in number:
        number, recurring = number.split(',,')
    else:
        recurring = ''

    #
    # The unicode characters are not all working correctly,
    # so we replace them by their correspondent unit
    #
    if number[-1] == '󱹰':
        number = 'SH-p/s ' + number[0:-1]
    elif number[-1] in ('%', '󱹱'):
        number = 'SH-p/n ' + number[0:-1]
    elif number[-1] in ('‰', '󱹲'):
        number = 'SH-p/a ' + number[0:-1]
    elif number[-1] in ('‱', '󱹳'):
        number = 'SH-p/sa ' + number[0:-1]
    elif number[-1] == '󱹴':
        number = 'SH-p/na ' + number[0:-1]
    elif number[-1] == '󱹵':
        number = 'SH-p/x ' + number[0:-1]
    elif number[-1] == '󱹶':
        number = 'SH-p/sx ' + number[0:-1]
    elif number[-1] == '󱹷':
        number = 'SH-p/nx ' + number[0:-1]
    elif number[-1] == '󱹸':
        number = 'SH-p/ax ' + number[0:-1]
    elif number[-1] == '󱹹':
        number = 'SH-p/sax ' + number[0:-1]
    elif number[-1] == '󱹺':
        number = 'SH-p/nax ' + number[0:-1]
    elif number[-1] == '󱹻':
        number = 'SH-p/Dx ' + number[0:-1]
    elif number[-1] == '󱹼':
        number = 'SH-p/Tx ' + number[0:-1]
    elif number[-1] == '󱹽':
        number = 'SH-p/Cx ' + number[0:-1]
    elif number[-1] == '󱹾':
        number = 'SH-p/Px ' + number[0:-1]
    elif number[-1] == '󱹿':
        number = 'SH-p/Xx ' + number[0:-1]

    if lang not in SPELLOUT_PROGRAMS:
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

        SPELLOUT_PROGRAMS[lang] = soros_compile(lang_file.replace('### UNITS_AND_PREFIXES ###', units_and_prefixes), lang)

    soros_program = SPELLOUT_PROGRAMS[lang]
    text = soros_program.run(number).strip()

    if recurring:
        text += ' ' + soros_program.run('..').strip()

        for n in recurring:
            text += ' ' + soros_program.run(n).strip()

    # del SPELLOUT_PROGRAMS[lang]

    return text
