
__all__ = (
    'sin', 'arcsin', 'asin', 'csc', 'arccsc', 'acsc',
    'cos', 'arccos', 'acos', 'sec', 'arcsec', 'asec',
    'tan', 'arctan', 'atan', 'cot', 'arccot', 'acot',
    'sinh', 'arcsinh', 'asinh', 'csch', 'arccsch', 'acsch',
    'cosh', 'arccosh', 'acosh', 'sech', 'arcsech', 'asech',
    'tanh', 'arctanh', 'atanh', 'coth', 'arccoth', 'acoth',
)

from typing import TypeVar

Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')
SympyRational = TypeVar('SympyRational', bound='Rational')


try:
    import sympy
except:
    sympy = None
    import math

from decimal import Decimal

from ..base import decimal_to_sezimal
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..constants import *
from ..base import sezimal_context
from ..units import sezimal_to_sezimal_unit, decimal_to_sezimal_unit


def _angle_to_mandala_fraction(angle, unit: str = 'mdl') -> SezimalFraction | SympyRational:
    if not unit:
        unit = 'mdl'

    if unit.endswith('mdl'):
        angle = sezimal_to_sezimal_unit(angle, unit, 'mdl', return_fraction=True)
    else:
        angle = decimal_to_sezimal_unit(angle, unit, 'mdl', return_fraction=True)

    if sympy:
        num = sympy.Integer(str(angle.numerator.decimal))
        den = sympy.Integer(str(angle.denominator.decimal))
        return sympy.Rational(num, den)

    return angle


def _sympy_to_sezimal(result) -> Sezimal:
    res = str(result.evalf(n=sezimal_context.decimal_precision + 4))
    return Sezimal(decimal_to_sezimal(res, sezimal_precision=sezimal_context.sezimal_precision))


def _float_to_sezimal(result: float) -> Sezimal:
    return round(
        Sezimal(Decimal(str(result)), _internal=True),
        sezimal_context.sezimal_precision,
    )


def sin(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.sin(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.sin(angle.decimal))

    return result


def arcsin(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.asin(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arcsin(angle.decimal))

    return result


asin = arcsin


def csc(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.csc(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.csc(angle.decimal))

    return result


def arccsc(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.acsc(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arccsc(angle.decimal))

    return result


acsc = arccsc


def cos(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.cos(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.cos(angle.decimal))

    return result


def arccos(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.acos(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arccos(angle.decimal))

    return result


acos = arccos


def sec(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.sec(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.sec(angle.decimal))

    return result


def arcsec(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.asec(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arcsec(angle.decimal))

    return result


asec = arcsec


def tan(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.tan(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.tan(angle.decimal))

    return result


def arctan(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.atan(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arctan(angle.decimal))

    return result


atan = arctan


def cot(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.cot(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.cot(angle.decimal))

    return result


def arccot(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.acot(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arccot(angle.decimal))

    return result


acot = arccot


def sinh(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.sinh(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.sinh(angle.decimal))

    return result


def arcsinh(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.asinh(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arcsinh(angle.decimal))

    return result


asinh = arcsinh


def csch(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.csch(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.csch(angle.decimal))

    return result


def arccsch(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.acsch(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arccsch(angle.decimal))

    return result


acsch = arccsch


def cosh(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.cosh(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.cosh(angle.decimal))

    return result


def arccosh(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.acosh(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arccosh(angle.decimal))

    return result


acosh = arccosh


def sech(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.sech(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.sech(angle.decimal))

    return result


def arcsech(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.asech(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arcsech(angle.decimal))

    return result


asech = arcsech


def tanh(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.tanh(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.tanh(angle.decimal))

    return result


def arctanh(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.atanh(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arctanh(angle.decimal))

    return result


atanh = arctanh


def coth(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.coth(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.coth(angle.decimal))

    return result


def arccoth(
    angle: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | Dozenal | DozenalInteger | DozenalFraction,
    unit: str = 'mdl',
) -> Sezimal:
    angle = _angle_to_mandala_fraction(angle, unit)

    if sympy:
        result = _sympy_to_sezimal(sympy.acoth(angle * (sympy.pi * 2)))
    else:
        result = _sympy_to_sezimal(math.arccoth(angle.decimal))

    return result


acoth = arccoth
