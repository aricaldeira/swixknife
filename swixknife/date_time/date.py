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

import re
import time as _time
import datetime as _datetime
from dateutils import relativedelta

from decimal import Decimal
from zoneinfo import ZoneInfo

from ..sezimal import Sezimal, SezimalInteger
from ..dozenal import Dozenal, DozenalInteger
from ..base import decimal_format, sezimal_format, \
    sezimal_to_niftimal, default_to_sezimal_digits, \
    default_niftimal_to_sezimal_digits, default_niftimal_to_regularized_digits, \
    default_niftimal_to_niftimal_digits
from .gregorian_functions import ordinal_date_to_gregorian_year_month_day, \
    gregorian_year_month_day_to_iso_year_week_day
from ..units import sezimal_to_decimal_unit
from .date_time_delta import SezimalDateTimeDelta
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from .sezimal_functions import *
from .format_tokens import DATE_NUMBER_FORMAT_TOKENS, \
    YEAR_NUMBER_FORMAT_TOKENS, DATE_TEXT_FORMAT_TOKEN, \
    ISO_DATE_NUMBER_FORMAT_TOKENS
from .dcc_functions import \
    ordinal_date_to_year_month_day as ordinal_date_to_dcc_year_month_day

try:
    from convertdate.julian import \
        from_gregorian as gregorian_to_julian, \
        to_gregorian as julian_to_gregorian, \
        month_length as julian_month_length

    from pyluach.dates import \
        GregorianDate as GregorianToHebrew, \
        HebrewDate as HebrewToGregorian

    from hijridate import \
        Gregorian as GregorianToHijri, \
        Hijri as HijriToGregorian

    CAN_CONVERT_CALENDARS = True
except:
    CAN_CONVERT_CALENDARS = False


class SezimalDate:
    __slots__ = (
        '_year', '_month', '_day', '_hashcode', '_gregorian_date',
        '_is_leap', '_ordinal_date', '_weekday',
        '_day_in_year', '_day_in_week', '_week_in_year',
        '_quarter', '_day_in_quarter', '_week_in_quarter', '_month_in_quarter',
        '_dcc_date'
    )

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

        self._dcc_date = ordinal_date_to_dcc_year_month_day(self._ordinal_date)

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
    def today(cls, time_zone: str = None) -> Self:
        "Construct a date from time.time()."
        if not time_zone:
            time_zone = system_time_zone()

        t = _datetime.datetime.now(tz=ZoneInfo(time_zone))

        return cls(t)

    @classmethod
    def from_ordinal_date(cls, ordinal_date) -> Self:
        ordinal_date = SezimalInteger(ordinal_date)
        y, m, d, *x = ordinal_to_year_month_day(ordinal_date)
        return cls(y, m, d)

    @classmethod
    def from_iso_format(cls, date_string) -> Self:
        return cls.from_ordinal_date(_datetime.date.fromisoformat(date_string).toordinal())

    @classmethod
    def from_iso_calendar(cls, year, week, day) -> Self:
        return cls.from_ordinal_date(_datetime.date.fromisocalendar(year, week, day).toordinal())

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
    def total_weeks_in_month(self) -> SezimalInteger:
        if self.is_long_month:
            return SezimalInteger(5)

        return SezimalInteger(4)

    @property
    def total_days_in_year(self) -> SezimalInteger:
        if self.is_leap:
            return SezimalInteger('1415')

        return SezimalInteger('1404')

    @property
    def day_in_year(self) -> SezimalInteger:
        return self._day_in_year

    @property
    def total_weeks_in_year(self) -> SezimalInteger:
        if self.is_leap:
            return SezimalInteger('125')

        return SezimalInteger('124')

    @property
    def week_in_year(self) -> SezimalInteger:
        return self._week_in_year

    @property
    def quarter(self) -> SezimalInteger:
        return self._quarter

    @property
    def total_days_in_quarter(self) -> SezimalInteger:
        if self.quarter == 4 and self.is_leap:
            return SezimalInteger('242')

        return SezimalInteger('231')

    @property
    def day_in_quarter(self) -> SezimalInteger:
        return self._day_in_quarter

    @property
    def total_weeks_in_quarter(self) -> SezimalInteger:
        if self.quarter == 4 and self.is_leap:
            return SezimalInteger('22')

        return SezimalInteger('21')

    @property
    def week_in_quarter(self) -> SezimalInteger:
        return self._week_in_quarter

    @property
    def total_months_in_quarter(self) -> SezimalInteger:
        return SezimalInteger('4')

    @property
    def month_in_quarter(self) -> SezimalInteger:
        return self._month_in_quarter

    @property
    def total_months_in_year(self) -> SezimalInteger:
        return SezimalInteger('20')

    @property
    def total_days_in_month(self) -> SezimalInteger:
        if self.is_long_month:
            return SezimalInteger('55')

        return SezimalInteger('44')

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

    def _apply_number_format(self, token: str, value_name: str, size: int | SezimalInteger = None, locale: SezimalLocale = None, from_decimal: bool = False) -> str:
        value = getattr(self, value_name, 0)

        if token.startswith('#') and value_name.startswith('gregorian_') or value_name.startswith('symmetric_'):
            if type(value) == Decimal:
                value = SezimalInteger(value)
            else:
                value = SezimalInteger(Decimal(value))

        if from_decimal:
            value = Decimal(str(value))

        if '*' in token and (not value):
            return ''

        if '@' in token or 'Z' in token:
            if from_decimal:
                value = SezimalInteger(value)

            value = str(value)

            value = sezimal_to_niftimal(value)

            #
            # For the year, using “>”
            # yields only the last 2 digits
            #
            if token.endswith('>y'):
                value = value[::-1][0:2][::-1]

            if size and '-' not in token and '>' not in token:
                if value[0] == '-':
                    value = value.zfill(int(SezimalInteger(size)) + 1)
                else:
                    value = value.zfill(int(SezimalInteger(size)))

            if '!' in token:
                value = default_niftimal_to_niftimal_digits(value)
            elif '@' in token:
                value = default_niftimal_to_regularized_digits(value)

        else:
            if '5' in token:
                value = str(SezimalInteger(value))

                #
                # For the year, using “>”
                # yields only the last 3 digits
                #
                if '>y' in token and value >= '213100' and value < '214000':
                    value = value[::-1][0:3][::-1]
                elif ('%5Y' in token or '%5!Y' in token) and value >= '13100' and value < '14000':
                    value = value[::-1][0:3][::-1]
                    size -= 2

                if len(value) >= 5:
                    value = value[::-1]
                    value = value[0:3] + locale.GROUP_SEPARATOR + value[3:]
                    value = value[::-1]

            elif '↋' in token:
                value = str(DozenalInteger(value))

                #
                # For the year, using “>”
                # yields only the last 2 digits
                #
                if '>y' in token:
                    value = value[::-1][0:2][::-1]

            elif '9' in token or from_decimal:
                if from_decimal:
                    value = str(int(value))
                else:
                    value = str(int(value.decimal))

                #
                # For the year, using “>”
                # yields only the last 2 digits
                #
                if '>y' in token:
                    value = value[::-1][0:2][::-1]

            else:
                value = str(value)

                #
                # For the year, using “>”
                # yields only the last 3 digits
                #
                if '>y' in token and value >= '213100' and value < '214000':
                    value = value[::-1][0:3][::-1]

            if size and '-' not in token and '>' not in token:
                if value[0] == '-':
                    value = value.zfill(int(SezimalInteger(size)) + 1)
                else:
                    value = value.zfill(int(SezimalInteger(size)))

            if '!' in token:
                value = default_to_sezimal_digits(value)

            elif '?' in token:
                value = locale.digit_replace(value)

        if value[0] == '-':
            value = '−' + value[1:]

        return value

    def format(self, fmt: str = None, locale: str | SezimalLocale = None, skip_strftime: bool = False, time_zone: str | ZoneInfo = None) -> str:
        if not fmt:
            return fmt

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
        # Day Count Calendar formats
        #
        fmt = self._apply_dcc_formats(fmt, locale=locale)

        #
        # Locale’s date separator
        #
        if '#/' in fmt:
            if locale:
                fmt = fmt.replace('#/', locale.DATE_SEPARATOR)
            else:
                fmt = fmt.replace('#/', '-')

        #
        # Year’s explicit sign
        #
        if '#+' in fmt:
            if self.year >= 0:
                fmt = fmt.replace('#+', '+')
            else:
                fmt = fmt.replace('#+', '')

        #
        # Let’s deal first with the numeric formats
        #
        for regex, token, base, zero, character, value_name, \
            size, size_niftimal, size_decimal in DATE_NUMBER_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            if base in ['@', '@!', 'Z']:
                value = self._apply_number_format(token, value_name, size_niftimal, locale)
            elif base in ['9', '9?', '↋', '↋?']:
                value = self._apply_number_format(token, value_name, size_decimal, locale)
            else:
                value = self._apply_number_format(token, value_name, size, locale)

            if locale and locale.RTL:
                value = '\N{LRI}' + value + '\N{PDI}'

            fmt = regex.sub(value, fmt)

        #
        # Formatted year number
        #
        for regex, token, base, separator, character, value_name in YEAR_NUMBER_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            year = getattr(self, value_name, 0)

            if 'X' in character and not separator:
                separator = '\U000f1e6d'  # Arda separator

            if value_name.startswith('gregorian_') or value_name.startswith('symmetric_'):
                if type(year) == Decimal:
                    year = SezimalInteger(year)
                else:
                    year = SezimalInteger(Decimal(year))

            if base in ['', '!', '?']:
                if '>' in character:
                    if value_name in ('year', 'dcc_year') \
                        and year >= '213100' and year < '214000':
                        year -= 213_000
                    elif value_name == 'gregorian_year' \
                        and year >= '13100' and year <= '14000':
                        year -= 13_000

                year = locale.format_number(
                    year,
                    sezimal_digits='!' in base,
                    use_group_separator=True,
                    sezimal_places=0,
                )

            elif base in ['@', '@!', 'Z', 'Z?']:
                year = locale.format_niftimal_number(
                    year,
                    sezimal_digits='!' in base,
                    regularized_digits='@' in base,
                    use_group_separator=True,
                    niftimal_places=0,
                )

            elif base in ['9', '9?']:
                year = locale.format_decimal_number(
                    year,
                    use_group_separator=True,
                    decimal_places=0,
                )

            elif base in ['↋', '↋?']:
                year = locale.format_dozenal_number(
                    year,
                    use_group_separator=True,
                    dozenal_places=0,
                )

            if '?' in base:
                year = locale.digit_replace(year)

            if separator:
                if separator[0] == '\\' and len(separator) >= 2:
                    separator = separator[1:]

                if separator != locale.GROUP_SEPARATOR:
                    year = year.replace(locale.GROUP_SEPARATOR, separator)

            if locale and locale.RTL:
                year = '\N{LRI}' + year + '\N{PDI}'

            fmt = regex.sub(year, fmt)

        #
        # And now, the text formats
        #
        for base, size, case, month_week, calendar in DATE_TEXT_FORMAT_TOKEN.findall(fmt):
            regex = re.compile(fr'#{base}{size}{case}{month_week}{calendar}')

            if month_week == 'M':
                if size == '@':
                    if calendar == '&':
                        text = locale.dcc_month_abbreviated_name(self.dcc_month)
                    elif base:
                        text = locale.iso_month_abbreviated_name(self.month)
                    else:
                        text = locale.month_abbreviated_name(self.month)
                else:
                    if calendar == '&':
                        text = locale.dcc_month_name(self.dcc_month)
                    elif base:
                        text = locale.iso_month_name(self.month)
                    else:
                        text = locale.month_name(self.month)

            else:
                if calendar == '&':
                    if size:
                        text = locale.dcc_weekday_abbreviated_name(self.dcc_weekday)
                    else:
                        text = locale.dcc_weekday_name(self.dcc_weekday)
                else:
                    if size:
                        text = locale.weekday_abbreviated_name(self.weekday)
                    else:
                        text = locale.weekday_name(self.weekday)

            if size == '1':
                if calendar == '&':
                    text = locale.dcc_weekday_symbol(self.dcc_weekday)
                else:
                    text = locale.weekday_symbol(self.weekday)
            elif size == '2':
                text = locale.slice(text, 0, 2)
            elif size == '3':
                text = locale.slice(text, 0, 3)

            if case == '!':
                text = locale.upper(text) if locale else text.upper()
            elif case == '?':
                text = locale.lower(text) if locale else text.lower()
            elif case == '>':
                if locale:
                    text = locale.upper(text[0]) + locale.lower(text[1:])
                else:
                    text = text[0].upper() + text[1:].lower()

            fmt = regex.sub(text, fmt)

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

            for regex, token, base, zero, character, value_name, \
                size_decimal, size_niftimal, size_sezimal in ISO_DATE_NUMBER_FORMAT_TOKENS:
                if not regex.findall(fmt):
                    continue

                if token.endswith('y'):
                    token = token[0:-1] + '>y'
                    size_sezimal -= 2
                    size_niftimal -= 1
                    size_decimal -= 2

                if base in ['@', '@!', 'Z']:
                    value = self._apply_number_format(token, value_name, size_niftimal, locale, from_decimal=True)
                elif base in ['5', '5!', '5?']:
                    value = self._apply_number_format(token, value_name, size_sezimal, locale, from_decimal=True)
                elif base in ['↋', '↋?']:
                    value = self._apply_number_format(token, value_name, size_decimal, locale, from_decimal=True)
                else:
                    value = self._apply_number_format(token, value_name, size_decimal, locale, from_decimal=True)

                if locale and locale.RTL:
                    value = '\N{LRI}' + value + '\N{PDI}'

                fmt = regex.sub(value, fmt)

            if '%A' in fmt:
                fmt = fmt.replace('%A', locale.weekday_name(self.weekday))

            if '%a' in fmt:
                fmt = fmt.replace('%a', locale.weekday_abbreviated_name(self.weekday))

            if '%o' in fmt:
                fmt = fmt.replace('%o', locale.day_ordinal_suffix(Decimal(self.gregorian_day)))

            if '%O' in fmt:
                fmt = fmt.replace('%O', locale.day_ordinal_suffix(Decimal(self.gregorian_day)))

            if '%B' in fmt:
                fmt = fmt.replace('%B', locale.iso_month_name(Decimal(self.gregorian_month)))

            if '%b' in fmt:
                fmt = fmt.replace('%b', locale.iso_month_abbreviated_name(Decimal(self.gregorian_month)))

            if not skip_strftime:
                if type(self.gregorian_date) == _datetime.date:
                    fmt = fmt.replace('__PERCENT__', '%%')
                    fmt = self.gregorian_date.strftime(fmt)

            fmt = fmt.replace('__PERCENT__', '%')

        return fmt

    @classmethod
    def from_gregorian(cls, year: int | Decimal, month: int | Decimal, day: int | Decimal) -> Self:
        return cls.from_ordinal_date(gregorian_year_month_day_to_ordinal_date(int(year), int(month), int(day)))

    @property
    def gregorian_year(self) -> Decimal:
        if type(self._gregorian_date) in (list, tuple):
            return Decimal(self._gregorian_date[0])

        return Decimal(self.gregorian_date.year)

    @property
    def gregorian_month(self) -> Decimal:
        if type(self._gregorian_date) in (list, tuple):
            return Decimal(self._gregorian_date[1])

        return Decimal(self.gregorian_date.month)

    @property
    def gregorian_day(self) -> Decimal:
        if type(self._gregorian_date) in (list, tuple):
            return Decimal(self._gregorian_date[2])

        return Decimal(self.gregorian_date.day)

    @property
    def gregorian_is_leap(self) -> bool:
        return \
            (self.gregorian_year % 4 == 0) \
            and (
                self.gregorian_year % 100 != 0
                or self.gregorian_year % 400 == 0
            )

    @property
    def gregorian_day_in_year(self) -> int:
        last_years_last_ordinal_date = gregorian_year_month_day_to_ordinal_date(self.gregorian_year - 1, 12, 31)

        return int(self.ordinal_date - last_years_last_ordinal_date)

    @property
    def gregorian_week_in_year(self) -> int:
        return self.gregorian_date.isocalendar().week

    @property
    def gregorian_total_days_in_year(self) -> int:
        if self.gregorian_is_leap:
            return 366

        return 365

    @property
    def iso_year(self) -> int:
        y, w, d = gregorian_year_month_day_to_iso_year_week_day(
            self.gregorian_year,
            self.gregorian_month,
            self.gregorian_day,
        )

        return y

    @property
    def iso_week(self) -> int:
        y, w, d = gregorian_year_month_day_to_iso_year_week_day(
            self.gregorian_year,
            self.gregorian_month,
            self.gregorian_day,
        )

        return w

    @property
    def iso_weekday(self) -> int:
        y, w, d = gregorian_year_month_day_to_iso_year_week_day(
            self.gregorian_year,
            self.gregorian_month,
            self.gregorian_day,
        )

        return d

    @property
    def iso_total_weeks_in_year(self) -> int:
        first_day_of_year = SezimalDate.from_gregorian(self.gregorian_year, 1, 1)

        if first_day_of_year.weekday == 4:
            return 53

        return 52

    @property
    def iso_weekformat(self) -> str:
        return f'{str(self.iso_year).zfill(4)}-W{str(self.iso_week).zfill(2)}-{self.iso_weekday}'

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
    def gregorian_is_leap(self):
        year = self.gregorian_year
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

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
    def julian_day(self) -> Sezimal:
        return self.ordinal_date + ISO_EPOCH_JULIAN_DAY

    @property
    def mars_sol(self) -> Sezimal:
        return mars_sol(self.julian_day)

    def replace(self,
        year: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        if year is None or not year:
            year = self._year

        if month is None or not month:
            month = self._month

        if day is None or not day:
            day = self._day
        else:
            day = SezimalInteger(day)

        if day > 44:
            if month == 20:
                if not is_leap(year - 200_000):
                    day -= 11
            elif month not in (2, 5, 12, 15):
                day -= 11

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

        return SezimalDate.from_ordinal_date(other._total_days + self.ordinal_date)

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
        self._year = yhi * SezimalInteger('1_104') + ylo

    def __reduce__(self):
        return (self.__class__, self._getstate())

    @property
    def as_agrimas(self) -> SezimalInteger:
        return self.ordinal_date * 1_000_000

    @property
    def as_seconds(self) -> Decimal:
        seconds = sezimal_to_decimal_unit(self.as_agrimas, 'agm', 's')
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
        MOON_MONTH = Sezimal('312_113') / Sezimal('3_534')

        #
        # Date and time at the end of the day
        # minus 1 day, compensating the moon cycle
        #
        moon_phase = self.ordinal_date - 1
        moon_phase += Sezimal('0.555_555')

        #
        # Specific point in time where the moon was knowingly
        # on the new phase:
        #
        # Ordinal date 23_014_020.04
        # Sezimal date 131_111-01-25 04:00
        # Gregorian date 1923-01-17 02:40
        #
        # It was first new moon of the first lunation (lunar month),
        # according to this site: https://www.timeanddate.com/moon/phases/?year=1923
        #
        moon_phase -= Sezimal('23_014_020.04')

        day_in_cycle = moon_phase.decimal % MOON_MONTH.decimal

        if day_in_cycle < 0:
            day_in_cycle = MOON_MONTH.decimal + day_in_cycle

        persixniff = Sezimal(day_in_cycle / MOON_MONTH.decimal * 216)

        if persixniff > 1_000:
            persixniff -= 1_000

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

    def previous(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        res = self

        if days:
            res = res.from_days(res.as_days - days)

        if weeks:
            res = res.from_days(res.as_days - (weeks * SezimalInteger(11)))

        months = SezimalInteger(months or 0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if months:
            year = res.year
            month = res.month - months

            while month <= 0:
                year -= 1
                month += 20

            res = res.replace(year=year, month=month)

        return res

    def next(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        res = self

        if days:
            res = res.from_days(res.as_days + days)

        if weeks:
            res = res.from_days(res.as_days + (weeks * SezimalInteger(11)))

        months = SezimalInteger(months or 0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if months:
            year = res.year
            month = res.month + months

            while month > 20:
                year += 1
                month -= 20

            res = res.replace(year=year, month=month)

        return res

    def gregorian_previous(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        res = self

        if days:
            res = res.from_days(res.as_days - days)

        if weeks:
            res = res.from_days(res.as_days - (weeks * SezimalInteger(11)))

        months = SezimalInteger(months or 0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if months:
            res = SezimalDate(res.gregorian_date - relativedelta(months=int(months.decimal)))

        return res

    def gregorian_next(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        res = self

        if days:
            res = res.from_days(res.as_days + days)

        if weeks:
            res = res.from_days(res.as_days + (weeks * SezimalInteger(11)))

        months = SezimalInteger(months or 0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if months:
            res = SezimalDate(res.gregorian_date + relativedelta(months=int(months.decimal)))

        return res

    @property
    def week_proportion_ellapsed(self) -> Sezimal:
        return (self.weekday - 1) / 11

    @property
    def month_proportion_ellapsed(self) -> Sezimal:
        return (self.day - 1) / self.total_days_in_month

    @property
    def quarter_proportion_ellapsed(self) -> Sezimal:
        return (self.day_in_quarter - 1) / self.total_days_in_quarter

    @property
    def year_proportion_ellapsed(self) -> Sezimal:
        return (self.day_in_year - 1) / self.total_days_in_year

    def julian_date(self, locale: SezimalLocale = None):
        if not CAN_CONVERT_CALENDARS:
            return ''

        year, month, day = gregorian_to_julian(int(self.gregorian_year), int(self.gregorian_month), int(self.gregorian_day))

        if not locale:
            jd = f'{str(year).zfill(4)}-{str(month).zfill(2)}-{str(day).zfill(2)}'
        elif locale.DATE_ENDIANNESS == 'B':
            jd = f'{str(year).zfill(4)}{locale.DATE_SEPARATOR}{str(month).zfill(2)}{locale.DATE_SEPARATOR}{str(day).zfill(2)}'
        elif locale.DATE_ENDIANNESS == 'L':
            jd = f'{str(day).zfill(2)}{locale.DATE_SEPARATOR}{str(month).zfill(2)}{locale.DATE_SEPARATOR}{str(year).zfill(4)}'
        else:
            jd = f'{str(month).zfill(2)}{locale.DATE_SEPARATOR}{str(day).zfill(2)}{locale.DATE_SEPARATOR}{str(year).zfill(4)}'

        return jd

    def julian_previous(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        #
        # Days and weeks are the same, so we just use the regular
        # function for them
        #
        res = self.previous(days, weeks)

        #
        # Months, quarters and years, have different durations,
        # so let’s see
        #
        if not months:
            months = SezimalInteger(0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if not months:
            return res

        #
        # We have a number of months that we have to
        # go back in the calendar
        #
        jy, jm, jd = res.julian_date().split('-')
        jy = int(jy)
        jm = int(jm)
        jd = int(jd)

        jm -= int(months)

        #
        # Since all years have 12 months, we
        # go back 1 year for every 12 months we need
        # to go back in the calendar
        #
        while jm <= 0:
            jy -= 1
            jm += 12

        #
        # Finally, let’s see if the day, 29, 30, 31,
        # exists for that particular month we landed
        #
        if julian_month_length(jy, jm) < jd:
            jd = julian_month_length(jy, jm)

        gregorian_date = julian_to_gregorian(jy, jm, jd)
        ordinal_date = gregorian_year_month_day_to_ordinal_date(*gregorian_date)

        return SezimalDate.from_ordinal_date(ordinal_date)

    def julian_next(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        #
        # Days and weeks are the same, so we just use the regular
        # function for them
        #
        res = self.next(days, weeks)

        #
        # Months, quarters and years, have different durations,
        # so let’s see
        #
        if not months:
            months = SezimalInteger(0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if not months:
            return res

        #
        # We have a number of months that we have to
        # go back in the calendar
        #
        jy, jm, jd = res.julian_date().split('-')
        jy = int(jy)
        jm = int(jm)
        jd = int(jd)

        jm += int(months)

        #
        # Since all years have 12 months, we
        # advance 1 year for every 12 months we need
        # to go further in the calendar
        #
        while jm > 12:
            jy += 1
            jm -= 12

        #
        # Finally, let’s see if the day, 29, 30, 31,
        # exists for that particular month we landed
        #
        if julian_month_length(jy, jm) < jd:
            jd = julian_month_length(jy, jm)

        gregorian_date = julian_to_gregorian(jy, jm, jd)
        ordinal_date = gregorian_year_month_day_to_ordinal_date(*gregorian_date)

        return SezimalDate.from_ordinal_date(ordinal_date)

    def hebrew_date(self, locale: SezimalLocale = None, number: bool = True, short: bool = False):
        if not CAN_CONVERT_CALENDARS:
            return ''

        year, month, day = GregorianToHebrew(int(self.gregorian_year), int(self.gregorian_month), int(self.gregorian_day)).to_heb().tuple()

        if locale:
            year = str(year).zfill(4) + ' ' + locale.JEWISH_CALENDAR_ANNO_MUNDI
        else:
            year = str(year).zfill(4) + ' AM'

        if (not locale):
            day = str(day).zfill(2)
            month = str(month).zfill(2)
            return f'{year}-{month}-{day}'

        if number:
            day = str(day).zfill(2)
            month = str(month).zfill(2)
        else:
            day = str(day)

            if short:
                month = locale.JEWISH_CALENDAR_MONTH_ABBREVIATED_NAME[month - 1]
            else:
                month = locale.JEWISH_CALENDAR_MONTH_NAME[month - 1]

        if number:
            hd = locale.ISO_DATE_FORMAT

        elif short:
            hd = locale.ISO_DATE_TEXT_SHORT_MONTH_FORMAT

        else:
            hd = locale.ISO_DATE_LONG_FORMAT

        hd = hd.replace('%d', day).replace('%-d', day)
        hd = hd.replace('%?d', day).replace('%?-d', day)
        hd = hd.replace('%5d', day).replace('%5-d', day)
        hd = hd.replace('%m', month).replace('%-m', month)
        hd = hd.replace('%?m', month).replace('%?-m', month)
        hd = hd.replace('%5m', month).replace('%5-m', month)
        hd = hd.replace('%y', year).replace('%-y', year)
        hd = hd.replace('%?y', year).replace('%?-y', year)
        hd = hd.replace('%5y', year).replace('%5-y', year)
        hd = hd.replace('%Y', year).replace('%-Y', year)
        hd = hd.replace('%?Y', year).replace('%?-Y', year)
        hd = hd.replace('%5Y', year).replace('%5-Y', year)
        hd = hd.replace('%o', locale.day_ordinal_suffix(SezimalInteger(Decimal(int(day)))))
        hd = hd.replace('%b', month).replace('%B', month)

        return hd

    def hijri_date(self, locale: SezimalLocale = None, number: bool = True, short: bool = False):
        if not CAN_CONVERT_CALENDARS:
            return ''

        year, month, day = GregorianToHijri(int(self.gregorian_year), int(self.gregorian_month), int(self.gregorian_day)).to_hijri().datetuple()

        if locale:
            year = str(year).zfill(4) + ' ' + locale.HIJRI_CALENDAR_ANNO_HEGIRAE
        else:
            year = str(year).zfill(4) + ' AH'

        if (not locale):
            day = str(day).zfill(2)
            month = str(month).zfill(2)
            return f'{year}-{month}-{day}'

        if number:
            day = str(day).zfill(2)
            month = str(month).zfill(2)
        else:
            day = str(day)

            if short:
                month = locale.HIJRI_CALENDAR_MONTH_ABBREVIATED_NAME[month - 1]
            else:
                month = locale.HIJRI_CALENDAR_MONTH_NAME[month - 1]

        if number:
            hd = locale.ISO_DATE_FORMAT

        elif short:
            hd = locale.ISO_DATE_TEXT_SHORT_MONTH_FORMAT

        else:
            hd = locale.ISO_DATE_LONG_FORMAT

        hd = hd.replace('%d', day).replace('%-d', day)
        hd = hd.replace('%?d', day).replace('%?-d', day)
        hd = hd.replace('%5d', day).replace('%5-d', day)
        hd = hd.replace('%m', month).replace('%-m', month)
        hd = hd.replace('%?m', month).replace('%?-m', month)
        hd = hd.replace('%5m', month).replace('%5-m', month)
        hd = hd.replace('%y', year).replace('%-y', year)
        hd = hd.replace('%?y', year).replace('%?-y', year)
        hd = hd.replace('%5y', year).replace('%5-y', year)
        hd = hd.replace('%Y', year).replace('%-Y', year)
        hd = hd.replace('%?Y', year).replace('%?-Y', year)
        hd = hd.replace('%5Y', year).replace('%5-Y', year)
        hd = hd.replace('%o', locale.day_ordinal_suffix(SezimalInteger(Decimal(int(day)))))
        hd = hd.replace('%b', month).replace('%B', month)

        return hd

    def hijri_previous(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        #
        # Days and weeks are the same, so we just use the regular
        # function for them
        #
        res = self.previous(days, weeks)

        #
        # Months, quarters and years, have different durations,
        # so let’s see
        #
        if not months:
            months = SezimalInteger(0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if not months:
            return res

        #
        # We have a number of months that we have to
        # go back in the calendar
        #
        hy, hm, hd = res.hijri_date().split('-')
        hy = int(hy)
        hm = int(hm)
        hd = int(hd)

        hm -= int(months)

        #
        # Since all years have 12 months, we
        # go back 1 year for every 12 months we need
        # to go back in the calendar
        #
        while hm <= 0:
            hy -= 1
            hm += 12

        #
        # Finally, let’s see if the day, 29, 30, 31,
        # exists for that particular month we landed
        #
        if hijri_month_length(hy, hm) < hd:
            hd = hijri_month_length(hy, hm)

        gregorian_date = hijri_to_gregorian(hy, hm, hd)
        ordinal_date = gregorian_year_month_day_to_ordinal_date(*gregorian_date)

        return SezimalDate.from_ordinal_date(ordinal_date)

    def hijri_next(self,
        days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        quarters: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        #
        # Days and weeks are the same, so we just use the regular
        # function for them
        #
        res = self.next(days, weeks)

        #
        # Months, quarters and years, have different durations,
        # so let’s see
        #
        if not months:
            months = SezimalInteger(0)

        if quarters:
            months += quarters * SezimalInteger(3)

        if years:
            months += years * SezimalInteger(20)

        if not months:
            return res

        #
        # We have a number of months that we have to
        # go back in the calendar
        #
        hy, hm, hd = res.hijri_date().split('-')
        hy = int(hy)
        hm = int(hm)
        hd = int(hd)

        hm += int(months)

        #
        # Since all years have 12 months, we
        # advance 1 year for every 12 months we need
        # to go further in the calendar
        #
        while hm > 12:
            hy += 1
            hm -= 12

        #
        # Finally, let’s see if the day 30
        # exists for that particular month we landed
        #
        if hijri_month_length(hy, hm) < hd:
            hd = hijri_month_length(hy, hm)

        gregorian_date = hijri_to_gregorian(hy, hm, hd)
        ordinal_date = gregorian_year_month_day_to_ordinal_date(*gregorian_date)

        return SezimalDate.from_ordinal_date(ordinal_date)

    @property
    def list_weeks_in_month(self) -> [SezimalInteger]:
        if self.month == 1:
            return [
                SezimalInteger(1),
                SezimalInteger(2),
                SezimalInteger(3),
                SezimalInteger(4),
            ]
        elif self.month == 2:
            return [
                SezimalInteger(5),
                SezimalInteger(10),
                SezimalInteger(11),
                SezimalInteger(12),
                SezimalInteger(13),
            ]
        elif self.month == 3:
            return [
                SezimalInteger(14),
                SezimalInteger(15),
                SezimalInteger(20),
                SezimalInteger(21),
            ]
        elif self.month == 4:
            return [
                SezimalInteger(22),
                SezimalInteger(23),
                SezimalInteger(24),
                SezimalInteger(25),
            ]
        elif self.month == 5:
            return [
                SezimalInteger(30),
                SezimalInteger(31),
                SezimalInteger(32),
                SezimalInteger(33),
                SezimalInteger(34),
            ]
        elif self.month == 10:
            return [
                SezimalInteger(35),
                SezimalInteger(40),
                SezimalInteger(41),
                SezimalInteger(42),
            ]
        elif self.month == 11:
            return [
                SezimalInteger(43),
                SezimalInteger(44),
                SezimalInteger(45),
                SezimalInteger(50),
            ]
        elif self.month == 12:
            return [
                SezimalInteger(51),
                SezimalInteger(52),
                SezimalInteger(53),
                SezimalInteger(54),
                SezimalInteger(55),
            ]
        elif self.month == 13:
            return [
                SezimalInteger(100),
                SezimalInteger(101),
                SezimalInteger(102),
                SezimalInteger(103),
            ]
        elif self.month == 14:
            return [
                SezimalInteger(104),
                SezimalInteger(105),
                SezimalInteger(110),
                SezimalInteger(111),
            ]
        elif self.month == 15:
            return [
                SezimalInteger(112),
                SezimalInteger(113),
                SezimalInteger(114),
                SezimalInteger(115),
                SezimalInteger(120),
            ]
        elif self.month == 20:
            if self.is_leap:
                return [
                    SezimalInteger(121),
                    SezimalInteger(122),
                    SezimalInteger(123),
                    SezimalInteger(124),
                    SezimalInteger(125),
                ]
            else:
                return [
                    SezimalInteger(121),
                    SezimalInteger(122),
                    SezimalInteger(123),
                    SezimalInteger(124),
                ]


SezimalDate.min = SezimalDate(1, 1, 1)
SezimalDate.max = SezimalDate(MAXYEAR, 20, 44)
SezimalDate.resolution = _datetime.timedelta(days=1)
