

__all__ = ('SezimalLocaleHE',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT


class SezimalLocaleHE(SezimalLocale):
    LANG = 'he'
    LANGUAGE = 'עברית'  # ’ivrít

    RTL = True

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '₪'
    CURRENCY_SUBUNIT_SYMBOL = 'א״ר'

    FIRST_WEEKDAY = 'SUN'
    DAY_OF_REST = 'SAT'
    OPTIONAL_DAY_OF_REST = 'FRI'

    WEEKDAY_NAME = [
        'יום שני', # yom ŝení
        'יום שלישי',  # yom ŝeliŝí
        'יום רביעי',  # yom revi’í
        'יום חמישי',  # yom ĥamiŝí
        'יום שישי',  # yom ŝiŝí
        'יום שבת',  # yom ŝabát
        'יום ראשון',  # yom riŝón
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'ב׳',
        'ג׳',
        'ד׳',
        'ה׳',
        'ו׳',
        'שבת',
        'א׳',
    ]

    WEEKDAY_SYMBOL = [
        'ב',
        'ג',
        'ד',
        'ה',
        'ו',
        'ש',
        'א',
    ]

    MONTH_NAME= [
        'ינואר',  # yánuar
        'פברואר',  # fébruar
        'מרץ',  #  merts
        'אפריל',  # apríl
        'מאי',  # may
        'יוני',  # yóni
        'יולי',  # yúli
        'אוגוסט',  # ogúst
        'ספטמבר',  # septémber
        'אוקטובר',  # október
        'נובמבר',  # novémber
        'דצמבר',  # detsémber
    ]

    MONTH_ABBREVIATED_NAME = [
        'ינו׳',
        'פבר׳',
        'מרץ',
        'אפר׳',
        'מאי',
        'יוני',
        'יולי',
        'אוג׳',
        'ספט׳',
        'אוק׳',
        'נוב׳',
        'דצמ׳',
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
    ERROR = 'שגיאה'
    WEEKDAY_ERROR = '{weekday} יום שבוע לא חוקי'
    MONTH_ERROR = '{month} חודש לא חוקי'
    WEEK_NUMBER_SYMBOL = 'שבו'
