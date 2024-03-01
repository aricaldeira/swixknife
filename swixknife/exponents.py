
from decimal import Decimal

from .sezimal import Sezimal, SezimalInteger, SezimalFraction
from .functions import SezimalRange
from .base import sezimal_context


def sezimal_exponent_to_decimal(exponent: str | int | SezimalInteger) -> SezimalInteger:
    if exponent == 0:
        return SezimalInteger(0)

    exponent = SezimalInteger(exponent)

    exponent_six = Sezimal(10) ** exponent

    if exponent > 0:
        start = exponent
        finish = 1
        step = -1
    else:
        start = exponent
        finish = -1
        step = 1

    for i in SezimalRange(start, finish, step):
        exponent_ten = Sezimal(14) ** i

        if exponent > 0:
            if exponent_ten <= exponent_six:
                return i + 1

        else:
            if exponent_ten >= exponent_six:
                return i - 1

    return SezimalInteger(0)


def decimal_exponent_to_sezimal(exponent: str | int | SezimalInteger) -> SezimalInteger:
    if exponent == 0:
        return SezimalInteger(0)

    exponent = SezimalInteger(exponent)

    exponent_ten = Sezimal(14) ** exponent

    if exponent > 0:
        start = ((exponent // 3) * 4) + 4
        finish = 1
        step = -1
    else:
        start = ((exponent // 3) * 4) - 4
        finish = -1
        step = 1

    for i in SezimalRange(start, finish, step):
        exponent_six = Sezimal(10) ** i

        if exponent > 0:
            if exponent_six <= exponent_ten:
                return i + 1

        else:
            if exponent_six >= exponent_ten:
                return i - 1

    return SezimalInteger(0)


def sezimal_exponent_to_decimal_factor(sezimal_exponent: str | int | SezimalInteger, decimal_exponent: str | int | SezimalInteger = None) -> SezimalInteger:
    if sezimal_exponent == 0:
        return SezimalFraction(0, 1)

    sezimal_exponent = SezimalInteger(sezimal_exponent)

    if decimal_exponent is None:
        decimal_exponent = sezimal_exponent_to_decimal(sezimal_exponent)
    else:
        decimal_exponent = SezimalInteger(decimal_exponent)

    if decimal_exponent == 0:
        return SezimalFraction(0, 1)

    if sezimal_exponent > 0 and decimal_exponent > 0:
        factor = SezimalFraction(Sezimal(10) ** sezimal_exponent, Sezimal(14) ** decimal_exponent)

    else:
        factor = SezimalFraction(Sezimal(10) ** abs(sezimal_exponent) , Sezimal(14) ** abs(decimal_exponent))
        factor = 1 / factor

    return factor


def decimal_exponent_to_sezimal_factor(decimal_exponent: str | int | SezimalInteger, sezimal_exponent: str | int | SezimalInteger = None) -> SezimalInteger:
    if decimal_exponent == 0:
        return SezimalFraction(0, 1)

    decimal_exponent = SezimalInteger(decimal_exponent)

    if sezimal_exponent is None:
        sezimal_exponent = decimal_exponent_to_sezimal(decimal_exponent)
    else:
        sezimal_exponent = SezimalInteger(sezimal_exponent)

    if sezimal_exponent == 0:
        return SezimalFraction(0, 1)

    if decimal_exponent > 0 and sezimal_exponent > 0:
        factor = SezimalFraction(Sezimal(14) ** decimal_exponent, Sezimal(10) ** sezimal_exponent)
    else:
        factor = SezimalFraction(Sezimal(14) ** abs(decimal_exponent), Sezimal(10) ** abs(sezimal_exponent))
        factor = 1 / factor

    # if str(factor).endswith('5555'):
    #     factor += Sezimal(f'1E{factor._precision}')

    return factor


_DIGIT_TO_PREFIX = {
    '0': 'shun',
    '1': 'eka',
    '2': 'di',
    '3': 'tri',
    '4': 'char',
    '5': 'pan',
    '10': 'sha',
    '11': 'shaeka',
    '12': 'shadi',
    '13': 'shatri',
    '14': 'shachar',
    '15': 'shapan',
    '20': 'disha',
    '30': 'trisha',
    '40': 'charsha',
    '50': 'pansha',
    '100': 'ni',
    '101': 'nieka',
    '102': 'nidi',
    '103': 'nitri',
    '104': 'nichar',
    '105': 'nipan',
    '110': 'nisha',
    '111': 'nishaeka',
    '112': 'nishadi',
    '113': 'nishatri',
    '114': 'nishachar',
    '115': 'nishapan',
    '120': 'nidisha',
    '130': 'nitrisha',
    '140': 'nicharsha',
    '150': 'nipansha',
    '200': 'dini',
    '300': 'trini',
    '400': 'charni',
    '500': 'pani',
    '1000': 'ar',
}

_DIGIT_TO_SYMBOL = {
    '0': 's',
    '1': 'e',
    '2': 'd',
    '3': 't',
    '4': 'c',
    '5': 'p',
    '10': 'x',
    '11': 'xe',
    '12': 'xd',
    '13': 'xt',
    '14': 'xc',
    '15': 'xp',
    '20': 'dx',
    '30': 'tx',
    '40': 'cx',
    '50': 'px',
    '100': 'n',
    '101': 'ne',
    '102': 'nd',
    '103': 'nt',
    '104': 'nc',
    '105': 'np',
    '110': 'nx',
    '111': 'nxe',
    '112': 'nxd',
    '113': 'nxt',
    '114': 'nxc',
    '115': 'nxp',
    '120': 'ndx',
    '130': 'ntx',
    '140': 'ncx',
    '150': 'npx',
    '200': 'dn',
    '300': 'tn',
    '400': 'cn',
    '500': 'pn',
    '1000': 'a',
}

_PREFIX_TO_DIGIT = {p: d for d, p in _DIGIT_TO_PREFIX.items()}
_SYMBOL_TO_DIGIT = {s: d for d, s in _DIGIT_TO_SYMBOL.items()}


def sezimal_exponent_to_prefix(exponent: str | int | SezimalInteger) -> str:
    if exponent == 0:
        return _DIGIT_TO_PREFIX['0'] + 'ti'

    exponent = SezimalInteger(exponent)

    if exponent > 0:
        infix = 'ma'
    else:
        infix = 'ti'

    exponent = str(abs(exponent))

    if exponent in _DIGIT_TO_PREFIX:
        prefix = _DIGIT_TO_PREFIX[exponent]
    else:
        prefix = ''

        for digit in str(exponent):
            prefix += _DIGIT_TO_PREFIX[digit]

    prefix += infix

    prefix = prefix.replace('nn', 'n')
    prefix = prefix.replace('nm', 'm')

    return prefix


def sezimal_exponent_to_symbol(exponent: str | int | SezimalInteger, with_infix: bool = False) -> str:
    if exponent == 0:
        return _DIGIT_TO_SYMBOL['0']

    exponent = SezimalInteger(exponent)

    if exponent > 0:
        upper_case = True
        infix = 'm'
    else:
        upper_case = False
        infix = 'i'

    if not with_infix:
        infix = ''

    exponent = str(abs(exponent))

    if exponent in _DIGIT_TO_SYMBOL:
        symbol = _DIGIT_TO_SYMBOL[exponent]
    else:
        symbol = ''

        for digit in str(exponent):
            symbol += _DIGIT_TO_SYMBOL[digit]

    if infix == '' and upper_case:
        symbol = symbol.upper()

    symbol += infix

    return symbol


def sezimal_prefix_to_exponent(prefix: str) -> SezimalInteger:
    if not prefix:
        return SezimalInteger(0)

    original_prefix = prefix

    if prefix.lower().endswith('ma'):
        negative = False
        prefix = prefix.lower()[:-2]

    elif prefix.lower().endswith('ti'):
        negative = True
        prefix = prefix.lower()[:-2]

    else:
        raise ValueError(f'Prefix {original_prefix} invalid')

    exponent = prefix

    for pf in _PREFIX_TO_DIGIT:
        digit = _PREFIX_TO_DIGIT[pf]
        exponent = exponent.replace(pf, digit)

    if not exponent.isdigit():
        raise ValueError(f'Prefix {original_prefix} invalid')

    exponent = SezimalInteger(exponent)

    if negative:
        exponent = SezimalInteger(exponent * -1)

    return exponent


def sezimal_symbol_to_exponent(symbol: str) -> SezimalInteger:
    if not symbol:
        return SezimalInteger(0)

    original_symbol = symbol

    if symbol.upper() == symbol:
        negative = False
        symbol = symbol.lower()

    elif symbol.lower() == symbol:
        negative = True
        symbol = symbol.lower()

    else:
        raise ValueError(f'Symbol {original_symbol} invalid')

    exponent = symbol

    for sy in _SYMBOL_TO_DIGIT:
        digit = _SYMBOL_TO_DIGIT[sy]
        exponent = exponent.replace(sy, digit)

    if not exponent.isdigit():
        raise ValueError(f'Symbol {original_symbol} invalid')

    exponent = SezimalInteger(exponent)

    if negative:
        exponent = SezimalInteger(exponent * -1)

    return exponent


def decimal_exponent_to_symbol(exponent: str | int | SezimalInteger) -> str:
    exponent = SezimalInteger(exponent)

    if exponent == 0:
        return ''

    if exponent > 0:
        if exponent == 1:
            return 'da'
        elif exponent == 2:
            return 'h'
        elif exponent < 10:
            return 'k'
        elif exponent < 13:
            return 'M'
        elif exponent < 20:
            return 'G'
        elif exponent < 23:
            return 'T'
        elif exponent < 30:
            return 'P'
        elif exponent < 33:
            return 'E'
        elif exponent < 40:
            return 'Z'
        elif exponent < 43:
            return 'Y'
        elif exponent < 50:
            return 'R'
        else:
            return 'Q'

    else:
        exponent = abs(exponent)

        if exponent == 1:
            return 'd'
        elif exponent == 2:
            return 'c'
        elif exponent < 10:
            return 'm'
        elif exponent < 13:
            return 'µ'
        elif exponent < 20:
            return 'n'
        elif exponent < 23:
            return 'p'
        elif exponent < 30:
            return 'f'
        elif exponent < 33:
            return 'a'
        elif exponent < 40:
            return 'z'
        elif exponent < 43:
            return 'y'
        elif exponent < 50:
            return 'r'
        else:
            return 'q'
