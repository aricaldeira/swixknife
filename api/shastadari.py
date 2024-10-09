
from flask import redirect, Response, render_template
from main import app, sitemapper, sezimal_render_template
from  locale_detection import browser_preferred_locale

from swixknife import sezimal_locale, sezimal_spellout, SezimalInteger
from swixknife.date_time import SezimalDateTime
from swixknife.date_time.seasons_colors import weekly_season_colors

from decimal import Decimal
from datetime import datetime


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/shastadari')
def shastadari_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari', code=302)

    return redirect('/en/shastadari', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/en/shastadari')
def shastadari_en_route() -> Response:
    return sezimal_render_template('shastadari_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/pt/xastadári')
def shastadari_pt_route() -> Response:
    return sezimal_render_template('shastadari_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/bz/xastadari')
def shastadari_bz_route() -> Response:
    return sezimal_render_template('shastadari_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/prefixes')
def shastadari_prefixes_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/prefixos', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/prefiksus', code=302)

    return redirect('/en/shastadari/prefixes', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/prefixes')
def shastadari_prefixes_en_route() -> Response:
    return sezimal_render_template('prefixes_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/prefixos')
def shastadari_prefixes_pt_route() -> Response:
    return sezimal_render_template('prefixes_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/prefiksus')
def shastadari_prefixes_bz_route() -> Response:
    return sezimal_render_template('prefixes_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/base-units')
def shastadari_base_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-fundamentais', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/unidadis-fundamentays', code=302)

    return redirect('/en/shastadari/base-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/base-units')
def shastadari_base_units_en_route() -> Response:
    return sezimal_render_template('base_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-fundamentais')
def shastadari_base_units_pt_route() -> Response:
    if browser_preferred_locale()[-2:] in ('BR', 'br'):
        return sezimal_render_template('base_units_pt_br.html')

    return sezimal_render_template('base_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-fundamentays')
def shastadari_base_units_bz_route() -> Response:
    return sezimal_render_template('base_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/time-units')
def shastadari_time_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-de-tempo', code=302)
    elif browser_preferred_locale()[0:2] == 'bf':
        return redirect('/bz/xastadari/unidadis-di-tenpu', code=302)

    return redirect('/en/shastadari/time-units', code=302)

@sitemapper.include(lastmod='2024-09-16', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/time-units')
def shastadari_time_units_en_route() -> Response:
    return sezimal_render_template('time_units_en.html')

@sitemapper.include(lastmod='2024-09-16', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-de-tempo')
def shastadari_time_units_pt_route() -> Response:
    return sezimal_render_template('time_units_pt.html')

@sitemapper.include(lastmod='2024-09-16', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-di-tenpu')
def shastadari_time_units_bz_route() -> Response:
    return sezimal_render_template('time_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/derived-units')
def shastadari_derived_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-derivadas', code=302)

    return redirect('/en/shastadari/derived-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/derived-units')
def shastadari_derived_units_en_route() -> Response:
    return sezimal_render_template('derived_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-derivadas')
def shastadari_derived_units_pt_route() -> Response:
    if browser_preferred_locale()[-2:] in ('BR', 'br'):
        return sezimal_render_template('derived_units_pt_br.html')

    return sezimal_render_template('derived_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-derivadas')
def shastadari_derived_units_bz_route() -> Response:
    return sezimal_render_template('derived_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/other-units')
def shastadari_other_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/outras-unidades', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/otras-unidadis', code=302)

    return redirect('/en/shastadari/other-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/other-units')
def shastadari_other_units_en_route() -> Response:
    return sezimal_render_template('other_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/outras-unidades')
def shastadari_other_units_pt_route() -> Response:
    return sezimal_render_template('other_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/otras-unidadis')
def shastadari_other_units_bz_route() -> Response:
    return sezimal_render_template('other_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/scales')
def shastadari_scales_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/escalas', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/iskalas', code=302)

    return redirect('/en/shastadari/scales', code=302)

@sitemapper.include(lastmod='2024-09-13', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/scales')
def shastadari_scales_en_route() -> Response:
    if browser_preferred_locale().lower() == 'en-us':
        return sezimal_render_template('scales_en_us.html')

    return sezimal_render_template('scales_en.html')

@sitemapper.include(lastmod='2024-09-13', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/escalas')
def shastadari_scales_pt_route() -> Response:
    return sezimal_render_template('scales_pt.html')

@sitemapper.include(lastmod='2024-09-13', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/iskalas')
def shastadari_scales_bz_route() -> Response:
    return sezimal_render_template('scales_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/fractions')
def sezimal_fractions_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/frações', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/frasoyns', code=302)

    return redirect('/en/shastadari/fractions', code=302)

@sitemapper.include(lastmod='2024-10-09', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/fractions')
def sezimal_fractions_en_route() -> Response:
    # return sezimal_render_template('fractions_en.html')
    return render_template('fractions_en.html')

@sitemapper.include(lastmod='2024-10-09', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/frações')
def sezimal_fractions_pt_route() -> Response:
    # return sezimal_render_template('fractions_pt.html')
    return render_template('fractions_pt.html')

@sitemapper.include(lastmod='2024-10-09', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/frasoyns')
def sezimal_fractions_bz_route() -> Response:
    # return sezimal_render_template('fractions_bz.html')
    return render_template('fractions_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/calendar')
def sezimal_calendar_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/calendário', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/kalendaryu', code=302)

    return redirect('/en/shastadari/calendar', code=302)


def _calendar_data(locale, tz_locale, date=None, gray_scale=False):
    if not date:
        date = SezimalDateTime.now(time_zone=tz_locale.DEFAULT_TIME_ZONE)

    day_text = f'({sezimal_spellout(date.day, locale.LANGUAGE_TAG)})'
    year_text = f'({sezimal_spellout(date.year, locale.LANGUAGE_TAG)})'
    colors = weekly_season_colors(
        date.year,
        tz_locale.DEFAULT_HEMISPHERE,
        tz_locale.DEFAULT_TIME_ZONE,
        gray_scale=gray_scale,
    )

    data = {
        'str': str,
        'eval': eval,
        'sezimal_today': date.format('#X-#m-#d'),
        'iso_today': date.format('%Y-%m-%d'),
        'sezimal_today_full': date.format(locale.DATE_LONG_FORMAT, locale),
        'sezimal_today_full_text': date.format(locale.DATE_LONG_FORMAT.replace('#-d', day_text).replace('#Y', year_text), locale),
        'locale': locale,
        'tz_locale': tz_locale,
        'colors': colors,
        'midquarter': 'Midquarter day',
        date.format('this_weekday_#m_#w'): f"background-color: {colors[date.week_in_year]['700']}; color: {colors[date.week_in_year]['50']}; font-weight: bold;",
        date.format('this_week_#wY'): f"background-color: {colors[date.week_in_year]['700']}; color: {colors[date.week_in_year]['50']}; font-weight: bold;",
        'shade_month': '100' if gray_scale else '300',
        'gray_scale': gray_scale,

        'shade_week_number': '300',
        'shade_01': '400',
        'shade_02': '500',
        'shade_03': '600',
        'shade_04': '500',
        'shade_05': '400',
        'shade_10': '400',
        'shade_11': '300',

        'back_shade_week_number': '300',
        'back_shade_01': '400',
        'back_shade_02': '500',
        'back_shade_03': '600',
        'back_shade_04': '500',
        'back_shade_05': '400',
        'back_shade_10': '400',
        'back_shade_11': '300',

        'text_shade_week_number': '900',
        'text_shade_01': '50',
        'text_shade_02': '50',
        'text_shade_03': '50',
        'text_shade_04': '50',
        'text_shade_05': '50',
        'text_shade_10': '50',
        'text_shade_11': '50',
        'date': date,
        'sezimal_digits': False,
        'base': 10,
        'format_token': '',
    }

    data['shade_february'] = data[f"shade_{str(colors['february'].weekday).zfill(2)}"]
    data['shade_march'] = data[f"shade_{str(colors['march'].weekday).zfill(2)}"]
    data['shade_may'] = data[f"shade_{str(colors['may'].weekday).zfill(2)}"]
    data['shade_june'] = data[f"shade_{str(colors['june'].weekday).zfill(2)}"]
    data['shade_august'] = data[f"shade_{str(colors['august'].weekday).zfill(2)}"]
    data['shade_september'] = data[f"shade_{str(colors['september'].weekday).zfill(2)}"]
    data['shade_november'] = data[f"shade_{str(colors['november'].weekday).zfill(2)}"]
    data['shade_december'] = data[f"shade_{str(colors['december'].weekday).zfill(2)}"]

    return data

@sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/calendar')
def sezimal_calendar_en_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'en':
        locale = sezimal_locale('en-gb')

    data = _calendar_data(locale, sezimal_locale(browser_preferred_locale()))

    return sezimal_render_template(
        'calendar_en.html',
        **data,
    )

@sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/calendário')
def sezimal_calendar_pt_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'pt':
        locale = sezimal_locale('pt-br')

    data = _calendar_data(locale, sezimal_locale(browser_preferred_locale()))
    data['midquarter'] = 'Meio do trimestre'

    return sezimal_render_template(
        'calendar_pt.html',
        **data,
    )

@sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/kalendaryu')
def sezimal_calendar_bz_route() -> Response:
    locale = sezimal_locale(browser_preferred_locale())

    if locale.LANG != 'bz':
        locale = sezimal_locale('bz-br')

    data = _calendar_data(locale, locale)
    data['midquarter'] = 'Meyu du trimèstri'

    return sezimal_render_template(
        'calendar_bz.html',
        **data,
    )

# @sitemapper.include(lastmod='2024-09-19', changefreq='weekly', priority=0.8)
@app.route('/decimal-calendar')
@app.route('/decimal-calendar/<string:locale>')
@app.route('/decimal-calendar/<int:year>')
@app.route('/decimal-calendar/<string:locale>/<int:year>')
@app.route('/decimal-calendar/<int:year>-<int:month>')
@app.route('/decimal-calendar/<string:locale>/<int:year>-<int:month>')
@app.route('/decimal-calendar/<int:year>-<int:month>-<int:day>')
@app.route('/decimal-calendar/<string:locale>/<int:year>-<int:month>-<int:day>')
def decimal_calendar_route(
    locale: str = None,
    year: int = None,
    month: int = None,
    day: int = None,
) -> Response:
    locale = sezimal_locale(locale or browser_preferred_locale())

    date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    if year:
        date = date.replace(year=SezimalInteger(Decimal(year)) + 200_000)

        if month:
            date = date.replace(month=SezimalInteger(Decimal(month)))

            if day:
                date = SezimalDateTime(
                    datetime(year, month, day, 12, 0, 0),
                    time_zone=locale.DEFAULT_TIME_ZONE
                )

    data = _calendar_data(locale, locale, date)
    return sezimal_render_template(
        'calendar_decimal.html',
        **data,
    )


@app.route('/teste')
@app.route('/teste/<string:locale>')
@app.route('/teste/<int:year>')
@app.route('/teste/<string:locale>/<int:year>')
@app.route('/teste/<int:year>-<int:month>')
@app.route('/teste/<string:locale>/<int:year>-<int:month>')
@app.route('/teste/<int:year>-<int:month>-<int:day>')
@app.route('/teste/<string:locale>/<int:year>-<int:month>-<int:day>')
def teste_calendar_route(
    locale: str = None,
    year: int = None,
    month: int = None,
    day: int = None,
) -> Response:
    locale = sezimal_locale(locale or browser_preferred_locale())

    date = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    if year:
        date = date.replace(year=SezimalInteger(Decimal(year)) + 200_000)

        if month:
            date = date.replace(month=SezimalInteger(Decimal(month)))

            if day:
                date = SezimalDateTime(
                    datetime(year, month, day, 12, 0, 0),
                    time_zone=locale.DEFAULT_TIME_ZONE
                )

    data = _calendar_data(locale, locale, date)
    return sezimal_render_template(
        'calendar_teste.html',
        **data,
    )
