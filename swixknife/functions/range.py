

from ..sezimal import SezimalInteger


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
