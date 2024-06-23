
from main import app

from swixknife.localization import sezimal_locale, SezimalLocale
from swixknife import SezimalDate, SezimalDateTime, SezimalTime
from decimal import Decimal
from swixknife import Sezimal, SezimalRange, SezimalInteger
from swixknife.units import sezimal_to_decimal_unit
from swixknife.weather.weather import SezimalWeather


@app.route('/long-now')
@app.route('/long-now/<string:locale>')
@app.route('/long-now/<string:locale>/<path:time_zone>')
def api_long_now(locale: str = None, time_zone: str = None) -> str:
    url = _manifest_url('long-now', locale, time_zone)
    locale = sezimal_locale(locale or 'en')
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE
    digits = locale.DIGITS

    date_time = SezimalDateTime.now(time_zone=time_zone)
    time_zone_offset = sezimal_to_decimal_unit(date_time.time._time_zone_offset, 'agm', 'ms')

    text = open('template/long-now.html').read()

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

def _manifest_url(base, locale, time_zone):
    url = base

    if locale:
        url += '___' + locale

    if time_zone:
        url += '___' + time_zone.replace('/', '__')

    return url

@app.route('/manifest___<string:base>.json')
@app.route('/manifest___<string:base>___<string:locale>.json')
@app.route('/manifest___<string:base>___<string:locale>___<string:time_zone>.json')
def api_manifest(base: str = 'now', locale: str = None, time_zone: str = None) -> str:
    url = _manifest_url(base, locale, time_zone)
    url = url.replace('___', '/')
    url = url.replace('__', '/')
    text = open('template/manifest.json').read()
    return eval(f'f"""{text}"""')


@app.route('/now')
@app.route('/now/<string:locale>')
@app.route('/now/<string:locale>/<path:time_zone>')
def api_short_now(locale: str = None, time_zone: str = None) -> str:
    url = _manifest_url('now', locale, time_zone)
    locale = sezimal_locale(locale or 'en')
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE
    digits = locale.DIGITS

    date_time = SezimalDateTime.now(time_zone=time_zone)
    time_zone_offset = sezimal_to_decimal_unit(date_time.time._time_zone_offset, 'agm', 'ms')

    text = open('template/now.html').read()

    date_format = locale.DATE_FORMAT

    if date_time.is_dst:
        if locale.RTL:
            time_format = '#@V ' + locale.TIME_FORMAT
        else:
            time_format = locale.TIME_FORMAT + ' #@V'

    else:
        time_format = locale.TIME_FORMAT

    season_format = f'#@~{locale.DEFAULT_HEMISPHERE}S'
    moon_format = f'#@~{locale.DEFAULT_HEMISPHERE}L'

    if locale.LANG.startswith('en') \
        or locale.LANG.startswith('pt') \
        or locale.LANG.startswith('bz'):

        sf = locale.DATE_TIME_LONG_FORMAT.replace(locale.TIME_FORMAT, '')

        if sf.endswith(', '):
            sf = sf[0:-2]

        spellout_year = locale.spellout(date_time.year)
        sf = sf.replace('#Y', spellout_year)
        sf = sf.replace('#y', spellout_year)
        sf = sf.replace('#-y', spellout_year)

        if '#O' in sf and locale.day_ordinal_suffix(date_time.day) != '':
            sf = sf.replace('#d#O', locale.spellout('ordinal ' + str(date_time.day)))
            sf = sf.replace('#-d#O', locale.spellout('ordinal ' + str(date_time.day)))
        else:
            sf = sf.replace('#d', locale.spellout(date_time.day))
            sf = sf.replace('#-d', locale.spellout(date_time.day))

        spellout = date_time.format(sf, locale)

    else:
        spellout_year = ''
        spellout = ''

    return eval(f'f"""{text}"""')


@app.route('/agòra')
@app.route('/agòra/<string:locale>')
@app.route('/agòra/<string:locale>/<path:time_zone>')
def api_agòra(locale: str = None, time_zone: str = None, weather: bool = False) -> str:
    url = _manifest_url('agòra', locale, time_zone)
    locale = sezimal_locale(locale or 'bz')
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE
    digits = locale.DIGITS

    date_time = SezimalDateTime.now(time_zone=time_zone)
    time_zone_offset = sezimal_to_decimal_unit(date_time.time._time_zone_offset, 'agm', 'ms')

    text = open('template/agòra.html').read()

    date_format = locale.DATE_FORMAT

    if date_time.is_dst:
        if locale.RTL:
            time_format = '#@V ' + locale.TIME_FORMAT
        else:
            time_format = locale.TIME_FORMAT + ' #@V'

    else:
        time_format = locale.TIME_FORMAT

    season_format = f'#@~{locale.DEFAULT_HEMISPHERE}S'
    moon_format = f'#@~{locale.DEFAULT_HEMISPHERE}L'

    if locale.LANG.startswith('en') \
        or locale.LANG.startswith('pt') \
        or locale.LANG.startswith('bz'):

        sf = locale.DATE_TIME_LONG_FORMAT.replace(locale.TIME_FORMAT, '')

        if sf.endswith(', '):
            sf = sf[0:-2]

        spellout_year = locale.spellout(date_time.year)
        sf = sf.replace('#Y', spellout_year)
        sf = sf.replace('#y', spellout_year)
        sf = sf.replace('#-y', spellout_year)

        if '#O' in sf and locale.day_ordinal_suffix(date_time.day) != '':
            sf = sf.replace('#d#O', locale.spellout('ordinal ' + str(date_time.day)))
            sf = sf.replace('#-d#O', locale.spellout('ordinal ' + str(date_time.day)))
        else:
            sf = sf.replace('#d', locale.spellout(date_time.day))
            sf = sf.replace('#-d', locale.spellout(date_time.day))

        spellout = date_time.format(sf, locale)

    else:
        spellout_year = ''
        spellout = ''

    sw = SezimalWeather(locale, time_zone)
    sw.get_openweathermap_conditions()
    sezimal_temperature = locale.format_number(sw.temperature_sensation, 0) + '\N{NNBSP}°S'
    decimal_temperature = locale.format_decimal_number(sezimal_to_decimal_unit(sw.temperature_sensation, 'tap', '°C'), 1) + '\N{NNBSP}°C'

    return eval(f'f"""{text}"""')


@app.route('/decimal-now')
@app.route('/decimal-now/<string:locale>')
@app.route('/decimal-now/<string:locale>/<path:time_zone>')
def api_decimal_now(locale: str = None, time_zone: str = None) -> str:
    url = _manifest_url('decimal-now', locale, time_zone)
    locale = sezimal_locale(locale or 'en')
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE
    digits = locale.DIGITS

    date_time = SezimalDateTime.now(time_zone=time_zone)
    time_zone_offset = sezimal_to_decimal_unit(date_time.time._time_zone_offset, 'agm', 'ms')

    text = open('template/decimal-now.html').read()

    date_format = locale.DATE_FORMAT

    if date_time.is_dst:
        if locale.RTL:
            time_format = '#@V ' + locale.TIME_FORMAT
        else:
            time_format = locale.TIME_FORMAT + ' #@V'

    else:
        time_format = locale.TIME_FORMAT

    season_format = f'#@~{locale.DEFAULT_HEMISPHERE}S'
    moon_format = f'#@~{locale.DEFAULT_HEMISPHERE}L'

    return eval(f'f"""{text}"""')


@app.route('/dozenal-now')
@app.route('/dozenal-now/<string:locale>')
@app.route('/dozenal-now/<string:locale>/<path:time_zone>')
def api_dozenal_now(locale: str = None, time_zone: str = None) -> str:
    url = _manifest_url('dozenal-now', locale, time_zone)
    locale = sezimal_locale(locale or 'en')
    time_zone = time_zone or locale.DEFAULT_TIME_ZONE
    digits = locale.DIGITS

    date_time = SezimalDateTime.now(time_zone=time_zone)
    time_zone_offset = sezimal_to_decimal_unit(date_time.time._time_zone_offset, 'agm', 'ms')

    text = open('template/dozenal-now.html').read()

    date_format = locale.DATE_FORMAT

    if date_time.is_dst:
        if locale.RTL:
            time_format = '#@V ' + locale.TIME_FORMAT
        else:
            time_format = locale.TIME_FORMAT + ' #@V'

    else:
        time_format = locale.TIME_FORMAT

    season_format = f'#@~{locale.DEFAULT_HEMISPHERE}S'
    moon_format = f'#@~{locale.DEFAULT_HEMISPHERE}L'

    return eval(f'f"""{text}"""')
