
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


global _SINE
global _COSINE
_SINE = {}
_COSINE = {}


def cos_radians(radians: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
    radians = Sezimal(radians)

    if radians < 0:
        while radians < 0:
            radians += TAU

    else:
        while radians >= TAU:
            radians -= TAU

    quadrant = Sezimal('1')

    if radians > TAU * 3 / 4:
        radians -= TAU * 3 / 4

    elif radians > PI:
        radians -= PI
        quadrant = Sezimal('-1')

    elif radians > TAU / 4:
        radians -= TAU / 4
        quadrant = Sezimal('-1')

    radians = round(Sezimal(radians), sezimal_context.sezimal_precision)

    if radians in _COSINE:
        result = _COSINE[radians]

        if result != 0:
            result *= quadrant

        return result

    print('calculo solto')

    sezimal_context.sezimal_precision_decimal += 4

    result = Sezimal(1)
    last_result = Sezimal(0)
    i = Sezimal(0)
    sign = Sezimal(1)
    num = Sezimal(1)

    while result != last_result:
        last_result = result
        i += 2
        sign *= -1
        num *= radians * radians
        den = i.factorial()
        result += sign * (num / den)

    sezimal_context.sezimal_precision_decimal -= 4

    return round(result, sezimal_context.sezimal_precision)


def cos_degree(degrees: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
    return cos_radians(degrees * PI / 500)


def cos_paridi(paridi: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction) -> Sezimal:
    return cos_radians(paridi * TAU)


SIN_0       = SezimalInteger('0')
SIN_0_013   = (SQRT_10 - SQRT_2) / 4
SIN_0_01__4 = (SQRT_5 - 1) / 4
SIN_0_0213  = (2 - SQRT_2).sqrt() / 2
SIN_0_030   = Sezimal('0.3')
SIN_0_0__3  = (14 - (2 * SQRT_5)).sqrt() / 4
SIN_0_043   = SQRT_2 / 2
SIN_0_05__2 = (SQRT_5 + 1) / 4
SIN_0_100   = SQRT_3 / 2
SIN_0_104_3 = (2 + SQRT_2).sqrt() / 2
SIN_0__1    = (14 + (2 * SQRT_5)).sqrt() / 4
SIN_0_113   = (SQRT_10 + SQRT_2) / 4
SIN_0_130   = SezimalInteger('1')
SIN_1   = SezimalInteger('0')


COS_0       = SezimalInteger('1')
COS_0_013   = (SQRT_10 + SQRT_2) / 4
COS_0_01__4 = (14 + (2 * SQRT_5)).sqrt() / 4
COS_0_0213  = (2 + SQRT_2).sqrt() / 2
COS_0_030   = SQRT_3 / 2
COS_0_0__3  = (SQRT_5 + 1) / 4
COS_0_043   = SQRT_2 / 2
COS_0_05__2 = (14 - (2 * SQRT_5)).sqrt() / 4
COS_0_100   = Sezimal('0.3')
COS_0_104_3 = (2 - SQRT_2).sqrt() / 2
COS_0__1    = (SQRT_5 - 1) / 4
COS_0_113   = (SQRT_10 - SQRT_2) / 4
COS_0_130   = SezimalInteger('0')
COS_1   = SezimalInteger('1')



def update_cosine():
    global _SINE

    _SINE = {
        # Sezimal(0): SezimalInteger('1'),
        # round(TAU, sezimal_context.sezimal_precision): SezimalInteger('1'),
        # TAU / 40: (SQRT_10 + SQRT_2) / 4,
        # TAU / 32: (10 + (2 * SQRT_5)).sqrt() / 4,
        # TAU / 24: (2 + SQRT_2).sqrt() / 2,
        # TAU / 20: SQRT_3 / 2,
        # TAU / 14: (SQRT_5 + 1) / 4,
        # TAU / 12: SQRT_2 / 2,
        # TAU * 3 / 32: (14 - (2 * SQRT_5)).sqrt() / 4,
        # TAU / 10: Sezimal('0.3'),
        # TAU * 3 / 24: (2 - SQRT_2).sqrt() / 2,
        # TAU / 5: (SQRT_5 - 1) / 4,
        # TAU * 5 / 40: (SQRT_10 - SQRT_2) / 4,
        # TAU / 4: SezimalInteger('0'),

        Sezimal(0)    : SIN_0,
        Sezimal(23)   : SIN_0_013,
        Sezimal(30)   : SIN_0_01__4,
        Sezimal(34.3) : SIN_0_0213,
        Sezimal(50)   : SIN_0_030,
        Sezimal(100)  : SIN_0_0__3,
        Sezimal(113)  : SIN_0_043,
        Sezimal(130)  : SIN_0_05__2,
        Sezimal(140)  : SIN_0_100,
        Sezimal(151.3): SIN_0_104_3,
        Sezimal(200)  : SIN_0__1,
        Sezimal(203)  : SIN_0_113,
        Sezimal(230)  : SIN_0_130,
        Sezimal(1400) : SIN_1,
    }

    global _COSINE

    _COSINE = {
        # Sezimal(0): SezimalInteger('1'),
        # round(TAU, sezimal_context.sezimal_precision): SezimalInteger('1'),
        # TAU / 40: (SQRT_10 + SQRT_2) / 4,
        # TAU / 32: (10 + (2 * SQRT_5)).sqrt() / 4,
        # TAU / 24: (2 + SQRT_2).sqrt() / 2,
        # TAU / 20: SQRT_3 / 2,
        # TAU / 14: (SQRT_5 + 1) / 4,
        # TAU / 12: SQRT_2 / 2,
        # TAU * 3 / 32: (14 - (2 * SQRT_5)).sqrt() / 4,
        # TAU / 10: Sezimal('0.3'),
        # TAU * 3 / 24: (2 - SQRT_2).sqrt() / 2,
        # TAU / 5: (SQRT_5 - 1) / 4,
        # TAU * 5 / 40: (SQRT_10 - SQRT_2) / 4,
        # TAU / 4: SezimalInteger('0'),

        Sezimal(0)    : COS_0,
        Sezimal(23)   : COS_0_013,
        Sezimal(30)   : COS_0_01__4,
        Sezimal(34.3) : COS_0_0213,
        Sezimal(50)   : COS_0_030,
        Sezimal(100)  : COS_0_0__3,
        Sezimal(113)  : COS_0_043,
        Sezimal(130)  : COS_0_05__2,
        Sezimal(140)  : COS_0_100,
        Sezimal(151.3): COS_0_104_3,
        Sezimal(200)  : COS_0__1,
        Sezimal(203)  : COS_0_113,
        Sezimal(230)  : COS_0_130,
        Sezimal(1400) : COS_1,
    }

update_cosine()
