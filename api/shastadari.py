
from flask import redirect, Response, render_template
from main import app, sitemapper, sezimal_render_template
import main
from  locale_detection import browser_preferred_locale

from swixknife import sezimal_locale, sezimal_spellout, SezimalInteger
from swixknife.date_time import SezimalDateTime
from swixknife.functions import SezimalList, SezimalDictionary, SezimalRange

from decimal import Decimal
from datetime import datetime
from zoneinfo import ZoneInfo

from swixknife import Sezimal, SezimalFraction
from swixknife.units import \
    sezimal_to_decimal_unit as sdu, sezimal_to_sezimal_unit as ssu, \
    decimal_to_sezimal_unit as dsu, decimal_to_decimal_unit as ddu
from fractions import Fraction


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/shastadari')
def shastadari_route() -> Response:
    main.log_access('/shastadari')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari', code=302)

    return redirect('/en/shastadari', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/en/shastadari')
def shastadari_en_route() -> Response:
    main.log_access('/en/shastadari')
    return sezimal_render_template('shastadari_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/pt/xastadári')
def shastadari_pt_route() -> Response:
    main.log_access('/pt/xastadári')
    return sezimal_render_template('shastadari_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/bz/xastadari')
def shastadari_bz_route() -> Response:
    main.log_access('/bz/xastadari')
    return sezimal_render_template('shastadari_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/prefixes')
def shastadari_prefixes_route() -> Response:
    main.log_access('/shastadari/prefixes')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/prefixos', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/prefiksus', code=302)

    return redirect('/en/shastadari/prefixes', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/prefixes')
def shastadari_prefixes_en_route() -> Response:
    main.log_access('/en/shastadari/prefixes')
    return sezimal_render_template('prefixes_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/prefixos')
def shastadari_prefixes_pt_route() -> Response:
    main.log_access('/pt/xastadári/prefixos')
    return sezimal_render_template('prefixes_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/prefiksus')
def shastadari_prefixes_bz_route() -> Response:
    main.log_access('/bz/xastadari/prefiksus')
    return sezimal_render_template('prefixes_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/base-units')
def shastadari_base_units_route() -> Response:
    main.log_access('/shastadari/base-units')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-fundamentais', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/unidadis-fundamentays', code=302)

    return redirect('/en/shastadari/base-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/base-units')
def shastadari_base_units_en_route() -> Response:
    main.log_access('/en/shastadari/base-units')
    return sezimal_render_template('base_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-fundamentais')
def shastadari_base_units_pt_route() -> Response:
    main.log_access('/pt/xastadári/unidades-fundamentais')
    if browser_preferred_locale()[-2:] in ('BR', 'br'):
        return sezimal_render_template('base_units_pt_br.html')

    return sezimal_render_template('base_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-fundamentays')
def shastadari_base_units_bz_route() -> Response:
    main.log_access('/bz/xastadari/unidadis-fundamentays')
    return sezimal_render_template('base_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/time-units')
def shastadari_time_units_route() -> Response:
    main.log_access('/shastadari/time-units')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-de-tempo', code=302)
    elif browser_preferred_locale()[0:2] == 'bf':
        return redirect('/bz/xastadari/unidadis-di-tenpu', code=302)

    return redirect('/en/shastadari/time-units', code=302)

@sitemapper.include(lastmod='2024-09-16', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/time-units')
def shastadari_time_units_en_route() -> Response:
    main.log_access('/en/shastadari/time-units')
    return sezimal_render_template('time_units_en.html')

@sitemapper.include(lastmod='2024-09-16', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-de-tempo')
def shastadari_time_units_pt_route() -> Response:
    main.log_access('/pt/xastadári/unidades-de-tempo')
    return sezimal_render_template('time_units_pt.html')

@sitemapper.include(lastmod='2024-09-16', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-di-tenpu')
def shastadari_time_units_bz_route() -> Response:
    main.log_access('/bz/xastadari/unidadis-di-tenpu')
    return sezimal_render_template('time_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/derived-units')
def shastadari_derived_units_route() -> Response:
    main.log_access('/shastadari/derived-units')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-derivadas', code=302)

    return redirect('/en/shastadari/derived-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/derived-units')
def shastadari_derived_units_en_route() -> Response:
    main.log_access('/en/shastadari/derived-units')
    return sezimal_render_template('derived_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-derivadas')
def shastadari_derived_units_pt_route() -> Response:
    main.log_access('/pt/xastadári/unidades-derivadas')
    if browser_preferred_locale()[-2:] in ('BR', 'br'):
        return sezimal_render_template('derived_units_pt_br.html')

    return sezimal_render_template('derived_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-derivadas')
def shastadari_derived_units_bz_route() -> Response:
    main.log_access('/bz/xastadari/unidadis-derivadas')
    return sezimal_render_template('derived_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/other-units')
def shastadari_other_units_route() -> Response:
    main.log_access('/shastadari/other-units')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/outras-unidades', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/otras-unidadis', code=302)

    return redirect('/en/shastadari/other-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/other-units')
def shastadari_other_units_en_route() -> Response:
    main.log_access('/en/shastadari/other-units')
    return sezimal_render_template('other_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/outras-unidades')
def shastadari_other_units_pt_route() -> Response:
    main.log_access('/pt/xastadári/outras-unidades')
    return sezimal_render_template('other_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/otras-unidadis')
def shastadari_other_units_bz_route() -> Response:
    main.log_access('/bz/xastadari/otras-unidadis')
    return sezimal_render_template('other_units_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/scales')
def shastadari_scales_route() -> Response:
    main.log_access('/shastadari/scales')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/escalas', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/iskalas', code=302)

    return redirect('/en/shastadari/scales', code=302)

@sitemapper.include(lastmod='2024-09-13', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/scales')
def shastadari_scales_en_route() -> Response:
    main.log_access('/en/shastadari/scales')
    if browser_preferred_locale().lower() == 'en-us':
        return sezimal_render_template('scales_en_us.html')

    return sezimal_render_template('scales_en.html')

@sitemapper.include(lastmod='2024-09-13', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/escalas')
def shastadari_scales_pt_route() -> Response:
    main.log_access('/pt/xastadári/escalas')
    return sezimal_render_template('scales_pt.html')

@sitemapper.include(lastmod='2024-09-13', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/iskalas')
def shastadari_scales_bz_route() -> Response:
    main.log_access('/bz/xastadari/iskalas')
    return sezimal_render_template('scales_bz.html')


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/fractions')
def sezimal_fractions_route() -> Response:
    main.log_access('/shastadari/fractions')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/frações', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/frasoyns', code=302)

    return redirect('/en/shastadari/fractions', code=302)

@sitemapper.include(lastmod='2024-10-09', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/fractions')
def sezimal_fractions_en_route() -> Response:
    main.log_access('/en/shastadari/fractions')
    # return sezimal_render_template('fractions_en.html')
    return render_template('fractions_en.html')

@sitemapper.include(lastmod='2024-10-09', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/frações')
def sezimal_fractions_pt_route() -> Response:
    main.log_access('/pt/xastadári/frações')
    # return sezimal_render_template('fractions_pt.html')
    return render_template('fractions_pt.html')

@sitemapper.include(lastmod='2024-10-09', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/frasoyns')
def sezimal_fractions_bz_route() -> Response:
    main.log_access('/bz/xastadari/frasoyns')
    # return sezimal_render_template('fractions_bz.html')
    return render_template('fractions_bz.html')


@app.route('/en/conversion')
@app.route('/en/shastadari/conversion')
def shastadari_conversion_en_route() -> Response:
    main.log_access('/en/conversion')
    if browser_preferred_locale().lower() == 'en-us':
        return sezimal_render_template('conversion_en_us.html')

    return render_template('conversion_en.html')

@app.route('/pt/conversão')
@app.route('/pt/xastadári/conversão')
def shastadari_conversion_pt_route() -> Response:
    main.log_access('/pt/conversão')
    return render_template('conversion_pt.html')

@app.route('/bz/konversawn')
@app.route('/bz/xastadari/konversawn')
def shastadari_conversion_bz_route() -> Response:
    main.log_access('/bz/konversawn')
    return render_template('conversion_bz.html')


@app.route('/api/shastadari/length/<string:locale>/<string:unit>/<string:value>')
def shastadari_conversion_length(locale: str = 'en', unit: str = 'pad', value: str = '0') -> dict:
    locale = sezimal_locale(locale)

    if unit == 'pad':
        pada = SezimalFraction(value)
        meter = sdu(pada, 'pad', 'm').decimal
        inch = meter / Decimal('0.0254')
    else:
        meter = Decimal(value)

        if unit != 'm':
            inch = meter
            meter = inch * Decimal('0.0254')
        else:
            inch = meter / Decimal('0.0254')

        pada = dsu(meter, 'm', 'pad', True)

    def sf(pada):
        res = locale.format_number(
            round(pada, 3),
            sezimal_places=3,
            sezimal_punctuation=False,
            use_fraction_group_separator=True,
        )

        while res[-1] in ('0', '󱹭', '󱹬', locale.FRACTION_GROUP_SEPARATOR):
            res = res[0:-1]

        if res.endswith('󱹮'):
            res = res[0:-1]

        if res.endswith(locale.SEZIMAL_SEPARATOR):
            res = res[0:-1]

        return res

    def df(meter, dp=3):
        try:
            meter = meter.quantize(Decimal('10') ** (dp * -1))
        except:
            return '―'

        res = locale.format_decimal_number(
            meter,
            decimal_places=dp,
            use_fraction_group_separator=True,
        )

        if dp > 0:
            while res[-1] in ('0', locale.FRACTION_GROUP_SEPARATOR):
                res = res[0:-1]

            if res.endswith(locale.DECIMAL_SEPARATOR):
                res = res[0:-1]

        return res

    def format_inches(inches, suffix=' in', fraction_of=64):
        if inches == 0:
            return ''

        fi = ''

        if inches // 1 != 0:
            fi += df(inches // 1, 0)

        inches -= inches // 1
        inches = (inches * fraction_of) // 1

        if inches > 0:
            num, den = inches, fraction_of

            while (num % 2 == 0) and (den % 2 == 0):
                num //= 2
                den //= 2

            fi += ' ' + str(num) + '⁄' + str(den)

        return fi + suffix

    feet = inch / 12
    yard = inch / 36
    mile = inch / 63_360

    in_ = Decimal(0)
    ft_ = Decimal(0)
    yd_ = Decimal(0)
    mi_ = Decimal(0)

    inn = inch
    mi_yd_ft_in = ''

    if inn >= 63_360:
        mi_ = inn // 63_360
        mi_yd_ft_in += df(mi_, 0) + ' mi'
        inn -= mi_ * 63_360

    if inn >= 36:
        if mi_yd_ft_in:
            mi_yd_ft_in += ' '

        yd_ = inn // 36
        mi_yd_ft_in += df(yd_, 0) + ' yd'
        inn -= yd_ * 36

    if inn >= 12:
        if mi_yd_ft_in:
            mi_yd_ft_in += ' '

        ft_ = inn // 12
        mi_yd_ft_in += df(ft_, 0) + ' ft'
        inn -= ft_ * 12

    if inn > 0:
        if mi_yd_ft_in:
            mi_yd_ft_in += ' '
        in_ = inn
        mi_yd_ft_in += format_inches(inn, ' in')

    inn = inch
    ft_in = ''

    if inn >= 12:
        ft_in += df(inn // 12, 0) + '′'
        inn -= (inn // 12).quantize(Decimal('1')) * 12

    if inn > 0:
        if ft_in:
            ft_in += ' '

        ft_in += format_inches(inn, '″')

    res = {
        'xmpad': sf(pada / (Sezimal(10) ** 10)),
        'pmpad': sf(pada / (Sezimal(10) ** 5)),
        'cmpad': sf(pada / (Sezimal(10) ** 4)),
        'tmpad': sf(pada / (Sezimal(10) ** 3)),
        'dmpad': sf(pada / (Sezimal(10) ** 2)),
        'empad': sf(pada / (Sezimal(10) ** 1)),
        'pad': sf(pada),
        'eipad': sf(pada * (Sezimal(10) ** 1)),
        'dipad': sf(pada * (Sezimal(10) ** 2)),
        'tipad': sf(pada * (Sezimal(10) ** 3)),
        'cipad': sf(pada * (Sezimal(10) ** 4)),
        'pipad': sf(pada * (Sezimal(10) ** 5)),
        'xipad': sf(pada * (Sezimal(10) ** 10)),

        'Gm': df(meter / (Decimal(10) ** 6)),
        'km': df(meter / (Decimal(10) ** 3)),
        'hm': df(meter / (Decimal(10) ** 2)),
        'dam': df(meter / (Decimal(10) ** 1)),
        'm': df(meter),
        'dm': df(meter * (Decimal(10) ** 1)),
        'cm': df(meter * (Decimal(10) ** 2)),
        'mm': df(meter * (Decimal(10) ** 3)),
        'µm': df(meter * (Decimal(10) ** 6)),

        'mi': df(mi_),
        'yd': df(yd_),
        'ft': df(ft_),
        'in': df(in_),

        'mi_': df(mile),
        'yd_': df(yard),
        'ft_': df(feet),
        'in_': df(inch) + ' = ' + format_inches(inch, ''),
        'mi_yd_ft_in': mi_yd_ft_in,
        'ft_in': ft_in,
    }

    return res


@app.route('/api/shastadari/mass/<string:locale>/<string:unit>/<string:value>')
def shastadari_conversion_mass(locale: str = 'en', unit: str = 'drv', value: str = '0') -> dict:
    locale = sezimal_locale(locale)

    if unit == 'drv':
        dravya = SezimalFraction(value)
        gram = sdu(dravya, 'drv', 'g').decimal
        oz = gram / Decimal('28.349_523_125')
    else:
        gram = Decimal(value)

        if unit != 'kg':
            oz = gram
            gram = oz * Decimal('28.349_523_125')
        else:
            gram *= 1000
            oz = gram / Decimal('28.349_523_125')

        dravya = dsu(gram, 'g', 'drv', True)

    def sf(dravya):
        res = locale.format_number(
            round(dravya, 3),
            sezimal_places=3,
            sezimal_punctuation=False,
            use_fraction_group_separator=True,
        )

        while res[-1] in ('0', '󱹭', '󱹬', locale.FRACTION_GROUP_SEPARATOR):
            res = res[0:-1]

        if res.endswith('󱹮'):
            res = res[0:-1]

        if res.endswith(locale.SEZIMAL_SEPARATOR):
            res = res[0:-1]

        return res

    def df(gram, dp=3):
        try:
            gram = gram.quantize(Decimal('10') ** (dp * -1))
        except:
            return '―'

        res = locale.format_decimal_number(
            gram,
            decimal_places=dp,
            use_fraction_group_separator=True,
        )

        if dp > 0:
            while res[-1] in ('0', locale.FRACTION_GROUP_SEPARATOR):
                res = res[0:-1]

            if res.endswith(locale.DECIMAL_SEPARATOR):
                res = res[0:-1]

        return res

    oz_ = oz
    lb_ = oz / 16
    tn_ = oz / 32_000

    us_lb_oz = ''

    ozz = oz

    if ozz >= 16:
        us_lb_oz = df(ozz // 16, 0) + ' lb'
        ozz -= (ozz // 16) * 16

    if ozz > 0:
        if us_lb_oz:
            us_lb_oz += ' '

        us_lb_oz += df(ozz, 0) + ' oz'

    lb = Decimal(0)
    tn = Decimal(0)

    if oz >= 32_000:
        tn = oz // 32_000
        oz -= tn * 32_000

    if oz >= 16:
        lb = oz // 16
        oz -= lb * 16

    res = {
        'xmdrv': sf(dravya / (Sezimal(10) ** 10)),
        'pmdrv': sf(dravya / (Sezimal(10) ** 5)),
        'cmdrv': sf(dravya / (Sezimal(10) ** 4)),
        'tmdrv': sf(dravya / (Sezimal(10) ** 3)),
        'dmdrv': sf(dravya / (Sezimal(10) ** 2)),
        'emdrv': sf(dravya / (Sezimal(10) ** 1)),
        'drv': sf(dravya),
        'eidrv': sf(dravya * (Sezimal(10) ** 1)),
        'didrv': sf(dravya * (Sezimal(10) ** 2)),
        'tidrv': sf(dravya * (Sezimal(10) ** 3)),
        'cidrv': sf(dravya * (Sezimal(10) ** 4)),
        'pidrv': sf(dravya * (Sezimal(10) ** 5)),
        'xidrv': sf(dravya * (Sezimal(10) ** 10)),

        'Gg': df(gram / (Decimal(10) ** 6)),
        'kg': df(gram / (Decimal(10) ** 3)),
        'hg': df(gram / (Decimal(10) ** 2)),
        'dag': df(gram / (Decimal(10) ** 1)),
        'g': df(gram),
        'dg': df(gram * (Decimal(10) ** 1)),
        'cg': df(gram * (Decimal(10) ** 2)),
        'mg': df(gram * (Decimal(10) ** 3)),
        'µg': df(gram * (Decimal(10) ** 6)),

        'oz_': df(oz_),
        'lb_': df(lb_),
        'tn_': df(tn_),

        'us_lb_oz': us_lb_oz,

        'oz': df(oz),
        'lb': df(lb),
        'tn': df(tn),
    }

    return res

@app.route('/shastadari/currency')
def sezimal_currency_route() -> Response:
    main.log_access('/shastadari/currency')
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/frações', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/frasoyns', code=302)

    return redirect('/en/shastadari/currency', code=302)

@sitemapper.include(lastmod='2025-08-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/currency')
def sezimal_currency_en_route() -> Response:
    main.log_access('/en/shastadari/currency')
    # return sezimal_render_template('currency_en.html')
    return render_template('currency_en.html')

@sitemapper.include(lastmod='2025-08-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/moeda')
def sezimal_currency_pt_route() -> Response:
    main.log_access('/pt/xastadári/moeda')
    # return sezimal_render_template('currency_pt.html')
    return render_template('currency_pt.html')

@sitemapper.include(lastmod='2025-08-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/moèda')
def sezimal_currency_bz_route() -> Response:
    main.log_access('/bz/xastadari/moèda')
    # return sezimal_render_template('currency_bz.html')
    return render_template('currency_bz.html')
