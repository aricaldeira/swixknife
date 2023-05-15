

__all__ = ('calculator',)

from ..sezimal import Sezimal
from decimal import Decimal
from ..units.conversions import  *
from ..base import decimal_format


_OPERATOR = {
    '+': ' __ADD__ ',
    '−': ' __SUBTRACT__ ',
    '-': ' __SUBTRACT__ ',
    '÷': ' __DIVIDE__ ',
    '/': ' __DIVIDE__ ',
    '^': ' __POWER__ ',
    '**': ' __POWER__ ',
    '×': ' __MULTIPLY__ ',
    '*': ' __MULTIPLY__ ',
    '%': ' __MOD__ ',
    '²': ' __SQUARE__ ',
    '³': ' __CUBE__ ',
    '(': ' __LEFT_PARENTHESIS__ ',
    ')': ' __RIGHT_PARENTHESIS__ ',
}

_OPERATION = {
    '__ADD__': '+',
    '__SUBTRACT__': '-',
    '__DIVIDE__': '/',
    '__MULTIPLY__': '*',
    '__POWER__': '**',
    '__MOD__': '%',
    '__SQUARE__': "** Sezimal('2')",
    '__CUBE__': "** Sezimal('3')",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
}

_NICE_OPERATION = {
    '__ADD__': ' + ',
    '__SUBTRACT__': ' − ',
    '__DIVIDE__': ' ÷ ',
    '__MULTIPLY__': ' × ',
    '__POWER__': ' ^ ',
    '__MOD__': ' % ',
    '__SQUARE__': "²",
    '__CUBE__': "³",
    '__LEFT_PARENTHESIS__': '(',
    '__RIGHT_PARENTHESIS__': ')',
}


def calculator(exp):
    for o in _OPERATOR:
        text = _OPERATOR[o]
        exp = exp.replace(o, text)

    parts = exp.split()

    parenthesis_opened = False

    final_exp = ''
    nice_exp = ''
    decimal_exp = ''

    for p in parts:
        p = p.strip()

        if not p:
            continue

        if p in _OPERATION:
            final_exp += _OPERATION[p]
            nice_exp += _NICE_OPERATION[p]
            decimal_exp += _NICE_OPERATION[p]

            if (not parenthesis_opened) and p == '__LEFT_PARENTHESIS__':
                parenthesis_opened = True
            elif parenthesis_opened and p == '__RIGHT_PARENTHESIS__':
                parenthesis_opened = False

            continue

        n = eval(p)

        if type(n) != Sezimal:
            n = Sezimal(p)

        final_exp += f"Sezimal('{n}')"
        nice_exp += n.formatted_number

        sign, digits, precision = n.decimal.as_tuple()
        decimal_exp += decimal_format(n.decimal, decimal_places=precision * -1)

    if parenthesis_opened:
        final_exp += ')'
        nice_exp += ')'
        decimal_exp += ')'

    res = eval(final_exp)

    nice_exp += f' = {res.formatted_number}'
    sign, digits, precision = res.decimal.as_tuple()
    decimal_exp += f' = {decimal_format(res.decimal, decimal_places=precision * -1)}'

    return final_exp, nice_exp, decimal_exp, res
