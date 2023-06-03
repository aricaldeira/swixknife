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

import datetime as _datetime
import time as _time
from pytz import timezone

from decimal import Decimal

from .date import SezimalDate
from .time import SezimalTime, TIME_SEPARATOR, tz_agrimas_offset
from ..sezimal import Sezimal, SezimalInteger
from ..units.conversions import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA


class SezimalDateTime():
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
        ekaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        time_zone: str = None,
        ):
        self = object.__new__(cls)

        if type(year) == SezimalDate:
            self._date = year
        elif type(year) == _datetime.date:
            self._date = SezimalDate(year)
        elif type(year) == _datetime.datetime:
            if year.tzinfo:
                return cls.from_timestamp(year.timestamp(), str(year.tzinfo))

            return cls.from_timestamp(year.timestamp(), time_zone)
        else:
            self._date = SezimalDate(year=year, month=month, day=day)

        if type(uta) == SezimalTime:
            self._time = uta
            time_zone = self._time.time_zone
        else:
            self._time = SezimalTime(uta=uta, posha=posha, agrima=agrima, anuga=anuga, boda=boda, ekaditiboda=ekaditiboda, day=0, time_zone=time_zone)

        if type(self._date.gregorian_date) == _datetime.date:
            if time_zone:
                self._iso_date_time = _datetime.datetime.fromtimestamp(self.timestamp, tz=timezone(self.time_zone))
            else:
                self._iso_date_time = _datetime.datetime.fromtimestamp(self.timestamp)

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

    def __repr__(self):
        return f'{self.__class__.__qualname__}(year={self.year.formatted_number}, month={self.month}, day={self.day}, uta={self.uta}, posha={self.posha}, agrima={self.agrima}, anuga={self.anuga}, boda={self.boda}, ekaditiboda={self.ekaditiboda}, time_zone={self.time_zone})'

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

    def isoformat(self):
        return self.format(f'#y-#m-#d #u{TIME_SEPARATOR}#p{TIME_SEPARATOR}#a.#n#b#e #t #V')

    __str__ = isoformat

    @property
    def year(self):
        return self._date._year

    @property
    def month(self):
        return self._date._month

    @property
    def day(self):
        return self._date._day

    @property
    def is_leap(self):
        return bool(self._date._is_leap)

    @property
    def weekday(self):
        return self._date._weekday

    @property
    def week_in_month(self):
        return self._date.week_in_month

    @property
    def day_in_year(self):
        return self._date._day_in_year

    @property
    def week_in_year(self):
        return self._date._week_in_year

    @property
    def quarter(self):
        return self._date._quarter

    @property
    def day_in_quarter(self):
        return self._date._day_in_quarter

    @property
    def week_in_quarter(self):
        return self._date._week_in_quarter

    @property
    def month_in_quarter(self):
        return self._date._month_in_quarter

    @property
    def weekday_name(self):
        return self._date.weekday_name

    @property
    def weekday_abbreviated_name(self):
        return self._date.weekday_abbreviated_name

    @property
    def month_name(self):
        return self._date.month_name

    @property
    def month_abbreviated_name(self):
        return self._date.month_abbreviated_name

    @property
    def era_name(self):
        return self._date.era_name

    @property
    def day_ordinal_suffix(self):
        return self._date.day_ordinal_suffix

    @property
    def gregorian_year(self):
        return self._date.gregorian_year

    @property
    def gregorian_month(self):
        return self._date.gregorian_month

    @property
    def gregorian_day(self):
        return self._date.gregorian_day

    @property
    def gregorian_isoformat(self):
        return self._date.gregorian_isoformat

    @property
    def gregorian_holocene_date(self):
        return self._date.gregorian_holocene_date

    @property
    def gregorian_holocene_year(self):
        return self._date.gregorian_holocene_year

    @property
    def gregorian_holocene_month(self):
        return self._date.gregorian_holocene_month

    @property
    def gregorian_holocene_day(self):
        return self._date.gregorian_holocene_day

    @property
    def gregorian_holocene_isoformat(self):
        return self._date.gregorian_holocene_isoformat

    @property
    def symmetric_date(self):
        return self._date.symmetric_date

    @property
    def symmetric_year(self):
        return self._date.symmetric_year

    @property
    def symmetric_month(self):
        return self._date.symmetric_month

    @property
    def symmetric_day(self):
        return self._date.symmetric_day

    @property
    def symmetric_isoformat(self):
        return self._date.symmetric_isoformat

    @property
    def symmetric_holocene_date(self):
        return self._date.symmetric_holocene_date

    @property
    def symmetric_holocene_year(self):
        return self._date.symmetric_holocene_year

    @property
    def symmetric_holocene_month(self):
        return self._date.symmetric_holocene_month

    @property
    def symmetric_holocene_day(self):
        return self._date.symmetric_holocene_day

    @property
    def symmetric_holocene_isoformat(self):
        return self._date.symmetric_holocene_isoformat

    @property
    def timetuple(self):
        return self._date.timetuple

    def toordinal(self):
        return self._date.toordinal()

    @property
    def ordinal_date(self):
        return self._date.ordinal_date

    @property
    def isocalendar(self):
        return self._date.isocalendar()

    @property
    def julian_date(self):
        return round(self._date.julian_date + self._time.julian_date, 10)

    @property
    def uta(self):
        return self._time.uta

    @property
    def posha(self):
        return self._time.posha

    @property
    def agrima(self):
        return self._time.agrima

    @property
    def anuga(self):
        return self._time.anuga

    @property
    def boda(self):
        return self._time.boda

    @property
    def ekaditiboda(self):
        return self._time.ekaditiboda

    @property
    def time_zone(self):
        return self._time.time_zone

    @property
    def is_dst(self):
        return self._time.is_dst

    @property
    def iso_time(self):
        return self._time.iso_time

    @property
    def iso_hour(self):
        return self._time.iso_hour

    @property
    def iso_minute(self):
        return self._time.iso_minute

    @property
    def iso_second(self):
        return self._time.iso_second

    @property
    def iso_microsecond(self):
        return self._time.iso_microsecond

    @property
    def as_agrimas(self):
        return self._date.as_agrimas + self._time.as_agrimas

    @property
    def as_seconds(self):
        return self._date.as_seconds + self._time.as_seconds

    def format(self, fmt: str = f'#_y-#m-#d #u{TIME_SEPARATOR}#p{TIME_SEPARATOR}#a', lang=None):
        fmt = self._date.format(fmt, lang=lang, skip_strftime=True)
        fmt = self._time.format(fmt, skip_strftime=True)

        if type(self.iso_date_time) != tuple and '%' in fmt:
            fmt = self.iso_date_time.strftime(fmt)

        return fmt

    @classmethod
    def now(cls, time_zone: str = None):
        time = SezimalTime.now(time_zone=time_zone)
        date = SezimalDate.today()
        return cls(year=date, uta=time)

    @classmethod
    def today(cls):
        today = SezimalDate.today()
        return cls(year=today)

    @property
    def timestamp(self):
        timestamp = self._date.timestamp
        timestamp += float(self._time.as_seconds)
        return timestamp

    @classmethod
    def from_timestamp(cls, timestamp: int | float | Decimal | Sezimal | SezimalInteger, time_zone: str = None):
        if type(timestamp) in (Sezimal, SezimalInteger):
            timestamp = timestamp.decimal

        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(float(timestamp))

        ordinal_date = _datetime.date(y, m, d).toordinal()

        total_seconds = hh * 60 * 60
        total_seconds += mm * 60
        total_seconds += ss
        total_seconds += timestamp - int(timestamp)
        total_agrimas = Decimal(total_seconds) * SECOND_TO_AGRIMA

        agrimas_offset, agrimas_dst_offset = tz_agrimas_offset(time_zone)

        total_agrimas -= agrimas_offset

        date = SezimalDate.fromordinal(ordinal_date)
        time = SezimalTime(agrima=total_agrimas, time_zone=time_zone)

        return cls(year=date, uta=time)

    @property
    def iso_date_time(self):
        return self._iso_date_time
