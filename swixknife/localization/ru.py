

__all__ = ('SezimalLocaleRU',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleRU(SezimalLocale):
    LANG = 'ru'
    LANGUAGE = 'русский'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = '₽'
    CURRENCY_SUBUNIT_SYMBOL = 'к'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    CASE_NOMINATIVE = 'N'
    CASE_GENITIVE = 'G'
    CASE_DATIVE = 'D'
    CASE_ACCUSATIVE = 'A'
    CASE_INSTRUMENTAL = 'I'
    CASE_PREPOSITIONAL = 'P'

    CASES = [
        CASE_NOMINATIVE,
        CASE_GENITIVE,
        CASE_DATIVE,
        CASE_ACCUSATIVE,
        CASE_INSTRUMENTAL,
        CASE_PREPOSITIONAL,
    ]

    WEEKDAY_NAME = [
        'понедельник',
        'вторник',
        'среда',
        'четверг',
        'пятница',
        'суббота',
        'воскресенье',
    ]

    WEEKDAY_NAME_GENITIVE = [
        'понедельника',
        'вторника',
        'среды',
        'четверга',
        'пятницы',
        'субботы',
        'воскресенья',
    ]

    WEEKDAY_NAME_DATIVE = [
        'понедельнику',
        'вторнику',
        'среде',
        'четвергу',
        'пятнице',
        'субботе',
        'воскресенью',
    ]

    WEEKDAY_NAME_ACCUSATIVE = [
        'понедельник',
        'вторник',
        'среду',
        'четверг',
        'пятницу',
        'субботу',
        'воскресенье',
    ]

    WEEKDAY_NAME_INSTRUMENTAL = [
        'понедельником',
        'вторником',
        'средой',
        'четвергом',
        'пятницей',
        'субботой',
        'воскресеньем',
    ]

    WEEKDAY_NAME_PREPOSITIONAL = [
        'понедельнике',
        'вторнике',
        'среде',
        'четверге',
        'пятнице',
        'субботе',
        'воскресенье',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'пн',
        'вт',
        'ср',
        'чт',
        'пт',
        'сб',
        'вс',
    ]

    MONTH_NAME = [
        'январь',
        'февраль',
        'март',
        'апрель',
        'май',
        'июнь',
        'июль',
        'август',
        'сентябрь',
        'октябрь',
        'ноябрь',
        'декабрь',
    ]

    MONTH_NAME_GENITIVE = [
        'января',
        'февраля',
        'марта',
        'апреля',
        'мая',
        'июня',
        'июля',
        'августа',
        'сентября',
        'октября',
        'ноября',
        'декабря',
    ]

    MONTH_NAME_DATIVE = [
        'январю',
        'февралю',
        'марту',
        'апрелю',
        'маю',
        'июню',
        'июлю',
        'августу',
        'сентябрю',
        'октябрю',
        'ноябрю',
        'декабрю',
    ]

    MONTH_NAME_ACCUSATIVE = [
        'январь',
        'февраль',
        'март',
        'апрель',
        'май',
        'июнь',
        'июль',
        'август',
        'сентябрь',
        'октябрь',
        'ноябрь',
        'декабрь',
    ]

    MONTH_NAME_INSTRUMENTAL = [
        'январём',
        'февралём',
        'мартом',
        'апрелем',
        'маем',
        'июнем',
        'июлем',
        'августом',
        'сентябрём',
        'октябрём',
        'ноябрём',
        'декабрём',
    ]

    MONTH_NAME_PREPOSITIONAL = [
        'январе',
        'феврале',
        'марте',
        'апреле',
        'мае',
        'июне',
        'июле',
        'августе',
        'сентябре',
        'октябре',
        'ноябре',
        'декабре',
    ]

    MONTH_ABBREVIATED_NAME = [
        'янв.',
        'февр.',
        'мар.',
        'апр.',
        'мая',
        'июн.',
        'июл.',
        'авг.',
        'сент.',
        'окт.',
        'нояб.',
        'дек.',
    ]

    ERA_NAME = [
        #
        # Sesuma Homara Erao
        #
        'SHE',
        #
        # Antaŭ Sesuma Homara Erao
        #
        'aSHE',
    ]

    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d-#O #$GM #Y г.'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d.#m.#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d-#O #$GM #Y г., #u:#p:#a'
    DST_NAME = 'Летнее Время'
    DST_SHORT_NAME = 'ЛВ'
    DEFAULT_TIME_ZONE = 'Europe/Moscow'
    ISO_DATE_LONG_FORMAT = '%-d. %b %Y г.'
    DATE_TEXT_SHORT_MONTH_FORMAT = '#$GM'
    TEXT_MONTH_DAY_FORMAT = '#-d-#O #$GM'
    YEAR_TEXT_MONTH_FORMAT = '#$NM #Y г.'

    SEASON_NAME = {
        'spring_cross_quarter': 'Переход Зима – Весна',
        'spring_equinox': 'Весна',
        'summer_cross_quarter': 'Переход Весна – Лето',
        'summer_solstice': 'Лето',
        'autumn_cross_quarter': 'Переход Лето – Осень',
        'autumn_equinox': 'Осень',
        'winter_cross_quarter': 'Переход Осень – Зима',
        'winter_solstice': 'Зима',
    }

    MOON_PHASE = {
        'new': 'Новолуние',
        'waxing_crescent': 'Молодая',
        'first_quarter': 'Первая Четверть',
        'waxing_gibbous': 'Прибывающая',
        'full': 'Полнолуние',
        'waning_gibbous': 'Убывающая',
        'third_quarter': 'Последняя Четверть',
        'waning_crescent': 'Старая',
    }

    #
    # Error messages
    #
    ERROR = 'Ошибка'
    WEEKDAY_ERROR = 'Неверный день недели {weekday}'
    MONTH_ERROR = 'Неверный месяц {month}'
    WEEK_NUMBER_SYMBOL = 'нед'
    DAY_NUMBER_SYMBOL = 'день'

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
            elif case == self.CASE_PREPOSITIONAL:
                return self.WEEKDAY_NAME_PREPOSITIONAL[int(weekday.decimal)]

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
            elif case == self.CASE_PREPOSITIONAL:
                return self.MONTH_NAME_PREPOSITIONAL[int(month.decimal)]

        return self.MONTH_NAME[int(month.decimal)]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 3:
            return 'ье'

        return 'ое'

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for case in self.CASES:
            if f'#${case}W' in fmt:
                fmt = fmt.replace(f'#${case}W', self.weekday_name(date.weekday, case))

            if f'#${case}M' in fmt:
                fmt = fmt.replace(f'#${case}M', self.month_name(date.month, case))

        #
        # Dealing with:
        # в → во
        # с → со
        # от → ото
        # к → ко
        # над → надо
        # перед → передо
        # под → подо
        #
        for preposition in ['В', 'С', 'ОТ', 'К', 'НАД', 'ПЕРЕД', 'ПОД']:
            if f'#${preposition}W' in fmt:
                if date.weekday == 2:
                    fmt = fmt.replace(f'#${preposition}W', preposition.lower() + 'о')
                elif date.weekday == 3 and preposition != 'В':
                    fmt = fmt.replace(f'#${preposition}W', preposition.lower() + 'о')
                elif date.weekday == 11 and preposition == 'В':
                    fmt = fmt.replace(f'#${preposition}W', preposition.lower() + 'о')
                else:
                    fmt = fmt.replace(f'#${preposition}W', preposition.lower())

            if f'#${preposition}M' in fmt:
                if date.month == 2 and preposition == 'В':
                    fmt = fmt.replace(f'#${preposition}M', preposition.lower() + 'о')
                elif date.month in (1, 12) and preposition != 'В':
                    fmt = fmt.replace(f'#${preposition}M', preposition.lower() + 'о')
                else:
                    fmt = fmt.replace(f'#${preposition}M', preposition.lower())

        #
        # Special case:
        # о → об
        #
        if f'#$ОM' in fmt:
            if date.month in (1, 4, 10, 11, 12, 14):
                fmt = fmt.replace(f'#$ОM', 'об')
            else:
                fmt = fmt.replace(f'#$ОM', 'о')

        return fmt
