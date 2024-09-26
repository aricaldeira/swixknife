
from collections import OrderedDict
from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger


class SezimalDictionary(OrderedDict):
    def __getitem__(self, key):
        if type(key) == int:
            key = SezimalInteger(str(key))
        elif type(key) == float:
            key = Sezimal(str(key))
        elif type(key) == Decimal:
            if key.quantize(Decimal('1')) == key:
                key = SezimalInteger(key)
            else:
                key = Sezimal(key)

        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if type(key) == int:
            key = SezimalInteger(str(key))
        elif type(key) == float:
            key = Sezimal(str(key))
        elif type(key) == Decimal:
            if key.quantize(Decimal('1')) == key:
                key = SezimalInteger(key)
            else:
                key = Sezimal(key)

        return super().__setitem__(key, value)

    def __getattr__(self, key):
        if key not in self:
            return ''

        attr = self[key]

        if isinstance(attr, dict) \
            or isinstance(collections.OrderedDict):
            d = SezimalDictionary()
            d.update(attr)
            self[key] = d
            attr = d

        return attr

    def __setattr__(self, key, value):
        self[key] = value
