
from main import app
from  locale_detection import browser_preferred_locale
from flask import Response

from swixknife.localization import sezimal_locale, SezimalLocale
from swixknife import SezimalDate, SezimalDateTime, SezimalTime
from decimal import Decimal
from swixknife import Sezimal, SezimalRange, SezimalInteger
from swixknife.units import sezimal_to_decimal_unit


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


@app.route('/now')
@app.route('/now/<string:locale>')
@app.route('/now/<string:locale>/<path:time_zone>')
def api_short_now(locale: str = None, time_zone: str = None) -> str:
    url = _manifest_url('now', locale, time_zone)
    locale = sezimal_locale(locale or browser_preferred_locale())
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


_TRANSLATIONS = {
    'ar': 'دلوقتي',  # delwaqti
    'bz': 'Agòra',
    'ca': 'Ara',
    'de': 'Jetzt',
    'el': 'Τώρα',
    'eo': 'Nun',
    'es': 'Ahora',
    'fa': 'حالا',
    'fr': 'Maintenant',
    'ga': 'Anois',
    'gl': 'Agora',
    'gn': 'Koꞌág̃a',
    'he': 'עכשיו',
    'hi': 'अब',
    'hu': 'Most',
    'id': 'Kini',
    'it': 'Adesso',
    'ja': '今',
    'ko': '지금',
    'nl': 'Nu',
    'pl': 'Teraz',
    'pt': 'Agora',
    'ro': 'Acum',
    'ru': 'Сейчас',
    'sw': 'Sasa',
    'tr': 'Şimdi',
    'uk': 'Тепер',
    'vi': 'Bây giờ',
    'yo': 'Báyìí',
    'zh': '現在',
    'zh_CN': '现在',
}


@app.route('/now/manifest.webmanifest')
def now_manifest() -> str:
    text = open('template/manifest_now.json').read()

    pl = browser_preferred_locale()

    if '_' in pl:
        lang = pl.split('_')[0]
    elif '-' in pl:
        lang = pl.split('-')[0]
    else:
        lang = pl

    if lang in _TRANSLATIONS:
        if pl in _TRANSLATIONS:
            text = text.replace('"Sezimal Now"', f'"{_TRANSLATIONS[pl]}"')
        else:
            text = text.replace('"Sezimal Now"', f'"{_TRANSLATIONS[lang]}"')

    if 'pt-' in pl or pl == 'pt':
        text = text.replace('"Sezimal calendar and clock"', '"Calendário e relógio sezimais"')
    elif 'bz-' in pl or pl == 'bz':
        text = text.replace('"Sezimal calendar and clock"', '"Kalendaryu i relòjyu sezimaw"')

    return text


@app.route('/now/now-icon.svg')
def now_icon() -> str:
    text = open('static/img/now-icon.svg').read()

    locale = sezimal_locale(browser_preferred_locale())

    date_time = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    uta_angle = round(date_time.uta / 100 * 1400, 0)
    posha_angle = round(date_time.posha / 100 * 1400, 0)
    agrima_angle = round((date_time.agrima + (date_time.anuga / 100) + (date_time.boda / 10_000)) / 100 * 1400, 0)

    date_parts = date_time.format(
        locale.DATE_FORMAT.replace('#d', '#-d').replace('#?d', '#?-d').replace('#m', '#M').replace('#?m', '#M'),
        locale,
    ).split(locale.DATE_SEPARATOR)

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
        f'id="face_uta" transform="rotate({uta_angle.decimal},216,216)"',
    )
    text = text.replace(
        'id="face_posha" transform="rotate(60,216,216)"',
        f'id="face_posha" transform="rotate({posha_angle.decimal},216,216)"',
    )
    text = text.replace(
        'id="face_agrima" transform="rotate(150,216,216)"',
        f'id="face_agrima" transform="rotate({agrima_angle.decimal + 10},216,216)"',
    )

    return Response(text, mimetype='image/svg+xml')


@app.route('/now/now-icon-sd.svg')
def now_icon_sd() -> str:
    text = open('static/img/now-icon-sd.svg').read()

    locale = sezimal_locale(browser_preferred_locale())

    date_time = SezimalDateTime.now(time_zone=locale.DEFAULT_TIME_ZONE)

    uta_angle = round(date_time.uta / 100 * 1400, 0)
    posha_angle = round(date_time.posha / 100 * 1400, 0)
    agrima_angle = round((date_time.agrima + (date_time.anuga / 100) + (date_time.boda / 10_000)) / 100 * 1400, 0)

    date_parts = date_time.format(
        locale.DATE_FORMAT.replace('#d', '#-d').replace('#?d', '#-d').replace('#m', '#M').replace('#?m', '#M').replace('#?Y', '#Y').replace('#', '#!'),
        locale,
    ).split(locale.DATE_SEPARATOR)

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
        f'id="face_uta" transform="rotate({uta_angle.decimal},216,216)"',
    )
    text = text.replace(
        'id="face_posha" transform="rotate(60,216,216)"',
        f'id="face_posha" transform="rotate({posha_angle.decimal},216,216)"',
    )
    text = text.replace(
        'id="face_agrima" transform="rotate(150,216,216)"',
        f'id="face_agrima" transform="rotate({agrima_angle.decimal + 10},216,216)"',
    )

    return Response(text, mimetype='image/svg+xml')
