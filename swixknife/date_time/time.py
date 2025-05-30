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

__all__ = ('SezimalDate', 'tz_agrimas_offset', 'system_time_zone')

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalTime')

import datetime as _datetime
from zoneinfo import ZoneInfo

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..dozenal import Dozenal, DozenalInteger
from ..units import sezimal_to_decimal_unit
from ..base import sezimal_format, sezimal_to_niftimal, default_to_sezimal_digits, \
    default_niftimal_to_sezimal_digits, default_niftimal_to_regularized_digits, \
    default_niftimal_to_niftimal_digits, \
    sezimal_to_dozenal, niftimal_to_sezimal, dozenal_to_sezimal, \
    decimal_to_sezimal
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from .sezimal_functions import *
from .format_tokens import TIME_NUMBER_FORMAT_TOKENS, \
    TIME_ZONE_OFFSET_FORMAT_TOKENS, ISO_TIME_NUMBER_FORMAT_TOKENS, \
    DAY_FRACTION_FORMAT_TOKEN


class SezimalTime:
    __slots__ = '_uta', '_posha', '_agrima', '_anuga', '_boda', '_shaditiboda', '_day', '_time_zone', '_total_agrimas', '_iso_time', '_time_zone_offset', '_dst_offset'

    def __new__(
        cls,
        uta: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.time | _datetime.datetime = 0,
        posha: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        agrima: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        anuga: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        boda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        shaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        time_zone: str | ZoneInfo = None,
        base_gregorian_date: str | _datetime.datetime | _datetime.date = None,
    ) -> Self:
        if type(uta) == str:
            if VALID_TIME_STRING.match(uta):
                uta, posha, agrima = uta.split(':')
            elif VALID_PARTIAL_TIME_STRING.match(uta):
                uta, posha = uta.split(':')

        elif type(uta) in (_datetime.time, _datetime.datetime):
            seconds = Decimal(str(uta.hour)) * 60 * 60
            seconds += Decimal(str(uta.minute)) * 60
            seconds += Decimal(str(uta.second))
            seconds += Decimal(str(uta.microsecond)) / 1_000_000
            days = seconds / 86400
            time_zone = time_zone or uta.tzinfo
            return cls.from_days(days, time_zone)

        day = Sezimal(day)
        uta = Sezimal(uta)
        posha = Sezimal(posha)
        agrima = Sezimal(agrima)
        anuga = Sezimal(anuga)
        boda = Sezimal(boda)
        shaditiboda = Sezimal(shaditiboda)

        total_agrimas = day * 1_000_000
        total_agrimas += uta * 10_000
        total_agrimas += posha * 100
        total_agrimas += agrima
        total_agrimas += anuga / 100
        total_agrimas += boda / 10_000
        total_agrimas += (shaditiboda / 100_000_000) / 10_000

        self = object.__new__(cls)

        self._day = SezimalInteger(0)

        while total_agrimas >= 1_000_000:
            self._day += 1
            total_agrimas -= 1_000_000

        while total_agrimas < 0:
            total_agrimas += 1_000_000
            self._day -= 1

        self._uta = SezimalInteger(total_agrimas // 10_000)
        total_agrimas -= self._uta * 10_000

        self._posha = SezimalInteger(total_agrimas // 100)
        total_agrimas -= self._posha * 100

        self._agrima = SezimalInteger(total_agrimas)
        total_agrimas -= SezimalInteger(total_agrimas)

        total_agrimas *= 100
        self._anuga = SezimalInteger(total_agrimas)
        total_agrimas -= self._anuga

        total_agrimas *= 100
        self._boda = SezimalInteger(total_agrimas)
        total_agrimas -= self._boda

        total_agrimas *= 100_000_000
        self._shaditiboda = round(Sezimal(total_agrimas), 0)

        total_agrimas = self._day * 1_000_000
        total_agrimas += self._uta * 10_000
        total_agrimas += self._posha * 100
        total_agrimas += self._agrima
        total_agrimas += self._anuga / 100
        total_agrimas += self._boda / 10_000
        total_agrimas += (self._shaditiboda / 100_000_000) / 10_000

        self._total_agrimas = total_agrimas

        if not time_zone:
            time_zone = system_time_zone()
        elif type(time_zone) == ZoneInfo:
            time_zone = str(time_zone)

        self._time_zone = time_zone
        self._time_zone_offset, self._dst_offset = tz_agrimas_offset(time_zone, base_gregorian_date)

        total_seconds = total_agrimas - (self._day * 1_000_000)

        total_seconds = total_seconds.decimal * sezimal_to_decimal_unit(1, 'agm', 's').decimal

        hour = int(total_seconds // 60 // 60)
        total_seconds -= hour * 60 * 60

        minute = int(total_seconds // 60)
        total_seconds -= minute * 60

        second = int(total_seconds)
        total_seconds -= second

        microssecond = int(total_seconds * 1_000_000)

        iso_time = _datetime.time(hour, minute, second, microssecond, tzinfo=ZoneInfo(time_zone))

        self._iso_time = iso_time

        return self

    @property
    def day(self) -> SezimalInteger:
        return self._day

    @property
    def uta(self) -> SezimalInteger:
        return self._uta

    @property
    def posha(self) -> SezimalInteger:
        return self._posha

    @property
    def agrima(self) -> SezimalInteger:
        return self._agrima

    @property
    def anuga(self) -> SezimalInteger:
        return self._anuga

    @property
    def boda(self) -> SezimalInteger:
        return self._boda

    @property
    def shaditiboda(self) -> Sezimal:
        return self._shaditiboda

    @property
    def time_zone(self) -> str:
        return self._time_zone

    @property
    def is_dst(self) -> bool:
        return self._dst_offset != 0

    @property
    def iso_time(self):
        return self._iso_time

    @property
    def iso_hour(self) -> int:
        return self._iso_time.hour

    @property
    def iso_minute(self) -> int:
        return self._iso_time.minute

    @property
    def iso_second(self) -> int:
        return self._iso_time.second

    @property
    def iso_microsecond(self) -> int:
        return self._iso_time.microsecond

    @property
    def as_agrimas(self) -> Sezimal:
        return self._total_agrimas

    @property
    def as_seconds(self) -> Decimal:
        seconds = sezimal_to_decimal_unit(self.as_agrimas, 'agm', 's')
        return seconds.decimal

    def __repr__(self) -> str:
        return f"SezimalTime(uta={self.uta}, posha={self.posha}, agrima={self.agrima}, anuga={self.anuga}, boda={self.boda}, shaditiboda={self.shaditiboda}, day={self.day}, time_zone={self.time_zone}) - {self.iso_time.__repr__()}"

    def __str__(self) -> str:
        res = self.format(f'#*d #u:#p:#a.#n#b#x #t #V')
        return res.strip()

    @classmethod
    def now(cls, time_zone: str = None) -> Self:
        if not time_zone:
            time_zone = system_time_zone()

        t = _datetime.datetime.now(ZoneInfo(time_zone))

        return cls(t, time_zone=time_zone)

    def at_time_zone(self, time_zone: str = 'UTC') -> Self:
        if not time_zone:
            time_zone = 'UTC'

        if self.time_zone == time_zone:
            return self

        utc_agrimas = self.as_agrimas - self._time_zone_offset # - self._dst_offset
        tz_offset, dst_offset = tz_agrimas_offset(time_zone)
        tz_agrimas = utc_agrimas + tz_offset # + dst_offset

        return SezimalTime(agrima=tz_agrimas, time_zone=time_zone)

    def _apply_number_format(self, token: str, value_name: str, size: int | SezimalInteger = None, locale: SezimalLocale = None, from_decimal: bool = False) -> str:
        value = getattr(self, value_name, 0)

        if from_decimal:
            value = Decimal(str(value))

        if '*' in token and (not value):
            return ''

        if '99' in token:
            decimal_time = self.decimal_time

            if token in ('#99u', '#99?u'):
                value = decimal_time[0]
            elif token in ('#99p', '#99?p'):
                value = decimal_time[1]
            elif token in ('#99a', '#99?a'):
                value = decimal_time[2]

            if size and '-' not in token:
                value = value.zfill(int(SezimalInteger(size)))

            if '?' in token:
                value = locale.digit_replace(value)

        elif '↋↋' in token:
            dozenal_time = self.dozenal_time

            if token in ('#↋↋u', '#↋↋?u'):
                value = dozenal_time[0]
            elif token in ('#↋↋p', '#↋↋?p'):
                value = dozenal_time[1]
            elif token in ('#↋↋a', '#↋↋?a'):
                value = dozenal_time[2]

            if size and '-' not in token:
                value = value.zfill(int(SezimalInteger(size)))

            if '?' in token:
                value = locale.digit_replace(value)

        elif '@' in token or 'Z' in token:
            if from_decimal:
                value = SezimalInteger(value)

            value = str(value)

            if size and '-' not in token:
                value = value.zfill(int(SezimalInteger(size)))

            value = sezimal_to_niftimal(value)

            if '!' in token:
                value = default_niftimal_to_niftimal_digits(value)
            elif '@' in token:
                value = default_niftimal_to_regularized_digits(value)

        else:
            if '5' in token:
                value = str(SezimalInteger(value))
            elif '9' in token:
                value = str(int(value.decimal))
            elif '↋' in token:
                value = str(DozenalInteger(value))
            else:
                value = str(value)

            if size and '-' not in token:
                value = value.zfill(int(SezimalInteger(size)))

            if '!' in token:
                value = default_to_sezimal_digits(value)

            elif '?' in token:
                value = locale.digit_replace(value)

        if locale and locale.RTL:
            value = '\N{LRI}' + value + '\N{PDI}'

        return value

    def format(self, fmt: str = None, locale: str | SezimalLocale = None, skip_strftime: bool = False) -> str:
        if not fmt:
            return fmt

        fmt = fmt.replace('##', '__HASHTAG__')

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
            fmt = locale.TIME_FORMAT

        #
        # Locale’s time separator
        #
        if '#:' in fmt:
            if locale:
                fmt = fmt.replace('#:', locale.TIME_SEPARATOR)
            else:
                fmt = fmt.replace('#:', ':')

        for regex, token, base, zero, character, value_name, \
            size, size_niftimal, size_decimal in TIME_NUMBER_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            if base in ['@', '@!', 'Z']:
                value = self._apply_number_format(token, value_name, size_niftimal, locale)
            elif base in ['9', '9?', '↋', '↋?', '99', '↋↋', '99?', '↋↋?']:
                value = self._apply_number_format(token, value_name, size_decimal, locale)
            else:
                value = self._apply_number_format(token, value_name, size, locale)

            if locale and locale.RTL:
                value = '\N{LRI}' + value + '\N{PDI}'

            fmt = regex.sub(value, fmt)

        for regex, token, base, colon in TIME_ZONE_OFFSET_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            if self._time_zone_offset == 0:
                sign = '+'
                uta = '00'
                posha = '00'
                agrima = '00'

            else:
                if self._time_zone_offset > 0:
                    sign = '+'
                else:
                    sign = '−'

                uta = str(SezimalInteger(abs(self._time_zone_offset / 100))).zfill(4)[0:2]
                posha = str(SezimalInteger(abs(self._time_zone_offset / 100))).zfill(4)[2:4]
                agrima = str(SezimalInteger(round(self._time_zone_offset, 0))).zfill(6)[4:6]

            if '@' in base or 'Z' in base:
                uta = locale.format_niftimal_number(
                    SezimalInteger(uta),
                    niftimal_places=0,
                    sezimal_digits='!' in base,
                    regularized_digits='@' in base,
                )
                posha = locale.format_niftimal_number(
                    SezimalInteger(posha),
                    niftimal_places=0,
                    sezimal_digits='!' in base,
                    regularized_digits='@' in base,
                )
                agrima = locale.format_niftimal_number(
                    SezimalInteger(agrima),
                    niftimal_places=0,
                    sezimal_digits='!' in base,
                    regularized_digits='@' in base,
                )

            elif '9' in base and '99' not in base:
                uta = locale.format_decimal_number(
                    SezimalInteger(uta),
                    decimal_places=0,
                ).zfill(2)
                posha = locale.format_decimal_number(
                    SezimalInteger(posha),
                    decimal_places=0,
                ).zfill(2)
                agrima = locale.format_decimal_number(
                    SezimalInteger(agrima),
                    decimal_places=0,
                ).zfill(2)

            elif '↋' in base and '↋↋' not in base:
                uta = locale.format_dozenal_number(
                    SezimalInteger(uta),
                    dozenal_places=0,
                ).zfill(2)
                posha = locale.format_dozenal_number(
                    SezimalInteger(posha),
                    dozenal_places=0,
                ).zfill(2)
                agrima = locale.format_dozenal_number(
                    SezimalInteger(agrima),
                    dozenal_places=0,
                ).zfill(2)

            elif '99' in base:
                decimal_time = str(Sezimal(f'0.{uta}{posha}').decimal).split('.')[1][0:6]
                uta = decimal_time[0:2]
                posha = decimal_time[2:4]
                agrima = decimal_time[4:6]

            elif '↋↋' in base:
                dozenal_time = locale.format_dozenal_number(
                    Sezimal(f'0.{uta}{posha}'),
                    dozenal_places=10,
                    use_fraction_group_separator=False,
                ).split(locale.SEZIMAL_SEPARATOR)[1]
                uta = dozenal_time[0:2]
                posha = dozenal_time[2:4]
                agrima = dozenal_time[4:6]

            text = f'{sign}{uta}{colon}{posha}'

            if agrima != '00':
                text += f'{colon}{agrima}'

            if '!' in token:
                text = default_to_sezimal_digits(text)

            elif '?' in token:
                text = locale.digit_replace(text)

            if locale and locale.RTL:
                text = '\N{LRI}' + text + '\N{PDI}'

            fmt = regex.sub(text, fmt)

        if '#T' in fmt:
            fmt = fmt.replace('#T', self.time_zone)

        if '#&V' in fmt:
            fmt = fmt.replace('#&V', locale.DST_NAME if self.is_dst else '')

        if '#&-V' in fmt:
            fmt = fmt.replace('#&-V', ' ' + locale.DST_NAME if self.is_dst else '')

        if '#V' in fmt:
            fmt = fmt.replace('#V', locale.DST_SHORT_NAME if self.is_dst else '')

        if '#-V' in fmt:
            fmt = fmt.replace('#-V', ' ' + locale.DST_SHORT_NAME if self.is_dst else '')

        if '#@V' in fmt:
            fmt = fmt.replace('#@V', locale.DST_EMOJI if self.is_dst else '')

        if '#@-V' in fmt:
            fmt = fmt.replace('#@-V', ' ' + locale.DST_EMOJI if self.is_dst else '')

        for base, integer, fraction in DAY_FRACTION_FORMAT_TOKEN.findall(fmt):
            regex = re.compile(fr'#{base}{integer}\.{fraction}fD')

            as_days = self.as_days

            while as_days < 0:
                as_days += 1

            while as_days >= 1:
                as_days -= 1

            if base in ['@', '@!', 'Z', 'Z?']:
                integer = SezimalInteger(niftimal_to_sezimal(integer))
                fraction = SezimalInteger(niftimal_to_sezimal(fraction))

                text = locale.format_niftimal_number(
                    as_days * (SezimalInteger('100') ** integer),
                    niftimal_places=fraction,
                    sezimal_digits='!' in base,
                    sezimal_punctuation='!' in base,
                    regularized_digits='@' in base,
                )

            elif base in ['9', '9?']:
                integer = SezimalInteger(decimal_to_sezimal(integer))
                fraction = SezimalInteger(decimal_to_sezimal(fraction))

                as_days *= SezimalInteger('14') ** integer
                as_days = round(as_days.decimal, int(fraction))

                text = locale.format_decimal_number(
                    as_days,
                    decimal_places=fraction,
                    native_digits='?' in base
                )

            elif base in ['↋', '↋?']:
                integer = SezimalInteger(dozenal_to_sezimal(integer))
                fraction = SezimalInteger(dozenal_to_sezimal(fraction))

                as_days *= SezimalInteger('20') ** integer
                as_days = round(Dozenal(as_days), int(fraction))

                text = locale.format_dozenal_number(
                    as_days,
                    dozenal_places=fraction,
                    native_digits='?' in base
                )

            else:
                integer = SezimalInteger(integer)
                fraction = SezimalInteger(fraction)

                as_days *= SezimalInteger('10') ** integer
                as_days = round(as_days, int(fraction))

                text = locale.format_number(
                    as_days,
                    sezimal_places=fraction,
                    sezimal_digits='!' in base,
                    sezimal_punctuation='!' in base,
                    native_digits='?' in base
                )

            fmt = regex.sub(text, fmt)

        fmt = fmt.replace('__HASHTAG__', '#')

        #
        # Some very basic formatting for ISO time
        #
        if '%' in fmt:
            fmt = fmt.replace('%%', '___PERCENT___')

            for regex, token, base, zero, character, value_name, \
                size_decimal, size_niftimal, size_sezimal in ISO_TIME_NUMBER_FORMAT_TOKENS:
                if not regex.findall(fmt):
                    continue

                if base in ['@', '@!', 'Z']:
                    value = self._apply_number_format(token, value_name, size_niftimal, locale, from_decimal=True)
                elif base in ['', '?', '↋', '↋?']:
                    value = self._apply_number_format(token, value_name, size_decimal, locale, from_decimal=True)
                else:
                    value = self._apply_number_format(token, value_name, size_sezimal, locale, from_decimal=True)

                if locale and locale.RTL:
                    value = '\N{LRI}' + value + '\N{PDI}'

                fmt = regex.sub(value, fmt)

            if '%z' in fmt or '%5z':
                if self._time_zone_offset == 0:
                    if locale and locale.RTL:
                        fmt = fmt.replace('%z', '\N{LRI}+0000\N{PDI}')
                        fmt = fmt.replace('%5z', '\N{LRI}+0000\N{PDI}')
                    else:
                        fmt = fmt.replace('%z', '+0000')
                        fmt = fmt.replace('%5z', '+0000')
                else:
                    if self._time_zone_offset > 0:
                        text = '+'
                    else:
                        text = '−'

                    tzo = SezimalInteger(abs(self._time_zone_offset / 100))
                    tzo /= 100
                    tzo = sezimal_to_decimal_unit(tzo, 'uta', 'h')
                    tzo_hour = int(tzo.decimal)
                    tzo_minute = int((tzo.decimal - tzo_hour) * 60)

                    if '%5z' in fmt:
                        text += str(SezimalInteger(Decimal(tzo_hour))).zfill(2) + str(SezimalInteger(Decimal(tzo_minute))).zfill(3)

                        if locale and locale.RTL:
                            text = '\N{LRI}' + text + '\N{PDI}'

                        fmt = fmt.replace('%5z', text)
                    else:
                        text += str(tzo_hour).zfill(2) + str(tzo_minute).zfill(2)

                        if locale and locale.RTL:
                            text = '\N{LRI}' + text + '\N{PDI}'

                        fmt = fmt.replace('%z', text)

            if '%:z' in fmt or '%:5z' in fmt:
                if self._time_zone_offset == 0:
                    if locale and locale.RTL:
                        fmt = fmt.replace('%:z', '\N{LRI}+00:00\N{PDI}')
                        fmt = fmt.replace('%:5z', '\N{LRI}+00:00\N{PDI}')
                    else:
                        fmt = fmt.replace('%:z', '+00:00')
                        fmt = fmt.replace('%:5z', '+00:00')
                else:
                    if self._time_zone_offset > 0:
                        text = '+'
                    else:
                        text = '−'

                    tzo = SezimalInteger(abs(self._time_zone_offset / 100))
                    tzo /= 100
                    tzo = sezimal_to_decimal_unit(tzo, 'uta', 'h')
                    tzo_hour = int(tzo.decimal)
                    tzo_minute = int((tzo.decimal - tzo_hour) * 60)

                    if '%:5z' in fmt:
                        text += str(SezimalInteger(Decimal(tzo_hour))).zfill(2) + ':' + str(SezimalInteger(Decimal(tzo_minute))).zfill(3)

                        if locale and locale.RTL:
                            text = '\N{LRI}' + text + '\N{PDI}'

                        fmt = fmt.replace('%:5z', text)
                    else:
                        text += str(tzo_hour).zfill(2) + ':' + str(tzo_minute).zfill(2)

                        if locale and locale.RTL:
                            text = '\N{LRI}' + text + '\N{PDI}'

                        fmt = fmt.replace('%:z', text)

            if '%Z' in fmt:
                fmt = fmt.replace('%Z', self.time_zone)

            if '%P' in fmt:
                if self.uta < 30:
                    fmt = fmt.replace('%P', locale.lower(locale.AM))
                else:
                    fmt = fmt.replace('%P', locale.lower(locale.PM))

            if '%p' in fmt:
                if self.uta < 30:
                    fmt = fmt.replace('%p', locale.upper(locale.AM))
                else:
                    fmt = fmt.replace('%p', locale.upper(locale.PM))

            fmt = fmt.replace('___PERCENT___', '%')

        if skip_strftime:
            return fmt

        return self.iso_time.strftime(fmt)

    def strftime(self, fmt: str) -> str:
        return self.format(fmt)

    @property
    def julian_day(self) -> Sezimal:
        total_agrimas = self.as_agrimas

        if self.time_zone:
            tz_offset, dst_offset = tz_agrimas_offset(self.time_zone)
            total_agrimas -= tz_offset # + dst_offset

        jd = total_agrimas / 1_000_000

        return jd

    @property
    def mars_sol(self) -> Sezimal:
        return mars_sol(self.julian_day)

    @property
    def as_days(self) -> Sezimal:
        return self.as_agrimas / 1_000_000

    @classmethod
    def from_days(cls, days: Sezimal, time_zone: str | ZoneInfo = None) -> Self:
        days = abs(days)
        agrimas = Sezimal(days) * 1_000_000
        return cls(agrima=agrimas, time_zone=time_zone)

    def replace(self,
        uta: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        posha: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        agrima: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        anuga: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        boda: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        shaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        time_zone: str | ZoneInfo = None,
    ) -> Self:
        if uta is None:
            uta = self._uta

        if posha is None:
            posha = self._posha

        if agrima is None:
            agrima = self._agrima

        if anuga is None:
            anuga = self._anuga

        if boda is None:
            boda = self._boda

        if shaditiboda is None:
            shaditiboda = self._shaditiboda

        if day is None:
            day = self._day

        if time_zone is None:
            time_zone = self._time_zone

        return type(self)(uta, posha, agrima, anuga, boda, shaditiboda, day, time_zone)

    @property
    def dozenal_time(self) -> tuple[str, str, str]:
        dt = sezimal_to_dozenal(self.as_days.decimal).split('.')[1][:6]

        if len(dt) < 6:
            dt = dt.ljust(6, '0')

        dozenal_uta = dt[0:2]
        dozenal_posha = dt[2:4]
        dozenal_agrima = dt[4:6]

        return dozenal_uta, dozenal_posha, dozenal_agrima

    @property
    def decimal_time(self) -> tuple[str, str, str]:
        dt = str(self.as_days.decimal).split('.')[1][:6]

        if len(dt) < 6:
            dt = dt.ljust(6, '0')

        decimal_uta = dt[0:2]
        decimal_posha = dt[2:4]
        decimal_agrima = dt[4:6]

        return decimal_uta, decimal_posha, decimal_agrima
