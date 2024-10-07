

__all__ = ('SezimalLocaleUK',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleUK(SezimalLocale):
    LANG = 'uk'
    LANGUAGE = 'українська'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = '₴'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0

    WEEKDAY_NAME = [
        'понеділок',
        'вівторок',
        'середа',
        'четвер',
        'п’ятниця',
        'субота',
        'неділя',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'пн',
        'вт',
        'ср',
        'чт',
        'пт',
        'сб',
        'нд',
    ]

    MONTH_NAME= [
        'січня',
        'лютого',
        'березня',
        'квітня',
        'травня',
        'червня',
        'липня',
        'серпня',
        'вересня',
        'жовтня',
        'листопада',
        'грудня',
    ]

    MONTH_ABBREVIATED_NAME = [
        'січ.',
        'лют.',
        'бер.',
        'квіт.',
        'трав.',
        'черв.',
        'лип.',
        'серп.',
        'вер.',
        'жовт.',
        'лист.',
        'груд.',
    ]

    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#d.#m.#Y #@W'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d.#m.#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Kyiv'

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
    ERROR = 'Помилка'
    WEEKDAY_ERROR = 'Недійсний день тижня {weekday}'
    MONTH_ERROR = 'Недійсний місяць {month}'
    WEEK_NUMBER_SYMBOL = 'тиж'
