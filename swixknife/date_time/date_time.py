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

__all__ = ('SezimalDateTime')

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalDate')

import datetime as _datetime
import time as _time
from zoneinfo import ZoneInfo

from decimal import Decimal

from .date import SezimalDate
from .time import SezimalTime
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from .sezimal_functions import *


class SezimalDateTime:
    __slots__ = '_date', '_time', '_iso_date_time'

    def __new__(
        cls,
        year: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.date | _datetime.datetime | SezimalDate,
        month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        uta: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalTime = 0,
        posha: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        agrima: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        anuga: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        boda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        shaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        time_zone: str | ZoneInfo = None,
        ) -> Self:
        self = object.__new__(cls)

        if type(year) == SezimalDate:
            self._date = year
        elif type(year) == _datetime.date:
            self._date = SezimalDate(year)
        elif type(year) == _datetime.datetime:
            if year.tzinfo:
                time_zone = str(year.tzinfo)

                #
                # ZoneInfo doesn’t work well
                # with purelly numeric offset time zones:
                # UTC[+-]9999
                # So we try to convert them to Etc/GMT[+-] with a simplified offset
                #
                if 'UTC+' in time_zone:
                    time_zone = time_zone.replace('UTC+', 'Etc/GMT+')[0:10]
                    time_zone = time_zone.replace('+0', '+')

                elif 'UTC-' in time_zone:
                    time_zone = time_zone.replace('UTC-', 'Etc/GMT-')[0:10]
                    time_zone = time_zone.replace('-0', '-')

                return cls.from_timestamp(year.timestamp(), time_zone=time_zone)

            return cls.from_timestamp(year.timestamp(), time_zone)

        elif type(year) == str:
            if VALID_DATE_TIME_STRING.match(year):
                year, uta = year.strip().split(' ')
                date = SezimalDate(year)
                time = SezimalTime(uta)
                return cls.combine(date, time, time_zone)

            elif VALID_DATE_PARTIAL_TIME_STRING.match(year):
                year, uta = year.strip().split(' ')
                date = SezimalDate(year)
                time = SezimalTime(uta)
                return cls.combine(date, time, time_zone)

            elif VALID_DATE_STRING.match(year):
                self._date = SezimalDate(year)

            else:
                self._date = SezimalDate(year=year, month=month, day=day)

        else:
            self._date = SezimalDate(year=year, month=month, day=day)

        if type(uta) == SezimalTime:
            self._time = uta
            time_zone = self._time.time_zone
        else:
            self._time = SezimalTime(uta=uta, posha=posha, agrima=agrima, anuga=anuga, boda=boda, shaditiboda=shaditiboda, day=0, time_zone=time_zone)

        if type(self._date.gregorian_date) == _datetime.date:
            if time_zone:
                self._iso_date_time = _datetime.datetime.combine(self._date.gregorian_date, self._time.iso_time, ZoneInfo(self.time_zone))
            else:
                self._iso_date_time = _datetime.datetime.combine(self._date.gregorian_date, self._time.iso_time)

        else:
            self._iso_date_time = (
                self._date.gregorian_year,
                self._date.gregorian_month,
                self._date.gregorian_day,
                self._time.iso_hour,
                self._time.iso_minute,
                self._time.iso_second,
                self._time.iso_microsecond,
                self._time._iso_time.tzinfo,
            )

        return self

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}(year={self.year.formatted_number}, month={self.month}, day={self.day}, uta={self.uta}, posha={self.posha}, agrima={self.agrima}, anuga={self.anuga}, boda={self.boda}, shaditiboda={self.shaditiboda}, time_zone={self.time_zone})'

    @property
    def gregorian_date(self):
        return self._date._gregorian_date

    def ctime(self):
        return self._date.ctime()

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.format(fmt)
        return str(self)

    def isoformat(self) -> str:
        return self.format(f'#y-#m-#d #u:#p:#a.#n#b#x #t#-V')

    __str__ = isoformat

    @property
    def year(self) -> SezimalInteger:
        return self._date._year

    @property
    def month(self) -> SezimalInteger:
        return self._date._month

    @property
    def day(self) -> SezimalInteger:
        return self._date._day

    @property
    def is_leap(self) -> bool:
        return self._date.is_leap

    @property
    def is_long_month(self) -> bool:
        return self._date.is_long_month

    @property
    def weekday(self) -> SezimalInteger:
        return self._date._weekday

    @property
    def week_in_month(self) -> SezimalInteger:
        return self._date.week_in_month

    @property
    def day_in_year(self) -> SezimalInteger:
        return self._date._day_in_year

    @property
    def week_in_year(self) -> SezimalInteger:
        return self._date._week_in_year

    @property
    def quarter(self) -> SezimalInteger:
        return self._date._quarter

    @property
    def day_in_quarter(self) -> SezimalInteger:
        return self._date._day_in_quarter

    @property
    def week_in_quarter(self) -> SezimalInteger:
        return self._date._week_in_quarter

    @property
    def month_in_quarter(self) -> SezimalInteger:
        return self._date._month_in_quarter

    @property
    def weekday_name(self) -> str:
        return self._date.weekday_name

    @property
    def weekday_abbreviated_name(self) -> str:
        return self._date.weekday_abbreviated_name

    @property
    def month_name(self) -> str:
        return self._date.month_name

    @property
    def month_abbreviated_name(self) -> str:
        return self._date.month_abbreviated_name

    @property
    def era_name(self) -> str:
        return self._date.era_name

    @property
    def day_ordinal_suffix(self) -> str:
        return self._date.day_ordinal_suffix

    @property
    def gregorian_year(self) -> int:
        return self._date.gregorian_year

    @property
    def gregorian_month(self) -> int:
        return self._date.gregorian_month

    @property
    def gregorian_day(self) -> int:
        return self._date.gregorian_day

    @property
    def gregorian_isoformat(self) -> str:
        return self._date.gregorian_isoformat

    @property
    def gregorian_holocene_date(self):
        return self._date.gregorian_holocene_date

    @property
    def gregorian_holocene_year(self) -> int:
        return self._date.gregorian_holocene_year

    @property
    def gregorian_holocene_month(self) -> int:
        return self._date.gregorian_holocene_month

    @property
    def gregorian_holocene_day(self) -> int:
        return self._date.gregorian_holocene_day

    @property
    def gregorian_holocene_isoformat(self) -> str:
        return self._date.gregorian_holocene_isoformat

    @property
    def symmetric_date(self):
        return self._date.symmetric_date

    @property
    def symmetric_year(self) -> int:
        return self._date.symmetric_year

    @property
    def symmetric_month(self) -> int:
        return self._date.symmetric_month

    @property
    def symmetric_day(self) -> int:
        return self._date.symmetric_day

    @property
    def symmetric_isoformat(self) -> str:
        return self._date.symmetric_isoformat

    @property
    def symmetric_holocene_date(self):
        return self._date.symmetric_holocene_date

    @property
    def symmetric_holocene_year(self) -> int:
        return self._date.symmetric_holocene_year

    @property
    def symmetric_holocene_month(self) -> int:
        return self._date.symmetric_holocene_month

    @property
    def symmetric_holocene_day(self) -> int:
        return self._date.symmetric_holocene_day

    @property
    def symmetric_holocene_isoformat(self) -> str:
        return self._date.symmetric_holocene_isoformat

    @property
    def timetuple(self):
        return self._date.timetuple

    def toordinal(self) -> SezimalInteger:
        return self._date.toordinal()

    @property
    def ordinal_date(self) -> SezimalInteger:
        return self._date.ordinal_date

    @property
    def isocalendar(self):
        return self._date.isocalendar()

    @property
    def julian_date(self) -> Sezimal:
        return self.as_days + ISO_EPOCH_JULIAN_DATE

    @property
    def mars_sol_date(self) -> Sezimal:
        return mars_sol_date(self.julian_date)

    @property
    def uta(self) -> SezimalInteger:
        return self._time.uta

    @property
    def posha(self) -> SezimalInteger:
        return self._time.posha

    @property
    def agrima(self) -> SezimalInteger:
        return self._time.agrima

    @property
    def anuga(self) -> SezimalInteger:
        return self._time.anuga

    @property
    def boda(self) -> SezimalInteger:
        return self._time.boda

    @property
    def shaditiboda(self) -> Sezimal:
        return self._time.shaditiboda

    @property
    def time_zone(self) -> str:
        return self._time.time_zone

    @property
    def is_dst(self) -> bool:
        return self._time.is_dst

    @property
    def iso_time(self):
        return self._time.iso_time

    @property
    def iso_hour(self) -> int:
        return self._time.iso_hour

    @property
    def iso_minute(self) -> int:
        return self._time.iso_minute

    @property
    def iso_second(self) -> int:
        return self._time.iso_second

    @property
    def iso_microsecond(self) -> int:
        return self._time.iso_microsecond

    @property
    def as_agrimas(self) -> Sezimal:
        return self._date.as_agrimas + self._time.as_agrimas

    @property
    def as_seconds(self) -> Decimal:
        return self._date.as_seconds + self._time.as_seconds

    def format(self, fmt: str = None, locale: str | SezimalLocale = None, season_moon_time_format: str = None) -> str:
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
            fmt = locale.DATE_TIME_FORMAT

        fmt = fmt.replace('##', '_|_HASHTAG_|_')
        fmt = fmt.replace('%%', '_|_PERCENT_|_')

        fmt = self._date.format(fmt, locale=locale, skip_strftime=True, time_zone=self.time_zone, season_moon_time_format=season_moon_time_format)
        fmt = self._time.format(fmt, locale=locale, skip_strftime=True)

        if type(self.iso_date_time) != tuple and '%' in fmt:
            fmt = self.iso_date_time.strftime(fmt)

        fmt = fmt.replace('_|_HASHTAG_|_', '#')
        fmt = fmt.replace('_|_PERCENT_|_', '%')

        return fmt

    @classmethod
    def now(cls, time_zone: str = None) -> Self:
        time = SezimalTime.now(time_zone=time_zone)

        if time.day:
            date = SezimalDate.from_days(SezimalDate.today().as_days + 1)
        else:
            date = SezimalDate.today()

        return cls(year=date, uta=time)

    @classmethod
    def today(cls) -> Self:
        today = SezimalDate.today()
        return cls(year=today)

    @property
    def timestamp(self) -> float:
        timestamp = self._date.timestamp
        timestamp += float(self._time.as_seconds)
        return timestamp

    @classmethod
    def from_timestamp(cls, timestamp: int | float | Decimal | Sezimal | SezimalInteger, time_zone: str | ZoneInfo = None) -> Self:
        if type(timestamp) in (Sezimal, SezimalInteger):
            timestamp = timestamp.decimal

        if not time_zone:
            time_zone = system_time_zone()

        time_zone = str(time_zone)

        ordinal_date, agrimas = timestamp_to_ordinal_date_and_agrima(timestamp, time_zone)

        date = SezimalDate.from_ordinal_date(ordinal_date)
        time = SezimalTime(agrima=agrimas, time_zone=time_zone, base_gregorian_date=date.gregorian_date)

        return cls(year=date, uta=time, time_zone=time_zone)

    @property
    def iso_date_time(self):
        return self._iso_date_time

    @property
    def date(self) -> SezimalDate:
        return self._date

    @property
    def time(self) -> SezimalTime:
        return self._time

    def at_time_zone(self, time_zone: str | ZoneInfo = 'UTC') -> Self:
        if not time_zone:
            time_zone = 'UTC'

        if self.time_zone == str(time_zone):
            return self

        utc_agrimas = self.as_agrimas - self.time._time_zone_offset # - self._dst_offset

        if self.time.day:
            utc_agrimas -= Sezimal('1_000_000') * self.time.day

        tz_offset, dst_offset = tz_agrimas_offset(time_zone)
        tz_agrimas = utc_agrimas + tz_offset # + dst_offset
        tz_days = tz_agrimas / 1_000_000
        return SezimalDateTime.from_days(days=tz_days, time_zone=time_zone)

    @classmethod
    def combine(cls, date: SezimalDate, time: SezimalTime, time_zone: str | ZoneInfo = None) -> Self:
        return cls(year=date, uta=time, time_zone=time_zone)

    @property
    def as_days(self) -> Sezimal:
        if self._date.as_days < 0:
            return self._date.as_days - self._time.as_days
        else:
            return self._date.as_days + self._time.as_days

    @classmethod
    def from_days(cls, days: Sezimal, time_zone: str | ZoneInfo = None) -> Self:
        date = SezimalDate.from_days(days)
        days = abs(days)
        days -= SezimalInteger(days)
        time = SezimalTime.from_days(days, time_zone)
        return cls.combine(date, time, time_zone)

    def replace(self,
        year: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        uta: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        posha: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        agrima: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        anuga: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        boda: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        shaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        time_zone: str | ZoneInfo = None,
    ) -> Self:
        date = self._date.replace(year, month, day)
        time = self._time.replace(uta, posha, agrima, anuga, boda, shaditiboda, time_zone=time_zone)
        return type(self).combine(date, time, time.time_zone)

    @classmethod
    def from_julian_date(cls, julian_date: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction, time_zone: str | ZoneInfo = None) -> Self:
        julian_date = Sezimal(julian_date)
        ordinal_date = julian_date - ISO_EPOCH_JULIAN_DATE
        return cls.from_days(ordinal_date, time_zone)

    def previous(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        date = self._date.previous(days, weeks, months, quarters, years)
        return self.combine(date, self._time, self.time_zone)

    def next(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        date = self._date.next(days, weeks, months, quarters, years)
        return self.combine(date, self._time, self.time_zone)

    @property
    def week_proportion_ellapsed(self) -> Sezimal:
        return self.date.week_proportion_ellapsed

    @property
    def month_proportion_ellapsed(self) -> Sezimal:
        return self.date.month_proportion_ellapsed

    @property
    def quarter_proportion_ellapsed(self) -> Sezimal:
        return self.date.quarter_proportion_ellapsed

    @property
    def year_proportion_ellapsed(self) -> Sezimal:
        return self.date.year_proportion_ellapsed
