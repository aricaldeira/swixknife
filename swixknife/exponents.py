
__all__ = (
    'sezimal_exponent_to_decimal_exponent', 'decimal_exponent_to_sezimal_exponent',
    'sezimal_exponent_to_factor', 'decimal_exponent_to_factor',
    'sezimal_exponent_to_decimal_exponent_factor', 'decimal_exponent_to_sezimal_exponent_factor',
    'sezimal_exponent_to_prefix', 'sezimal_exponent_to_symbol',
    'sezimal_symbol_to_exponent',
    'decimal_exponent_to_symbol', 'decimal_symbol_to_exponent',
)

from decimal import Decimal

from .base import sezimal_context
from .sezimal import Sezimal, SezimalInteger, SezimalFraction
from .functions import SezimalRange
from .base import sezimal_context


def sezimal_exponent_to_decimal_exponent(exponent: str | int | SezimalInteger) -> SezimalInteger:
    if exponent == 0 or exponent == -0:
        return SezimalInteger(0)

    exponent = SezimalInteger(exponent)

    if exponent in _SEZIMAL_EXPONENT_TO_DECIMAL_EXPONENT:
        return _SEZIMAL_EXPONENT_TO_DECIMAL_EXPONENT[exponent]

    _precision = sezimal_context.precision

    if _precision < 120:
        sezimal_context.precision = 120

    exponent_six = Sezimal(10) ** exponent

    exponent_ten = SezimalInteger(0)

    if exponent > 0:
        while exponent_six / (Sezimal(14) ** exponent_ten) > 1:
            exponent_ten += 1
    else:
        while exponent_six * (Sezimal(14) ** exponent_ten) < 1:
            exponent_ten += 1

        exponent_ten *= -1

    sezimal_context.precision = _precision

    return exponent_ten


def decimal_exponent_to_sezimal_exponent(exponent: str | int | SezimalInteger) -> SezimalInteger:
    if exponent == 0 or exponent == -0:
        return SezimalInteger(0)

    exponent = SezimalInteger(exponent)

    if exponent in _DECIMAL_EXPONENT_TO_SEZIMAL_EXPONENT:
        return _DECIMAL_EXPONENT_TO_SEZIMAL_EXPONENT[exponent]

    _precision = sezimal_context.precision

    if _precision < 120:
        sezimal_context.precision = 120

    exponent_ten = Sezimal(14) ** exponent
    exponent_six = SezimalInteger(0)

    if exponent > 0:
        while exponent_ten / (Sezimal(10) ** exponent_six) > 1:
            exponent_six += 1
    else:
        while exponent_ten * (Sezimal(10) ** exponent_six) < 1:
            exponent_six += 1

        exponent_six *= -1

    sezimal_context.precision = _precision

    return exponent_six


def sezimal_exponent_to_factor(sezimal_exponent: str | int | SezimalInteger, return_fraction: bool = False) -> Sezimal | SezimalFraction:
    if type(sezimal_exponent) != SezimalInteger:
        sezimal_exponent = SezimalInteger(sezimal_exponent)

    _precision = sezimal_context.precision

    if _precision < 120:
        sezimal_context.precision = 120

    if sezimal_exponent in _SEZIMAL_EXPONENT_FACTOR:
        sezimal_factor = _SEZIMAL_EXPONENT_FACTOR[sezimal_exponent]
    elif sezimal_exponent < 0:
        sezimal_factor = SezimalFraction(1, SezimalInteger(10) ** abs(sezimal_exponent))
    else:
        sezimal_factor = SezimalFraction(SezimalInteger(10) ** sezimal_exponent, 1)

    if not return_fraction:
        sezimal_factor = sezimal_factor.sezimal

    sezimal_context.precision = _precision

    return sezimal_factor


def decimal_exponent_to_factor(decimal_exponent: str | int | SezimalInteger, return_fraction: bool = False) -> Sezimal | SezimalFraction:
    if type(decimal_exponent) != SezimalInteger:
        decimal_exponent = SezimalInteger(decimal_exponent)

    _precision = sezimal_context.precision

    if _precision < 120:
        sezimal_context.precision = 120

    if decimal_exponent in _DECIMAL_EXPONENT_FACTOR:
        decimal_factor = _DECIMAL_EXPONENT_FACTOR[decimal_exponent]
    elif decimal_exponent < 0:
        decimal_factor = SezimalFraction(1, SezimalInteger(14) ** abs(decimal_exponent))
    else:
        decimal_factor = SezimalFraction(SezimalInteger(14) ** decimal_exponent, 1)

    if not return_fraction:
        decimal_factor = decimal_factor.sezimal

    sezimal_context.precision = _precision

    return decimal_factor


def sezimal_exponent_to_decimal_exponent_factor(sezimal_exponent: str | int | SezimalInteger, decimal_exponent: str | int | SezimalInteger = None, return_fraction: bool = False) -> Sezimal | SezimalFraction :
    sezimal_exponent = SezimalInteger(sezimal_exponent)
    sezimal_factor = sezimal_exponent_to_factor(sezimal_exponent, True)

    if decimal_exponent is None:
        decimal_exponent = sezimal_exponent_to_decimal_exponent(sezimal_exponent)
    elif type(decimal_exponent) != SezimalInteger:
        decimal_exponent = SezimalInteger(decimal_exponent)

    decimal_factor = decimal_exponent_to_factor(decimal_exponent, True)

    _precision = sezimal_context.precision

    if _precision < 120:
        sezimal_context.precision = 120

    factor = sezimal_factor / decimal_factor

    if not return_fraction:
        factor = factor.sezimal

    sezimal_context.precision = _precision

    return factor


def decimal_exponent_to_sezimal_exponent_factor(decimal_exponent: str | int | SezimalInteger, sezimal_exponent: str | int | SezimalInteger = None, return_fraction: bool = False) -> Sezimal | SezimalFraction:
    decimal_exponent = SezimalInteger(decimal_exponent)
    decimal_factor = decimal_exponent_to_factor(decimal_exponent, True)

    if sezimal_exponent is None:
        sezimal_exponent = decimal_exponent_to_sezimal_exponent(decimal_exponent)
    elif type(sezimal_exponent) != SezimalInteger:
        sezimal_exponent = SezimalInteger(sezimal_exponent)

    sezimal_factor = sezimal_exponent_to_factor(sezimal_exponent, True)

    _precision = sezimal_context.precision

    if _precision < 120:
        sezimal_context.precision = 120

    factor = decimal_factor / sezimal_factor

    if not return_fraction:
        factor = factor.sezimal

    sezimal_context.precision = _precision

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
    '0': 'z',
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
        return ''

    if type(exponent) != SezimalInteger:
        exponent = SezimalInteger(exponent)

    if exponent in _SEZIMAL_EXPONENT_TO_PREFIX:
        return _SEZIMAL_EXPONENT_TO_PREFIX[exponent]

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


def sezimal_exponent_to_symbol(exponent: str | int | SezimalInteger, unicase: bool = False) -> str:
    if exponent == 0:
        return ''

    if type(exponent) != SezimalInteger:
        exponent = SezimalInteger(exponent)

    if exponent in _SEZIMAL_EXPONENT_TO_SYMBOL:
        return _SEZIMAL_EXPONENT_TO_SYMBOL[exponent]

    if exponent > 0:
        upper_case = True
        infix = 'm'
    else:
        upper_case = False
        infix = 'i'

    if not unicase:
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

    if unicase:
        symbol = symbol.lower()

    return symbol


def sezimal_prefix_to_exponent(prefix: str) -> SezimalInteger:
    if not prefix:
        return SezimalInteger(0)

    original_prefix = prefix

    prefix = prefix.lower()

    if prefix in _SEZIMAL_PREFIX_TO_EXPONENT:
        return _SEZIMAL_PREFIX_TO_EXPONENT[prefix]

    if prefix.endswith('ma'):
        negative = False
        prefix = prefix[:-2]

    elif prefix.endswith('ti'):
        negative = True
        prefix = prefix[:-2]

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

    if symbol in _SEZIMAL_SYMBOL_TO_EXPONENT:
        return _SEZIMAL_SYMBOL_TO_EXPONENT[symbol]

    original_symbol = symbol

    if symbol.upper() == symbol:
        negative = False
        symbol = symbol.lower()

    elif symbol.lower() == symbol:
        negative = True
        symbol = symbol.lower()

    else:
        raise ValueError(f'Symbol {original_symbol} invalid')

    if symbol in _SYMBOL_TO_DIGIT:
        exponent = SezimalInteger(_SYMBOL_TO_DIGIT[symbol])

    else:
        exponent = SezimalInteger(0)

        i = SezimalInteger(1)

        for sy in symbol[::-1]:
            if i > 1 and sy in 'edtcp':
                if i == 2:
                    sy += 'x'
                elif i == 3:
                    sy += 'n'

            digit = _SYMBOL_TO_DIGIT[sy]
            exponent += SezimalInteger(digit)
            i += 1

    if negative:
        exponent *= -1

    return exponent


def decimal_exponent_to_symbol(exponent: str | int | SezimalInteger) -> str:
    if exponent == 0:
        return ''

    if type(exponent) != SezimalInteger:
        exponent = SezimalInteger(exponent)

    if exponent not in _DECIMAL_EXPONENT_SYMBOL:
        return 'Q' if exponent > 0 else 'q'

    return _DECIMAL_EXPONENT_SYMBOL[exponent]


def decimal_symbol_to_exponent(symbol: str) -> SezimalInteger:
    if not symbol:
        return SezimalInteger(0)

    if symbol not in _DECIMAL_SYMBOL_EXPONENT:
        raise ValueError(f'Symbol {symbol} invalid')

    return _DECIMAL_SYMBOL_EXPONENT[symbol]


#
# Pre-calculated sezimal exponent to decimal exponent
#
_SEZIMAL_EXPONENT_TO_DECIMAL_EXPONENT = {
    SezimalInteger('-120'): SezimalInteger('-102'),
    SezimalInteger('-115'): SezimalInteger('-101'),
    SezimalInteger('-114'): SezimalInteger('-100'),
    SezimalInteger('-113'): SezimalInteger('-100'),
    SezimalInteger('-112'): SezimalInteger('-55'),
    SezimalInteger('-111'): SezimalInteger('-54'),
    SezimalInteger('-110'): SezimalInteger('-53'),
    SezimalInteger('-105'): SezimalInteger('-52'),
    SezimalInteger('-104'): SezimalInteger('-52'),
    SezimalInteger('-103'): SezimalInteger('-51'),
    SezimalInteger('-102'): SezimalInteger('-50'),
    SezimalInteger('-101'): SezimalInteger('-45'),
    SezimalInteger('-100'): SezimalInteger('-45'),
    SezimalInteger('-55'): SezimalInteger('-44'),
    SezimalInteger('-54'): SezimalInteger('-43'),
    SezimalInteger('-53'): SezimalInteger('-42'),
    SezimalInteger('-52'): SezimalInteger('-41'),
    SezimalInteger('-51'): SezimalInteger('-41'),
    SezimalInteger('-50'): SezimalInteger('-40'),
    SezimalInteger('-45'): SezimalInteger('-35'),
    SezimalInteger('-44'): SezimalInteger('-34'),
    SezimalInteger('-43'): SezimalInteger('-34'),
    SezimalInteger('-42'): SezimalInteger('-33'),
    SezimalInteger('-41'): SezimalInteger('-32'),
    SezimalInteger('-40'): SezimalInteger('-31'),
    SezimalInteger('-35'): SezimalInteger('-30'),
    SezimalInteger('-34'): SezimalInteger('-30'),
    SezimalInteger('-33'): SezimalInteger('-25'),
    SezimalInteger('-32'): SezimalInteger('-24'),
    SezimalInteger('-31'): SezimalInteger('-23'),
    SezimalInteger('-30'): SezimalInteger('-23'),
    SezimalInteger('-25'): SezimalInteger('-22'),
    SezimalInteger('-24'): SezimalInteger('-21'),
    SezimalInteger('-23'): SezimalInteger('-20'),
    SezimalInteger('-22'): SezimalInteger('-15'),
    SezimalInteger('-21'): SezimalInteger('-15'),
    SezimalInteger('-20'): SezimalInteger('-14'),
    SezimalInteger('-15'): SezimalInteger('-13'),
    SezimalInteger('-14'): SezimalInteger('-12'),
    SezimalInteger('-13'): SezimalInteger('-12'),
    SezimalInteger('-12'): SezimalInteger('-11'),
    SezimalInteger('-11'): SezimalInteger('-10'),
    SezimalInteger('-10'): SezimalInteger('-5'),
    SezimalInteger('-5'): SezimalInteger('-4'),
    SezimalInteger('-4'): SezimalInteger('-4'),
    SezimalInteger('-3'): SezimalInteger('-3'),
    SezimalInteger('-2'): SezimalInteger('-2'),
    SezimalInteger('-1'): SezimalInteger('-1'),
    SezimalInteger('0'): SezimalInteger('0'),
    SezimalInteger('1'): SezimalInteger('1'),
    SezimalInteger('2'): SezimalInteger('2'),
    SezimalInteger('3'): SezimalInteger('3'),
    SezimalInteger('4'): SezimalInteger('4'),
    SezimalInteger('5'): SezimalInteger('4'),
    SezimalInteger('10'): SezimalInteger('5'),
    SezimalInteger('11'): SezimalInteger('10'),
    SezimalInteger('12'): SezimalInteger('11'),
    SezimalInteger('13'): SezimalInteger('12'),
    SezimalInteger('14'): SezimalInteger('12'),
    SezimalInteger('15'): SezimalInteger('13'),
    SezimalInteger('20'): SezimalInteger('14'),
    SezimalInteger('21'): SezimalInteger('15'),
    SezimalInteger('22'): SezimalInteger('15'),
    SezimalInteger('23'): SezimalInteger('20'),
    SezimalInteger('24'): SezimalInteger('21'),
    SezimalInteger('25'): SezimalInteger('22'),
    SezimalInteger('30'): SezimalInteger('23'),
    SezimalInteger('31'): SezimalInteger('23'),
    SezimalInteger('32'): SezimalInteger('24'),
    SezimalInteger('33'): SezimalInteger('25'),
    SezimalInteger('34'): SezimalInteger('30'),
    SezimalInteger('35'): SezimalInteger('30'),
    SezimalInteger('40'): SezimalInteger('31'),
    SezimalInteger('41'): SezimalInteger('32'),
    SezimalInteger('42'): SezimalInteger('33'),
    SezimalInteger('43'): SezimalInteger('34'),
    SezimalInteger('44'): SezimalInteger('34'),
    SezimalInteger('45'): SezimalInteger('35'),
    SezimalInteger('50'): SezimalInteger('40'),
    SezimalInteger('51'): SezimalInteger('41'),
    SezimalInteger('52'): SezimalInteger('41'),
    SezimalInteger('53'): SezimalInteger('42'),
    SezimalInteger('54'): SezimalInteger('43'),
    SezimalInteger('55'): SezimalInteger('44'),
    SezimalInteger('100'): SezimalInteger('45'),
    SezimalInteger('101'): SezimalInteger('45'),
    SezimalInteger('102'): SezimalInteger('50'),
    SezimalInteger('103'): SezimalInteger('51'),
    SezimalInteger('104'): SezimalInteger('52'),
    SezimalInteger('105'): SezimalInteger('52'),
    SezimalInteger('110'): SezimalInteger('53'),
    SezimalInteger('111'): SezimalInteger('54'),
    SezimalInteger('112'): SezimalInteger('55'),
    SezimalInteger('113'): SezimalInteger('100'),
    SezimalInteger('114'): SezimalInteger('100'),
    SezimalInteger('115'): SezimalInteger('101'),
    SezimalInteger('120'): SezimalInteger('102'),
}


#
# Pre-calculated decimal exponent to sezimal exponent
#
_DECIMAL_EXPONENT_TO_SEZIMAL_EXPONENT = {
    SezimalInteger('-102'): SezimalInteger('-121'),
    SezimalInteger('-101'): SezimalInteger('-120'),
    SezimalInteger('-100'): SezimalInteger('-115'),
    SezimalInteger('-55'): SezimalInteger('-113'),
    SezimalInteger('-54'): SezimalInteger('-112'),
    SezimalInteger('-53'): SezimalInteger('-111'),
    SezimalInteger('-52'): SezimalInteger('-110'),
    SezimalInteger('-51'): SezimalInteger('-104'),
    SezimalInteger('-50'): SezimalInteger('-103'),
    SezimalInteger('-45'): SezimalInteger('-102'),
    SezimalInteger('-44'): SezimalInteger('-100'),
    SezimalInteger('-43'): SezimalInteger('-55'),
    SezimalInteger('-42'): SezimalInteger('-54'),
    SezimalInteger('-41'): SezimalInteger('-53'),
    SezimalInteger('-40'): SezimalInteger('-51'),
    SezimalInteger('-35'): SezimalInteger('-50'),
    SezimalInteger('-34'): SezimalInteger('-45'),
    SezimalInteger('-33'): SezimalInteger('-43'),
    SezimalInteger('-32'): SezimalInteger('-42'),
    SezimalInteger('-31'): SezimalInteger('-41'),
    SezimalInteger('-30'): SezimalInteger('-40'),
    SezimalInteger('-25'): SezimalInteger('-34'),
    SezimalInteger('-24'): SezimalInteger('-33'),
    SezimalInteger('-23'): SezimalInteger('-32'),
    SezimalInteger('-22'): SezimalInteger('-30'),
    SezimalInteger('-21'): SezimalInteger('-25'),
    SezimalInteger('-20'): SezimalInteger('-24'),
    SezimalInteger('-15'): SezimalInteger('-23'),
    SezimalInteger('-14'): SezimalInteger('-21'),
    SezimalInteger('-13'): SezimalInteger('-20'),
    SezimalInteger('-12'): SezimalInteger('-15'),
    SezimalInteger('-11'): SezimalInteger('-13'),
    SezimalInteger('-10'): SezimalInteger('-12'),
    SezimalInteger('-5'): SezimalInteger('-11'),
    SezimalInteger('-4'): SezimalInteger('-10'),
    SezimalInteger('-3'): SezimalInteger('-4'),
    SezimalInteger('-2'): SezimalInteger('-3'),
    SezimalInteger('-1'): SezimalInteger('-2'),
    SezimalInteger('0'): SezimalInteger('0'),
    SezimalInteger('1'): SezimalInteger('2'),
    SezimalInteger('2'): SezimalInteger('3'),
    SezimalInteger('3'): SezimalInteger('4'),
    SezimalInteger('4'): SezimalInteger('10'),
    SezimalInteger('5'): SezimalInteger('11'),
    SezimalInteger('10'): SezimalInteger('12'),
    SezimalInteger('11'): SezimalInteger('13'),
    SezimalInteger('12'): SezimalInteger('15'),
    SezimalInteger('13'): SezimalInteger('20'),
    SezimalInteger('14'): SezimalInteger('21'),
    SezimalInteger('15'): SezimalInteger('23'),
    SezimalInteger('20'): SezimalInteger('24'),
    SezimalInteger('21'): SezimalInteger('25'),
    SezimalInteger('22'): SezimalInteger('30'),
    SezimalInteger('23'): SezimalInteger('32'),
    SezimalInteger('24'): SezimalInteger('33'),
    SezimalInteger('25'): SezimalInteger('34'),
    SezimalInteger('30'): SezimalInteger('40'),
    SezimalInteger('31'): SezimalInteger('41'),
    SezimalInteger('32'): SezimalInteger('42'),
    SezimalInteger('33'): SezimalInteger('43'),
    SezimalInteger('34'): SezimalInteger('45'),
    SezimalInteger('35'): SezimalInteger('50'),
    SezimalInteger('40'): SezimalInteger('51'),
    SezimalInteger('41'): SezimalInteger('53'),
    SezimalInteger('42'): SezimalInteger('54'),
    SezimalInteger('43'): SezimalInteger('55'),
    SezimalInteger('44'): SezimalInteger('100'),
    SezimalInteger('45'): SezimalInteger('102'),
    SezimalInteger('50'): SezimalInteger('103'),
    SezimalInteger('51'): SezimalInteger('104'),
    SezimalInteger('52'): SezimalInteger('110'),
    SezimalInteger('53'): SezimalInteger('111'),
    SezimalInteger('54'): SezimalInteger('112'),
    SezimalInteger('55'): SezimalInteger('113'),
    SezimalInteger('100'): SezimalInteger('115'),
    SezimalInteger('101'): SezimalInteger('120'),
    SezimalInteger('102'): SezimalInteger('121'),
}


#
# Pre-calculated sezimal exponents conversion
#
_SEZIMAL_EXPONENT_FACTOR = {
    SezimalInteger('-120'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-115'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-114'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-113'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-112'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-111'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-110'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-105'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-104'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-103'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-102'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-101'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-100'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-55'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-54'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-53'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-52'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-51'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-50'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-45'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-44'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-43'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-42'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-41'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-40'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-35'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-34'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-33'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000_000',
        ),
    SezimalInteger('-32'): SezimalFraction(
            '1 / 100_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000_000',
        ),
    SezimalInteger('-31'): SezimalFraction(
            '1 / 10_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000_000',
        ),
    SezimalInteger('-30'): SezimalFraction(
            '1 / 1_000_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000_000',
        ),
    SezimalInteger('-25'): SezimalFraction(
            '1 / 100_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000_000',
        ),
    SezimalInteger('-24'): SezimalFraction(
            '1 / 10_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000_000',
        ),
    SezimalInteger('-23'): SezimalFraction(
            '1 / 1_000_000_000_000_000',
            _precalculated_value='0.000_000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000_000',
        ),
    SezimalInteger('-22'): SezimalFraction(
            '1 / 100_000_000_000_000',
            _precalculated_value='0.000_000_000_000_01',
            _precalculated_reciprocal='100_000_000_000_000',
        ),
    SezimalInteger('-21'): SezimalFraction(
            '1 / 10_000_000_000_000',
            _precalculated_value='0.000_000_000_000_1',
            _precalculated_reciprocal='10_000_000_000_000',
        ),
    SezimalInteger('-20'): SezimalFraction(
            '1 / 1_000_000_000_000',
            _precalculated_value='0.000_000_000_001',
            _precalculated_reciprocal='1_000_000_000_000',
        ),
    SezimalInteger('-15'): SezimalFraction(
            '1 / 100_000_000_000',
            _precalculated_value='0.000_000_000_01',
            _precalculated_reciprocal='100_000_000_000',
        ),
    SezimalInteger('-14'): SezimalFraction(
            '1 / 10_000_000_000',
            _precalculated_value='0.000_000_000_1',
            _precalculated_reciprocal='10_000_000_000',
        ),
    SezimalInteger('-13'): SezimalFraction(
            '1 / 1_000_000_000',
            _precalculated_value='0.000_000_001',
            _precalculated_reciprocal='1_000_000_000',
        ),
    SezimalInteger('-12'): SezimalFraction(
            '1 / 100_000_000',
            _precalculated_value='0.000_000_01',
            _precalculated_reciprocal='100_000_000',
        ),
    SezimalInteger('-11'): SezimalFraction(
            '1 / 10_000_000',
            _precalculated_value='0.000_000_1',
            _precalculated_reciprocal='10_000_000',
        ),
    SezimalInteger('-10'): SezimalFraction(
            '1 / 1_000_000',
            _precalculated_value='0.000_001',
            _precalculated_reciprocal='1_000_000',
        ),
    SezimalInteger('-5'): SezimalFraction(
            '1 / 100_000',
            _precalculated_value='0.000_01',
            _precalculated_reciprocal='100_000',
        ),
    SezimalInteger('-4'): SezimalFraction(
            '1 / 10_000',
            _precalculated_value='0.000_1',
            _precalculated_reciprocal='10_000',
        ),
    SezimalInteger('-3'): SezimalFraction(
            '1 / 1_000',
            _precalculated_value='0.001',
            _precalculated_reciprocal='1_000',
        ),
    SezimalInteger('-2'): SezimalFraction(
            '1 / 100',
            _precalculated_value='0.01',
            _precalculated_reciprocal='100',
        ),
    SezimalInteger('-1'): SezimalFraction(
            '1 / 10',
            _precalculated_value='0.1',
            _precalculated_reciprocal='10',
        ),
    SezimalInteger('0'): SezimalFraction(
            '1 / 1',
            _precalculated_value='1',
            _precalculated_reciprocal='1',
        ),
    SezimalInteger('1'): SezimalFraction(
            '10 / 1',
            _precalculated_value='10',
            _precalculated_reciprocal='0.1',
        ),
    SezimalInteger('2'): SezimalFraction(
            '100 / 1',
            _precalculated_value='100',
            _precalculated_reciprocal='0.01',
        ),
    SezimalInteger('3'): SezimalFraction(
            '1_000 / 1',
            _precalculated_value='1_000',
            _precalculated_reciprocal='0.001',
        ),
    SezimalInteger('4'): SezimalFraction(
            '10_000 / 1',
            _precalculated_value='10_000',
            _precalculated_reciprocal='0.000_1',
        ),
    SezimalInteger('5'): SezimalFraction(
            '100_000 / 1',
            _precalculated_value='100_000',
            _precalculated_reciprocal='0.000_01',
        ),
    SezimalInteger('10'): SezimalFraction(
            '1_000_000 / 1',
            _precalculated_value='1_000_000',
            _precalculated_reciprocal='0.000_001',
        ),
    SezimalInteger('11'): SezimalFraction(
            '10_000_000 / 1',
            _precalculated_value='10_000_000',
            _precalculated_reciprocal='0.000_000_1',
        ),
    SezimalInteger('12'): SezimalFraction(
            '100_000_000 / 1',
            _precalculated_value='100_000_000',
            _precalculated_reciprocal='0.000_000_01',
        ),
    SezimalInteger('13'): SezimalFraction(
            '1_000_000_000 / 1',
            _precalculated_value='1_000_000_000',
            _precalculated_reciprocal='0.000_000_001',
        ),
    SezimalInteger('14'): SezimalFraction(
            '10_000_000_000 / 1',
            _precalculated_value='10_000_000_000',
            _precalculated_reciprocal='0.000_000_000_1',
        ),
    SezimalInteger('15'): SezimalFraction(
            '100_000_000_000 / 1',
            _precalculated_value='100_000_000_000',
            _precalculated_reciprocal='0.000_000_000_01',
        ),
    SezimalInteger('20'): SezimalFraction(
            '1_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_001',
        ),
    SezimalInteger('21'): SezimalFraction(
            '10_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_1',
        ),
    SezimalInteger('22'): SezimalFraction(
            '100_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_01',
        ),
    SezimalInteger('23'): SezimalFraction(
            '1_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_001',
        ),
    SezimalInteger('24'): SezimalFraction(
            '10_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_1',
        ),
    SezimalInteger('25'): SezimalFraction(
            '100_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_01',
        ),
    SezimalInteger('30'): SezimalFraction(
            '1_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_001',
        ),
    SezimalInteger('31'): SezimalFraction(
            '10_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_1',
        ),
    SezimalInteger('32'): SezimalFraction(
            '100_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_01',
        ),
    SezimalInteger('33'): SezimalFraction(
            '1_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_001',
        ),
    SezimalInteger('34'): SezimalFraction(
            '10_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('35'): SezimalFraction(
            '100_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('40'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('41'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('42'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('43'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('44'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('45'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('50'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('51'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('52'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('53'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('54'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('55'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('100'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('101'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('102'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('103'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('104'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('105'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('110'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('111'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('112'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('113'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_001',
        ),
    SezimalInteger('114'): SezimalFraction(
            '10_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='10_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_1',
        ),
    SezimalInteger('115'): SezimalFraction(
            '100_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='100_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_01',
        ),
    SezimalInteger('120'): SezimalFraction(
            '1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000 / 1',
            _precalculated_value='1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_001',
        ),
}

#
# Pre-calculated decimal exponents conversion
#
_DECIMAL_EXPONENT_FACTOR = {
    SezimalInteger('-102'): SezimalFraction(
            '1 / 4_242_012_532_323_105_415_404_333_144_142_511_412_054_320_214_544',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
            _precalculated_reciprocal='4_242_012_532_323_105_415_404_333_144_142_511_412_054_320_214_544',
        ),
    SezimalInteger('-101'): SezimalFraction(
            '1 / 240_112_032_020_152_545_545_132_044_010_141_545_341_020_012_144',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_002',
            _precalculated_reciprocal='240_112_032_020_152_545_545_132_044_010_141_545_341_020_012_144',
        ),
    SezimalInteger('-100'): SezimalFraction(
            '1 / 13_342_002_001_122_032_555_154_225_111_454_555_210_034_445_344',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_034',
            _precalculated_reciprocal='13_342_002_001_122_032_555_154_225_111_454_555_210_034_445_344',
        ),
    SezimalInteger('-55'): SezimalFraction(
            '1 / 543_445_000_042_335_411_044_350_304_214_411_045_224_402_544',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_001_013',
            _precalculated_reciprocal='543_445_000_042_335_411_044_350_304_214_411_045_224_402_544',
        ),
    SezimalInteger('-54'): SezimalFraction(
            '1 / 32_440_300_002_354_434_151_355_241_345_511_525_201_400_144',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_014_221',
            _precalculated_reciprocal='32_440_300_002_354_434_151_355_241_345_511_525_201_400_144',
        ),
    SezimalInteger('-53'): SezimalFraction(
            '1 / 2_024_503_333_511_024_344_211_051_210_330_442_533_433_344',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_251_540',
            _precalculated_reciprocal='2_024_503_333_511_024_344_211_051_210_330_442_533_433_344',
        ),
    SezimalInteger('-52'): SezimalFraction(
            '1 / 112_515_054_330_412_510_234_151_534_131_513_520_550_544',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_004_451_243',
            _precalculated_reciprocal='112_515_054_330_412_510_234_151_534_131_513_520_550_544',
        ),
    SezimalInteger('-51'): SezimalFraction(
            '1 / 4_253_303_243_023_141_502_121_554_343_104_331_144_144',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_000_120_042_322',
            _precalculated_reciprocal='4_253_303_243_023_141_502_121_554_343_104_331_144_144',
        ),
    SezimalInteger('-50'): SezimalFraction(
            '1 / 240_541_313_523_532_330_120_111_021_304_020_421_344',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_002_121_121_350',
            _precalculated_reciprocal='240_541_313_523_532_330_120_111_021_304_020_421_344',
        ),
    SezimalInteger('-45'): SezimalFraction(
            '1 / 13_410_053_220_220_505_231_115_301_204_001_134_544',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_000_034_140_144_213',
            _precalculated_reciprocal='13_410_053_220_220_505_231_115_301_204_001_134_544',
        ),
    SezimalInteger('-44'): SezimalFraction(
            '1 / 545_225_423_350_030_313_042_203_422_444_532_144',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_001_010_442_551_431',
            _precalculated_reciprocal='545_225_423_350_030_313_042_203_422_444_532_144',
        ),
    SezimalInteger('-43'): SezimalFraction(
            '1 / 32_535_212_433_001_504_302_345_101_251_405_344',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_014_151_525_445_311',
            _precalculated_reciprocal='32_535_212_433_001_504_302_345_101_251_405_344',
        ),
    SezimalInteger('-42'): SezimalFraction(
            '1 / 2_032_200_513_144_552_503_510_303_425_322_544',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_000_251_051_054_011_202',
            _precalculated_reciprocal='2_032_200_513_144_552_503_510_303_425_322_544',
        ),
    SezimalInteger('-41'): SezimalFraction(
            '1 / 113_122_253_155_144_252_441_503_550_320_144',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_004_435_235_324_201_223',
            _precalculated_reciprocal='113_122_253_155_144_252_441_503_550_320_144',
        ),
    SezimalInteger('-40'): SezimalFraction(
            '1 / 4_305_014_311_044_014_251_215_110_353_344',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_000_115_430_231_431_222_015',
            _precalculated_reciprocal='4_305_014_311_044_014_251_215_110_353_344',
        ),
    SezimalInteger('-35'): SezimalFraction(
            '1 / 241_412_130_414_001_014_201_041_510_544',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_002_113_304_125_321_552_254',
            _precalculated_reciprocal='241_412_130_414_001_014_201_041_510_544',
        ),
    SezimalInteger('-34'): SezimalFraction(
            '1 / 13_434_231_512_111_145_500_040_104_144',
            _precalculated_value='0.000_000_000_000_000_000_000_000_000_034_035_110_251_351_500_520',
            _precalculated_reciprocal='13_434_231_512_111_145_500_040_104_144',
        ),
    SezimalInteger('-33'): SezimalFraction(
            '1 / 551_013_104_230_421_441_113_341_344',
            _precalculated_value='0.000_000_000_000_000_000_000_000_001_005_023_544_444_250_212_513',
            _precalculated_reciprocal='551_013_104_230_421_441_113_341_344',
        ),
    SezimalInteger('-32'): SezimalFraction(
            '1 / 33_034_304_013_023_440_042_054_544',
            _precalculated_value='0.000_000_000_000_000_000_000_000_014_122_423_355_552_423_424_432',
            _precalculated_reciprocal='33_034_304_013_023_440_042_054_544',
        ),
    SezimalInteger('-31'): SezimalFraction(
            '1 / 2_035_504_000_523_551_113_452_144',
            _precalculated_value='0.000_000_000_000_000_000_000_000_250_203_220_355_503_221_235_340',
            _precalculated_reciprocal='2_035_504_000_523_551_113_452_144',
        ),
    SezimalInteger('-30'): SezimalFraction(
            '1 / 113_330_222_253_555_304_325_344',
            _precalculated_value='0.000_000_000_000_000_000_000_004_423_253_530_354_253_542_232_040',
            _precalculated_reciprocal='113_330_222_253_555_304_325_344',
        ),
    SezimalInteger('-25'): SezimalFraction(
            '1 / 4_320_350_125_444_430_242_544',
            _precalculated_value='0.000_000_000_000_000_000_000_115_214_523_110_332_523_320_133_041',
            _precalculated_reciprocal='4_320_350_125_444_430_242_544',
        ),
    SezimalInteger('-24'): SezimalFraction(
            '1 / 242_244_120_325_135_240_144',
            _precalculated_value='0.000_000_000_000_000_000_002_105_501_011_545_545_015_322_351_053',
            _precalculated_reciprocal='242_244_120_325_135_240_144',
        ),
    SezimalInteger('-23'): SezimalFraction(
            '1 / 13_502_453_354_043_313_344',
            _precalculated_value='0.000_000_000_000_000_000_033_534_214_211_415_402_311_402_235_303',
            _precalculated_reciprocal='13_502_453_354_043_313_344',
        ),
    SezimalInteger('-22'): SezimalFraction(
            '1 / 552_403_211_002_430_544',
            _precalculated_value='0.000_000_000_000_000_001_003_211_451_405_112_441_204_440_231_052',
            _precalculated_reciprocal='552_403_211_002_430_544',
        ),
    SezimalInteger('-21'): SezimalFraction(
            '1 / 33_133_534_145_024_144',
            _precalculated_value='0.000_000_000_000_000_014_053_410_044_524_023_501_315_444_115_253',
            _precalculated_reciprocal='33_133_534_145_024_144',
        ),
    SezimalInteger('-20'): SezimalFraction(
            '1 / 2_043_221_010_301_344',
            _precalculated_value='0.000_000_000_000_000_245_320_541_201_024_422_223_313_550_110_511',
            _precalculated_reciprocal='2_043_221_010_301_344',
        ),
    SezimalInteger('-15'): SezimalFraction(
            '1 / 113_534_523_014_544',
            _precalculated_value='0.000_000_000_000_004_411_333_301_214_435_200_015_243_421_552_355',
            _precalculated_reciprocal='113_534_523_014_544',
        ),
    SezimalInteger('-14'): SezimalFraction(
            '1 / 4_332_142_412_144',
            _precalculated_value='0.000_000_000_000_115_003_555_021_455_425_200_310_341_151_502_344',
            _precalculated_reciprocal='4_332_142_412_144',
        ),
    SezimalInteger('-13'): SezimalFraction(
            '1 / 243_121_245_344',
            _precalculated_value='0.000_000_000_002_102_103_542_350_153_245_205_150_101_050_242_152',
            _precalculated_reciprocal='243_121_245_344',
        ),
    SezimalInteger('-12'): SezimalFraction(
            '1 / 13_531_202_544',
            _precalculated_value='0.000_000_000_033_433_503_322_223_114_405_325_021_415_224',
            _precalculated_reciprocal='13_531_202_544',
        ),
    SezimalInteger('-11'): SezimalFraction(
            '1 / 554_200_144',
            _precalculated_value='0.000_000_001_001_402_255_400_012_054_531_442_345_110_033_303_215',
            _precalculated_reciprocal='554_200_144',
        ),
    SezimalInteger('-10'): SezimalFraction(
            '1 / 33_233_344',
            _precalculated_value='0.000_000_014_024_440_552_400_213_341_125_522_203_540_555_053_505',
            _precalculated_reciprocal='33_233_344',
        ),
    SezimalInteger('-5'): SezimalFraction(
            '1 / 2_050_544',
            _precalculated_value='0.000_000_244_435_453_502_403_440_100_254_555_303_253_543_322_315',
            _precalculated_reciprocal='2_050_544',
        ),
    SezimalInteger('-4'): SezimalFraction(
            '1 / 114_144',
            _precalculated_value='0.000_004_355_434_122_242_501_441_404_541_551_054_523_335_401_255',
            _precalculated_reciprocal='114_144',
        ),
    SezimalInteger('-3'): SezimalFraction(
            '1 / 4_344',
            _precalculated_value='0.000_114_353_410_200_324_225_504_521_311_435_341_020_032_422_551',
            _precalculated_reciprocal='4_344',
        ),
    SezimalInteger('-2'): SezimalFraction(
            '1 / 244',
            _precalculated_value='0.002_054_320_543_205_432_054_320_543_205_432_054_320_543_205_432',
            _precalculated_reciprocal='244',
        ),
    SezimalInteger('-1'): SezimalFraction(
            '1 / 14',
            _precalculated_value='0.033_333_333_333_333_333_333_333_333_333_333_333_333_333_333_334',
            _precalculated_reciprocal='14',
        ),
    SezimalInteger('0'): SezimalFraction(
            '1 / 1',
            _precalculated_value='1',
            _precalculated_reciprocal='1',
        ),
    SezimalInteger('1'): SezimalFraction(
            '14 / 1',
            _precalculated_value='14',
            _precalculated_reciprocal='0.033_333_333_333_333_333_333_333_333_333_333_333_333_333_333_334',
        ),
    SezimalInteger('2'): SezimalFraction(
            '244 / 1',
            _precalculated_value='244',
            _precalculated_reciprocal='0.002_054_320_543_205_432_054_320_543_205_432_054_320_543_205_432',
        ),
    SezimalInteger('3'): SezimalFraction(
            '4_344 / 1',
            _precalculated_value='4_344',
            _precalculated_reciprocal='0.000_114_353_410_200_324_225_504_521_311_435_341_020_032_422_551',
        ),
    SezimalInteger('4'): SezimalFraction(
            '114_144 / 1',
            _precalculated_value='114_144',
            _precalculated_reciprocal='0.000_004_355_434_122_242_501_441_404_541_551_054_523_335_401_255',
        ),
    SezimalInteger('5'): SezimalFraction(
            '2_050_544 / 1',
            _precalculated_value='2_050_544',
            _precalculated_reciprocal='0.000_000_244_435_453_502_403_440_100_254_555_303_253_543_322_315',
        ),
    SezimalInteger('10'): SezimalFraction(
            '33_233_344 / 1',
            _precalculated_value='33_233_344',
            _precalculated_reciprocal='0.000_000_014_024_440_552_400_213_341_125_522_203_540_555_053_505',
        ),
    SezimalInteger('11'): SezimalFraction(
            '554_200_144 / 1',
            _precalculated_value='554_200_144',
            _precalculated_reciprocal='0.000_000_001_001_402_255_400_012_054_531_442_345_110_033_303_215',
        ),
    SezimalInteger('12'): SezimalFraction(
            '13_531_202_544 / 1',
            _precalculated_value='13_531_202_544',
            _precalculated_reciprocal='0.000_000_000_033_433_503_322_223_114_405_325_021_415_224',
        ),
    SezimalInteger('13'): SezimalFraction(
            '243_121_245_344 / 1',
            _precalculated_value='243_121_245_344',
            _precalculated_reciprocal='0.000_000_000_002_102_103_542_350_153_245_205_150_101_050_242_152',
        ),
    SezimalInteger('14'): SezimalFraction(
            '4_332_142_412_144 / 1',
            _precalculated_value='4_332_142_412_144',
            _precalculated_reciprocal='0.000_000_000_000_115_003_555_021_455_425_200_310_341_151_502_344',
        ),
    SezimalInteger('15'): SezimalFraction(
            '113_534_523_014_544 / 1',
            _precalculated_value='113_534_523_014_544',
            _precalculated_reciprocal='0.000_000_000_000_004_411_333_301_214_435_200_015_243_421_552_355',
        ),
    SezimalInteger('20'): SezimalFraction(
            '2_043_221_010_301_344 / 1',
            _precalculated_value='2_043_221_010_301_344',
            _precalculated_reciprocal='0.000_000_000_000_000_245_320_541_201_024_422_223_313_550_110_511',
        ),
    SezimalInteger('21'): SezimalFraction(
            '33_133_534_145_024_144 / 1',
            _precalculated_value='33_133_534_145_024_144',
            _precalculated_reciprocal='0.000_000_000_000_000_014_053_410_044_524_023_501_315_444_115_253',
        ),
    SezimalInteger('22'): SezimalFraction(
            '552_403_211_002_430_544 / 1',
            _precalculated_value='552_403_211_002_430_544',
            _precalculated_reciprocal='0.000_000_000_000_000_001_003_211_451_405_112_441_204_440_231_052',
        ),
    SezimalInteger('23'): SezimalFraction(
            '13_502_453_354_043_313_344 / 1',
            _precalculated_value='13_502_453_354_043_313_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_033_534_214_211_415_402_311_402_235_303',
        ),
    SezimalInteger('24'): SezimalFraction(
            '242_244_120_325_135_240_144 / 1',
            _precalculated_value='242_244_120_325_135_240_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_002_105_501_011_545_545_015_322_351_053',
        ),
    SezimalInteger('25'): SezimalFraction(
            '4_320_350_125_444_430_242_544 / 1',
            _precalculated_value='4_320_350_125_444_430_242_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_115_214_523_110_332_523_320_133_041',
        ),
    SezimalInteger('30'): SezimalFraction(
            '113_330_222_253_555_304_325_344 / 1',
            _precalculated_value='113_330_222_253_555_304_325_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_004_423_253_530_354_253_542_232_040',
        ),
    SezimalInteger('31'): SezimalFraction(
            '2_035_504_000_523_551_113_452_144 / 1',
            _precalculated_value='2_035_504_000_523_551_113_452_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_250_203_220_355_503_221_235_340',
        ),
    SezimalInteger('32'): SezimalFraction(
            '33_034_304_013_023_440_042_054_544 / 1',
            _precalculated_value='33_034_304_013_023_440_042_054_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_014_122_423_355_552_423_424_432',
        ),
    SezimalInteger('33'): SezimalFraction(
            '551_013_104_230_421_441_113_341_344 / 1',
            _precalculated_value='551_013_104_230_421_441_113_341_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_001_005_023_544_444_250_212_513',
        ),
    SezimalInteger('34'): SezimalFraction(
            '13_434_231_512_111_145_500_040_104_144 / 1',
            _precalculated_value='13_434_231_512_111_145_500_040_104_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_034_035_110_251_351_500_520',
        ),
    SezimalInteger('35'): SezimalFraction(
            '241_412_130_414_001_014_201_041_510_544 / 1',
            _precalculated_value='241_412_130_414_001_014_201_041_510_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_002_113_304_125_321_552_254',
        ),
    SezimalInteger('40'): SezimalFraction(
            '4_305_014_311_044_014_251_215_110_353_344 / 1',
            _precalculated_value='4_305_014_311_044_014_251_215_110_353_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_115_430_231_431_222_015',
        ),
    SezimalInteger('41'): SezimalFraction(
            '113_122_253_155_144_252_441_503_550_320_144 / 1',
            _precalculated_value='113_122_253_155_144_252_441_503_550_320_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_004_435_235_324_201_223',
        ),
    SezimalInteger('42'): SezimalFraction(
            '2_032_200_513_144_552_503_510_303_425_322_544 / 1',
            _precalculated_value='2_032_200_513_144_552_503_510_303_425_322_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_251_051_054_011_202',
        ),
    SezimalInteger('43'): SezimalFraction(
            '32_535_212_433_001_504_302_345_101_251_405_344 / 1',
            _precalculated_value='32_535_212_433_001_504_302_345_101_251_405_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_014_151_525_445_311',
        ),
    SezimalInteger('44'): SezimalFraction(
            '545_225_423_350_030_313_042_203_422_444_532_144 / 1',
            _precalculated_value='545_225_423_350_030_313_042_203_422_444_532_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_001_010_442_551_431',
        ),
    SezimalInteger('45'): SezimalFraction(
            '13_410_053_220_220_505_231_115_301_204_001_134_544 / 1',
            _precalculated_value='13_410_053_220_220_505_231_115_301_204_001_134_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_034_140_144_213',
        ),
    SezimalInteger('50'): SezimalFraction(
            '240_541_313_523_532_330_120_111_021_304_020_421_344 / 1',
            _precalculated_value='240_541_313_523_532_330_120_111_021_304_020_421_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_002_121_121_350',
        ),
    SezimalInteger('51'): SezimalFraction(
            '4_253_303_243_023_141_502_121_554_343_104_331_144_144 / 1',
            _precalculated_value='4_253_303_243_023_141_502_121_554_343_104_331_144_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_120_042_322',
        ),
    SezimalInteger('52'): SezimalFraction(
            '112_515_054_330_412_510_234_151_534_131_513_520_550_544 / 1',
            _precalculated_value='112_515_054_330_412_510_234_151_534_131_513_520_550_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_004_451_243',
        ),
    SezimalInteger('53'): SezimalFraction(
            '2_024_503_333_511_024_344_211_051_210_330_442_533_433_344 / 1',
            _precalculated_value='2_024_503_333_511_024_344_211_051_210_330_442_533_433_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_251_540',
        ),
    SezimalInteger('54'): SezimalFraction(
            '32_440_300_002_354_434_151_355_241_345_511_525_201_400_144 / 1',
            _precalculated_value='32_440_300_002_354_434_151_355_241_345_511_525_201_400_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_014_221',
        ),
    SezimalInteger('55'): SezimalFraction(
            '543_445_000_042_335_411_044_350_304_214_411_045_224_402_544 / 1',
            _precalculated_value='543_445_000_042_335_411_044_350_304_214_411_045_224_402_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_001_013',
        ),
    SezimalInteger('100'): SezimalFraction(
            '13_342_002_001_122_032_555_154_225_111_454_555_210_034_445_344 / 1',
            _precalculated_value='13_342_002_001_122_032_555_154_225_111_454_555_210_034_445_344',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_034',
        ),
    SezimalInteger('101'): SezimalFraction(
            '240_112_032_020_152_545_545_132_044_010_141_545_341_020_012_144 / 1',
            _precalculated_value='240_112_032_020_152_545_545_132_044_010_141_545_341_020_012_144',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_002',
        ),
    SezimalInteger('102'): SezimalFraction(
            '4_242_012_532_323_105_415_404_333_144_142_511_412_054_320_214_544 / 1',
            _precalculated_value='4_242_012_532_323_105_415_404_333_144_142_511_412_054_320_214_544',
            _precalculated_reciprocal='0.000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000',
        ),
}

#
# Pre-calculated sezimal exponent to symbol
#
_SEZIMAL_EXPONENT_TO_SYMBOL = {
    SezimalInteger('-120'): 'ndx',
    SezimalInteger('-115'): 'nxp',
    SezimalInteger('-114'): 'nxc',
    SezimalInteger('-113'): 'nxt',
    SezimalInteger('-112'): 'nxd',
    SezimalInteger('-111'): 'nxe',
    SezimalInteger('-110'): 'nx',
    SezimalInteger('-105'): 'np',
    SezimalInteger('-104'): 'nc',
    SezimalInteger('-103'): 'nt',
    SezimalInteger('-102'): 'nd',
    SezimalInteger('-101'): 'ne',
    SezimalInteger('-100'): 'n',
    SezimalInteger('-55'): 'pp',
    SezimalInteger('-54'): 'pc',
    SezimalInteger('-53'): 'pt',
    SezimalInteger('-52'): 'pd',
    SezimalInteger('-51'): 'pe',
    SezimalInteger('-50'): 'px',
    SezimalInteger('-45'): 'cp',
    SezimalInteger('-44'): 'cc',
    SezimalInteger('-43'): 'ct',
    SezimalInteger('-42'): 'cd',
    SezimalInteger('-41'): 'ce',
    SezimalInteger('-40'): 'cx',
    SezimalInteger('-35'): 'tp',
    SezimalInteger('-34'): 'tc',
    SezimalInteger('-33'): 'tt',
    SezimalInteger('-32'): 'td',
    SezimalInteger('-31'): 'te',
    SezimalInteger('-30'): 'tx',
    SezimalInteger('-25'): 'dp',
    SezimalInteger('-24'): 'dc',
    SezimalInteger('-23'): 'dt',
    SezimalInteger('-22'): 'dd',
    SezimalInteger('-21'): 'de',
    SezimalInteger('-20'): 'dx',
    SezimalInteger('-15'): 'xp',
    SezimalInteger('-14'): 'xc',
    SezimalInteger('-13'): 'xt',
    SezimalInteger('-12'): 'xd',
    SezimalInteger('-11'): 'xe',
    SezimalInteger('-10'): 'x',
    SezimalInteger('-5'): 'p',
    SezimalInteger('-4'): 'c',
    SezimalInteger('-3'): 't',
    SezimalInteger('-2'): 'd',
    SezimalInteger('-1'): 'e',
    SezimalInteger('1'): 'E',
    SezimalInteger('2'): 'D',
    SezimalInteger('3'): 'T',
    SezimalInteger('4'): 'C',
    SezimalInteger('5'): 'P',
    SezimalInteger('10'): 'X',
    SezimalInteger('11'): 'XE',
    SezimalInteger('12'): 'XD',
    SezimalInteger('13'): 'XT',
    SezimalInteger('14'): 'XC',
    SezimalInteger('15'): 'XP',
    SezimalInteger('20'): 'DX',
    SezimalInteger('21'): 'DE',
    SezimalInteger('22'): 'DD',
    SezimalInteger('23'): 'DT',
    SezimalInteger('24'): 'DC',
    SezimalInteger('25'): 'DP',
    SezimalInteger('30'): 'TX',
    SezimalInteger('31'): 'TE',
    SezimalInteger('32'): 'TD',
    SezimalInteger('33'): 'TT',
    SezimalInteger('34'): 'TC',
    SezimalInteger('35'): 'TP',
    SezimalInteger('40'): 'CX',
    SezimalInteger('41'): 'CE',
    SezimalInteger('42'): 'CD',
    SezimalInteger('43'): 'CT',
    SezimalInteger('44'): 'CC',
    SezimalInteger('45'): 'CP',
    SezimalInteger('50'): 'PX',
    SezimalInteger('51'): 'PE',
    SezimalInteger('52'): 'PD',
    SezimalInteger('53'): 'PT',
    SezimalInteger('54'): 'PC',
    SezimalInteger('55'): 'PP',
    SezimalInteger('100'): 'N',
    SezimalInteger('101'): 'NE',
    SezimalInteger('102'): 'ND',
    SezimalInteger('103'): 'NT',
    SezimalInteger('104'): 'NC',
    SezimalInteger('105'): 'NP',
    SezimalInteger('110'): 'NX',
    SezimalInteger('111'): 'NXE',
    SezimalInteger('112'): 'NXD',
    SezimalInteger('113'): 'NXT',
    SezimalInteger('114'): 'NXC',
    SezimalInteger('115'): 'NXP',
    SezimalInteger('120'): 'NDX',
}
_SEZIMAL_SYMBOL_TO_EXPONENT = {symbol: exponent for symbol, exponent in _SEZIMAL_EXPONENT_TO_SYMBOL.items()}
_SEZIMAL_SYMBOL_TO_EXPONENT.update({symbol.lower() + 't' if exponent < 0 else 'm': exponent for exponent, symbol in _SEZIMAL_EXPONENT_TO_SYMBOL.items()})


#
# Pre-calculated sezimal exponent to prefix
#
_SEZIMAL_EXPONENT_TO_PREFIX = {
    SezimalInteger('-120'): 'nidishati',
    SezimalInteger('-115'): 'nishapanti',
    SezimalInteger('-114'): 'nishacharti',
    SezimalInteger('-113'): 'nishatriti',
    SezimalInteger('-112'): 'nishaditi',
    SezimalInteger('-111'): 'nishaekati',
    SezimalInteger('-110'): 'nishati',
    SezimalInteger('-105'): 'nipanti',
    SezimalInteger('-104'): 'nicharti',
    SezimalInteger('-103'): 'nitriti',
    SezimalInteger('-102'): 'niditi',
    SezimalInteger('-101'): 'niekati',
    SezimalInteger('-100'): 'niti',
    SezimalInteger('-55'): 'panpanti',
    SezimalInteger('-54'): 'pancharti',
    SezimalInteger('-53'): 'pantriti',
    SezimalInteger('-52'): 'panditi',
    SezimalInteger('-51'): 'panekati',
    SezimalInteger('-50'): 'panshati',
    SezimalInteger('-45'): 'charpanti',
    SezimalInteger('-44'): 'charcharti',
    SezimalInteger('-43'): 'chartriti',
    SezimalInteger('-42'): 'charditi',
    SezimalInteger('-41'): 'charekati',
    SezimalInteger('-40'): 'charshati',
    SezimalInteger('-35'): 'tripanti',
    SezimalInteger('-34'): 'tricharti',
    SezimalInteger('-33'): 'tritriti',
    SezimalInteger('-32'): 'triditi',
    SezimalInteger('-31'): 'triekati',
    SezimalInteger('-30'): 'trishati',
    SezimalInteger('-25'): 'dipanti',
    SezimalInteger('-24'): 'dicharti',
    SezimalInteger('-23'): 'ditriti',
    SezimalInteger('-22'): 'diditi',
    SezimalInteger('-21'): 'diekati',
    SezimalInteger('-20'): 'dishati',
    SezimalInteger('-15'): 'shapanti',
    SezimalInteger('-14'): 'shacharti',
    SezimalInteger('-13'): 'shatriti',
    SezimalInteger('-12'): 'shaditi',
    SezimalInteger('-11'): 'shaekati',
    SezimalInteger('-10'): 'shati',
    SezimalInteger('-5'): 'panti',
    SezimalInteger('-4'): 'charti',
    SezimalInteger('-3'): 'triti',
    SezimalInteger('-2'): 'diti',
    SezimalInteger('-1'): 'ekati',
    SezimalInteger('1'): 'ekama',
    SezimalInteger('2'): 'dima',
    SezimalInteger('3'): 'trima',
    SezimalInteger('4'): 'charma',
    SezimalInteger('5'): 'pama',
    SezimalInteger('10'): 'shama',
    SezimalInteger('11'): 'shaekama',
    SezimalInteger('12'): 'shadima',
    SezimalInteger('13'): 'shatrima',
    SezimalInteger('14'): 'shacharma',
    SezimalInteger('15'): 'shapama',
    SezimalInteger('20'): 'dishama',
    SezimalInteger('21'): 'diekama',
    SezimalInteger('22'): 'didima',
    SezimalInteger('23'): 'ditrima',
    SezimalInteger('24'): 'dicharma',
    SezimalInteger('25'): 'dipama',
    SezimalInteger('30'): 'trishama',
    SezimalInteger('31'): 'triekama',
    SezimalInteger('32'): 'tridima',
    SezimalInteger('33'): 'tritrima',
    SezimalInteger('34'): 'tricharma',
    SezimalInteger('35'): 'tripama',
    SezimalInteger('40'): 'charshama',
    SezimalInteger('41'): 'charekama',
    SezimalInteger('42'): 'chardima',
    SezimalInteger('43'): 'chartrima',
    SezimalInteger('44'): 'charcharma',
    SezimalInteger('45'): 'charpama',
    SezimalInteger('50'): 'panshama',
    SezimalInteger('51'): 'panekama',
    SezimalInteger('52'): 'pandima',
    SezimalInteger('53'): 'pantrima',
    SezimalInteger('54'): 'pancharma',
    SezimalInteger('55'): 'panpama',
    SezimalInteger('100'): 'nima',
    SezimalInteger('101'): 'niekama',
    SezimalInteger('102'): 'nidima',
    SezimalInteger('103'): 'nitrima',
    SezimalInteger('104'): 'nicharma',
    SezimalInteger('105'): 'nipama',
    SezimalInteger('110'): 'nishama',
    SezimalInteger('111'): 'nishaekama',
    SezimalInteger('112'): 'nishadima',
    SezimalInteger('113'): 'nishatrima',
    SezimalInteger('114'): 'nishacharma',
    SezimalInteger('115'): 'nishapama',
    SezimalInteger('120'): 'nidishama',
}
_SEZIMAL_PREFIX_TO_EXPONENT = {prefix: exponent for exponent, prefix in _SEZIMAL_EXPONENT_TO_SYMBOL.items()}


_DECIMAL_EXPONENT_SYMBOL = {
    SezimalInteger('-102'): 'q',
    SezimalInteger('-101'): 'q',
    SezimalInteger('-100'): 'q',
    SezimalInteger('-55'): 'q',
    SezimalInteger('-54'): 'q',
    SezimalInteger('-53'): 'q',
    SezimalInteger('-52'): 'q',
    SezimalInteger('-51'): 'q',
    SezimalInteger('-50'): 'q',
    SezimalInteger('-45'): 'r',
    SezimalInteger('-44'): 'r',
    SezimalInteger('-43'): 'r',
    SezimalInteger('-42'): 'y',
    SezimalInteger('-41'): 'y',
    SezimalInteger('-40'): 'y',
    SezimalInteger('-35'): 'z',
    SezimalInteger('-34'): 'z',
    SezimalInteger('-33'): 'z',
    SezimalInteger('-32'): 'a',
    SezimalInteger('-31'): 'a',
    SezimalInteger('-30'): 'a',
    SezimalInteger('-25'): 'f',
    SezimalInteger('-24'): 'f',
    SezimalInteger('-23'): 'f',
    SezimalInteger('-22'): 'p',
    SezimalInteger('-21'): 'p',
    SezimalInteger('-20'): 'p',
    SezimalInteger('-15'): 'n',
    SezimalInteger('-14'): 'n',
    SezimalInteger('-13'): 'n',
    SezimalInteger('-12'): 'µ',
    SezimalInteger('-11'): 'µ',
    SezimalInteger('-10'): 'µ',
    SezimalInteger('-5'): 'm',
    SezimalInteger('-4'): 'm',
    SezimalInteger('-3'): 'm',
    SezimalInteger('-2'): 'c',
    SezimalInteger('-1'): 'd',
    SezimalInteger('1'): 'da',
    SezimalInteger('2'): 'h',
    SezimalInteger('3'): 'k',
    SezimalInteger('4'): 'k',
    SezimalInteger('5'): 'k',
    SezimalInteger('10'): 'M',
    SezimalInteger('11'): 'M',
    SezimalInteger('12'): 'M',
    SezimalInteger('13'): 'G',
    SezimalInteger('14'): 'G',
    SezimalInteger('15'): 'G',
    SezimalInteger('20'): 'T',
    SezimalInteger('21'): 'T',
    SezimalInteger('22'): 'T',
    SezimalInteger('23'): 'P',
    SezimalInteger('24'): 'P',
    SezimalInteger('25'): 'P',
    SezimalInteger('30'): 'E',
    SezimalInteger('31'): 'E',
    SezimalInteger('32'): 'E',
    SezimalInteger('33'): 'Z',
    SezimalInteger('34'): 'Z',
    SezimalInteger('35'): 'Z',
    SezimalInteger('40'): 'Y',
    SezimalInteger('41'): 'Y',
    SezimalInteger('42'): 'Y',
    SezimalInteger('43'): 'R',
    SezimalInteger('44'): 'R',
    SezimalInteger('45'): 'R',
    SezimalInteger('50'): 'Q',
    SezimalInteger('51'): 'Q',
    SezimalInteger('52'): 'Q',
    SezimalInteger('53'): 'Q',
    SezimalInteger('54'): 'Q',
    SezimalInteger('55'): 'Q',
    SezimalInteger('100'): 'Q',
    SezimalInteger('101'): 'Q',
    SezimalInteger('102'): 'Q',
}
_DECIMAL_SYMBOL_EXPONENT = {symbol: exponent for exponent, symbol in _DECIMAL_EXPONENT_SYMBOL.items()}

_DECIMAL_EXPONENT_PREFIX = {
    SezimalInteger('-102'): 'quecto',
    SezimalInteger('-101'): 'quecto',
    SezimalInteger('-100'): 'quecto',
    SezimalInteger('-55'): 'quecto',
    SezimalInteger('-54'): 'quecto',
    SezimalInteger('-53'): 'quecto',
    SezimalInteger('-52'): 'quecto',
    SezimalInteger('-51'): 'quecto',
    SezimalInteger('-50'): 'quecto',
    SezimalInteger('-45'): 'ronto',
    SezimalInteger('-44'): 'ronto',
    SezimalInteger('-43'): 'ronto',
    SezimalInteger('-42'): 'yocto',
    SezimalInteger('-41'): 'yocto',
    SezimalInteger('-40'): 'yocto',
    SezimalInteger('-35'): 'zepto',
    SezimalInteger('-34'): 'zepto',
    SezimalInteger('-33'): 'zepto',
    SezimalInteger('-32'): 'atto',
    SezimalInteger('-31'): 'atto',
    SezimalInteger('-30'): 'atto',
    SezimalInteger('-25'): 'femto',
    SezimalInteger('-24'): 'femto',
    SezimalInteger('-23'): 'femto',
    SezimalInteger('-22'): 'pico',
    SezimalInteger('-21'): 'pico',
    SezimalInteger('-20'): 'pico',
    SezimalInteger('-15'): 'nano',
    SezimalInteger('-14'): 'nano',
    SezimalInteger('-13'): 'nano',
    SezimalInteger('-12'): 'micro',
    SezimalInteger('-11'): 'micro',
    SezimalInteger('-10'): 'micro',
    SezimalInteger('-5'): 'milli',
    SezimalInteger('-4'): 'milli',
    SezimalInteger('-3'): 'milli',
    SezimalInteger('-2'): 'centi',
    SezimalInteger('-1'): 'deci',
    SezimalInteger('1'): 'deca',
    SezimalInteger('2'): 'hecto',
    SezimalInteger('3'): 'kilo',
    SezimalInteger('4'): 'kilo',
    SezimalInteger('5'): 'kilo',
    SezimalInteger('10'): 'mega',
    SezimalInteger('11'): 'mega',
    SezimalInteger('12'): 'mega',
    SezimalInteger('13'): 'giga',
    SezimalInteger('14'): 'giga',
    SezimalInteger('15'): 'giga',
    SezimalInteger('20'): 'tera',
    SezimalInteger('21'): 'tera',
    SezimalInteger('22'): 'tera',
    SezimalInteger('23'): 'peta',
    SezimalInteger('24'): 'peta',
    SezimalInteger('25'): 'peta',
    SezimalInteger('30'): 'exa',
    SezimalInteger('31'): 'exa',
    SezimalInteger('32'): 'exa',
    SezimalInteger('33'): 'zetta',
    SezimalInteger('34'): 'zetta',
    SezimalInteger('35'): 'zetta',
    SezimalInteger('40'): 'yotta',
    SezimalInteger('41'): 'yotta',
    SezimalInteger('42'): 'yotta',
    SezimalInteger('43'): 'ronna',
    SezimalInteger('44'): 'ronna',
    SezimalInteger('45'): 'ronna',
    SezimalInteger('50'): 'quetta',
    SezimalInteger('51'): 'quetta',
    SezimalInteger('52'): 'quetta',
    SezimalInteger('53'): 'quetta',
    SezimalInteger('54'): 'quetta',
    SezimalInteger('55'): 'quetta',
    SezimalInteger('100'): 'quetta',
    SezimalInteger('101'): 'quetta',
    SezimalInteger('102'): 'quetta',
}
_DECIMAL_PREFIX_EXPONENT = {prefix: exponent for exponent, prefix in _DECIMAL_EXPONENT_PREFIX.items()}
