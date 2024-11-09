
import pathlib

TEMPLATE_PATH = pathlib.Path(__file__).parent.resolve().joinpath('template')

from flask import Flask, request, render_template, redirect
from flask_sitemapper import Sitemapper

from swixknife.localization import sezimal_locale, SezimalLocale
from swixknife import SezimalDate, SezimalDateTime, SezimalTime
from decimal import Decimal
from swixknife import Sezimal, SezimalRange, SezimalInteger
from swixknife.weather.weather import SezimalWeather


from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
app.json.sort_keys = False
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
app.template_folder = TEMPLATE_PATH

sitemapper = Sitemapper()
sitemapper.init_app(app)

def sezimal_render_template(template_name_or_list, **context) -> str:
    res = render_template(template_name_or_list, **context)
    #
    # Protects the sezimal punctuation from being
    # treated as spaces
    #
    res = res.replace('󱹮', '''\u200d󱹮\u200d''')
    res = res.replace('󱹯', '''\u200d󱹯\u200d''')
    res = res.replace('󱹭', '''\u200d󱹭\u200d''')
    res = res.replace('󱹬', '''\u200d󱹬\u200d''')
    res = res.replace('󱹶', '''\u200d󱹶\u200d''')
    res = res.replace('󱹷', '''\u200d󱹷\u200d''')
    res = res.replace('󱹱', '''\u200d󱹱\u200d''')
    res = res.replace('󱹲', '''\u200d󱹲\u200d''')
    res = res.replace('󱹳', '''\u200d󱹳\u200d''')
    res = res.replace('󱹴', '''\u200d󱹴\u200d''')
    res = res.replace('󱹴', '''\u200d󱹴\u200d''')

    # res = res.replace('\u202c', 'V')  # '&#8236;')
    # res = res.replace('\u202d', 'E-D')  # '&#8237;')
    # res = res.replace('\u202e', 'D-E')  # '&#8238;')

    return res


from locale_info import *
from number_conversion import *
from now import *
from agòra import *
from calculator import *
from digits import *
from today import *
from shastadari import *

from  locale_detection import browser_preferred_locale


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/')
def index_route():
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz', code=302)

    return redirect('/en', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/en')
def index_en_route():
    return sezimal_render_template('sezimal_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/pt')
def index_pt_route():
    return sezimal_render_template('sezimal_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/bz')
def index_bz_route():
    return sezimal_render_template('sezimal_bz.html')


@app.route('/comparing-fractions')
def comparing_fractions_route():
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/comparando-frações', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz', code=302)

    return redirect('/en/comparing-fractions', code=302)

@sitemapper.include(lastmod='2024-09-21', changefreq='weekly', priority=1)
@app.route('/en/comparing-fractions')
def comparing_fractions_en_route():
    return sezimal_render_template('comparing_fractions_en.html')

@sitemapper.include(lastmod='2024-09-21', changefreq='weekly', priority=1)
@app.route('/pt/comparando-frações')
def comparing_fractions_pt_route():
    return sezimal_render_template('comparing_fractions_pt.html')

@sitemapper.include(lastmod='2024-09-21', changefreq='weekly', priority=1)
@app.route('/bz/konparandu-frasoyns')
def comparing_fractions_bz_route():
    return sezimal_render_template('comparing_fractions_bz.html')


@app.route('/comparing-bases')
def comparing_bases_route():
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/comparando-bases', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz', code=302)

    return redirect('/en/comparing-bases', code=302)

@sitemapper.include(lastmod='2024-09-27', changefreq='weekly', priority=1)
@app.route('/en/comparing-bases')
def comparing_bases_en_route():
    return sezimal_render_template('comparing_bases_en.html')

@sitemapper.include(lastmod='2024-09-27', changefreq='weekly', priority=1)
@app.route('/pt/comparando-bases')
def comparing_bases_pt_route():
    return sezimal_render_template('comparing_bases_pt.html')

@sitemapper.include(lastmod='2024-09-27', changefreq='weekly', priority=1)
@app.route('/bz/konparandu-bazis')
def comparing_bases_bz_route():
    return sezimal_render_template('comparing_bases_bz.html')


def _date_to_json(sdt: SezimalDateTime, locale: SezimalLocale) -> dict:
    res = {
        #
        # Date and time
        #
        'date_time': {
            'format': sdt.format(locale.DATE_TIME_FORMAT, locale),
            'long_format': sdt.format(locale.DATE_TIME_LONG_FORMAT, locale),
            'season_name': sdt.format(f'#~{locale.DEFAULT_HEMISPHERE}S', locale),
            'season_emoji': sdt.format(f'#@~{locale.DEFAULT_HEMISPHERE}S', locale),
            'moon_name': sdt.format(f'#~{locale.DEFAULT_HEMISPHERE}L', locale),
            'moon_emoji': sdt.format(f'#@~{locale.DEFAULT_HEMISPHERE}L', locale),
            'date_time': sdt.format('#y-#m-#d #u:#p:#a.#n#b#x #:t', locale),
            'iso': sdt.format('%5Y-%5m-%5d %5H:%5M:%5S.%5f %:5z'),
            'julian_day': float(str(sdt.julian_day)),
            'rata_die': float(str(sdt.as_days)),
            'decimal_symmetry454': str(int(sdt.symmetric_year)).zfill(4) + sdt.format('-#9m-#9d %H:%M:%S.%f %:z', locale),
            'decimal_iso': sdt.format('%Y-%m-%d %H:%M:%S.%f %:z', locale),
            'decimal_julian_day': float(sdt.julian_day.decimal),
            'decimal_rata_die': float(sdt.as_days.decimal),
        },

        'date': {
            #
            # Date
            #
            'format': sdt.format(locale.DATE_FORMAT, locale),
            'long_format': sdt.format(locale.DATE_LONG_FORMAT, locale),
            'year': int(str(sdt.year)),
            'month': int(str(sdt.month)),
            'day': int(str(sdt.day)),
            'weekday': int(sdt.format('#w', locale)),
            'leap_year': sdt.is_leap,
            'long_month': sdt.is_long_month,
            'month_name': sdt.format('#M', locale),
            'weekday_name': sdt.format('#W', locale),
        },

        'time': {
            #
            # Time
            #
            'format': sdt.format(locale.TIME_FORMAT, locale),
            'uta': int(str(sdt.uta)),
            'posha': int(str(sdt.posha)),
            'agrima': int(str(sdt.agrima)),
            'anuga': int(str(sdt.anuga)),
            'boda': int(str(sdt.boda)),
            'shaditiboda': int(str(sdt.shaditiboda)),
            'time_zone': str(sdt.time_zone),
            'time_zone_offset': sdt.format('#t'),
            'dst': sdt.is_dst,
        },
    }

    return res


@app.route('/api/date-time/from-julian-day')
@app.route('/api/date-time/from-julian-date')
@app.route('/api/date-time/from-sezimal-julian-day')
@app.route('/api/date-time/from-sezimal-julian-date')
@app.route('/api/date-time/from-julian-day/<float:julian_date>')
@app.route('/api/date-time/from-julian-day/<float:julian_date>/<string:locale>')
@app.route('/api/date-time/from-julian-day/<float:julian_date>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-julian-date/<float:julian_date>')
@app.route('/api/date-time/from-julian-date/<float:julian_date>/<string:locale>')
@app.route('/api/date-time/from-julian-date/<float:julian_date>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-sezimal-julian-day/<float:julian_date>')
@app.route('/api/date-time/from-sezimal-julian-day/<float:julian_date>/<string:locale>')
@app.route('/api/date-time/from-sezimal-julian-day/<float:julian_date>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-sezimal-julian-date/<float:julian_date>')
@app.route('/api/date-time/from-sezimal-julian-date/<float:julian_date>/<string:locale>')
@app.route('/api/date-time/from-sezimal-julian-date/<float:julian_date>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-julian-day/<string:locale>')
@app.route('/api/date-time/from-julian-day/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-julian-date/<string:locale>')
@app.route('/api/date-time/from-julian-date/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-sezimal-julian-day/<string:locale>')
@app.route('/api/date-time/from-sezimal-julian-day/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-sezimal-julian-date/<string:locale>')
@app.route('/api/date-time/from-sezimal-julian-date/<string:locale>/<path:time_zone>')
def from_sezimal_julian_date(julian_date: float = None, locale: str ='en', time_zone: str = None) -> dict:
    locale = sezimal_locale(locale)
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE

    if julian_date is None:
        return _date_to_json(SezimalDateTime.now(time_zone), locale)

    julian_date = Sezimal(str(julian_date))

    sdt = SezimalDateTime.from_julian_date(julian_date, 'UTC')
    sdt = sdt.at_time_zone(time_zone)

    return _date_to_json(sdt, locale)


@app.route('/api/date-time/from-decimal-julian-day')
@app.route('/api/date-time/from-decimal-julian-date')
@app.route('/api/date-time/from-decimal-julian-day/<float:julian_date>')
@app.route('/api/date-time/from-decimal-julian-day/<float:julian_date>/<string:locale>')
@app.route('/api/date-time/from-decimal-julian-day/<float:julian_date>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-decimal-julian-date/<float:julian_date>')
@app.route('/api/date-time/from-decimal-julian-date/<float:julian_date>/<string:locale>')
@app.route('/api/date-time/from-decimal-julian-date/<float:julian_date>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-decimal-julian-day/<string:locale>')
@app.route('/api/date-time/from-decimal-julian-day/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-decimal-julian-date/<string:locale>')
@app.route('/api/date-time/from-decimal-julian-date/<string:locale>/<path:time_zone>')
def from_decimal_julian_date(julian_date: float = None, locale: str ='en', time_zone: str = None) -> dict:
    locale = sezimal_locale(locale)
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE

    if julian_date is None:
        return _date_to_json(SezimalDateTime.now(time_zone), locale)

    julian_date = Sezimal(Decimal(str(julian_date)))

    sdt = SezimalDateTime.from_julian_date(julian_date, 'UTC')
    sdt = sdt.at_time_zone(time_zone)

    return _date_to_json(sdt, locale)


@app.route('/api/date-time')
@app.route('/api/date-time/from-rata-die')
@app.route('/api/date-time/from-sezimal-rata-die')
@app.route('/api/date-time/from-rata-die/<float:rata_die>')
@app.route('/api/date-time/from-rata-die/<float:rata_die>/<string:locale>')
@app.route('/api/date-time/from-rata-die/<float:rata_die>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-sezimal-rata-die/<float:rata_die>')
@app.route('/api/date-time/from-sezimal-rata-die/<float:rata_die>/<string:locale>')
@app.route('/api/date-time/from-sezimal-rata-die/<float:rata_die>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/<string:locale>')
@app.route('/api/date-time/from-rata-die/<string:locale>')
@app.route('/api/date-time/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-rata-die/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/from-sezimal-rata-die/<string:locale>')
@app.route('/api/date-time/from-sezimal-rata-die/<string:locale>/<path:time_zone>')
def from_sezimal_rata_die(rata_die: float = None, locale: str ='en', time_zone: str = None) -> dict:
    locale = sezimal_locale(locale)
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE

    if rata_die is None:
        return _date_to_json(SezimalDateTime.now(time_zone), locale)

    rata_die = Sezimal(str(rata_die))

    sdt = SezimalDateTime.from_days(rata_die, 'UTC')
    sdt = sdt.at_time_zone(time_zone)

    return _date_to_json(sdt, locale)


@app.route('/api/format/<string:locale>/<path:time_zone>')
def api_date(locale: str = None, time_zone: str = None) -> str:
    locale = sezimal_locale(locale or 'en')
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE

    date_time = SezimalDateTime.now(time_zone=time_zone.rstrip('/'))

    if 'format' in request.args:
        return date_time.format(request.args['format'], locale)

    return date_time.format(locale.DATE_TIME_FORMAT, locale)

@app.route('/sitemap.xml')
def sitemap():
  return sitemapper.generate()


@app.route('/robots.txt')
def robots():
    text = '''User-agent: *
Sitemap: https://sezimal.tauga.online/sitemap.xml
'''
    return Response(text, status=200, mimetype='text/plain')
