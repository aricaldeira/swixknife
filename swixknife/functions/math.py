
import math
from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction


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
