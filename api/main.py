
import pathlib

TEMPLATE_PATH = pathlib.Path(__file__).parent.resolve().joinpath('template')
LOG_PATH = pathlib.Path('~/.sezimal/access.log').expanduser()


from flask import Flask, request, render_template, redirect
from flask import has_request_context
from flask_sitemapper import Sitemapper

from datetime import datetime

from swixknife.localization import sezimal_locale, SezimalLocale
from swixknife import SezimalDate, SezimalDateTime, SezimalTime
from decimal import Decimal
from swixknife import Sezimal, SezimalRange, SezimalInteger
from swixknife.weather.weather import SezimalWeather
from swixknife import Dozenal

from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.middleware.profiler import ProfilerMiddleware


app = Flask(__name__)
app.json.sort_keys = False
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
# app.wsgi_app = ProfilerMiddleware(ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# ))
app.template_folder = TEMPLATE_PATH

sitemapper = Sitemapper()
sitemapper.init_app(app)

def sezimal_render_template(template_name_or_list, **context) -> str:
    res = render_template(template_name_or_list, **context)
    #
    # Protects the sezimal punctuation from being
    # treated as spaces
    #
    # res = res.replace('󱹮', '''\u200d󱹮\u200d''')
    # res = res.replace('󱹯', '''\u200d󱹯\u200d''')
    # res = res.replace('󱹭', '''\u200d󱹭\u200d''')
    # res = res.replace('󱹬', '''\u200d󱹬\u200d''')
    # res = res.replace('󱹶', '''\u200d󱹶\u200d''')
    # res = res.replace('󱹷', '''\u200d󱹷\u200d''')
    # res = res.replace('󱹱', '''\u200d󱹱\u200d''')
    # res = res.replace('󱹲', '''\u200d󱹲\u200d''')
    # res = res.replace('󱹳', '''\u200d󱹳\u200d''')
    # res = res.replace('󱹴', '''\u200d󱹴\u200d''')
    # res = res.replace('󱹴', '''\u200d󱹴\u200d''')

    # res = res.replace('\u202c', 'V')  # '&#8236;')
    # res = res.replace('\u202d', 'E-D')  # '&#8237;')
    # res = res.replace('\u202e', 'D-E')  # '&#8238;')

    # res = res.replace('󱹮', '''<span class="punctuation">Ꞌ</span>''')
    # res = res.replace('󱹯', '''<span class="punctuation">ꞋꞋ</span>''')
    # res = res.replace('󱹭', "ꞌ")
    # res = res.replace('󱹬', 'Ꞌ')
    # res = res.replace('󱹶', '''<span class="punctuation">Ꞌ̥</span>''')
    # res = res.replace('󱹷', '''<span class="punctuation">ꞌ̣</span>''')

    return res


from locale_info import *
from number_conversion import *
# from now import *
# from agòra import *
from calculator import *
from digits import *
from today import *
from shastadari import *
from watchface import *

from  locale_detection import browser_preferred_locale


def log_access(f):
    if request.headers.get('X-Forwarded-For', '') == '177.139.219.194':
        return

    now = SezimalDateTime.now()
    msg = now.format('#>Y-#m-#d #u:#p:#a')
    msg += '||'
    msg += now.format('&>Y-&m-&d #u:#p:#a')
    msg += '||'
    msg += now.format('%Y-%m-%d %H:%M:%S')
    msg += '||'
    msg += request.headers.get('X-Forwarded-For', '')
    msg += '||'
    msg += f
    msg += '||'
    msg += browser_preferred_locale()
    msg += '||'

    if 'sezimal' in request.cookies:
        msg += str(request.cookies['sezimal'])

    print(msg)

    if not app.debug:
        with open(LOG_PATH, 'a') as log:
            log.write(msg + '\n')
            log.close()


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/')
def index_route():
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz', code=302)

    return redirect('/en', code=302)

@sitemapper.include(lastmod='2025-05-26', changefreq='weekly', priority=1)
@app.route('/en')
def index_en_route():
    log_access('/en')
    return sezimal_render_template('sezimal_en.html')

@sitemapper.include(lastmod='2025-05-26', changefreq='weekly', priority=1)
@app.route('/pt')
def index_pt_route():
    log_access('/pt')
    return sezimal_render_template('sezimal_pt.html')

@sitemapper.include(lastmod='2025-05-26', changefreq='weekly', priority=1)
@app.route('/bz')
def index_bz_route():
    log_access('/bz')
    return sezimal_render_template('sezimal_bz.html')


@app.route('/comparing-fractions')
def comparing_fractions_route():
    log_access('/comparing-fractions')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/comparando-frações', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz', code=302)

    return redirect('/en/comparing-fractions', code=302)

@sitemapper.include(lastmod='2024-09-21', changefreq='weekly', priority=1)
@app.route('/en/comparing-fractions')
def comparing_fractions_en_route():
    log_access('/en/comparing-fractions')
    return sezimal_render_template('comparing_fractions_en.html')

@sitemapper.include(lastmod='2024-09-21', changefreq='weekly', priority=1)
@app.route('/pt/comparando-frações')
def comparing_fractions_pt_route():
    log_access('/pt/comparando-frações')
    return sezimal_render_template('comparing_fractions_pt.html')

@sitemapper.include(lastmod='2024-09-21', changefreq='weekly', priority=1)
@app.route('/bz/konparandu-frasoyns')
def comparing_fractions_bz_route():
    log_access('/bz/konparandu-frasoyns')
    return sezimal_render_template('comparing_fractions_bz.html')


@app.route('/comparing-bases')
def comparing_bases_route():
    log_access('/comparing-bases')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/comparando-bases', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz', code=302)

    return redirect('/en/comparing-bases', code=302)

@sitemapper.include(lastmod='2024-09-27', changefreq='weekly', priority=1)
@app.route('/en/comparing-bases')
def comparing_bases_en_route():
    log_access('/en/comparing-bases')
    return sezimal_render_template('comparing_bases_en.html')

@sitemapper.include(lastmod='2024-09-27', changefreq='weekly', priority=1)
@app.route('/pt/comparando-bases')
def comparing_bases_pt_route():
    log_access('/pt/comparando-bases')
    return sezimal_render_template('comparing_bases_pt.html')

@sitemapper.include(lastmod='2024-09-27', changefreq='weekly', priority=1)
@app.route('/bz/konparandu-bazis')
def comparing_bases_bz_route():
    log_access('/bz/konparandu-bazis')
    return sezimal_render_template('comparing_bases_bz.html')


def _date_to_json(sdt: SezimalDateTime, locale: SezimalLocale, base=10) -> dict:
    if base == 10:
        locale.to_short_year_format()
    elif base == 14:
        locale.to_decimal_base()
    elif base == 20:
        locale.to_dozenal_base()

    res = {
        'date_time': {
            'utc': {
                'iso':
                    sdt.format('ISO%+%5>Y-%5m-%5d %5H:%5M:%5S.%5f UTC%5:z', 'en').replace(',', '_', 1) if base == 10 else
                    sdt.format('ISO%+%Y-%m-%d %H:%M:%S.%f UTC%:z', 'en') if base == 14 else
                    sdt.format('ISO%+%↋>Y-%↋m-%↋d %↋H:%↋M:%↋S.%↋f UTC%↋:z', 'en'),
                'sym':
                    sdt.format('SYM#+#_Y-#m-#d #u:#p:#a.#n#b#x UTC#:t', 'en') if base == 10 else
                    sdt.format('SYM#9+#9sY-#9m-#9d %H:%M:%S.%f UTC%:z', 'en') if base == 14 else
                    sdt.format('SYM#↋+#↋sY-#↋m-#↋d #↋3.2fD UTC#↋↋t', 'en'),
                'dcc':
                    sdt.format('DCC&+&_Y&DS&m&DS&d #u:#p:#a.#n#b#x UTC#:t', 'en') if base == 10 else
                    sdt.format('DCC&9+&9Y&DS&9m&DS&9wM&DS&9dW %H:%M:%S.%f UTC%:z', 'en') if base == 14 else
                    sdt.format('DCC&↋+&↋Y&DS&↋m&DS&↋wM&DS&↋dW #↋3.2fD UTC#↋↋t', 'en'),
                'hol':
                    sdt.format('HOL%h+#_ghY-%5m-%5d %5H:%5M:%5S.%5f UTC%5:z', 'en').replace(',', '_', 1) if base == 10 else
                    sdt.format('HOL%h+#9_ghY-%m-%d %H:%M:%S.%f UTC%:z', 'en').replace(',', '_', 1) if base == 14 else
                    sdt.format('HOL%h+#↋_ghY-%↋m-%↋d %↋H:%↋M:%↋S.%↋f UTC%↋:z', 'en').replace(',', '_', 1),
            },
            'spm': {
                'iso':
                    sdt.format('ISO%+%5>Y-%5m-%5d %5H:%5M:%5S.%5f SPM%:ß', 'en').replace(',', '_', 1) if base == 10 else
                    sdt.format('ISO%+%Y-%m-%d %H:%M:%S.%f SPM%:ß', 'en') if base == 14 else
                    sdt.format('ISO%+%↋>Y-%↋m-%↋d %↋H:%↋M:%↋S.%↋f SPM%↋:ß', 'en'),
                'sym':
                    sdt.format('SYM#+#_Y-#m-#d #u:#p:#a.#n#b#x SPM#:ß', 'en') if base == 10 else
                    sdt.format('SYM#9+#9sY-#9m-#9d %H:%M:%S.%f SPM%:ß', 'en') if base == 14 else
                    sdt.format('SYM#↋+#↋sY-#↋m-#↋d #↋3.2fD SPM#↋↋ß', 'en'),
                'dcc':
                    sdt.format('DCC&+&_Y&DS&m&DS&d #u:#p:#a.#n#b#x SPM#:ß', 'en') if base == 10 else
                    sdt.format('DCC&9+&9Y&DS&9m&DS&9wM&DS&9dW %H:%M:%S.%f SPM%:ß', 'en') if base == 14 else
                    sdt.format('DCC&↋+&↋Y&DS&↋m&DS&↋wM&DS&↋dW #↋3.2fD SPM#↋↋ß', 'en'),
                'hol':
                    sdt.format('HOL%h+#ghY-%5m-%5d %5H:%5M:%5S.%5f SPM%:ß', 'en').replace(',', '_', 1) if base == 10 else
                    sdt.format('HOL%h+#9ghY-%m-%d %H:%M:%S.%f SPM%:ß', 'en').replace(',', '_', 1) if base == 14 else
                    sdt.format('HOL%h+#↋ghY-%↋m-%↋d %↋H:%↋M:%↋S.%↋f SPM%↋:ß', 'en').replace(',', '_', 1),
            },
            'julian_day':
                float(str(sdt.julian_day)) if base == 10 else
                float(str(sdt.julian_day.decimal)) if base == 14 else
                str(Dozenal(sdt.julian_day.decimal)),
            'rata_die':
                float(str(sdt.as_days)) if base == 10 else
                float(str(sdt.as_days.decimal)) if base == 14 else
                str(Dozenal(sdt.as_days.decimal)),
        },
        'date': {
            'iso': {
                'format': {
                    'numeric': sdt.format(locale.ISO_DATE_FORMAT, locale),
                    'text': sdt.format(locale.ISO_DATE_LONG_FORMAT, locale),
                    'numeric_weekday': sdt.format(locale.ISO_DATE_FULL_FORMAT, locale),
                    'text_weekday': sdt.format(locale.ISO_DATE_FULL_LONG_FORMAT, locale),
                    'full_year': {
                        'numeric': sdt.format(locale.ISO_DATE_FORMAT.replace('%5Y', "#'gY"), locale),
                        'text': sdt.format(locale.ISO_DATE_LONG_FORMAT.replace('%5Y', "#'gY"), locale),
                        'numeric_weekday': sdt.format(locale.ISO_DATE_FULL_FORMAT.replace('%5Y', "#'gY"), locale),
                        'text_weekday': sdt.format(locale.ISO_DATE_FULL_LONG_FORMAT.replace('%5Y', "#'gY"), locale),
                    },
                },
                'year':
                    int(str(SezimalInteger(sdt.gregorian_year))[-3:]) if base == 10 else
                    int(str(sdt.gregorian_year)) if base == 14 else
                    str(Dozenal(sdt.gregorian_year)),
                'full_year':
                    int(str(SezimalInteger(sdt.gregorian_year))) if base == 10 else
                    int(sdt.gregorian_year) if base == 14 else
                    str(Dozenal(sdt.gregorian_year)),
                'month':
                    int(str(SezimalInteger(sdt.gregorian_month))) if base == 10 else
                    int(sdt.gregorian_month) if base == 14 else
                    str(Dozenal(sdt.gregorian_month)),
                'day':
                    int(str(SezimalInteger(sdt.gregorian_day))) if base == 10 else
                    int(sdt.gregorian_day) if base == 14 else
                    str(Dozenal(sdt.gregorian_day)),
                'weekday':
                    int(str(sdt.weekday)) if base == 10 else
                    int(str(sdt.weekday.decimal)) if base == 14 else
                    str(sdt.weekday.dozenal),
                'is_leap_year': sdt.gregorian_is_leap,
                'month_name': sdt.format('%B', locale),
                'month_abbreviation': sdt.format('%b', locale),
                'weekday_name': sdt.format('%A', locale),
                'weekday_abbreviation': sdt.format('%a', locale),
            },
            'sym': {
                #
                # Date
                #
                'format': {
                    'numeric': sdt.format(locale.DATE_FORMAT, locale),
                    'text': sdt.format(locale.DATE_LONG_FORMAT, locale),
                    'numeric_weekday': sdt.format(locale.DATE_FULL_FORMAT, locale),
                    'text_weekday': sdt.format(locale.DATE_FULL_LONG_FORMAT, locale),
                    'full_year': {
                        'numeric': sdt.format(locale.DATE_FORMAT.replace('>', "'"), locale),
                        'text': sdt.format(locale.DATE_LONG_FORMAT.replace('>', "'"), locale),
                        'numeric_weekday': sdt.format(locale.DATE_FULL_FORMAT.replace('>', "'"), locale),
                        'text_weekday': sdt.format(locale.DATE_FULL_LONG_FORMAT.replace('>', "'"), locale),
                    },
                },
                'year':
                    int(str(sdt.year)[-3:]) if base == 10 else
                    int(str(sdt.symmetric_year)) if base == 14 else
                    str(Dozenal(Decimal(sdt.symmetric_year))),
                'full_year':
                    int(str(sdt.year)) if base == 10 else
                    int(str(sdt.symmetric_year)) if base == 14 else
                    str(Dozenal(Decimal(sdt.symmetric_year))),
                'month':
                    int(str(sdt.month)) if base == 10 else
                    int(str(sdt.month.decimal)) if base == 14 else
                    str(sdt.month.dozenal),
                'day':
                    int(str(sdt.day)) if base == 10 else
                    int(str(sdt.day.decimal)) if base == 14 else
                    str(sdt.day.dozenal),
                'weekday':
                    int(str(sdt.weekday)) if base == 10 else
                    int(str(sdt.weekday.decimal)) if base == 14 else
                    str(sdt.weekday.dozenal),
                'week_in_year':
                    int(str(sdt.week_in_year)) if base == 10 else
                    int(str(sdt.week_in_year.decimal)) if base == 14 else
                    str(sdt.week_in_year.dozenal),
                'day_in_year':
                    int(str(sdt.day_in_year)) if base == 10 else
                    int(str(sdt.day_in_year.decimal)) if base == 14 else
                    str(sdt.day_in_year.dozenal),
                'quarter':
                    int(str(sdt.quarter)) if base == 10 else
                    int(str(sdt.quarter.decimal)) if base == 14 else
                    str(sdt.quarter.dozenal),
                'month_in_quarter':
                    # int(str(sdt.month_in_quarter)) if base == 10 else
                    int(str(sdt.month_in_quarter.decimal)) if base == 14 else
                    str(sdt.month_in_quarter.dozenal),
                'week_in_quarter':
                    int(str(sdt.week_in_quarter)) if base == 10 else
                    int(str(sdt.week_in_quarter.decimal)) if base == 14 else
                    str(sdt.week_in_quarter.dozenal),
                'day_in_quarter':
                    int(str(sdt.day_in_quarter)) if base == 10 else
                    int(str(sdt.day_in_quarter.decimal)) if base == 14 else
                    str(sdt.day_in_quarter.dozenal),
                'total': {
                    'in_year': {
                        'quarters':
                            4 if base == 10 else
                            4 if base == 14 else
                            '4',
                        'months':
                            20 if base == 10 else
                            12 if base == 14 else
                            '10',
                        'weeks':
                            int(str(sdt.date.total_weeks_in_year)) if base == 10 else
                            int(str(sdt.date.total_weeks_in_year.decimal)) if base == 14 else
                            str(sdt.date.total_weeks_in_year.dozenal),
                        'days':
                            int(str(sdt.date.total_days_in_year)) if base == 10 else
                            int(str(sdt.date.total_days_in_year.decimal)) if base == 14 else
                            str(sdt.date.total_days_in_year.dozenal),
                    },
                    'in_quarter': {
                        'months':
                            3 if base == 10 else
                            3 if base == 14 else
                            '3',
                        'weeks':
                            int(str(sdt.date.total_weeks_in_quarter)) if base == 10 else
                            int(str(sdt.date.total_weeks_in_quarter.decimal)) if base == 14 else
                            str(sdt.date.total_weeks_in_quarter.dozenal),
                        'days':
                            int(str(sdt.date.total_days_in_quarter)) if base == 10 else
                            int(str(sdt.date.total_days_in_quarter.decimal)) if base == 14 else
                            str(sdt.date.total_days_in_quarter.dozenal),
                    },
                    'in_month': {
                        'weeks':
                            int(str(sdt.date.total_weeks_in_month)) if base == 10 else
                            int(str(sdt.date.total_weeks_in_month.decimal)) if base == 14 else
                            str(sdt.date.total_weeks_in_month.dozenal),
                        'days':
                            int(str(sdt.date.total_days_in_month)) if base == 10 else
                            int(str(sdt.date.total_days_in_month.decimal)) if base == 14 else
                            str(sdt.date.total_days_in_month.dozenal),
                    },
                    'in_week': {
                        'days':
                            11 if base == 10 else
                            7 if base == 14 else
                            '7',
                    },
                },
                'ellapsed_proportion': {
                    'year':
                            float(str(sdt.date.year_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.year_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.year_proportion_ellapsed), 10)),
                    'quarter':
                            float(str(sdt.date.quarter_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.quarter_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.quarter_proportion_ellapsed), 10)),
                    'month':
                            float(str(sdt.date.month_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.month_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.month_proportion_ellapsed), 10)),
                    'week':
                            float(str(sdt.date.week_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.week_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.week_proportion_ellapsed), 10)),
                    'day':
                            float(str(sdt.time.as_days)) if base == 10 else
                            float(str(sdt.time.as_days.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.time.as_days), 10)),
                },
                'is_leap_year': sdt.is_leap,
                'is_long_month': sdt.is_long_month,
                'month_name': sdt.format('#M', locale),
                'month_abbreviation': sdt.format('#@M', locale),
                'weekday_name': sdt.format('#W', locale),
                'weekday_abbreviation': sdt.format('#@W', locale),
            },
            'dcc': {
                #
                # Date
                #
                'format': {
                    'numeric': sdt.format(locale.DCC_DATE_FORMAT, locale),
                    'month_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE, locale),
                    'day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE_DAYS, locale),
                    'week_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE_WEEKS, locale),
                    'month_week_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE_MONTHS_WEEKS, locale),
                    'astronomical': {
                        'month_day': sdt.format(locale.ADC_DATE_LONG_FORMAT_ON_DATE, locale),
                        'month_week_day': sdt.format(locale.ADC_DATE_LONG_FORMAT_ON_DATE_WEEKS, locale),
                        'text': sdt.format(locale.ADC_DATE_LONG_FORMAT_ON_DATE_WEEKDAY, locale),
                    },
                    'counting': {
                        'month_day': sdt.format(locale.DCC_DATE_LONG_FORMAT, locale),
                        'day': sdt.format(locale.DCC_DATE_LONG_FORMAT_DAYS, locale),
                        'week_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_WEEKS, locale),
                        'month_week_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_MONTHS_WEEKS, locale),
                    },
                    'full_year': {
                        'numeric': sdt.format(locale.DCC_DATE_FORMAT.replace('>', ''), locale).replace('󱹭', "'"),
                        'month_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE.replace('>', ''), locale).replace('󱹭', "'"),
                        'day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE_DAYS.replace('>', ''), locale).replace('󱹭', "'"),
                        'week_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE_WEEKS.replace('>', ''), locale).replace('󱹭', "'"),
                        'month_week_day': sdt.format(locale.DCC_DATE_LONG_FORMAT_ON_DATE_MONTHS_WEEKS.replace('>', '').replace('󱹭', "'"), locale),
                        'astronomical': {
                            'day': sdt.format(locale.ADC_DATE_LONG_FORMAT_ON_DATE.replace('>', ''), locale).replace('󱹭', "'"),
                            'week_day': sdt.format(locale.ADC_DATE_LONG_FORMAT_ON_DATE_WEEKS.replace('>', ''), locale).replace('󱹭', "'"),
                            'text': sdt.format(locale.ADC_DATE_LONG_FORMAT_ON_DATE_WEEKDAY.replace('>', ''), locale).replace('󱹭', "'"),
                        },
                        'counting': {
                            'month_day': "213'" +  sdt.format(locale.DCC_DATE_LONG_FORMAT.replace('>', ''), locale),
                            'day': "213'" + sdt.format(locale.DCC_DATE_LONG_FORMAT_DAYS.replace('>', ''), locale),
                            'week_day': "213'" + sdt.format(locale.DCC_DATE_LONG_FORMAT_WEEKS.replace('>', ''), locale),
                            'month_week_day': "213'" + sdt.format(locale.DCC_DATE_LONG_FORMAT_MONTHS_WEEKS.replace('>', ''), locale),
                        },
                    },
                },
                'year':
                    int(str(sdt.dcc_year)[-3:]) if base == 10 else
                    int(str(sdt.dcc_year.decimal )) if base == 14 else
                    str(sdt.dcc_year.dozenal),
                'full_year':
                    int(str(sdt.dcc_year)) if base == 10 else
                    int(str(sdt.dcc_year.decimal )) if base == 14 else
                    str(sdt.dcc_year.dozenal),
                'month':
                    int(str(sdt.dcc_month)) if base == 10 else
                    int(str(sdt.dcc_month.decimal)) if base == 14 else
                    str(sdt.dcc_month.dozenal),
                'day':
                    int(str(sdt.day)) if base == 10 else
                    int(str(sdt.day.decimal)) if base == 14 else
                    str(sdt.day.dozenal),
                'weekday':
                    int(str(sdt.dcc_weekday)) if base == 10 else
                    int(str(sdt.dcc_weekday.decimal)) if base == 14 else
                    str(sdt.dcc_weekday.dozenal),
                'week_in_year':
                    int(str(sdt.dcc_week_in_year)) if base == 10 else
                    int(str(sdt.dcc_week_in_year.decimal)) if base == 14 else
                    str(sdt.dcc_week_in_year.dozenal),
                'day_in_year':
                    int(str(sdt.dcc_day_in_year)) if base == 10 else
                    int(str(sdt.dcc_day_in_year.decimal)) if base == 14 else
                    str(sdt.dcc_day_in_year.dozenal),
                'term':
                    int(str(sdt.dcc_term)) if base == 10 else
                    int(str(sdt.dcc_term.decimal)) if base == 14 else
                    str(sdt.dcc_term.dozenal),
                'month_in_term':
                    int(str(sdt.dcc_month_in_term)) if base == 10 else
                    int(str(sdt.dcc_month_in_term.decimal)) if base == 14 else
                    str(sdt.dcc_month_in_term.dozenal),
                'week_in_term':
                    int(str(sdt.dcc_week_in_term)) if base == 10 else
                    int(str(sdt.dcc_week_in_term.decimal)) if base == 14 else
                    str(sdt.dcc_week_in_term.dozenal),
                'day_in_term':
                    int(str(sdt.dcc_day_in_term)) if base == 10 else
                    int(str(sdt.dcc_day_in_term.decimal)) if base == 14 else
                    str(sdt.dcc_day_in_term.dozenal),
                'total': {
                    'in_year': {
                        'terms':
                            int(str(sdt.dcc_total_terms_in_year)) if base == 10 else
                            int(str(sdt.dcc_total_terms_in_year.decimal)) if base == 14 else
                            str(sdt.dcc_total_terms_in_year.dozenal),
                        'months':
                            int(str(sdt.dcc_total_months_in_year)) if base == 10 else
                            int(str(sdt.dcc_total_months_in_year.decimal)) if base == 14 else
                            str(sdt.dcc_total_months_in_year.dozenal),
                        'weeks':
                            int(str(sdt.dcc_total_weeks_in_year)) if base == 10 else
                            int(str(sdt.dcc_total_weeks_in_year.decimal)) if base == 14 else
                            str(sdt.dcc_total_weeks_in_year.dozenal),
                        'days':
                            int(str(sdt.dcc_total_days_in_year)) if base == 10 else
                            int(str(sdt.dcc_total_days_in_year.decimal)) if base == 14 else
                            str(sdt.dcc_total_days_in_year.dozenal),
                    },
                    'in_term': {
                        'months':
                            int(str(sdt.dcc_total_months_in_term)) if base == 10 else
                            int(str(sdt.dcc_total_months_in_term.decimal)) if base == 14 else
                            str(sdt.dcc_total_months_in_term.dozenal),
                        'weeks':
                            int(str(sdt.dcc_total_weeks_in_term)) if base == 10 else
                            int(str(sdt.dcc_total_weeks_in_term.decimal)) if base == 14 else
                            str(sdt.dcc_total_weeks_in_term.dozenal),
                        'days':
                            int(str(sdt.dcc_total_days_in_term)) if base == 10 else
                            int(str(sdt.dcc_total_days_in_term.decimal)) if base == 14 else
                            str(sdt.dcc_total_days_in_term.dozenal),
                    },
                    'in_month': {
                        'weeks':
                            int(str(sdt.dcc_total_weeks_in_month)) if base == 10 else
                            int(str(sdt.dcc_total_weeks_in_month.decimal)) if base == 14 else
                            str(sdt.dcc_total_weeks_in_month.dozenal),
                        'days':
                            int(str(sdt.dcc_total_days_in_month)) if base == 10 else
                            int(str(sdt.dcc_total_days_in_month.decimal)) if base == 14 else
                            str(sdt.dcc_total_days_in_month.dozenal),
                    },
                    'in_week': {
                        'days':
                            int(str(sdt.dcc_total_days_in_week)) if base == 10 else
                            int(str(sdt.dcc_total_days_in_week.decimal)) if base == 14 else
                            str(sdt.dcc_total_days_in_week.dozenal),
                    },
                },
                'ellapsed_proportion': {
                    'year':
                            float(str(sdt.date.dcc_year_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.dcc_year_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.dcc_year_proportion_ellapsed), 10)),
                    'term':
                            float(str(sdt.date.dcc_term_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.dcc_term_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.dcc_term_proportion_ellapsed), 10)),
                    'month':
                            float(str(sdt.date.dcc_month_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.dcc_month_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.dcc_month_proportion_ellapsed), 10)),
                    'week':
                            float(str(sdt.date.dcc_week_proportion_ellapsed)) if base == 10 else
                            float(str(sdt.date.dcc_week_proportion_ellapsed.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.date.dcc_week_proportion_ellapsed), 10)),
                    'day':
                            float(str(sdt.time.as_days)) if base == 10 else
                            float(str(sdt.time.as_days.decimal)) if base == 14 else
                            str(round(Dozenal(sdt.time.as_days), 10)),
                },
                'is_short_year': sdt.dcc_is_short_year,
                'month_name': sdt.format('&M', locale),
                'month_abbreviation': sdt.format('&@M', locale),
                'weekday_name': sdt.format('&W', locale),
                'weekday_abbreviation': sdt.format('&@W', locale),
                'term_name': sdt.format('&T', locale),
                'term_abbreviation': sdt.format('&@T', locale),
                'astronomical_month_name': sdt.format('&cM', locale),
                'astronomical_month_abbreviation': sdt.format('&c@M', locale),
                # 'astronomical_month_icon': sdt.format('&iM', locale),
                'astronomical_week_name': sdt.format('&cW', locale),
                'astronomical_week_abbreviation': sdt.format('&c@W', locale),
                # 'astronomical_week_icon': sdt.format('&iW', locale),
                'astronomical_day_name': sdt.format('&cD', locale),
                'astronomical_day_abbreviation': sdt.format('&c@D', locale),
                # 'astronomical_day_icon': sdt.format('&iD', locale),
            },
        },
        'time': {
            'format': sdt.format(locale.TIME_FORMAT, locale),
            'uta': int(str(sdt.uta)),
            'posha': int(str(sdt.posha)),
            'agrima': int(str(sdt.agrima)),
            'anuga': int(str(sdt.anuga)),
            'boda': int(str(sdt.boda)),
            'shaditiboda': int(str(sdt.shaditiboda)),
            'time_zone': str(sdt.time_zone),
            'utc_offset': sdt.format('#:t'),
            'spm_offset': sdt.format('#:ß'),
            'dst': sdt.is_dst,
        } if base == 10 else
        {
            'format': sdt.format(locale.TIME_FORMAT, locale),
            'hour': sdt.iso_time.hour,
            'hour_12': sdt.iso_time.hour if sdt.iso_time.hour <= 12 else sdt.iso_time.hour - 12,
            'hour_am_pm': 'am' if sdt.iso_time.hour <= 12 else 'pm',
            'minute': sdt.iso_time.minute,
            'second': sdt.iso_time.second,
            'time_zone': str(sdt.time_zone),
            'utc_offset': sdt.format('%:z'),
            'spm_offset': sdt.format('%:ß'),
            'dst': sdt.is_dst,
        } if base == 14 else
        {
            'format': sdt.format(locale.TIME_FORMAT, locale),
            'time_zone': str(sdt.time_zone),
            'utc_offset': sdt.format('#↋↋t'),
            'spm_offset': sdt.format('#↋↋ß'),
            'dst': sdt.is_dst,
        },
        'astronomical': {
            'season_name': sdt.format(f'#~{locale.DEFAULT_HEMISPHERE}S', locale),
            'season_emoji': sdt.format(f'#@~{locale.DEFAULT_HEMISPHERE}S', locale),
            'moon_name': sdt.format(f'#~{locale.DEFAULT_HEMISPHERE}L', locale),
            'moon_emoji': sdt.format(f'#@~{locale.DEFAULT_HEMISPHERE}L', locale),
        }
    }

    if base != 10:
        del res['date']['iso']['format']['full_year']
        del res['date']['iso']['full_year']

        del res['date']['sym']['format']['full_year']
        del res['date']['sym']['full_year']

        del res['date']['dcc']['format']['full_year']
        del res['date']['dcc']['full_year']

        del res['date']['dcc']['format']['month_day']
        del res['date']['dcc']['format']['day']
        del res['date']['dcc']['format']['week_day']
        del res['date']['dcc']['format']['astronomical']['month_day']
        del res['date']['dcc']['format']['counting']['month_day']
        del res['date']['dcc']['format']['counting']['day']
        del res['date']['dcc']['format']['counting']['week_day']
        del res['date']['dcc']['month_name']
        del res['date']['dcc']['month_abbreviation']
        del res['date']['dcc']['weekday_name']
        del res['date']['dcc']['weekday_abbreviation']
        del res['date']['dcc']['term_name']
        del res['date']['dcc']['term_abbreviation']

    else:
            res['date']['iso']['spellout'] = {
                'year': locale.spellout(str(SezimalInteger(sdt.gregorian_year))[-3:]),
                'full_year': locale.spellout(SezimalInteger(sdt.gregorian_year)),
                'month': locale.spellout(SezimalInteger(sdt.gregorian_month)),
                'day': locale.spellout(SezimalInteger(sdt.gregorian_day)),
                'weekday': locale.spellout(sdt.weekday),
            }
            res['date']['sym']['spellout'] = {
                'year': locale.spellout(str(sdt.year)[-3:]),
                'full_year': locale.spellout(sdt.year),
                'month': locale.spellout(sdt.month),
                'day': locale.spellout(sdt.day),
                'weekday': locale.spellout(sdt.weekday),
            }
            res['date']['dcc']['spellout'] = {
                'year': locale.spellout(str(sdt.dcc_year)[-3:]),
                'full_year': locale.spellout(sdt.dcc_year),
                'month': locale.spellout(sdt.dcc_month),
                'day': locale.spellout(sdt.dcc_day),
                'day_in_year': locale.spellout(sdt.dcc_day_in_year),
                'week_in_year': locale.spellout(sdt.dcc_week_in_year),
                'day_in_term': locale.spellout(sdt.dcc_day_in_term),
                'week_in_term': locale.spellout(sdt.dcc_week_in_term),
            }
            res['time']['spellout'] = {
                'uta': locale.spellout(sdt.uta),
                'posha': locale.spellout(sdt.posha),
                'agrima': locale.spellout(sdt.agrima),
                'anuga': locale.spellout(sdt.anuga),
                'boda': locale.spellout(sdt.boda),
                'shaditiboda': locale.spellout(sdt.shaditiboda),
            }

            if sdt.gregorian_year < 1980 or sdt.gregorian_year >= 2160:
                del res['date']['iso']['format']['full_year']
                res['date']['iso']['year'] = res['date']['iso']['full_year']
                del res['date']['iso']['full_year']
                res['date']['iso']['spellout']['year'] = res['date']['iso']['spellout']['full_year']
                del res['date']['iso']['spellout']['full_year']

            if sdt.year < 213_100 or sdt.year >= 214_000:
                del res['date']['sym']['format']['full_year']
                res['date']['sym']['year'] = res['date']['sym']['full_year']
                del res['date']['sym']['full_year']
                res['date']['sym']['spellout']['year'] = res['date']['sym']['spellout']['full_year']
                del res['date']['sym']['spellout']['full_year']

            if sdt.dcc_year < 213_100 or sdt.dcc_year >= 214_000:
                del res['date']['dcc']['format']['full_year']
                res['date']['dcc']['year'] = res['date']['dcc']['full_year']
                del res['date']['dcc']['full_year']
                res['date']['dcc']['spellout']['year'] = res['date']['dcc']['spellout']['full_year']
                del res['date']['dcc']['spellout']['full_year']

    if base != 14:
        res['date_time']['decimal'] = {
            'utc': {
                'iso': sdt.format('%Y-%m-%d %H:%M:%S.%f UTC%:z', 'en'),
                'sym': sdt.format('#9sY-#9m-#9d %H:%M:%S.%f UTC%:z', 'en'),
                'dcc': sdt.format('&9Y-&9m-&9wM-&9dW %H:%M:%S.%f UTC%:z', 'en'),
                'hol': sdt.format('#9_ghY-%m-%d %H:%M:%S.%f UTC%:z', 'en'),
            },
            'spm': {
                'iso': sdt.format('%Y-%m-%d %H:%M:%S.%f SPM%:ß', 'en'),
                'sym': sdt.format('#9sY-#9m-#9d %H:%M:%S.%f SPM%:ß', 'en'),
                'dcc': sdt.format('&9Y-&9m-&9wM-&9dW %H:%M:%S.%f SPM%:ß', 'en'),
                'hol': sdt.format('#9_ghY-%m-%d %H:%M:%S.%f SPM%:ß', 'en'),
            },
            'julian_day': float(sdt.julian_day.decimal),
            'rata_die': float(sdt.as_days.decimal),
        }

    return res


@app.route('/api/date-time')
@app.route('/api/date-time/<string:locale>')
@app.route('/api/date-time/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/<string:year>-<string:month>-<string:day>')
@app.route('/api/date-time/<string:year>-<string:month>-<string:day>/<string:locale>')
@app.route('/api/date-time/<string:year>-<string:month>-<string:day>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>')
@app.route('/api/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>')
@app.route('/api/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/-<string:negative_year>-<string:month>-<string:day>')
@app.route('/api/date-time/-<string:negative_year>-<string:month>-<string:day>/<string:locale>')
@app.route('/api/date-time/-<string:negative_year>-<string:month>-<string:day>/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>')
@app.route('/api/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>')
@app.route('/api/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>/<path:time_zone>')
def from_iso_date_time(
    year: str = None, negative_year: str = None, month: str = None, day: str = None,
    hour: str = None, minute: str = None, second: str = None,
    locale: str ='en', time_zone: str = None,
    base: int = 10,
) -> dict:
    log_access(request.path)
    locale = sezimal_locale(locale)

    if base == 14:
        locale.to_decimal_base()
    elif base == 20:
        locale.to_dozenal_base()

    time_zone = time_zone or locale.DEFAULT_TIME_ZONE

    if time_zone and time_zone.startswith('SPM') and 'SPM/' not in time_zone:
        time_zone = 'SPM/' + time_zone

    sdt = SezimalDateTime.now(time_zone)

    if year is None and negative_year is None:
        return _date_to_json(sdt, locale, base)

    if negative_year:
        year = int(negative_year) * -1

    sd = SezimalDate.from_gregorian(int(year), int(month), int(day))
    sdt = sdt.replace(year=sd.year, month=sd.month, day=sd.day)

    if hour is not None:
        st = SezimalTime.from_hour_minute_second(int(hour), int(minute), int(second), time_zone)
        sdt = sdt.replace(
            uta=st.uta, posha=st.posha, agrima=st.agrima,
            anuga=st.anuga, boda=st.boda, shaditiboda=st.shaditiboda
        )

    return _date_to_json(sdt, locale, base)


@app.route('/api/decimal/date-time')
@app.route('/api/decimal/date-time/<string:locale>')
@app.route('/api/decimal/date-time/<string:locale>/<path:time_zone>')
@app.route('/api/decimal/date-time/<string:year>-<string:month>-<string:day>')
@app.route('/api/decimal/date-time/<string:year>-<string:month>-<string:day>/<string:locale>')
@app.route('/api/decimal/date-time/<string:year>-<string:month>-<string:day>/<string:locale>/<path:time_zone>')
@app.route('/api/decimal/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>')
@app.route('/api/decimal/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>')
@app.route('/api/decimal/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>/<path:time_zone>')
@app.route('/api/decimal/date-time/-<string:negative_year>-<string:month>-<string:day>')
@app.route('/api/decimal/date-time/-<string:negative_year>-<string:month>-<string:day>/<string:locale>')
@app.route('/api/decimal/date-time/-<string:negative_year>-<string:month>-<string:day>/<string:locale>/<path:time_zone>')
@app.route('/api/decimal/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>')
@app.route('/api/decimal/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>')
@app.route('/api/decimal/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>/<path:time_zone>')
def from_iso_date_time_decimal(
    year: str = None, negative_year: str = None, month: str = None, day: str = None,
    hour: str = None, minute: str = None, second: str = None,
    locale: str ='en', time_zone: str = None,
    base: int = 10,
) -> dict:
    return from_iso_date_time(
        year, negative_year, month, day,
        hour, minute, second,
        locale, time_zone,
        base=14,
    )


@app.route('/api/dozenal/date-time')
@app.route('/api/dozenal/date-time/<string:locale>')
@app.route('/api/dozenal/date-time/<string:locale>/<path:time_zone>')
@app.route('/api/dozenal/date-time/<string:year>-<string:month>-<string:day>')
@app.route('/api/dozenal/date-time/<string:year>-<string:month>-<string:day>/<string:locale>')
@app.route('/api/dozenal/date-time/<string:year>-<string:month>-<string:day>/<string:locale>/<path:time_zone>')
@app.route('/api/dozenal/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>')
@app.route('/api/dozenal/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>')
@app.route('/api/dozenal/date-time/<string:year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>/<path:time_zone>')
@app.route('/api/dozenal/date-time/-<string:negative_year>-<string:month>-<string:day>')
@app.route('/api/dozenal/date-time/-<string:negative_year>-<string:month>-<string:day>/<string:locale>')
@app.route('/api/dozenal/date-time/-<string:negative_year>-<string:month>-<string:day>/<string:locale>/<path:time_zone>')
@app.route('/api/dozenal/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>')
@app.route('/api/dozenal/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>')
@app.route('/api/dozenal/date-time/-<string:negative_year>-<string:month>-<string:day>T<string:hour>:<string:minute>:<string:second>/<string:locale>/<path:time_zone>')
def from_iso_date_time_dozenal(
    year: str = None, negative_year: str = None, month: str = None, day: str = None,
    hour: str = None, minute: str = None, second: str = None,
    locale: str ='en', time_zone: str = None,
    base: int = 10,
) -> dict:
    return from_iso_date_time(
        year, negative_year, month, day,
        hour, minute, second,
        locale, time_zone,
        base=14,
    )


@app.route('/api/format/<string:locale>/<path:time_zone>')
def api_date(locale: str = None, time_zone: str = None) -> str:
    locale = sezimal_locale(locale or 'en')
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE

    if time_zone and time_zone.startswith('SPM') and 'SPM/' not in time_zone:
        time_zone = 'SPM/' + time_zone

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
