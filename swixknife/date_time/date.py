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

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalDate')
SezimalTime = TypeVar('SezimalTime', bound='SezimalTime')
SezimalDateTime = TypeVar('SezimalDateTime', bound='SezimalDateTime')

import time as _time
import datetime as _datetime
import locale

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..functions import floor, ceil
from ..base import decimal_format, sezimal_format, \
    sezimal_compression, default_to_dedicated_digits, \
    default_compressed_to_dedicated_digits, default_compressed_to_regularized_digits, \
    default_compressed_to_regularized_dedicated_digits
from .gregorian_functions import ordinal_date_to_gregorian_year_month_day
from ..units.conversions import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA
from .date_time_delta import SezimalDateTimeDelta
from ..text import sezimal_spellout
from ..localization import sezimal_locale, DEFAULT_LOCALE

#
# Epoch
#
# Julian date -1_0521_5450.3 → -1_930_998.5_dec → -9_999-01-03_dec GREGORIAN
#
EPOCH = SezimalInteger('-2_1014_1212')  # -3_652_424_dec
EPOCH_JULIAN_DATE = Sezimal('-1_0521_5450.3')  # -1_930_998.5_dec

ISO_EPOCH = SezimalInteger('1')
ISO_EPOCH_JULIAN_DATE = Sezimal('1_0052_1320.3')  # 1_721_424.5_dec → 00-12-31_dec GREGORIAN
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

    return year, month, day, day_in_year, week_in_year, quarter, day_in_quarter, week_in_quarter, month_in_quarter


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
    __slots__ = '_year', '_month', '_day', '_hashcode', '_gregorian_date', '_is_leap', '_ordinal_date', '_weekday', \
        '_day_in_year', '_day_in_week', '_week_in_year', \
        '_quarter', '_day_in_quarter', '_week_in_quarter', '_month_in_quarter'

    def __new__(
        cls,
        year: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self,
        month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None
        ):
        if month is None:
            if type(year) in (_datetime.date, _datetime.datetime):
                return cls.fromordinal(Decimal(year.toordinal()))

            elif type(year).__name__ in ('SezimalDate', 'SezimalDateTime', 'SezimalTime'):
                return cls.fromordinal(year.ordinal_date)

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

        y, m, d, diy, wiy, q, diq, wiq, miq = _ordinal_to_year_month_day(self._ordinal_date)

        self._day_in_year = diy
        self._week_in_year = wiy
        self._quarter = q
        self._day_in_quarter = diq
        self._week_in_quarter = wiq
        self._month_in_quarter = miq

        if self._ordinal_date <= 0:
            self._weekday = SezimalInteger(((self._ordinal_date.decimal - EPOCH.decimal) % SezimalInteger('11').decimal) + 1)
        else:
            self._weekday = SezimalInteger(((self._ordinal_date.decimal - 1) % SezimalInteger('11').decimal) + 1)

        self._hashcode = -1
        self._is_leap = _is_leap(year)

        gregorian_date = ordinal_date_to_gregorian_year_month_day(int(self._ordinal_date.decimal))

        if gregorian_date[0] >= 1 and gregorian_date[0] <= 9_999:
            self._gregorian_date = _datetime.date(*gregorian_date)
        else:
            self._gregorian_date = gregorian_date

        return self

    # Additional constructors

    @classmethod
    def from_timestamp(cls, timestamp):
        "Construct a date from a POSIX timestamp (like time.time())."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(timestamp)
        x = _datetime.date(y, m, d)
        return cls.fromordinal(x.toordinal())

    @property
    def timestamp(self):
        ordinal_date = self.toordinal()
        timestamp = ordinal_date.decimal - POSIX_EPOCH.decimal
        timestamp *= 24 * 60 * 60
        return int(timestamp)

    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.from_timestamp(t)

    @classmethod
    def fromordinal(cls, ordinal_date):
        try:
            ordinal_date = SezimalInteger(ordinal_date)
        except:
            ordinal_date = SezimalInteger(Decimal(ordinal_date))

        y, m, d, *x = _ordinal_to_year_month_day(ordinal_date)
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

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.format(fmt)
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
    def weekday(self):
        return self._weekday

    @property
    def week_in_month(self):
        if self.day <= 11:
            return SezimalInteger(1)
        elif self.day <= 22:
            return SezimalInteger(2)
        elif self.day <= 33:
            return SezimalInteger(3)
        elif self.day <= 44:
            return SezimalInteger(4)

        return SezimalInteger(5)

    @property
    def day_in_year(self):
        return self._day_in_year

    @property
    def week_in_year(self):
        return self._week_in_year

    @property
    def quarter(self):
        return self._quarter

    @property
    def day_in_quarter(self):
        return self._day_in_quarter

    @property
    def week_in_quarter(self):
        return self._week_in_quarter

    @property
    def month_in_quarter(self):
        return self._month_in_quarter

    @property
    def weekday_name(self):
        return DEFAULT_LOCALE.weekday_name(self.weekday)

    @property
    def weekday_abbreviated_name(self):
        return DEFAULT_LOCALE.weekday_abbreviated_name(self.weekday)

    @property
    def month_name(self):
        return DEFAULT_LOCALE.month_name(self.month)

    @property
    def month_abbreviated_name(self):
        return DEFAULT_LOCALE.month_abbreviated_name(self.month)

    @property
    def era_name(self):
        return DEFAULT_LOCALE.era_name(self.year)

    @property
    def day_ordinal_suffix(self):
        return DEFAULT_LOCALE.day_ordinal_suffix(self.day)

    def _apply_format(self, fmt, token, value, size=None, compressed=False, dedicated_digits=False):
        if token not in fmt:
            return fmt

        value = getattr(self, value, 0)

        if '*' in token and (not value):
            fmt = fmt.replace(token, '')
        else:
            if compressed:
                value = str(value)

                if size:
                    value = value.zfill(int(SezimalInteger(size)))

                value = sezimal_compression(value)

                if dedicated_digits:
                    value = default_compressed_to_regularized_dedicated_digits(value)
                else:
                    value = default_compressed_to_regularized_digits(value)

            else:
                value = str(value)

                if size:
                    value = value.zfill(int(SezimalInteger(size)))

                if dedicated_digits:
                    value = default_to_dedicated_digits(value)

            fmt = fmt.replace(token, value)

        return fmt

    def format(self, fmt: str = '#y-#m-#d', lang=None, skip_strftime=False):
        fmt = fmt.replace('##', '__HASHTAG__')

        if lang:
            loc = sezimal_locale(lang)
        else:
            loc = DEFAULT_LOCALE
            lang = loc.LANG

        #
        # Let’s deal first with the numeric formats
        #
        for character, value, size in [
            ['d', 'day', 2],                # 01 – 44/55 (01_dec – 28_dec/35_dec)
            ['w', 'weekday', 2],            # 01 - 11 (01_dec – 7_dec)
            ['m', 'month', 2],              # 01 – 20 (01_dec – 12_dec)
            ['q', 'quarter', 1],            # 1 – 4
            ['y', 'year', 10],              # 00_0000 – 55_5555 (−10_000_dec – 36_655_dec)

            ['dQ', 'day_in_quarter', 3],    # 001 – 231/242 (01_dec – 91_dec/98_dec)
            ['dY', 'day_in_year', 4],       # 0001 – 1404/1415 (001_dec – 364_dec/371_dec)

            ['wM', 'week_in_month', 1],     # 1 – 4/5
            ['wQ', 'week_in_quarter', 2],   # 01 – 21/22 (01_dec – 13_dec/14_dec)
            ['wY', 'week_in_year', 3],      # 001 – 124/125 (01_dec – 52_dec/53_dec)

            ['mQ', 'month_in_quarter', 1],  # 1 – 3
        ]:
            fmt = self._apply_format(fmt, f'#*-{character}', value)
            fmt = self._apply_format(fmt, f'#*{character}', value, size)
            fmt = self._apply_format(fmt, f'#-{character}', value)
            fmt = self._apply_format(fmt, f'#{character}', value, size)

            fmt = self._apply_format(fmt, f'#!*-{character}', value, dedicated_digits=True)
            fmt = self._apply_format(fmt, f'#!*{character}', value, size, dedicated_digits=True)
            fmt = self._apply_format(fmt, f'#!-{character}', value, dedicated_digits=True)
            fmt = self._apply_format(fmt, f'#!{character}', value, size, dedicated_digits=True)

            fmt = self._apply_format(fmt, f'#@*-{character}', value, compressed=True)
            fmt = self._apply_format(fmt, f'#@*{character}', value, size, compressed=True)
            fmt = self._apply_format(fmt, f'#@-{character}', value, compressed=True)
            fmt = self._apply_format(fmt, f'#@{character}', value, size, compressed=True)

            fmt = self._apply_format(fmt, f'#@!*-{character}', value, compressed=True, dedicated_digits=True)
            fmt = self._apply_format(fmt, f'#@!*{character}', value, size, compressed=True, dedicated_digits=True)
            fmt = self._apply_format(fmt, f'#@!-{character}', value, compressed=True, dedicated_digits=True)
            fmt = self._apply_format(fmt, f'#@!{character}', value, size, compressed=True, dedicated_digits=True)

        for character, value in [
            ['wM', 'week_in_month'],
            ['dQ', 'day_in_quarter'],
            ['wQ', 'week_in_quarter'],
            ['mQ', 'month_in_quarter'],
            ['dY', 'day_in_year'],
            ['wY', 'week_in_year'],

            ['d', 'day'],
            ['m', 'month'],
            ['y', 'year'],
            ['w', 'weekday'],
            ['q', 'quarter'],
        ]:
            if f'#&{character}' in fmt:
                fmt = fmt.replace(f'#&{character}', sezimal_spellout(str(getattr(self, value, 0)), lang or 'en'))

            elif f'#&o{character}' in fmt:
                fmt = fmt.replace(f'#o&{character}', sezimal_spellout('ordinal ' + str(getattr(self, value, 0)), lang or 'en'))

            elif f'#&a{character}' in fmt:
                fmt = fmt.replace(f'#a&{character}', sezimal_spellout('ordinal-feminine ' + str(getattr(self, value, 0)), lang or 'en'))

        #
        # Some languages have special rules for using ordinal days,
        # so, we only use ordinal if there is a suffix for the ordinal day
        #
        if '#&Od' in fmt:
            suffix = loc.day_ordinal_suffix(self.day)

            if suffix:
                fmt = fmt.replace('#O&d', sezimal_spellout('ordinal ' + str(self.day), lang or 'en'))
            else:
                fmt = fmt.replace('#O&d', sezimal_spellout(str(self.day), lang or 'en'))

        #
        # Formatted year number
        #
        for separator in '''_.,˙ʼ’'•◦\u0020\u00a0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f''':
            if f'#{separator}y' in fmt:
                fmt = fmt.replace(f'#{separator}y', self.year.formatted_number.replace('_', separator))

            if f'#!{separator}y' in fmt:
                fmt = fmt.replace(f'#!{separator}y', default_to_dedicated_digits( self.year.formatted_number.replace('_', separator)))

        #
        # And now, the text formats
        #
        if '#M' in fmt:
            fmt = fmt.replace('#M', loc.month_name(self.month))

        if '#@M' in fmt:
            fmt = fmt.replace('#@M', loc.month_abbreviated_name(self.month))

        if '#W' in fmt:
            fmt = fmt.replace('#W', loc.weekday_name(self.weekday))

        if '#@W' in fmt:
            fmt = fmt.replace('#@W', loc.weekday_abbreviated_name(self.weekday))

        if '#O' in fmt:
            fmt = fmt.replace('#O', loc.day_ordinal_suffix(self.day))

        if '#E' in fmt:
            fmt = fmt.replace('#E', loc.era_name(self.year))

        fmt = loc.apply_date_format(self, fmt)

        fmt = fmt.replace('__HASHTAG__', '#')

        #
        # Some very basic formatting for Gregorian years below
        # Python’s minimum year number
        #
        if '%' in fmt:
            fmt = fmt.replace('%%', '__PERCENT__')

            if '%A' in fmt:
                fmt = fmt.replace('%A', loc.weekday_name(self.weekday))

            if '%a' in fmt:
                fmt = fmt.replace('%A', loc.weekday_abbreviated_name(self.weekday))

            if '%d' in fmt:
                fmt = fmt.replace('%d', str(self.gregorian_day).zfill(2))

            if '%-d' in fmt:
                fmt = fmt.replace('%-d', str(self.gregorian_day))

            if '%e' in fmt:
                fmt = fmt.replace('%e', str(self.gregorian_day).rjust(2))

            if '%-e' in fmt:
                fmt = fmt.replace('%-e', str(self.gregorian_day))

            if '%o' in fmt:
                fmt = fmt.replace('%o', loc.day_ordinal_suffix(Decimal(self.gregorian_day)))

            if '%m' in fmt:
                fmt = fmt.replace('%m', str(self.gregorian_month).zfill(2))

            if '%-m' in fmt:
                fmt = fmt.replace('%-m', str(self.gregorian_month))

            if '%B' in fmt:
                fmt = fmt.replace('%B', loc.month_name(Decimal(self.gregorian_month)))

            if '%b' in fmt:
                fmt = fmt.replace('%B', loc.month_abbreviated_name(Decimal(self.gregorian_month)))

            if '%y' in fmt:
                fmt = fmt.replace('%y', str(self.gregorian_year))

            if '%Y' in fmt:
                fmt = fmt.replace('%Y', str(self.gregorian_year).zfill(4))

            fmt = fmt.replace('__PERCENT__', '%%')

            if not skip_strftime:
                if type(self.gregorian_date) == _datetime.date:
                    return self.gregorian_date.strftime(fmt)
                else:
                    fmt = fmt.replace('__PERCENT__', '%')

        return fmt

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

    @property
    def gregorian_isoformat(self):
        if self.gregorian_year > 9_999:
            return f'+{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'
        else:
            return f'{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'

    @property
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

    @property
    def gregorian_holocene_isoformat(self):
        return f'{str(self.gregorian_holocene_year).zfill(5)}-{str(self.gregorian_holocene_month).zfill(2)}-{str(self.gregorian_holocene_day).zfill(2)}'

    @property
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

    @property
    def symmetric_isoformat(self):
        return f'{str(self.symmetric_year).zfill(4)}-{str(self.symmetric_month).zfill(2)}-{str(self.symmetric_day).zfill(2)}'

    @property
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

    @property
    def symmetric_holocene_isoformat(self):
        return f'{str(self.symmetric_holocene_year).zfill(5)}-{str(self.symmetric_holocene_month).zfill(2)}-{str(self.symmetric_holocene_day).zfill(2)}'

    def timetuple(self):
        return self.gregorian_date.timetuple()

    def toordinal(self):
        return self._ordinal_date

    @property
    def ordinal_date(self):
        return self._ordinal_date

    @property
    def isocalendar(self):
        return self.gregorian_date.isocalendar()

    @property
    def julian_date(self):
        return self.ordinal_date + ISO_EPOCH_JULIAN_DATE

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

    def __eq__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) == 0

    def __le__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) <= 0

    def __lt__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) < 0

    def __ge__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) >= 0

    def __gt__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) > 0

    def _cmp(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        if type(other) != SezimalDate:
            other = SezimalDate(other)

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

    def __add__(self, other: SezimalDateTimeDelta):
        if type(other) != SezimalDateTimeDelta:
            raise ValueError('You can only add a SezimalDate to a SezimalDateTimeDelta')

        return SezimalDate.fromordinal(other._total_days + self.ordinal_date)

    __radd__ = __add__

    def __sub__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self | SezimalDateTimeDelta):
        """Subtract two dates, or a date and a timedelta."""
        if isinstance(other, timedelta):
            return self + timedelta(-other.days)
        if isinstance(other, _datetime.date) or isinstance(other, SezimalDate):
            days1 = self.toordinal()
            days2 = other.toordinal()
            return timedelta(days1 - days2)
        return NotImplemented


    # Pickle support.

    def _getstate(self):
        return self.gregorian_date._getstate()

    def __setstate(self, string):
        yhi, ylo, self._month, self._day = string
        self._year = yhi * SezimalInteger('1104') + ylo

    def __reduce__(self):
        return (self.__class__, self._getstate())

    @property
    def as_agrimas(self):
        return self.ordinal_date * 100_0000

    @property
    def as_seconds(self):
        seconds = self.as_agrimas * AGRIMA_TO_SECOND
        return seconds.decimal


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
