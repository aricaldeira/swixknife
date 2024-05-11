
from typing import TypeVar

Self = TypeVar('Self', bound='SezimalUnit')


from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..dozenal import Dozenal, DozenalInteger, DozenalFraction
from ..exponents import sezimal_exponent_to_symbol, sezimal_exponent_to_prefix, \
    decimal_exponent_to_symbol, decimal_exponent_to_sezimal_factor

from ..functions import SezimalRange
from decimal import Decimal
from fractions import Fraction as DecimalFraction


class SezimalUnit(object):
    __slots__ = ('_value', '_symbol', '_name', '_base_unit')

    @classmethod
    def __normalize_value(cls, value: str | int | float | Decimal | DecimalFraction | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> Sezimal | SezimalInteger | SezimalFraction:
        if type(value) in (str, int, float):
            value = Sezimal(str(value))
        elif type(value) in (Decimal, Dozenal, DozenalInteger):
            value = Sezimal(value)

        return value

    def __new__(cls, value: str | int | float | Decimal | DecimalFraction | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction = 1, symbol: str = '', name: str = '', base_unit : Self = None) -> Self:
        self = object.__new__(cls)
        self._value = cls.__normalize_value(value)
        self._symbol = symbol
        self._name = name
        self._base_unit = base_unit

        return self

    def __repr__(self) -> str:
        return self._value.formatted_number + ' ' + self._symbol

    @property
    def value(self) -> Sezimal | SezimalInteger | SezimalFraction:
        return self._value

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def name(self) -> str:
        return self._name

    @property
    def base_unit(self) -> Self:
        return self._base_unit

    def __mul__(self, other_value: str | int | float | Decimal | DecimalFraction | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction | Self) -> Self:
        if type(other_value) not in (SezimalUnit, DecimalUnit):
            other_value = self.__normalize_value(other_value)

            base_unit = self.base_unit

            if base_unit:
                base_unit *= other_value

            return self.__class__(value=self.value * other_value, symbol=self.symbol, name=self.name, base_unit=base_unit)

        if self.base_unit.symbol.startswith(other_value.base_unit.symbol):
            value = self.base_unit.value * other_value.base_unit.value

            if self.base_unit.symbol == other_value.base_unit.symbol:
                exponent = '2'
            else:
                exponent = self.base_unit.symbol[-1]

                if not exponent.isdigit():
                    exponent = other_value.base_unit.symbol[-1]

                exponent = SI(exponent) + 1

            if self.base_unit.symbol + exponent in globals():
                square_unit = globals()[self.base_unit.symbol + exponent]
                symbol = square_unit.symbol
                name = square_unit.name
            else:
                symbol = self.base_unit.symbol + exponent
                name = self.base_unit.name + exponent

        else:
            value = self.value * other_value.value
            symbol = self.symbol + '·' + other_value.symbol
            name = self.name + ' ' + other_value.name

        return self.__class__(value, symbol, name)

    def __rmul__(self, other_value: str | int | float | Decimal | DecimalFraction | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_value) not in (SezimalUnit, DecimalUnit):
            other_value = self.__normalize_value(other_value)

            base_unit = self.base_unit

            if base_unit:
                base_unit *= other_value

            return self.__class__(value=self.value * other_value, symbol=self.symbol, name=self.name, base_unit=base_unit)

        if self.base_unit.symbol == other_value.base_unit.symbol:
            value = self.base_unit.value * other_value.base_unit.value
            symbol = self.base_unit.symbol + '²'
            name = 'square ' + self.base_unit.name

        else:
            value = self.value * other_value.value
            symbol = self.symbol + '·' + other_value.symbol
            name = self.name + ' ' + other_value.name

        return self.__class__(value, symbol, name)


class DecimalUnit(SezimalUnit):
    @classmethod
    def __normalize_value(cls, value: str | int | float | Decimal | DecimalFraction | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> Sezimal | SezimalInteger | SezimalFraction:
        if type(value) in (str, int, float):
            value = Decimal(str(value))
        elif type(value) != Decimal:
            value = value.decimal

        return value

    def __repr__(self) -> str:
        return self._value.decimal_formatted_number + ' ' + self._symbol



pad = pada = SezimalUnit(symbol='pad', name='pada')
m = meter = metre = DecimalUnit(symbol='m', name='metre', base_unit=Sezimal('102..304_003_214_232_052_043_015_225_105_000_231_145...') * pad)

kex = keshe = pad2 = pada2 = square_pada = SezimalUnit(symbol='kex', name='kexe')
m2 = meter2 = metre2 = square_meter = square_metre = DecimalUnit(symbol='m²', name='square metre', base_unit=Sezimal('10_511.403_140_301_542_144_503_035_401_055_345_101_343_231_523_435_004') * kex)


def full_prefixes(unit):
    for i in SezimalRange(1, 111):
        symbol = sezimal_exponent_to_symbol(i) + unit.symbol
        name = sezimal_exponent_to_prefix(i) + unit.name
        value = SezimalInteger(10) ** i

        new_unit = SezimalUnit(symbol=symbol, name=name, base_unit=unit * value)

        globals()[symbol] = new_unit
        globals()[name] = new_unit

        symbol = sezimal_exponent_to_symbol(i * -1) + unit.symbol
        name = sezimal_exponent_to_prefix(i * -1) + unit.name
        value = SezimalInteger(10) ** (i * -1)

        new_unit = SezimalUnit(symbol=symbol, name=name, base_unit=unit * value)

        globals()[symbol] = new_unit
        globals()[name] = new_unit


full_prefixes(pad)
