

__all__ = ('SezimalLocaleBZ',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleBZ(SezimalLocale):
    LANG = 'bz'
    LANGUAGE = 'brazileru'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'segunda',
        'tersa',
        'kwarta',
        'kinta',
        'sesta',
        'sábadu',
        'dumingu',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'seg',
        'ter',
        'kwa',
        'kin',
        'ses',
        'sáb',
        'dum',
    ]

    MONTH_NAME= [
        'janeru',
        'fevereru',
        'marsu',
        'abriw',
        'mayu',
        'juỹu',
        'julyu',
        'agostu',
        'setenbru',
        'otubru',
        'novenbru',
        'dezenbru',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'fev',
        'mar',
        'abr',
        'may',
        'juỹ',
        'jul',
        'ago',
        'set',
        'otu',
        'nov',
        'dez',
    ]

    ERA_NAME = [
        #
        # Èra Umana Sezimaw
        #
        'ÈUS',
        #
        # Antis da Èra Umana Sezimaw
        #
        'aÈUS',
    ]

    WEEKDAY_ERROR = 'Dia da semana inválidu {weekday}'
    MONTH_ERROR = 'Mez inválidu {month}'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'ᵘ̱'

        return ''

    def _change_word(self, word: str, weekday: SezimalInteger) -> str:
        if weekday >= 10:
            if word == 'èsa':
                word = 'esi'
            elif word == 'èsta':
                word = 'esti'
            elif word == 'akèla':
                word = 'akeli'
            elif word == 'kwa':
                word = 'ku'
            else:
                word = 'u'

        return word

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for word in ['A', 'KWA', 'ÈSA', 'ÈSTA', 'AKÈLA']:
            if f'#${word}W' in fmt:
                palavra = self._change_word(word.lower(), date.weekday)
                fmt = fmt.replace(f'#${word}W', palavra)

        return fmt
