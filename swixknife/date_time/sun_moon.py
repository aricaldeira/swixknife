
import sqlite3
import pathlib

DB_NAME = pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), 'sun_moon.db')

from .date import SezimalDate
from .date_time import SezimalDateTime
from .sezimal_functions import system_time_zone
from ..sezimal import SezimalInteger
from ..localization import SezimalLocale


NORTHERN_HEMISPHERE = 'N'
SOUTHERN_HEMISPHERE = 'S'


def _sun_moon_search(self, sun_moon: str, hemisphere: str = '', only_four: bool = False, nearest: bool = False):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

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
    sm.date <= '{str(self)}'
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
    sm.date = '{str(self)}'
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
    date_time = SezimalDateTime.from_days(res[1], time_zone='UTC')

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

    return name, date_time


def _season_name(self, hemisphere: str, locale: SezimalLocale, four_seasons: bool = False, nearest: bool = False) -> str:
    season_name, season_date_time = self._sun_moon_search(
        'sun', hemisphere=hemisphere, only_four=four_seasons, nearest=nearest,
    )

    if season_name in locale.SEASON_NAME:
        return locale.SEASON_NAME[season_name]

    return season_name


def _season_emoji(self, hemisphere: str, locale: SezimalLocale, four_seasons: bool = False, nearest: bool = False) -> str:
    season_name, season_date_time = self._sun_moon_search(
        'sun', hemisphere=hemisphere, only_four=four_seasons, nearest=nearest,
    )

    if hemisphere == NORTHERN_HEMISPHERE and season_name in locale.SEASON_EMOJI_NORTHERN_HEMISPHERE:
        return locale.SEASON_EMOJI_NORTHERN_HEMISPHERE[season_name]
    elif hemisphere == SOUTHERN_HEMISPHERE and season_name in locale.SEASON_EMOJI_SOUTHERN_HEMISPHERE:
        return locale.SEASON_EMOJI_SOUTHERN_HEMISPHERE[season_name]

    return season_name


def _season_time(self, fmt: str, locale: SezimalLocale, four_seasons: bool = False) -> str:
    season_name, season_date_time = self._sun_moon_search(
        'sun', only_four=four_seasons,
    )

    if not season_date_time:
        return ''

    if type(self) == SezimalDate:
        time_zone = system_time_zone()
    else:
        time_zone = self.time_zone

    season_date_time = season_date_time.at_time_zone(time_zone)

    return season_date_time.format(fmt, locale)


def _moon_phase(self, hemisphere: str, locale: SezimalLocale, four_phases: bool = False, nearest: bool = False) -> str:
    moon_phase, moon_phase_date_time = self._sun_moon_search(
        'moon', only_four=four_phases, nearest=nearest,
    )

    if moon_phase in locale.MOON_PHASE:
        return locale.MOON_PHASE[moon_phase]

    return moon_phase


def _moon_emoji(self, hemisphere: str, four_phases: bool = False, nearest: bool = False) -> str:
    moon_phase, moon_phase_date_time = self._sun_moon_search(
        'moon', only_four=four_phases, nearest=nearest,
    )

    emoji = ''

    if moon_phase == 'new':
        emoji = '\ufe0f🌑'
    elif moon_phase == 'waxing crescent':
        emoji = '\ufe0f🌒' if hemisphere == 'N' else '\ufe0f🌘'
    elif moon_phase == 'first quarter':
        emoji = '\ufe0f🌓' if hemisphere == 'N' else '\ufe0f🌗'
    elif moon_phase == 'waxing gibbous':
        emoji = '\ufe0f🌔' if hemisphere == 'N' else '\ufe0f🌖'
    elif moon_phase == 'full':
        emoji = '\ufe0f🌕'
    elif moon_phase == 'waning gibbous':
        emoji = '\ufe0f🌖' if hemisphere == 'N' else '\ufe0f🌔'
    elif moon_phase == 'third quarter':
        emoji = '\ufe0f🌗' if hemisphere == 'N' else '\ufe0f🌓'
    elif moon_phase == 'waning crescent':
        emoji = '\ufe0f🌘' if hemisphere == 'N' else '\ufe0f🌒'

    return emoji


def _moon_time(self, fmt: str, locale: SezimalLocale, four_phases: bool = False) -> str:
    moon_phase, moon_phase_date_time = self._sun_moon_search(
        'moon', only_four=four_phases,
    )

    if not moon_phase_date_time:
        return ''

    if type(self) == SezimalDate:
        time_zone = system_time_zone()
    else:
        time_zone = self.time_zone

    moon_phase_date_time = moon_phase_date_time.at_time_zone(time_zone)

    return moon_phase_date_time.format(fmt, locale)


def _apply_season_format(self, fmt: str, locale: SezimalLocale) -> str:
    for hemisphere in (NORTHERN_HEMISPHERE, SOUTHERN_HEMISPHERE, ''):
        if f'#{hemisphere}S' in fmt:
            fmt = fmt.replace(
                f'#{hemisphere}S',
                self._season_name(hemisphere or locale.DEFAULT_HEMISPHERE, locale),
            )

        if f'#{hemisphere}4S' in fmt:
            fmt = fmt.replace(
                f'#{hemisphere}4S',
                self._season_name(hemisphere or locale.DEFAULT_HEMISPHERE, locale, four_seasons=True),
            )

        if f'#@{hemisphere}S' in fmt:
            fmt = fmt.replace(
                f'#@{hemisphere}S',
                self._season_emoji(hemisphere or locale.DEFAULT_HEMISPHERE, locale),
            )

        if f'#@{hemisphere}4S' in fmt:
            fmt = fmt.replace(
                f'#@{hemisphere}4S',
                self._season_emoji(hemisphere or locale.DEFAULT_HEMISPHERE, locale, four_seasons=True),
            )

        if f'#~{hemisphere}S' in fmt:
            fmt = fmt.replace(
                f'#~{hemisphere}S',
                self._season_name(hemisphere or locale.DEFAULT_HEMISPHERE, locale, nearest=True),
            )

        if f'#~{hemisphere}4S' in fmt:
            fmt = fmt.replace(
                f'#~{hemisphere}4S',
                self._season_name(hemisphere or locale.DEFAULT_HEMISPHERE, locale, four_seasons=True, nearest=True),
            )

        if f'#@~{hemisphere}S' in fmt:
            fmt = fmt.replace(
                f'#@~{hemisphere}S',
                self._season_emoji(hemisphere or locale.DEFAULT_HEMISPHERE, locale, nearest=True),
            )

        if f'#@~{hemisphere}4S' in fmt:
            fmt = fmt.replace(
                f'#@~{hemisphere}4S',
                self._season_emoji(hemisphere or locale.DEFAULT_HEMISPHERE, locale, four_seasons=True, nearest=True),
            )

        if f'#{hemisphere}L' in fmt:
            fmt = fmt.replace(
                f'#{hemisphere}L',
                self._moon_phase(hemisphere or locale.DEFAULT_HEMISPHERE, locale),
            )

        if f'#{hemisphere}4L' in fmt:
            fmt = fmt.replace(
                f'#{hemisphere}4L',
                self._moon_phase(hemisphere or locale.DEFAULT_HEMISPHERE, locale, four_phases=True),
            )

        if f'#@{hemisphere}L' in fmt:
            fmt = fmt.replace(
                f'#@{hemisphere}L',
                self._moon_emoji(hemisphere or locale.DEFAULT_HEMISPHERE),
            )

        if f'#@{hemisphere}4L' in fmt:
            fmt = fmt.replace(
                f'#@{hemisphere}4L',
                self._moon_emoji(hemisphere or locale.DEFAULT_HEMISPHERE, four_phases=True),
            )

        if f'#~{hemisphere}L' in fmt:
            fmt = fmt.replace(
                f'#~{hemisphere}L',
                self._moon_phase(hemisphere or locale.DEFAULT_HEMISPHERE, locale, nearest=True),
            )

        if f'#~{hemisphere}4L' in fmt:
            fmt = fmt.replace(
                f'#~{hemisphere}4L',
                self._moon_phase(hemisphere or locale.DEFAULT_HEMISPHERE, locale, four_phases=True, nearest=True),
            )

        if f'#@~{hemisphere}L' in fmt:
            fmt = fmt.replace(
                f'#@~{hemisphere}L',
                self._moon_emoji(hemisphere or locale.DEFAULT_HEMISPHERE, nearest=True),
            )

        if f'#@~{hemisphere}4L' in fmt:
            fmt = fmt.replace(
                f'#@~{hemisphere}4L',
                self._moon_emoji(hemisphere or locale.DEFAULT_HEMISPHERE, four_phases=True, nearest=True),
            )

    if f'#TS' in fmt:
        fmt = fmt.replace('#TS', self._season_time('#u:#p', locale))

    if f'#T4S' in fmt:
        fmt = fmt.replace('#T4S', self._season_time('#u:#p', locale, four_seasons=True))

    if f'#TL' in fmt:
        fmt = fmt.replace('#TL', self._moon_time('#u:#p', locale))

    if f'#T4L' in fmt:
        fmt = fmt.replace('#T4L', self._moon_time('#u:#p', locale, four_phases=True))

    return fmt

SezimalDate._sun_moon_search = _sun_moon_search
SezimalDate._season_name = _season_name
SezimalDate._season_emoji = _season_emoji
SezimalDate._season_time = _season_time
SezimalDate._moon_phase = _moon_phase
SezimalDate._moon_emoji = _moon_emoji
SezimalDate._moon_time = _moon_time
SezimalDate._apply_season_format = _apply_season_format


def list_sun_moon(year: SezimalInteger, month: SezimalInteger, locale: SezimalLocale, hemisphere: str) -> str:
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    sql = f'''
select
    sm.sun_moon,
    sm.date_time_as_days

from
    sun_moon sm

where
    sm.date like '{str(year).zfill(6)}-{str(month).zfill(2)}-%'

order by
    sm.date_time_as_days;
'''

    res = cursor.execute(sql)
    res = res.fetchall()
    connection.close()

    if res is None:
        return ''

    time_zone = system_time_zone()

    text = ''

    for sun_moon, date_time_as_days in res:
        date = SezimalDateTime.from_days(date_time_as_days, 'UTC').at_time_zone(time_zone)

        if sun_moon == 'sun':
            fmt = f'{str(date.day).rjust(2)} - #@{hemisphere}S #{hemisphere}S (#TS)\n'
        else:
            fmt = f'{str(date.day).rjust(2)} - #@{hemisphere}L #{hemisphere}L (#TL)\n'

        text += date.format(fmt, locale)

    return text
