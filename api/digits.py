
import pathlib

TEMPLATE_PATH = pathlib.Path(__file__).parent.resolve().joinpath('template')


from flask import send_file, redirect, Response
from main import app
from  locale_detection import browser_preferred_locale


@app.route('/digits')
def digits_route() -> Response:
    if browser_preferred_locale()[0:2] == 'pt':
        return redirect('/pt/dígitos', code=302)

    elif browser_preferred_locale()[0:2] == 'bz':
        return redirect('/bz/díjitus', code=302)

    return redirect('/en/digits', code=302)

@app.route('/en/digits')
def digits_en_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('digits_en.html'), mimetype='text/html')

@app.route('/pt/dígitos')
def digits_pt_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('digits_pt.html'), mimetype='text/html')

@app.route('/bz/díjitus')
def digits_bz_route() -> Response:
    return send_file(TEMPLATE_PATH.joinpath('digits_bz.html'), mimetype='text/html')
