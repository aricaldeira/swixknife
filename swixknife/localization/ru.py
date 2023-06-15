

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
        'понеде́льник',
        'вто́рник',
        'среда́',
        'четве́рг',
        'пя́тница',
        'суббо́та',
        'воскресе́нье',
    ]

    WEEKDAY_NAME_GENITIVE = [
        'понеде́льника',
        'вто́рника',
        'среды́',
        'четверга́',
        'пя́тницы',
        'суббо́ты',
        'воскресе́нья',
    ]

    WEEKDAY_NAME_DATIVE = [
        'понеде́льнику',
        'вто́рнику',
        'среде́',
        'четвергу́',
        'пя́тнице',
        'суббо́те',
        'воскресе́нью',
    ]

    WEEKDAY_NAME_ACCUSATIVE = [
        'понеде́льник',
        'вто́рник',
        'сре́ду',
        'четве́рг',
        'пя́тницу',
        'суббо́ту',
        'воскресе́нье',
    ]

    WEEKDAY_NAME_INSTRUMENTAL = [
        'понеде́льником',
        'вто́рником',
        'средо́й',
        'четверго́м',
        'пя́тницей',
        'суббо́той',
        'воскресе́ньем',
    ]

    WEEKDAY_NAME_PREPOSITIONAL = [
        'понеде́льнике',
        'вто́рнике',
        'среде́',
        'четверге́',
        'пя́тнице',
        'суббо́те',
        'воскресе́нье',
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
        'янва́рь',
        'февра́ль',
        'ма́рт',
        'апре́ль',
        'ма́й',
        'ию́нь',
        'ию́ль',
        'а́вгуст',
        'сентя́брь',
        'октя́брь',
        'ноя́брь',
        'дека́брь',
    ]

    MONTH_NAME_GENITIVE = [
        'января́',
        'февраля́',
        'ма́рта',
        'апре́ля',
        'ма́я',
        'ию́ня',
        'ию́ля',
        'а́вгуста',
        'сентября́',
        'октября́',
        'ноября́',
        'декабря́',
    ]

    MONTH_NAME_DATIVE = [
        'январю́',
        'февралю́',
        'ма́рту',
        'апре́лю',
        'ма́ю',
        'ию́ню',
        'ию́лю',
        'а́вгусту',
        'сентябрю́',
        'октябрю́',
        'ноябрю́',
        'декабрю́',
    ]

    MONTH_NAME_ACCUSATIVE = [
        'янва́рь',
        'февра́ль',
        'ма́рт',
        'апре́ль',
        'ма́й',
        'ию́нь',
        'ию́ль',
        'а́вгуст',
        'сентя́брь',
        'октя́брь',
        'ноя́брь',
        'дека́брь',
    ]

    MONTH_NAME_INSTRUMENTAL = [
        'январём',
        'февралём',
        'ма́ртом',
        'апре́лем',
        'ма́ем',
        'ию́нем',
        'ию́лем',
        'а́вгустом',
        'сентябрём',
        'октябрём',
        'ноябрём',
        'декабрём',
    ]

    MONTH_NAME_PREPOSITIONAL = [
        'январе́',
        'феврале́',
        'ма́рте',
        'апре́ле',
        'ма́е',
        'ию́не',
        'ию́ле',
        'а́вгусте',
        'сентябре́',
        'октябре́',
        'ноябре́',
        'декабре́',
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
