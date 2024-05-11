
import os

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalCalendar')

import time as _time
import datetime as _datetime
from decimal import Decimal

from ..date import SezimalDate
from ..time import SezimalTime
from ..date_time import SezimalDateTime
from ..sezimal_functions import *
from ...localization import sezimal_locale, SezimalLocale
from ...sezimal import Sezimal, SezimalInteger
from ...functions import SezimalRange
from .conversion import other_calendar_date_to_ordinal_date
from ...base import default_to_sezimal_digits, \
    default_niftimal_to_sezimal_digits
from ...user_preferences import user_preferences


WEEKDAY_MONDAY = 'MON'
WEEKDAY_TUESDAY = 'TUE'
WEEKDAY_WEDNESDAY = 'WED'
WEEKDAY_THURSDAY = 'THU'
WEEKDAY_FRIDAY = 'FRI'
WEEKDAY_SATURDAY = 'SAT'
WEEKDAY_SUNDAY = 'SUN'

WEEKDAYS = [
    WEEKDAY_MONDAY,
    WEEKDAY_TUESDAY,
    WEEKDAY_WEDNESDAY,
    WEEKDAY_THURSDAY,
    WEEKDAY_FRIDAY,
    WEEKDAY_SATURDAY,
    WEEKDAY_SUNDAY,
]

LTR_MARKER = '\u200e'
RTL_MARKER = '\u200f'

TERMINAL_COLOR_RESET = '\x1b[0m'
TERMINAL_COLOR_START = '\x1b['
TERMINAL_COLOR_END = 'm'


class SezimalCalendar:
    __slots__ = (
        '_date_time', '_locale', '_first_weekday',
        '_day_format', '_month_format', '_year_format', '_month_year_format',
        '_time_format', '_date_format',
        '_use_rtl', '_hemisphere',
        '_holidays', '_events',
        '_holidays_other_calendar', '_events_other_calendar',
    )
    def __new__(
        cls,
        date_time: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.date | _datetime.datetime | SezimalDate | SezimalDateTime = None,
        locale: str | SezimalLocale = None,
        first_weekday: str = WEEKDAY_MONDAY,
        day_format: str = None,
        month_format: str = None,
        year_format: str = None,
        month_year_format: str = None,
        time_format: str = None,
        date_format: str = None,
        use_rtl: bool = False,
        hemisphere: str = None,
    ):
        if date_time is None:
            date_time = SezimalDateTime.now()

        elif type(date_time) == _datetime.date:
            date_time = SezimalDate(date_time)
            date_time = SezimalDateTime.combine(date_time, SezimalTime.now())

        elif type(date_time) == _datetime.datetime:
            date_time = SezimalDateTime(date_time)

        elif type(date_time) == SezimalDate:
            date_time = SezimalDateTime.combine(date_time, SezimalTime.now())

        elif type(date_time) == SezimalDateTime:
            pass

        elif type(date_time) == str:
            if VALID_DATE_TIME_STRING.match(date_time):
                date_time = SezimalDateTime(date_time)

            elif VALID_DATE_PARTIAL_TIME_STRING.match(date_time):
                date_time = SezimalDateTime(date_time)

            elif VALID_DATE_STRING.match(date_time):
                date_time = SezimalDateTime.combine(SezimalDate(date_time), SezimalTime.now())

            elif VALID_TIME_STRING.match(date_time):
                date_time = SezimalDateTime.combine(SezimalDate.today(), SezimalTime(date_time))

            else:
                year = SezimalInteger(date_time)
                date_time = SezimalDateTime.now()
                date_time = date_time.replace(year=year)

        else:
            year = SezimalInteger(date_time)
            date_time = SezimalDateTime.now()
            date_time = date_time.replace(year=year)

        if type(locale) != SezimalLocale:
            locale = sezimal_locale(locale)

        if (not first_weekday) or first_weekday.upper() in ('LOC', 'LOCALE'):
            first_weekday = locale.FIRST_WEEKDAY

        elif first_weekday not in WEEKDAYS:
            raise ValueError(f'Wrong first day of the week: {first_weekday}; must be one of the following: MON, TUE, WED, THU, FRI, SAT, SUN, or LOC for using the locale’s default first weekday.')

        if hemisphere and hemisphere.upper() not in ('S', 'N', 'E'):
            raise ValueError(f'Wrong hemisphere: {hemisphere}; accepted values are S for South, N for North, E for Equator')

        self = object.__new__(cls)
        self._date_time = date_time
        self._locale = locale
        self._first_weekday = first_weekday
        self._use_rtl = use_rtl
        self._hemisphere = hemisphere or locale.DEFAULT_HEMISPHERE

        if not day_format:
            if locale.DIGITS:
                if locale.RTL:
                    day_format = RTL_MARKER + '#?-d' + LTR_MARKER
                else:
                    day_format = '#?-d'

            else:
                day_format = '#-d'

        elif day_format and locale.DIGITS and locale.RTL:
            if day_format[0] != RTL_MARKER:
                day_format = RTL_MARKER + day_format

            if day_format[-1] != LTR_MARKER:
                day_format += LTR_MARKER

        if not month_format:
            if locale.RTL:
                month_format = RTL_MARKER + '#M' + LTR_MARKER
            else:
                month_format = '#M'

        elif month_format and locale.DIGITS and locale.RTL:
            if month_format[0] != RTL_MARKER:
                month_format = RTL_MARKER + month_format

            if month_format[-1] != LTR_MARKER:
                month_format += LTR_MARKER

        if not year_format:
            if locale.DIGITS:
                if locale.RTL:
                    year_format = RTL_MARKER + '#?Y' + LTR_MARKER
                else:
                    year_format = '#?Y'

            else:
                year_format = '#Y'

        elif year_format and locale.DIGITS and locale.RTL:
            if year_format[0] != RTL_MARKER:
                year_format = RTL_MARKER + year_format

            if year_format[-1] != LTR_MARKER:
                year_format += LTR_MARKER

        if not month_year_format:
            if locale.DIGITS:
                if locale.RTL:
                    month_year_format = RTL_MARKER + '#M #?Y' + LTR_MARKER
                else:
                    month_year_format = '#M #?Y'

            else:
                month_year_format = '#M #Y'

        elif month_year_format and locale.DIGITS and locale.RTL:
            if month_year_format[0] != RTL_MARKER:
                month_year_format = RTL_MARKER + month_year_format

            if month_year_format[-1] != LTR_MARKER:
                month_year_format += LTR_MARKER

        self._day_format = day_format
        self._month_format = month_format
        self._year_format = year_format
        self._month_year_format = month_year_format

        if time_format and locale.DIGITS and locale.RTL:
            if time_format[0] != RTL_MARKER:
                time_format = RTL_MARKER + time_format

            if time_format[-1] != LTR_MARKER:
                time_format += LTR_MARKER

        if date_format and locale.DIGITS and locale.RTL:
            if date_format[0] != RTL_MARKER:
                date_format = RTL_MARKER + date_format

            if date_format[-1] != LTR_MARKER:
                date_format += LTR_MARKER

        self._time_format = time_format or locale.TIME_FORMAT
        self._date_format = date_format or locale.DATE_FORMAT

        self._prepare_holiday_events()

        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}('{self.date_time}', locale='{self.locale.LANG}', first_weekday='{self.first_weekday}')"

    @property
    def date_time(self):
        return self._date_time

    @property
    def locale(self):
        return self._locale

    @property
    def first_weekday(self):
        return self._first_weekday

    def _weeks(self, month: SezimalInteger, year: SezimalInteger = None) -> list[list[int]]:
        weeks = []

        if self.first_weekday == WEEKDAY_MONDAY:
            weeks += [[]]
        elif self.first_weekday == WEEKDAY_SUNDAY:
            weeks += [[0]]
        elif self.first_weekday == WEEKDAY_SATURDAY:
            weeks += [[0, 0]]
        elif self.first_weekday == WEEKDAY_FRIDAY:
            weeks += [[0, 0, 0]]
        elif self.first_weekday == WEEKDAY_THURSDAY:
            weeks += [[0, 0, 0, 0]]
        elif self.first_weekday == WEEKDAY_WEDNESDAY:
            weeks += [[0, 0, 0, 0, 0]]
        elif self.first_weekday == WEEKDAY_TUESDAY:
            weeks += [[0, 0, 0, 0, 0, 0]]

        date = self.date_time.date.replace(month=month, year=year)

        if date.is_long_month:
            days = SezimalInteger(55)
        else:
            days = SezimalInteger(44)

        for day in SezimalRange(1, days + 1):
            if len(weeks[-1]) == 7:
                weeks += [[]]

            weeks[-1].append(day)

        if len(weeks[-1]) < 7:
            weeks[-1] += [0 for i in range(7 - len(weeks[-1]))]

        return weeks

    def _week_header(self) -> list[str]:
        if self.first_weekday == WEEKDAY_MONDAY:
            header = [
                WEEKDAY_MONDAY,
                WEEKDAY_TUESDAY,
                WEEKDAY_WEDNESDAY,
                WEEKDAY_THURSDAY,
                WEEKDAY_FRIDAY,
                WEEKDAY_SATURDAY,
                WEEKDAY_SUNDAY,
            ]
        elif self.first_weekday == WEEKDAY_SUNDAY:
            header = [
                WEEKDAY_SUNDAY,
                WEEKDAY_MONDAY,
                WEEKDAY_TUESDAY,
                WEEKDAY_WEDNESDAY,
                WEEKDAY_THURSDAY,
                WEEKDAY_FRIDAY,
                WEEKDAY_SATURDAY,
            ]

        elif self.first_weekday == WEEKDAY_SATURDAY:
            header = [
                WEEKDAY_SATURDAY,
                WEEKDAY_SUNDAY,
                WEEKDAY_MONDAY,
                WEEKDAY_TUESDAY,
                WEEKDAY_WEDNESDAY,
                WEEKDAY_THURSDAY,
                WEEKDAY_FRIDAY,
            ]

        elif self.first_weekday == WEEKDAY_FRIDAY:
            header = [
                WEEKDAY_FRIDAY,
                WEEKDAY_SATURDAY,
                WEEKDAY_SUNDAY,
                WEEKDAY_MONDAY,
                WEEKDAY_TUESDAY,
                WEEKDAY_WEDNESDAY,
                WEEKDAY_THURSDAY,
            ]

        elif self.first_weekday == WEEKDAY_THURSDAY:
            header = [
                WEEKDAY_THURSDAY,
                WEEKDAY_FRIDAY,
                WEEKDAY_SATURDAY,
                WEEKDAY_SUNDAY,
                WEEKDAY_MONDAY,
                WEEKDAY_TUESDAY,
                WEEKDAY_WEDNESDAY,
            ]

        elif self.first_weekday == WEEKDAY_WEDNESDAY:
            header = [
                WEEKDAY_WEDNESDAY,
                WEEKDAY_THURSDAY,
                WEEKDAY_FRIDAY,
                WEEKDAY_SATURDAY,
                WEEKDAY_SUNDAY,
                WEEKDAY_MONDAY,
                WEEKDAY_TUESDAY,
            ]

        elif self.first_weekday == WEEKDAY_TUESDAY:
            header = [
                WEEKDAY_TUESDAY,
                WEEKDAY_WEDNESDAY,
                WEEKDAY_THURSDAY,
                WEEKDAY_FRIDAY,
                WEEKDAY_SATURDAY,
                WEEKDAY_SUNDAY,
                WEEKDAY_MONDAY,
            ]

        return header

    def _month_template(self, month: SezimalInteger = None, year: SezimalInteger = None, with_year: bool = True) -> str:
        today = self.date_time.date

        if not month:
            month = self.date_time.month

        if not year:
            year = self.date_time.year

        date = SezimalDate(year, month, 30)

        calendar = ''

        if self._day_format in ('#-dY', '#dY', '#!-dY', '#!dY', '#?-dY', '#?dY'):
            width = 4
        else:
            width = 3

        if with_year:
            header = date.format(self._month_year_format, locale=self.locale)
        else:
            header = date.format(self._month_format, locale=self.locale)

        calendar += f'[SM_{str(month).zfill(2)}]' + self.locale.center(header, (SezimalInteger(11) * width) + 10) + f'[EM_{str(month).zfill(2)}]\n'

        header = self._week_header()

        if self.locale.RTL and self._use_rtl:
            header = header[::-1]
            calendar += ' '.join(header) + '\n'
        else:
            calendar += ' '.join(header) + '\n'

        if self.locale.RTL:
            monday =    f'{RTL_MARKER}{self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[0], 0, width)}{LTR_MARKER}'
            tuesday =   f'{RTL_MARKER}{self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[1], 0, width)}{LTR_MARKER}'
            wednesday = f'{RTL_MARKER}{self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[2], 0, width)}{LTR_MARKER}'
            thursday =  f'{RTL_MARKER}{self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[3], 0, width)}{LTR_MARKER}'
            friday =    f'{RTL_MARKER}{self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[4], 0, width)}{LTR_MARKER}'
            saturday =  f'{RTL_MARKER}{self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[5], 0, width)}{LTR_MARKER}'
            sunday =    f'{RTL_MARKER}{self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[6], 0, width)}{LTR_MARKER}'

        else:
            monday =    self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[0], 0, width)
            tuesday =   self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[1], 0, width)
            wednesday = self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[2], 0, width)
            thursday =  self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[3], 0, width)
            friday =    self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[4], 0, width)
            saturday =  self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[5], 0, width)
            sunday =    self.locale.slice(self.locale.WEEKDAY_ABBREVIATED_NAME[6], 0, width)

        calendar = calendar.replace(WEEKDAY_MONDAY,    '[SW_01]' + self.locale.rjust(monday, width) + '[EW_01]')
        calendar = calendar.replace(WEEKDAY_TUESDAY,   '[SW_02]' + self.locale.rjust(tuesday, width) + '[EW_02]')
        calendar = calendar.replace(WEEKDAY_WEDNESDAY, '[SW_03]' + self.locale.rjust(wednesday, width) + '[EW_03]')
        calendar = calendar.replace(WEEKDAY_THURSDAY,  '[SW_04]' + self.locale.rjust(thursday, width) + '[EW_04]')
        calendar = calendar.replace(WEEKDAY_FRIDAY,    '[SW_05]' + self.locale.rjust(friday, width) + '[EW_05]')
        calendar = calendar.replace(WEEKDAY_SATURDAY,  '[SW_10]' + self.locale.rjust(saturday, width) + '[EW_10]')
        calendar = calendar.replace(WEEKDAY_SUNDAY,    '[SW_11]' + self.locale.rjust(sunday, width) + '[EW_11]')

        for week in self._weeks(month, year):
            if self.locale.RTL and self._use_rtl:
                week = week[::-1]

            for day in week:
                if day == 0:
                    calendar += f'[Sd_00]{"".ljust(width)}[Ed_00] '
                    continue

                date = SezimalDate(today.year, month, day)
                key = date.format('#m-#d')

                if key in self._holidays_other_calendar:
                    tag = 'f'
                elif key in self._events_other_calendar:
                    tag = 'a'
                elif key in self._holidays:
                    tag = 'h'
                elif key in self._events:
                    tag = 'e'
                elif date.day == 30 and date.month in (2, 5, 12, 15):
                    tag = 'q'
                else:
                    tag = 'd'

                if date == today:
                    tag = tag.upper()

                calendar += f'[S{tag}_{str(day).zfill(2)}]' + self.locale.rjust(date.format(self._day_format, locale=self.locale), width) + f'[E{tag}_{str(day).zfill(2)}] '

            calendar = calendar[:-1] + '\n'

        return calendar

    def _quarter_template(self, month: SezimalInteger = None, with_year: bool = True) -> str:
        today = self.date_time.date

        if not month:
            month = self.date_time.month

        first_month_date = SezimalDate(self.date_time.year, month, 1)
        second_month_date = SezimalDate.from_ordinal_date(first_month_date.ordinal_date + 55).replace(day=1)
        third_month_date = SezimalDate.from_ordinal_date(second_month_date.ordinal_date + 55).replace(day=1)

        first_month_calendar = self._month_template(first_month_date.month, first_month_date.year, with_year=with_year)
        second_month_calendar = self._month_template(second_month_date.month, second_month_date.year, with_year=with_year)
        third_month_calendar = self._month_template(third_month_date.month, third_month_date.year, with_year=with_year)

        if self._locale.RTL and self._use_rtl:
            calendar = self._merge_lines(second_month_calendar, first_month_calendar)
            calendar = self._merge_lines(third_month_calendar, calendar)
        else:
            calendar = self._merge_lines(first_month_calendar, second_month_calendar)
            calendar = self._merge_lines(calendar, third_month_calendar)

        return calendar

    def _merge_lines(self, calendar_1: str, calendar_2: str) -> str:
        lines_1 = calendar_1.splitlines()
        lines_2 = calendar_2.splitlines()

        max_line_size_1 = 0
        max_line_size_2 = 0

        for line in lines_1:
            cleaned_line = self._clear_template(line)

            if max_line_size_1 < self.locale.len(cleaned_line):
                max_line_size_1 = self.locale.len(cleaned_line)

        for line in lines_2:
            cleaned_line = self._clear_template(line)

            if max_line_size_2 < self.locale.len(cleaned_line):
                max_line_size_2 = self.locale.len(cleaned_line)

        amount_lines_1 = len(lines_1)
        amount_lines_2 = len(lines_2)

        calendar = ''

        for i in range(max(amount_lines_1, amount_lines_2)):
            if i >= amount_lines_1:
                line_1 = self.locale.ljust('', max_line_size_1)
            else:
                # line_1 = lines_1[i]
                line_1 = self.locale.ljust(lines_1[i], max_line_size_1)

            if i >= amount_lines_2:
                line_2 = self.locale.ljust('', max_line_size_2)
            else:
                # line_2 = lines_2[i]
                line_2 = self.locale.ljust(lines_2[i], max_line_size_2)

            calendar += line_1 + '  ' + line_2 + '\n'

        return calendar

    def _year_template(self) -> str:
        calendar = '\n[SY]' + self.locale.center(self.date_time.format(self._year_format, self.locale), 222) + '[EY]\n\n'
        calendar += self._quarter_template(1, with_year=False)
        calendar += '\n' + self._quarter_template(4, with_year=False)
        calendar += '\n' + self._quarter_template(11, with_year=False)
        calendar += '\n' + self._quarter_template(14, with_year=False)[:-1]
        return calendar

    def _clear_template(self, calendar: str) -> str:
        for tag in (
            'Y', 'd_00', 'q_30', 'Q_30',
            'M_01', 'M_02', 'M_03', 'M_04', 'M_05', 'M_10',
            'M_11', 'M_12', 'M_13', 'M_14', 'M_15', 'M_20',
            'W_01', 'W_02', 'W_03', 'W_04', 'W_05', 'W_10', 'W_11',
        ):
            calendar = calendar.replace(f'[S{tag}]', '').replace(f'[E{tag}]', '')

        for day in SezimalRange(1, 100):
            for tag in ('h', 'H', 'f', 'F', 'e', 'E', 'a', 'A', 'd', 'D'):
                calendar = calendar.replace(f'[S{tag}_{str(day).zfill(2)}]', '').replace(f'[E{tag}_{str(day).zfill(2)}]', '')

        return calendar

    def month(self, month: SezimalInteger = None, year: SezimalInteger = None,
              include_time: bool = True, include_events: bool = True,
              appended_text: str = None, return_template: bool = False) -> str:
        return self._clear_template(self._month_template(month, year))[:-1]

    def quarter(self, month: SezimalInteger = None, year: SezimalInteger = None) -> str:
        return self._clear_template(self._quarter_template(month, year))[:-1]

    def year(self):
        return self._clear_template(self._year_template())[:-1]

    def _prepare_holiday_events(self):
        self._holidays = {}
        self._holidays_other_calendar = {}
        self._events = {}
        self._events_other_calendar = {}

        holidays = self._locale.HOLIDAYS
        holidays_other_calendar = self._locale.HOLIDAYS_OTHER_CALENDAR
        events = []
        events_other_calendar = []

        up = user_preferences(self._locale)

        if 'HOLIDAYS' in up:
            holidays += up['HOLIDAYS']

        if 'HOLIDAYS_OTHER_CALENDAR' in up:
            holidays_other_calendar += up['HOLIDAYS_OTHER_CALENDAR']

        if 'EVENTS' in up:
            events += up['EVENTS']

        if 'EVENTS_OTHER_CALENDAR' in up:
            events_other_calendar += up['EVENTS_OTHER_CALENDAR']

        self._compute_convert_age_holidays_events(self._holidays, holidays)
        self._compute_convert_age_holidays_events(self._holidays_other_calendar, holidays_other_calendar)
        self._compute_convert_age_holidays_events(self._events, events)
        self._compute_convert_age_holidays_events(self._events_other_calendar, events_other_calendar)

    def _compute_convert_age_holidays_events(self, date_dict, date_list):
        for key, name in date_list:
            ordinal_date, ymd, age = other_calendar_date_to_ordinal_date(key, self._date_time.year)
            year, month, day = ymd

            date = SezimalDate.from_ordinal_date(ordinal_date)

            if age < 0:
                continue

            if date.year != self._date_time.year:
                continue

            new_key = date.format('#m-#d')

            if '#i' in name:
                if '9' in self._day_format:
                    age = age.decimal_formatted_number
                elif '↋' in self._day_format:
                    age = age.dozenal_formatted_number
                elif '@' in self._day_format:
                    if '!' in self._day_format:
                        age = default_niftimal_to_sezimal_digits(age.niftimal_formatted_number)
                    else:
                        age = age.niftimal_formatted_number

                elif '!' in self._day_format:
                    age = default_to_sezimal_digits(str(age))

                if '?' in self._day_format:
                    age = self._locale.digit_replace(str(age))

                name = name.replace('#i', str(age))

            if '#9i' in name:
                name = name.replace('#9i', str(age.decimal))

            if '%i' in name:
                name = name.replace('%i', str(age.decimal))

            if '#↋i' in name:
                name = name.replace('#↋i', age.dozenal)

            if '#@i' in name:
                name = name.replace('#@i', age.niftimal)

            if '%d' in name:
                name = name.replace('%d', str(day).zfill(2))

            if '%-d' in name:
                name = name.replace('%-d', str(day))

            if '%m' in name:
                name = name.replace('%m', str(month).zfill(2))

            if '%-m' in name:
                name = name.replace('%-m', str(month))

            if '%y' in name:
                name = name.replace('%y', str(year)[-2:])

            if '%Y' in name:
                name = name.replace('%Y', str(year).zfill(4))

            name = date.format(name, locale=self._locale)

            if '?' in self._day_format:
                name = self._locale.digit_replace(name)

            if new_key in date_dict:
                if name.startswith(date_dict[new_key]) \
                    or date_dict[new_key].startswith(name):
                    date_dict[new_key] = name
                else:
                    date_dict[new_key] += '; ' + name
            else:
                date_dict[new_key] = name
