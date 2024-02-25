

from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

Decimal = TypeVar('Decimal', bound='Decimal')

# from .validation import validate_clean_sezimal, validate_clean_decimal, validate_clean_dozenal


class SezimalContext:
    def __init__(self):
        # self.sezimal_precision = 30
        self.sezimal_precision = 33
        # self.sezimal_precision = 1200

    @property
    def sezimal_precision(self) -> SezimalInteger:
        return self._sezimal_precision

    @sezimal_precision.setter
    def sezimal_precision(self, precision: int | float | str | Decimal | Sezimal | SezimalInteger):
        # precision = validate_clean_sezimal(precision)
        precision = str(precision)

        if '.' in precision:
            integer, fraction = precision.split('.')
            precision = integer

        self._sezimal_precision = int(precision)
        self._sezimal_precision_decimal = int(precision, 6)
        self._decimal_precision = int(int(precision, 6) / 4 * 3)
        # self._decimal_precision = self._sezimal_precision_decimal // 4 * 3

        p = int(self._decimal_precision)
        sp = ''

        while p:
            sp += str(p % 12)
            p //= 12

        sp = sp[::-1]

        self._dozenal_precision = sp
        self._dozenal_precision_decimal = self._decimal_precision

    @property
    def sezimal_precision_decimal(self) -> int:
        return self._sezimal_precision_decimal

    @sezimal_precision_decimal.setter
    def sezimal_precision_decimal(self, precision: int | float | str | Decimal):
        # precision = validate_clean_decimal(precision)
        precision = str(precision)

        if '.' in precision:
            integer, fraction = precision.split('.')
            precision = integer

        self._sezimal_precision_decimal = int(precision)

        p = int(precision)
        sp = ''

        while p:
            sp += str(p % 6)
            p //= 6

        sp = sp[::-1]

        self._sezimal_precision = int(sp)

    @property
    def decimal_precision(self) -> int:
        return self._decimal_precision

    @decimal_precision.setter
    def decimal_precision(self, precision: int | float | str | Decimal):
        # precision = validate_clean_decimal(precision)
        precision = str(precision)

        if '.' in precision:
            integer, fraction = precision.split('.')
            precision = integer

        self._decimal_precision = int(precision)

    @property
    def dozenal_precision(self) -> DozenalInteger:
        return self._dozenal_precision

    @dozenal_precision.setter
    def dozenal_precision(self, precision: int | float | str | Decimal | Dozenal | DozenalInteger):
        # precision = validate_clean_dozenal(precision)
        precision = str(precision)

        if '.' in precision:
            integer, fraction = precision.split('.')
            precision = integer

        self._dozenal_precision = int(precision)
        self._dozenal_precision_decimal = int(precision, 12)

    @property
    def dozenal_precision_decimal(self):
        return self._dozenal_precision_decimal


sezimal_context = SezimalContext()
