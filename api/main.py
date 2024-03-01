
from flask import Flask
from swixknife.localization import sezimal_locale, SezimalLocale
from swixknife import SezimalDate, SezimalDateTime, SezimalTime, SezimalInteger
from decimal import Decimal
from swixknife import Sezimal, SezimalRange


app = Flask(__name__)
app.json.sort_keys = False


@app.route('/')
@app.route('/index.html')
def date_time_text():
    text = open('date_time.html').read()
    text = SezimalDateTime.now('UTC').format(text, 'en_gb')
    return text


@app.route('/api/now')
@app.route('/api/now/<string:locale>')
@app.route('/api/now/<string:locale>/<path:time_zone>')
@app.route('/api/date-time/now')
@app.route('/api/date-time/now/<string:locale>')
@app.route('/api/date-time/now/<string:locale>/<path:time_zone>')
def api_now(locale: str ='en', time_zone: str = None) -> str:
    locale = sezimal_locale(locale)
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE

    date_time = SezimalDateTime.now('UTC').at_time_zone(time_zone)

    text = open('now.html').read()

    date_format = locale.DATE_TIME_LONG_FORMAT.replace(locale.TIME_FORMAT, '')

    if date_format.endswith(', '):
        date_format = date_format[0:-2] + ' '

    if date_time.is_dst:
        if locale.RTL:
            time_format = '#@V ' + locale.TIME_FORMAT
        else:
            time_format = locale.TIME_FORMAT + ' #@V'

    else:
        time_format = locale.TIME_FORMAT

    if locale.RTL:
        season_format = f'#~{locale.DEFAULT_HEMISPHERE}S #@~{locale.DEFAULT_HEMISPHERE}S'
        moon_format = f'#~{locale.DEFAULT_HEMISPHERE}L #@~{locale.DEFAULT_HEMISPHERE}L'
    else:
        season_format = f'#@~{locale.DEFAULT_HEMISPHERE}S #~{locale.DEFAULT_HEMISPHERE}S'
        moon_format = f'#@~{locale.DEFAULT_HEMISPHERE}L #~{locale.DEFAULT_HEMISPHERE}L'

    return eval(f'f"""{text}"""')


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
            'julian_date': float(str(sdt.julian_date)),
            'rata_die': float(str(sdt.as_days)),
            'decimal_symmetry454': str(int(sdt.symmetric_year)).zfill(4) + sdt.format('-#9m-#9d %H:%M:%S.%f %:z', locale),
            'decimal_iso': sdt.format('%Y-%m-%d %H:%M:%S.%f %:z', locale),
            'decimal_julian_date': float(sdt.julian_date.decimal),
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


LOCALE_LIST = [
    'ar',
    'ar_latn',
    'bz',
    'ca',
    'de',
    'el',
    'en',
    'en_au',
    'en_br',
    'en_ca',
    'en_nz',
    'en_us',
    'en_shavian',
    'eo',
    'eo_br',
    'es',
    'es_ar',
    'es_bo',
    'es_cl',
    'es_co',
    'es_ec',
    'es_mx',
    'es_pe',
    'es_py',
    'es_uy',
    'fa',
    'fa_latn',
    'fr',
    'fr_ca',
    'fr_ch',
    'fr_ortograf',
    'ga',
    'ga_clo_gaelach',
    'ga_traditional',
    'gl',
    'gn',
    'he',
    'he_latn',
    'hi',
    'hi_latn',
    'hu',
    'id',
    'it',
    'ja',
    'ko',
    'nl',
    'pl',
    'pt',
    'pt_ao',
    'pt_br',
    'pt_ch',
    'pt_cv',
    'pt_gq',
    'pt_gw',
    'pt_lu',
    'pt_mo',
    'pt_mz',
    'pt_pt',
    'pt_st',
    'pt_tl',
    'ro',
    'ru',
    'sw',
    'sw_traditional',
    'tr',
    'uk',
    'vi',
    'yo',
    'yrl',
    'zh',
    'zh_cn',
    'zh_hk',
    'zh_mo',
    'zh_sg',
    'zh_tw',
    'zh_hans',
    'zh_hant',
    'zh_latn',
]


def _locale_info(locale: str = None) -> dict:
    locale = sezimal_locale(locale)

    res = {
        'lang': locale.LANG,
        'language_name': locale.LANGUAGE,
        'from_icu': str(locale.__class__).split('.')[2] == 'lokale',
        'script': {
            'is_rtl': locale.RTL,
            'ideographic_script': locale.IDEOGRAPHIC,
            'localized_digits': locale.DIGITS,
        },
        'number_format': {
            'sezimal_separator': locale.SEZIMAL_SEPARATOR,
            'group_separator': locale.GROUP_SEPARATOR,
            'subgroup_separator': locale.SUBGROUP_SEPARATOR,
            'fraction_group_separator': locale.FRACTION_GROUP_SEPARATOR,
            'fraction_subgroup_separator': locale.FRACTION_SUBGROUP_SEPARATOR,
        },
        'date_time_localization': {
            'default_time_zone': locale.DEFAULT_TIME_ZONE,
            'first_weekday': locale.FIRST_WEEKDAY,
            'day_of_rest': locale.FIRST_WEEKDAY,
            'optional_day_of_rest': locale.OPTIONAL_DAY_OF_REST,
            'weekday_name': locale.WEEKDAY_NAME,
            'weekday_abbreviated_name': locale.WEEKDAY_ABBREVIATED_NAME,
            'month_name': locale.MONTH_NAME,
            'month_abbreviated_name': locale.MONTH_ABBREVIATED_NAME,
            'era_name': locale.ERA_NAME,
            'day_ordinal_suffix': {},
        },
        'date_time_format': {
            'date_format': locale.DATE_FORMAT,
            'date_long_format': locale.DATE_LONG_FORMAT,
            'time_format': locale.TIME_FORMAT,
            'date_time_format': locale.DATE_TIME_FORMAT,
            'date_time_long_format': locale.DATE_TIME_LONG_FORMAT,
            'dst_name': locale.DST_NAME,
            'dst_short_name': locale.DST_SHORT_NAME,
            'iso_date_format': locale.ISO_DATE_FORMAT,
            'iso_time_format': locale.ISO_TIME_FORMAT,
        },
        'astronomic_events': {
            'default_hemisphere': locale.DEFAULT_HEMISPHERE,
            'season_name': locale.SEASON_NAME,
            'moonphase_name': locale.MOON_PHASE,
        },
    }

    for day in SezimalRange(100):
        od = locale.day_ordinal_suffix(day)

        if od:
            res['date_time_localization']['day_ordinal_suffix'][str(day)] = od

    return res


@app.route('/api/locale-info')
@app.route('/api/locale-info/<string:locale>')
def locale_list(locale: str = None):
    if locale is not None:
        return _locale_info(locale)

    res = {}

    for locale in LOCALE_LIST:
        res[locale] = _locale_info(locale)

    return res
