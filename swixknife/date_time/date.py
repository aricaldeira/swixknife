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

from decimal import Decimal
from zoneinfo import ZoneInfo

from ..sezimal import Sezimal, SezimalInteger
from ..base import decimal_format, sezimal_format, \
    sezimal_to_niftimal, default_to_dedicated_digits, \
    default_niftimal_to_dedicated_digits, default_niftimal_to_regularized_digits, \
    default_niftimal_to_regularized_dedicated_digits
from .gregorian_functions import ordinal_date_to_gregorian_year_month_day
from ..units.conversions import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA
from .date_time_delta import SezimalDateTimeDelta
from ..text import sezimal_spellout
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from .sezimal_functions import *


class SezimalDate:
    __slots__ = '_year', '_month', '_day', '_hashcode', '_gregorian_date', '_is_leap', '_ordinal_date', '_weekday', \
        '_day_in_year', '_day_in_week', '_week_in_year', \
        '_quarter', '_day_in_quarter', '_week_in_quarter', '_month_in_quarter'

    def __new__(
        cls,
        year: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self,
        month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None
        ) -> Self:
        if month is None:
            if type(year) in (_datetime.date, _datetime.datetime):
                return cls.from_ordinal_date(Decimal(year.toordinal()))

            elif type(year).__name__ in ('SezimalDate', 'SezimalDateTime', 'SezimalTime'):
                return cls.from_ordinal_date(year.ordinal_date)

            elif type(year) == str:
                if VALID_DATE_STRING.match(year):
                    year, month, day = year.split('-')

        year = SezimalInteger(year)
        month = SezimalInteger(month)
        day = SezimalInteger(day)

        check_date_fields(year, month, day)

        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        self._ordinal_date = year_month_day_to_ordinal(year, month, day)

        y, m, d, diy, wiy, q, diq, wiq, miq = ordinal_to_year_month_day(self._ordinal_date)

        self._day_in_year = diy
        self._week_in_year = wiy
        self._quarter = q
        self._day_in_quarter = diq
        self._week_in_quarter = wiq
        self._month_in_quarter = miq

        self._weekday = day % SezimalInteger(11)

        if self._weekday == 0:
            self._weekday = SezimalInteger(11)

        self._hashcode = -1
        self._is_leap = is_leap(year - ISO_YEAR_DIFF)

        gregorian_date = ordinal_date_to_gregorian_year_month_day(int(self._ordinal_date.decimal))

        if gregorian_date[0] >= 1 and gregorian_date[0] <= 9_999:
            self._gregorian_date = _datetime.date(*gregorian_date)
        else:
            self._gregorian_date = gregorian_date

        return self

    # Additional constructors

    @classmethod
    def from_timestamp(cls, timestamp) -> Self:
        "Construct a date from a POSIX timestamp (like time.time())."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(timestamp)
        x = _datetime.date(y, m, d)
        return cls.from_ordinal_date(Decimal(x.toordinal()))

    @property
    def timestamp(self) -> float:
        timestamp = self.ordinal_date.decimal - POSIX_EPOCH.decimal
        timestamp *= 24 * 60 * 60
        return float(timestamp)

    @classmethod
    def today(cls) -> Self:
        "Construct a date from time.time()."
        t = _time.time()
        return cls.from_timestamp(t)

    @classmethod
    def from_ordinal_date(cls, ordinal_date) -> Self:
        ordinal_date = SezimalInteger(ordinal_date)
        y, m, d, *x = ordinal_to_year_month_day(ordinal_date)
        return cls(y, m, d)

    @classmethod
    def from_iso_format(cls, date_string) -> Self:
        return cls.fromordinal(_datetime.date.fromisoformat(date_string).toordinal())

    @classmethod
    def from_iso_calendar(cls, year, week, day) -> Self:
        return cls.fromordinal(_datetime.date.fromisocalendar(year, week, day).toordinal())

    def __repr__(self) -> str:
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

    def isoformat(self) -> str:
        return f'{str(self.year).zfill(6)}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}'

    def isoformat_decimal(self) -> str:
        return f'{str(self.year.decimal).zfill(5)}-{str(self.month.decimal).zfill(2)}-{str(self.day.decimal).zfill(2)}'

    __str__ = isoformat

    @property
    def year(self) -> SezimalInteger:
        return self._year

    @property
    def month(self) -> SezimalInteger:
        return self._month

    @property
    def day(self) -> SezimalInteger:
        return self._day

    @property
    def is_leap(self) -> bool:
        return bool(self._is_leap)

    @property
    def is_long_month(self) -> bool:
        return self.month in (2, 5, 12, 15) or (self.is_leap and self.month == 20)

    @property
    def weekday(self) -> SezimalInteger:
        return self._weekday

    @property
    def week_in_month(self) -> SezimalInteger:
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
    def day_in_year(self) -> SezimalInteger:
        return self._day_in_year

    @property
    def week_in_year(self) -> SezimalInteger:
        return self._week_in_year

    @property
    def quarter(self) -> SezimalInteger:
        return self._quarter

    @property
    def day_in_quarter(self) -> SezimalInteger:
        return self._day_in_quarter

    @property
    def week_in_quarter(self) -> SezimalInteger:
        return self._week_in_quarter

    @property
    def month_in_quarter(self) -> SezimalInteger:
        return self._month_in_quarter

    @property
    def weekday_name(self) -> str:
        return DEFAULT_LOCALE.weekday_name(self.weekday)

    @property
    def weekday_abbreviated_name(self) -> str:
        return DEFAULT_LOCALE.weekday_abbreviated_name(self.weekday)

    @property
    def month_name(self) -> str:
        return DEFAULT_LOCALE.month_name(self.month)

    @property
    def month_abbreviated_name(self) -> str:
        return DEFAULT_LOCALE.month_abbreviated_name(self.month)

    @property
    def era_name(self) -> str:
        return DEFAULT_LOCALE.era_name(self.year)

    @property
    def day_ordinal_suffix(self) -> str:
        return DEFAULT_LOCALE.day_ordinal_suffix(self.day)

    def _apply_format(self, fmt: str, token: str, value_name: str, size: int | SezimalInteger = None) -> str:
        if token not in fmt:
            return fmt

        value = getattr(self, value_name, 0)

        if '*' in token and (not value):
            fmt = fmt.replace(token, '')
        else:
            if '@' in token:
                value = str(value)

                if size:
                    value = value.zfill(int(SezimalInteger(size)))

                value = sezimal_to_niftimal(value)

                if size:
                    value = value.zfill(int(SezimalInteger(size)))

                if '!' in token:
                    value = default_niftimal_to_regularized_dedicated_digits(value)
                else:
                    value = default_niftimal_to_regularized_digits(value)

            else:
                if '9' in token:
                    value = str(int(value.decimal))
                elif '↋' in token:
                    value = value.dozenal
                else:
                    value = str(value)

                if size:
                    value = value.zfill(int(SezimalInteger(size)))

                if '!' in token:
                    value = default_to_dedicated_digits(value)

            fmt = fmt.replace(token, value)

        return fmt

    def format(self, fmt: str = None, locale: str | SezimalLocale = None, skip_strftime: bool = False, time_zone: str | ZoneInfo = None) -> str:
        if locale:
            if isinstance(locale, SezimalLocale):
                lang = locale.LANG
            else:
                lang = locale
                locale = sezimal_locale(lang)

        else:
            locale = DEFAULT_LOCALE
            lang = locale.LANG

        if not fmt:
            fmt = locale.DATE_FORMAT

        fmt = fmt.replace('##', '__HASHTAG__')

        #
        # Astronomical formats: seasons and moon phases
        #
        fmt = self._apply_season_format(fmt, locale=locale, time_zone=time_zone)

        #
        # Let’s deal first with the numeric formats
        #
        for character, value, size, size_niftimal, size_decimal in [
            ['d', 'day', 2, 1, 2],                # 01 – 44/55 (01_dec – 28_dec/35_dec)
            ['w', 'weekday', 2, 1, 1],            # 01 - 11 (01_dec – 7_dec)
            ['m', 'month', 2, 1, 2],              # 01 – 20 (01_dec – 12_dec)
            ['q', 'quarter', 1, 1, 1],            # 1 – 4
            ['y', 'year', 10, 3, 5],              # 00_0000 – 55_5555 (−10_000_dec – 36_655_dec)

            ['dQ', 'day_in_quarter', 3, 2, 2],    # 001 – 231/242 (01_dec – 91_dec/98_dec)
            ['dY', 'day_in_year', 4, 2, 3],       # 0001 – 1404/1415 (001_dec – 364_dec/371_dec)

            ['wM', 'week_in_month', 1, 1, 1],     # 1 – 4/5
            ['wQ', 'week_in_quarter', 2, 1, 2],   # 01 – 21/22 (01_dec – 13_dec/14_dec)
            ['wY', 'week_in_year', 3, 2, 2],      # 001 – 124/125 (01_dec – 52_dec/53_dec)

            ['mQ', 'month_in_quarter', 1, 1, 1],  # 1 – 3
        ]:
            fmt = self._apply_format(fmt, f'#*-{character}', value)
            fmt = self._apply_format(fmt, f'#*{character}', value, size)
            fmt = self._apply_format(fmt, f'#-{character}', value)
            fmt = self._apply_format(fmt, f'#{character}', value, size)
            fmt = self._apply_format(fmt, f'#9{character}', value, size_decimal)
            fmt = self._apply_format(fmt, f'#↋{character}', value, size_decimal)

            fmt = self._apply_format(fmt, f'#!*-{character}', value)
            fmt = self._apply_format(fmt, f'#!*{character}', value, size)
            fmt = self._apply_format(fmt, f'#!-{character}', value)
            fmt = self._apply_format(fmt, f'#!{character}', value, size)

            fmt = self._apply_format(fmt, f'#@*-{character}', value)
            fmt = self._apply_format(fmt, f'#@*{character}', value, size_niftimal)
            fmt = self._apply_format(fmt, f'#@-{character}', value)
            fmt = self._apply_format(fmt, f'#@{character}', value, size_niftimal)

            fmt = self._apply_format(fmt, f'#@!*-{character}', value)
            fmt = self._apply_format(fmt, f'#@!*{character}', value, size_niftimal)
            fmt = self._apply_format(fmt, f'#@!-{character}', value)
            fmt = self._apply_format(fmt, f'#@!{character}', value, size_niftimal)

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
            suffix = locale.day_ordinal_suffix(self.day)

            if suffix:
                fmt = fmt.replace('#O&d', sezimal_spellout('ordinal ' + str(self.day), lang or 'en'))
            else:
                fmt = fmt.replace('#O&d', sezimal_spellout(str(self.day), lang or 'en'))

        #
        # Formatted year number
        #
        if f'#Y' in fmt:
            fmt = fmt.replace(f'#Y', self.year.formatted_number.replace('_', locale.GROUP_SEPARATOR))

        if f'#9Y' in fmt:
            fmt = fmt.replace(f'#9Y', self.year.decimal_formatted_number.replace('_', locale.GROUP_SEPARATOR))

        if f'#↋Y' in fmt:
            fmt = fmt.replace(f'#↋Y', self.year.dozenal_formatted_number.replace('_', locale.GROUP_SEPARATOR))

        if f'#!Y' in fmt:
            fmt = fmt.replace(f'#!Y', default_to_dedicated_digits(self.year.formatted_number.replace('_', locale.GROUP_SEPARATOR)))

        for separator in '''_.,˙ʼ’'•◦\u0020\u00a0\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f''':
            if f'#{separator}Y' in fmt:
                fmt = fmt.replace(f'#{separator}Y', self.year.formatted_number.replace('_', separator))

            if f'#9{separator}Y' in fmt:
                fmt = fmt.replace(f'#9{separator}Y', self.year.decimal_formatted_number.replace('_', separator))

            if f'#↋{separator}Y' in fmt:
                fmt = fmt.replace(f'#↋{separator}Y', self.year.dozenal_formatted_number.replace('_', separator))

            if f'#!{separator}Y' in fmt:
                fmt = fmt.replace(f'#!{separator}Y', default_to_dedicated_digits( self.year.formatted_number.replace('_', separator)))

        #
        # And now, the text formats
        #
        if '#M' in fmt:
            fmt = fmt.replace('#M', locale.month_name(self.month))

        if '#@M' in fmt:
            fmt = fmt.replace('#@M', locale.month_abbreviated_name(self.month))

        if '#1M' in fmt:
            fmt = fmt.replace('#1M', locale.month_name(self.month)[0])

        if '#W' in fmt:
            fmt = fmt.replace('#W', locale.weekday_name(self.weekday))

        if '#@W' in fmt:
            fmt = fmt.replace('#@W', locale.weekday_abbreviated_name(self.weekday))

        if '#1W' in fmt:
            fmt = fmt.replace('#1W', locale.weekday_name(self.weekday)[0])

        if '#O' in fmt:
            fmt = fmt.replace('#O', locale.day_ordinal_suffix(self.day))

        if '#E' in fmt:
            fmt = fmt.replace('#E', locale.era_name(self.year))

        fmt = locale.apply_date_format(self, fmt)

        fmt = fmt.replace('__HASHTAG__', '#')

        #
        # Some very basic formatting for Gregorian years below
        # Python’s minimum year number
        #
        if '%' in fmt:
            fmt = fmt.replace('%%', '__PERCENT__')

            if '%A' in fmt:
                fmt = fmt.replace('%A', locale.weekday_name(self.weekday))

            if '%a' in fmt:
                fmt = fmt.replace('%a', locale.weekday_abbreviated_name(self.weekday))

            if '%d' in fmt:
                fmt = fmt.replace('%d', str(self.gregorian_day).zfill(2))

            if '%-d' in fmt:
                fmt = fmt.replace('%-d', str(self.gregorian_day))

            if '%e' in fmt:
                fmt = fmt.replace('%e', str(self.gregorian_day).rjust(2))

            if '%-e' in fmt:
                fmt = fmt.replace('%-e', str(self.gregorian_day))

            if '%o' in fmt:
                fmt = fmt.replace('%o', locale.day_ordinal_suffix(Decimal(self.gregorian_day)))

            if '%m' in fmt:
                fmt = fmt.replace('%m', str(self.gregorian_month).zfill(2))

            if '%-m' in fmt:
                fmt = fmt.replace('%-m', str(self.gregorian_month))

            if '%B' in fmt:
                fmt = fmt.replace('%B', locale.month_name(Decimal(self.gregorian_month)))

            if '%b' in fmt:
                fmt = fmt.replace('%b', locale.month_abbreviated_name(Decimal(self.gregorian_month)))

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
    def gregorian_year(self) -> int:
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[0]

        return self.gregorian_date.year

    @property
    def gregorian_month(self) -> int:
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[1]

        return self.gregorian_date.month

    @property
    def gregorian_day(self) -> int:
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[2]

        return self.gregorian_date.day

    @property
    def gregorian_isoformat(self) -> str:
        if self.gregorian_year > 9_999:
            return f'+{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'
        else:
            return f'{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'

    @property
    def gregorian_holocene_date(self):
        return (self.gregorian_holocene_year, self.gregorian_holocene_month, self.gregorian_holocene_day)

    @property
    def gregorian_holocene_year(self) -> int:
        return self.gregorian_year + int(ISO_HOLOCENE_YEAR_DIFF)

    @property
    def gregorian_holocene_month(self) -> int:
        return self.gregorian_month

    @property
    def gregorian_holocene_day(self) -> int:
        return self.gregorian_day

    @property
    def gregorian_holocene_isoformat(self) -> str:
        return f'{str(self.gregorian_holocene_year).zfill(5)}-{str(self.gregorian_holocene_month).zfill(2)}-{str(self.gregorian_holocene_day).zfill(2)}'

    @property
    def symmetric_date(self):
        return (self.symmetric_year, self.symmetric_month, self.symmetric_day)

    @property
    def symmetric_year(self) -> int:
        return int(self.year) - int(ISO_YEAR_DIFF)

    @property
    def symmetric_month(self) -> int:
        return int(self.month)

    @property
    def symmetric_day(self) -> int:
        return int(self.day)

    @property
    def symmetric_isoformat(self) -> str:
        return f'{str(self.symmetric_year).zfill(4)}-{str(self.symmetric_month).zfill(2)}-{str(self.symmetric_day).zfill(2)}'

    @property
    def symmetric_holocene_date(self):
        return (self.symmetric_holocene_year, self.symmetric_holocene_month, self.symmetric_holocene_day)

    @property
    def symmetric_holocene_year(self) -> int:
        return self.symmetric_year + int(ISO_HOLOCENE_YEAR_DIFF)

    @property
    def symmetric_holocene_month(self) -> int:
        return int(self.month)

    @property
    def symmetric_holocene_day(self) -> int:
        return int(self.day)

    @property
    def symmetric_holocene_isoformat(self) -> str:
        return f'{str(self.symmetric_holocene_year).zfill(5)}-{str(self.symmetric_holocene_month).zfill(2)}-{str(self.symmetric_holocene_day).zfill(2)}'

    def timetuple(self):
        return self.gregorian_date.timetuple()

    def toordinal(self) -> SezimalInteger:
        return self._ordinal_date

    @property
    def ordinal_date(self) -> SezimalInteger:
        return self._ordinal_date

    @property
    def isocalendar(self):
        return self.gregorian_date.isocalendar()

    @property
    def julian_date(self) -> SezimalInteger:
        return self.ordinal_date + ISO_EPOCH_JULIAN_DATE

    def replace(self, year=None, month=None, day=None) -> Self:
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
    def as_agrimas(self) -> SezimalInteger:
        return self.ordinal_date * 100_0000

    @property
    def as_seconds(self) -> Decimal:
        seconds = self.as_agrimas * AGRIMA_TO_SECOND
        return seconds.decimal

    @property
    def as_days(self) -> SezimalInteger:
        return self.ordinal_date

    @classmethod
    def from_days(cls, days: SezimalInteger) -> Self:
        return cls.from_ordinal_date(SezimalInteger(days))

    def _moon_phase_name_simplified(self) -> str:
        #
        # Mean moon month = days ÷ years
        # According to Wikipedia, this gives a mean lunar month
        # 1 day behind the actual moon phase
        #
        MOON_MONTH = Sezimal('31_2113') / Sezimal('3534')

        #
        # Date and time at the end of the day
        # minus 1 day, compensating the moon cycle
        #
        moon_phase = self.ordinal_date - 1
        moon_phase += Sezimal('0.555555')

        #
        # Specific point in time where the moon was knowingly
        # on the new phase:
        #
        # Ordinal date 2301_4020.04
        # Sezimal date 13_1111-01-25 04:00
        # Gregorian date 1923-01-17 02:40
        #
        # It was first new moon of the first lunation (lunar month),
        # according to this site: https://www.timeanddate.com/moon/phases/?year=1923
        #
        moon_phase -= Sezimal('2301_4020.04')

        day_in_cycle = moon_phase.decimal % MOON_MONTH.decimal

        if day_in_cycle < 0:
            day_in_cycle = MOON_MONTH.decimal + day_in_cycle

        persixniff = Sezimal(day_in_cycle / MOON_MONTH.decimal * 216)

        if persixniff > 1000:
            persixniff -= 1000

        if persixniff < 20:
            phase = 'new'

        elif persixniff < 130:
            phase = 'waxing_crescent'

        elif persixniff < 140:
            phase = 'first_quarter'

        elif persixniff < 300:
            phase = 'waxing_gibbous'

        elif persixniff < 320:
            phase = 'full'

        elif persixniff < 430:
            phase = 'waning_gibbous'

        elif persixniff < 440:
            phase = 'third_quarter'

        else:
            phase = 'waning_crescent'

        return phase



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
