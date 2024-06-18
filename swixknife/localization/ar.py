

__all__ = ('SezimalLocaleAR',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleAR(SezimalLocale):
    LANG = 'ar'
    LANGUAGE = 'العربية'  # al-ʕarabiyya

    RTL = True
    DIGITS = '٠١٢٣٤٥٦٧٨٩'

    SEZIMAL_SEPARATOR = '٫'

    GROUP_SEPARATOR = '٬'
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    FIRST_WEEKDAY = 'SUN'
    DAY_OF_REST = 'SAT'
    OPTIONAL_DAY_OF_REST = 'FRI'

    WEEKDAY_NAME = [
        'الاثنين',  # al-iṯnayn
        'الثلاثاء',  # aṯ-ṯulāṯāʔ
        'الأربعاء',  # al-ʔarbiʕāʔ
        'الخميس',  # al-ḵamīs
        'الجمعة',  # al-jumuʕa
        'السبت',  # as-sabt
        'الأحد',  # al-ʔaḥad
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'يو٢',
        'يو٣',
        'يو٤',
        'يو٥',
        'جمع',
        'سبت',
        'يو١',
    ]

    MONTH_NAME= [
        'يناير',
        'فبراير',
        'مارس',
        'أبريل',
        'مايو',
        'يونيو',
        'يوليو',
        'أغسطس',
        'سبتمبر',
        'أكتوبر',
        'نوفمبر',
        'ديسمبر',
    ]

    MONTH_ABBREVIATED_NAME = [
        'ينا',
        'فبر',
        'مار',
        'أبر',
        'ماي',
        'يون',
        'يول',
        'أغس',
        'سبت',
        'أكت',
        'نوف',
        'ديس',
    ]

    DATE_FORMAT = '#?d/#?m/#?Y'
    DATE_LONG_FORMAT = '#?d/#?m/#?Y #@W'
    TIME_FORMAT = '#?u:#?p:#?a'
    DATE_TIME_FORMAT = '#?d/#?m/#?Y #?u:#?p:#?a'
    DATE_TIME_LONG_FORMAT = '#?d/#?m/#?Y #@W #?u:#?p:#?a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Africa/Cairo'

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
    ERROR = 'خطأ'
    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'

