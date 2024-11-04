

__all__ = ('SezimalLocaleSV',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleSV(SezimalLocale):
    LANG = 'sv'
    LANGUAGE = 'svenska'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'måndag',
        'tisdag',
        'onsdag',
        'torsdag',
        'fredag',
        'lördag',
        'söndag',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'mån',
        'tis',
        'ons',
        'tors',
        'fre',
        'lör',
        'sön',
    ]

    MONTH_NAME= [
        'januari',
        'februari',
        'mars',
        'april',
        'maj',
        'juni',
        'juli',
        'augusti',
        'september',
        'oktober',
        'november',
        'december',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan.',
        'feb.',
        'mars',
        'apr.',
        'maj',
        'juni',
        'juli',
        'aug.',
        'sep.',
        'okt.',
        'nov.',
        'dec.',
    ]

    DATE_SEPARATOR = '-'
    DATE_FORMAT = '#Y-#m-#d'
    DATE_LONG_FORMAT = '#-d #M #Y'
    TIME_SEPARATOR = '.'
    TIME_FORMAT = '#u.#p.#a'
    DATE_TIME_FORMAT = '#Y-#m-#d #u.#p.#a'
    DATE_TIME_LONG_FORMAT = '#W #-d #M #Y #u.#p.#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    WEEK_NUMBER_SYMBOL = 'v.'
    DAY_NUMBER_SYMBOL = 'dag'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Stockholm'
