
import math
from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..constants import *
from ..base import sezimal_context


def floor(number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> SezimalInteger:
    number = Sezimal(number)
    res = math.floor(number)
    res = SezimalInteger(Decimal(str(res)))
    return res


def ceil(number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> SezimalInteger:
    number = Sezimal(number)
    res = math.ceil(number)
    res = SezimalInteger(Decimal(str(res)))
    return res


def gcd(
    number_1: str | int | float | Decimal | Sezimal | SezimalInteger,
    number_2: str | int | float | Decimal | Sezimal | SezimalInteger,
) -> SezimalInteger:
    using_ultra_precision = sezimal_context.using_ultra_precision
    precision = sezimal_context.precision

    if not using_ultra_precision:
        sezimal_context.use_ultra_precision()

    number_1 = Sezimal(number_1)
    number_2 = Sezimal(number_2)
    gcd = SezimalInteger(1)

    while True:
        x = number_1.decimal
        y = number_2.decimal

        while y:
            x, y = y, x % y

        x = abs(x)
        gcd *= x

        if x == 1 or x == 0:
            break

        number_1 = SezimalInteger(number_1.decimal / x)
        number_2 = SezimalInteger(number_2.decimal / x)

    if not using_ultra_precision:
        sezimal_context.back_to_regular_precision()

    return gcd
