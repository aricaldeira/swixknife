
from flask import redirect, Response, render_template
from main import app, sitemapper, sezimal_render_template
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

from pybrasil.valor import formata_metros_em_milhas_jardas_pes_polegadas, \
    converte_metros_para_milhas_jardas_pes_polegadas, \
    formata_metros_em_pes_polegadas


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


@app.route('/en/conversion')
def shastadari_conversion_en_route() -> Response:
    if browser_preferred_locale().lower() == 'en-us':
        return sezimal_render_template('conversion_en_us.html')

    return render_template('conversion_en.html')

@app.route('/pt/conversão')
def shastadari_conversion_pt_route() -> Response:
    return render_template('conversion_pt.html')

@app.route('/bz/konversawn')
def shastadari_conversion_bz_route() -> Response:
    return render_template('conversion_bz.html')


@app.route('/api/shastadari/length/<string:locale>/<string:unit>/<string:value>')
def shastadari_conversion_length(locale: str = 'en', unit: str = 'pad', value: str = '0') -> dict:
    locale = sezimal_locale(locale)

    if unit == 'pad':
        pada = SezimalFraction(value)
        meter = sdu(pada, 'pad', 'm').decimal
    else:
        meter = Decimal(value)

        if unit != 'm':
            meter = ddu(meter, unit, 'm').decimal

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

    def df(meter):
        try:
            meter = meter.quantize(Decimal('0.001'))
        except:
            return '―'

        res = locale.format_decimal_number(
            meter,
            decimal_places=3,
            use_fraction_group_separator=True,
        )

        while res[-1] in ('0', locale.FRACTION_GROUP_SEPARATOR):
            res = res[0:-1]

        if res.endswith(locale.DECIMAL_SEPARATOR):
            res = res[0:-1]

        return res

    mile, yard, feet, inch = converte_metros_para_milhas_jardas_pes_polegadas(meter)

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

        'ml': df(mile),
        'yd': df(yard),
        'ft': df(feet),
        'in': df(inch),

        'ml_': df(ddu(meter, 'm', 'ml').decimal),
        'yd_': df(ddu(meter, 'm', 'yd').decimal),
        'ft_': df(ddu(meter, 'm', 'ft').decimal),
        'in_': df(ddu(meter, 'm', 'in').decimal),
        'ml_yd_ft_in': formata_metros_em_milhas_jardas_pes_polegadas(meter, casas_decimais=3, usa_fracao=True),
        'ft_in': formata_metros_em_pes_polegadas(meter, casas_decimais=3, usa_fracao=True),
    }

    return res
