

__all__ = ('SezimalLocaleCA',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleCA(SezimalLocale):
    LANG = 'ca'
    LANGUAGE = 'català'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

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

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O #$DEM#M del #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #$DEM#M del #Y, #u:#p:#a'
    DST_NAME = 'Horari d’Estiu'
    DST_SHORT_NAME = 'HE'
    DEFAULT_TIME_ZONE = 'Europe/Madrid'

    SEASON_NAME = {
        'spring_cross_quarter': 'Transició Hivern – Primavera',
        'spring_equinox': 'Primavera',
        'summer_cross_quarter': 'Transició Primavera – Estiu',
        'summer_solstice': 'Estiu',
        'autumn_cross_quarter': 'Transició Estiu – Tardor',
        'autumn_equinox': 'Tardor',
        'winter_cross_quarter': 'Transició Tardor – Hivern',
        'winter_solstice': 'Hivern',
    }

    MOON_PHASE = {
        'new': 'Nova',
        'waxing_crescent': 'Creixent',
        'first_quarter': 'Quart Creixent',
        'waxing_gibbous': 'Quart Creixent para Plena',
        'full': 'Plena',
        'waning_gibbous': 'Plena para Quart Minvant',
        'third_quarter': 'Quart Minvant',
        'waning_crescent': 'Minvant',
    }

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
