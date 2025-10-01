
import sqlite3

import pathlib

DB_NAME = pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), 'sun_moon.db')

from .date import SezimalDate
from .date_time import SezimalDateTime
from .sezimal_functions import system_time_zone, tz_days_offset, ZoneInfo
from ..sezimal import SezimalInteger, Sezimal
from ..localization import SezimalLocale
from ..functions import SezimalRange
from .format_tokens import SEASON_MOON_TEXT_FORMAT_TOKENS, SEASON_MOON_TIME_FORMAT_TOKENS


NORTHERN_HEMISPHERE = 'N'
SOUTHERN_HEMISPHERE = 'S'
NORTHERN_EQUATOR_HEMISPHERE = 'NE'
SOUTHERN_EQUATOR_HEMISPHERE = 'SE'


def _sun_moon_search(self, sun_moon: str, hemisphere: str = '', only_four: bool = False, nearest: bool = False, time_zone: str | ZoneInfo = None):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    if not time_zone:
        time_zone = system_time_zone()

    days_offset, days_offset_dst = tz_days_offset(time_zone, self.gregorian_isoformat)

    search_start = self.as_days - days_offset
    search_end = search_start + Sezimal('0.555_555_555_555_555_555')

    sql = f'''
select
    sm.name,
    sm.date_time_as_days

from
    sun_moon sm
'''

    if nearest:
        sql += f'''
where
    sm.date_time_as_days <= '{str(search_end)}'
    and sm.sun_moon = '{sun_moon}'
'''

        if only_four and sun_moon == 'sun':
            sql += f'''
    and sm.name not like '%cross%'
'''
        elif only_four and sun_moon == 'moon':
            sql += f'''
    and sm.name not like '%waxing%'
    and sm.name not like '%waning%'
'''

        sql += '''
order by
    sm.date desc

limit 1
'''
    else:
        sql += f'''
where
    sm.date_time_as_days >= '{str(search_start)}'
    and sm.date_time_as_days <= '{str(search_end)}'
    and sm.sun_moon = '{sun_moon}'
'''

        if only_four and sun_moon == 'sun':
            sql += f'''
    and sm.name not like '%cross%'
'''
        elif only_four and sun_moon == 'moon':
            sql += f'''
    and sm.name not like '%waxing%'
    and sm.name not like '%waning%'
'''

    sql += ';'

    res = cursor.execute(sql)
    res = res.fetchone()
    connection.close()

    if res is None:
        return '', None

    name = res[0]
    date_time = SezimalDateTime.from_days(Sezimal(res[1]), time_zone='UTC')

    if sun_moon == 'sun' and hemisphere:
        if hemisphere == NORTHERN_HEMISPHERE:
            name = name.replace('february', 'spring')
            name = name.replace('march', 'spring')
            name = name.replace('may', 'summer')
            name = name.replace('june', 'summer')
            name = name.replace('august', 'autumn')
            name = name.replace('september', 'autumn')
            name = name.replace('november', 'winter')
            name = name.replace('december', 'winter')

        elif hemisphere == SOUTHERN_HEMISPHERE:
            name = name.replace('february', 'autumn')
            name = name.replace('march', 'autumn')
            name = name.replace('may', 'winter')
            name = name.replace('june', 'winter')
            name = name.replace('august', 'spring')
            name = name.replace('september', 'spring')
            name = name.replace('november', 'summer')
            name = name.replace('december', 'summer')

        elif hemisphere == NORTHERN_EQUATOR_HEMISPHERE or hemisphere == SOUTHERN_EQUATOR_HEMISPHERE:
            name = name.replace('february', 'summer')
            name = name.replace('march', 'summer')
            name = name.replace('may', 'summer')
            name = name.replace('june', 'summer')
            name = name.replace('august', 'summer')
            name = name.replace('september', 'summer')
            name = name.replace('november', 'summer')
            name = name.replace('december', 'summer')

    return name, date_time


def _season_name(self, hemisphere: str, locale: SezimalLocale, four_seasons: bool = False, nearest: bool = False, time_zone: str | ZoneInfo = None) -> str:
    season_name, season_date_time = self._sun_moon_search(
        'sun', hemisphere=hemisphere,
        only_four=four_seasons, nearest=nearest, time_zone=time_zone,
    )

    if season_name in locale.SEASON_NAME:
        return locale.SEASON_NAME[season_name]

    return season_name


def _season_emoji(self, hemisphere: str, locale: SezimalLocale, four_seasons: bool = False, nearest: bool = False, time_zone: str | ZoneInfo = None) -> str:
    season_name, season_date_time = self._sun_moon_search(
        'sun', hemisphere=hemisphere,
        only_four=four_seasons, nearest=nearest, time_zone=time_zone,
    )

    if hemisphere in (NORTHERN_HEMISPHERE, NORTHERN_EQUATOR_HEMISPHERE) \
        and season_name in locale.SEASON_EMOJI_NORTHERN_HEMISPHERE:
        return locale.SEASON_EMOJI_NORTHERN_HEMISPHERE[season_name]
    elif hemisphere in (SOUTHERN_HEMISPHERE, SOUTHERN_EQUATOR_HEMISPHERE) \
        and season_name in locale.SEASON_EMOJI_SOUTHERN_HEMISPHERE:
        return locale.SEASON_EMOJI_SOUTHERN_HEMISPHERE[season_name]

    return season_name


def _season_time(self, fmt: str, locale: SezimalLocale, four_seasons: bool = False, time_zone: str | ZoneInfo = None) -> str:
    season_name, season_date_time = self._sun_moon_search(
        'sun', only_four=four_seasons, time_zone=time_zone,
    )

    if not season_date_time:
        return ''

    if type(self) == SezimalDate:
        time_zone = system_time_zone()
    else:
        time_zone = self.time_zone

    season_date_time = season_date_time.at_time_zone(time_zone)

    return season_date_time.format(fmt, locale)


def _moon_phase(self, hemisphere: str, locale: SezimalLocale, four_phases: bool = False, nearest: bool = False, time_zone: str | ZoneInfo = None) -> str:
    moon_phase, moon_phase_date_time = self._sun_moon_search(
        'moon', only_four=four_phases, nearest=nearest, time_zone=time_zone,
    )

    if moon_phase in locale.MOON_PHASE:
        return locale.MOON_PHASE[moon_phase]

    return moon_phase


def _moon_emoji(self, hemisphere: str, four_phases: bool = False, nearest: bool = False, time_zone: str | ZoneInfo = None) -> str:
    moon_phase, moon_phase_date_time = self._sun_moon_search(
        'moon', only_four=four_phases, nearest=nearest, time_zone=time_zone,
    )

    emoji = moon_phase

    if moon_phase == 'new':
        emoji = '🌑\ufe0f'
    elif moon_phase == 'waxing_crescent':
        emoji = '🌒\ufe0f' if hemisphere == 'N' else '🌘\ufe0f'
    elif moon_phase == 'first_quarter':
        emoji = '🌓\ufe0f' if hemisphere == 'N' else '🌗\ufe0f'
    elif moon_phase == 'waxing_gibbous':
        emoji = '🌔\ufe0f' if hemisphere == 'N' else '🌖\ufe0f'
    elif moon_phase == 'full':
        emoji = '🌕\ufe0f'
    elif moon_phase == 'waning_gibbous':
        emoji = '🌖\ufe0f' if hemisphere == 'N' else '🌔\ufe0f'
    elif moon_phase == 'third_quarter':
        emoji = '🌗\ufe0f' if hemisphere == 'N' else '🌓\ufe0f'
    elif moon_phase == 'waning_crescent':
        emoji = '🌘\ufe0f' if hemisphere == 'N' else '🌒\ufe0f'

    return emoji


def _moon_time(self, fmt: str, locale: SezimalLocale, four_phases: bool = False, time_zone: str | ZoneInfo = None) -> str:
    moon_phase, moon_phase_date_time = self._sun_moon_search(
        'moon', only_four=four_phases, time_zone=time_zone,
    )

    if not moon_phase_date_time:
        return ''

    if type(self) == SezimalDate:
        time_zone = system_time_zone()
    else:
        time_zone = self.time_zone

    moon_phase_date_time = moon_phase_date_time.at_time_zone(time_zone)

    return moon_phase_date_time.format(fmt, locale)


def _apply_season_format(self, fmt: str, locale: SezimalLocale, time_zone: str | ZoneInfo = None, season_moon_time_format: str = None) -> str:
    for regex, base, hemisphere, number, case, season_moon in SEASON_MOON_TEXT_FORMAT_TOKENS:
        if not regex.findall(fmt):
            continue

        if season_moon == 'S':
            if '@' in base:
                text = self._season_emoji(
                    hemisphere,
                    locale=locale,
                    four_seasons=number == '4',
                    time_zone=time_zone,
                    nearest='~' in base,
                )
            else:
                text = self._season_name(
                    hemisphere,
                    locale=locale,
                    four_seasons=number == '4',
                    time_zone=time_zone,
                    nearest='~' in base,
                )

        else:
            if '@' in base:
                text = self._moon_emoji(
                    hemisphere,
                    four_phases=number == '4',
                    nearest='~' in base,
                    time_zone=time_zone,
                )
            else:
                text = self._moon_phase(
                    hemisphere,
                    locale=locale,
                    four_phases=number == '4',
                    nearest='~' in base,
                    time_zone=time_zone,
                )

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

    for regex, base, number, season_moon in SEASON_MOON_TIME_FORMAT_TOKENS:
        if not regex.findall(fmt):
            continue

        if base:
            season_moon_time_format = f'#{base}u:#{base}p'
        else:
            season_moon_time_format = locale.SHORT_TIME_FORMAT

        if season_moon == 'S':
            text = self._season_time(
                season_moon_time_format,
                locale=locale,
                four_seasons=number == '4',
                time_zone=time_zone,
            )
        else:
            text = self._moon_time(
                season_moon_time_format,
                locale=locale,
                four_phases=number == '4',
                time_zone=time_zone,
            )

        fmt = regex.sub(text, fmt)

    return fmt


_SEASONS_CACHE = {}
_SEASONS_4_CACHE = {}
_SEASONS_WEEKS_CACHE = {}
_SEASONS_4_WEEKS_CACHE = {}


def _list_seasons_dates(self) -> list:
    if self.year in _SEASONS_CACHE:
        return _SEASONS_CACHE[self.year]

    seasons = []
    seasons_weeks = []

    for event_date, _, event_name in list_sun_moon(
        self.year,
        time_zone=self.time_zone,
        only_sun=True,
        only_four=False,
    ):
        seasons.append(event_date)
        seasons_weeks.append(event_date.week_in_year)

    _SEASONS_CACHE[self.year] = seasons
    _SEASONS_WEEKS_CACHE[self.year] = seasons_weeks

    seasons_4 = []
    seasons_weeks_4 = []

    for i in (1, 3, 5, 7):
        seasons_4.append(seasons[i])
        seasons_weeks_4.append(seasons[i].week_in_year)

    _SEASONS_4_CACHE[self.year] = seasons_4
    _SEASONS_4_WEEKS_CACHE[self.year] = seasons_weeks_4

    return seasons

def _list_4_seasons_dates(self) -> list:
    if self.year in _SEASONS_4_CACHE:
        return _SEASONS_4_CACHE[self.year]

    self.list_seasons_dates()
    return _SEASONS_4_CACHE[self.year]

def _list_seasons_weeks(self) -> list:
    if self.year in _SEASONS_WEEKS_CACHE:
        return _SEASONS_WEEKS_CACHE[self.year]

    self.list_seasons_dates()
    return _SEASONS_WEEKS_CACHE[self.year]

def _list_4_seasons_weeks(self) -> list:
    if self.year in _SEASONS_4_WEEKS_CACHE:
        return _SEASONS_4_WEEKS_CACHE[self.year]

    self.list_seasons_dates()
    return _SEASONS_4_WEEKS_CACHE[self.year]


_DCC_SEASONS_CACHE = {}
_DCC_SEASONS_4_CACHE = {}
_DCC_SEASONS_WEEKS_CACHE = {}
_DCC_SEASONS_4_WEEKS_CACHE = {}

def _list_dcc_seasons_dates(self) -> list:
    if self.dcc_year in _DCC_SEASONS_CACHE:
        return _DCC_SEASONS_CACHE[self.dcc_year]

    seasons = []
    seasons_weeks = []

    for event_date, _, event_name in list_sun_moon(
        self.year,
        time_zone=self.time_zone,
        only_sun=True,
        only_four=False,
        dcc_year=self.dcc_year,
    ):
        seasons.append(event_date)
        seasons_weeks.append(event_date.dcc_week_in_year)

    _DCC_SEASONS_CACHE[self.dcc_year] = seasons
    _DCC_SEASONS_WEEKS_CACHE[self.dcc_year] = seasons_weeks

    seasons_4 = []
    seasons_weeks_4 = []

    for i in (0, 2, 4, 6):
        seasons_4.append(seasons[i])
        seasons_weeks_4.append(seasons[i].dcc_week_in_year)

    _DCC_SEASONS_4_CACHE[self.dcc_year] = seasons_4
    _DCC_SEASONS_4_WEEKS_CACHE[self.dcc_year] = seasons_weeks_4

    return seasons

def _list_dcc_4_seasons_dates(self) -> list:
    if self.dcc_year in _DCC_SEASONS_4_CACHE:
        return _DCC_SEASONS_4_CACHE[self.dcc_year]

    self.list_dcc_seasons_dates()
    return _DCC_SEASONS_4_CACHE[self.dcc_year]

def _list_dcc_seasons_weeks(self) -> list:
    if self.dcc_year in _DCC_SEASONS_WEEKS_CACHE:
        return _DCC_SEASONS_WEEKS_CACHE[self.dcc_year]

    self.list_dcc_seasons_dates()
    return _DCC_SEASONS_WEEKS_CACHE[self.dcc_year]

def _list_dcc_4_seasons_weeks(self) -> list:
    if self.dcc_year in _DCC_SEASONS_4_WEEKS_CACHE:
        return _DCC_SEASONS_4_WEEKS_CACHE[self.dcc_year]

    self.list_dcc_seasons_dates()
    return _DCC_SEASONS_4_WEEKS_CACHE[self.dcc_year]


SezimalDate._sun_moon_search = _sun_moon_search
SezimalDate._season_name = _season_name
SezimalDate._season_emoji = _season_emoji
SezimalDate._season_time = _season_time
SezimalDate._moon_phase = _moon_phase
SezimalDate._moon_emoji = _moon_emoji
SezimalDate._moon_time = _moon_time
SezimalDate._apply_season_format = _apply_season_format

SezimalDateTime.list_seasons_dates = _list_seasons_dates
SezimalDateTime.list_4_seasons_dates = _list_4_seasons_dates
SezimalDateTime.list_dcc_seasons_dates = _list_dcc_seasons_dates
SezimalDateTime.list_dcc_4_seasons_dates = _list_dcc_4_seasons_dates

SezimalDateTime.list_seasons_weeks = _list_seasons_weeks
SezimalDateTime.list_4_seasons_weeks = _list_4_seasons_weeks
SezimalDateTime.list_dcc_seasons_weeks = _list_dcc_seasons_weeks
SezimalDateTime.list_dcc_4_seasons_weeks = _list_dcc_4_seasons_weeks


def list_sun_moon(year: SezimalInteger, month: SezimalInteger = None, time_zone: str | ZoneInfo = None, only_sun: bool = False, only_moon: bool = False, event: str = None, only_four: bool = False, dcc_year: SezimalInteger = None) -> list[str]:
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    if not time_zone:
        time_zone = system_time_zone()

    if month is None:
        date_start = SezimalDate(year, 1, 1)
        days_offset, days_offset_dst = tz_days_offset(time_zone, date_start.gregorian_isoformat)
        search_start = date_start.as_days - days_offset

        if dcc_year:
            date_end = SezimalDate(year + 1, 20, 44)

            if date_end.is_leap:
                date_end = SezimalDate(year + 1, 20, 55)

        else:
            date_end = SezimalDate(year, 20, 55) if date_start.is_leap else SezimalDate(year, 20, 44)

        days_offset, days_offset_dst = tz_days_offset(time_zone, date_end.gregorian_isoformat)
        search_end = date_end.as_days - days_offset + Sezimal('0.555_555_555_555_555_555')

    else:
        date_start = SezimalDate(year, month, 1)
        days_offset, days_offset_dst = tz_days_offset(time_zone, date_start.gregorian_isoformat)
        search_start = date_start.as_days - days_offset

        if dcc_year:
            date_end = SezimalDate(year + 1, 20, 44)

            if date_end.is_leap:
                date_end = SezimalDate(year + 1, 20, 55)

        else:
            date_end = SezimalDate(year, month, 55) if date_start.is_long_month else SezimalDate(year, month, 44)

        days_offset, days_offset_dst = tz_days_offset(time_zone, date_end.gregorian_isoformat)
        search_end = date_end.as_days - days_offset + Sezimal('0.555_555_555_555_555_555')

    sql = f'''
select
    sm.sun_moon,
    sm.name,
    sm.date_time_as_days

from
    sun_moon sm

where
    sm.date_time_as_days >= '{search_start}'
    and sm.date_time_as_days <= '{search_end}'
    {"and sm.sun_moon = 'sun'" if only_sun else ''}
    {"""and sm.sun_moon = 'sun'
        and sm.name not like '%cross%'""" if only_sun and only_four else ''}
    {"and sm.sun_moon = 'moon'" if only_moon else ''}
    {"""and sm.sun_moon = 'moon'
        and sm.name not like '%waxing%'
        and sm.name not like '%waning%'""" if only_moon and only_four else ''}
    {f"and sm.name = '{event}'" if event else ''}

order by
    sm.date_time_as_days;
'''

    res = cursor.execute(sql)
    res = res.fetchall()
    connection.close()

    if res is None:
        return []

    events = []

    for sun_moon, name, date_time_as_days in res:
        date_time_as_days = Sezimal(date_time_as_days)
        date = SezimalDateTime.from_days(date_time_as_days, 'UTC').at_time_zone(time_zone)

        if dcc_year:
            if date.dcc_year == dcc_year:
                events +=  [[
                    date,
                    sun_moon,
                    name,
                ]]
        elif date.year == year:
            events +=  [[
                date,
                sun_moon,
                name,
            ]]

    return events
