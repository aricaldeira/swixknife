

__all__ = ('SezimalLocaleCA',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleCA(SezimalLocale):
    LANG = 'ca'
    LANGUAGE = 'català'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'dilluns',
        'dimarts',
        'dimecres',
        'dijous',
        'divendres',
        'dissabte',
        'diumenge',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'dl.',
        'dt.',
        'dc.',
        'dj.',
        'dv.',
        'ds.',
        'dg.',
    ]

    MONTH_NAME= [
        'gener',
        'febrer',
        'març',
        'abril',
        'maig',
        'juny',
        'juliol',
        'agost',
        'setembre',
        'octubre',
        'novembre',
        'desembre',
    ]

    MONTH_ABBREVIATED_NAME = [
        'gen.',
        'febr.',
        'març',
        'abr.',
        'maig',
        'juny',
        'jul.',
        'ag.',
        'set.',
        'oct.',
        'nov.',
        'des.',
    ]

    ERA_NAME = [
        #
        # Era Humana Sezimal
        #
        'EHS',
        #
        # Abans de l’Era Humana Sezimal
        #
        'aEHS',
    ]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'r'

        return ''

    def _change_word(self, word: str, month: SezimalInteger) -> str:
        if month not in (4, 12, 14):
            word += ' '
        elif word == 'de':
            word = 'd’'
        elif word == 'le':
            word = 'l’'

        return word

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for word in ['DE', 'EL']:
            if f'#${word}M' in fmt:
                paraula = self._change_word(word.lower(), date.month)
                fmt = fmt.replace(f'#${word}M', paraula)

        return fmt