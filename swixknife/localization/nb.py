

__all__ = ('SezimalLocaleNB',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleNB(SezimalLocale):
    LANG = 'nb'
    LANGUAGE = 'norsk bokmål'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'mandag',
        'tirsdag',
        'onsdag',
        'torsdag',
        'fredag',
        'lørdag',
        'søndag',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'man.',
        'tir.',
        'ons.',
        'tor.',
        'fre.',
        'lør.',
        'søn.',
    ]

    MONTH_NAME= [
        'januar',
        'februar',
        'mars',
        'april',
        'mai',
        'juni',
        'juli',
        'august',
        'september',
        'oktober',
        'november',
        'desember',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan.',
        'feb.',
        'mars',
        'apr.',
        'mai',
        'juni',
        'juli',
        'aug.',
        'sep.',
        'okt.',
        'nov.',
        'des.',
    ]

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#d. #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d. #M #Y, #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    WEEK_NUMBER_SYMBOL = 'uge'
    DAY_NUMBER_SYMBOL = 'dag'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Oslo'
    TEXT_MONTH_DAY_FORMAT = '#-d. #M'
