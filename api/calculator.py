
import pathlib

TEMPLATE_PATH = pathlib.Path(__file__).parent.resolve().joinpath('template')
CALCULATOR_TEMPLATE_PATH = TEMPLATE_PATH.joinpath('calculator')


import os
import json
from io import StringIO

from flask import send_file, Response, request, jsonify
from swixknife.localization import sezimal_locale
from swixknife.calculator import SezimalCalculator
from swixknife import Sezimal

from main import app, sitemapper
from  locale_detection import browser_preferred_locale


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
    'espn': '\N{NNBSP}espn (󱹰)',
    'dspn': '\N{NNBSP}dspn (󱹱)',
    'tspn': '\N{NNBSP}tspn (󱹲)',
    'cspn': '\N{NNBSP}cspn (󱹳)',
    'pspn': '\N{NNBSP}pspn (󱹴)',
    'xspn': '\N{NNBSP}xspn (󱹵)',
    'xespn': '\N{NNBSP}xespn (󱹶)',
    'xdspn': '\N{NNBSP}xdspn (󱹷)',
}


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=1)
@app.route('/calculator')
def api_calculator() -> Response:
    text = open(TEMPLATE_PATH.joinpath('calculator.html'), 'r').read()
    locals().update(_get_calculator_templates())
    text = eval(f'f"""{text}"""')
    return Response(text, mimetype='text/html')


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
    dados['sezimal_punctuation'] = dados['sezimal_punctuation'] == 'true'
    dados['spellout'] = dados['spellout'] == 'true'
    dados['currency_mode'] = dados['currency_mode'] == 'true'

    calculator = SezimalCalculator()
    calculator.locale = dados['locale']
    calculator.grouping_digits = dados['grouping']
    calculator.currency_mode = dados['currency_mode']
    calculator.decimal = False
    calculator.precision = dados['places']
    calculator.decimal = dados['base'] == 14
    calculator.sezimal_digits = dados['sezimal_digits']
    calculator.sezimal_punctuation = dados['sezimal_punctuation']
    calculator.regularized_digits = dados['niftimal'] != 'Z' and dados['niftimal'] != 'z'
    calculator.regularized_letter_digits = dados['niftimal'] == 'z'
    calculator.unit = dados['sezimal_unit']
    # calculator.suffix = dados['sezimal_unit']
    calculator.decimal_unit = dados['decimal_unit']
    # calculator.decimal_suffix = dados['decimal_unit']
    calculator.unit_as_fraction = False
    calculator.angle = dados['sezimal_angle_unit']
    calculator.decimal_angle = dados['decimal_angle_unit']
    calculator.angle_as_fraction = calculator.angle == 'mdl'
    # calculator.angle_as_fraction = False

    if calculator.decimal_unit.endswith('turn') \
        or calculator.decimal_unit.startswith('tau_') \
        or calculator.decimal_unit.startswith('pi_'):
        calculator.unit_as_fraction = True

    # calculator.debug = True

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
        elif dados['expression'].endswith('lbin('):
            calculator.expression = dados['expression'].strip()[:-5]
        elif dados['expression'].endswith('SIN('):
            calculator.expression = dados['expression'].strip()[:-4]
        elif dados['expression'].endswith('arcsin('):
            calculator.expression = dados['expression'].strip()[:-7]
        elif dados['expression'].endswith('CSC('):
            calculator.expression = dados['expression'].strip()[:-4]
        elif dados['expression'].endswith('arccsc('):
            calculator.expression = dados['expression'].strip()[:-7]
        elif dados['expression'].endswith('COS('):
            calculator.expression = dados['expression'].strip()[:-4]
        elif dados['expression'].endswith('arccos('):
            calculator.expression = dados['expression'].strip()[:-7]
        elif dados['expression'].endswith('SEC('):
            calculator.expression = dados['expression'].strip()[:-4]
        elif dados['expression'].endswith('arcsec('):
            calculator.expression = dados['expression'].strip()[:-7]
        elif dados['expression'].endswith('TAN('):
            calculator.expression = dados['expression'].strip()[:-4]
        elif dados['expression'].endswith('arctan('):
            calculator.expression = dados['expression'].strip()[:-7]
        elif dados['expression'].endswith('cot('):
            calculator.expression = dados['expression'].strip()[:-4]
        elif dados['expression'].endswith('arccot('):
            calculator.expression = dados['expression'].strip()[:-7]
        elif dados['expression'].endswith(' mod '):
            calculator.expression = dados['expression'].strip()[:-5]
        else:
            calculator.expression = dados['expression'].strip()[:-1]

    elif dados['value'] == '.' and (not calculator.decimal) and dados['currency_mode']:
        if dados['expression'].endswith(';'):
            pass

        elif ';' in dados['expression'] and dados['expression'][-1] != ';':
            if ' ' in dados['expression']:
                parts = dados['expression'].split(' ')[-1].replace('_', '').split(';')
            else:
                parts = dados['expression'].replace('_', '').split(';')

            if len(parts) >= 2 and parts[-1].isdigit() and parts[-2].isdigit():
                pass

            elif parts[-1].isdigit():
                calculator.expression = dados['expression'] + ';'

        else:
            calculator.expression = dados['expression'] + ';'

    elif dados['value'] == '.' and not dados['currency_mode']:
        if dados['expression'].endswith('..'):
            pass

        elif '.' in dados['expression'] and dados['expression'][-1] != '.':
            if ' ' in dados['expression']:
                parts = dados['expression'].split(' ')[-1].replace('_', '').split('.')
            else:
                parts = dados['expression'].replace('_', '').split('.')

            if len(parts) >= 2 and parts[-1].isdigit() and parts[-2].isdigit():
                calculator.expression = dados['expression'] + dados['value'] + dados['value']
            elif parts[-1].isdigit():
                calculator.expression = dados['expression'] + dados['value']

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
        calculator.expression = dados['expression'][:-2] + '󱹳 '

    elif dados['value'] == '󱹱' and dados['expression'].endswith('󱹳 '):
        calculator.expression = dados['expression'][:-2] + '󱹵 '

    elif dados['value'] == '󱹱' and dados['expression'].endswith('󱹵 '):
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

    elif dados['value'] == 'ln(' and dados['expression'].endswith('ln('):
        calculator.expression = dados['expression'][:-3] + 'e'

    elif dados['value'] == 'ln(' and dados['expression'].endswith('e'):
        calculator.expression = dados['expression'][:-3] + 'lsez('

    elif dados['value'] == 'ln(' and dados['expression'].endswith('lsez('):
        calculator.expression = dados['expression'][:-5] + 'ldec('

    elif dados['value'] == 'ln(' and dados['expression'].endswith('ldec('):
        calculator.expression = dados['expression'][:-5] + 'ln('

    elif dados['value'] == 'lsez(' and dados['expression'].endswith('lsez('):
        calculator.expression = dados['expression'][:-5] + 'ldec('

    elif dados['value'] == 'lsez(' and dados['expression'].endswith('ldec('):
        calculator.expression = dados['expression'][:-5] + 'lsez('

    elif dados['value'] == 'ldec(' and dados['expression'].endswith('ldec('):
        calculator.expression = dados['expression'][:-5] + 'lsez('

    elif dados['value'] == 'ldec(' and dados['expression'].endswith('lsez('):
        calculator.expression = dados['expression'][:-5] + 'ldec('

    elif dados['value'] == 'SIN(' and dados['expression'].endswith('SIN('):
        calculator.expression = dados['expression'][:-4] + 'asin('

    elif dados['value'] == 'SIN(' and dados['expression'].endswith('asin('):
        calculator.expression = dados['expression'][:-5] + 'CSC('

    elif dados['value'] == 'SIN(' and dados['expression'].endswith('CSC('):
        calculator.expression = dados['expression'][:-4] + 'acsc('

    elif dados['value'] == 'SIN(' and dados['expression'].endswith('acsc('):
        calculator.expression = dados['expression'][:-5] + 'SIN('

    elif dados['value'] == 'COS(' and dados['expression'].endswith('COS('):
        calculator.expression = dados['expression'][:-4] + 'acos('

    elif dados['value'] == 'COS(' and dados['expression'].endswith('acos('):
        calculator.expression = dados['expression'][:-5] + 'SEC('

    elif dados['value'] == 'COS(' and dados['expression'].endswith('SEC('):
        calculator.expression = dados['expression'][:-4] + 'asec('

    elif dados['value'] == 'COS(' and dados['expression'].endswith('asec('):
        calculator.expression = dados['expression'][:-5] + 'COS('

    elif dados['value'] == 'TAN(' and dados['expression'].endswith('TAN('):
        calculator.expression = dados['expression'][:-4] + 'atan('

    elif dados['value'] == 'TAN(' and dados['expression'].endswith('atan('):
        calculator.expression = dados['expression'][:-5] + 'COT('

    elif dados['value'] == 'TAN(' and dados['expression'].endswith('COT('):
        calculator.expression = dados['expression'][:-4] + 'acot('

    elif dados['value'] == 'TAN(' and dados['expression'].endswith('acot('):
        calculator.expression = dados['expression'][:-5] + 'TAN('

    else:
        if dados['expression'] == '0':
            if dados['value'] == '.':
                calculator.expression = dados['expression'] + dados['value']
            elif dados['expression'] in '0123456789↊↋':
                calculator.expression = dados['value']
            elif '(' in dados['value']:
                calculator.expression = dados['value']
            else:
                calculator.expression = dados['expression'] + dados['value']

        else:
            calculator.expression = dados['expression'] + dados['value']

    display = calculator.display

    if dados['niftimal'] == '-':
        niftimal_display = ''
    else:
        niftimal_display = calculator.niftimal_display

    if calculator.sezimal_digits:
        display = display.replace(calculator.locale.SEZIMAL_SEPARATOR, '󱹮')
        display = display.replace('󱹮󱹮', '󱹯')
        display = display.replace(calculator.locale.GROUP_SEPARATOR, '󱹭')
        display = display.replace(calculator.locale.FRACTION_GROUP_SEPARATOR, '󱹭')

        niftimal_display = niftimal_display.replace(calculator.locale.SEZIMAL_SEPARATOR, '󱹮')
        niftimal_display = niftimal_display.replace('󱹮󱹮', '󱹯')
        niftimal_display = niftimal_display.replace(calculator.locale.GROUP_SEPARATOR, '󱹭')
        niftimal_display = niftimal_display.replace(calculator.locale.FRACTION_GROUP_SEPARATOR, '󱹭')

    else:
        display = display.replace(',,', '„').replace('..', '‥')
        niftimal_display = niftimal_display.replace(',,', '„')

    decimal_display = calculator.decimal_display.replace(',,', '„').replace('..', '‥')

    display = display.replace('ₑ', '<sub class="constant">𝑒</sub>')
    niftimal_display = niftimal_display.replace('ₑ', '<sub class="constant">𝑒</sub>')
    decimal_display = decimal_display.replace('ₑ', '<sub class="constant">𝑒</sub>')

    display = display.replace('e', '<span class="constant">𝑒</span>')
    niftimal_display = niftimal_display.replace('e', '<span class="constant">𝑒</span>')
    decimal_display = decimal_display.replace('e', '<span class="constant">𝑒</span>')

    for c in ('τ', 'π', 'φ'):
        display = display.replace(c, f'<span class="constant">{c}</span>')
        niftimal_display = niftimal_display.replace(c, f'<span class="constant">{c}</span>')
        decimal_display = decimal_display.replace(c, f'<span class="constant">{c}</span>')

    #
    # Chrome doesn’t play nice with the fraction slash,
    # so we convert it to mathml
    #
    # if 'Chrome' in request.headers.get('User-Agent', ''):
    #     display = _fraction_to_mathml(display)
    #     niftimal_display = _fraction_to_mathml(niftimal_display)
    #     decimal_display = _fraction_to_mathml(decimal_display)

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
        'digits': calculator.locale.DIGITS,
        'sezimal_digits': calculator.sezimal_digits,
        'currency_separator': calculator.locale.CURRENCY_SEPARATOR,
        'currency_unit_symbol': calculator.locale.CURRENCY_UNIT_SYMBOL,
    }

    if not calculator.error:
        # if dados['sezimal_unit']:
        #     if dados['sezimal_unit'] in UNIT_SIMPLIFIED_SYMBOL:
        #         resposta['display'] += UNIT_SIMPLIFIED_SYMBOL[dados['sezimal_unit']]
        #     else:
        #         resposta['display'] += '\N{NNBSP}' + dados['sezimal_unit']
        #
        # if dados['decimal_unit']:
        #     if dados['decimal_unit'] in '%‰‱':
        #         resposta['decimal_display'] += dados['decimal_unit']
        #     elif dados['decimal_unit'][0] in ('π', 'τ') \
        #         or 'pi_' in dados['decimal_unit'] \
        #         or 'tau_' in dados['decimal_unit']:
        #         resposta['decimal_display'] += '\N{ZWSP}' + dados['decimal_unit']
        #     else:
        #         resposta['decimal_display'] += '\N{NNBSP}' + dados['decimal_unit']

        if dados['spellout']:
            resposta['show_spellout'] = True
            resposta['spellout'] = calculator.spellout

    return jsonify(resposta)


_TRANSLATIONS = {
    'ar': 'حاسبة',
    'bz': 'Kawkuladora',
    'ca': 'Calculadora',
    'de': 'Taschenrechner',
    'el': 'Αριθμομηχανή',
    'eo': 'Kalkulilo',
    'es': 'Calculadora',
    'fa': 'حساب',
    'fr': 'Calculatrice',
    'ga': 'Áireamhán',
    'gl': 'Calculadora',
    'gn': 'Calculadora',
    'he': 'מחשבון',
    'hi': 'कैलकुलेटर',
    'hu': 'Számológép',
    'id': 'Kalkulator',
    'it': 'Calcolatrice',
    'ja': '電卓',
    'ko': '계산자',
    'nl': 'Rekenmachine',
    'pl': 'Kalkulator',
    'pt': 'Calculadora',
    'ro': 'Calculator',
    'ru': 'Калькулятор',
    'sw': 'Kikokotozi',
    'tr': 'Hesap',
    'uk': 'Калькулятор',
    'vi': 'Máy tính',
    'yo': 'Ẹrọ iṣiro',
    'zh': '計算機',
    'zh_CN': '计算器',
}


@sitemapper.include(lastmod='2024-09-11', changefreq='weekly', priority=0.8)
@app.route('/calculator/manifest.webmanifest')
def calculator_manifest() -> str:
    text = open('template/manifest_calculator.json').read()

    pl = browser_preferred_locale()

    if '_' in pl:
        lang = pl.split('_')[0]
    elif '-' in pl:
        lang = pl.split('-')[0]
    else:
        lang = pl

    if lang in _TRANSLATIONS:
        if pl in _TRANSLATIONS:
            text = text.replace('"Sezimal Calculator"', f'"{_TRANSLATIONS[pl]}"')
        else:
            text = text.replace('"Sezimal Calculator"', f'"{_TRANSLATIONS[lang]}"')

    if 'pt-' in pl or pl == 'pt':
        text = text.replace('"Sezimal calculator, base and units converter"', '"Calculadora sezimal, conversão de base numérica e unidades de medida"')
    elif 'bz-' in pl or pl == 'bz':
        text = text.replace('"Sezimal calculator, base and units converter"', '"Kawkuladora sezimaw, konversawn di bazi numérika i unidadis di medida"')

    return text


def _fraction_to_mathml(display):
    if '⁄' not in display:
        return display

    PARTS_OF_FRACTION = '0123456789󱸀󱸁󱸂󱸃󱸄󱸅󱹮,.󱹯󱹭„‥ 󱹬\N{ZWJ}'

    while len(display.split('⁄', 1)) == 2:
        parts = display.split('⁄', 1)

        #
        # Check if there’s a space or parentheses in either part
        #
        if ' ' not in parts[0] and '(' not in parts[0]:
            display = '<math><mfrac><mn>' + parts[0]
        #
        # There are either spaces or parentheses in the first term,
        # we have to find which is closer to the number
        #
        else:
            subparts_space = parts[0].split(' ')
            subparts_parentheses = parts[0].split('(')

            if len(subparts_space[-1]) < len(subparts_parentheses[-1]):
                display = ' '.join(subparts_space[:-1]) + '<math><mfrac><mn>' + subparts_space[-1]
            else:
                display = ' '.join(subparts_parentheses[:-1]) + '<math><mfrac><mn>' + subparts_parentheses[-1]

        display += '</mn><mn>'

        if ' ' not in parts[1] and '(' not in parts[1]:
            display += parts[1] + '</mn></mfrac></math>'
        #
        # There are either spaces or parentheses in the first term,
        # we have to find which is closer to the number
        #
        else:
            subparts_space = parts[1].split(' ')
            subparts_parentheses = parts[1].split('(')

            if len(subparts_space[0]) < len(subparts_parentheses[0]):
                display += subparts_space[0] + '</mn></mfrac></math>' + ' '.join(subparts_space[1:])
            else:
                display += subparts_parentheses[0] + '</mn></mfrac></math>' + ' '.join(subparts_parentheses[1:])

    return display


def _get_calculator_templates() -> dict:
    templates = {}

    for file_name in os.listdir(CALCULATOR_TEMPLATE_PATH):
        if '.html' not in file_name:
            continue

        templates[file_name.replace('.html', '').replace('-', '_')] = open(CALCULATOR_TEMPLATE_PATH.joinpath(file_name), 'r').read()

    return templates
