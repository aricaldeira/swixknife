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
from ..units.conversions import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA, UTA_TO_HOUR
from ..base import sezimal_format, sezimal_to_niftimal, default_to_dedicated_digits, \
    default_niftimal_to_dedicated_digits, default_niftimal_to_regularized_digits, \
    default_niftimal_to_regularized_dedicated_digits, \
    sezimal_to_dozenal
from ..text import sezimal_spellout
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from .sezimal_functions import *
from .format_tokens import TIME_NUMBER_FORMAT_TOKENS, \
    TIME_ZONE_OFFSET_FORMAT_TOKENS, ISO_TIME_NUMBER_FORMAT_TOKENS


class SezimalTime:
    __slots__ = '_uta', '_posha', '_agrima', '_anuga', '_boda', '_ekaditiboda', '_day', '_time_zone', '_total_agrimas', '_iso_time', '_time_zone_offset', '_dst_offset'

    def __new__(
        cls,
        uta: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.time = 0,
        posha: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        agrima: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        anuga: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        boda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        ekaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        time_zone: str | ZoneInfo = None,
        base_gregorian_date: str = None,
    ) -> Self:
        if type(uta) == str:
            if VALID_TIME_STRING.match(uta):
                uta, posha, agrima = uta.split(':')
            elif VALID_PARTIAL_TIME_STRING.match(uta):
                uta, posha = uta.split(':')

        elif type(uta) == _datetime.time:
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
        ekaditiboda = Sezimal(ekaditiboda)

        total_agrimas = day * 100_0000
        total_agrimas += uta * 1_0000
        total_agrimas += posha * 100
        total_agrimas += agrima
        total_agrimas += anuga / 100
        total_agrimas += boda / 1_0000
        total_agrimas += (ekaditiboda / 1_0000_0000) / 1_0000

        self = object.__new__(cls)

        self._day = SezimalInteger(total_agrimas // 100_0000)
        total_agrimas -= self._day * 100_0000

        self._uta = SezimalInteger(total_agrimas // 1_0000)
        total_agrimas -= self._uta * 1_0000

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

        total_agrimas *= 1_0000_0000
        self._ekaditiboda = round(Sezimal(total_agrimas), 0)

        total_agrimas = self._day * 100_0000
        total_agrimas += self._uta * 1_0000
        total_agrimas += self._posha * 100
        total_agrimas += self._agrima
        total_agrimas += self._anuga / 100
        total_agrimas += self._boda / 1_0000
        total_agrimas += (self._ekaditiboda / 1_0000_0000) / 1_0000

        self._total_agrimas = total_agrimas

        if not time_zone:
            time_zone = system_time_zone()
        elif type(time_zone) == ZoneInfo:
            time_zone = str(time_zone)

        self._time_zone = time_zone
        self._time_zone_offset, self._dst_offset = tz_agrimas_offset(time_zone, base_gregorian_date)

        total_seconds = self._total_agrimas
        total_seconds -= self._day * 100_0000
        total_seconds = total_seconds.decimal * AGRIMA_TO_SECOND.decimal

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
    def ekaditiboda(self) -> Sezimal:
        return self._ekaditiboda

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
        seconds = self.as_agrimas * AGRIMA_TO_SECOND
        return seconds.decimal

    def __repr__(self) -> str:
        return f"SezimalTime(uta={self.uta}, posha={self.posha}, agrima={self.agrima}, anuga={self.anuga}, boda={self.boda}, ekaditiboda={self.ekaditiboda}, day={self.day}, time_zone={self.time_zone}) - {self.iso_time.__repr__()}"

    def __str__(self) -> str:
        res = self.format(f'#*d #u:#p:#a.#n#b#e #t #V')
        return res.strip()

    @classmethod
    def now(cls, time_zone: str = None) -> Self:
        if not time_zone:
            time_zone = system_time_zone()

        traditional_utc_now = _datetime.datetime.now(ZoneInfo('UTC'))
        total_agrimas = date_time_to_agrima(traditional_utc_now)
        tz_offset, dst_offset = tz_agrimas_offset(time_zone)
        total_agrimas += tz_offset # + dst_offset

        #
        # Date has shifted?
        #
        if total_agrimas < 0:
            total_agrimas = total_agrimas + Sezimal('100_0000')

        return cls(agrima=total_agrimas, time_zone=time_zone)

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

            match token:
                case '#99u' | '#99?u':
                    value = decimal_time[0]
                case '#99p' | '#99?p':
                    value = decimal_time[1]
                case '#99a' | '#99?a':
                    value = decimal_time[2]

            if size and '-' not in token:
                value = value.zfill(int(SezimalInteger(size)))

            if '?' in token:
                value = locale.digit_replace(value)

        elif '↋↋' in token:
            dozenal_time = self.dozenal_time

            match token:
                case '#↋↋u' | '#↋↋?u':
                    value = dozenal_time[0]
                case '#↋↋p' | '#↋↋?p':
                    value = dozenal_time[1]
                case '#↋↋a' | '#↋↋?a':
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
                value = default_niftimal_to_regularized_dedicated_digits(value)
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
                value = default_to_dedicated_digits(value)

            elif '?' in token:
                value = locale.digit_replace(value)

        return value

    def format(self, fmt: str = None, locale: str | SezimalLocale = None, skip_strftime: bool = False) -> str:
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

            fmt = regex.sub(value, fmt)

        # for character, value, unit in [
        #     ['d', 'day', 'SH-day'],
        #     ['u', 'uta', 'SH-uta'],
        #     ['p', 'posha', 'SH-psh'],
        #     ['a', 'agrima', 'SH-agm'],
        #     ['n', 'anuga', 'SH-ang'],
        #     ['b', 'boda', 'SH-bda'],
        #     ['e', 'ekaditiboda', 'SH-edbda'],
        # ]:
        #     if f'#&{character}' in fmt:
        #         fmt = fmt.replace(f'#&{character}', sezimal_spellout(unit + ' ' + str(getattr(self, value, 0)), lang or 'en'))
        #
        #     if f'#&@{character}' in fmt:
        #         fmt = fmt.replace(f'#&@{character}', sezimal_spellout(str(getattr(self, value, 0)), lang or 'en'))

        for regex, token, base, colon in TIME_ZONE_OFFSET_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            if self._time_zone_offset == 0:
                sign = '+'
                uta = '00'
                posha = '00'
            else:
                if self._time_zone_offset > 0:
                    sign = '+'
                else:
                    sign = '−'

                uta = str(SezimalInteger(abs(self._time_zone_offset / 100))).zfill(4)[0:2]
                posha = str(SezimalInteger(abs(self._time_zone_offset / 100))).zfill(4)[2:4]

            if '@' in base or 'Z' in base:
                uta = locale.format_niftimal_number(
                    SezimalInteger(uta),
                    niftimal_places=0,
                    dedicated_digits='!' in base,
                    regularized_digits='@' in base,
                )
                posha = locale.format_niftimal_number(
                    SezimalInteger(posha),
                    niftimal_places=0,
                    dedicated_digits='!' in base,
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

            elif '↋' in base and '↋↋' not in base:
                uta = locale.format_dozenal_number(
                    SezimalInteger(uta),
                    dozenal_places=0,
                ).zfill(2)
                posha = locale.format_dozenal_number(
                    SezimalInteger(posha),
                    dozenal_places=0,
                ).zfill(2)

            elif '99' in base:
                decimal_time = str(Sezimal(f'0.{uta}{posha}').decimal).split('.')[1][0:6]
                uta = decimal_time[0:2]
                posha = decimal_time[2:4]
                agrima = decimal_time[4:6]

                if agrima != '00':
                    posha += colon + agrima

            elif '↋↋' in base:
                dozenal_time = locale.format_dozenal_number(
                    Sezimal(f'0.{uta}{posha}'),
                    dozenal_places=10,
                    use_fraction_group_separator=False,
                ).split(locale.SEZIMAL_SEPARATOR)[1]
                uta = dozenal_time[0:2]
                posha = dozenal_time[2:4]
                agrima = dozenal_time[4:6]

                if agrima != '00':
                    posha += colon + agrima

            text = f'{sign}{uta}{colon}{posha}'

            if '!' in token:
                text = default_to_dedicated_digits(text)

            elif '?' in token:
                text = locale.digit_replace(text)

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

        fmt = fmt.replace('__HASHTAG__', '#')

        #
        # Some very basic formatting for ISO time
        #
        if '%' in fmt:
            fmt = fmt.replace('%%', '__PERCENT__')

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

                fmt = regex.sub(value, fmt)

            # if '%H' in fmt:
            #     fmt = fmt.replace('%H', str(self.iso_hour).zfill(2))
            #
            # if '%-H' in fmt:
            #     fmt = fmt.replace('%-H', str(self.iso_hour))
            #
            # if '%M' in fmt:
            #     fmt = fmt.replace('%M', str(self.iso_minute).zfill(2))
            #
            # if '%-M' in fmt:
            #     fmt = fmt.replace('%-M', str(self.iso_minute))
            #
            # if '%S' in fmt:
            #     fmt = fmt.replace('%S', str(self.iso_second).zfill(2))
            #
            # if '%-S' in fmt:
            #     fmt = fmt.replace('%-S', str(self.iso_second))
            #
            # if '%?H' in fmt:
            #     fmt = fmt.replace('%?H', locale.digit_replace(str(self.iso_hour).zfill(2)))
            #
            # if '%?-H' in fmt:
            #     fmt = fmt.replace('%?-H', locale.digit_replace(str(self.iso_hour)))
            #
            # if '%?M' in fmt:
            #     fmt = fmt.replace('%?M', locale.digit_replace(str(self.iso_minute).zfill(2)))
            #
            # if '%?-M' in fmt:
            #     fmt = fmt.replace('%?-M', locale.digit_replace(str(self.iso_minute)))
            #
            # if '%?S' in fmt:
            #     fmt = fmt.replace('%?S', locale.digit_replace(str(self.iso_second).zfill(2)))
            #
            # if '%?-S' in fmt:
            #     fmt = fmt.replace('%?-S', locale.digit_replace(str(self.iso_second)))
            #
            # if '%f' in fmt:
            #     fmt = fmt.replace('%f', str(self.iso_microsecond).zfill(6))

            if '%z' in fmt:
                if self._time_zone_offset == 0:
                    fmt = fmt.replace('%z', '+0000')
                else:
                    if self._time_zone_offset > 0:
                        text = '+'
                    else:
                        text = '−'

                    tzo = SezimalInteger(abs(self._time_zone_offset / 100))
                    tzo /= 100
                    tzo *= UTA_TO_HOUR
                    tzo_hour = int(tzo.decimal)
                    tzo_minute = int((tzo.decimal - tzo_hour) * 60)
                    text += str(tzo_hour).zfill(2) + str(tzo_minute).zfill(2)

                    fmt = fmt.replace('%z', text)

            if '%:z' in fmt:
                if self._time_zone_offset == 0:
                    fmt = fmt.replace('%:z', '+00:00')
                else:
                    if self._time_zone_offset > 0:
                        text = '+'
                    else:
                        text = '−'

                    tzo = SezimalInteger(abs(self._time_zone_offset / 100))
                    tzo /= 100
                    tzo *= UTA_TO_HOUR
                    tzo_hour = int(tzo.decimal)
                    tzo_minute = int((tzo.decimal - tzo_hour) * 60)
                    text += str(tzo_hour).zfill(2) + ':' + str(tzo_minute).zfill(2)

                    fmt = fmt.replace('%:z', text)

            if '%Z' in fmt:
                fmt = fmt.replace('%Z', self.time_zone)

        if skip_strftime:
            return fmt

        return self.iso_time.strftime(fmt)

    def strftime(self, fmt: str) -> str:
        return self.format(fmt)

    @property
    def julian_date(self) -> Sezimal:
        total_agrimas = self.as_agrimas

        if self.time_zone:
            tz_offset, dst_offset = tz_agrimas_offset(self.time_zone)
            total_agrimas -= tz_offset # + dst_offset

        jd = total_agrimas / 100_0000

        return jd

    @property
    def mars_sol_date(self) -> Sezimal:
        return mars_sol_date(self.julian_date)

    @property
    def as_days(self) -> Sezimal:
        return self.as_agrimas / 100_0000

    @classmethod
    def from_days(cls, days: Sezimal, time_zone: str | ZoneInfo = None) -> Self:
        days = abs(days)
        agrimas = Sezimal(days) * 100_0000
        return cls(agrima=agrimas, time_zone=time_zone)

    def replace(self,
        uta: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        posha: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        agrima: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        anuga: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        boda: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        ekaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = None,
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

        if ekaditiboda is None:
            ekaditiboda = self._ekaditiboda

        if day is None:
            day = self._day

        if time_zone is None:
            time_zone = self._time_zone

        return type(self)(uta, posha, agrima, anuga, boda, ekaditiboda, day, time_zone)

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
