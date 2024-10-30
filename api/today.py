
import json
import urllib

from flask import redirect, Response, request, render_template, jsonify
from main import app, sitemapper, sezimal_render_template
from  locale_detection import browser_preferred_locale

from swixknife import sezimal_locale, sezimal_spellout, SezimalInteger
from swixknife import default_to_sezimal_digits, Dozenal
from swixknife.date_time import SezimalDateTime, SezimalDate, SezimalTime
from swixknife.date_time.seasons_colors import weekly_season_colors
from swixknife.functions import SezimalList, SezimalDictionary, SezimalRange
from swixknife.date_time.calendar import other_calendar_date_to_ordinal_date

from decimal import Decimal
from datetime import datetime
from zoneinfo import ZoneInfo

EVENTS_CACHE = SezimalDictionary({})


def _calendar_context(locale, date=None, gray_scale=False):
    if not date:
        date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    colors = weekly_season_colors(
        date.year,
        locale.DEFAULT_HEMISPHERE,
        locale.DEFAULT_TIME_ZONE,
        gray_scale=gray_scale,
    )

    data = {
        'SezimalList': SezimalList,
        'SezimalDictionary': SezimalDictionary,
        'SezimalRange': SezimalRange,
        'SezimalInteger': SezimalInteger,
        'str': str,
        'int': int,
        'eval': eval,
        'len': len,
        'sorted': sorted,
        'locale': locale,
        'tz_locale': locale,
        'gray_scale': gray_scale,
        'dark_mode': True,
        'small_screen': False,
        'colors': colors,
        'date': date,
        'sezimal_digits': False,
        'base': 10,
        'format_token': '',
        'date_last_month': date.previous(months=1),
        'date_next_month': date.next(months=1),
        'uta_first': None,
        'uta_last': None,
    }

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

    if date.quarter == 1:
        data['quarter_first_month'] = date.replace(month=1)
        data['quarter_last_month'] = date.replace(month=3)
    elif date.quarter == 2:
        data['quarter_first_month'] = date.replace(month=4)
        data['quarter_last_month'] = date.replace(month=10)
    elif date.quarter == 3:
        data['quarter_first_month'] = date.replace(month=11)
        data['quarter_last_month'] = date.replace(month=13)
    else:
        data['quarter_first_month'] = date.replace(month=14)
        data['quarter_last_month'] = date.replace(month=20)

    data['shade_february'] = data[f"shade_{str(colors['february'].weekday).zfill(2)}"]
    data['shade_march'] = data[f"shade_{str(colors['march'].weekday).zfill(2)}"]
    data['shade_may'] = data[f"shade_{str(colors['may'].weekday).zfill(2)}"]
    data['shade_june'] = data[f"shade_{str(colors['june'].weekday).zfill(2)}"]
    data['shade_august'] = data[f"shade_{str(colors['august'].weekday).zfill(2)}"]
    data['shade_september'] = data[f"shade_{str(colors['september'].weekday).zfill(2)}"]
    data['shade_november'] = data[f"shade_{str(colors['november'].weekday).zfill(2)}"]
    data['shade_december'] = data[f"shade_{str(colors['december'].weekday).zfill(2)}"]

    month_date = date.date.replace(day=1).previous(days=1)
    data['month_dates'] = SezimalList([])

    for week in SezimalRange(5):
        data['month_dates'].append(SezimalList([]))

        for day in SezimalRange(11):
            month_date = month_date.next(days=1)
            data['month_dates'][week].append(month_date)

    return data


# @sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/decimal-calendar')
@app.route('/symmetry454-calendar')
def decimal_today_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    data = _calendar_context(locale, date)
    data['base'] = 14
    data['format_token'] = '9'

    if locale.DIGITS:
        data['format_token'] += '?'

    return sezimal_render_template(
        'today_decimal.html',
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
        cookie = urllib.parse.unquote(request.cookies['sezimal'])
        base, format_token, locale, time_zone, hour_format, hemisphere = cookie.split('|')

        locale = sezimal_locale(locale)
        locale.DEFAULT_TIME_ZONE = time_zone
        locale.HOUR_FORMAT = hour_format
        locale.DEFAULT_HEMISPHERE = hemisphere

    else:
        locale = sezimal_locale(browser_preferred_locale())

    date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)


    data = _calendar_context(locale, date)

    if locale.DIGITS:
        data['format_token'] = (data['format_token'] or '') + '?'

    return sezimal_render_template(
        'today.html',
        sezimal_month_number=date.month,
        **data,
    )

@app.route('/calendar/process', methods=['POST'])
def api_calendar_process():
    dados = json.loads(request.data.decode('utf-8'))
    dados['base'] = int(dados['base'])

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    locale.DEFAULT_TIME_ZONE = dados['time_zone'] or locale.DEFAULT_TIME_ZONE
    gray_scale = dados['theme'] == 'GRAY'

    if dados['hemisphere'] == 'locale':
        dados['hemisphere'] = locale.DEFAULT_HEMISPHERE

    locale.DEFAULT_HEMISPHERE = dados['hemisphere'] or locale.DEFAULT_HEMISPHERE

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    if 'date' in dados and dados['date']:
        date = SezimalDateTime.combine(SezimalDate(dados['date']), now.time, locale.DEFAULT_TIME_ZONE)

    else:
        date = now

    if dados['direction'] == 'today':
        date = now
    elif dados['direction'] == 'previous':
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

        if date.year < 155_500:
            date = date.replace(year=155_500)

    elif dados['direction'] == 'next':
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

        if date.year > 230_000:
            date = date.replace(year=230_000)

    context = _calendar_context(locale, date, gray_scale)
    context['locale'] = locale
    context['now'] = now
    context['base'] = dados['base']
    context['format_token'] = (dados['format_token'] or '')
    context['short_year'] = True

    if context['short_year']:
        locale.DATE_FORMAT = locale._to_short_year_format(locale.DATE_FORMAT)
        locale.DATE_LONG_FORMAT = locale._to_short_year_format(locale.DATE_LONG_FORMAT)

    #
    # Digits for the change view line
    #
    if context['base'] == 10:
        if '!' in context['format_token']:
            context['change_view_twelve'] = '󱸂󱸀'
            context['change_view_seven'] = '󱸁󱸁'
            context['change_view_five'] = '󱸅'
            context['change_view_four'] = '󱸄'
            context['change_view_one'] = '󱸁'
        else:
            context['change_view_twelve'] = '20'
            context['change_view_seven'] = '11'
            context['change_view_five'] = '5'
            context['change_view_four'] = '4'
            context['change_view_one'] = '1'

    elif context['base'] == 14:
        context['change_view_twelve'] = '12'
        context['change_view_seven'] = '7'
        context['change_view_five'] = '5'
        context['change_view_four'] = '4'
        context['change_view_one'] = '1'

    elif context['base'] == 20:
        context['change_view_twelve'] = '10'
        context['change_view_seven'] = '7'
        context['change_view_five'] = '5'
        context['change_view_four'] = '4'
        context['change_view_one'] = '1'

    if locale.DIGITS:
        context['format_token'] += '?'

        context['change_view_twelve'] = locale.digit_replace(context['change_view_twelve'])
        context['change_view_seven'] = locale.digit_replace(context['change_view_seven'])
        context['change_view_five'] = locale.digit_replace(context['change_view_five'])
        context['change_view_four'] = locale.digit_replace(context['change_view_four'])
        context['change_view_one'] = locale.digit_replace(context['change_view_one'])

    if dados['hour_format'] != 'locale':
        locale.HOUR_FORMAT = dados['hour_format']

    context['events'] = _calendar_events(locale, date, context)

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
    date: SezimalDate = None
    time: SezimalTime = None
    emoji: str = ''
    name: str = ''
    full_day: bool = True
    end_date: SezimalDate = None
    end_time: SezimalTime = None
    origin: str = ''

    def __repr__(self):
        return f"SezimalEvent({self.date}, {self.time}, {self.emoji}, {self.name}, {self.full_day}, {self.end_date}, {self.end_time}, {self.origin})"

    def __str__(self):
        return f"SezimalEvent({self.date}, {self.time}, {self.emoji}, {self.name}, {self.full_day}, {self.end_date}, {self.end_time}, {self.origin})"

    @property
    def daily_view(self):
        if self.emoji:
            line = self.emoji + ' - '
        else:
            line = ''

        if self.name:
            line += self.name

        return line


def _calendar_events(locale, date, context):
    cache_key = str(date.year)
    cache_key += '|' + locale.LANGUAGE_TAG
    cache_key += '|' + locale.DEFAULT_TIME_ZONE
    cache_key += '|' + str(context['base']) + context['format_token']

    if cache_key in EVENTS_CACHE:
        return EVENTS_CACHE[cache_key]

    events = SezimalDictionary({})

    for event_origin, event_name in locale.HOLIDAYS + locale.HOLIDAYS_OTHER_CALENDAR:
        for reference_year in (date.year - 1, date.year, date.year + 1):
            event_ordinal_date, (event_year, event_month, event_day), age = \
                other_calendar_date_to_ordinal_date(event_origin, reference_year)

            event_date = SezimalDate.from_ordinal_date(event_ordinal_date)

            if event_date.year != date.year:
                continue

            event_name = event_name.replace('🕆', '🕇')
            event_emoji = event_name.split(' ')[0]
            event_name = event_name.replace(event_emoji, '').strip()

            if context['base'] == 10:
                if context['format_token'] == '!':
                    event_name = event_name.replace('#i', default_to_sezimal_digits(str(age)))
                    event_name = locale._to_sezimal_date_format(event_name)

                elif '?' in context['format_token'] and locale.DIGITS:
                    event_name = event_name.replace('#i', locale.digit_replace(str(age)))

                else:
                    event_name = event_name.replace('#i', str(age))

            elif context['base'] == 14:
                if '?' in context['format_token'] and locale.DIGITS:
                    event_name = event_name.replace('#i', locale.digit_replace(str(age.decimal)))
                else:
                    event_name = event_name.replace('#i', str(age.decimal))

                if '%P' in locale.ISO_TIME_FORMAT.upper():
                    event_name = event_name.replace('#u', '%I')
                    event_name = event_name.replace('#p', '%M %P')
                else:
                    event_name = event_name.replace('#u', '%H')
                    event_name = event_name.replace('#p', '%M')

            elif context['base'] == 20:
                if '?' in context['format_token'] and locale.DIGITS:
                    event_name = event_name.replace('#i', locale.digit_replace(age.dozenal))
                else:
                    event_name = event_name.replace('#i', age.dozenal)

                event_name = locale._to_dozenal_date_format(event_name)
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
            event.date = event_date
            event.emoji = event_emoji
            event.name = event_name
            event.origin = event_origin

            if event.date.month not in events:
                events[event.date.month] = SezimalDictionary({})

            if event.date.day not in events[event.date.month]:
                events[event.date.month][event.date.day] = SezimalList([])

            events[event.date.month][event.date.day].append(event)

    EVENTS_CACHE[cache_key] = events

    return events


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/calendar')
def sezimal_calendar_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/calendário', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/kalendaryu', code=302)

    return redirect('/en/shastadari/calendar', code=302)

@sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/calendar')
def sezimal_calendar_en_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'en':
        locale = sezimal_locale('en-gb')

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = ''
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT, locale)
    context['sezimal_today_full'] = now.format(locale.DATE_LONG_FORMAT, locale)

    sf = locale.DATE_LONG_FORMAT

    spellout_year = f'({locale.spellout(now.year)})'
    sf = sf.replace('#Y', spellout_year)
    sf = sf.replace('#y', spellout_year)
    sf = sf.replace('#-y', spellout_year)

    if '#O' in sf and locale.day_ordinal_suffix(now.day) != '':
        sf = sf.replace('#d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
        sf = sf.replace('#-d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
    else:
        sf = sf.replace('#d', f"({locale.spellout(now.day)})")
        sf = sf.replace('#-d', f"({locale.spellout(now.day)})")

    context['sezimal_today_full_text'] = now.format(sf, locale)

    return sezimal_render_template(
        'calendar_en.html',
        **context,
    )

@sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/calendário')
def sezimal_calendar_pt_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'pt':
        locale = sezimal_locale('pt-br')

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = ''
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT, locale)
    context['sezimal_today_full'] = now.format(locale.DATE_LONG_FORMAT, locale)

    sf = locale.DATE_LONG_FORMAT

    spellout_year = f'({locale.spellout(now.year)})'
    sf = sf.replace('#Y', spellout_year)
    sf = sf.replace('#y', spellout_year)
    sf = sf.replace('#-y', spellout_year)

    if '#O' in sf and locale.day_ordinal_suffix(now.day) != '':
        sf = sf.replace('#d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
        sf = sf.replace('#-d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
    else:
        sf = sf.replace('#d', f"({locale.spellout(now.day)})")
        sf = sf.replace('#-d', f"({locale.spellout(now.day)})")

    context['sezimal_today_full_text'] = now.format(sf, locale)

    locale.HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '\ufe0f🎉🎭 Karnavaw'),
        ('EASTER-115', '\ufe0f🎉🎭 Karnavaw'),
        # ('EASTER-114', '\ufe0f🎉🎭 Kwarta-fera di Sinzas'),
        ('EASTER-2',   '\ufe0f🕆\ufe0f🥀 Paxawn di Kristu'),
        ('EASTER',     '\ufe0f🐣🌱 Paskwa'),
        ('EASTER+140', '\ufe0f🥖🍷 Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '\ufe0f🕊️ 🌎 Konfraternizasawn Universaw'),
        ('05-01', '\ufe0f🐝🐜 Dia du Trabalyu'),
        ('14-20', '\ufe0f⛪👸🏿 Nòsa Seỹòra Aparesida'),
        ('15-02', '\ufe0f🪦🕊️  Finadus'),
        ('20-40', '\ufe0f🥂🍽️  Véspera di Nataw'),
        ('20-41', '\ufe0f🌟👼🏼 Nataw'),
        ('20-55', '\ufe0f🍾🎆 Véspera di Anu Novu'),

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
        # ('212_144-04-32', '\ufe0f🇧🇷🔺 Tiradentis'),                 # sábadu  212_144-04-32 ~ 1792-04-21_dec
        # ('212_540-11-10', '\ufe0f🪖📜 Revolusawn di 1932 (1̈5̈0̄/540)'),   # sábadu  212_540-11-10 ~ 1932-07-09_dec
        # ('212_234-13-10', '\ufe0f🇧🇷🕊️ Independensya du Braziw'),    # sábadu  212_234-13-10 ~ 1822-09-07_dec
        # ('212_425-15-31', '\ufe0f🇧🇷📜 Proklamasawn da Repúblika'),  # sesta   212_425-15-31 ~ 1889-11-15_dec
        # ('211_503-15-33', '\ufe0f👨🏿 Konsyensya Negra'),             # dumingu 211_503-15-33 ~ 1695-11-20_dec

        ('212_144-04-33', '\ufe0f🇧🇷🔺 Tiradentis'),                      # dumingu, 04-33 ~ 04-21_dec
        ('212_540-11-13', '\ufe0f🪖📜 Revolusawn di 1932 (1̈5̈0̄/540) (#i)'),   # tersa,   11-13 ~ 07-09_dec
        ('212_234-13-11', '\ufe0f🇧🇷🕊️ Independensya du Braziw (#i)'),    # dumingu, 13-11 ~ 09-07_dec
        ('212_425-15-23', '\ufe0f🇧🇷📜 Proklamasawn da Repúblika (#i)'),  # sigunda, 15-23 ~ 11-15_dec
        ('211_503-15-32', '\ufe0f👨🏿 Konsyensya Negra'),                  # sábadu,  15-32 ~ 11-20_dec
    ]
    locale.HOLIDAYS_OTHER_CALENDAR = []
    locale.CALENDAR = 'symmetry454'

    context['events'] = _calendar_events(locale, now, context)

    return sezimal_render_template(
        'calendar_pt.html',
        **context,
    )

@sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/kalendaryu')
def sezimal_calendar_bz_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'bz':
        locale = sezimal_locale('bz-br')

    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = ''
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT, locale)
    context['sezimal_today_full'] = now.format(locale.DATE_LONG_FORMAT, locale)

    sf = locale.DATE_LONG_FORMAT

    spellout_year = f'({locale.spellout(now.year)})'
    sf = sf.replace('#Y', spellout_year)
    sf = sf.replace('#y', spellout_year)
    sf = sf.replace('#-y', spellout_year)

    if '#O' in sf and locale.day_ordinal_suffix(now.day) != '':
        sf = sf.replace('#d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
        sf = sf.replace('#-d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
    else:
        sf = sf.replace('#d', f"({locale.spellout(now.day)})")
        sf = sf.replace('#-d', f"({locale.spellout(now.day)})")

    context['sezimal_today_full_text'] = now.format(sf, locale)
    now = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    context = _calendar_context(locale, now)
    context['locale'] = locale
    context['now'] = now
    context['base'] = 10
    context['format_token'] = ''
    context['calendar_presentation'] = True
    context['sezimal_today'] = now.format(locale.DATE_FORMAT, locale)
    context['iso_today'] = now.format(locale.ISO_DATE_FORMAT, locale)
    context['sezimal_today_full'] = now.format(locale.DATE_LONG_FORMAT, locale)

    sf = locale.DATE_LONG_FORMAT

    spellout_year = f'({locale.spellout(now.year)})'
    sf = sf.replace('#Y', spellout_year)
    sf = sf.replace('#y', spellout_year)
    sf = sf.replace('#-y', spellout_year)

    if '#O' in sf and locale.day_ordinal_suffix(now.day) != '':
        sf = sf.replace('#d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
        sf = sf.replace('#-d#O', f"({locale.spellout('ordinal ' + str(now.day))})")
    else:
        sf = sf.replace('#d', f"({locale.spellout(now.day)})")
        sf = sf.replace('#-d', f"({locale.spellout(now.day)})")

    context['sezimal_today_full_text'] = now.format(sf, locale)

    locale.HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '\ufe0f🎉🎭 Karnavaw'),
        ('EASTER-115', '\ufe0f🎉🎭 Karnavaw'),
        # ('EASTER-114', '\ufe0f🎉🎭 Kwarta-fera di Sinzas'),
        ('EASTER-2',   '\ufe0f🕆\ufe0f🥀 Paxawn di Kristu'),
        ('EASTER',     '\ufe0f🐣🌱 Paskwa'),
        ('EASTER+140', '\ufe0f🥖🍷 Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '\ufe0f🕊️ 🌎 Konfraternizasawn Universaw'),
        ('05-01', '\ufe0f🐝🐜 Dia du Trabalyu'),
        ('14-20', '\ufe0f⛪👸🏿 Nòsa Seỹòra Aparesida'),
        ('15-02', '\ufe0f🪦🕊️  Finadus'),
        ('20-40', '\ufe0f🥂🍽️  Véspera di Nataw'),
        ('20-41', '\ufe0f🌟👼🏼 Nataw'),
        ('20-55', '\ufe0f🍾🎆 Véspera di Anu Novu'),

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
        # ('212_144-04-32', '\ufe0f🇧🇷🔺 Tiradentis'),                 # sábadu  212_144-04-32 ~ 1792-04-21_dec
        # ('212_540-11-10', '\ufe0f🪖📜 Revolusawn di 1932 (1̈5̈0̄/540)'),   # sábadu  212_540-11-10 ~ 1932-07-09_dec
        # ('212_234-13-10', '\ufe0f🇧🇷🕊️ Independensya du Braziw'),    # sábadu  212_234-13-10 ~ 1822-09-07_dec
        # ('212_425-15-31', '\ufe0f🇧🇷📜 Proklamasawn da Repúblika'),  # sesta   212_425-15-31 ~ 1889-11-15_dec
        # ('211_503-15-33', '\ufe0f👨🏿 Konsyensya Negra'),             # dumingu 211_503-15-33 ~ 1695-11-20_dec

        ('212_144-04-33', '\ufe0f🇧🇷🔺 Tiradentis'),                      # dumingu, 04-33 ~ 04-21_dec
        ('212_540-11-13', '\ufe0f🪖📜 Revolusawn di 1932 (1̈5̈0̄/540) (#i)'),   # tersa,   11-13 ~ 07-09_dec
        ('212_234-13-11', '\ufe0f🇧🇷🕊️ Independensya du Braziw (#i)'),    # dumingu, 13-11 ~ 09-07_dec
        ('212_425-15-23', '\ufe0f🇧🇷📜 Proklamasawn da Repúblika (#i)'),  # sigunda, 15-23 ~ 11-15_dec
        ('211_503-15-32', '\ufe0f👨🏿 Konsyensya Negra'),                  # sábadu,  15-32 ~ 11-20_dec
    ]
    locale.HOLIDAYS_OTHER_CALENDAR = []
    locale.CALENDAR = 'symmetry454'

    context['events'] = _calendar_events(locale, now, context)

    return sezimal_render_template(
        'calendar_bz.html',
        **context,
    )


@app.route('/calendar/event-window', methods=['POST'])
def api_event_window():
    dados = json.loads(request.data.decode('utf-8'))
    dados['base'] = int(dados['base'])

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    locale.DEFAULT_TIME_ZONE = dados['time_zone'] or locale.DEFAULT_TIME_ZONE
    gray_scale = dados['theme'] == 'GRAY'

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

    locale = sezimal_locale(dados['locale'] or browser_preferred_locale())
    locale.DEFAULT_TIME_ZONE = dados['time_zone'] or locale.DEFAULT_TIME_ZONE

    date_string = dados['calendar_type']
    date_error = ''
    time_error = ''
    reference_year = SezimalInteger(213_212)

    if 'EASTER' in date_string:
        if dados['easter_days']:
            date_string += dados['easter_sign'].replace('_', '+') or '+'

            try:
                if base == 10:
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
            try:
                dados['year'] = int(dados['year'])

                if dados['year'] <= 0:
                    date_error = 'Invalid year'
                    res = {
                        'date_error': date_error,
                        'time_error': time_error,
                    }
                    return jsonify(res)

            except:
                date_error = 'Invalid date'
                res = {
                    'date_error': date_error,
                    'time_error': time_error,
                }
                return jsonify(res)

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

    if base == 10:
        if dados['format_token'] == '!':
            date_format = locale.SEZIMAL_DATE_TEXT_SHORT_MONTH_FORMAT
        else:
            date_format = locale.DATE_TEXT_SHORT_MONTH_FORMAT

    elif base == 14:
        date_format = locale.DECIMAL_DATE_TEXT_SHORT_MONTH_FORMAT

    elif base == 20:
        date_format = locale.DOZENAL_DATE_TEXT_SHORT_MONTH_FORMAT

    if base == 10:
        month_names = locale.MONTH_ABBREVIATED_NAME
    else:
        month_names = locale.ISO_MONTH_ABBREVIATED_NAME

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

            if base == 10:
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

            if base == 10:
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
