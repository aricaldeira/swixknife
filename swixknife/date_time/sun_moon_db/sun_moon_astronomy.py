
__all__ = ('SezimalSun',)

from tqdm import tqdm

from zoneinfo import ZoneInfo
from decimal import Decimal

from swixknife import Sezimal, SezimalInteger, SezimalRange, SezimalLocale, \
    SezimalDate, SezimalTime, SezimalDateTime
from swixknife.date_time.sezimal_functions import system_time_zone

import datetime as _datetime


from astronomy import Seasons, SearchMoonQuarter, Time

import sqlite3


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

        previous_year_seasons = Seasons(date.gregorian_year - 1)
        this_year_seasons = Seasons(date.gregorian_year)
        # next_year_seasons = Seasons(date.gregorian_year + 1)

        self._previous_december_solstice = \
            SezimalDateTime(_datetime.datetime.fromisoformat(str(previous_year_seasons.dec_solstice)))
        self._march_equinox = \
            SezimalDateTime(_datetime.datetime.fromisoformat(str(this_year_seasons.mar_equinox)))
        self._june_solstice = \
            SezimalDateTime(_datetime.datetime.fromisoformat(str(this_year_seasons.jun_solstice)))
        self._september_equinox = \
            SezimalDateTime(_datetime.datetime.fromisoformat(str(this_year_seasons.sep_equinox)))
        self._december_solstice = \
            SezimalDateTime(_datetime.datetime.fromisoformat(str(this_year_seasons.dec_solstice)))

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

    #
    # Let’s find the New Moon first
    #
    time = Time(date.gregorian_isoformat + 'T00:00:00.000Z').AddDays(-29)
    moon_quarter = SearchMoonQuarter(time)

    while moon_quarter.quarter != 0:
        time = time.AddDays(-7)
        moon_quarter = SearchMoonQuarter(time)

    date = SezimalDateTime(_datetime.datetime.fromisoformat(str(moon_quarter.time)))

    previous_quarter_date = None

    while date.year <= year_finish:
        moon_quarter = SearchMoonQuarter(time)
        date = SezimalDateTime(_datetime.datetime.fromisoformat(str(moon_quarter.time)))

        if moon_quarter.quarter == 0:
            quarter = 'new'
            cross_quarter = 'waning_crescent'
        elif moon_quarter.quarter == 1:
            quarter = 'first_quarter'
            cross_quarter = 'waxing_crescent'
        elif moon_quarter.quarter == 2:
            quarter = 'full'
            cross_quarter = 'waxing_gibbous'
        else:
            quarter = 'third_quarter'
            cross_quarter = 'waning_gibbous'

        if date.ordinal_date not in MOONS:
            MOONS[date.ordinal_date] = [date, quarter]
        else:
            previous_quarter_date = date
            time = time.AddDays(6)
            continue

        print(quarter, date)

        if previous_quarter_date is not None:
            cross_quarter_date = _middle_date_time(previous_quarter_date, date, time_zone)

            if cross_quarter_date.ordinal_date not in MOONS:
                MOONS[cross_quarter_date.ordinal_date] = [cross_quarter_date, cross_quarter]

            print(cross_quarter, cross_quarter_date)

        previous_quarter_date = date
        time = time.AddDays(6)


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

        name = name.replace(' ', '_')

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
