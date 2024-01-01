

from ..sezimal import SezimalInteger
from ..dozenal import DozenalInteger


class SezimalRange:
    def __init__(self, start: int | SezimalInteger, stop: int | SezimalInteger = None, step: int | SezimalInteger = None):
        if stop is None:
            stop = start
            start = SezimalInteger(0)

        if step is None:
            step = SezimalInteger(1)

        if step == 0:
            raise ValueError('Cannot create a range with step 0')

        self.start = SezimalInteger(start)
        self.stop = SezimalInteger(stop)
        self.step = SezimalInteger(step)

    def __repr__(self):
        return f'SezimalRange({self.start}, {self.stop}, {self.step})'

    def __iter__(self):
        if self.start == self.stop:
            return []

        if self.step > 0:
            if self.start > self.stop:
                return []

            x = SezimalInteger(str(self.start))

            while x < self.stop:
                yield SezimalInteger(x)
                x += self.step

        else:
            if self.start < self.stop:
                return []

            x = SezimalInteger(str(self.start))

            while x > self.stop:
                yield SezimalInteger(x)
                x += self.step


class DozenalRange:
    def __init__(self, start: int | DozenalInteger, stop: int | DozenalInteger = None, step: int | DozenalInteger = None):
        if stop is None:
            stop = start
            start = DozenalInteger(0)

        if step is None:
            step = DozenalInteger(1)

        if step == 0:
            raise ValueError('Cannot create a range with step 0')

        self.start = DozenalInteger(start)
        self.stop = DozenalInteger(stop)
        self.step = DozenalInteger(step)

    def __repr__(self):
        return f'DozenalRange({self.start}, {self.stop}, {self.step})'

    def __iter__(self):
        if self.start == self.stop:
            return []

        if self.step > 0:
            if self.start > self.stop:
                return []

            x = DozenalInteger(str(self.start))

            while x < self.stop:
                yield DozenalInteger(x)
                x += self.step

        else:
            if self.start < self.stop:
                return []

            x = DozenalInteger(str(self.start))

            while x > self.stop:
                yield DozenalInteger(x)
                x += self.step
