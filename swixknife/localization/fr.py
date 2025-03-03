

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

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

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
        'juill.',
        'août',
        'sept.',
        'oct.',
        'nov.',
        'déc.',
    ]

    ERA_NAME = [
        #
        # Ère Humaine Sézimale
        #
        'ÈHS',
        #
        # Avant l’Ère Humaine Sézimale
        #
        'av. l’ÈHS',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'
    DST_NAME = 'Heure d’été'
    DST_SHORT_NAME = 'HÉ'
    DEFAULT_TIME_ZONE = 'Europe/Paris'
    ISO_DATE_LONG_FORMAT = '%-d%O %b. %Y'
    TEXT_MONTH_DAY_FORMAT = '#-d#O #M'

    SEASON_NAME = {
        'spring_cross_quarter': 'Transition hiver – printemps',
        'spring_equinox': 'Printemps',
        'summer_cross_quarter': 'Transition printemps – été',
        'summer_solstice': 'Été',
        'autumn_cross_quarter': 'Transition été – automne',
        'autumn_equinox': 'Automne',
        'winter_cross_quarter': 'Transition automne – hiver',
        'winter_solstice': 'Hiver',
    }

    MOON_PHASE = {
        'new': 'Nouvelle',
        'waxing_crescent': 'Premier croissant',
        'first_quarter': 'Premier quartier',
        'waxing_gibbous': 'Premier quartier à la pleine',
        'full': 'Pleine',
        'waning_gibbous': 'Pleine au dernier quartier',
        'third_quarter': 'Dernier quartier',
        'waning_crescent': 'Dernier croissant',
    }

    #
    # Error messages
    #
    ERROR = 'Erreur'
    WEEKDAY_ERROR = 'Jour de la semaine invalide {weekday}'
    MONTH_ERROR = 'Mois invalide {month}'
    WEEK_NUMBER_SYMBOL = 'sem'
    DAY_NUMBER_SYMBOL = 'jour'

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

    DCC_TERM_NAME = [
        'bimestre‐zéro',
        'bimestre‐un',
        'bimestre‐deux',
        'bimestre‐trois',
        'bimestre‐quatre',
    ]

    DCC_TERM_ABBREVIATED_NAME = [
        'B0',
        'B1',
        'B2',
        'B3',
        'B4',
    ]

    DCC_MONTH_NAME = [
        'mois‐zéro',
        'mois‐un',
        'mois‐deux',
        'mois‐trois',
        'mois‐quatre',
        'mois‐cinq',
        'mois‐six',
        'mois‐six‐et‐un',
        'mois‐six‐deux',
        'mois‐six‐trois',
        'mois‐six‐quatre',
    ]

    DCC_WEEKDAY_NAME = [
        'jour‐de‐la‐semaine‐zéro',
        'jour‐de‐la‐semaine‐un',
        'jour‐de‐la‐semaine‐deux',
        'jour‐de‐la‐semaine‐trois',
        'jour‐de‐la‐semaine‐quatre',
        'jour‐de‐la‐semaine‐cinq',
    ]

    DCC_WEEKDAY_ABBREVIATED_NAME = [
        'JS0',
        'JS1',
        'JS2',
        'JS3',
        'JS4',
        'JS5',
    ]

    DCC_NUMBER = [
        'zéro',
        'un',
        'deux',
        'trois',
        'quatre',
        'cinq',
        'six',
        'six‐et‐un',
        'six‐deux',
        'six‐trois',
        'six‐quatre',
    ]

    DCC_YEAR_COUNT = {
        None: '&>Y années',
        SezimalInteger('1'): '&>Y année',
    }

    DCC_TERM_COUNT = {
        None: '&-t bimestres',
        SezimalInteger('1'): '&-t bimestre',
    }

    DCC_MONTH_COUNT = {
        None: '&-m mois',
        SezimalInteger('1'): '&-m mois',
    }

    DCC_WEEK_COUNT = {
        None: '&-wM semaines',
        SezimalInteger('1'): '&-wM semaine',
    }

    DCC_WEEK_IN_YEAR_COUNT = {
        None: '&-wY semaines',
        SezimalInteger('1'): '&-wY semaine',
    }

    DCC_DAY_COUNT = {
        None: '&-d jours',
        SezimalInteger('1'): '&-d jour',
    }

    DCC_DAY_IN_YEAR_COUNT = {
        None: '&-dY jours',
        SezimalInteger('1'): '&-dY jour',
    }

    DCC_DAY_IN_WEEK_COUNT = {
        None: '&-dW jours',
        SezimalInteger('1'): '&-dW jour',
    }

    DCC_DATE_MONTH_DAY_SEPARATOR = ' et '
