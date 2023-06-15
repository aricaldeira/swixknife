

__all__ = ('SezimalLocaleFR',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleFR(SezimalLocale):
    LANG = 'fr'
    LANGUAGE = 'français'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'lundi',
        'mardi',
        'mercredi',
        'jeudi',
        'vendredi',
        'samedi',
        'dimanche',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lundi',
        'mardi',
        'mercr.',
        'jeudi',
        'vendr.',
        'sam.',
        'dim.',
    ]

    MONTH_NAME= [
        'janvier',
        'février',
        'mars',
        'avril',
        'mai',
        'juin',
        'juillet',
        'août',
        'septembre',
        'octobre',
        'novembre',
        'décembre',
    ]

    MONTH_ABBREVIATED_NAME = [
        'janv.',
        'févr.',
        'mars',
        'avr.',
        'mai',
        'juin',
        'juill.'
        'août',
        'sept.',
        'oct.',
        'nov.',
        'déc.',
    ]

    ERA_NAME = [
        #
        # Ère Humaine Sezimale
        #
        'ÈHS',
        #
        # Avant l’Ère Humaine Sezimale
        #
        'av. l’ÈHS',
    ]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'ᵉʳ'

        return ''

    def _change_word(self, word: str, month: SezimalInteger) -> str:
        if month not in (4, 12, 14):
            if word != 'ce':
                word += ' '

        elif word == 'de':
            word = 'd’'
        elif word == 'le':
            word = 'l’'
        elif word == 'ce':
            word = 'cet'

        return word

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for word in ['DE', 'LE', 'CE']:
            if f'#${word}M' in fmt:
                mot = self._change_word(word.lower(), date.month)
                fmt = fmt.replace(f'#${word}M', mot)

            if f'#@${word}M' in fmt:
                mot = self._change_word(word.lower(), date.month)
                fmt = fmt.replace(f'#@${word}M', mot)

        return fmt