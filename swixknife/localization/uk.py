

__all__ = ('SezimalLocaleUK',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')

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

    MONTH_NAME = [
        'січень',
        'лютий',
        'березень',
        'квітень',
        'травень',
        'червень',
        'липень',
        'серпень',
        'вересень',
        'жовтень',
        'листопад',
        'грудень',
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

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d-#O #$GM #Y р.'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d-#O #$GM #Y р., #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Kyiv'
    ISO_DATE_LONG_FORMAT = '%-d. %$GM %Y р.'
    DATE_TEXT_SHORT_MONTH_FORMAT = '#$GM'
    TEXT_MONTH_DAY_FORMAT = '#-d-#O #$GM'
    YEAR_TEXT_MONTH_FORMAT = '#$NM #Y р.'
    ISO_YEAR_TEXT_MONTH_FORMAT = '%$NM %Y р.'

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
    DAY_NUMBER_SYMBOL = 'день'

    CASE_NOMINATIVE = 'N'
    CASE_GENITIVE = 'G'
    CASE_DATIVE = 'D'
    CASE_ACCUSATIVE = 'A'
    CASE_INSTRUMENTAL = 'I'
    CASE_LOCATIVE = 'L'
    CASE_VOCATIVE = 'V'

    CASES = [
        CASE_NOMINATIVE,
        CASE_GENITIVE,
        CASE_DATIVE,
        CASE_ACCUSATIVE,
        CASE_INSTRUMENTAL,
        CASE_LOCATIVE,
        CASE_VOCATIVE,
    ]

    WEEKDAY_NAME_GENITIVE = [
        'понеділка',
        'вівторка',
        'середи',
        'четверга',
        'п’ятниці',
        'суботи',
        'неділі',
    ]

    WEEKDAY_NAME_DATIVE = [
        'понеділкові',
        'вівторкові',
        'середі',
        'четвергові',
        'п’ятниці',
        'суботі',
        'неділі',
    ]

    WEEKDAY_NAME_ACCUSATIVE = [
        'понеділок',
        'вівторок',
        'середу',
        'четвер',
        'п’ятницю',
        'суботи',
        'неділю',
    ]

    WEEKDAY_NAME_INSTRUMENTAL = [
        'понеділком',
        'вівторком',
        'середою',
        'четвергом',
        'п’ятницею',
        'суботою',
        'неділею',
    ]

    WEEKDAY_NAME_LOCATIVE = [
        'понеділкові',
        'вівторкові',
        'середі',
        'четвергу',
        'п’ятниці',
        'суботі',
        'неділі',
        'неділе',
    ]

    WEEKDAY_NAME_VOCATIVE = [
        'понеділку',
        'вівторку',
        'середо',
        'четвергу',
        'п’ятнице',
        'субото',
    ]

    MONTH_NAME_GENITIVE = [
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

    MONTH_NAME_DATIVE = [
        'січневі',
        'лютому',
        'березневі',
        'квітневі',
        'травневі',
        'червневі',
        'липневі',
        'серпневі',
        'вересневі',
        'жовтневі',
        'листопадові',
        'грудневі',
    ]

    MONTH_NAME_ACCUSATIVE = [
        'січень',
        'лютий',
        'березень',
        'квітень',
        'травень',
        'червень',
        'липень',
        'серпень',
        'вересень',
        'жовтневі',
        'листопад',
        'грудень',
    ]

    MONTH_NAME_INSTRUMENTAL = [
        'січнем',
        'лютим',
        'березнем',
        'квітнем',
        'травнем',
        'червнем',
        'липнем',
        'серпнем',
        'вереснем',
        'жовтнем',
        'листопадом',
        'груднем',
    ]

    MONTH_NAME_LOCATIVE = [
        'січню',
        'лютому',
        'березнем',
        'квітню',
        'травню',
        'червню',
        'липню',
        'серпню',
        'вересню',
        'жовтню',
        'листопаді',
        'грудню',
    ]

    MONTH_NAME_VOCATIVE = [
        'січню',
        'лютий',
        'березню',
        'квітню',
        'травню',
        'червню',
        'липню',
        'серпню',
        'вересню',
        'жовтню',
        'листопаде',
        'грудню',
    ]

    def weekday_name(self, weekday: SezimalInteger, case: str = CASE_ACCUSATIVE) -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        if case:
            case = case.upper()

            if case == self.CASE_GENITIVE:
                return self.WEEKDAY_NAME_GENITIVE[int(weekday.decimal)]
            elif case == self.CASE_DATIVE:
                return self.WEEKDAY_NAME_DATIVE[int(weekday.decimal)]
            elif case == self.CASE_ACCUSATIVE:
                return self.WEEKDAY_NAME_ACCUSATIVE[int(weekday.decimal)]
            elif case == self.CASE_INSTRUMENTAL:
                return self.WEEKDAY_NAME_INSTRUMENTAL[int(weekday.decimal)]
            elif case == self.CASE_LOCATIVE:
                return self.WEEKDAY_NAME_LOCATIVE[int(weekday.decimal)]
            elif case == self.CASE_VOCATIVE:
                return self.WEEKDAY_NAME_VOCATIVE[int(weekday.decimal)]

        return self.WEEKDAY_NAME[int(weekday.decimal)]

    def month_name(self, month: SezimalInteger, case: str = CASE_GENITIVE) -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month -= 1

        if case:
            case = case.upper()

            if case == self.CASE_GENITIVE:
                return self.MONTH_NAME_GENITIVE[int(month.decimal)]
            elif case == self.CASE_DATIVE:
                return self.MONTH_NAME_DATIVE[int(month.decimal)]
            elif case == self.CASE_ACCUSATIVE:
                return self.MONTH_NAME_ACCUSATIVE[int(month.decimal)]
            elif case == self.CASE_INSTRUMENTAL:
                return self.MONTH_NAME_INSTRUMENTAL[int(month.decimal)]
            elif case == self.CASE_LOCATIVE:
                return self.MONTH_NAME_LOCATIVE[int(month.decimal)]
            elif case == self.CASE_VOCATIVE:
                return self.MONTH_NAME_VOCATIVE[int(month.decimal)]

        return self.MONTH_NAME[int(month.decimal)]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if str(day)[-1] == '3':
            return 'є'

        return 'е'

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for case in self.CASES:
            if f'#${case}W' in fmt:
                fmt = fmt.replace(f'#${case}W', self.weekday_name(date.weekday, case))

            if f'#${case}M' in fmt:
                fmt = fmt.replace(f'#${case}M', self.month_name(date.month, case))

            if f'%${case}M' in fmt:
                fmt = fmt.replace(f'%${case}M', self.month_name(date.gregorian_month, case))

            if f'%${case}B' in fmt:
                fmt = fmt.replace(f'%${case}B', self.month_name(date.gregorian_month, case))

        return fmt
