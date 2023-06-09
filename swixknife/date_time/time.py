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

__all__ = ('SezimalDate', 'TIME_SEPARATOR', 'tz_agrimas_offset', 'system_time_zone')

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalTime')

import datetime as _datetime
from zoneinfo import ZoneInfo

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..units.conversions import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA, UTA_TO_HOUR
from ..base import sezimal_format, sezimal_to_niftimal, default_to_dedicated_digits, \
    default_niftimal_to_dedicated_digits, default_niftimal_to_regularized_digits, \
    default_niftimal_to_regularized_dedicated_digits
from ..text import sezimal_spellout
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from .sezimal_functions import *


class SezimalTime:
    __slots__ = '_uta', '_posha', '_agrima', '_anuga', '_boda', '_ekaditiboda', '_day', '_time_zone', '_total_agrimas', '_iso_time', '_time_zone_offset', '_dst_offset'

    def __new__(
        cls,
        uta: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        posha: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        agrima: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        anuga: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        boda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        ekaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
        time_zone: str | ZoneInfo = None,
    ) -> Self:
        if type(uta) == str:
            if VALID_TIME_STRING.match(uta):
                uta, posha, agrima = uta.split(':')
            elif VALID_PARTIAL_TIME_STRING.match(uta):
                uta, posha = uta.split(':')

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

        self._time_zone = time_zone
        self._time_zone_offset, self._dst_offset = tz_agrimas_offset(time_zone)

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
        res = self.format(f'#*d #u{TIME_SEPARATOR}#p{TIME_SEPARATOR}#a.#n#b#e #t #V')
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

        utc_agrimas = self.as_agrimas - self._time_zone_offset # - self._dst_offset
        tz_offset, dst_offset = tz_agrimas_offset(time_zone)
        tz_agrimas = utc_agrimas + tz_offset # + dst_offset

        return SezimalTime(agrima=tz_agrimas, time_zone=time_zone)

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

        for character, value, size, size_niftimal, size_decimal in [
            ['d', 'day', 2, 1, 2],
            ['u', 'uta', 2, 1, 2],
            ['p', 'posha', 2, 1, 2],
            ['a', 'agrima', 2, 1, 2],
            ['n', 'anuga', 2, 1, 2],
            ['b', 'boda', 2, 1, 2],
            ['e', 'ekaditiboda', 12, 4, 7],
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

        for character, value, unit in [
            ['d', 'day', 'SH-day'],
            ['u', 'uta', 'SH-uta'],
            ['p', 'posha', 'SH-psh'],
            ['a', 'agrima', 'SH-agm'],
            ['b', 'boda', 'SH-bda'],
            ['n', 'anuga', 'SH-ang'],
            ['e', 'ekaditiboda', 'SH-edbda'],
        ]:
            if f'#&{character}' in fmt:
                fmt = fmt.replace(f'#&{character}', sezimal_spellout(unit + ' ' + str(getattr(self, value, 0)), lang or 'en'))
            elif f'#&@{character}' in fmt:
                fmt = fmt.replace(f'#&@{character}', sezimal_spellout(str(getattr(self, value, 0)), lang or 'en'))

        if '#t' in fmt:
            if self._time_zone_offset == 0:
                fmt = fmt.replace('#t', f'+00{TIME_SEPARATOR}00')
            else:
                if self._time_zone_offset > 0:
                    text = '+'
                else:
                    text = '−'

                text += sezimal_format(
                    abs(self._time_zone_offset / 100),
                    sezimal_places=0,
                    minimum_size=4,
                    group_separator=TIME_SEPARATOR,
                    subgroup_separator=TIME_SEPARATOR,
                )

                fmt = fmt.replace('#t', text)

        if '#T' in fmt:
            fmt = fmt.replace('#T', self.time_zone)

        if '#z' in fmt:
            if self._time_zone_offset == 0:
                fmt = fmt.replace('#z', '+0000')
            else:
                if self._time_zone_offset > 0:
                    text = '+'
                else:
                    text = '−'

                text += str(SezimalInteger(abs(self._time_zone_offset / 100))).zfill(4)

                fmt = fmt.replace('#z', text)

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

            if '%H' in fmt:
                fmt = fmt.replace('%H', str(self.iso_hour).zfill(2))

            if '%-H' in fmt:
                fmt = fmt.replace('%-H', str(self.iso_hour))

            if '%M' in fmt:
                fmt = fmt.replace('%M', str(self.iso_minute).zfill(2))

            if '%-M' in fmt:
                fmt = fmt.replace('%-M', str(self.iso_minute))

            if '%S' in fmt:
                fmt = fmt.replace('%S', str(self.iso_second).zfill(2))

            if '%-S' in fmt:
                fmt = fmt.replace('%-S', str(self.iso_second))

            if '%f' in fmt:
                fmt = fmt.replace('%f', str(self.iso_microsecond).zfill(6))

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

        return round(total_agrimas / 100_0000, 10)

    @property
    def as_days(self) -> Sezimal:
        return self.as_agrimas / 100_0000

    @classmethod
    def from_days(cls, days: Sezimal, time_zone: str | ZoneInfo = None) -> Self:
        agrimas = Sezimal(days) * 100_0000
        return cls(agrima=agrimas, time_zone=time_zone)
