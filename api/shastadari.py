
from flask import render_template, redirect, Response
from main import app, sitemapper
from  locale_detection import browser_preferred_locale

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
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
    return render_template('shastadari_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/pt/xastadári')
def shastadari_pt_route() -> Response:
    return render_template('shastadari_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/bz/xastadari')
def shastadari_bz_route() -> Response:
    return render_template('shastadari_bz.html')


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
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
    return render_template('prefixes_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/prefixos')
def shastadari_prefixes_pt_route() -> Response:
    return render_template('prefixes_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/prefiksus')
def shastadari_prefixes_bz_route() -> Response:
    return render_template('prefixes_bz.html')


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
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
    return render_template('base_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-fundamentais')
def shastadari_base_units_pt_route() -> Response:
    if browser_preferred_locale()[-2:] in ('BR', 'br'):
        return render_template('base_units_pt_br.html')

    return render_template('base_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-fundamentays')
def shastadari_base_units_bz_route() -> Response:
    return render_template('base_units_bz.html')


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/time-units')
def shastadari_time_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-de-tempo', code=302)
    elif browser_preferred_locale()[0:2] == 'bf':
        return redirect('/bz/xastadari/unidadis-di-tenpu', code=302)

    return redirect('/en/shastadari/time-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/time-units')
def shastadari_time_units_en_route() -> Response:
    return render_template('time_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-de-tempo')
def shastadari_time_units_pt_route() -> Response:
    return render_template('time_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-di-tenpu')
def shastadari_time_units_bz_route() -> Response:
    return render_template('time_units_bz.html')


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/derived-units')
def shastadari_derived_units_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/unidades-derivadas', code=302)

    return redirect('/en/shastadari/derived-units', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/derived-units')
def shastadari_derived_units_en_route() -> Response:
    return render_template('derived_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/unidades-derivadas')
def shastadari_derived_units_pt_route() -> Response:
    if browser_preferred_locale()[-2:] in ('BR', 'br'):
        return render_template('derived_units_pt_br.html')

    return render_template('derived_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/unidadis-derivadas')
def shastadari_derived_units_bz_route() -> Response:
    return render_template('derived_units_bz.html')


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
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
    return render_template('other_units_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/outras-unidades')
def shastadari_other_units_pt_route() -> Response:
    return render_template('other_units_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/otras-unidadis')
def shastadari_other_units_bz_route() -> Response:
    return render_template('other_units_bz.html')


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/scales')
def shastadari_scales_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/escalas', code=302)

    return redirect('/en/shastadari/scales', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/scales')
def shastadari_scales_en_route() -> Response:
    if browser_preferred_locale().lower() == 'en-us':
        return render_template('scales_en_us.html')
    elif browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/escalas', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/eskalas', code=302)

    return render_template('scales_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/escalas')
def shastadari_scales_pt_route() -> Response:
    return render_template('scales_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/eskalas')
def shastadari_scales_bz_route() -> Response:
    return render_template('scales_bz.html')


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/shastadari/fractions')
def sezimal_fractions_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/xastadári/frações', code=302)
    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/xastadari/frasoyns', code=302)

    return redirect('/en/shastadari/fractions', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/en/shastadari/fractions')
def sezimal_fractions_en_route() -> Response:
    return render_template('fractions_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/pt/xastadári/frações')
def sezimal_fractions_pt_route() -> Response:
    return render_template('fractions_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/bz/xastadari/frasoyns')
def sezimal_fractions_bz_route() -> Response:
    return render_template('fractions_bz.html')
