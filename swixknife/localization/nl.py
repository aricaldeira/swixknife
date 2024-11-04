

__all__ = ('SezimalLocaleNL',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleNL(SezimalLocale):
    LANG = 'nl'
    LANGUAGE = 'Nederlands'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'

    WEEKDAY_NAME = [
        'maandag',
        'dinsdag',
        'woensdag',
        'donderdag',
        'vrijdag',
        'zaterdag',
        'zondag',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'maa',
        'din',
        'woe',
        'don',
        'vri',
        'zat',
        'zon',
    ]

    MONTH_NAME= [
        'januari',
        'februari',
        'maart',
        'april',
        'mei',
        'juni',
        'juli',
        'augustus',
        'september',
        'oktober',
        'november',
        'december',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'feb',
        'mrt',
        'apr',
        'mei',
        'jun',
        'jul',
        'aug',
        'sep',
        'okt',
        'nov',
        'dec',
    ]

    DATE_SEPARATOR = '-'
    DATE_FORMAT = '#d-#m-#Y'
    DATE_LONG_FORMAT = '#d-#m-#Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d-#m-#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d-#m-#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Amsterdam'

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
    ERROR = 'Fout'
    WEEKDAY_ERROR = 'Ongeldige weekdag {weekday}'
    MONTH_ERROR = 'Ongeldige maand {month}'
    WEEK_NUMBER_SYMBOL = 'wk'
    DAY_NUMBER_SYMBOL = 'dag'
