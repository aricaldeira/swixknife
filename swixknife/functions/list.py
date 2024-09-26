
from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger


class SezimalList(list):
    def __getitem__(self, key):
        if type(key) == slice:
            start = key.start
            stop = key.stop
            step = key.step

            if start is not None:
                start = SezimalInteger(str(start))
                start = int(start)

            if stop is not None:
                stop = SezimalInteger(str(stop))
                stop = int(stop)

            if step is not None:
                step = SezimalInteger(str(step))
                step = int(step)

            if start is None and step is None:
                key = slice(stop)
            else:
                key = slice(start, stop, step)

        elif type(key) == int:
            key = SezimalInteger(str(key))
            key = int(key)
        elif type(key) == Decimal:
            key = SezimalInteger(key)
            key = int(key)

        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if type(key) == slice:
            start = key.start
            stop = key.stop
            step = key.step

            if start is not None:
                start = SezimalInteger(str(start))
                start = int(start)

            if stop is not None:
                stop = SezimalInteger(str(stop))
                stop = int(stop)

            if step is not None:
                step = SezimalInteger(str(step))
                step = int(step)

            if start is None and step is None:
                key = slice(stop)
            else:
                key = slice(start, stop, step)

        elif type(key) == int:
            key = SezimalInteger(str(key))
            key = int(key)
        elif type(key) == float:
            key = Sezimal(str(key))
            key = int(key)
        elif type(key) == Decimal:
            if key.quantize(Decimal('1')) == key:
                key = SezimalInteger(key)
            else:
                key = Sezimal(key)
            key = int(key)

        return super().__setitem__(key, value)


class SezimalTuple(tuple):
    def __getitem__(self, key):
        if type(key) == slice:
            start = key.start
            stop = key.stop
            step = key.step

            if start is not None:
                start = SezimalInteger(str(start))
                start = int(start)

            if stop is not None:
                stop = SezimalInteger(str(stop))
                stop = int(stop)

            if step is not None:
                step = SezimalInteger(str(step))
                step = int(step)

            if start is None and step is None:
                key = slice(stop)
            else:
                key = slice(start, stop, step)

        elif type(key) == int:
            key = SezimalInteger(str(key))
            key = int(key)
        elif type(key) == Decimal:
            key = SezimalInteger(key)
            key = int(key)

        return super().__getitem__(key)
