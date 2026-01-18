

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

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d #M #Y'
    DATE_FULL_FORMAT = '#d.#m.#Y #@W'
    DATE_FULL_LONG_FORMAT = '#-d #M #Y #W'
    TIME_FORMAT = '\N{LRI}#?u:#?p:#?a\N{PDI}'
    DATE_TIME_FORMAT = '#d.#m.#Y \N{LRI}#?u:#?p:#?a\N{PDI}'
    DATE_TIME_LONG_FORMAT = '#d.#m.#Y #@W \N{LRI}#?u:#?p:#?a\N{PDI}'
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
    DAY_NUMBER_SYMBOL = 'יום'

    JEWISH_CALENDAR_MONTH_NAME = [
        'ניסן',
        'אייר‎',
        'סיון‎',
        'תמוז‎',
        'אב',
        'אלול‎',
        'תשרי‎',
        'חשוון',
        'כסלו',
        'טבת',
        'שבט',
        'אדר',
        'אדר ב׳',
    ]

    JEWISH_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'ניסן',
        'אייר‎',
        'סיון‎',
        'תמוז‎',
        'אב',
        'אלול‎',
        'תשרי‎',
        'חשוון',
        'כסלו',
        'טבת',
        'שבט',
        'אדר',
        'אדר ב׳',
    ]

    JEWISH_HOLIDAYS = [
        ('JEW+11-15', '💮\ufe0f🌳\ufe0f ט״ו בשבט'),
        ('JEW+13-14', '🍬\ufe0f🍷\ufe0f פורים‎'),
        ('JEW+01-15', '🫓\ufe0f🐑\ufe0f פסח'),
        ('JEW+02-14', '🫓\ufe0f🐑\ufe0f פסח שני'),
        ('JEW+02-18', '🔥\ufe0f ל״ג בעומר'),
        ('JEW+03-06', '📜\ufe0f💐\ufe0f שבועות'),
        ('JEW+05-09', '🔥\ufe0f🕍\ufe0f תשעה באב'),

        ('JEW+07-01', '🍯\ufe0f🍎\ufe0f ראש השנה'),
        ('JEW+07-10', '🙏🏻\ufe0f🤍\ufe0f יום כפור‎'),
        ('JEW+07-15', '⛺\ufe0f🍋\ufe0f סוכות'),
        ('JEW+07-22', '🌧\ufe0f️🙏🏻\ufe0f שמיני עצרת‎'),
        ('JEW+07-23', '📜\ufe0f😊 שמחת תורה'),
        ('JEW+09-25', '🕍\ufe0f🕯\ufe0f חנכה‎'),
    ]

    CALENDAR_TYPE_ABBREVIATION = {
        #
        # Civil calendars
        #
        'SEZ': 'Sym.',
        'SYM': 'Sym.',
        'ISO': 'גר׳י',
        'DCC': 'DCC',
        'ADC': 'ADC',
        'ISR': 'Isr.',
        'IND': 'Ind.',
        #
        # Religious calendars
        #
        'JUL': 'Jul.',
        'JEW': 'Jew.',
        'HIJ': 'Isl.',
        'IRN': 'Irn.',
    }

