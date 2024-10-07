

__all__ = ('SezimalLocaleFA',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleFA(SezimalLocale):
    LANG = 'fa'
    LANGUAGE = 'فارسی'

    RTL = True
    DIGITS = '۰۱۲۳۴۵۶۷۸۹'

    SEZIMAL_SEPARATOR = '٫'

    GROUP_SEPARATOR = '٬'
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = '﷼'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0

    FIRST_WEEKDAY = 'SAT'
    DAY_OF_REST = 'FRI'
    OPTIONAL_DAY_OF_REST = ''

    WEEKDAY_NAME = [
        'دوشنبه',
        'سه‌شنبه',
        'چهارشنبه',
        'پنجشنبه',
        'جمعه',
        'شنبه',
        'یکشنبه',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        '۲شب',
        '۳شب',
        '۴شب',
        '۵شب',
        'جمع',
        'شنب',
        #
        # The line below uses \u06f1 (Arabic digit 1 - used in Iran)
        # I don’t know if it is font problem, or a rendering problem,
        # but it causes doŝanbe to swap \u06f2 to show at the left of ŝb,
        # instead of at the right, when the first day of the week is Monday
        #
        # '۱شب',
        #
        # The line below uses \u0661 (Arabic digit 1 - the “regular” one)
        # Just so it renders properly, for now
        #
        '١شب',
    ]

    MONTH_NAME= [
        'ژانویهٔ',
        'فوریهٔ',
        'مارس',
        'آوریل',
        'مهٔ',
        'ژوئن',
        'ژوئیهٔ',
        'اوت',
        'سپتامبر',
        'اکتبر',
        'نوامبر',
        'دسامبر',
    ]

    MONTH_ABBREVIATED_NAME = [
        'ژان',
        'فور',
        'مار',
        'آور',
        'مهٔ',
        'ژوئ',
        'ژوئی',
        'اوت',
        'سپت',
        'اکت',
        'نوا',
        'دسا',
    ]

    DATE_FORMAT = '#?d/#?m/#?Y'
    DATE_LONG_FORMAT = '#?d/#?m/#?Y #@W'
    TIME_FORMAT = '#?u:#?p:#?a'
    DATE_TIME_FORMAT = '#?d/#?m/#?Y #?u:#?p:#?a'
    DATE_TIME_LONG_FORMAT = '#?d/#?m/#?Y #@W #?u:#?p:#?a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Tehran'

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
    ERROR = 'خطا'
    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'
    WEEK_NUMBER_SYMBOL = 'هف'
