

__all__ = ('SezimalLocaleYO',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleYO(SezimalLocale):
    LANG = 'yo'
    LANGUAGE = 'Èdè Yorùbá'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = '₦'
    CURRENCY_SUBUNIT_SYMBOL = 'kb'
    CURRENCY_SUBUNIT_SYMBOL_POSITION = 'R'

    WEEKDAY_NAME = [
        'Ọjọ́ Ajé',
        'Ọjọ́ Ìsẹ́gun',
        'Ọjọ́rú',
        'Ọjọ́bọ',
        'Ọjọ́ Ẹtì',
        'Ọjọ́ Àbámẹ́ta',
        'Ọjọ́ Àìkú',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Ajé',
        'Ìsẹ́',
        'Rú',
        'Bọ',
        'Ẹtì',
        'Àbá',
        'Àìk',
    ]

    MONTH_NAME= [
        'Oṣù Ṣẹ́rẹ́',
        'Oṣù Èrèlè',
        'Oṣù Ẹrẹ̀nà',
        'Oṣù Ìgbé',
        'Oṣù Ẹ̀bibi',
        'Oṣù Òkúdu',
        'Oṣù Agẹmọ',
        'Oṣù Ògún',
        'Oṣù Owewe',
        'Oṣù Ọ̀wàrà',
        'Oṣù Bélú',
        'Oṣù Ọ̀pẹ̀',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Ṣẹ́r',
        'Èrè',
        'Ẹrẹ̀',
        'Ìgb',
        'Ẹ̀bi',
        'Òkú',
        'Agẹ',
        'Ògú',
        'Owe',
        'Ọ̀wà',
        'Bél',
        'Ọ̀pẹ̀',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#d/#m/#Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d/#m/#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Africa/Lagos'

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
    ERROR = 'Asise'
    WEEKDAY_ERROR = 'Ọjọ́ ọ̀sẹ̀ ti ko wulo {weekday}'
    MONTH_ERROR = 'Oṣu ti ko tọ {month}'
    WEEK_NUMBER_SYMBOL = 'ọ̀sẹ̀'
    WEEK_NUMBER_SYMBOL = 'ọjọ́'
