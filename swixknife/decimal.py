

__all__ = ('Decimal', 'DecimalFraction')

from typing import TypeVar
import numbers as _numbers

Self = TypeVar('Self', bound='Decimal')
IntegerSelf = TypeVar('IntegerSelf', bound='DecimalInteger')
FractionSelf = TypeVar('FractionSelf', bound='DecimalFraction')

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')

Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

from decimal import Decimal as _Decimal

from .base import validate_clean_decimal


class Decimal(_Decimal):
    def __new__(cls, value='0', **kwargs):
        value = validate_clean_decimal(value)
        return super(Decimal, cls).__new__(cls, value, **kwargs)


class DecimalFraction(Decimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', '_numerator', '_denominator', '_decimal']

    def __init__(self, numerator: str | int | float | Decimal | FractionSelf | FractionSelf | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction, denominator: str | int | float | Decimal | FractionSelf | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction = None) -> Sezimal:
        if type(numerator) == str:
            if '/' in numerator:
                numerator, denominator = numerator.split('/')
            elif '⁄' in numerator:
                numerator, denominator = numerator.split('⁄')
            elif '÷' in numerator:
                numerator, denominator = numerator.split('÷')

        cleaned_numerator = validate_clean_decimal(numerator)
        cleaned_denominator = validate_clean_decimal(denominator)

        self._numerator = Decimal(cleaned_numerator)
        self._denominator = Decimal(cleaned_denominator)
        self._decimal = self._numerator / self._denominator

        super().__init__(self._decimal)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @property
    def decimal(self):
        return self._decimal

    @property
    def reciprocal(self) -> FractionSelf:
        return DecimalFraction(self._denominator, self._numerator)

    @reciprocal.setter
    def reciprocal(self, value):
        pass

    def __str__(self) -> str:
        if self._sign == -1:
            res = '-'
        else:
            res = ''

        res += str(self._numerator)
        res += ' / '
        res += str(self._denominator)

        return res

    def __repr__(self) -> str:
        return f"DecimalFraction('{self._numerator.formatted_number} / {self._denominator.formatted_number}') == {self._decimal.__repr__()}"

    def as_integer_ratio(self) -> tuple[int, int]:
        return int(self._numerator), int(self._denominator)

    def __mul__(self, other_number: str | int | float | Decimal | FractionSelf | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Decimal:
        if type(other_number) == DecimalFraction:
            numerator = self.numerator * other_number.numerator
            denominator = self.denominator * other_number.denominator
            return DecimalFraction(numerator, denominator)

        if type(other_number) != Decimal:
            other_number = Decimal(other_number)

        if other_number == int(other_number):
            numerator = self.numerator * other_number
            denominator = self.denominator
            return DecimalFraction(numerator, denominator)

        return super().__mul__(other_number)

    def __rmul__(self, other_number: str | int | float | Decimal | FractionSelf | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Decimal:
        if type(other_number) == DecimalFraction:
            numerator = self.numerator * other_number.numerator
            denominator = self.denominator * other_number.denominator
            return DecimalFraction(numerator, denominator)

        if type(other_number) != Decimal:
            other_number = Decimal(other_number)

        if other_number == int(other_number):
            numerator = self.numerator * other_number
            denominator = self.denominator
            return DecimalFraction(numerator, denominator)

        return super().__rmul__(other_number)

    def __truediv__(self, other_number: str | int | float | Decimal | FractionSelf | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Decimal:
        if type(other_number) == DecimalFraction:
            numerator = self.numerator * other_number.denominator
            denominator = self.denominator * other_number.numerator
            return DecimalFraction(numerator, denominator)

        if type(other_number) != Decimal:
            other_number = Decimal(other_number)

        if other_number == int(other_number):
            numerator = self.numerator
            denominator = self.denominator * other_number
            return DecimalFraction(numerator, denominator)

        return super().__truediv__(other_number)

    def __rtruediv__(self, other_number: str | int | float | Decimal | FractionSelf | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Decimal:
        if type(other_number) == DecimalFraction:
            numerator = self.numerator * other_number.denominator
            denominator = self.denominator * other_number.numerator
            return DecimalFraction(numerator, denominator)

        if type(other_number) != Decimal:
            other_number = Decimal(other_number)

        if other_number == int(other_number):
            numerator = self.numerator
            denominator = self.denominator * other_number
            return DecimalFraction(denominator, numerator)

        return super().__rtruediv__(other_number)

    def __pow__(self, other_number: str | int | float | Decimal | FractionSelf | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Decimal:
        if type(other_number) != Decimal:
            other_number = Decimal(other_number)

        if other_number == int(other_number):
            numerator = self.numerator ** other_number
            denominator = self.denominator ** other_number
            return DecimalFraction(numerator, denominator)

        return super().__pow__(other_number)


_numbers.Number.register(Decimal)
_numbers.Integral.register(Decimal)
_numbers.Rational.register(Decimal)

# _numbers.Number.register(DecimalInteger)
# _numbers.Integral.register(DecimalInteger)

_numbers.Number.register(DecimalFraction)
_numbers.Integral.register(DecimalFraction)
