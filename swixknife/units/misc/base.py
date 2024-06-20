

__all__ = [
    'BaseUnit',
    'SezimalUnit',
    'DecimalUnit',
]

from typing import TypeVar

BaseUnitClass = TypeVar('BaseUnitClass', bound='BaseUnit')
SezimalUnitClass = TypeVar('SezimalUnitClass', bound='SezimalUnit')
DecimalUnitClass = TypeVar('DecimalUnitClass', bound='DecimalUnit')

from ..sezimal import Sezimal
from ..prefixes import SezimalPrefix, DecimalPrefix


class BaseUnit:
    def __init__(self, base_unit: None | BaseUnitClass, symbol: str, name: str, prefix: SezimalPrefix | DecimalPrefix, classification: str) -> BaseUnitClass:
        self.base_unit = base_unit
        self.symbol = symbol
        self.name = name
        self.prefix = prefix
        self.classification = classification

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Unit(name='{self.name}')"

    @property
    def multiplier(self) -> Sezimal:
        if not self.prefix:
            return Sezimal(0)

        return self.prefix.multiplier


class SezimalUnit(BaseUnit):
    def __init__(self, base_unit: None | BaseUnitClass | SezimalUnitClass, symbol: str, name: str, prefix: SezimalPrefix, classification: str) -> SezimalUnitClass:
        return super().__init__(base_unit, symbol, name, prefix, classification)

    def __repr__(self):
        return f"SezimalUnit(name='{self.name}')"


class DecimalUnit(BaseUnit):
    def __init__(self, base_unit: None | BaseUnitClass | DecimalUnitClass, symbol: str, name: str, prefix: DecimalPrefix, classification: str) -> DecimalUnitClass:
        return super().__init__(base_unit, symbol, name, prefix, classification)

    def __repr__(self):
        return f"DecimalUnit(name='{self.name}')"
