
import json
import pathlib
import urllib
import uuid
import threading

from flask import redirect, Response, request, render_template, jsonify
from main import app, sitemapper, sezimal_render_template
from  locale_detection import browser_preferred_locale

from swixknife import sezimal_locale, sezimal_spellout, SezimalInteger, Sezimal
from swixknife import default_to_sezimal_digits, Dozenal, DozenalInteger
from swixknife.date_time import SezimalDateTime, SezimalDate, SezimalTime
from swixknife.date_time.seasons_colors import weekly_season_colors
from swixknife.date_time.sun_moon import list_sun_moon
from swixknife.functions import SezimalList, SezimalDictionary, SezimalRange
from swixknife.date_time.calendar import other_calendar_date_to_ordinal_date
from swixknife.weather import SezimalWeather
from swixknife.units import sezimal_to_decimal_unit


from decimal import Decimal
from datetime import datetime
from zoneinfo import ZoneInfo

EVENTS_CACHE = SezimalDictionary({})


def _calendar_context(locale, date=None, gray_scale=False):
    if not date:
        date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    colors = weekly_season_colors(
        year=date.year,
        hemisphere=locale.DEFAULT_HEMISPHERE,
        time_zone=locale.DEFAULT_TIME_ZONE,
        gray_scale=gray_scale,
        calendar=locale.calendar_displayed or 'SYM',
    )

    if not SezimalInteger(130) in colors:
        colors[SezimalInteger(130)] = colors[SezimalInteger(1)]

    data = {
        'SezimalDate': SezimalDate,
        'SezimalList': SezimalList,
        'SezimalDictionary': SezimalDictionary,
        'SezimalRange': SezimalRange,
        'SezimalInteger': SezimalInteger,
        'Sezimal': Sezimal,
        'Decimal': Decimal,
        'Dozenal': Dozenal,
        'sdu': sezimal_to_decimal_unit,
        'round': round,
        'getattr': getattr,
        'str': str,
        'int': int,
        'eval': eval,
        'len': len,
        'sorted': sorted,
        'datetime': datetime,
        'locale': locale,
        'gray_scale': gray_scale,
        'dark_mode': True,
        'small_screen': False,
        'colors': colors,
        'date': date,
        'sezimal_digits': False,
        'base': locale.base,
        'format_token': locale.format_token,
        'uta_first': None,
        'uta_last': None,
    }

    if not locale.calendar_displayed:
        locale.calendar_displayed = 'SYM'

    if locale.calendar_displayed == 'SYM':
        data['date_last_month'] = date.previous(months=1)
        data['date_next_month'] = date.next(months=1)
    elif locale.calendar_displayed == 'ISO':
        data['date_last_month'] = date.gregorian_previous(months=1)
        data['date_next_month'] = date.gregorian_next(months=1)
    elif locale.calendar_displayed == 'DCC':
        data['date_last_month'] = date.dcc_previous(months=1)
        data['date_next_month'] = date.dcc_next(months=1)

    # Dark mode
    if data['dark_mode']:
        data['shade_month'] =  '100' if gray_scale else '300'
        data['shade_week_number'] =  '300'
        data['shade_01'] =  '400'
        data['shade_02'] =  '500'
        data['shade_03'] =  '600'
        data['shade_04'] =  '500'
        data['shade_05'] =  '400'
        data['shade_10'] =  '400'
        data['shade_11'] =  '300'

        data['back_shade_week_number'] =  '300'
        data['back_shade_01'] =  '400'
        data['back_shade_02'] =  '500'
        data['back_shade_03'] =  '600'
        data['back_shade_04'] =  '500'
        data['back_shade_05'] =  '400'
        data['back_shade_10'] =  '400'
        data['back_shade_11'] =  '300'

        data['text_shade_week_number'] =  '900'
        data['text_shade_01'] =  '50'
        data['text_shade_02'] =  '50'
        data['text_shade_03'] =  '50'
        data['text_shade_04'] =  '50'
        data['text_shade_05'] =  '50'
        data['text_shade_10'] =  '50'
        data['text_shade_11'] =  '50'
    else:
        data['shade_month'] =  '300' if gray_scale else '600'

        data['shade_week_number'] =  '900'
        data['shade_01'] =  '900'
        data['shade_02'] =  '900'
        data['shade_03'] =  '900'
        data['shade_04'] =  '900'
        data['shade_05'] =  '900'
        data['shade_10'] =  '900'
        data['shade_11'] =  '900'
        # data['shade_week_number'] =  '600'
        # data['shade_01'] =  '700'
        # data['shade_02'] =  '800'
        # data['shade_03'] =  '900'
        # data['shade_04'] =  '800'
        # data['shade_05'] =  '700'
        # data['shade_10'] =  '700'
        # data['shade_11'] =  '600'

        data['back_shade_week_number'] =  '900'
        data['back_shade_01'] =  '900'
        data['back_shade_02'] =  '900'
        data['back_shade_03'] =  '900'
        data['back_shade_04'] =  '900'
        data['back_shade_05'] =  '900'
        data['back_shade_10'] =  '900'
        data['back_shade_11'] =  '900'
        # data['back_shade_week_number'] =  '600'
        # data['back_shade_01'] =  '700'
        # data['back_shade_02'] =  '800'
        # data['back_shade_03'] =  '900'
        # data['back_shade_04'] =  '800'
        # data['back_shade_05'] =  '700'
        # data['back_shade_10'] =  '700'
        # data['back_shade_11'] =  '600'

        data['text_shade_week_number'] =  '900'
        data['text_shade_01'] =  '50'
        data['text_shade_02'] =  '50'
        data['text_shade_03'] =  '50'
        data['text_shade_04'] =  '50'
        data['text_shade_05'] =  '50'
        data['text_shade_10'] =  '50'
        data['text_shade_11'] =  '50'

    if locale.calendar_displayed == 'SYM':
        month_date = date.date.replace(day=1)

    elif locale.calendar_displayed == 'ISO':
        month_date = date.date.replace(day=date.day)
        gd = datetime(int(month_date.gregorian_year), int(month_date.gregorian_month), 1)
        month_date = SezimalDate(gd)
        month_date = month_date.previous(days=month_date.weekday - 1)

    elif locale.calendar_displayed == 'DCC':
        month_date = date.date.replace(day=date.day)
        month_date = SezimalDate.from_dcc(month_date.dcc_year, month_date.dcc_month, 0)

    month_date = month_date.previous(days=1)

    if locale.calendar_displayed != 'DCC' and locale.use_first_weekday:
        if locale.FIRST_WEEKDAY == 'SUN':
            month_date = month_date.previous(days=1)
        elif locale.FIRST_WEEKDAY == 'SAT':
            month_date = month_date.previous(days=2)

    data['month_dates'] = SezimalList([])

    if locale.calendar_displayed == 'DCC':
        for week in SezimalRange(10):
            data['month_dates'].append(SezimalList([]))

            for day in SezimalRange(10):
                month_date = month_date.next(days=1)
                data['month_dates'][week].append(month_date)

    else:
        for week in SezimalRange(11):
            data['month_dates'].append(SezimalList([]))

            for day in SezimalRange(11):
                month_date = month_date.next(days=1)
                data['month_dates'][week].append(month_date)

    return data


# @sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/decimal-calendar')
@app.route('/symmetry454-calendar')
def decimal_today_route() -> Response:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
        base = locale.base
        format_token = locale.format_token
        theme = locale.theme
        mobile = locale.mobile
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale = _prepare_locale(locale, {
            'base': 10,
            'format_token': '',
            'time_zone': locale.DEFAULT_TIME_ZONE,
            'hemisphere': 'locale',
            'hour_format': 'locale',
            'calendar_displayed': 'SYM',
            'mobile': 'false',
            'theme': 'FULL_COLOR',
            'show_seconds': 'true',
            'locale_first_weekday': 'false',
        })

    date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    data = _calendar_context(locale, date)
    data['base'] = 14
    data['format_token'] = '9'
    data['hide_base'] = True
    data['force_decimal'] = True

    if locale.DIGITS:
        data['format_token'] += '?'

    return sezimal_render_template(
        'today.html',
        sezimal_month_number=date.month,
        **data,
    )


@app.route('/dozenal-today')
def dozenal_today_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    data = _calendar_context(locale, date)
    data['base'] = 20
    data['format_token'] = '↋'
    data['hide_base'] = True

    if locale.DIGITS:
        data['format_token'] += '?'

    return sezimal_render_template(
        'today_dozenal.html',
        sezimal_month_number=date.month,
        **data,
    )


@app.route('/today')
def today_route() -> Response:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
        mobile = locale.mobile
        base = locale.base
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale = _prepare_locale(locale, {
            'base': 10,
            'format_token': '',
            'time_zone': locale.DEFAULT_TIME_ZONE,
            'hemisphere': 'locale',
            'hour_format': 'locale',
            'calendar_displayed': 'SYM',
            'mobile': 'false',
            'theme': 'FULL_COLOR',
            'show_seconds': 'true',
            'locale_first_weekday': 'false',
        })
        base = 10
        mobile = False

    date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, date)
    context['mobile'] = mobile
    context['base'] = base

    # if locale.DIGITS:
    #     context['format_token'] = (context['format_token'] or '') + '?'

    return sezimal_render_template(
        'today.html',
        sezimal_month_number=date.month,
        **context,
    )

@app.route('/calendar/process', methods=['POST'])
def api_calendar_process():
    dados = json.loads(request.data.decode('utf-8'))

    dados['base'] = int(dados['base'])
    base = dados['base']
    format_token = dados['format_token'] or ''

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    gray_scale = dados['theme'] == 'GRAY'

    locale = _prepare_locale(locale, dados)

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    if 'date' in dados and dados['date']:
        date = SezimalDateTime.combine(SezimalDate(dados['date']), now.time, locale.DEFAULT_TIME_ZONE)

    else:
        date = now

    if dados['direction'] == 'today':
        date = now
    elif dados['direction'] == 'previous':
        if locale.calendar_displayed == 'SYM':
            if dados['direction_type'] == 'day':
                date = date.previous(days=1)
            elif dados['direction_type'] == 'week':
                date = date.previous(weeks=1)
            elif dados['direction_type'] == 'month':
                date = date.previous(months=1)
            elif dados['direction_type'] == 'quarter':
                date = date.previous(quarters=1)
            elif dados['direction_type'] == 'year':
                date = date.previous(years=1)
            elif dados['direction_type'] == '10_years':
                date = date.previous(years=dados['base'] or '10')
            elif dados['direction_type'] == '100_years':
                date = date.previous(years=SezimalInteger(dados['base']) ** 2)

        elif locale.calendar_displayed == 'ISO':
            if dados['direction_type'] == 'day':
                date = date.gregorian_previous(days=1)
            elif dados['direction_type'] == 'week':
                date = date.gregorian_previous(weeks=1)
            elif dados['direction_type'] == 'month':
                date = date.gregorian_previous(months=1)
            elif dados['direction_type'] == 'quarter':
                date = date.gregorian_previous(quarters=1)
            elif dados['direction_type'] == 'year':
                date = date.gregorian_previous(years=1)
            elif dados['direction_type'] == '10_years':
                date = date.gregorian_previous(years=dados['base'] or '10')
            elif dados['direction_type'] == '100_years':
                date = date.gregorian_previous(years=SezimalInteger(dados['base']) ** 2)

        elif locale.calendar_displayed == 'DCC':
            if dados['direction_type'] == 'day':
                date = date.dcc_previous(days=1)
            elif dados['direction_type'] == 'week':
                date = date.dcc_previous(weeks=1)
            elif dados['direction_type'] == 'month':
                date = date.dcc_previous(months=1)
            elif dados['direction_type'] == 'quarter':
                date = date.dcc_previous(terms=1)
            elif dados['direction_type'] == 'year':
                date = date.dcc_previous(years=1)
            elif dados['direction_type'] == '10_years':
                date = date.dcc_previous(years=dados['base'] or '10')
            elif dados['direction_type'] == '100_years':
                date = date.dcc_previous(years=SezimalInteger(dados['base']) ** 2)

        if date.year < 155_500:
            date = date.replace(year=155_500)

    elif dados['direction'] == 'next':
        if locale.calendar_displayed == 'SYM':
            if dados['direction_type'] == 'day':
                date = date.next(days=1)
            elif dados['direction_type'] == 'week':
                date = date.next(weeks=1)
            elif dados['direction_type'] == 'month':
                date = date.next(months=1)
            elif dados['direction_type'] == 'quarter':
                date = date.next(quarters=1)
            elif dados['direction_type'] == 'year':
                date = date.next(years=1)
            elif dados['direction_type'] == '10_years':
                date = date.next(years=dados['base'] or '10')
            elif dados['direction_type'] == '100_years':
                date = date.next(years=SezimalInteger(dados['base']) ** 2)

        elif locale.calendar_displayed == 'ISO':
            if dados['direction_type'] == 'day':
                date = date.gregorian_next(days=1)
            elif dados['direction_type'] == 'week':
                date = date.gregorian_next(weeks=1)
            elif dados['direction_type'] == 'month':
                date = date.gregorian_next(months=1)
            elif dados['direction_type'] == 'quarter':
                date = date.gregorian_next(quarters=1)
            elif dados['direction_type'] == 'year':
                date = date.gregorian_next(years=1)
            elif dados['direction_type'] == '10_years':
                date = date.gregorian_next(years=dados['base'] or '10')
            elif dados['direction_type'] == '100_years':
                date = date.gregorian_next(years=SezimalInteger(dados['base']) ** 2)

        elif locale.calendar_displayed == 'DCC':
            if dados['direction_type'] == 'day':
                date = date.dcc_next(days=1)
            elif dados['direction_type'] == 'week':
                date = date.dcc_next(weeks=1)
            elif dados['direction_type'] == 'month':
                date = date.dcc_next(months=1)
            elif dados['direction_type'] == 'quarter':
                date = date.dcc_next(terms=1)
            elif dados['direction_type'] == 'year':
                date = date.dcc_next(years=1)
            elif dados['direction_type'] == '10_years':
                date = date.dcc_next(years=dados['base'] or '10')
            elif dados['direction_type'] == '100_years':
                date = date.dcc_next(years=SezimalInteger(dados['base']) ** 2)

        if date.year > 230_000:
            date = date.replace(year=230_000)

    context = _calendar_context(locale, date, gray_scale)
    context['locale'] = locale
    context['now'] = now
    # context['base'] = dados['base']
    # context['format_token'] = (dados['format_token'] or '')
    context['mobile'] = dados['mobile']

    if locale.DIGITS:
        context['format_token'] += '?'

    if dados['hour_format'] != 'locale':
        locale.HOUR_FORMAT = dados['hour_format']

    if locale.calendar_displayed == 'SYM':
        context['events'] = _calendar_events(locale, date.year, context) or {}

        if dados['view'] == 'quarterly':
            if date.month == 1:
                context['events_last_year'] = _calendar_events(locale, date.year - 1, context) or {}
            else:
                context['events_last_year'] = context['events']

            if date.month == 20:
                context['events_next_year'] = _calendar_events(locale, date.year + 1, context) or {}
            else:
                context['events_next_year'] = context['events']

    elif locale.calendar_displayed == 'ISO':
        context['events'] = _calendar_events(locale, date.gregorian_year, context) or {}

        if dados['view'] == 'quarterly':
            if date.gregorian_month == 1:
                context['events_last_year'] = _calendar_events(locale, date.gregorian_year - 1, context) or {}
            else:
                context['events_last_year'] = context['events']

            if date.gregorian_month == 20:
                context['events_next_year'] = _calendar_events(locale, date.gregorian_year + 1, context) or {}
            else:
                context['events_next_year'] = context['events']

    elif locale.calendar_displayed == 'DCC':
        context['events'] = _calendar_events(locale, date.dcc_year, context) or {}

        if dados['view'] == 'quarterly':
            if date.dcc_month == 0:
                context['events_last_year'] = _calendar_events(locale, date.dcc_year - 1, context) or {}
            else:
                context['events_last_year'] = context['events']

            if date.dcc_month == 14 or (date.dcc_month == 13 and date.dcc_is_short_year):
                context['events_next_year'] = _calendar_events(locale, date.dcc_year + 1, context) or {}
            else:
                context['events_next_year'] = context['events']

    script = ''

    view = sezimal_render_template(
        f'''calendar_view_{dados['view']}.html''',
        **context,
    )

    if '<script type="text/javascript" id="view_script">' in view:
        view, script = view.split('<script type="text/javascript" id="view_script">')
        script = script.split('</script>')[0]

    res = {
        'date_to_store': str(date.date),
        'view': view,
        'script_text': script,
    }

    return jsonify(res)


class SezimalEvent:
    def __init__(
        self, origin: str = '', emoji: str = '', name: str = '',
        date: str | SezimalDate = None, full_day: bool = True,
        start_time: str | SezimalTime = None,
        finish_time: str | SezimalTime = None,
        id: str = None,
        obs: str = None,
    ):
        if not date:
            self.date = SezimalDate.today()
        elif type(date) == SezimalDate:
            self.date = date
        else:
            if ' ' in date:
                self.date = SezimalDateTime(date)
            else:
                self.date = SezimalDate(date)

        if not origin:
            self.origin = 'SYM+' + self.date.format('#9sY-#9m-#9d')
        else:
            self.origin = origin

        self.emoji = emoji
        self.name = name

        self.full_day = full_day

        if not start_time:
            self.start_time = None
        elif type(start_time) == SezimalTime:
            self.start_time = start_time
        else:
            self.start_time = SezimalTime(start_time)

        if not finish_time:
            self.finish_time = None
        elif type(finish_time) == SezimalTime:
            self.finish_time = finish_time
        else:
            self.finish_time = SezimalTime(finish_time)

        if not id:
            number = int(SezimalDateTime.now('UTC').format('#>y#dY#u#p#a'))
            self.id = str(uuid.uuid1(node=number, clock_seq=number))
        else:
            self.id = id

        self.obs = obs

    def __repr__(self):
        return f"""SezimalEvent('{self.origin}', '{self.emoji}', '{self.name}', {"'" + str(self.date) + "'" if self.date else None}, {self.full_day}, {"'" + str(self.start_time) + "'" if self.start_time else None}, {"'" + str(self.finish_time) + "'" if self.finish_time else None}, id={"'" + self.id + "'" if self.id else None}, obs={"'" + self.obs + "'" if self.obs else None})"""

    def __str__(self):
        return self.__repr__()

    @property
    def daily_view(self):
        if self.emoji:
            line = self.emoji + ' - '
        else:
            line = ''

        if self.name:
            line += self.name

        return line

    @property
    def origin_calendar(self):
        if (not self.origin) or len(self.origin) <= 3:
            return ''

        if self.origin[0:3] in ('SYM', 'SEZ',
            'ISO', 'GRE', 'ISR', 'IND',
            'JUL', 'HEB', 'JEW', 'HIJ', 'IRN', 'CHR', 'ORT', 'ISL'):
            return self.origin[0:3]

        return 'SEZ'

    @property
    def day(self) -> str:
        if self.origin_calendar in ('SYM', 'SEZ'):
            return str(self.date.symmetric_day).zfill(2)
        elif self.origin_calendar in ('ISO', 'GRE', 'CHR'):
            return str(self.date.gregorian_day).zfill(2)
        elif self.origin_calendar in ('HEB', 'JEW'):
            return self.hebrew_date().split('-')[-1]
        elif self.origin_calendar in ('HIJ', 'ISL'):
            return self.islamic_date().split('-')[-1]

        return ''

    @property
    def month(self) -> str:
        if self.origin_calendar in ('SYM', 'SEZ'):
            return str(self.date.symmetric_month).zfill(2)
        elif self.origin_calendar in ('ISO', 'GRE', 'CHR'):
            return str(self.date.gregorian_month).zfill(2)
        elif self.origin_calendar in ('HEB', 'JEW'):
            return self.hebrew_date().split('-')[1]
        elif self.origin_calendar in ('HIJ', 'ISL'):
            return self.islamic_date().split('-')[1]

        return ''

    @property
    def year(self) -> str:
        if self.origin_calendar in ('SYM', 'SEZ'):
            return str(self.date.symmetric_year).zfill(4)
        elif self.origin_calendar in ('ISO', 'GRE', 'CHR'):
            return str(self.date.gregorian_year).zfill(4)
        elif self.origin_calendar in ('HEB', 'JEW'):
            return self.hebrew_date().split('-')[0]
        elif self.origin_calendar in ('HIJ', 'ISL'):
            return self.islamic_date().split('-')[0]

        return ''


def _write_calendar_cache(locale: str, cache_key: str, events: SezimalDictionary) -> None:
    file_path = pathlib.Path.home().joinpath(f'.sezimal/{locale}/')
    file_path.mkdir(parents=True, exist_ok=True)
    file_path = file_path.joinpath(f"{cache_key.replace('|', '_').replace('/', '_')}.json")

    text = str(events)

    for i in range(0, 62):
        text = text.replace(f" == Decimal('{i}')", '')

    open(file_path, 'w').write(text)


def _read_calendar_cache(locale: str, cache_key: str, only_check: bool = False) -> SezimalDictionary | None | bool:
    file_path = pathlib.Path.home().joinpath(
        f".sezimal/{locale}/{cache_key.replace('|', '_').replace('/', '_')}.json"
    )

    if not file_path.is_file():
        return False

    if only_check:
        return True

    text = open(file_path, 'r').read()

    return eval(text)


def _limit_holidays(events, show_holidays):
    if (not show_holidays) or (not events) or type(events) == bool:
        return events

    limited_events = SezimalDictionary()

    if 'moon' in events:
        limited_events['moon'] = events['moon']

    for month in events:
        if type(month) == str:
            continue

        for day in events[month]:
            for event in events[month][day]:
                if 'SYM' in event.origin and 'SYM' not in show_holidays:
                    continue

                if not event.origin_calendar in show_holidays:
                    continue

                if month not in limited_events:
                    limited_events[month] = SezimalDictionary()

                if day not in limited_events[month]:
                    limited_events[month][day] = SezimalList()

                limited_events[month][day].append(event)

    return limited_events


def _calendar_events(locale, year, context, only_check: bool = False):
    if locale.calendar_displayed == 'SYM':
        if year >= 0:
            cache_key = 'SYM+' + str(year)
        else:
            cache_key = 'SYM' + str(year)

    elif locale.calendar_displayed == 'ISO':
        if year >= 0:
            cache_key = 'ISO+' + str(year)
        else:
            cache_key = 'ISO' + str(year)

    elif locale.calendar_displayed == 'DCC':
        if year >= 0:
            cache_key = 'DCC+' + str(year)
        else:
            cache_key = 'DCC' + str(year)

    cache_key += '|' + locale.LANGUAGE_TAG
    cache_key += '|' + locale.DEFAULT_TIME_ZONE
    cache_key += '|' + locale.DEFAULT_HEMISPHERE

    if locale.base == 14:
        cache_key += '|' + locale.HOUR_FORMAT
    else:
        cache_key += '|24h'

    cache_key += '|' + str(locale.base) + locale.format_token

    if cache_key in EVENTS_CACHE:
        show_holidays = getattr(locale, 'SHOW_HOLIDAYS', 'ISO') or 'ISO'

        ck = cache_key + '|' + show_holidays

        if ck in EVENTS_CACHE:
            return EVENTS_CACHE[ck]

        EVENTS_CACHE[ck] = _limit_holidays(EVENTS_CACHE[cache_key], show_holidays)

        return EVENTS_CACHE[ck]

    cache = _read_calendar_cache(locale.LANGUAGE_TAG, cache_key, only_check=only_check)

    if cache:
        EVENTS_CACHE[cache_key] = cache

        return _calendar_events(locale, year, context, only_check)

    events = SezimalDictionary({})

    all_events = []

    if locale.calendar_displayed == 'SYM':
        all_events += locale.HOLIDAYS

    all_events += locale.HOLIDAYS_OTHER_CALENDAR
    all_events += locale.CHRISTIAN_HOLIDAYS
    all_events += locale.JEWISH_HOLIDAYS
    all_events += locale.ISLAMIC_HOLIDAYS

    _process_events_list(all_events, events, locale.calendar_displayed, year, locale, context)

    EVENTS_CACHE[cache_key] = events
    _write_calendar_cache(locale.LANGUAGE_TAG, cache_key, events)

    return _calendar_events(locale, year, context, only_check)


def _process_events_list(all_events, events, calendar, year, locale, context):
    if calendar == 'ISO':
        years = \
            SezimalInteger(200_000) + Decimal(year) - 1, \
            SezimalInteger(200_000) + Decimal(year), \
            SezimalInteger(200_000) + Decimal(year) + 1
    else:
        years = year - 1, year, year + 1

    #
    # First the Seasons
    #
    for reference_year in years:
        seasons = list_sun_moon(reference_year, time_zone=locale.DEFAULT_TIME_ZONE, only_sun=True, only_four=False)

        for event_date, _, season_name in seasons:
            if calendar == 'SYM':
                if event_date.year != year:
                    continue
            elif calendar == 'ISO':
                if event_date.gregorian_year != year:
                    continue
            elif calendar == 'DCC':
                if event_date.dcc_year != year:
                    continue

            event_emoji = event_date.format(f'#@{locale.DEFAULT_HEMISPHERE}S', locale)
            event_name = event_date.format(f'#{locale.DEFAULT_HEMISPHERE}S ({locale.SHORT_TIME_FORMAT})', locale)

            event = SezimalEvent()
            event.origin = 'ISO-' + str(event_date.gregorian_date)
            event.emoji = event_emoji
            event.name = event_name
            event.date = event_date
            event.obs = season_name

            event_sym = SezimalEvent()
            event_sym.origin = 'SYM+' + str(event_date)
            event_sym.emoji = event_emoji
            event_sym.name = event_name
            event_sym.date = event_date
            event_sym.obs = season_name

            if calendar == 'SYM':
                if event.date.month not in events:
                    events[event.date.month] = SezimalDictionary({})

                if event.date.day not in events[event.date.month]:
                    events[event.date.month][event.date.day] = SezimalList([])

                events[event.date.month][event.date.day].append(event)
                events[event.date.month][event.date.day].append(event_sym)

            elif calendar == 'ISO':
                if event.date.gregorian_month not in events:
                    events[event.date.gregorian_month] = SezimalDictionary({})

                if event.date.gregorian_day not in events[event.date.gregorian_month]:
                    events[event.date.gregorian_month][event.date.gregorian_day] = SezimalList([])

                events[event.date.gregorian_month][event.date.gregorian_day].append(event)
                events[event.date.gregorian_month][event.date.gregorian_day].append(event_sym)

            elif calendar == 'DCC':
                if event.date.dcc_month not in events:
                    events[event.date.dcc_month] = SezimalDictionary({})

                if event.date.dcc_day not in events[event.date.dcc_month]:
                    events[event.date.dcc_month][event.date.dcc_day] = SezimalList([])

                events[event.date.dcc_month][event.date.dcc_day].append(event)
                events[event.date.dcc_month][event.date.dcc_day].append(event_sym)

    events['moon'] = SezimalDictionary()

    #
    # Second, Moon Phases
    #
    for reference_year in years:
        phases = list_sun_moon(reference_year, time_zone=locale.DEFAULT_TIME_ZONE, only_moon=True, only_four=False)

        for event_date, _, phase_name in phases:
            if calendar == 'SYM':
                if event_date.year != year:
                    continue
            elif calendar == 'ISO':
                if event_date.gregorian_year != year:
                    continue
            elif calendar == 'DCC':
                if event_date.dcc_year != year:
                    continue

            event_emoji = event_date.format(f'#@{locale.DEFAULT_HEMISPHERE}L', locale)
            event_name = event_date.format(f'#{locale.DEFAULT_HEMISPHERE}L ({locale.SHORT_TIME_FORMAT})', locale)

            event = SezimalEvent()

            if calendar == 'SYM':
                event.origin = 'SYM+' + str(event_date)
            else:
                event.origin = 'ISO-' + str(event_date.gregorian_date)

            event.emoji = event_emoji
            event.name = event_name
            event.date = event_date
            event.obs = phase_name

            if calendar == 'SYM':
                if event.date.month not in events['moon']:
                    events['moon'][event.date.month] = SezimalDictionary({})

                if event.date.day not in events['moon'][event.date.month]:
                    events['moon'][event.date.month][event.date.day] = SezimalList([])

                events['moon'][event.date.month][event.date.day].append(event)

            elif calendar == 'ISO':
                if event.date.gregorian_month not in events['moon']:
                    events['moon'][event.date.gregorian_month] = SezimalDictionary({})

                if event.date.gregorian_day not in events['moon'][event.date.gregorian_month]:
                    events['moon'][event.date.gregorian_month][event.date.gregorian_day] = SezimalList([])

                events['moon'][event.date.gregorian_month][event.date.gregorian_day].append(event)

            elif calendar == 'DCC':
                if event.date.dcc_month not in events['moon']:
                    events['moon'][event.date.dcc_month] = SezimalDictionary({})

                if event.date.dcc_day not in events['moon'][event.date.dcc_month]:
                    events['moon'][event.date.dcc_month][event.date.dcc_day] = SezimalList([])

                events['moon'][event.date.dcc_month][event.date.dcc_day].append(event)

    for event_origin, event_name_ in all_events:
        for reference_year in years:
            event_ordinal_date, (event_year, event_month, event_day), age = \
                other_calendar_date_to_ordinal_date(event_origin.replace('CHR+SYM+', 'SYM+'), reference_year)

            event_date = SezimalDate.from_ordinal_date(event_ordinal_date)

            if calendar == 'SYM':
                if event_date.year != year:
                    continue
            elif calendar == 'ISO':
                if event_date.gregorian_year != year:
                    continue
            elif calendar == 'DCC':
                if event_date.dcc_year != year:
                    continue

            event_name = event_name_.replace('🕆', '🕇')

            event_emoji = event_name.split(' ')[0]
            event_name = event_name.replace(event_emoji, '').strip()

            if context['base'] == 10:
                if context['format_token'] == '!':
                    event_name = event_name.replace('#i', default_to_sezimal_digits(str(age)))
                    # event_name = locale.to_sezimal_digits(event_name)

                elif '?' in context['format_token'] and locale.DIGITS:
                    event_name = event_name.replace('#i', locale.digit_replace(str(age)))

                else:
                    event_name = event_name.replace('#i', str(age))

            elif context['base'] == 14:
                if '?' in context['format_token'] and locale.DIGITS:
                    event_name = event_name.replace('#i', locale.digit_replace(str(age.decimal)))
                else:
                    event_name = event_name.replace('#i', str(age.decimal))

                if locale.HOUR_FORMAT == '12h':
                    event_name = event_name.replace('#u', '%I')
                    event_name = event_name.replace('#p', '%M %P')
                else:
                    event_name = event_name.replace('#u', '%H')
                    event_name = event_name.replace('#p', '%M')

            elif context['base'] == 20:
                if '?' in context['format_token'] and locale.DIGITS:
                    event_name = event_name.replace('#i', locale.digit_replace(age.dozenal))
                else:
                    event_name = event_name.replace('#i', age.dozenal)

                event_name = locale._to_other_base(20, event_name)
                event_name = event_name.replace('#u', '.#↋↋u')
                event_name = event_name.replace('#p', '#↋↋p')

            if '?' in context['format_token'] and locale.DIGITS:
                event_name = event_name.replace('%i', locale.digit_replace(str(age.decimal)))
                event_name = event_name.replace('%Y', locale.digit_replace(str(event_year).zfill(4)))
                event_name = event_name.replace('%m', locale.digit_replace(str(event_month).zfill(2)))
                event_name = event_name.replace('%d', locale.digit_replace(str(event_day).zfill(2)))
            else:
                event_name = event_name.replace('%i', str(age.decimal))
                event_name = event_name.replace('%Y', str(event_year).zfill(4))
                event_name = event_name.replace('%m', str(event_month).zfill(2))
                event_name = event_name.replace('%d', str(event_day).zfill(2))

            event = SezimalEvent()
            event.origin = event_origin
            event.emoji = event_emoji
            event.name = event_name
            event.date = event_date

            if calendar == 'SYM':
                if event.date.month not in events:
                    events[event.date.month] = SezimalDictionary({})

                if event.date.day not in events[event.date.month]:
                    events[event.date.month][event.date.day] = SezimalList([])

                events[event.date.month][event.date.day].append(event)

            elif calendar == 'ISO':
                if event.date.gregorian_month not in events:
                    events[event.date.gregorian_month] = SezimalDictionary({})

                if event.date.gregorian_day not in events[event.date.gregorian_month]:
                    events[event.date.gregorian_month][event.date.gregorian_day] = SezimalList([])

                events[event.date.gregorian_month][event.date.gregorian_day].append(event)

            elif calendar == 'DCC':
                if event.date.dcc_month not in events:
                    events[event.date.dcc_month] = SezimalDictionary({})

                if event.date.dcc_day not in events[event.date.dcc_month]:
                    events[event.date.dcc_month][event.date.dcc_day] = SezimalList([])

                events[event.date.dcc_month][event.date.dcc_day].append(event)


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/calendar')
def sezimal_calendar_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/calendário', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/kalendaryu', code=302)

    return redirect('/en/shastadari/calendar', code=302)

@sitemapper.include(lastmod='2025-02-19', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/calendar')
def sezimal_calendar_en_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'en':
        hemisphere = locale.DEFAULT_HEMISPHERE
        locale = sezimal_locale('en-gb')
        locale.DEFAULT_HEMISPHERE = hemisphere

    locale.calendar_displayed = 'SYM'
    locale.use_first_weekday = False
    locale.base = 10
    locale.format_token = ''
    locale.SHOW_HOLIDAYS = 'ISO'
    locale.GROUP_SEPARATOR = '󱹭'

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = ''
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT.replace('%5Y', '13󱹭%5Y').replace('%↋Y', '13󱹭%↋Y').replace('%Y', '13󱹭%Y'), locale)
    context['sezimal_today_full'] = now.format(locale.DATE_LONG_FORMAT, locale)

    context['events'] = _calendar_events(locale, now.year, context) or {}

    return sezimal_render_template(
        'calendar_en.html',
        **context,
    )

@sitemapper.include(lastmod='2025-02-19', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/calendário')
def sezimal_calendar_pt_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'pt':
        hemisphere = locale.DEFAULT_HEMISPHERE
        locale = sezimal_locale('pt-br')
        locale.DEFAULT_HEMISPHERE = hemisphere

    locale.calendar_displayed = 'SYM'
    locale.use_first_weekday = False
    locale.base = 10
    locale.format_token = ''
    locale.SHOW_HOLIDAYS = 'ISO'
    locale.GROUP_SEPARATOR = '󱹭'

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = ''
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT.replace('%5Y', '13󱹭%5Y').replace('%↋Y', '13󱹭%↋Y').replace('%Y', '13󱹭%Y'), locale)
    context['sezimal_today_full'] = now.format(locale.DATE_LONG_FORMAT, locale)

    context['events'] = _calendar_events(locale, now.year, context) or {}

    return sezimal_render_template(
        'calendar_pt.html',
        **context,
    )

@sitemapper.include(lastmod='2025-02-19', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/kalendaryu')
def sezimal_calendar_bz_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'bz':
        hemisphere = locale.DEFAULT_HEMISPHERE
        locale = sezimal_locale('bz-br')
        locale.DEFAULT_HEMISPHERE = hemisphere

    locale.calendar_displayed = 'SYM'
    locale.use_first_weekday = False
    locale.base = 10
    locale.format_token = ''
    locale.SHOW_HOLIDAYS = 'ISO'
    locale.GROUP_SEPARATOR = '󱹭'

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = ''
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT.replace('%5Y', '13󱹭%5Y').replace('%↋Y', '13󱹭%↋Y').replace('%Y', '13󱹭%Y'), locale)
    context['sezimal_today_full'] = now.format(locale.DATE_LONG_FORMAT, locale)

    locale.HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        ('EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        # ('EASTER-114', '🎉\ufe0f🎭\ufe0f Kwarta-fera di Sinzas'),
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Paxawn di Kristu'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Paskwa'),
        ('EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Konfraternizasawn Universaw'),
        ('05-01', '🐝\ufe0f🐜\ufe0f Dia du Trabalyu'),
        ('14-20', '⛪\ufe0f👸🏾\ufe0f Nòsa Seỹòra Aparesida'),
        ('15-02', '🪦\ufe0f🕊\ufe0f️  Finadus'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️  Véspera di Nataw'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Nataw'),
        ('20-55', '🍾\ufe0f🎆\ufe0f Véspera di Anu Novu'),

        #
        # National Holidays
        # that have a year of reference;
        # There are 2 ways of dealing with them:
        #     1. converting the original date to the Sezimal calendar
        #     2. using the original month and day without converting the calendar
        #
        # Using 2 here, but leaving 1 commented for reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using #i as a format tag
        #
        # ('212_144-04-32', '🇧🇷\ufe0f🔺\ufe0f Tiradentis'),                 # sábadu  212_144-04-32 ~ 1792-04-21_dec
        # ('212_540-11-10', '🪖\ufe0f📜\ufe0f Revolusawn di 1932 (1̈5̈0̄/540)'),   # sábadu  212_540-11-10 ~ 1932-07-09_dec
        # ('212_234-13-10', '🇧🇷\ufe0f🕊\ufe0f️ Independensya du Braziw'),    # sábadu  212_234-13-10 ~ 1822-09-07_dec
        # ('212_425-15-31', '🇧🇷\ufe0f📜\ufe0f Proklamasawn da Repúblika'),  # sesta   212_425-15-31 ~ 1889-11-15_dec
        # ('211_503-15-33', '👨🏾\ufe0f Konsyensya Negra'),             # dumingu 211_503-15-33 ~ 1695-11-20_dec

        ('212_144-04-33', '🇧🇷\ufe0f🔺\ufe0f Tiradentis'),                      # dumingu, 04-33 ~ 04-21_dec
        ('212_540-11-13', '🪖\ufe0f📜\ufe0f Revolusawn di 1932 (1̈5̈0̄/540) (#i)'),   # tersa,   11-13 ~ 07-09_dec
        ('212_234-13-11', '🇧🇷\ufe0f🕊\ufe0f️ Independensya du Braziw (#i)'),    # dumingu, 13-11 ~ 09-07_dec
        ('212_425-15-23', '🇧🇷\ufe0f📜\ufe0f Proklamasawn da Repúblika (#i)'),  # sigunda, 15-23 ~ 11-15_dec
        ('211_503-15-32', '👨🏾\ufe0f Konsyensya Negra'),                  # sábadu,  15-32 ~ 11-20_dec
    ]
    locale.HOLIDAYS_OTHER_CALENDAR = []

    context['events'] = _calendar_events(locale, now.year, context) or {}

    return sezimal_render_template(
        'calendar_bz.html',
        **context,
    )


@app.route('/calendar/event-list-window', methods=['POST'])
def api_event_list_window():
    dados = json.loads(request.data.decode('utf-8'))
    dados['base'] = int(dados['base'])

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    locale = _prepare_locale(locale, dados)

    gray_scale = dados['theme'] == 'GRAY'
    format_token = dados['format_token'] or ''

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    if 'date' in dados and dados['date']:
        date = SezimalDateTime.combine(SezimalDate(dados['date']), now.time, locale.DEFAULT_TIME_ZONE)

    else:
        date = now

    context = _calendar_context(locale, date, gray_scale)
    context['locale'] = locale
    context['now'] = now
    context['base'] = dados['base']
    context['format_token'] = (dados['format_token'] or '')

    script = ''

    view = sezimal_render_template(
        f'''calendar_view_event_list.html''',
        **context,
    )

    if '<script>' in view:
        view, script = view.split('<script>')
        script = script.split('</script>')[0]

    res = {
        'date_to_store': str(date.date),
        'view': view,
        'script_text': script,
    }

    return jsonify(res)


@app.route('/calendar/event-window', methods=['POST'])
def api_event_window():
    dados = json.loads(request.data.decode('utf-8'))
    dados['base'] = int(dados['base'])

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    locale = _prepare_locale(locale, dados)

    gray_scale = dados['theme'] == 'GRAY'
    format_token = dados['format_token'] or ''

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    if 'date' in dados and dados['date']:
        date = SezimalDateTime.combine(SezimalDate(dados['date']), now.time, locale.DEFAULT_TIME_ZONE)

    else:
        date = now

    context = _calendar_context(locale, date, gray_scale)
    context['locale'] = locale
    context['now'] = now
    context['base'] = dados['base']
    context['format_token'] = (dados['format_token'] or '')
    context['event'] = SezimalEvent()

    script = ''

    view = sezimal_render_template(
        f'''calendar_view_event.html''',
        **context,
    )

    if '<script>' in view:
        view, script = view.split('<script>')
        script = script.split('</script>')[0]

    res = {
        'date_to_store': str(date.date),
        'view': view,
        'script_text': script,
    }

    return jsonify(res)


@app.route('/calendar/build-date-string', methods=['POST'])
def api_calendar_build_date_string() -> dict:
    dados = json.loads(request.data.decode('utf-8'))
    # dados['base'] = 14 # int(dados['base'])
    dados['base'] = int(dados['base'])
    dados['easter_days'] = int(dados['easter_days'] or 0)

    base = dados['base']
    format_token = dados['format_token'] or ''

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    locale = _prepare_locale(locale, dados)

    date_string = dados['calendar_type']
    date_error = ''
    time_error = ''
    reference_year = SezimalInteger(213_212)

    if 'EASTER' in date_string:
        if dados['easter_days']:
            date_string += dados['easter_sign'].replace('_', '+') or '+'

            try:
                if base == 10 or base == 100:
                    date_string += str(SezimalInteger(dados['easter_days']))
                elif base == 14:
                    date_string += str(SezimalInteger(Decimal(dados['easter_days'])))
                elif base == 20:
                    date_string += str(SezimalInteger(Dozenal(dados['easter_days'])))
            except:
                date_error = 'Invalid input for the number of days from Easter'
                res = {
                    'date_error': date_error,
                    'time_error': time_error,
                }
                return jsonify(res)

    else:
        date_string += dados['year_sign'].replace('_', '+') or '+'

        if dados['year']:
            # try:
            if True:
                if 'SYM' in date_string:
                    if base == 10 or base == 100:
                        if len(dados['year']) <= 3:
                            dados['year'] = SezimalInteger(dados['year'])
                            dados['year'] += 213_000
                        else:
                            dados['year'] = SezimalInteger(dados['year'])

                        dados['year'] = int((dados['year'] - 200_000).decimal)

                    elif base == 14:
                        dados['year'] = int(dados['year'])

                    elif base == 20:
                        dados['year'] = int(DozenalInteger(dados['year']).decimal)

                else:
                    dados['year'] = int(dados['year'])

                if dados['year'] <= 0:
                    date_error = 'Invalid year'
                    res = {
                        'date_error': date_error,
                        'time_error': time_error,
                    }
                    return jsonify(res)

            # except:
            #     date_error = 'Invalid date'
            #     res = {
            #         'date_error': date_error,
            #         'time_error': time_error,
            #     }
            #     return jsonify(res)

            date_string += str(dados['year']).zfill(4) + '-'

        date_string += dados['month'] + '-'
        date_string += dados['day']

        if dados['weekday_sign'] in '+-' and dados['weekday'] != '_':
            date_string += dados['weekday_sign']
            date_string += dados['weekday']

            if dados['weekday_number'] in '1234':
                date_string += '_' + dados['weekday_number']

    try:
        ordinal_date, (year, month, day), age, original_date = \
            other_calendar_date_to_ordinal_date(date_string, reference_year, return_original_date=True)
    except:
        date_error = locale.CALENDAR_DATE_ERROR.format(
            calendar_type=locale.CALENDAR_TYPE[dados['calendar_type']]
        )
        res = {
            'date_error': date_error,
            'time_error': time_error,
        }
        return jsonify(res)

    date = SezimalDate.from_ordinal_date(ordinal_date)

    if original_date:
        original_date = SezimalDate.from_ordinal_date(original_date)

    if dados['calendar_type'] == 'SYM':
        year -= 200_000

    date_format = locale.DATE_TEXT_SHORT_MONTH_FORMAT
    month_names = locale.MONTH_ABBREVIATED_NAME

    if 'JEW' in date_string or 'ISR' in date_string:
        month_names = locale.JEWISH_CALENDAR_MONTH_ABBREVIATED_NAME
    elif 'HIJ' in date_string:
        month_names = locale.HIJRI_CALENDAR_MONTH_ABBREVIATED_NAME
    elif 'IRN' in date_string:
        month_names = locale.IRANIAN_CALENDAR_MONTH_ABBREVIATED_NAME
    elif 'IND' in date_string:
        month_names = locale.INDIAN_CALENDAR_MONTH_ABBREVIATED_NAME
    elif 'SYM' in date_string and base != 10:
        year -= 200_000

    if 'ISO' in date_string or 'SYM' in date_string:
        this_year = ''

    elif locale.DATE_ENDIANNESS == 'B':
        this_year = str(year).zfill(4) + locale.DATE_SEPARATOR + month_names[int(month) - 1] + locale.DATE_SEPARATOR + str(day).zfill(2)
    elif locale.DATE_ENDIANNESS == 'L':
        this_year = str(day).zfill(2) + locale.DATE_SEPARATOR + month_names[int(month) - 1] + locale.DATE_SEPARATOR + str(year).zfill(4)
    else:
        this_year = month_names[int(month) - 1] + locale.DATE_SEPARATOR + str(day).zfill(2) + locale.DATE_SEPARATOR + str(year).zfill(4)

    res = {
        'date_string': date_string,
        'date_error': date_error,
        'time_error': time_error,
        'date': str(date),
        'original_date': str(original_date) if original_date else '',
        'this_year': this_year,
        'year': int(year),
        'month': int(month),
        'day': int(day),
        'age': int(age),
        'date_formatted': date.format(date_format, locale),
        'date_iso_formatted': date.format(locale.ISO_DATE_TEXT_SHORT_MONTH_FORMAT, locale),
        'original_date_formatted': original_date.format(date_format, locale) if original_date else '',
        'original_date_iso_formatted': original_date.format(locale.ISO_DATE_TEXT_SHORT_MONTH_FORMAT, locale) if original_date else '',
    }

    date_this_year = ''

    if dados['year'] and 'EASTER' not in date_string:
        if locale.LANG == 'pt':
            date_this_year += 'Data original'
        elif locale.LANG == 'bz':
            date_this_year += 'Data orijinaw'
        else:
            date_this_year += 'Original date'

        date_this_year += ' (' + locale.WEEKDAY_NAME[int(original_date.weekday) - 1] + ')'
        date_this_year += '<br/>'

        if dados['calendar_type'] not in ('SEZ', 'SYM'):
            date_this_year += '    • '

            if base == 10 or base == 100:
                date_this_year += locale.CALENDAR_TYPE['SEZ']
            else:
                date_this_year += locale.CALENDAR_TYPE['SYM']

            date_this_year += ': ' + res['original_date_formatted']

        if dados['calendar_type'] != 'ISO':
            if dados['calendar_type'] not in ('SEZ', 'SYM'):
                date_this_year += '<br/>'

            date_this_year += '    • '
            date_this_year += 'ISO: ' + res['original_date_iso_formatted']

    if (not original_date) or (str(original_date) != str(date)):
        date_this_year += '<br/>'

        if locale.LANG == 'pt':
            date_this_year += 'Data este ano'
        elif locale.LANG == 'bz':
            date_this_year += 'Data esi anu'
        else:
            date_this_year += 'Date this year'

        date_this_year += ' (' + locale.WEEKDAY_NAME[int(date.weekday) - 1] + ')'
        date_this_year += '<br/>'

        if dados['calendar_type'] not in ('ISO', 'ISO+EASTER', 'SEZ', 'SEZ+EASTER', 'SYM', 'SYM+EASTER'):
            date_this_year += '    • '
            date_this_year += locale.CALENDAR_TYPE[dados['calendar_type']]
            date_this_year += ': ' + res['this_year']
            date_this_year += '<br/>'

        if dados['calendar_type'] not in ('SEZ', 'SYM'):
            date_this_year += '    • '

            if base == 10 or base == 100:
                date_this_year += locale.CALENDAR_TYPE['SEZ']
            else:
                date_this_year += locale.CALENDAR_TYPE['SYM']

            date_this_year += ': ' + res['date_formatted']

        if dados['calendar_type'] != 'ISO':
            if dados['calendar_type'] not in ('SEZ', 'SYM'):
                date_this_year += '<br/>'

            date_this_year += '    • '
            date_this_year += 'ISO: ' + res['date_iso_formatted']

    res['date_this_year'] = date_this_year

    return jsonify(res)


@app.route('/now')
def now_route() -> Response:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
        base = locale.base
        format_token = locale.format_token
        theme = locale.theme
        mobile = locale.mobile
    else:
        locale = sezimal_locale(browser_preferred_locale())
        hour_format = locale.HOUR_FORMAT
        base = 10
        format_token = ''
        mobile = False
        theme = 'FULL_COLOR'

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)
    date = now

    context = _calendar_context(locale, date, gray_scale=theme == 'GRAY')
    context['locale'] = locale
    context['now'] = now
    context['base'] = int(base)
    context['format_token'] = format_token
    context['hour_format'] = locale.HOUR_FORMAT
    context['mobile'] = mobile

    if locale.calendar_displayed == 'SYM':
        context['events'] = _calendar_events(locale, date.year, context) or {}
    elif locale.calendar_displayed == 'ISO':
        context['events'] = _calendar_events(locale, date.gregorian_year, context) or {}
    elif locale.calendar_displayed == 'DCC':
        context['events'] = _calendar_events(locale, date.dcc_year, context) or {}

    return sezimal_render_template(
        'now.html',
        sezimal_month_number=date.month,
        **context,
    )


def _prepare_locale_from_cookie():
    cookie = urllib.parse.unquote(request.cookies['sezimal'])

    show_seconds = 'true'
    calendar_displayed = 'SYM'
    locale_first_weekday = 'false'
    local_time_zone = None

    try:
            base, format_token, locale, time_zone, hour_format, hemisphere, theme, mobile, show_holiday, show_seconds, calendar_displayed, locale_first_weekday, local_time_zone = cookie.split('|')

    except:
        try:
            base, format_token, locale, time_zone, hour_format, hemisphere, theme, mobile, show_holiday, show_seconds, calendar_displayed, locale_first_weekday = cookie.split('|')
        except:
            try:
                base, format_token, locale, time_zone, hour_format, hemisphere, theme, mobile, show_holiday, show_seconds, calendar_displayed = cookie.split('|')
            except:
                try:
                    base, format_token, locale, time_zone, hour_format, hemisphere, theme, mobile, show_holiday = cookie.split('|')
                except:
                    base, format_token, locale, time_zone, hour_format, hemisphere, theme, mobile = cookie.split('|')
                    show_holiday = 'ISO_SEZ_SYM'

    locale = sezimal_locale(locale)

    if calendar_displayed == 'true' or calendar_displayed == 'null':
        calendar_displayed = 'SYM'
    elif calendar_displayed == 'false':
        calendar_displayed = 'ISO'

    dados = {
        'base': base,
        'format_token': format_token,
        'locale': locale,
        'time_zone': time_zone,
        'hour_format': hour_format,
        'hemisphere': hemisphere,
        'theme': theme,
        'mobile': mobile,
        'show_holiday': show_holiday,
        'show_seconds': show_seconds,
        'calendar_displayed': calendar_displayed,
        'locale_first_weekday': locale_first_weekday,
        'local_time_zone': local_time_zone or time_zone,
    }

    locale = _prepare_locale(locale, dados)

    return locale


def _prepare_locale(locale, dados):
    base = int(dados['base'])
    format_token = dados['format_token']

    if dados['time_zone'] != 'locale':
        locale.DEFAULT_TIME_ZONE = dados['time_zone']

    if dados['hemisphere'] != 'locale':
        locale.DEFAULT_HEMISPHERE = dados['hemisphere']

    if dados['hour_format'] == 'iso':
        locale.to_iso_format()
    elif dados['hour_format'] == '24h':
        if locale.DIGITS:
            locale.ISO_TIME_FORMAT = '%?H:%?M:%?S'
        else:
            locale.ISO_TIME_FORMAT = '%H:%M:%S'
    elif dados['hour_format'] == '12h':
        if locale.DIGITS:
            locale.ISO_TIME_FORMAT = '%?I:%?M:%?S %P'
        else:
            locale.ISO_TIME_FORMAT = '%I:%M:%S %P'

    if base == 10:
        locale.to_short_year_format()

        if '!' in format_token:
            locale.to_sezimal_digits()

        if 'c' in format_token:
            locale.to_astronomical_names()

    elif base == 14:
        locale.to_decimal_base()

        if 'c' in format_token:
            locale.to_astronomical_names()

    elif base == 20:
        locale.to_dozenal_base()

        if 'c' in format_token:
            locale.to_astronomical_names()

    elif base == 100:
        if format_token == 'Z':
            locale.to_niftimal_text_base()
        else:
            locale.to_niftimal_base(sezimal_digits='!' in format_token)

        if 'c' in format_token:
            locale.to_astronomical_names()

    if 'show_holiday' in dados:
        locale.SHOW_HOLIDAYS = dados['show_holiday']
    else:
        locale.SHOW_HOLIDAYS = 'ISO'

    locale.mobile = dados['mobile'] == 'true'

    locale.format_token = dados['format_token']
    locale.base = int(dados['base'])
    locale.theme = dados['theme']

    locale.show_seconds = dados['show_seconds'] == 'true'
    locale.use_first_weekday = dados['locale_first_weekday'] == 'true'
    locale.calendar_displayed = dados['calendar_displayed'] or 'SYM'

    if 'local_time_zone' in dados:
        locale.LOCAL_TIME_ZONE = dados['local_time_zone']
    else:
        locale.LOCAL_TIME_ZONE = locale.DEFAULT_TIME_ZONE

    return locale


def _now_icon(text: str, locale) -> str:
    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    if locale.calendar_displayed == 'DCC':
        if now.dcc_weekday in (0, 5):
            text = text.replace('#2a7fff', '#d40000')

    elif now.weekday >= 10:
        text = text.replace('#2a7fff', '#d40000')

    if locale.base == 10 or locale.base == 100:
        locale.to_short_year_format()
        uta_angle = now.time.as_days
        posha_angle = (now.time.as_days * 100) - round(now.time.as_days * 100, 0)
        agrima_angle = (now.time.as_days * 10_000) - round(now.time.as_days * 10_000, 0)
        uta_angle = round(uta_angle * 1400, 0).decimal
        posha_angle = round(posha_angle * 1400, 0).decimal
        agrima_angle = round(agrima_angle * 1400, 0).decimal

    elif locale.base == 14:
        locale.to_decimal_base()
        text = text.replace('id="sezimal_marks" style="display: inline;"', 'id="sezimal_marks" style="display: none;"')
        text = text.replace('id="dozenal_marks" style="display: none;"', 'id="dozenal_marks" style="display: inline;"')
        text = text.replace('dur="66667ms"', 'dur="60000ms"')
        text = text.replace('dur="2400s"', 'dur="3600s"')
        text = text.replace('dur="86400s"', 'dur="43200s"')

        hour = now.iso_date_time.hour

        if now.iso_date_time.hour >= 12:
            hour -= 12

        hour /= 12
        hour += now.iso_date_time.minute / 60 / 12
        hour += now.iso_date_time.second / 60 / 60 / 12

        minute = now.iso_date_time.minute / 60
        minute += now.iso_date_time.second / 60 / 60

        second = now.iso_date_time.second / 60

        uta_angle = round(hour * 360, 0) + 180
        posha_angle = round(minute * 360, 0) + 180
        agrima_angle = round(second * 360, 0) + 180

    elif locale.base == 20:
        locale.to_dozenal_base()
        text = text.replace('id="sezimal_marks" style="display: inline;"', 'id="sezimal_marks" style="display: none;"')
        text = text.replace('id="dozenal_marks" style="display: none;"', 'id="dozenal_marks" style="display: inline;"')
        text = text.replace('dur="66667ms"', 'dur="50s"')
        text = text.replace('dur="2400s"', 'dur="600s"')
        text = text.replace('dur="86400s"', 'dur="7200s"')

        uta_angle = now.time.as_days
        posha_angle = (now.time.as_days * Dozenal('100')) - round(now.time.as_days * Dozenal('100'), 0)
        agrima_angle = (now.time.as_days * Dozenal('1000')) - round(now.time.as_days * Dozenal('1000'), 0)
        uta_angle = round(uta_angle * 1400, 0).decimal
        posha_angle = round(posha_angle * 1400, 0).decimal
        agrima_angle = round(agrima_angle * 1400, 0).decimal

    if locale.calendar_displayed == 'DCC':
        if locale.base in (14, 20):
            date_parts = [
                now.format('&' + locale.format_token + '>Y', locale),
                now.format('&' + locale.format_token + 'M', locale),
                now.format('&-wM‐&-w', locale),
            ]
        else:
            date_parts = [
                now.format('&' + locale.format_token + '>Y', locale),
                now.format('&' + locale.format_token + 'M', locale),
                now.format('&' + locale.format_token + '-d', locale),
            ]

    else:
        date_parts = now.format(locale.DATE_FORMAT.replace('d', '-d').replace('m', 'M'), locale).split(locale.DATE_SEPARATOR)

    text = text.replace(
        'id="date-1">213 212',
        'id="date-1">' + date_parts[0],
    )
    text = text.replace(
        'id="date-2">11',
        'id="date-2">' + date_parts[1],
    )
    text = text.replace(
        'id="date-3">01',
        'id="date-3">' + date_parts[2],
    )
    text = text.replace(
        'id="face_uta" transform="rotate(300,216,216)"',
        f'id="face_uta" transform="rotate({uta_angle},216,216)"',
    )
    text = text.replace(
        'id="face_posha" transform="rotate(60,216,216)"',
        f'id="face_posha" transform="rotate({posha_angle},216,216)"',
    )
    text = text.replace(
        'id="face_agrima" transform="rotate(150,216,216)"',
        f'id="face_agrima" transform="rotate({agrima_angle + 10},216,216)"',
    )

    return text


@app.route('/now/<string:when>/icon-mono.svg')
@app.route('/now/<string:when>/icon-<string:size>.svg')
@app.route('/now/icon.svg')
@app.route('/now/icon-<string:size>.svg')
def now_icon(when: str = None, size: str = None) -> str:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale.base = 10

    text = open('static/img/now-icon.svg').read()

    if size and size != 'any':
        text = text.replace('width="1632.7559"', f'width="{size}"')
        text = text.replace('height="1632.7559"', f'height="{size}"')

    return Response(_now_icon(text, locale), mimetype='image/svg+xml')


@app.route('/now/manifest.json')
def now_manifest() -> str:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale.base = 10

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    text = sezimal_render_template(
        'manifest_now.json',
        locale=locale,
        now=now,
    )

    return jsonify(json.loads(text))


@app.route('/now/now_service.js')
def now_service_js() -> Response:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale.base = 10

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    text = sezimal_render_template(
        'now_service.js',
        locale=locale,
        now=now,
    )

    return Response(text, mimetype='application/javascript')


@app.route('/today/<string:when>/icon-mono.svg')
@app.route('/today/<string:when>/icon-<string:size>.svg')
@app.route('/today/icon.svg')
@app.route('/today/icon-<string:size>.svg')
def today_icon(when: str = None, size: str = None) -> str:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
        base = locale.base
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale.base = 10
        base = 10

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    text = open('static/img/today-icon.svg').read()

    if size and size != 'any':
        text = text.replace('width="1632.7559"', f'width="{size}"')
        text = text.replace('height="1632.7559"', f'height="{size}"')

    if locale.calendar_displayed == 'DCC':
        if now.dcc_weekday in (0, 5):
            text = text.replace('#2a7fff', '#d40000')

    elif now.weekday >= 10:
        text = text.replace('#2a7fff', '#d40000')

    if base == 10 or base == 100:
        if locale.calendar_displayed == 'DCC':
            day = str(now.date.dcc_day)
            month = str(now.date.dcc_month)
        else:
            day = str(now.date.day)
            month = str(now.date.month)

    elif base == 14:
        if locale.calendar_displayed == 'DCC':
            day = str(now.date.dcc_week) + str(now.date.dcc_weekday)
            month = str(now.date.dcc_month.decimal)
        else:
            day = str(now.date.day.decimal)
            month = str(now.date.month.decimal)

    else:
        if locale.calendar_displayed == 'DCC':
            day = str(now.date.dcc_week) + str(now.date.dcc_weekday)
            month = str(now.date.dcc_month.dozenal)
        else:
            day = str(now.date.day.dozenal)
            month = str(now.date.month.dozenal)

    text = text.replace('>20</tspan>', '>' + month.rjust(2, ' ') + 'm</tspan>')
    text = text.replace('>55</tspan>', '>' + day.rjust(2, ' ') + '</tspan>')
    text = text.replace('>' + month.rjust(2, ' ')+ 'm</tspan>', '>' + month.rjust(2, ' ') + '</tspan>')

    return Response(text, mimetype='image/svg+xml')


@app.route('/today/manifest.json')
def today_manifest() -> str:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale.base = 10

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    text = sezimal_render_template(
        'manifest_today.json',
        locale=locale,
        now=now,
    )

    return jsonify(json.loads(text))


@app.route('/today/today_service.js')
def today_service_js() -> Response:
    if 'sezimal' in request.cookies:
        locale = _prepare_locale_from_cookie()
    else:
        locale = sezimal_locale(browser_preferred_locale())
        locale.base = 10

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    text = sezimal_render_template(
        'today_service.js',
        locale=locale,
        now=now,
    )

    return Response(text, mimetype='application/javascript')


@app.route('/now/process', methods=['POST'])
def api_now_process():
    dados = json.loads(request.data.decode('utf-8'))

    dados['base'] = int(dados['base'])
    base = dados['base']
    format_token = dados['format_token'] or ''

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    gray_scale = dados['theme'] == 'GRAY'

    locale = _prepare_locale(locale, dados)

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)
    date = now

    context = _calendar_context(locale, date, gray_scale)
    context['locale'] = locale
    context['now'] = now
    context['base'] = dados['base']
    context['format_token'] = (dados['format_token'] or '')
    context['mobile'] = dados['mobile']

    if locale.DIGITS:
        context['format_token'] += '?'

    if dados['hour_format'] != 'locale':
        locale.HOUR_FORMAT = dados['hour_format']

    if locale.calendar_displayed == 'SYM':
        context['events'] = _calendar_events(locale, date.year, context) or {}
    elif locale.calendar_displayed == 'ISO':
        context['events'] = _calendar_events(locale, date.gregorian_year, context) or {}
    elif locale.calendar_displayed == 'DCC':
        context['events'] = _calendar_events(locale, date.dcc_year, context) or {}

    script = ''

    view = sezimal_render_template(
        f'''calendar_view_now.html''',
        **context,
    )

    if '<script type="text/javascript" id="view_script">' in view:
        view, script = view.split('<script type="text/javascript" id="view_script">')
        script = script.split('</script>')[0]

    res = {
        'view': view,
        'script_text': script,
    }

    return jsonify(res)


@app.route('/weather/process', methods=['POST'])
def api_weather_process():
    dados = json.loads(request.data.decode('utf-8'))

    dados['base'] = int(dados['base'])
    base = dados['base']
    format_token = dados['format_token'] or ''

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    gray_scale = dados['theme'] == 'GRAY'

    locale = _prepare_locale(locale, dados)

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)
    date = now

    context = _calendar_context(locale, date, gray_scale)
    context['locale'] = locale
    context['now'] = now
    context['base'] = dados['base']
    context['format_token'] = (dados['format_token'] or '')
    context['mobile'] = dados['mobile']
    context['weather'] = None

    if 'latitude' in dados and 'longitude' in dados \
        and dados['latitude'] and dados['longitude']:
        weather = SezimalWeather(
            locale,
            locale.DEFAULT_TIME_ZONE,
            use_last_reading=False,
        )
        weather.get_openweathermap_conditions(
            latitude=dados['latitude'],
            longitude=dados['longitude'],
        )
        context['weather'] = weather

    if locale.DIGITS:
        context['format_token'] += '?'

    if dados['hour_format'] != 'locale':
        locale.HOUR_FORMAT = dados['hour_format']

    view = sezimal_render_template(
        f'''calendar_view_weather.html''',
        **context,
    )

    if '-metric' in dados['locale']:
        locale.DECIMAL_TEMPERATURE = '°C'
        locale.DECIMAL_SPEED = 'km/h'

    decimal_weather = ' ―  ' + locale.format_decimal_number(
        round(sezimal_to_decimal_unit(
            weather.temperature,
            'tap', locale.DECIMAL_TEMPERATURE
        ).decimal, 1),
        decimal_places=1
    ) + ' ' + locale.DECIMAL_TEMPERATURE

    res = {
        'view': view,
        'decimal_weather': decimal_weather
    }

    return jsonify(res)

# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/day-count-calendar')
def sezimal_day_count_calendar_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/calendário-quantos-dias', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/kalendaryu-kwantus-dias', code=302)

    return redirect('/en/shastadari/day-count-calendar', code=302)

@sitemapper.include(lastmod='2025-02-19', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/day-count-calendar')
def sezimal_day_count_calendar_en_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'en':
        hemisphere = locale.DEFAULT_HEMISPHERE
        locale = sezimal_locale('en-gb')
        locale.DEFAULT_HEMISPHERE = hemisphere

    locale.calendar_displayed = 'DCC'
    locale.use_first_weekday = False
    locale.base = 10
    locale.format_token = 'c'
    locale.SHOW_HOLIDAYS = 'ISO'
    locale.GROUP_SEPARATOR = '󱹭'
    locale.DCC_YEAR_FORMAT = locale.DCC_YEAR_FORMAT.replace('>', '').replace('&Y', '213󱹭&Y')

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = 'c'
    context['calendar_presentation'] = True
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT.replace('%5Y', '13󱹭%5Y').replace('%↋Y', '13󱹭%↋Y').replace('%Y', '13󱹭%Y'), locale)

    context['events'] = _calendar_events(locale, now.year, context) or {}

    return sezimal_render_template(
        'calendar_day_count_en.html',
        **context,
    )

@sitemapper.include(lastmod='2025-02-19', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/calendário-quantos-dias')
def sezimal_day_count_calendar_pt_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'pt':
        hemisphere = locale.DEFAULT_HEMISPHERE
        locale = sezimal_locale('pt-br')
        locale.DEFAULT_HEMISPHERE = hemisphere

    locale.calendar_displayed = 'DCC'
    locale.use_first_weekday = False
    locale.base = 10
    locale.format_token = 'c'
    locale.SHOW_HOLIDAYS = 'ISO'
    locale.GROUP_SEPARATOR = '󱹭'
    locale.DCC_YEAR_FORMAT = locale.DCC_YEAR_FORMAT.replace('>', '')

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = 'c'
    context['calendar_presentation'] = True
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT.replace('%5Y', '13󱹭%5Y').replace('%↋Y', '13󱹭%↋Y').replace('%Y', '13󱹭%Y'), locale)

    context['events'] = _calendar_events(locale, now.year, context) or {}

    return sezimal_render_template(
        'calendar_day_count_pt.html',
        **context,
    )

@sitemapper.include(lastmod='2025-02-19', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/kalendaryu-kwantus-dias')
def sezimal_day_count_calendar_bz_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'bz':
        hemisphere = locale.DEFAULT_HEMISPHERE
        locale = sezimal_locale('bz-br')
        locale.DEFAULT_HEMISPHERE = hemisphere

    locale.calendar_displayed = 'DCC'
    locale.use_first_weekday = False
    locale.base = 10
    locale.format_token = 'c'
    locale.SHOW_HOLIDAYS = 'ISO'
    locale.GROUP_SEPARATOR = '󱹭'
    locale.DCC_YEAR_FORMAT = locale.DCC_YEAR_FORMAT.replace('>', '').replace('&Y', '213󱹭&Y')

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    locale.HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        ('EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        # ('EASTER-114', '🎉\ufe0f🎭\ufe0f Kwarta-fera di Sinzas'),
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Paxawn di Kristu'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Paskwa'),
        ('EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Konfraternizasawn Universaw'),
        ('05-01', '🐝\ufe0f🐜\ufe0f Dia du Trabalyu'),
        ('14-20', '⛪\ufe0f👸🏾\ufe0f Nòsa Seỹòra Aparesida'),
        ('15-02', '🪦\ufe0f🕊\ufe0f️  Finadus'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️  Véspera di Nataw'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Nataw'),
        ('20-55', '🍾\ufe0f🎆\ufe0f Véspera di Anu Novu'),

        #
        # National Holidays
        # that have a year of reference;
        # There are 2 ways of dealing with them:
        #     1. converting the original date to the Sezimal calendar
        #     2. using the original month and day without converting the calendar
        #
        # Using 2 here, but leaving 1 commented for reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using #i as a format tag
        #
        # ('212_144-04-32', '🇧🇷\ufe0f🔺\ufe0f Tiradentis'),                 # sábadu  212_144-04-32 ~ 1792-04-21_dec
        # ('212_540-11-10', '🪖\ufe0f📜\ufe0f Revolusawn di 1932 (1̈5̈0̄/540)'),   # sábadu  212_540-11-10 ~ 1932-07-09_dec
        # ('212_234-13-10', '🇧🇷\ufe0f🕊\ufe0f️ Independensya du Braziw'),    # sábadu  212_234-13-10 ~ 1822-09-07_dec
        # ('212_425-15-31', '🇧🇷\ufe0f📜\ufe0f Proklamasawn da Repúblika'),  # sesta   212_425-15-31 ~ 1889-11-15_dec
        # ('211_503-15-33', '👨🏾\ufe0f Konsyensya Negra'),             # dumingu 211_503-15-33 ~ 1695-11-20_dec

        ('212_144-04-33', '🇧🇷\ufe0f🔺\ufe0f Tiradentis'),                      # dumingu, 04-33 ~ 04-21_dec
        ('212_540-11-13', '🪖\ufe0f📜\ufe0f Revolusawn di 1932 (1̈5̈0̄/540) (#i)'),   # tersa,   11-13 ~ 07-09_dec
        ('212_234-13-11', '🇧🇷\ufe0f🕊\ufe0f️ Independensya du Braziw (#i)'),    # dumingu, 13-11 ~ 09-07_dec
        ('212_425-15-23', '🇧🇷\ufe0f📜\ufe0f Proklamasawn da Repúblika (#i)'),  # sigunda, 15-23 ~ 11-15_dec
        ('211_503-15-32', '👨🏾\ufe0f Konsyensya Negra'),                  # sábadu,  15-32 ~ 11-20_dec
    ]
    locale.HOLIDAYS_OTHER_CALENDAR = []

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = 'c'
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DCC_DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT.replace('%5Y', '13󱹭%5Y').replace('%↋Y', '13󱹭%↋Y').replace('%Y', '13󱹭%Y'), locale)
    context['sezimal_today_full'] = now.format(locale.DCC_DATE_LONG_FORMAT, locale)

    context['events'] = _calendar_events(locale, now.year, context) or {}

    return sezimal_render_template(
        'calendar_bz.html',
        **context,
    )


def _create_store_events(itens: list = None):
    year_range = (213_212, 213_221)

    if itens is None:
        itens = (
        'pt-BR|America/Sao_Paulo',
        'bz|America/Sao_Paulo',
        'eo-BR|America/Sao_Paulo',
        'en-BR|America/Sao_Paulo',

        'pt-BR|Natural/NT4-03',
        'bz|Natural/NT4-03',
        'eo-BR|Natural/NT4-03',
        'en-BR|Natural/NT4-03',

        'pt-BR|Natural/NT6-03',
        'bz|Natural/NT6-03',
        'eo-BR|Natural/NT6-03',
        'en-BR|Natural/NT6-03',

        'pt-BR|Sezimal/SPM-0530',
        'bz|Sezimal/SPM-0530',
        'eo-BR|Sezimal/SPM-0530',
        'en-BR|Sezimal/SPM-0530',

        'pt-BR|Sezimal/SPM-10',
        'bz|Sezimal/SPM-10',
        'eo-BR|Sezimal/SPM-10',
        'en-BR|Sezimal/SPM-10',

        'pt-BR|Sezimal/NT10-0530',
        'bz|Sezimal/NT10-0530',
        'eo-BR|Sezimal/NT10-0530',
        'en-BR|Sezimal/NT10-0530',

        'pt-BR|Sezimal/NT10-10',
        'bz|Sezimal/NT10-10',
        'eo-BR|Sezimal/NT10-10',
        'en-BR|Sezimal/NT10-10',

        'pt-BR|Sezimal/NT13-0530',
        'bz|Sezimal/NT13-0530',
        'eo-BR|Sezimal/NT13-0530',
        'en-BR|Sezimal/NT13-0530',

        'pt-BR|Sezimal/NT13-10',
        'bz|Sezimal/NT13-10',
        'eo-BR|Sezimal/NT13-10',
        'en-BR|Sezimal/NT13-10',

        'fr-CA|America/Montreal',
        'fr-FR|Europe/Paris',

        'pt-PT|Europe/Lisbon',
        'it-IT|Europe/Rome',
        'de-DE|Europe/Berlin',
        'es-ES|Europe/Madrid',

        'es-MX|America/Mexico_City',

        'en-US|America/Chicago',
        'en-US|America/Denver',
        'en-US|Pacific/Honolulu',
        'en-US|America/Los_Angeles',
        'en-US|America/New_York',
        'en-US|America/Anchorage',

        'en-AU|Australia/Adelaide',
        'en-AU|Australia/Sydney',
        'en-AU|Australia/Brisbane',

        'en-CA|America/Toronto',

        'en-GB|Europe/London',
        'en-IE|Europe/Dublin',
        'en-IL|Asia/Jerusalem',
        'en-IN|Asia/Calcutta',
        'en-MY|Asia/Kuala_Lumpur',

        'es-US|America/Chicago',
        'es-US|America/Denver',
        'es-US|Pacific/Honolulu',
        'es-US|America/Los_Angeles',
        'es-US|America/New_York',
        'es-US|America/Anchorage',

        'eo-US|America/Chicago',
        'eo-US|America/Denver',
        'eo-US|Pacific/Honolulu',
        'eo-US|America/Los_Angeles',
        'eo-US|America/New_York',
        'eo-US|America/Anchorage',

        'eo-AU|Australia/Adelaide',
        'eo-AU|Australia/Sydney',
        'eo-AU|Australia/Brisbane',

        'eo-CA|America/Toronto',

        'ja-JP|Asia/Tokyo',
        'eo-JP|Asia/Tokyo',
    )

    for item in itens:
        loc, tz = item.split('|')

        #
        # DCC is only sezimal
        #
        base = 10
        locale = sezimal_locale(loc)
        locale.base = base
        locale.DEFAULT_TIME_ZONE = tz
        locale.format_token = ''
        locale.calendar_displayed = 'DCC'

        for year in SezimalRange(*year_range):
            context = {
                'base': locale.base,
                'format_token': locale.format_token,
            }

            print('vai fazer', item, year, base, 'DCC', locale.format_token)
            _calendar_events(locale, year, context, only_check=True)

            if locale.ISO_TIME_FORMAT[:2] == '%I':
                locale.ISO_TIME_FORMAT = '%H:%M:%S'
                locale.HOUR_FORMAT = '24h'
                _calendar_events(locale, year, context, only_check=True)

        for calendar in ('SYM', 'ISO', 'DCC'):
            locale = sezimal_locale(loc)
            locale.DEFAULT_TIME_ZONE = tz
            locale.calendar_displayed = calendar

            for base in (10, 14, 20):
                locale.base = base

                for year in SezimalRange(*year_range):
                    if base == 10:
                        locale.format_token = ''
                    elif base == 14:
                        locale.format_token = '9'
                        locale.to_decimal_base()
                    elif base == 20:
                        locale.format_token = '↋'
                        locale.to_dozenal_base()

                    if calendar == 'DCC':
                        locale.format_token = 'c' + locale.format_token

                    context = {
                        'base': locale.base,
                        'format_token': locale.format_token,
                    }

                    print('vai fazer', item, year, base, calendar, locale.format_token)
                    if calendar == 'ISO':
                        _calendar_events(locale, (year - 200_000).decimal, context, only_check=True)

                        if locale.ISO_TIME_FORMAT[:2] == '%I':
                            locale.ISO_TIME_FORMAT = '%H:%M:%S'
                            locale.HOUR_FORMAT = '24h'
                            _calendar_events(locale, (year - 200_000).decimal, context, only_check=True)

                    else:
                        _calendar_events(locale, year, context, only_check=True)

                        if locale.ISO_TIME_FORMAT[:2] == '%I':
                            locale.ISO_TIME_FORMAT = '%H:%M:%S'
                            locale.HOUR_FORMAT = '24h'
                            _calendar_events(locale, year, context, only_check=True)
