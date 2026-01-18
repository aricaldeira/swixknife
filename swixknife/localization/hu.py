

__all__ = ('SezimalLocaleHU',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleHU(SezimalLocale):
    LANG = 'hu'
    LANGUAGE = 'magyar'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = 'Ft'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    WEEKDAY_NAME = [
        'hétfő',
        'kedd',
        'szerda',
        'csütörtök',
        'péntek',
        'szombat',
        'vasárnap',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'hét',
        'ked',
        'sze',
        'csü',
        'pén',
        'szo',
        'vas',
    ]

    MONTH_NAME= [
        'január',
        'február',
        'március',
        'április',
        'május',
        'június',
        'július',
        'augusztus',
        'szeptember',
        'október',
        'november',
        'december',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan.',
        'febr.',
        'márc.',
        'ápr.',
        'máj.',
        'jún.',
        'júl.',
        'aug.',
        'szept.',
        'okt.',
        'nov.',
        'dec.',
    ]

    DATE_SEPARATOR = '. '
    DATE_FORMAT = '#y. #m. #d.'
    DATE_LONG_FORMAT = '#y. #M #-d.'
    DATE_FULL_FORMAT = '#y. #m. #d. #@W'
    DATE_FULL_LONG_FORMAT = '#y. #M #-d., #W'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#y. #m. #d. #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#y. #M #-d., #W, #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Budapest'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Summer',
        'autumn_cross_quarter': 'Autumn Cross-Quarter',
        'autumn_equinox': 'Autumn',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Winter',
    }

    MOON_PHASE = {
        'new': 'New',
        'waxing_crescent': 'Waxing Crescent',
        'first_quarter': 'First Quarter',
        'waxing_gibbous': 'Waxing Gibbous',
        'full': 'Full',
        'waning_gibbous': 'Waning Gibbous',
        'third_quarter': 'Third Quarter',
        'waning_crescent': 'Waning Crescent',
    }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []

    #
    # Error messages
    #
    ERROR = 'Hiba'
    WEEKDAY_ERROR = 'Érvénytelen hétköznap {weekday}'
    MONTH_ERROR = 'Érvénytelen hónap {month}'
    WEEK_NUMBER_SYMBOL = 'hét'
    DAY_NUMBER_SYMBOL = 'nap'
