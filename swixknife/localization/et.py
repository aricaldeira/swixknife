

__all__ = ('SezimalLocaleET',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleET(SezimalLocale):
    LANG = 'et'
    LANGUAGE = 'eesti'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'esmaspäev',
        'teisipäev',
        'kolmapäev',
        'neljapäev',
        'reede',
        'laupäev',
        'pühapäev',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'esm',
        'tei',
        'kol',
        'nel',
        'ree',
        'lau',
        'püh',
    ]

    MONTH_NAME= [
        'jaanuar',
        'veebruar',
        'märts',
        'aprill',
        'mai',
        'juuni',
        'juuli',
        'august',
        'september',
        'oktoober',
        'november',
        'detsember',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jaan',
        'veebr',
        'märts',
        'apr',
        'mai',
        'juuni',
        'juuli',
        'aug',
        'sept',
        'okt',
        'nov',
        'dets',
    ]

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#y'
    DATE_LONG_FORMAT = '#-d #M #y'
    DATE_FULL_FORMAT = '#@W #d.#m.#y'
    DATE_FULL_LONG_FORMAT = '#W #-d #M #y'
    TIME_SEPARATOR = '.'
    TIME_FORMAT = '#u.#p.#a'
    DATE_TIME_FORMAT = '#d.#m.#y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W #-d #M #y, #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    WEEK_NUMBER_SYMBOL = 'näd'
    DAY_NUMBER_SYMBOL = 'päev'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Tallinn'
