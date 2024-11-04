

__all__ = ('SezimalLocaleSW',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleSW(SezimalLocale):
    LANG = 'sw'
    LANGUAGE = 'Kiswahili'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'Jumatatu',
        'Jumanne',
        'Jumatano',
        'Alhamisi',
        'Ijumaa',
        'Jumamosi',
        'Jumapili',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'J03',
        'J04',
        'J05',
        'Alh',
        'Iju',
        'J01',
        'J02',
    ]

    WEEKDAY_SYMBOL = [
        '3',
        '4',
        '5',
        'A',
        'I',
        '1',
        '2',
    ]

    MONTH_NAME= [
        'Januari',
        'Februari',
        'Machi',
        'Aprili',
        'Mei',
        'Juni',
        'Julai',
        'Agosti',
        'Septemba',
        'Oktoba',
        'Novemba',
        'Desemba',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Jan',
        'Feb',
        'Mac',
        'Apr',
        'Mei',
        'Jun',
        'Jul',
        'Ago',
        'Sep',
        'Okt',
        'Nov',
        'Des',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#d/#m/#Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d/#m/#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'UTC'

    SEASON_NAME = {
        'spring_cross_quarter': 'Kwanzia Majira ya baridi hadi Majira ya kuchipua',
        'spring_equinox': 'Majira ya kuchipua',
        'summer_cross_quarter': 'Kwanzia Majira ya kuchipua hadi Majira ya joto',
        'summer_solstice': 'Majira ya joto',
        'autumn_cross_quarter': 'Kwanzia Majira ya joto hadi Majira ya kupuputika majani',
        'autumn_equinox': 'Majira ya kupuputika majani',
        'winter_cross_quarter': 'Kwanzia Majira ya kupuputika majani hadi Majira ya baridi',
        'winter_solstice': 'Majira ya baridi',
    }

    MOON_PHASE = {
        'new': 'Mwezi mpya',
        'waxing_crescent': 'Mwezi mpevu',
        'first_quarter': 'First Quarter',
        'waxing_gibbous': 'Waxing Gibbous',
        'full': 'Mwezi Mzima',
        'waning_gibbous': 'Waning Gibbous',
        'third_quarter': 'Third Quarter',
        'waning_crescent': 'Mwezi Unaopungua',
    }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []

    #
    # Error messages
    #
    ERROR = 'Hitilafu'
    WEEKDAY_ERROR = 'Siku ya juma si sahihi {weekday}'
    MONTH_ERROR = 'Mwezi batili {month}'
    WEEK_NUMBER_SYMBOL = 'jum'
    DAY_NUMBER_SYMBOL = 'siku'
