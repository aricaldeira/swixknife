

__all__ = [
    'LENGTH',
    'LENGTH_SYMBOL',
    'LENGTH_NAME',
]


from .base import BaseUnit, SezimalUnit, DecimalUnit
from ..prefixes import *


METRE = BaseUnit(None, 'm', 'metre', SEZIMAL_PREFIX_BASE, classification='length')

LENGTH = [METRE]

LENGTH_SYMBOL = {
    METRE.symbol: METRE,
}

LENGTH_NAME = {
    METRE.name: METRE,
}


for prefix in SEZIMAL_PREFIXES:
    constant = prefix.name.upper() + 'METRE'
    constant_symbol = prefix.symbol + 'm'
    constant_name = prefix.name + 'metre'
    unit = SezimalUnit(METRE, constant_symbol, constant_name, prefix, classification='length')

    LENGTH_SYMBOL[unit.symbol] = unit
    LENGTH_NAME[unit.name] = unit
    LENGTH.append(unit)


for prefix in DECIMAL_PREFIXES:
    constant = prefix.name.upper() + 'METRE'
    constant_symbol = prefix.symbol + 'm'
    constant_name = prefix.name + 'metre'
    unit = DecimalUnit(METRE, constant_symbol, constant_name, prefix, classification='length')

    LENGTH_SYMBOL[unit.symbol] = unit
    LENGTH_NAME[unit.name] = unit
    LENGTH.append(unit)
