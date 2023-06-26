

__all__ = ('SezimalLocaleDE',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleDE(SezimalLocale):
    LANG = 'de'
    LANGUAGE = 'Deutsch'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'Montag',
        'Dienstag',
        'Mittwoch',
        'Donnerstag',
        'Freitag',
        'Samstag',
        'Sonntag',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Mo.',
        'Di.',
        'Mi.',
        'Do.',
        'Fr.',
        'Sa.',
        'So.',
    ]

    MONTH_NAME= [
        'Januar',
        'Februar',
        'März',
        'April',
        'Mai',
        'Juni',
        'Juli',
        'August',
        'September',
        'Oktober',
        'November',
        'Dezember',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Jan.',
        'Febr.',
        'März',
        'Apr.',
        'Mai.',
        'Juni',
        'Juli',
        'Aug.',
        'Sep.',
        'Okt.',
        'Nov.',
        'Dez.',
    ]

    ERA_NAME = [
        #
        # Senarische Zeitalter der Menschheit
        #
        'SZM',
        #
        # vor das Senarische Zeitalter der Menschheit
        #
        'v. SZM',
    ]

    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d.#m.#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'

    SEASON_NAME = {
        'spring_cross_quarter': 'Übergang Winter – Frühling',
        'spring_equinox': 'Frühling',
        'summer_cross_quarter': 'Übergang Frühling – Sommer',
        'summer_solstice': 'Sommer',
        'autumn_cross_quarter': 'Übergang Sommer – Herbst',
        'autumn_equinox': 'Herbst',
        'winter_cross_quarter': 'Übergang Herbst – Winter',
        'winter_solstice': 'Winter',
    }

    MOON_PHASE = {
        'new': 'Neumond',
        'waxing crescent': 'Zunehmender Sichelmond',
        'first quarter': 'Zunehmender Halbmond',
        'waxing gibbous': 'Zunehmender Mond',
        'full': 'Vollmond',
        'waning gibbous': 'Abnehmender Mond',
        'third quarter': 'Abnehmender Halbmond',
        'waning crescent': 'Abnehmender Sichelmond',
    }

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        return '.'
