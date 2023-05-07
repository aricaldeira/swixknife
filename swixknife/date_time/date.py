#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# SezimalCalendar - The Symmetry454 Calendar, with Holocene Epoch and Sezimal in Python
#
# Copyright (C) 2023–
# Copyright (C) Ari Caldeira <aricaldeira at gmail.com>
#
# Original calendar documentation is Public Domain by it’s author:
# http://individual.utoronto.ca/kalendis/symmetry.htm
#

__all__ = ('SezimalDate')

import time as _time
import datetime as _datetime
import locale

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..functions import floor, ceil
from ..base import decimal_format
from .gregorian_functions import ordinal_date_to_gregorian_year_month_day

#
# Epoch
#
# Julian date -1_0521_5450.3 → -1_930_998.5_dec → -9_999-01-03_dec GREGORIAN
#
EPOCH = SezimalInteger('-2_1014_1212')  # -3_652_424_dec
EPOCH_JULIAN_DATE = Sezimal('-1_0521_5450.3')  # -1_930_998.5_dec

ISO_EPOCH = SezimalInteger('1')
ISO_EPOCH_JULIAN_DATE = Sezimal('1_0052_1320.3')  # 1_721_424.5_dec → 01-01-01_dec GREGORIAN
# ISO_YEAR_DIFF = SezimalInteger('10_0000')  # 7_776_dec
ISO_YEAR_DIFF = SezimalInteger('11_4144')  # 10_000_dec
# ISO_YEAR_DIFF = SezimalInteger('12_0000')  # 10_368_dec
# ISO_YEAR_DIFF = SezimalInteger('13_0000')  # 11_664_dec
# ISO_YEAR_DIFF = SezimalInteger('14_0000')  # 12_960_dec
# ISO_YEAR_DIFF = SezimalInteger('15_0000')  # 14_256_dec
# ISO_YEAR_DIFF = SezimalInteger('20_0000')  # 15_552_dec
ISO_HOLOCENE_YEAR_DIFF = SezimalInteger('11_4144')  # 10_000_dec


#
# For compatibility with Python’s original date and datetime,
# MAXYEAR has to be 1 year less, because:
#
# 23_2331-20-55 (19_999-12-35_dec) SEZIMAL → 10_000-01-02_dec GREGORIAN → 2_1013_5405 (3_652_061_dec) ORDINAL
# 23_2331-20-54 (19_999-12-34_dec) SEZIMAL → 10_000-01-01_dec GREGORIAN → 2_1013_5404 (3_652_060_dec) ORDINAL
#
# This is the actual maximum Python date
# 23_2331-20-53 (19_999-12-33_dec) SEZIMAL →  9_999-12-31_dec GREGORIAN → 2_1013_5403 (3_652_059_dec) ORDINAL
#
# So we use the maximum full year we can use
# 23_2330-20-44 (19_998-12-28_dec) SEZIMAL → 9_998-12-27_dec GREGORIAN → 2_1013_3550 (3_651_690_dec) ORDINAL
#
MIN_ISO_YEAR = ISO_YEAR_DIFF + SezimalInteger('1')
MAX_ISO_YEAR = ISO_YEAR_DIFF + SezimalInteger('11_4144')
MINYEAR = SezimalInteger('1')
MAXYEAR = MAX_ISO_YEAR - SezimalInteger('1')
MAXORDINAL = SezimalInteger('2_1013_3550')


CYCLE_MEAN_YEAR = Sezimal('1405') + (Sezimal('155') / Sezimal('1205'))  # 365_dec + (71_dec / 293_dec)

#
# 13_1230-01-04 SEZIMAL → 1_970-01-01_dec GREGORIAN → 2322_5243 (719_163_dec)
#
POSIX_EPOCH = SezimalInteger('2322_5243')
POSIX_JULIAN_DATE = Sezimal('1_2415_1003.3')

_LEAP_FACTOR = SezimalInteger('402')
# _LEAP_FACTOR = SezimalInteger('1005')

#
# -1 is just a placeholder, so we don’t need to worry about month number 0
#
DAYS_IN_MONTH = [
    SezimalInteger('-1'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
]
DAYS_BEFORE_MONTH = [SezimalInteger('-1')]

days_before_month = SezimalInteger('0')

for days_in_month in DAYS_IN_MONTH[1:]:
    DAYS_BEFORE_MONTH.append(days_before_month)
    days_before_month += days_in_month

del days_before_month, days_in_month


def _is_leap(year):
    is_leap = ((SezimalInteger('124') * year) + _LEAP_FACTOR) % SezimalInteger('1205') < SezimalInteger('124')
    return is_leap


def _days_before_year(year):
    "year -> number of days before January 1st of year."
    year -= SezimalInteger('1')

    dby = SezimalInteger('1404') * year
    weeks = (SezimalInteger('124') * year) + _LEAP_FACTOR
    weeks *= SezimalInteger(1) / SezimalInteger('1205')
    dby += SezimalInteger('11') * floor(weeks)

    return dby


def _days_in_month(year, month):
    "year, month -> number of days in that month in that year."
    assert 1 <= month <= 20, month

    if month == 20 and _is_leap(year):
        return SezimalInteger('55')

    return DAYS_IN_MONTH[month]


def _days_before_month(month):
    "year, month -> number of days in year preceding first day of month."
    assert 1 <= month <= 20, f'month must be in 1..20: {month}'

    return DAYS_BEFORE_MONTH[month]


def _year_month_day_to_ordinal(year, month, day):
    "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
    assert 1 <= month <= 20, f'month must be in 1..20: {month}'

    year -= ISO_YEAR_DIFF

    days_in_month = _days_in_month(year, month)

    assert 1 <= day <= days_in_month, (f'day must be in 1..{days_in_month}: day')

    ordinal_date = _days_before_year(year)
    ordinal_date += _days_before_month(month)
    ordinal_date += day

    return SezimalInteger(ordinal_date)


def _first_day_year(year):
    return _days_before_year(year) + SezimalInteger('1')


def _ordinal_to_year(ordinal_date):
    year = ordinal_date - ISO_EPOCH
    year /= CYCLE_MEAN_YEAR
    year = ceil(year)
    return year


def _ordinal_to_year_month_day(ordinal_date):
    ordinal_date = SezimalInteger(ordinal_date)
    #
    # First, we find the year corresponding to the ordinal date
    #
    year = _ordinal_to_year(ordinal_date)

    first_day_year = _first_day_year(year)

    #
    # We now check if the year is correct
    # The start of the year is either on the year or we must increment the year
    #
    if ordinal_date > first_day_year:
        #
        # Check if the ordinal date informed may be
        # on the leap week of December or the next year
        #
        if ordinal_date - first_day_year >= SezimalInteger('1404'):
            first_day_next_year = _first_day_year(year + SezimalInteger('1'))

            #
            # If the given ordinal date is after the next year’s first day,
            # then it is on the next year
            #
            if ordinal_date >= first_day_next_year:
                year += SezimalInteger('1')
                first_day_year = first_day_next_year

    #
    # The year estimate is too far in the future, go back 1 year
    #
    elif first_day_year > ordinal_date:
        year -= SezimalInteger('1')
        first_day_year = _first_day_year(year)

    day_in_year = SezimalInteger(ordinal_date - first_day_year + SezimalInteger('1'))
    week_in_year = SezimalInteger(ceil(day_in_year / SezimalInteger('11')))
    quarter = SezimalInteger(ceil((SezimalInteger('4') / SezimalInteger('125')) *  week_in_year))
    day_in_quarter = SezimalInteger(day_in_year - (SezimalInteger('231') * (quarter - SezimalInteger('1'))))
    week_in_quarter = SezimalInteger(ceil(day_in_quarter / SezimalInteger('11')))
    month_in_quarter = SezimalInteger(ceil((SezimalInteger('2') / SezimalInteger('13')) * week_in_quarter))
    month = SezimalInteger((SezimalInteger('3') * (quarter - SezimalInteger('1'))) + month_in_quarter)

    #
    # The day is in the leap week
    #
    if month == SezimalInteger('21'):
        month = SezimalInteger('20')

    day = SezimalInteger(day_in_year - _days_before_month(month))

    year += ISO_YEAR_DIFF

    return year, month, day, day_in_year, week_in_year


def _check_date_fields(year, month, day):
    # if not MINYEAR <= year <= MAXYEAR:
    #     raise ValueError(f'Year must be in {MINYEAR}..{MAXYEAR}', year)

    if not 1 <= month <= 20:
        raise ValueError('Month must be in 1..20', month)

    year -= ISO_YEAR_DIFF

    days_in_month = _days_in_month(year, month)

    if not 1 <= day <= days_in_month:
        raise ValueError(f'Day must be in 1..{days_in_month} for month {year}-{str(month).zfill(2)}', day)

    return year, month, day


class SezimalDate():
    __slots__ = '_year', '_month', '_day', '_hashcode', '_gregorian_date', '_is_leap', '_ordinal_date', '_weekday'

    def __new__(cls, year: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.date,
                month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
                day: str | int | float | Decimal | Sezimal | SezimalInteger = None):
        if month is None:
            if type(year) in (_datetime.date, cls):
                return cls.fromordinal(Decimal(year.toordinal()))

            elif type(year) == str:
                year, month, day = year.split('-')
                year = SezimalInteger(year)
                month = SezimalInteger(month)
                day = SezimalInteger(day)

        year = SezimalInteger(year)
        month = SezimalInteger(month)
        day = SezimalInteger(day)

        _check_date_fields(year, month, day)

        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        self._ordinal_date = _year_month_day_to_ordinal(year, month, day)

        if self._ordinal_date <= 0:
            self._weekday = SezimalInteger((self._ordinal_date.decimal - EPOCH.decimal) % SezimalInteger('11').decimal)
        else:
            self._weekday = SezimalInteger((self._ordinal_date.decimal - 1) % SezimalInteger('11').decimal)

        self._hashcode = -1
        self._is_leap = _is_leap(year)

        gregorian_date = ordinal_date_to_gregorian_year_month_day(int(self._ordinal_date.decimal))

        if gregorian_date[0] >= 1 and gregorian_date[0] <= 10_000:
            self._gregorian_date = _datetime.date(*gregorian_date)
        else:
            self._gregorian_date = gregorian_date

        return self

    # Additional constructors

    @classmethod
    def fromtimestamp(cls, timestamp):
        "Construct a date from a POSIX timestamp (like time.time())."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(timestamp)
        x = _datetime.date(y, m, d)
        return cls.fromordinal(x.toordinal())

    def timestamp(self):
        ordinal_date = self.toordinal()
        timestamp = ordinal_date - POSIX_EPOCH
        timestamp *= 24 * 60 * 60
        return timestamp

    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, ordinal_date):
        try:
            ordinal_date = SezimalInteger(ordinal_date)
        except:
            ordinal_date = SezimalInteger(Decimal(ordinal_date))

        y, m, d, diy, wiy = _ordinal_to_year_month_day(ordinal_date)
        return cls(y, m, d)

    @classmethod
    def fromisoformat(cls, date_string):
        return cls.fromordinal(_datetime.date.fromisoformat(date_string).toordinal())

    @classmethod
    def fromisocalendar(cls, year, week, day):
        return cls.fromordinal(_datetime.date.fromisocalendar(year, week, day).toordinal())

    def __repr__(self):
        return f'{self.__class__.__qualname__}({self.year.formatted_number}, {self.month}, {self.day})'

    @property
    def gregorian_date(self):
        return self._gregorian_date

    def ctime(self):
        return self.gregorian_date.ctime()

    def _strftime_locale(self, format='%a'):
        if format == '%a' or format == '%A':
            weekday_names = {
                SezimalInteger('0'): (locale.ABDAY_2, locale.DAY_2),
                SezimalInteger('1'): (locale.ABDAY_3, locale.DAY_3),
                SezimalInteger('2'): (locale.ABDAY_4, locale.DAY_4),
                SezimalInteger('3'): (locale.ABDAY_5, locale.DAY_5),
                SezimalInteger('4'): (locale.ABDAY_6, locale.DAY_6),
                SezimalInteger('5'): (locale.ABDAY_7, locale.DAY_7),
                SezimalInteger('10'): (locale.ABDAY_1, locale.DAY_1),
            }

            if format == '%a':
                return locale.nl_langinfo(weekday_names[self.weekday()][0])
            else:
                return locale.nl_langinfo(weekday_names[self.weekday()][1])

        elif format == '%b' or format == '%B':
            month_names = {
                SezimalInteger('1'): (locale.ABMON_1, locale.MON_1),
                SezimalInteger('2'): (locale.ABMON_2, locale.MON_2),
                SezimalInteger('3'): (locale.ABMON_3, locale.MON_3),
                SezimalInteger('4'): (locale.ABMON_4, locale.MON_4),
                SezimalInteger('5'): (locale.ABMON_5, locale.MON_5),
                SezimalInteger('10'): (locale.ABMON_6, locale.MON_6),
                SezimalInteger('11'): (locale.ABMON_7, locale.MON_7),
                SezimalInteger('12'): (locale.ABMON_8, locale.MON_8),
                SezimalInteger('13'): (locale.ABMON_9, locale.MON_9),
                SezimalInteger('14'): (locale.ABMON_10, locale.MON_10),
                SezimalInteger('15'): (locale.ABMON_11, locale.MON_11),
                SezimalInteger('20'): (locale.ABMON_12, locale.MON_12),
            }

            if format == '%b':
                return locale.nl_langinfo(month_names[self._month][0])
            else:
                return locale.nl_langinfo(month_names[self._month][1])

        elif format == '%E' or format == '%EC':
            used_locale = locale.getlocale()[0]

            if 'pt_' in used_locale:
                if self.year >= 0:
                    return 'EHS'
                else:
                    return 'aEHS'

            if self.year >= 0:
                return 'SHE'
            else:
                return 'BSHE'

    def _strftime_day_in_year(self):
        y, m, d, diy, wiy = _ordinal_to_year_month_day(self.toordinal())
        return str(diy)

    def _strftime_week_in_year(self):
        y, m, d, diy, wiy = _ordinal_to_year_month_day(self.toordinal())
        return str(wiy)

    def _strftime_weekday_number(self):
        return str(self.weekday() + 1)

    def _strftime_ordinal_suffix(self):
        used_locale = locale.getlocale()[0]

        if 'pt_' in used_locale:
            if self.day != 1:
                return ''

            if used_locale == 'pt_BR':
                return 'º'
            else:
                return '.º'

        if str(self.day)[-1] == '1':
            return 'st'
        elif str(self.day)[-1] == '2':
            return 'nd'
        elif str(self.day)[-1] == '3':
            return 'rd'
        else:
            return 'th'

    def strftime(self, fmt):
        #
        # Deals with what is or may be different from the Gregorian Calendar
        #
        fmt = fmt.replace('%%', '__PERCENT__')

        if '%a' in fmt:
            fmt = fmt.replace('%a', self._strftime_locale('%a'))

        if '%A' in fmt:
            fmt = fmt.replace('%A', self._strftime_locale('%A'))

        if '%d' in fmt:
            fmt = fmt.replace('%d', str(self.day).zfill(2))

        if '%-d' in fmt:
            fmt = fmt.replace('%-d', str(self.day))

        if '%e' in fmt:
            fmt = fmt.replace('%e', str(self.day).rjust(2))

        if '%-e' in fmt:
            fmt = fmt.replace('%-e', str(self.day))

        if '%o' in fmt:
            fmt = fmt.replace('%o', self._strftime_ordinal_suffix())

        if '%m' in fmt:
            fmt = fmt.replace('%m', str(self.month).zfill(2))

        if '%-m' in fmt:
            fmt = fmt.replace('%-m', str(self.month))

        if '%b' in fmt:
            fmt = fmt.replace('%b', self._strftime_locale('%b'))

        if '%h' in fmt:
            fmt = fmt.replace('%h', self._strftime_locale('%b'))

        if '%B' in fmt:
            fmt = fmt.replace('%B', self._strftime_locale('%B'))

        if '%y' in fmt:
            fmt = fmt.replace('%y', str(self.year)[-2:])

        if '%Y' in fmt:
            fmt = fmt.replace('%Y', str(self.year))

        if '%_Y' in fmt:
            fmt = fmt.replace('%_Y', self.year.formatted_number)

        if '%EC' in fmt:
            fmt = fmt.replace('%EC', self._strftime_locale('%EC'))

        if '%E' in fmt:
            fmt = fmt.replace('%E', self._strftime_locale('%E'))

        if '%j' in fmt:
            fmt = fmt.replace('%j', self._strftime_day_in_year().zfill(4))

        if '%-j' in fmt:
            fmt = fmt.replace('%j', self._strftime_day_in_year())

        if '%w' in fmt:
            fmt = fmt.replace('%w', self._strftime_weekday_number())

        if '%U' in fmt:
            fmt = fmt.replace('%U', self._strftime_week_in_year().zfill(3))

        if '%-U' in fmt:
            fmt = fmt.replace('%U', self._strftime_week_in_year())

        if '%W' in fmt:
            fmt = fmt.replace('%W', self._strftime_week_in_year().zfill(3))

        if '%-W' in fmt:
            fmt = fmt.replace('%W', self._strftime_week_in_year())

        if '%c' in fmt:
            fmt = fmt.replace('%c', self.strftime(locale.nl_langinfo(locale.D_T_FMT)))
            fmt = self.strftime(fmt)

        if '%x' in fmt:
            fmt = fmt.replace('%x', self.strftime(locale.nl_langinfo(locale.D_FMT)))
            fmt = self.strftime(fmt)

        if '%X' in fmt:
            fmt = fmt.replace('%X', self.strftime(locale.nl_langinfo(locale.T_FMT)))
            fmt = self.strftime(fmt)

        if '%D' in fmt:
            fmt = fmt.replace('%D', '%Y-%m-%d')
            fmt = self.strftime(fmt)

        if '%F' in fmt:
            fmt = fmt.replace('%F', '%Y-%m-%d')
            fmt = self.strftime(fmt)

        if '%n' in fmt:
            fmt = fmt.replace('%n', '\n')

        if '%t' in fmt:
            fmt = fmt.replace('%t', '\n')

        fmt = fmt.replace('__PERCENT__', '%%')

        if '%' not in fmt:
            return fmt

        return self.gregorian_date.strftime(fmt)

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.strftime(fmt)
        return str(self)

    def isoformat(self):
        return f'{str(self.year).zfill(6)}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}'

    def isoformat_decimal(self):
        return f'{str(self.year.decimal).zfill(5)}-{str(self.month.decimal).zfill(2)}-{str(self.day.decimal).zfill(2)}'

    __str__ = isoformat

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def is_leap(self):
        return bool(self._is_leap)

    @property
    def gregorian_year(self):
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[0]

        return self.gregorian_date.year

    @property
    def gregorian_month(self):
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[1]

        return self.gregorian_date.month

    @property
    def gregorian_day(self):
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[2]

        return self.gregorian_date.day

    def gregorian_isoformat(self):
        if self.gregorian_year > 9_999:
            return f'+{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'
        else:
            return f'{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'

    def gregorian_holocene_date(self):
        return (self.gregorian_holocene_year, self.gregorian_holocene_month, self.gregorian_holocene_day)

    @property
    def gregorian_holocene_year(self):
        return self.gregorian_year + int(ISO_HOLOCENE_YEAR_DIFF)

    @property
    def gregorian_holocene_month(self):
        return self.gregorian_month

    @property
    def gregorian_holocene_day(self):
        return self.gregorian_day

    def gregorian_holocene_isoformat(self):
        return f'{str(self.gregorian_holocene_year).zfill(5)}-{str(self.gregorian_holocene_month).zfill(2)}-{str(self.gregorian_holocene_day).zfill(2)}'

    def symmetric_date(self):
        return (self.symmetric_year, self.symmetric_month, self.symmetric_day)

    @property
    def symmetric_year(self):
        return int(self.year) - int(ISO_YEAR_DIFF)

    @property
    def symmetric_month(self):
        return int(self.month)

    @property
    def symmetric_day(self):
        return int(self.day)

    def symmetric_isoformat(self):
        return f'{str(self.symmetric_year).zfill(4)}-{str(self.symmetric_month).zfill(2)}-{str(self.symmetric_day).zfill(2)}'

    def symmetric_holocene_date(self):
        return (self.symmetric_holocene_year, self.symmetric_holocene_month, self.symmetric_holocene_day)

    @property
    def symmetric_holocene_year(self):
        return self.symmetric_year + int(ISO_HOLOCENE_YEAR_DIFF)

    @property
    def symmetric_holocene_month(self):
        return int(self.month)

    @property
    def symmetric_holocene_day(self):
        return int(self.day)

    def symmetric_holocene_isoformat(self):
        return f'{str(self.symmetric_holocene_year).zfill(5)}-{str(self.symmetric_holocene_month).zfill(2)}-{str(self.symmetric_holocene_day).zfill(2)}'

    def timetuple(self):
        return self.gregorian_date.timetuple()

    def toordinal(self):
        return self._ordinal_date

    @property
    def ordinal_date(self):
        return self._ordinal_date

    def replace(self, year=None, month=None, day=None):
        """Return a new date with new values for the specified fields."""
        if year is None:
            year = self._year
        if month is None:
            month = self._month
        if day is None:
            day = self._day
        return type(self)(year, month, day)

    # Comparisons of date objects with other.

    def __eq__(self, other):
        if type(other) in (_datetime.date, SezimalDate):
            return self._cmp(other) == 0
        return NotImplemented

    def __le__(self, other):
        if type(other) in (_datetime.date, SezimalDate):
            return self._cmp(other) <= 0
        return NotImplemented

    def __lt__(self, other):
        if type(other) in (_datetime.date, SezimalDate):
            return self._cmp(other) < 0
        return NotImplemented

    def __ge__(self, other):
        if type(other) in (_datetime.date, SezimalDate):
            return self._cmp(other) >= 0
        return NotImplemented

    def __gt__(self, other):
        if type(other) in (_datetime.date, SezimalDate):
            return self._cmp(other) > 0
        return NotImplemented

    def _cmp(self, other):
        assert type(other) in (_datetime.date, SezimalDate)

        this_ordinal = self.toordinal()
        other_ordinal = other.toordinal()

        if this_ordinal == other_ordinal:
            return 0
        elif this_ordinal > other_ordinal:
            return 1
        else:
            return -1

    def __hash__(self):
        if self._hashcode == -1:
            self._hashcode = hash(self._getstate())

        return self._hashcode

    def __add__(self, other):
        if isinstance(other, timedelta):
            o = self.toordinal() + other.days
            if 0 < o <= MAXORDINAL:
                return type(self).fromordinal(o)
            raise OverflowError("result out of range")
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract two dates, or a date and a timedelta."""
        if isinstance(other, timedelta):
            return self + timedelta(-other.days)
        if isinstance(other, _datetime.date) or isinstance(other, SezimalDate):
            days1 = self.toordinal()
            days2 = other.toordinal()
            return timedelta(days1 - days2)
        return NotImplemented

    def weekday(self):
        return self._weekday

    def isoweekday(self):
        return self._weekday + 1

    def isocalendar(self):
        return self.gregorian_date.isocalendar()

    # Pickle support.

    def _getstate(self):
        return self.gregorian_date._getstate()

    def __setstate(self, string):
        yhi, ylo, self._month, self._day = string
        self._year = yhi * SezimalInteger('1104') + ylo

    def __reduce__(self):
        return (self.__class__, self._getstate())

    def to_julian_date(self):
        return self.ordinal_date + ISO_EPOCH_JULIAN_DATE


SezimalDate.min = SezimalDate(1, 1, 1)
SezimalDate.max = SezimalDate(MAXYEAR, 20, 44)
SezimalDate.resolution = _datetime.timedelta(days=1)


if __name__ == '__main__':
    try:
        1/0
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
        documentation_title = '     Datas da Documentação do Calendário'
        holidays_title = '   Feriados e Eventos Históricos do Brasil'
        size = 16
        date_format = '%a. %d-%b-%_Y'

    except:
        documentation_title = '  Dates from the Symmetry454 Documentation'
        holidays_title = '   Brazilian Holidays and Historical Events'
        size = 16
        date_format = '%_Y-%m-%d %a.'

    print(documentation_title)
    print(holidays_title)
    print(' ===========================================')

    dates = [
        # (( -753,  1,  1), 'Kalendae Ianuarius I AUC => -0753-12-23 CE, -0753-12-24 Gregorian/ISO (no year zero)'),
        # (( -121,  4, 27), '=> -0121-04-27 CE, -0121-04-26 Gregorian/ISO (no year zero)'),
        # ((  -91,  9, 22), '=> -0091-09-22 CE, -0091-09-27 Gregorian/ISO (no year zero)'),
        ((    1,  1,  1), 'First date possible, Python’s date doesn’t deal with years before 1'),
        ((  122,  9,  7), 'Building of Hadrian’s Wall (circa)'),
        ((1_776,  7,  4), 'Independence Day - USA'),
        ((1_867,  7,  1), 'Canadian Confederence - Canada'),
        ((1_947, 10, 24), ''),
        ((1_970,  1,  1), 'POSIX epoch'),
        ((1_995,  8, 10), ''),
        ((2_000,  2, 29), ''),
        ((2_004,  5,  2), ''),
        ((2_004, 12, 31), 'Dr. Irv Bromberg proposed switching calendars on 2005-01-01'),
        ((2_020,  2, 20), ''),
        ((2_023,  1, 16), 'Day I commited this code to GitHub'),
        ((2_222,  2,  6), ''),
        ((3_333,  3,  1), ''),
        ((9_998, 12, 27), 'Last date compatible with Python’s date, see code'),

        ((1500,  5,  2), 'Descobrimento do Brasil (22-abr-1500 cal. juliano)'),
        ((1532,  2,  1), 'Fundação de São Vicente (22-jan-1532 cal. juliano)'),
        ((1554,  2,  4), 'Fundação de São Paulo (25-jan-1554 cal. juliano)'),
        ((1792,  4, 21), 'Tiradentes'),
        ((1822,  9,  7), 'Independência'),
        ((1857,  5,  8), 'Dia da Mulher'),
        ((1886,  5,  1), 'Dia do Trabalhador'),
        ((1888,  5, 13), 'Libertação da Escravatura'),
        ((1889, 11, 15), 'Proclamação da República'),
        ((1932,  7,  9), 'Revolução Constitucionalista'),
        ((1968,  1,  1), 'Fraternidade Universal'),
        ((1980, 10, 12), 'Nossa Senhora Aparecida'),
    ]

    for ymd, name in dates:
        dt = _datetime.date(*ymd)
        sd = SezimalDate(dt)
        # print(dt, dt.toordinal(), sd, sd.isoformat_decimal(), sd.toordinal().decimal, Decimal(dt.toordinal()) == sd.toordinal().decimal)
        print(sd.isoformat_decimal(), decimal_format(sd.toordinal().decimal, decimal_places=0), decimal_format(sd.to_julian_date().decimal))
        # print(' ', sd.gregorian_date.strftime(date_format).rjust(size), f'Greg. =', sd.strftime(date_format + ' %E').rjust(size), f'({sd.isoformat_decimal()})', name)

    # sd = SezimalDate.today()
    # dt = sd.gregorian_date
    # print()
    # print(' ', sd.gregorian_date.strftime(date_format).rjust(size), f'Greg. =', sd.strftime(date_format + ' %E').rjust(size), f'({sd.isoformat_decimal()})', 'Today')
