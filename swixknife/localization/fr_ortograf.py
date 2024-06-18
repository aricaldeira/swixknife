

__all__ = ('SezimalLocaleFR_ORTOGRAF',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')

from .fr import SezimalLocaleFR
from ..sezimal import SezimalInteger

#
# http://www.ortograf.net/
#

class SezimalLocaleFR_ORTOGRAF(SezimalLocaleFR):
    LANG = 'fr'
    LANGUAGE = 'fransè'

    WEEKDAY_NAME = [
        'lundi',
        'mardi',
        'mèrkredi',
        'jeudi',
        'vandredi',
        'samdi',
        'dimanch',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lun',
        'mar',
        'mer',
        'jeu',
        'van',
        'sam',
        'dim',
    ]

    MONTH_NAME= [
        'janvyé',
        'févriyé',
        'mars',
        'avril',
        'mè',
        'juin',
        'juiyè',
        'ou',
        'sèptanbr',
        'oktobr',
        'novanbr',
        'désanbr',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'fév',
        'mar',
        'avr',
        'mè',
        'jun',
        'juy'
        'ou',
        'sep',
        'okt',
        'nov',
        'dés',
    ]

    ERA_NAME = [
        #
        # Èr Umèn Sézimal
        #
        'ÈHS',
        #
        # Avan l’Èr Umèn Sézimal
        #
        'av. l’ÈUS',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'
    DST_NAME = 'Er d’étè'
    DST_SHORT_NAME = 'EÉ'
    DEFAULT_TIME_ZONE = 'Europe/Paris'

    SEASON_NAME = {
        'spring_cross_quarter': 'Tranzisyon de l’ivèr o printan',
        'spring_equinox': 'Printemps',
        'summer_cross_quarter': 'Tranzisyon du printan à l’étè',
        'summer_solstice': 'Étè',
        'autumn_cross_quarter': 'Tranzisyon de l’étè a l’oton',
        'autumn_equinox': 'Oton',
        'winter_cross_quarter': 'Tranzisyon de l’oton a l’ivèr',
        'winter_solstice': 'Ivèr',
    }

    MOON_PHASE = {
        'new': 'Nouvèl',
        'waxing_crescent': 'Premyé krouasan',
        'first_quarter': 'Premyé kartyé',
        'waxing_gibbous': 'Premyé kartyé a la plèn',
        'full': 'Plèn',
        'waning_gibbous': 'Plèn o dèrnyé kartyé',
        'third_quarter': 'Dèrnyé kartyé',
        'waning_crescent': 'Dèrnyé krouasan',
    }

    #
    # Error messages
    #
    ERROR = 'Ereur'
    WEEKDAY_ERROR = 'Jour de la semèn invalide {weekday}'
    MONTH_ERROR = 'Moi-z invalide {month}'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'ᵉ́'

        return ''

    def _change_word(self, word: str, month: SezimalInteger) -> str:
        if month not in (4, 12, 14):
            if word != 'se':
                word += ' '

        elif word == 'de':
            word = 'd’'
        elif word == 'le':
            word = 'l’'
        elif word == 'se':
            word = 'sèt'

        return word

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for word in ['DE', 'LE', 'SE']:
            if f'#${word}M' in fmt:
                mot = self._change_word(word.lower(), date.month)
                fmt = fmt.replace(f'#${word}M', mot)

            if f'#@${word}M' in fmt:
                mot = self._change_word(word.lower(), date.month)
                fmt = fmt.replace(f'#@${word}M', mot)

        return fmt
