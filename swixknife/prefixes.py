
__all__ = [
    'SezimalPrefix',
    'SEZIMAL_PREFIX_QUESSE',
    'SEZIMAL_PREFIX_ROSSE',
    'SEZIMAL_PREFIX_YOSSE',
    'SEZIMAL_PREFIX_ZESSE',
    'SEZIMAL_PREFIX_EXASSE',
    'SEZIMAL_PREFIX_PESSE',
    'SEZIMAL_PREFIX_TESSE',
    'SEZIMAL_PREFIX_GISSE',
    'SEZIMAL_PREFIX_MESSE',
    'SEZIMAL_PREFIX_ZILO',
    'SEZIMAL_PREFIX_SEZO',
    'SEZIMAL_PREFIX_ZENO',
    'SEZIMAL_PREFIX_SESSO',
    'SEZIMAL_PREFIX_BASE',
    'SEZIMAL_PREFIX_SESSI',
    'SEZIMAL_PREFIX_ZENI',
    'SEZIMAL_PREFIX_SEZI',
    'SEZIMAL_PREFIX_ZILI',
    'SEZIMAL_PREFIX_MESSI',
    'SEZIMAL_PREFIX_GISSI',
    'SEZIMAL_PREFIX_TESSI',
    'SEZIMAL_PREFIX_PESSI',
    'SEZIMAL_PREFIX_EXASSI',
    'SEZIMAL_PREFIX_ZESSI',
    'SEZIMAL_PREFIX_YOSSI',
    'SEZIMAL_PREFIX_ROSSI',
    'SEZIMAL_PREFIX_QUESSI',
    'SEZIMAL_PREFIXES',

    'DecimalPrefix',
    'DECIMAL_PREFIX_QUETTA',
    'DECIMAL_PREFIX_RONNA',
    'DECIMAL_PREFIX_YOTTA',
    'DECIMAL_PREFIX_ZETTA',
    'DECIMAL_PREFIX_EXA',
    'DECIMAL_PREFIX_PETA',
    'DECIMAL_PREFIX_TERA',
    'DECIMAL_PREFIX_GIGA',
    'DECIMAL_PREFIX_MEGA',
    'DECIMAL_PREFIX_KILO',
    'DECIMAL_PREFIX_HECTO',
    'DECIMAL_PREFIX_DECA',
    'DECIMAL_PREFIX_BASE',
    'DECIMAL_PREFIX_DECI',
    'DECIMAL_PREFIX_CENTI',
    'DECIMAL_PREFIX_MILLI',
    'DECIMAL_PREFIX_MICRO',
    'DECIMAL_PREFIX_NANO',
    'DECIMAL_PREFIX_PICO',
    'DECIMAL_PREFIX_FEMTO',
    'DECIMAL_PREFIX_ATTO',
    'DECIMAL_PREFIX_ZEPTO',
    'DECIMAL_PREFIX_YOCTO',
    'DECIMAL_PREFIX_RONTO',
    'DECIMAL_PREFIX_QUECTO',
    'DECIMAL_PREFIXES',

    'SEZIMAL_PREFIX_TO_DECIMAL',
    'DECIMAL_PREFIX_TO_SEZIMAL',

    'sezimal_exponent_to_decimal',
    'decimal_exponent_to_sezimal',

    'sezimal_prefix_exponent_to_decimal',
    'decimal_prefix_exponent_to_sezimal',
]

from typing import TypeVar

PrefixClass = TypeVar('PrefixClass', bound='Prefix')
SezimalPrefixClass = TypeVar('SezimalPrefixClass', bound='SezimalPrefix')
DecimalPrefixClass = TypeVar('DecimalPrefixClass', bound='DecimalPrefix')


from decimal import Decimal
from .sezimal import Sezimal


class Prefix:
    def __init__(self, symbol: str, name: str, exponent: Sezimal, base: Sezimal = Sezimal(10)) -> PrefixClass:
        self.symbol = symbol
        self.name = name
        self.exponent = exponent
        self.base = base

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Prefix(symbol='{self.symbol}', name='{self.name}')"

    @property
    def multiplier(self) -> Sezimal:
        multiplier = Sezimal(1)

        for i in range(0, int(abs(self.exponent.decimal))):
            if self.exponent < 0:
                multiplier /= self.base
            else:
                multiplier *= self.base

        return multiplier


class SezimalPrefix(Prefix):
    def __init__(self, symbol: str, name: str, exponent: Sezimal) -> SezimalPrefixClass:
        return super().__init__(symbol, name, exponent, Sezimal(10))

    def __repr__(self):
        return f"SezimalPrefix(symbol='{self.symbol}', name='{self.name}')"


class DecimalPrefix(Prefix):
    def __init__(self, symbol: str, name: str, exponent: Sezimal) -> DecimalPrefixClass:
        return super().__init__(symbol, name, exponent, Sezimal(14))

    def __repr__(self):
        return f"DecimalPrefix(symbol='{self.symbol}', name='{self.name}')"


#
# Sezimal prefixes
#
SEZIMAL_PREFIX_QUESSE = SezimalPrefix('Qe', 'quesse',  Sezimal('104'))
SEZIMAL_PREFIX_ROSSE =  SezimalPrefix('Re',  'rosse',  Sezimal('100'))
SEZIMAL_PREFIX_YOSSE =  SezimalPrefix('Ye',  'yosse',   Sezimal('52'))
SEZIMAL_PREFIX_ZESSE =  SezimalPrefix('Ze',  'zesse',   Sezimal('44'))
SEZIMAL_PREFIX_EXASSE = SezimalPrefix('Ee', 'exasse',   Sezimal('40'))
SEZIMAL_PREFIX_PESSE =  SezimalPrefix('Pe',  'pesse',   Sezimal('32'))
SEZIMAL_PREFIX_TESSE =  SezimalPrefix('Te',  'tesse',   Sezimal('24'))
SEZIMAL_PREFIX_GISSE =  SezimalPrefix('Ge',  'gisse',   Sezimal('20'))
SEZIMAL_PREFIX_MESSE =  SezimalPrefix('Me',  'messe',   Sezimal('12'))
SEZIMAL_PREFIX_ZILO =   SezimalPrefix('Zl',   'zilo',    Sezimal('4'))
SEZIMAL_PREFIX_SEZO =   SezimalPrefix('Sz',   'sezo',    Sezimal('3'))
SEZIMAL_PREFIX_ZENO =   SezimalPrefix('Zn',   'zeno',    Sezimal('2'))
SEZIMAL_PREFIX_SESSO =  SezimalPrefix('Ss',  'sesso',    Sezimal('1'))

SEZIMAL_PREFIX_BASE =   SezimalPrefix('',         '',    Sezimal('0'))

SEZIMAL_PREFIX_SESSI =  SezimalPrefix('ss',  'sessi',   Sezimal('-1'))
SEZIMAL_PREFIX_ZENI =   SezimalPrefix('zn',   'zeni',   Sezimal('-2'))
SEZIMAL_PREFIX_SEZI =   SezimalPrefix('sz',   'sezi',   Sezimal('-3'))
SEZIMAL_PREFIX_ZILI =   SezimalPrefix('zl',   'zili',   Sezimal('-4'))
SEZIMAL_PREFIX_MESSI =  SezimalPrefix('me',  'messi',  Sezimal('-12'))
SEZIMAL_PREFIX_GISSI =  SezimalPrefix('ge',  'gissi',  Sezimal('-20'))
SEZIMAL_PREFIX_TESSI =  SezimalPrefix('te',  'tessi',  Sezimal('-24'))
SEZIMAL_PREFIX_PESSI =  SezimalPrefix('pe',  'pessi',  Sezimal('-32'))
SEZIMAL_PREFIX_EXASSI = SezimalPrefix('ee', 'exassi',  Sezimal('-40'))
SEZIMAL_PREFIX_ZESSI =  SezimalPrefix('ze',  'zessi',  Sezimal('-44'))
SEZIMAL_PREFIX_YOSSI =  SezimalPrefix('ye',  'yossi',  Sezimal('-52'))
SEZIMAL_PREFIX_ROSSI =  SezimalPrefix('re',  'rossi', Sezimal('-100'))
SEZIMAL_PREFIX_QUESSI = SezimalPrefix('qe', 'quessi', Sezimal('-104'))

SEZIMAL_PREFIXES = [
    SEZIMAL_PREFIX_QUESSE,
    SEZIMAL_PREFIX_ROSSE,
    SEZIMAL_PREFIX_YOSSE,
    SEZIMAL_PREFIX_ZESSE,
    SEZIMAL_PREFIX_EXASSE,
    SEZIMAL_PREFIX_PESSE,
    SEZIMAL_PREFIX_TESSE,
    SEZIMAL_PREFIX_GISSE,
    SEZIMAL_PREFIX_MESSE,
    SEZIMAL_PREFIX_ZILO ,
    SEZIMAL_PREFIX_SEZO ,
    SEZIMAL_PREFIX_ZENO ,
    SEZIMAL_PREFIX_SESSO,

    SEZIMAL_PREFIX_BASE ,

    SEZIMAL_PREFIX_SESSI,
    SEZIMAL_PREFIX_ZENI ,
    SEZIMAL_PREFIX_SEZI ,
    SEZIMAL_PREFIX_ZILI ,
    SEZIMAL_PREFIX_MESSI,
    SEZIMAL_PREFIX_GISSI,
    SEZIMAL_PREFIX_TESSI,
    SEZIMAL_PREFIX_PESSI,
    SEZIMAL_PREFIX_EXASSI,
    SEZIMAL_PREFIX_ZESSI,
    SEZIMAL_PREFIX_YOSSI,
    SEZIMAL_PREFIX_ROSSI,
    SEZIMAL_PREFIX_QUESSI,
]


#
# Decimal prefixes
#
DECIMAL_PREFIX_QUETTA = DecimalPrefix('Q', 'quetta',  Sezimal('50'))
DECIMAL_PREFIX_RONNA =  DecimalPrefix('R',  'ronna',  Sezimal('43'))
DECIMAL_PREFIX_YOTTA =  DecimalPrefix('Y',  'yotta',  Sezimal('40'))
DECIMAL_PREFIX_ZETTA =  DecimalPrefix('Z',  'zetta',  Sezimal('33'))
DECIMAL_PREFIX_EXA =    DecimalPrefix('E',    'exa',  Sezimal('30'))
DECIMAL_PREFIX_PETA =   DecimalPrefix('P',   'peta',  Sezimal('23'))
DECIMAL_PREFIX_TERA =   DecimalPrefix('T',   'tera',  Sezimal('20'))
DECIMAL_PREFIX_GIGA =   DecimalPrefix('G',   'giga',  Sezimal('13'))
DECIMAL_PREFIX_MEGA =   DecimalPrefix('M',   'mega',  Sezimal('10'))
DECIMAL_PREFIX_KILO =   DecimalPrefix('k',   'kilo',   Sezimal('3'))
DECIMAL_PREFIX_HECTO =  DecimalPrefix('h',  'hecto',   Sezimal('2'))
DECIMAL_PREFIX_DECA =   DecimalPrefix('da',  'deca',   Sezimal('1'))

DECIMAL_PREFIX_BASE =   DecimalPrefix('',        '',   Sezimal('0'))

DECIMAL_PREFIX_DECI =   DecimalPrefix('d',   'deci',  Sezimal('-1'))
DECIMAL_PREFIX_CENTI =  DecimalPrefix('c',  'centi',  Sezimal('-2'))
DECIMAL_PREFIX_MILLI =  DecimalPrefix('m',  'milli',  Sezimal('-3'))
DECIMAL_PREFIX_MICRO =  DecimalPrefix('µ',  'micro', Sezimal('-10'))
DECIMAL_PREFIX_NANO =   DecimalPrefix('n',   'nano', Sezimal('-13'))
DECIMAL_PREFIX_PICO =   DecimalPrefix('p',   'pico', Sezimal('-20'))
DECIMAL_PREFIX_FEMTO =  DecimalPrefix('f',  'femto', Sezimal('-23'))
DECIMAL_PREFIX_ATTO =   DecimalPrefix('a',   'atto', Sezimal('-30'))
DECIMAL_PREFIX_ZEPTO =  DecimalPrefix('z',  'zepto', Sezimal('-33'))
DECIMAL_PREFIX_YOCTO =  DecimalPrefix('y',  'yocto', Sezimal('-40'))
DECIMAL_PREFIX_RONTO =  DecimalPrefix('r',  'ronto', Sezimal('-43'))
DECIMAL_PREFIX_QUECTO = DecimalPrefix('q', 'quecto', Sezimal('-50'))

DECIMAL_PREFIXES = [
    DECIMAL_PREFIX_QUETTA,
    DECIMAL_PREFIX_RONNA,
    DECIMAL_PREFIX_YOTTA,
    DECIMAL_PREFIX_ZETTA,
    DECIMAL_PREFIX_EXA,
    DECIMAL_PREFIX_PETA,
    DECIMAL_PREFIX_TERA,
    DECIMAL_PREFIX_GIGA,
    DECIMAL_PREFIX_MEGA,
    DECIMAL_PREFIX_KILO,
    DECIMAL_PREFIX_HECTO,
    DECIMAL_PREFIX_DECA,

    DECIMAL_PREFIX_BASE,

    DECIMAL_PREFIX_DECI,
    DECIMAL_PREFIX_CENTI,
    DECIMAL_PREFIX_MILLI,
    DECIMAL_PREFIX_MICRO,
    DECIMAL_PREFIX_NANO,
    DECIMAL_PREFIX_PICO,
    DECIMAL_PREFIX_FEMTO,
    DECIMAL_PREFIX_ATTO,
    DECIMAL_PREFIX_ZEPTO,
    DECIMAL_PREFIX_YOCTO,
    DECIMAL_PREFIX_RONTO,
    DECIMAL_PREFIX_QUECTO,
]

SEZIMAL_PREFIX_TO_DECIMAL = {
    SEZIMAL_PREFIX_QUESSE: DECIMAL_PREFIX_QUETTA,
    SEZIMAL_PREFIX_ROSSE:  DECIMAL_PREFIX_RONNA,
    SEZIMAL_PREFIX_YOSSE:  DECIMAL_PREFIX_YOTTA,
    SEZIMAL_PREFIX_ZESSE:  DECIMAL_PREFIX_ZETTA,
    SEZIMAL_PREFIX_EXASSE: DECIMAL_PREFIX_EXA,
    SEZIMAL_PREFIX_PESSE:  DECIMAL_PREFIX_PETA,
    SEZIMAL_PREFIX_TESSE:  DECIMAL_PREFIX_TERA,
    SEZIMAL_PREFIX_GISSE:  DECIMAL_PREFIX_GIGA,
    SEZIMAL_PREFIX_MESSE:  DECIMAL_PREFIX_MEGA,
    SEZIMAL_PREFIX_ZILO:   DECIMAL_PREFIX_KILO,
    SEZIMAL_PREFIX_SEZO:   DECIMAL_PREFIX_HECTO,
    SEZIMAL_PREFIX_ZENO:   DECIMAL_PREFIX_DECA,
    SEZIMAL_PREFIX_SESSO:  DECIMAL_PREFIX_DECA,

    SEZIMAL_PREFIX_BASE:   DECIMAL_PREFIX_BASE,

    SEZIMAL_PREFIX_SESSI:  DECIMAL_PREFIX_DECI,
    SEZIMAL_PREFIX_ZENI:   DECIMAL_PREFIX_DECI,
    SEZIMAL_PREFIX_SEZI:   DECIMAL_PREFIX_CENTI,
    SEZIMAL_PREFIX_ZILI:   DECIMAL_PREFIX_MILLI,
    SEZIMAL_PREFIX_MESSI:  DECIMAL_PREFIX_MICRO,
    SEZIMAL_PREFIX_GISSI:  DECIMAL_PREFIX_NANO,
    SEZIMAL_PREFIX_TESSI:  DECIMAL_PREFIX_PICO,
    SEZIMAL_PREFIX_PESSI:  DECIMAL_PREFIX_FEMTO,
    SEZIMAL_PREFIX_EXASSI: DECIMAL_PREFIX_ATTO,
    SEZIMAL_PREFIX_ZESSI:  DECIMAL_PREFIX_ZEPTO,
    SEZIMAL_PREFIX_YOSSI:  DECIMAL_PREFIX_YOCTO,
    SEZIMAL_PREFIX_ROSSI:  DECIMAL_PREFIX_RONTO,
    SEZIMAL_PREFIX_QUESSI: DECIMAL_PREFIX_QUECTO,
}

DECIMAL_PREFIX_TO_SEZIMAL = {
    DECIMAL_PREFIX_QUETTA: SEZIMAL_PREFIX_QUESSE,
    DECIMAL_PREFIX_RONNA:  SEZIMAL_PREFIX_ROSSE,
    DECIMAL_PREFIX_YOTTA:  SEZIMAL_PREFIX_YOSSE,
    DECIMAL_PREFIX_ZETTA:  SEZIMAL_PREFIX_ZESSE,
    DECIMAL_PREFIX_EXA:    SEZIMAL_PREFIX_EXASSE,
    DECIMAL_PREFIX_PETA:   SEZIMAL_PREFIX_PESSE,
    DECIMAL_PREFIX_TERA:   SEZIMAL_PREFIX_TESSE,
    DECIMAL_PREFIX_GIGA:   SEZIMAL_PREFIX_GISSE,
    DECIMAL_PREFIX_MEGA:   SEZIMAL_PREFIX_MESSE,
    DECIMAL_PREFIX_KILO:   SEZIMAL_PREFIX_ZILO,
    DECIMAL_PREFIX_HECTO:  SEZIMAL_PREFIX_SEZO,
    DECIMAL_PREFIX_DECA:   SEZIMAL_PREFIX_ZENO,

    DECIMAL_PREFIX_BASE:   SEZIMAL_PREFIX_ZENO,

    DECIMAL_PREFIX_DECI:   SEZIMAL_PREFIX_ZENI,
    DECIMAL_PREFIX_CENTI:  SEZIMAL_PREFIX_SEZI,
    DECIMAL_PREFIX_MILLI:  SEZIMAL_PREFIX_ZILI,
    DECIMAL_PREFIX_MICRO:  SEZIMAL_PREFIX_MESSI,
    DECIMAL_PREFIX_NANO:   SEZIMAL_PREFIX_GISSI,
    DECIMAL_PREFIX_PICO:   SEZIMAL_PREFIX_TESSI,
    DECIMAL_PREFIX_FEMTO:  SEZIMAL_PREFIX_PESSI,
    DECIMAL_PREFIX_ATTO:   SEZIMAL_PREFIX_EXASSI,
    DECIMAL_PREFIX_ZEPTO:  SEZIMAL_PREFIX_ZESSI,
    DECIMAL_PREFIX_YOCTO:  SEZIMAL_PREFIX_YOSSI,
    DECIMAL_PREFIX_RONTO:  SEZIMAL_PREFIX_ROSSI,
    DECIMAL_PREFIX_QUECTO: SEZIMAL_PREFIX_QUESSI,
}


def sezimal_exponent_to_decimal(exponent: int) -> int:
    exponent_6 = Decimal(6) ** Decimal(exponent)

    if exponent >= 0:
        start = 0
        finish = exponent
        step = 1
    else:
        start = -1
        finish = exponent
        step = -1

    for i in range(start, finish, step):
        exponent_10 = Decimal(10) ** Decimal(i)

        if exponent >= 0:
            if exponent_10 >= exponent_6:
                return i

        else:
            if exponent_10 <= exponent_6:
                return i + 1

    return 0


def decimal_exponent_to_sezimal(exponent: int) -> int:
    exponent_10 = Decimal(10) ** Decimal(exponent)

    if exponent >= 0:
        start = 0
        finish = exponent * 3
        step = 1
    else:
        start = -1
        finish = exponent * 3
        step = -1

    for i in range(start, finish, step):
        exponent_6 = Decimal(6) ** Decimal(i)

        if exponent >= 0:
            if exponent_6 >= exponent_10:
                return i

        else:
            if exponent_6 <= exponent_10:
                return i + 1

    return 0


def sezimal_prefix_exponent_to_decimal(exponent: int | Sezimal) -> Sezimal:
    exponent = Sezimal(exponent)

    if exponent < SEZIMAL_PREFIX_QUESSI.exponent:
        raise ValueError(f'Exponent {exponent} cannot be under -104 (quessi)')
    elif exponent > SEZIMAL_PREFIX_QUESSE.exponent:
        raise ValueError(f'Exponent {exponent} cannot be above 104 (quesse)')
    elif exponent == 0:
        raise ValueError('Exponent cannot be zero')

    if exponent not in SEZIMAL_PREFIX_TO_DECIMAL:
        if exponent > 0:
            exponent = exponent + (4 - (exponent % 4))
        else:
            exponent = exponent - (4 - (exponent % 4))

    return SEZIMAL_PREFIX_TO_DECIMAL[exponent]


def decimal_prefix_exponent_to_sezimal(exponent: int | Sezimal) -> Sezimal:
    exponent = Sezimal(exponent)

    if exponent < DECIMAL_PREFIX_QUECTO.exponent:
        raise ValueError(f'Exponent {exponent} cannot be under -50 (quecto)')
    elif exponent > DECIMAL_PREFIX_QUETTA.exponent:
        raise ValueError(f'Exponent {exponent} cannot be above 50 (quetta)')
    elif exponent == 0:
        raise ValueError('Exponent cannot be zero')

    if exponent not in DECIMAL_PREFIX_TO_SEZIMAL:
        if exponent > 0:
            exponent = exponent + (3 - (exponent % 3))
        else:
            exponent = exponent - (3 - (exponent % 3))

    return DECIMAL_PREFIX_TO_SEZIMAL[exponent]

#
# def decimal_exponent_to_sezimal(decimal_exponent: int | Sezimal, sezimal_exponent: int | Sezimal = None) -> Sezimal:
#     decimal_exponent = Sezimal(decimal_exponent)
#
#     if sezimal_exponent is None:
#         sezimal_exponent = decimal_exponent_to_sezimal(decimal_exponent)
#
#     conversion = decimal_exponent.multiplier / sezimal_exponent.multiplier
#
#     return conversion
