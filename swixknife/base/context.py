

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
        self.sezimal_precision = 33
        self._locale = None
        self.show_recurring_digits = True
        self.fractions_use_decimal = False
        self.fractions_simplify = True
        self.fractions_precision = None
        self.minimum_size = 0
        self.sezimal_digits = False

    @property
    def precision(self) -> SezimalInteger:
        return self._sezimal_precision

    @precision.setter
    def precision(self, precision: int | float | str | Decimal | Sezimal | SezimalInteger):
        self.sezimal_precision = precision

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

        self._niftimal_precision_decimal = self._sezimal_precision_decimal // 2
        self._niftimal_precision = ''

        p = self._niftimal_precision_decimal
        n = 0

        while p >= 36:
            p -= 36
            n += 1

        if n:
            self._niftimal_precision = '0123456789ABCDEFGHIJKMLMNOPQRSTUVWXYZ'[n]

        self._niftimal_precision += '0123456789ABCDEFGHIJKMLMNOPQRSTUVWXYZ'[p]

        if self._sezimal_precision_decimal <= 48:
            decimal_precision = 0

            while (6 ** (self._sezimal_precision_decimal * -1)) * (10 ** decimal_precision) < 1:
                decimal_precision += 1
        else:
            decimal_precision = int(self._sezimal_precision_decimal / 4 * 3)
            if decimal_precision % 3 != 0:
                decimal_precision -= decimal_precision % 3

        self.decimal_precision = decimal_precision

        p = self.decimal_precision
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

        from decimal import getcontext
        getcontext().prec = int(precision) + 1

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
    def dozenal_precision_decimal(self) -> int:
        return self._dozenal_precision_decimal

    @property
    def niftimal_precision(self) -> str:
        return self._niftimal_precision

    @property
    def niftimal_precision_decimal(self) -> int:
        return self._niftimal_precision_decimal

    @property
    def locale(self):
        if self._locale is None:
            from swixknife import sezimal_locale
            self._locale = sezimal_locale()

        return self._locale

    @locale.setter
    def locale(self, locale: str = None):
        from swixknife import sezimal_locale
        self._locale = sezimal_locale(locale)


sezimal_context = SezimalContext()
