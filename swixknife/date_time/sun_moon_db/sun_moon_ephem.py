

__all__ = ('SezimalSun', 'SezimalMoon')

from tqdm import tqdm

from zoneinfo import ZoneInfo
from decimal import Decimal

from swixknife import Sezimal, SezimalInteger, SezimalRange, SezimalLocale, \
    SezimalDate, SezimalTime, SezimalDateTime
from swixknife.date_time.sezimal_functions import system_time_zone

import datetime as _datetime


from ephem import (
    next_spring_equinox, next_summer_solstice, next_autumn_equinox, next_winter_solstice,
    previous_spring_equinox, previous_summer_solstice, previous_autumn_equinox, previous_winter_solstice,
    next_new_moon, next_first_quarter_moon, next_full_moon, next_last_quarter_moon,
    previous_new_moon, previous_first_quarter_moon, previous_full_moon, previous_last_quarter_moon
)

import sqlite3


def _ephem_date_to_date(ed, time_zone) -> SezimalDateTime:
    #
    # Ephem dates are floats, the amount of time
    # passed since:
    # 13_1031-20-44 30:00:00 UTC
    # ISO 1899-12-31 12:00:00 UTC
    # Ordinal date is 2251_1031.3 693_595.5_dec
    #
    od = Sezimal('2251_1031.3').decimal + Decimal(str(float(ed)))
    date = SezimalDate.from_ordinal_date(Decimal(int(od)))

    od -= int(od)
    od *= Sezimal('100_0000').decimal

    time = SezimalTime(agrima=od, time_zone='UTC')

    return SezimalDateTime.combine(date, time).at_time_zone(time_zone)


def _middle_date_time(first_date, second_date, time_zone) -> SezimalDateTime:
    cross_quarter = first_date.at_time_zone('UTC').as_days.decimal
    cross_quarter += (second_date.at_time_zone('UTC').as_days.decimal - first_date.at_time_zone('UTC').as_days.decimal) / 2
    return SezimalDateTime.from_days(cross_quarter, time_zone='UTC').at_time_zone(time_zone)


class SezimalSun:
    def __new__(cls, year: int | SezimalInteger, time_zone: str | ZoneInfo = None):
        date = SezimalDate(year, 1, 1)

        self = object.__new__(cls)

        time_zone = time_zone or system_time_zone()

        self._year = year
        self._time_zone = str(time_zone)

        #
        # Equinoxes and Solstices
        #
        self._previous_december_solstice = _ephem_date_to_date(previous_winter_solstice(date.gregorian_isoformat), time_zone)
        self._march_equinox = _ephem_date_to_date(next_spring_equinox(date.gregorian_isoformat), time_zone)
        self._june_solstice = _ephem_date_to_date(next_summer_solstice(date.gregorian_isoformat), time_zone)
        self._september_equinox = _ephem_date_to_date(next_autumn_equinox(date.gregorian_isoformat), time_zone)
        self._december_solstice = _ephem_date_to_date(next_winter_solstice(date.gregorian_isoformat), time_zone)

        #
        # Cross-quarters
        #
        self._february_cross_quarter = _middle_date_time(self._previous_december_solstice, self._march_equinox, time_zone)
        self._may_cross_quarter = _middle_date_time(self._march_equinox, self._june_solstice, time_zone)
        self._august_cross_quarter = _middle_date_time(self._june_solstice, self._september_equinox, time_zone)
        self._november_cross_quarter = _middle_date_time(self._september_equinox, self._december_solstice, time_zone)

        return self

    def __repr__(self) -> str:
        return f"SezimalSun(year={self.year}, time_zone='{self.time_zone}')"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def year(self) -> SezimalInteger:
        return self._year

    @property
    def time_zone(self) -> str:
        return self._time_zone

    @property
    def february_cross_quarter(self) -> SezimalDateTime:
        return self._february_cross_quarter

    @property
    def march_equinox(self) -> SezimalDateTime:
        return self._march_equinox

    @property
    def may_cross_quarter(self) -> SezimalDateTime:
        return self._may_cross_quarter

    @property
    def june_solstice(self) -> SezimalDateTime:
        return self._june_solstice

    @property
    def august_cross_quarter(self) -> SezimalDateTime:
        return self._august_cross_quarter

    @property
    def september_equinox(self) -> SezimalDateTime:
        return self._september_equinox

    @property
    def november_cross_quarter(self) -> SezimalDateTime:
        return self._november_cross_quarter

    @property
    def december_solstice(self) -> SezimalDateTime:
        return self._december_solstice


MOONS = {}


def calculate_moon_phases(year_start: int | SezimalInteger, year_finish: int | SezimalInteger, time_zone: str | ZoneInfo = None):
    date = SezimalDate(year_start, 1, 1)

    time_zone = time_zone or system_time_zone()

    year = str(date.gregorian_year)

    #
    # All moon phases for the year
    #
    previous_new = previous_new_moon(year)
    previous_first_quarter = next_first_quarter_moon(previous_new)
    previous_full = next_full_moon(previous_first_quarter)
    previous_third_quarter = next_last_quarter_moon(previous_full)

    previous_new = _ephem_date_to_date(previous_new, time_zone)

    if previous_new.ordinal_date not in MOONS:
        MOONS[previous_new.ordinal_date] = [previous_new, 'new']

    previous_first_quarter = _ephem_date_to_date(previous_first_quarter, time_zone)

    if previous_first_quarter.ordinal_date not in MOONS:
        MOONS[previous_first_quarter.ordinal_date] = [previous_first_quarter, 'first quarter']

    previous_waxing_crescent = _middle_date_time(previous_new, previous_first_quarter, time_zone)

    if previous_waxing_crescent.ordinal_date not in MOONS:
        MOONS[previous_waxing_crescent.ordinal_date] = [previous_waxing_crescent, 'waxing crescent']

    previous_full = _ephem_date_to_date(previous_full, time_zone)

    if previous_full.ordinal_date not in MOONS:
        MOONS[previous_full.ordinal_date] = [previous_full, 'full']

    previous_waxing_gibbous = _middle_date_time(previous_first_quarter, previous_full, time_zone)

    if previous_waxing_gibbous.ordinal_date not in MOONS:
        MOONS[previous_waxing_gibbous.ordinal_date] = [previous_waxing_gibbous, 'waxing gibbous']

    previous_third_quarter = _ephem_date_to_date(previous_third_quarter, time_zone)

    if previous_third_quarter.ordinal_date not in MOONS:
        MOONS[previous_third_quarter.ordinal_date] = [previous_third_quarter, 'third quarter']

    previous_waning_gibbous = _middle_date_time(previous_full, previous_third_quarter, time_zone)

    if previous_waning_gibbous.ordinal_date not in MOONS:
        MOONS[previous_waning_gibbous.ordinal_date] = [previous_waning_gibbous, 'waning gibbous']

    print('Calculated moon', previous_third_quarter)

    while previous_third_quarter.year <= year_finish + 1:
        next_new = next_new_moon(year)
        next_first_quarter = next_first_quarter_moon(next_new)
        next_full = next_full_moon(next_first_quarter)
        next_third_quarter = next_last_quarter_moon(next_full)

        year = str(next_third_quarter)

        #
        # Now, convert everything to SezimalDateTime,
        # also, calculating the crescent and gibbous phases
        #
        next_new = _ephem_date_to_date(next_new, time_zone)

        if next_new.ordinal_date not in MOONS:
            MOONS[next_new.ordinal_date] = [next_new, 'new']

        previous_waning_crescent = _middle_date_time(previous_third_quarter, next_new, time_zone)

        if previous_waning_crescent.ordinal_date not in MOONS:
            MOONS[previous_waning_crescent.ordinal_date] = [previous_waning_crescent, 'waning crescent']

        next_first_quarter = _ephem_date_to_date(next_first_quarter, time_zone)

        if next_first_quarter.ordinal_date not in MOONS:
            MOONS[next_first_quarter.ordinal_date] = [next_first_quarter, 'first quarter']

        next_waxing_crescent = _middle_date_time(next_new, next_first_quarter, time_zone)

        if next_waxing_crescent.ordinal_date not in MOONS:
            MOONS[next_waxing_crescent.ordinal_date] = [next_waxing_crescent, 'waxing crescent']

        next_full = _ephem_date_to_date(next_full, time_zone)

        if next_full.ordinal_date not in MOONS:
            MOONS[next_full.ordinal_date] = [next_full, 'full']

        next_waxing_gibbous = _middle_date_time(next_first_quarter, next_full, time_zone)

        if next_waxing_gibbous.ordinal_date not in MOONS:
            MOONS[next_waxing_gibbous.ordinal_date] = [next_waxing_gibbous, 'waxing gibbous']

        next_third_quarter = _ephem_date_to_date(next_third_quarter, time_zone)

        if next_third_quarter.ordinal_date not in MOONS:
            MOONS[next_third_quarter.ordinal_date] = [next_third_quarter, 'third quarter']

        next_waning_gibbous = _middle_date_time(next_full, next_third_quarter, time_zone)

        if next_waning_gibbous.ordinal_date not in MOONS:
            MOONS[next_waning_gibbous.ordinal_date] = [next_waning_gibbous, 'waning gibbous']

        previous_third_quarter = next_third_quarter
        print('Calculated moon', previous_third_quarter, _datetime.datetime.now())


if __name__ == '__main__':
    connection = sqlite3.connect('./sun_moon.db')
    cursor = connection.cursor()
    cursor.execute('create table if not exists sun_moon(date text, sun_moon text, name text, date_time_as_days text);')
    cursor.execute('create unique index if not exists sun_moon_pk_index on sun_moon(date, sun_moon, name);')
    cursor.execute('create unique index if not exists sun_moon_desc_pk_index on sun_moon(date desc, sun_moon, name);')

    SPAN = SezimalInteger(300)
    MIN_YEAR = 13_1400 - SPAN
    MAX_YEAR = 13_1400 + SPAN

    #
    # Let’s precalculate the seasons and moon phases for the years
    # from 13_1100 (11_916_dec)
    #   to 13_2100 (12_132_dec)
    # both are 300 (108_dec) years (1/20 [1/12_dec] of a "millenium")
    # appart from 13_1400 (12_024_dec)
    #
    print('Pre-calculating and inserting seasons')
    for year in tqdm(list(SezimalRange(MIN_YEAR, MAX_YEAR + 1))):
        sun = SezimalSun(year, time_zone='UTC')

        for field in ('february_cross_quarter', 'march_equinox',
                      'may_cross_quarter', 'june_solstice',
                      'august_cross_quarter', 'september_equinox',
                      'november_cross_quarter', 'december_solstice'):

            date = getattr(sun, field)

            sql = f'''
insert or ignore into sun_moon (
    date,
    sun_moon,
    name,
    date_time_as_days
)
values (
    '{str(date.date)}',
    'sun',
    '{field}',
    '{str(date.as_days)}'
);
'''
            cursor.execute('begin transaction;')
            cursor.execute(sql)
            cursor.execute('commit transaction;')

    print('Pre-calculating moon phases')
    calculate_moon_phases(MIN_YEAR, MAX_YEAR, time_zone='UTC')

    print('Inserting moon phases')
    for od in tqdm(sorted(MOONS)):
        date, name = MOONS[od]

        if date.year < MIN_YEAR or date.year > MAX_YEAR:
            continue

        sql = f'''
insert or ignore into sun_moon (
    date,
    sun_moon,
    name,
    date_time_as_days
)
values (
    '{str(date.date)}',
    'moon',
    '{name}',
    '{str(date.as_days)}'
);
'''
        cursor.execute('begin transaction;')
        cursor.execute(sql)
        cursor.execute('commit transaction;')

    print('Done moon')

    connection.close()
