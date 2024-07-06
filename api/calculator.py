
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
    'eprt': '\N{NNBSP}eprt (󱹰)',
    'dprt': '\N{NNBSP}dprt (󱹱)',
    'tprt': '\N{NNBSP}tprt (󱹲)',
    'cprt': '\N{NNBSP}cprt (󱹳)',
    'pprt': '\N{NNBSP}pprt (󱹴)',
    'xprt': '\N{NNBSP}pprt (󱹵)',
    'xeprt': '\N{NNBSP}xeprt (󱹶)',
    'xdprt': '\N{NNBSP}xdprt (󱹷)',
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
        elif dados['expression'].endswith('ln('):
            calculator.expression = dados['expression'].strip()[:-3]
        elif dados['expression'].endswith('lsez('):
            calculator.expression = dados['expression'].strip()[:-5]
        elif dados['expression'].endswith('ldec('):
            calculator.expression = dados['expression'].strip()[:-5]
        elif dados['expression'].endswith(' mod '):
            calculator.expression = dados['expression'].strip()[:-5]
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
        calculator.expression = dados['expression'][:-2] + '! '

    elif dados['value'] == '*' and dados['expression'].endswith('! '):
        calculator.expression = dados['expression'][:-2] + '* '

    elif dados['value'] == '^' and dados['expression'].endswith('^ '):
        calculator.expression = dados['expression'][:-2] + '\u200b²'

    elif dados['value'] == '^' and dados['expression'].endswith('\u200b²'):
        calculator.expression = dados['expression'][:-2] + 'sqrt('

    elif dados['value'] == '^' and dados['expression'].endswith('sqrt('):
        calculator.expression = dados['expression'][:-5] + '\u200b³'

    elif dados['value'] == '^' and dados['expression'].endswith('\u200b³'):
        calculator.expression = dados['expression'][:-2] + 'cbrt('

    elif dados['value'] == '^' and dados['expression'].endswith('cbrt('):
        calculator.expression = dados['expression'][:-5] + '^ 1⁄'

    elif dados['value'] == '^' and dados['expression'].endswith('^ 1⁄'):
        calculator.expression = dados['expression'][:-5] + '^ '

    elif dados['value'] == '/' and dados['expression'].endswith(' / '):
        calculator.expression = dados['expression'][:-3] + '⁄'

    elif dados['value'] == '/' and dados['expression'].endswith('⁄'):
        calculator.expression = dados['expression'][:-1] + ' mod '

    elif dados['value'] == '/' and dados['expression'].endswith(' mod '):
        calculator.expression = dados['expression'][:-1] + ' / '

    elif dados['value'] == '%' and dados['expression'].endswith('% '):
        calculator.expression = dados['expression'][:-2] + '‰ '

    elif dados['value'] == '%' and dados['expression'].endswith('‰ '):
        calculator.expression = dados['expression'][:-2] + '‱ '

    elif dados['value'] == '%' and dados['expression'].endswith('‱ '):
        calculator.expression = dados['expression'][:-2] + '% '

    elif dados['value'] == '󱹱' and dados['expression'].endswith('󱹱 '):
        calculator.expression = dados['expression'][:-2] + '󱹲 '

    elif dados['value'] == '󱹱' and dados['expression'].endswith('󱹲 '):
        calculator.expression = dados['expression'][:-2] + '󱹲 '

    elif dados['value'] == '󱹱' and dados['expression'].endswith('󱹲 '):
        calculator.expression = dados['expression'][:-2] + '󱹳 '

    elif dados['value'] == '󱹱' and dados['expression'].endswith('󱹳 '):
        calculator.expression = dados['expression'][:-2] + '󱹴 '

    elif dados['value'] == '󱹱' and dados['expression'].endswith('󱹴 '):
        calculator.expression = dados['expression'][:-2] + '󱹱 '

    elif dados['value'] == 'τ' and dados['expression'].endswith('τ'):
        calculator.expression = dados['expression'][:-1] + 'π'

    elif dados['value'] == 'τ' and dados['expression'].endswith('π'):
        calculator.expression = dados['expression'][:-1] + 'τ'

    elif dados['value'] == 'π' and dados['expression'].endswith('π'):
        calculator.expression = dados['expression'][:-1] + 'τ'

    elif dados['value'] == 'π' and dados['expression'].endswith('τ'):
        calculator.expression = dados['expression'][:-1] + 'π'

    elif dados['value'] == 'e' and dados['expression'].endswith('e'):
        calculator.expression = dados['expression'][:-1] + 'ln('

    elif dados['value'] == 'e' and dados['expression'].endswith('ln('):
        calculator.expression = dados['expression'][:-3] + 'lsez('

    elif dados['value'] == 'e' and dados['expression'].endswith('lsez('):
        calculator.expression = dados['expression'][:-5] + 'ldec('

    elif dados['value'] == 'e' and dados['expression'].endswith('ldec('):
        calculator.expression = dados['expression'][:-5] + 'e'

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

    display = calculator.display
    niftimal_display = calculator.niftimal_display

    if calculator.sezimal_digits:
        display = display.replace(calculator.locale.SEZIMAL_SEPARATOR, '󱹭')
        display = display.replace('󱹭󱹭', '󱹮')
        display = display.replace(calculator.locale.GROUP_SEPARATOR, ' ')
        display = display.replace(calculator.locale.FRACTION_GROUP_SEPARATOR, ' ')

        niftimal_display = niftimal_display.replace(calculator.locale.SEZIMAL_SEPARATOR, '󱹭')
        niftimal_display = niftimal_display.replace('󱹭󱹭', '󱹮')
        niftimal_display = niftimal_display.replace(calculator.locale.GROUP_SEPARATOR, ' ')
        niftimal_display = niftimal_display.replace(calculator.locale.FRACTION_GROUP_SEPARATOR, ' ')

    else:
        display = display.replace(',,', '„').replace('..', '‥')
        niftimal_display = niftimal_display.replace(',,', '„')

    decimal_display = calculator.decimal_display.replace(',,', '„').replace('..', '‥')

    resposta = {
        'expression': calculator.sezimal_expression,
        'decimal_expression': calculator.decimal_expression,
        'display': display,
        'decimal_display': decimal_display,
        'niftimal_display': niftimal_display,
        'show_spellout': False,
        'spellout': '',
        'separator': calculator.locale.SEZIMAL_SEPARATOR,
        'group_separator': calculator.locale.GROUP_SEPARATOR,
        'sezimal_digits': calculator.sezimal_digits,
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

    # resposta['display'] += ' ⹁ ⹂ ⹉ :'
    print('dados', dados)
    print()
    print('expressão', calculator.expression)
    print()
    print('resposta', resposta)
    print()

    return jsonify(resposta)


@app.route('/manifest_calculator.json')
def calculator_manifest() -> str:
    text = open('template/manifest_calculator.json').read()
    return text
