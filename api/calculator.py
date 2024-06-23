
from flask import send_file, Response, request, jsonify
import json
from swixknife.localization import sezimal_locale
from swixknife.calculator import SezimalCalculator
from swixknife.units import sezimal_to_decimal_unit
from swixknife import Sezimal

from main import app


UNIT_SIMPLIFIED_SYMBOL = {
    'tap': '\N{NNBSP}°S',
    'p/n': '󱹹 (p/n)',
    'p/a': '󱹹 (p/a)',
    'p/sa': '󱹻 (p/sa)',
    'p/na': '󱹼 (p/na)',
    'p/x': '󱹽 (p/x)',
    'p/sx': '󱹾 (p/sx)',
    'p/nx': '󱹿 (p/nx)',
    'p/ax': '󱺀 (p/ax)',
    'p/sax': '󱺁 (p/sax)',
    'p/nax': '󱺂 (p/nax)',
    'p/Dx': '󱺃 (p/Dx)',
    'p/Tx': '󱺄 (p/Tx)',
    'p/Cx': '󱺅 (p/Cx)',
    'p/Px': '󱺆 (p/Px)',
    'p/Xx': '󱺇 (p/Xx)',
    'eprt': '\N{NNBSP}eprt (󱺈 per six)',
    'dprt': '\N{NNBSP}dprt (󱺉 per nif)',
    'tprt': '\N{NNBSP}tprt (󱺊 per arda)',
    'cprt': '\N{NNBSP}cprt (󱺋 per six arda)',
    'pprt': '\N{NNBSP}pprt (󱺌 per nif arda)',
    'xprt': '\N{NNBSP}pprt (󱺍 per shadara)',
    'xeprt': '\N{NNBSP}xeprt (󱺎 per six shadara)',
    'xdprt': '\N{NNBSP}xdprt (󱺏 per nif shadara)',
}


@app.route('/calculator')
def api_calculator() -> Response:
    return send_file('template/calculator.html', mimetype='text/html', as_attachment=False)


@app.route('/static/css/calculator.css')
def api_calculator_style() -> Response:
    return send_file('static/css/calculator.css', mimetype='text/css', as_attachment=False)


@app.route('/calculator/process', methods=['POST'])
def api_calculator_process() -> dict:
    dados = json.loads(request.data.decode('utf-8'))
    dados['base'] = int(dados['base'])
    dados['places'] = int(dados['places'])
    dados['grouping'] = int(dados['grouping'])
    dados['sezimal_digits'] = dados['sezimal_digits'] == 'true'
    dados['spellout'] = dados['spellout'] == 'true'

    print('dados', dados)

    calculator = SezimalCalculator()
    calculator.locale = dados['locale']
    calculator.grouping_digits = dados['grouping']
    calculator.decimal = False
    calculator.precision = dados['places']
    calculator.decimal = dados['base'] == 14
    calculator.sezimal_digits = dados['sezimal_digits']
    calculator.regularized_digits = dados['niftimal'] != 'Z'
    calculator.unit = dados['sezimal_unit']
    # calculator.suffix = dados['sezimal_unit']
    calculator.decimal_unit = dados['decimal_unit']
    # calculator.decimal_suffix = dados['decimal_unit']
    calculator.debug = True

    if not dados['value']:
        calculator.expression = dados['expression']
    elif dados['value'] == '=':
        calculator.expression = dados['expression']
        calculator.eval_expression()
    elif dados['value'] == 'C':
        calculator.expression = '0'
    elif dados['value'] == '⌫':
        if len(dados['expression']) <= 1:
            calculator.expression = '0'
        else:
            calculator.expression = dados['expression'].strip()[:-1]
    elif dados['value'] == '.':
        if dados['expression'].endswith('..'):
            pass

        elif '.' in dados['expression'] and dados['expression'][-1] != '.':
            parts = dados['expression'].replace('_', '').split('.')

            if len(parts) >= 2 and parts[-1].isdigit() and parts[-2].isdigit():
                calculator.expression = dados['expression'] + dados['value'] + dados['value']

        else:
            calculator.expression = dados['expression'] + dados['value']

    elif dados['value'] == '*' and dados['expression'].endswith('* '):
        calculator.expression = dados['expression'][:-2] + '^'

    elif dados['value'] == '/' and dados['expression'].endswith(' / '):
        calculator.expression = dados['expression'][:-3] + '⁄'

    elif dados['value'] == '%' and dados['expression'].endswith('% '):
        calculator.expression = dados['expression'][:-2] + '‰ '

    elif dados['value'] == '%' and dados['expression'].endswith('‰ '):
        calculator.expression = dados['expression'][:-2] + '‱ '

    elif dados['value'] == '%' and dados['expression'].endswith('‱ '):
        calculator.expression = dados['expression'][:-2] + '% '

    # elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺈 '):
    #     calculator.expression = dados['expression'][:-2] + '󱺉 '

    elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺉 '):
        calculator.expression = dados['expression'][:-2] + '󱺊 '

    elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺊 '):
        calculator.expression = dados['expression'][:-2] + '󱺋 '

    elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺋 '):
        calculator.expression = dados['expression'][:-2] + '󱺌 '

    elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺌 '):
        calculator.expression = dados['expression'][:-2] + '󱺍 '

    elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺍 '):
        calculator.expression = dados['expression'][:-2] + '󱺉 '

    # elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺎 '):
    #     calculator.expression = dados['expression'][:-2] + '󱺏 '
    #
    # elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺏 '):
    #     calculator.expression = dados['expression'][:-2] + '󱺐 '
    #
    # elif dados['value'] == '󱺉' and dados['expression'].endswith('󱺐 '):
    #     calculator.expression = dados['expression'][:-2] + '󱺉 '

    else:
        if dados['expression'] == '0':
            if dados['value'] == '.':
                calculator.expression = dados['expression'] + dados['value']
            elif dados['expression'] in '0123456789↊↋':
                calculator.expression = dados['value']
            else:
                calculator.expression = dados['expression'] + dados['value']

        else:
            calculator.expression = dados['expression'] + dados['value']

    resposta = {
        'expression': calculator.sezimal_expression,
        'decimal_expression': calculator.decimal_expression,
        'display': calculator.display,
        'decimal_display': calculator.decimal_display,
        'niftimal_display': calculator.niftimal_display,
        'show_spellout': False,
        'spellout': '',
        'separator': calculator.locale.SEZIMAL_SEPARATOR,
        'group_separator': calculator.locale.GROUP_SEPARATOR,
    }

    if not calculator.error:
        if dados['sezimal_unit']:
            if dados['sezimal_unit'] in UNIT_SIMPLIFIED_SYMBOL:
                resposta['display'] += UNIT_SIMPLIFIED_SYMBOL[dados['sezimal_unit']]
            else:
                resposta['display'] += '\N{NNBSP}' + dados['sezimal_unit']

        if dados['decimal_unit']:
            if dados['decimal_unit'] in '%‰‱':
                resposta['decimal_display'] += dados['decimal_unit']
            else:
                resposta['decimal_display'] += '\N{NNBSP}' + dados['decimal_unit']

        if dados['spellout']:
            resposta['show_spellout'] = True
            resposta['spellout'] = calculator.spellout

    print('resposta', resposta)

    return jsonify(resposta)

@app.route('/manifest_calculator.json')
def calculator_manifest() -> str:
    text = open('template/manifest_calculator.json').read()
    return text