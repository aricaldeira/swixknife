
__all__ = ('json',)


from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from .._decimal import Decimal, DecimalFraction
from ..dozenal import Dozenal, DozenalInteger, DozenalFraction
from ..date_time import SezimalDate, SezimalTime, SezimalDateTime


import json

_CLASSES = (
    Sezimal, SezimalInteger, SezimalFraction,
    Decimal, DecimalFraction,
    Dozenal, DozenalInteger, DozenalFraction,
    SezimalDate, SezimalTime, SezimalDateTime,
)


def json_sezimal_default(value):
    for _class in _CLASSES:
        if isinstance(value, _class):
            return str(value)

    return value

json._default_encoder.default = json_sezimal_default
