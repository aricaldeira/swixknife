

__all__ = ('SezimalLocaleDA',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleDA(SezimalLocale):
    LANG = 'da'
    LANGUAGE = 'dansk'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
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
        'tirs.',
        'ons.',
        'tors.',
        'fre.',
        'lør.',
        'søn.',
    ]

    MONTH_NAME= [
        'januar',
        'februar',
        'marts',
        'april',
        'maj',
        'juni',
        'juli',
        'august',
        'september',
        'oktober',
        'november',
        'december',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan.',
        'feb.',
        'mar.',
        'apr.',
        'maj',
        'jun.',
        'jul.',
        'aug.',
        'sep.',
        'okt.',
        'nov.',
        'dec.',
    ]

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d. #M #Y'
    TIME_SEPARATOR = '.'
    TIME_FORMAT = '#u.#p.#a'
    DATE_TIME_FORMAT = '#d.#m.#Y #u.#p.#a'
    DATE_TIME_LONG_FORMAT = '#W, den #-d. #M #Y, #u.#p.#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    WEEK_NUMBER_SYMBOL = 'uge'
    DAY_NUMBER_SYMBOL = 'dag'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Copenhagen'
    TEXT_MONTH_DAY_FORMAT = '#-d. #M'
