

__all__ = ('SezimalLocaleDE',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleDE(SezimalLocale):
    LANG = 'de'
    LANGUAGE = 'Deutsch'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'C'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    WEEKDAY_NAME = [
        'Montag',
        'Dienstag',
        'Mittwoch',
        'Donnerstag',
        'Freitag',
        'Samstag',
        'Sonntag',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Mo.',
        'Di.',
        'Mi.',
        'Do.',
        'Fr.',
        'Sa.',
        'So.',
    ]

    MONTH_NAME= [
        'Januar',
        'Februar',
        'März',
        'April',
        'Mai',
        'Juni',
        'Juli',
        'August',
        'September',
        'Oktober',
        'November',
        'Dezember',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Jan.',
        'Febr.',
        'März',
        'Apr.',
        'Mai.',
        'Juni',
        'Juli',
        'Aug.',
        'Sep.',
        'Okt.',
        'Nov.',
        'Dez.',
    ]

    ERA_NAME = [
        #
        # Senarische Zeitalter der Menschheit
        #
        'SZM',
        #
        # vor das Senarische Zeitalter der Menschheit
        #
        'v. SZM',
    ]

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#X'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    DATE_FULL_FORMAT = '#@W, #d.#m.#X'
    DATE_FULL_LONG_FORMAT = '#W, #-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d.#m.#X, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'
    DST_NAME = 'Sommerzeit'
    DST_SHORT_NAME = 'SZ'
    DEFAULT_TIME_ZONE = 'Europe/Berlin'
    WEEK_NUMBER_SYMBOL = 'W.'
    DAY_NUMBER_SYMBOL = 'Tag'

    SEASON_NAME = {
        'spring_cross_quarter': 'Übergang Winter – Frühling',
        'spring_equinox': 'Frühling',
        'summer_cross_quarter': 'Übergang Frühling – Sommer',
        'summer_solstice': 'Sommer',
        'autumn_cross_quarter': 'Übergang Sommer – Herbst',
        'autumn_equinox': 'Herbst',
        'winter_cross_quarter': 'Übergang Herbst – Winter',
        'winter_solstice': 'Winter',
    }

    MOON_PHASE = {
        'new': 'Neumond',
        'waxing_crescent': 'Zunehmender Sichelmond',
        'first_quarter': 'Zunehmender Halbmond',
        'waxing_gibbous': 'Zunehmender Mond',
        'full': 'Vollmond',
        'waning_gibbous': 'Abnehmender Mond',
        'third_quarter': 'Abnehmender Halbmond',
        'waning_crescent': 'Abnehmender Sichelmond',
    }

    #
    # Error messages
    #
    ERROR = 'Fehler'
    WEEKDAY_ERROR = 'Ungültiger Wochentag {weekday}'
    MONTH_ERROR = 'Ungültiger Monat {month}'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        return '.'

    UPPERCASE_MAPPING = {
        ord('ß'): 'ẞ',
    }
    LOWERCASE_MAPPING = {
        ord('ẞ'): 'ß',
    }

    DCC_TERM_NAME = [
        'Jahrfünftel‐Null',
        'Jahrfünftel‐Eins',
        'Jahrfünftel‐Zwei',
        'Jahrfünftel‐Drei',
        'Jahrfünftel‐Vier',
    ]

    DCC_TERM_ABBREVIATED_NAME = [
        'JF0',
        'JF1',
        'JF2',
        'JF3',
        'JF4',
    ]

    DCC_MONTH_NAME = [
        'Monat‐Null',
        'Monat‐Eins',
        'Monat‐Zwei',
        'Monat‐Drei',
        'Monat‐Vier',
        'Monat‐Fünf',
        'Monat‐Sechs',
        'Monat‐Einundsechs',
        'Monat‐Zweiundsechs',
        'Monat‐Dreiundsechs',
        'Monat‐Vierundsechs',
    ]

    DCC_WEEKDAY_NAME = [
        'Wochentag‐Null',
        'Wochentag‐Eins',
        'Wochentag‐Zwei',
        'Wochentag‐Drei',
        'Wochentag‐Vier',
        'Wochentag‐Fünf',
    ]

    DCC_WEEKDAY_ABBREVIATED_NAME = [
        'WT0',
        'WT1',
        'WT2',
        'WT3',
        'WT4',
        'WT5',
    ]

    DCC_NUMBER = [
        'Null',
        'Eins',
        'Zwei',
        'Drei',
        'Vier',
        'Fünf',
        'Sechs',
        'Einundsechs',
        'Zweiundsechs',
        'Dreiundsechs',
        'Vierundsechs',
    ]

    DCC_YEAR_COUNT = {
        None: '&󱹭>Y Jahre',
        SezimalInteger('1'): '&󱹭>Y Jahr',
    }

    DCC_TERM_COUNT = {
        None: '&-t Bimester',
        SezimalInteger('1'): '&-t Bimester',
    }

    DCC_MONTH_COUNT = {
        None: '&-m Monate',
        SezimalInteger('1'): '&-m Monat',
    }

    DCC_WEEK_COUNT = {
        None: '&-wM Wochen',
        SezimalInteger('1'): '&-wM Woche',
    }

    DCC_WEEK_IN_YEAR_COUNT = {
        None: '&-wY Wochen',
        SezimalInteger('1'): '&-wY Woche',
    }

    DCC_DAY_COUNT = {
        None: '&-d Tage',
        SezimalInteger('1'): '&-d Tag',
    }

    DCC_DAY_IN_YEAR_COUNT = {
        None: '&-dY Tage',
        SezimalInteger('1'): '&-dY Tag',
    }

    DCC_DAY_IN_WEEK_COUNT = {
        None: '&-dW Tage',
        SezimalInteger('1'): '&-dW Tag',
    }

    DCC_DATE_MONTH_DAY_SEPARATOR = ' und '
