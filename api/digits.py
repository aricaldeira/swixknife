
from flask import render_template, redirect, Response
from main import app, sitemapper
from  locale_detection import browser_preferred_locale


# @sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/digits')
def digits_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/dígitos', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/díjitus', code=302)

    return redirect('/en/digits', code=302)

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/en/digits')
def digits_en_route() -> Response:
    return render_template('digits_en.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/pt/dígitos')
def digits_pt_route() -> Response:
    return render_template('digits_pt.html')

@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/bz/díjitus')
def digits_bz_route() -> Response:
    return render_template('digits_bz.html')
