

__all__ = ('SezimalLocaleHE_LATN',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleHE_LATN(SezimalLocale):
    LANG = 'he'
    LANGUAGE = '’ivrít'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    FIRST_WEEKDAY = 'SUN'
    DAY_OF_REST = 'SAT'
    OPTIONAL_DAY_OF_REST = 'FRI'

    WEEKDAY_NAME = [
        'yom shení',
        'yom shelishí',
        'yom reviʼí',
        'yom xamishí',
        'yom shishí',
        'yom shabát',
        'yom rishón',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'shn',
        'shl',
        'rev',
        'xam',
        'shi',
        'sha',
        'ris',
    ]

    MONTH_NAME= [
        'yanuár',
        'fébruar',
        'merts',
        'apríl',
        'may',
        'yóni',
        'yúli',
        'agúst',
        'septémber',
        'október',
        'novémber',
        'detsémber',
    ]

    MONTH_ABBREVIATED_NAME = [
        'yan',
        'féb',
        'mer',
        'apr',
        'may',
        'yón',
        'yúl',
        'agú',
        'sep',
        'okt',
        'nov',
        'det',
    ]

    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#d.#m.#Y #@W'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d.#m.#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Jerusalem'

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
    ERROR = 'Shegiá'
    WEEKDAY_ERROR = 'Yom shavúa lo chuki {weekday}'
    MONTH_ERROR = 'Hodesh lo chuki {month}'

