
from decimal import Decimal

from .sezimal import Sezimal, SezimalInteger, MAX_PRECISION, MAX_DECIMAL_PRECISION
from .functions import SezimalRange

MAX_EXPONENT = SezimalInteger(MAX_PRECISION) - 4
MIN_EXPONENT = MAX_EXPONENT * -1

MAX_DECIMAL_EXPONENT = SezimalInteger(Decimal(MAX_DECIMAL_PRECISION)) - 4
MIN_DECIMAL_EXPONENT = MAX_DECIMAL_EXPONENT * -1


def sezimal_exponent_to_decimal(exponent: str | int | SezimalInteger) -> SezimalInteger:
    if exponent == 0:
        return SezimalInteger(0)

    exponent = SezimalInteger(exponent)

    # if exponent > 0 and exponent > MAX_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be above {MAX_EXPONENT}')
    # elif exponent < 0 and exponent < MIN_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be under {MIN_EXPONENT}')

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

    # if exponent > 0 and exponent > MAX_DECIMAL_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be above {MAX_DECIMAL_EXPONENT}')
    # elif exponent < 0 and exponent < MIN_DECIMAL_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be under {MIN_DECIMAL_EXPONENT}')

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
        return SezimalInteger(0)

    sezimal_exponent = SezimalInteger(sezimal_exponent)

    if sezimal_exponent > 0 and sezimal_exponent > MAX_EXPONENT:
        raise ValueError(f'Sezimal exponent {sezimal_exponent} cannot be above {MAX_EXPONENT}')
    elif sezimal_exponent < 0 and sezimal_exponent < MIN_EXPONENT:
        raise ValueError(f'Sezimal exponent {sezimal_exponent} cannot be under {MIN_EXPONENT}')

    if decimal_exponent is None:
        decimal_exponent = sezimal_exponent_to_decimal(sezimal_exponent)
    else:
        decimal_exponent = SezimalInteger(decimal_exponent)

        if decimal_exponent > 0 and decimal_exponent > MAX_DECIMAL_EXPONENT:
            raise ValueError(f'Decimal exponent {decimal_exponent} cannot be above {MAX_DECIMAL_EXPONENT}')
        elif decimal_exponent < 0 and decimal_exponent < MIN_DECIMAL_EXPONENT:
            raise ValueError(f'Decimal exponent {decimal_exponent} cannot be under {MIN_DECIMAL_EXPONENT}')

    if decimal_exponent == 0:
        return SezimalInteger(0)

    if sezimal_exponent > 0 and decimal_exponent > 0:
        factor = (Sezimal(10) ** sezimal_exponent) / (Sezimal(14) ** decimal_exponent)

    else:
        factor = (Sezimal(10) ** abs(sezimal_exponent)) / (Sezimal(14) ** abs(decimal_exponent))
        factor = 1 / factor

    # if str(factor).endswith('5555'):
    #     factor += Sezimal(f'1E{factor._precision}')

    return factor


def decimal_exponent_to_sezimal_factor(decimal_exponent: str | int | SezimalInteger, sezimal_exponent: str | int | SezimalInteger = None) -> SezimalInteger:
    if decimal_exponent == 0:
        return SezimalInteger(0)

    decimal_exponent = SezimalInteger(decimal_exponent)

    if decimal_exponent > 0 and decimal_exponent > MAX_DECIMAL_EXPONENT:
        raise ValueError(f'Decimal exponent {decimal_exponent} cannot be above {MAX_DECIMAL_EXPONENT}')
    elif decimal_exponent < 0 and decimal_exponent < MIN_DECIMAL_EXPONENT:
        raise ValueError(f'Decimal exponent {decimal_exponent} cannot be under {MIN_DECIMAL_EXPONENT}')

    if sezimal_exponent is None:
        sezimal_exponent = decimal_exponent_to_sezimal(decimal_exponent)
    else:
        sezimal_exponent = SezimalInteger(sezimal_exponent)

        if sezimal_exponent > 0 and sezimal_exponent > MAX_EXPONENT:
            raise ValueError(f'Sezimal exponent {sezimal_exponent} cannot be above {MAX_EXPONENT}')
        elif sezimal_exponent < 0 and sezimal_exponent < MIN_EXPONENT:
            raise ValueError(f'Sezimal exponent {sezimal_exponent} cannot be under {MIN_EXPONENT}')

    if sezimal_exponent == 0:
        return SezimalInteger(0)

    if decimal_exponent > 0 and sezimal_exponent > 0:
        factor = (Sezimal(14) ** decimal_exponent) / (Sezimal(10) ** sezimal_exponent)
    else:
        factor = (Sezimal(14) ** abs(decimal_exponent)) / (Sezimal(10) ** abs(sezimal_exponent))
        factor = 1 / factor

    # if str(factor).endswith('5555'):
    #     factor += Sezimal(f'1E{factor._precision}')

    return factor


_DIGIT_TO_PREFIX = {
    '0': 'shun',
    '1': 'eka',
    '2': 'di',
    '3': 'tri',
    '4': 'cha',
    '5': 'pan',
}

_DIGIT_TO_SYMBOL = {
    '0': 's',
    '1': 'e',
    '2': 'd',
    '3': 't',
    '4': 'c',
    '5': 'p',
}

_PREFIX_TO_DIGIT = {
    'shun': '0',
    'eka': '1',
    'di': '2',
    'tri': '3',
    'cha': '4',
    'pan': '5',
}

_SYMBOL_TO_DIGIT = {
    's': '0',
    'e': '1',
    'd': '2',
    't': '3',
    'c': '4',
    'p': '5',
}


def sezimal_exponent_to_prefix(exponent: str | int | SezimalInteger) -> str:
    if exponent == 0:
        return _DIGIT_TO_PREFIX['0'] + 'ti'

    exponent = SezimalInteger(exponent)

    # if exponent > 0 and exponent > MAX_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be above {MAX_EXPONENT}')
    # elif exponent < 0 and exponent < MIN_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be under {MIN_EXPONENT}')

    prefix = ''

    if exponent > 0:
        for digit in str(exponent):
            prefix += _DIGIT_TO_PREFIX[digit]

        prefix += 'ma'

    else:
        for digit in str(abs(exponent)):
            prefix += _DIGIT_TO_PREFIX[digit]

        prefix += 'ti'

    return prefix


def sezimal_exponent_to_symbol(exponent: str | int | SezimalInteger) -> str:
    if exponent == 0:
        return _DIGIT_TO_SYMBOL['0']

    exponent = SezimalInteger(exponent)
    #
    # if exponent > 0 and exponent > MAX_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be above {MAX_EXPONENT}')
    # elif exponent < 0 and exponent < MIN_EXPONENT:
    #     raise ValueError(f'Exponent {exponent} cannot be under {MIN_EXPONENT}')

    symbol = ''

    if exponent > 0:
        for digit in str(exponent):
            symbol += _DIGIT_TO_SYMBOL[digit]

        symbol = symbol.upper()

    else:
        for digit in str(abs(exponent)):
            symbol += _DIGIT_TO_SYMBOL[digit]

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
