
__all__ = (
    'Sezimal',
    'SezimalInteger',
    'SezimalFraction',
    'SezimalDecimalUnit',
)


from decimal import Decimal, localcontext, getcontext
from fractions import Fraction as DecimalFraction

from typing import TypeVar
import numbers as _numbers

Self = TypeVar('Self', bound='Sezimal')
IntegerSelf = TypeVar('IntegerSelf', bound='SezimalInteger')
FractionSelf = TypeVar('FractionSelf', bound='SezimalFraction')
DecimalUnitSelf = TypeVar('DecimalUnitSelf', bound='SezimalDecimalUnit')

Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

from .base import validate_clean_sezimal, \
    decimal_to_sezimal, sezimal_to_decimal, \
    sezimal_format, decimal_format, \
    sezimal_to_dozenal, dozenal_format, \
    sezimal_to_niftimal, niftimal_format, \
    dozenal_to_sezimal, \
    sezimal_context


getcontext().prec = sezimal_context.decimal_precision

#
# Operations maps/tables
#
from . import _sezimal_maps, _sezimal_reciprocal_map

_ADDITION_MAP = _sezimal_maps.ADDITION_MAP
_SUBTRACTION_MAP = _sezimal_maps.SUBTRACTION_MAP
_SUBTRACTION_BORROWED = _sezimal_maps.SUBTRACTION_BORROWED
_MULTIPLICATION_MAP = _sezimal_maps.MULTIPLICATION_MAP
_RECIPROCAL_MAP = _sezimal_reciprocal_map.RECIPROCAL_MAP
# _RECIPROCAL_MAP = {}
_FACTORIAL = _sezimal_maps.FACTORIAL
_EXP = {}
_LN = {}


class Sezimal:
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', 'reciprocal']

    def __init__(self, number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction, _internal: bool = False) -> Self:
        original_decimal = None

        if type(number) == Decimal:
            original_decimal = number
            cleaned_number = validate_clean_sezimal(decimal_to_sezimal(str(number)))

        elif type(number).__name__ == 'SezimalDecimalUnit':
            original_decimal = number.decimal
            cleaned_number = validate_clean_sezimal(decimal_to_sezimal(str(number.decimal)))

        elif type(number).__name__ in ('Sezimal', 'SezimalInteger'):
            cleaned_number = str(number)

        elif type(number).__name__ == 'SezimalFraction':
            cleaned_number = str(number.sezimal)

        elif type(number).__name__ in ('Dozenal', 'DozenalInteger'):
            cleaned_number = dozenal_to_sezimal(str(number))

        elif type(number).__name__ == 'DozenalFraction':
            cleaned_number = dozenal_to_sezimal(str(number.dozenal))

        elif type(number) == str and ('/' in number or '⁄' in number or '÷' in number):
            cleaned_number = str(SezimalFraction(number).sezimal)

        elif type(number) == str and ';' in number:
            cleaned_number = str(SezimalDecimalUnit(number).sezimal)

        else:
            if _internal:
                cleaned_number = str(number)
            else:
                cleaned_number = validate_clean_sezimal(number)

        if cleaned_number[0] == '-':
            cleaned_number = cleaned_number[1:]
            self._sign = -1
        else:
            self._sign = 1

        if '.' in cleaned_number:
            self._integer = str(int(cleaned_number.split('.')[0]))
            self._fraction = cleaned_number.split('.')[1]
        else:
            self._integer = str(int(cleaned_number))
            self._fraction = ''

        self._precision = len(self._fraction)
        self._digits = list(self._integer + self._fraction)

        #
        # Converts and stores as decimal
        #
        if original_decimal is None:
            dec = sezimal_to_decimal(cleaned_number)

            if self._sign < 0 and dec[0] != '-':
                dec = '-' + dec

            self._value = Decimal(dec)

        else:
            self._value = original_decimal

    def __str__(self) -> str:
        if self._sign == -1 and self._integer[0] != '-':
            res = '-' + self._integer
        else:
            res = self._integer

        if self._precision:
            res += '.'
            res += self._fraction

        return res

    def __repr__(self) -> str:
        if not self._fraction:
            return f"Sezimal('{self.formatted_number}') == Decimal('{decimal_format(self.decimal, decimal_places=0)}')"
        else:
            return f"Sezimal('{self.formatted_number}') == Decimal('{decimal_format(self.decimal, decimal_places=sezimal_context.decimal_precision)}')"

    @property
    def formatted_number(self) -> str:
        return sezimal_format(
            str(self),
            sezimal_places=decimal_to_sezimal(self._precision),
            sezimal_digits=sezimal_context.sezimal_digits,
        )

    @property
    def decimal(self) -> Decimal:
        return self._value

    @property
    def decimal_formatted_number(self) -> str:
        if not self._fraction:
            return decimal_format(str(self._value), decimal_places=0)
        else:
            return decimal_format(str(self._value), decimal_places=sezimal_context.decimal_precision)

    @property
    def dozenal(self) -> str:
        if not self._fraction:
            return dozenal_format(self, dozenal_places=0, group_separator='')
        else:
            return dozenal_format(self, group_separator='')

    @property
    def dozenal_formatted_number(self) -> str:
        if not self._fraction:
            return dozenal_format(self, dozenal_places=0)
        else:
            return dozenal_format(self)

    @property
    def niftimal(self) -> str:
        if not self._fraction:
            return niftimal_format(self, niftimal_places=0, group_separator='')
        else:
            return niftimal_format(self, group_separator='')

    @property
    def niftimal_formatted_number(self) -> str:
        if not self._fraction:
            return niftimal_format(self, niftimal_places=0)
        else:
            return niftimal_format(self)

    def __int__(self) -> int:
        return int(sezimal_to_decimal(self._integer)) * self._sign

    def __trunc__(self) -> IntegerSelf:
        return SezimalInteger(self._integer) * self._sign

    def __float__(self) -> float:
        return float(sezimal_to_decimal(str(self)))

    def __decimal__(self) -> Decimal:
        return self._value

    def __compare__(self, other_number: Self) -> IntegerSelf:
        #
        # If the sign of both numbers are not equal,
        # they can be compared only by their sign, unless
        # it is 0 and -0
        #
        if self._sign != other_number._sign:
            if self._value == 0 and other_number._value == 0:
                return 0

            return self._sign

        #
        # The signs are the same, let’s check the numbers
        #
        precision = max(self._precision, other_number._precision)

        this = str(self._integer) + str(self._fraction).ljust(precision, '0')
        other = str(other_number._integer) + str(other_number._fraction).ljust(precision, '0')

        length = max(len(this), len(other))

        this = this.rjust(length, '0')
        other = other.rjust(length, '0')

        if this == other:
            return 0

        if self._sign == 1:
            return 1 if this > other else -1
        else:
            return -1 if this > other else 1

    def __eq__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__compare__(other_number) == 0

    def __ne__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        return not self.__eq__(other_number)

    def __lt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__compare__(other_number) < 0

    def __ge__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        return not self.__lt__(other_number)

    def __gt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__compare__(other_number) > 0

    def __le__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        return not self.__gt__(other_number)

    def __hash__(self):
        return self.decimal.__hash__()

    def __bool__(self) -> bool:
        return not self == 0

    def __pos__(self) -> Self:
        return Sezimal(self)

    def __neg__(self) -> Self:
        return Sezimal(self * -1)

    def __abs__(self) -> Self:
        if self._sign == 1:
            return Sezimal(self)

        return Sezimal(self * -1)

    def __addition(self, other_number: Self) -> str:
        if other_number == 0:
            return str(self)

        #
        # Adds two values;
        # the final sign of the operation is dealt with by the calling method: __add__ or __sub__
        #
        digits_a = list(self._digits)
        digits_b = list(other_number._digits)

        #
        # Normalizes the fractional part between the two values,
        #
        if self._precision > other_number._precision:
            digits_b += list('0' * (self._precision - other_number._precision))
            final_precision = self._precision

        elif other_number._precision > self._precision:
            digits_a += list('0' * (other_number._precision - self._precision))
            final_precision = other_number._precision

        else:
            final_precision = self._precision

        digits_a = digits_a[::-1]
        digits_b = digits_b[::-1]

        adition = ''
        carries = '0'

        for i in range(max(len(digits_a), len(digits_b))):
            if i + 1 <= len(digits_a):
                d1 = digits_a[i]
            else:
                d1 = '0'

            if i + 1 <= len(digits_b):
                d2 = digits_b[i]
            else:
                d2 = '0'

            sd = _ADDITION_MAP[d1][d2]
            sd = _ADDITION_MAP[carries][sd]

            adition += sd[-1]

            if len(sd) > 1:
                carries = sd[0]
            else:
                carries = '0'

        if carries != '0':
            adition += carries

        if final_precision:
            adition = adition[0:final_precision] + '.' + adition[final_precision:]

        adition = adition[::-1]

        return adition

    def __subtraction(self, other_number: Self) -> str:
        if other_number == 0:
            return str(self)

        #
        # Subtracts the lesser value from the greater one;
        # the final sign of the operation is dealt with by the calling method: __add__ or __sub__
        #
        digits_a = list(self._digits)
        digits_b = list(other_number._digits)

        #
        # Normalizes the fractional part between the two values,
        #
        if self._precision > other_number._precision:
            digits_b += list('0' * (self._precision - other_number._precision))
            final_precision = self._precision

        elif other_number._precision > self._precision:
            digits_a += list('0' * (other_number._precision - self._precision))
            final_precision = other_number._precision

        else:
            final_precision = self._precision

        digits_a = digits_a[::-1]
        digits_b = digits_b[::-1]

        if abs(self) < abs(other_number):
            d = digits_a
            digits_a = digits_b
            digits_b = d

        subtraction = ''

        i = 0
        while i < len(digits_a):
            d1 = digits_a[i]

            if i + 1 <= len(digits_b):
                d2 = digits_b[i]
            else:
                d2 = '0'

            if d1 >= d2:
                sd = _SUBTRACTION_MAP[d1][d2]

            #
            # Vay presizar enprestar 1?
            #
            else:
                d1 = '1' + d1
                sd = _SUBTRACTION_MAP[d1][d2]

                #
                # Trata u enpréstimu nus prósimus díjitus,
                # kuydandu ki u 0 propaga u enpréstimu uma kaza
                # pra frenti
                #
                if len(digits_a) >= i + 1:
                    j = i + 1

                    while j < len(digits_a):
                        if digits_a[j] != '0':
                            digits_a[j] = _SUBTRACTION_BORROWED[digits_a[j]]
                            break

                        else:
                            digits_a[j] = _SUBTRACTION_BORROWED[digits_a[j]]
                            j += 1

                else:
                    i = len(digits_a)

            i += 1

            subtraction += sd

        if final_precision:
            subtraction = subtraction[0:final_precision] + '.' + subtraction[final_precision:]

        subtraction = subtraction[::-1]

        return subtraction

    def __add__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__radd__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        #
        # Deals with the signs, and does the adition or subtraction accordingly
        #
        if self._sign == 1 and other_number._sign == 1:
            res = self.__addition(other_number)

        elif self._sign == 1 and other_number._sign == -1:
            res = self.__subtraction(other_number)

            if abs(other_number) > abs(self) and res[0] != '-':
                res = '-' + res

        elif self._sign == -1 and other_number._sign == -1:
            res = self.__addition(other_number)
            res = '-' + res

        elif self._sign == -1 and other_number._sign == 1:
            res = other_number.__subtraction(self)

            if abs(self) > abs(other_number) and res[0] != '-':
               res = '-' + res

        return Sezimal(res, _internal=True)

    def __radd__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__add__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__add__(self)

    def __sub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__rsub__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        #
        # Deals with the signs, and does the adition or subtraction accordingly
        #
        if self._sign == 1 and other_number._sign == 1:
            res = self.__subtraction(other_number)

            if abs(other_number) > abs(self) and res[0] != '-':
                res = '-' + res

        elif self._sign == 1 and other_number._sign == -1:
            res = self.__addition(other_number)

        elif self._sign == -1 and other_number._sign == -1:
            res = self.__subtraction(other_number)

            if abs(self) > abs(other_number) and res[0] != '-':
                res = '-' + res

        elif self._sign == -1 and other_number._sign == 1:
            res = self.__addition(other_number)

            if res[0] != '-':
                res = '-' + res

        return Sezimal(res, _internal=True)

    def __rsub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__sub__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__sub__(self)

    def __round_half_up__(self, precision: IntegerSelf, last_digit: str, next_digit: str, to_discard: str) -> Self:
        adjust = Sezimal(0)

        if next_digit == '3':
            if to_discard.replace('0', '') != '':
                adjust = Sezimal(f'1e-{precision}') * self._sign
            elif last_digit in '135':
                adjust = Sezimal(f'1e-{precision}') * self._sign

        elif next_digit in '45':
            adjust = Sezimal(f'1e-{precision}') * self._sign

        return adjust

    def __round_half_down__(self, precision: IntegerSelf, last_digit: str, next_digit: str, to_discard: str) -> Self:
        adjust = Sezimal(0)

        if next_digit == '3':
            if to_discard.replace('0', '') != '':
                adjust = Sezimal(f'1e-{precision}') * self._sign

        elif next_digit in '45':
            adjust = Sezimal(f'1e-{precision}') * self._sign

        return adjust

    def __round__(self, precision: IntegerSelf = sezimal_context.sezimal_precision) -> Self:
        precision = SezimalInteger(precision)

        if self._precision <= int(precision):
            return self

        to_round = self._integer + '.' + self._fraction[:int(precision)]

        if self._sign == -1:
            to_round = '-' + to_round

        if precision == 0:
            last_digit = self._integer[-1]
            next_digit = self._fraction[0]
            to_discard = self._fraction[1:]

        else:
            last_digit = self._fraction[int(precision) - 1]
            next_digit = self._fraction[int(precision)]
            to_discard = self._fraction[int(precision) + 1:]

        adjust = self.__round_half_up__(precision, last_digit, next_digit, to_discard)

        rounded = Sezimal(to_round, _internal=True) + adjust

        if rounded._sign != self._sign:
            rounded = Sezimal(0, _internal=True)

        return rounded

    def trunc(self, precision: IntegerSelf = sezimal_context.sezimal_precision) -> Self:
        if precision is None:
            precision = 0

        precision = SezimalInteger(precision)

        if self._precision <= int(precision):
            return self

        to_round = self._integer + '.' + self._fraction[:int(precision)]

        if self._sign == -1:
            to_round = '-' + to_round

        return Sezimal(to_round, _internal=True)

    def is_integer(self) -> bool:
        return self == self.trunc(0)

    def _mult_div_finalizing(self):
        res = round(self, sezimal_context.sezimal_precision)

        if res._fraction and len(res._fraction) >= 3:
            fives = res._fraction[::-1][3:][::-1]

            if len(fives) >= 5 and fives[-5:] in ('55555', '55554', '55553'):
                new = round(res, decimal_to_sezimal(res._precision - 4))
                res = Sezimal(new._integer + '.' + new._fraction.ljust(res._precision, '0'))
            elif len(fives) >= 6 and fives[-6:] in (
                '555555',
                '555545', '555544', '555543',
                '555535', '555534', '555533',
            ):
                new = round(res, decimal_to_sezimal(res._precision - 6))
                res = Sezimal(new._integer + '.' + new._fraction.ljust(res._precision, '0'))

        return res

    def __multiplication(self, other_number: Self) -> str:
        if self == 0 or other_number == 0:
            return '0'

        if other_number == 1 or other_number == -1:
            if self._sign == -1:
                return str(self)[1:]
            else:
                return str(self)

        #
        # Multiplies two values;
        # the final sign of the operation is dealt with by the calling method: __mul__
        #
        digits_a = list(self._digits)[::-1]
        digits_b = list(other_number._digits)[::-1]
        final_precision = self._precision + other_number._precision
        sums = []

        i = 0
        for d1 in digits_a:
            carries = '0'
            sums.append('0' * i)
            i += 1

            for d2 in digits_b:
                md = _MULTIPLICATION_MAP[d1][d2]

                if carries != '0':
                    md = str(Sezimal(md, _internal=True) + carries)

                sums[-1] += md[-1]

                if len(md) != 1:
                    carries = md[0]
                else:
                    carries = '0'

            if carries != '0':
                sums[-1] += carries

        multiplication = Sezimal('0', _internal=True)

        for s in sums:
            if s:
                multiplication += Sezimal(s[::-1], _internal=True)

        multiplication = str(multiplication)

        if final_precision:
            multiplication = multiplication[::-1]

            if len(multiplication) < final_precision + 1:
                multiplication += '0' * (final_precision - len(multiplication) + 1)

            multiplication = multiplication[0:final_precision] + '.' + multiplication[final_precision:]
            multiplication = multiplication[::-1]

        return multiplication

    def __mul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__rmul__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        #
        # Deals with the signs
        #
        if self._sign == 1 and other_number._sign == 1:
            res = self.__multiplication(other_number)

        elif self._sign == 1 and other_number._sign == -1:
            res = self.__multiplication(other_number)
            res = '-' + res

        elif self._sign == -1 and other_number._sign == -1:
            res = self.__multiplication(other_number)

        elif self._sign == -1 and other_number._sign == 1:
            res = self.__multiplication(other_number)
            res = '-' + res

        return Sezimal(res, _internal=True)._mult_div_finalizing()

    def __rmul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__mul__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__mul__(self)

    def __basic_division(self, dividend: Self, divisor: Self) -> tuple[Self]:
        remainder = dividend
        quotient = Sezimal('0', _internal=True)

        while remainder >= divisor:
            remainder -= divisor
            quotient += 1

        return quotient, remainder

    def new_division(self, dividend: Self, divisor: Self) -> tuple[Self]:
        if dividend < divisor:
            return Sezimal(0, _internal=True), dividend

        quotient = Sezimal('0', _internal=True)
        remainder = Sezimal(dividend._digits[0], _internal=True)

        for i in range(1, len(dividend._digits)):
            remainder *= 10
            remainder += Sezimal(dividend._digits[i], _internal=True)

            factor = Sezimal(0, _internal=True)

            while (divisor * (factor + 1)) < remainder:
                factor += 1

            quotient *= 10
            quotient += factor
            remainder -= divisor * factor

        return quotient, remainder

        # # Convert quotient and remainder to strings
        # remainder_str = ''
        # while remainder:
        #     remainder_str += str(remainder % base)
        #     remainder //= base
        #
        # # Return quotient and remainder as strings
        # return quotient_str, int(remainder_str[::-1])

    def __division(self, other_number: Self, max_precision: IntegerSelf = None) -> str:
        #
        # Divides two values;
        # the final sign of the operation is dealt with by the calling method: __div__
        #
        if other_number == 0:
            raise ZeroDivisionError('Division by zero')

        if self == 0:
            return '0'

        if other_number == 1:
            return str(self)

        if sezimal_context.fractions_use_decimal:
            using_ultra_precision = sezimal_context.using_ultra_precision
            precision = sezimal_context.precision

            if not using_ultra_precision:
                sezimal_context.use_ultra_precision()

            res = round(Sezimal(self.decimal / other_number.decimal), precision)

            if not using_ultra_precision:
                sezimal_context.back_to_regular_precision()

            return res

        negative = other_number < 0
        check = str(other_number).replace('-', '')

        if self == 1 and check in _RECIPROCAL_MAP:
            division = validate_clean_sezimal(_RECIPROCAL_MAP[check], double_precision=True)

            if negative:
                division = '-' + division

            return division

        using_ultra_precision = sezimal_context.using_ultra_precision
        precision = sezimal_context.precision

        if not using_ultra_precision:
            sezimal_context.use_ultra_precision()

        max_precision = sezimal_context.sezimal_precision
        max_precision = int(SezimalInteger(max_precision))

        digits_a = list(self._digits)
        digits_b = list(other_number._digits)

        #
        # Normalizes the fractional part between the two values,
        #
        if self._precision > other_number._precision:
            digits_b += list('0' * (self._precision - other_number._precision))
            final_precision = self._precision

        elif other_number._precision > self._precision:
            digits_a += list('0' * (other_number._precision - self._precision))
            final_precision = other_number._precision

        else:
            final_precision = self._precision

        initial_precision = final_precision

        dividend = Sezimal(''.join(digits_a), _internal=True)
        divisor = Sezimal(''.join(digits_b), _internal=True)
        quotient, remainder = self.__basic_division(dividend, divisor)
        max_precision = max(final_precision, max_precision) * 2

        sezimal_context.sezimal_precision = decimal_to_sezimal(str(max_precision))

        while remainder > 0 and final_precision < max_precision:
            dividend = remainder * 10
            final_precision += 1
            q, remainder = self.__basic_division(dividend, divisor)
            quotient = Sezimal(str(quotient) + str(q), _internal=True)

        division = str(quotient)

        final_precision -= initial_precision

        if final_precision:
            division = division[::-1]

            if len(division) < final_precision + 1:
                division += '0' * (final_precision - len(division) + 1)

            division = division[0:final_precision] + '.' + division[final_precision:]
            division = division[::-1]

        if self == 1:
            _RECIPROCAL_MAP[check] = division
            # print(f"""    '{check}': '{sezimal_format(division, sezimal_places=sezimal_context.sezimal_precision)}',""")

        if negative:
            division = '-' + division

        if not using_ultra_precision:
            sezimal_context.back_to_regular_precision()

        return division

    def __truediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        #
        # Calculate the reciprocal first
        #
        if hasattr(other_number, 'reciprocal'):
            reciprocal = other_number.reciprocal
        else:
            if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
                return other_number.__rtruediv__(self)

            if type(other_number) != Sezimal:
                other_number = Sezimal(other_number)

            if other_number == 1 or other_number == -1:
                reciprocal = other_number
            else:
                reciprocal = Sezimal('1', _internal=True).__division(other_number)

        return self * reciprocal

        # #
        # # Deals with the signs
        # #
        # if self._sign == 1 and other_number._sign == 1:
        #     res = self.__division(other_number)
        #
        # elif self._sign == 1 and other_number._sign == -1:
        #     res = self.__division(other_number)
        #     res = '-' + res
        #
        # elif self._sign == -1 and other_number._sign == -1:
        #     res = self.__division(other_number)
        #
        # elif self._sign == -1 and other_number._sign == 1:
        #     res = self.__division(other_number)
        #     res = '-' + res
        #
        # return Sezimal(res)._mult_div_finalizing()

    def __rtruediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__truediv__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__truediv__(self)

    def __divmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> tuple[Self]:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        dividend = Sezimal(self._integer, _internal=True)
        divisor = Sezimal(other_number._integer, _internal=True)

        if divisor == 0:
            raise ZeroDivisionError('Division by zero')

        if divisor == 1:
            return dividend, Sezimal(0, _internal=True)

        quotient, remainder = self.__basic_division(dividend, divisor)

        if self._sign == 1 and other_number._sign == 1:
            pass

        elif self._sign == 1 and other_number._sign == -1:
            quotient *= -1
            remainder *= -1

            if remainder != 0:
                quotient -= 1
                remainder = dividend + (quotient * divisor)

        elif self._sign == -1 and other_number._sign == -1:
            remainder *= -1

        elif self._sign == -1 and other_number._sign == 1:
            quotient *= -1

            if remainder != 0:
                quotient -= 1
                remainder = (dividend + (quotient * divisor)) * -1

        return quotient, remainder

    def __floordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__rfloordiv__(self)

        quotient, remainder = self.__divmod__(other_number)
        return quotient

    def __rfloordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number).__name__ in ('SezimalDecimalUnit', 'DozenalDecimalUnit'):
            return other_number.__floordiv__(self)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__floordiv__(self)

    def __mod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        quotient, remainder = self.__divmod__(other_number)
        return remainder

    def __rmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__mod__(self)

    def factorial(self) -> IntegerSelf:
        if self == 0 or self == 1:
            return SezimalInteger(1)

        if self == 2:
            return SezimalInteger(2)

        integer = SezimalInteger(self._integer)

        if integer in _FACTORIAL:
            return _FACTORIAL[integer]

        if str(integer) in _FACTORIAL:
            _FACTORIAL[integer] = SezimalInteger(_FACTORIAL[str(integer)])
            del _FACTORIAL[str(integer)]
            return _FACTORIAL[integer]

        next_integer = integer - 1

        _FACTORIAL[integer] = SezimalInteger(integer * next_integer.factorial())

        return _FACTORIAL[integer]

    def calculus_exp(self) -> Self:
        sezimal_context.sezimal_precision_decimal += 4

        result = Sezimal(1, _internal=True)

        for i in range(1, sezimal_context.sezimal_precision_decimal + 1):
            i = SezimalInteger(Decimal(i))
            result += (self ** i) / i.factorial()

        sezimal_context.sezimal_precision_decimal -= 4

        return result._mult_div_finalizing()

    def exp(self) -> Self:
        with localcontext() as context:
            context.prec = sezimal_context.decimal_precision + 3
            sezimal_context.sezimal_precision_decimal += 4
            result = self.decimal.exp()
            result = Sezimal(result)
            sezimal_context.sezimal_precision_decimal -= 4

        return result._mult_div_finalizing()

    # def calculus_ln(self) -> Self:
    #     result = Sezimal(0)
    #
    #     if str(self) in LOGARITHM_TABLE:
    #         return Sezimal(LOGARITHM_TABLE[str(self)])._mult_div_finalizing()
    #
    #     term = (self - 1) * (Sezimal(1) / self)
    #
    #     i = Sezimal(1)
    #
    #     while i <= 200:
    #         result += (term ** i) * (Sezimal(1) / i)
    #         i += 1
    #
    #     return result

    def ln(self) -> Self:
        with localcontext() as context:
            context.prec = sezimal_context.decimal_precision + 3
            sezimal_context.sezimal_precision_decimal += 4
            result = self.decimal.ln()
            result = Sezimal(result)
            sezimal_context.sezimal_precision_decimal -= 4

        return result._mult_div_finalizing()

    def __calculus_power(self, other_number: Self) -> Self:
        if other_number == 0:
            return Sezimal(1, _internal=True)

        if self == 0:
            return Sezimal(0, _internal=True)

        if other_number < 0:
            return Sezimal(1, _internal=True) / self.__power(other_number * -1)

        if other_number.is_integer():
            result = self

            while other_number > 1:
                result *= self
                other_number -= 1

        else:
            result = self.ln() * other_number
            result = result.exp()

        return result

    def __power(self, other_number: Self) -> Self:
        if other_number == 0:
            return SezimalInteger(1, _internal=True)

        #
        # When the exponent is an integer,
        # avoid loosing precision in the decimal conversion,
        #
        if other_number.is_integer():
            result = self

            negative = other_number < 0

            if negative:
                other_number *= -1

            while other_number > 1:
                result *= self
                other_number -= 1

            if negative:
                return 1 / result

            return result

        result = self.decimal ** other_number.decimal
        result = Sezimal(result)
        return result._mult_div_finalizing()

    def __pow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__power(other_number)

    def __rpow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__pow__(self)

    def log(self) -> Self:
        with localcontext() as context:
            context.prec = sezimal_context.decimal_precision + 3
            sezimal_context.sezimal_precision_decimal += 4
            result = self.decimal.ln() / Decimal(6).ln()
            result = Sezimal(result)
            sezimal_context.sezimal_precision_decimal -= 4

        return result._mult_div_finalizing()

    def log2(self) -> Self:
        with localcontext() as context:
            context.prec = sezimal_context.decimal_precision + 3
            sezimal_context.sezimal_precision_decimal += 4
            result = self.decimal.ln() / Decimal(2).ln()
            result = Sezimal(result)
            sezimal_context.sezimal_precision_decimal -= 4

        return result._mult_div_finalizing()

    def log14(self) -> Self:
        with localcontext() as context:
            context.prec = sezimal_context.decimal_precision + 3
            sezimal_context.sezimal_precision_decimal += 4
            result = self.decimal.ln() / Decimal(10).ln()
            result = Sezimal(result)
            sezimal_context.sezimal_precision_decimal -= 4

        return result._mult_div_finalizing()

    def sqrt(self) -> Self:
        return self ** Sezimal('0.3')

    def cbrt(self) -> Self:
        return self ** Sezimal('0.2')

    def _find_gcd(self, numerator: Self, denominator: Self) -> Self:
        if denominator == 0:
            return numerator

        return self._find_gcd(denominator, numerator % denominator)

    def as_integer_ratio(self) -> tuple[IntegerSelf, IntegerSelf]:
        if self.is_integer():
            return SezimalInteger(self), SezimalInteger(1)

        numerator = SezimalInteger(self._integer + self._fraction, _internal=True)
        denominator = SezimalInteger(f'1e+{SezimalInteger(Decimal(self._precision))}')

        # gcd = self._find_gcd(numerator, denominator)
        # numerator //= gcd
        # denominator //= gcd

        return numerator, denominator


class SezimalInteger(Sezimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits']

    def __init__(
            self,
            number: str | int | float | Decimal | Self | IntegerSelf | Dozenal | DozenalInteger,
            _internal: bool = False
        ) -> Self:
        super().__init__(number, _internal=_internal)

        original_decimal = None

        if type(number) == Decimal:
            original_decimal = Decimal(int(number))

        self._fraction = ''
        self._precision = 0
        self._digits = list(self._integer)

        #
        # Converts and stores as decimal
        #
        if original_decimal is None:
            dec = sezimal_to_decimal(self._integer)

            if self._sign == -1:
                dec = '-' + dec

            if '.' in dec:
                dec = dec.split('.')[0]

            self._value = Decimal(dec)

        else:
            self._value = original_decimal

    def __repr__(self) -> str:
        return super().__repr__().replace('Sezimal', 'SezimalInteger')

    def __index__(self):
        return int(self._integer, 6)


class SezimalFraction(Sezimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', '_numerator', '_denominator', '_sezimal', '_precalculated_value', '_precalculated_reciprocal']

    def __init__(self, numerator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction, denominator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction = None, _precalculated_value: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction = None, _precalculated_reciprocal: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction = None) -> Self:
        if type(numerator) == str:
            if '/' in numerator:
                numerator, denominator = numerator.split('/')
            elif '⁄' in numerator:
                numerator, denominator = numerator.split('⁄')
            elif '÷' in numerator:
                numerator, denominator = numerator.split('÷')

        elif type(numerator) == Decimal:
            numerator = decimal_to_sezimal(str(numerator))

        cleaned_numerator = validate_clean_sezimal(numerator)

        if denominator is None:
            numerator = Sezimal(cleaned_numerator)
            _precalculated_value = numerator
            numerator, denominator = numerator.as_integer_ratio()
            cleaned_numerator = str(numerator)
            cleaned_denominator = str(denominator)

        elif type(denominator) == Decimal:
            denominator = decimal_to_sezimal(str(denominator))
            cleaned_denominator = validate_clean_sezimal(denominator)

        else:
            cleaned_denominator = validate_clean_sezimal(denominator)

        old_precision = sezimal_context.sezimal_precision

        if sezimal_context.fractions_precision:
            sezimal_context.sezimal_precision = sezimal_context.fractions_precision

        # self._numerator, self._denominator = \
        #     self.__simplify(
        #         Sezimal(cleaned_numerator),
        #         Sezimal(cleaned_denominator),
        #     )
        self._numerator, self._denominator = \
            Sezimal(cleaned_numerator), \
            Sezimal(cleaned_denominator)

        if _precalculated_value is not None:
            self._sezimal = Sezimal(_precalculated_value)
        elif sezimal_context.fractions_use_decimal:
            self._sezimal = Sezimal(self._numerator.decimal / self._denominator.decimal)
        else:
            self._sezimal = self._numerator / self._denominator

        if old_precision != sezimal_context.sezimal_precision:
            self._sezimal = round(self._sezimal, old_precision)
            sezimal_context.sezimal_precision = old_precision

        self._precalculated_value = _precalculated_value
        self._precalculated_reciprocal = _precalculated_reciprocal

        super().__init__(self._sezimal)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @property
    def sezimal(self) -> Sezimal:
        return self._sezimal

    @property
    def decimal(self) -> Decimal:
        return self._numerator.decimal / self._denominator.decimal

    @property
    def reciprocal(self) -> FractionSelf:
        return SezimalFraction(self._denominator, self._numerator, self._precalculated_reciprocal, self._precalculated_value)

    @reciprocal.setter
    def reciprocal(self, value):
        pass

    def __str__(self) -> str:
        if self._sign == -1 and str(self._numerator)[0] != '-':
            res = '-'
        else:
            res = ''

        res += str(self._numerator)
        res += ' / '
        res += str(self._denominator)

        return res

    @property
    def formatted_number(self):
        return f'{self._numerator.formatted_number} / {self._denominator.formatted_number}'

    @property
    def decimal_formatted_number(self):
        return f'{self._numerator.decimal_formatted_number} / {self._denominator.decimal_formatted_number}'

    def __repr__(self) -> str:
        return f"SezimalFraction('{self.formatted_number}') == {self._sezimal.__repr__()}"

    def as_integer_ratio(self) -> tuple[IntegerSelf, IntegerSelf]:
        return self._numerator, self._denominator

    def as_decimal_integer_ratio(self) -> tuple[Decimal, Decimal]:
        return int(self._numerator.decimal), int(self._denominator.decimal)

    def as_decimal_ratio(self) -> tuple[Decimal, Decimal]:
        return self._numerator.decimal, self._denominator.decimal

    def __mul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.numerator
            denominator = self.denominator * other_number.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        numerator = self.numerator * other_number

        if numerator._fraction == '':
            numerator = self.numerator * other_number
            denominator = self.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        return super().__mul__(other_number)

    def __rmul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.numerator
            denominator = self.denominator * other_number.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        numerator = self.numerator * other_number

        if numerator._fraction == '':
            denominator = self.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        return super().__rmul__(other_number)

    def __truediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.denominator
            denominator = self.denominator * other_number.numerator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator
            denominator = self.denominator * other_number
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        return super().__truediv__(other_number)

    def __rtruediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.denominator
            denominator = self.denominator * other_number.numerator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator
            denominator = self.denominator * other_number
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(denominator, numerator)

        return super().__rtruediv__(other_number)

    def __pow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator ** other_number
            denominator = self.denominator ** other_number
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        return super().__pow__(other_number)

    def __add__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            if self.denominator == other_number.denominator:
                numerator = self.numerator + other_number.numerator
                numerator, denominator = self.__simplify(numerator, self.denominator)
                return SezimalFraction(numerator, denominator)

            numerator = self.numerator * other_number.denominator
            numerator += other_number.numerator * self.denominator
            denominator = self.denominator * other_number.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator
            numerator += other_number * self.denominator
            numerator, denominator = self.__simplify(numerator, self.denominator)
            return SezimalFraction(numerator, denominator)

        return super().__add__(other_number)

    def __radd__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            if self.denominator == other_number.denominator:
                numerator = self.numerator + other_number.numerator
                numerator, denominator = self.__simplify(numerator, self.denominator)
                return SezimalFraction(numerator, denominator)

            numerator = self.numerator * other_number.denominator
            numerator += other_number.numerator * self.denominator
            denominator = self.denominator * other_number.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator
            numerator += other_number * self.denominator
            numerator, denominator = self.__simplify(numerator, self.denominator)
            return SezimalFraction(numerator, denominator)

        return super().__radd__(other_number)

    def __sub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            if self.denominator == other_number.denominator:
                numerator = self.numerator - other_number.numerator
                numerator, denominator = self.__simplify(numerator, self.denominator)
                return SezimalFraction(numerator, denominator)

            numerator = self.numerator * other_number.denominator
            numerator -= other_number.numerator * self.denominator
            denominator = self.denominator * other_number.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator
            numerator -= other_number * self.denominator
            numerator, denominator = self.__simplify(numerator, self.denominator)
            return SezimalFraction(numerator, denominator)

        return super().__sub__(other_number)

    def __rsub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            if self.denominator == other_number.denominator:
                numerator = other_number.numerator - self.numerator
                numerator, denominator = self.__simplify(numerator, self.denominator)
                return SezimalFraction(numerator, denominator)

            numerator = other_number.numerator * self.denominator
            numerator -= self.numerator * other_number.denominator
            denominator = self.denominator * other_number.denominator
            numerator, denominator = self.__simplify(numerator, denominator)
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = other_number * self.denominator
            numerator -= self.numerator
            numerator, denominator = self.__simplify(numerator, self.denominator)
            return SezimalFraction(numerator, denominator)

        return super().__rsub__(other_number)

    @property
    def decimal_fraction(self):
        return DecimalFraction(*self.as_decimal_integer_ratio())

    def simplify(self, precision=None) -> FractionSelf:
        num, den = self.__simplify(self.numerator, self.denominator, force=True, precision=precision)

        if num == self.numerator and den == self.denominator:
            return self

        return SezimalFraction(num, den)

    def __simplify(self, num, den, force: bool = False, precision = None):
        if (not sezimal_context.fractions_simplify) and (not force):
            return num, den

        using_ultra_precision = sezimal_context.using_ultra_precision
        precision = sezimal_context.precision

        if not using_ultra_precision:
            sezimal_context.use_ultra_precision()

        with localcontext() as context:
            context.prec = sezimal_context.decimal_precision

            while True:
                x = num.decimal
                y = den.decimal

                while y:
                    x, y = y, x % y

                x = abs(x)

                if x == 1 or x == 0:
                    break

                num = SezimalInteger(num.decimal / x)
                den = SezimalInteger(den.decimal / x)

        if not using_ultra_precision:
            sezimal_context.back_to_regular_precision()

        return num, den

        # if precision:
        #     precision = int(SezimalInteger(precision).decimal)
        # else:
        #     precision = getcontext().prec + 10
        #
        # with localcontext() as context:
        #     if precision < 16:
        #         context.prec = 16
        #     else:
        #         context.prec = precision
        #
        #     num = num.decimal
        #     den = den.decimal
        #
        #     for factor in _sezimal_maps._PRIMES:
        #         factor = Decimal(factor)
        #
        #         if factor > min(abs(num), abs(den)):
        #             break
        #
        #         while True:
        #             num_test = num / factor
        #
        #             if num_test != int(num_test):
        #                 break
        #
        #             den_test = den / factor
        #
        #             if den_test != int(den_test):
        #                 break
        #
        #             num = num_test
        #             den = den_test

        return SezimalInteger(num), SezimalInteger(den)


class SezimalDecimalUnit(Sezimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision',
                 '_digits', '_unit', '_subunit', '_decimal_precision',
                 '_sezimal_precision', '_unit_symbol', '_subunit_symbol']

    def __init__(
        self,
        unit: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction,
        subunit: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction = None,
        decimal_precision: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction = 2,
        unit_symbol: str = '',
        subunit_symbol: str = '',
    ) -> Self:
        self._unit_symbol = unit_symbol
        self._subunit_symbol = subunit_symbol

        if type(unit) == str and ';' in unit:
            parts = unit.split(';')

            if len(parts) == 2:
                unit, subunit = parts
            else:
                unit, subunit, decimal_precision = parts

            unit = unit or '0'
            subunit = subunit or '0'

        elif type(unit) == Decimal:
            if '.' in str(unit):
                unit, subunit = str(unit).split('.')
                unit = decimal_to_sezimal(unit)

                if decimal_precision:
                    decimal_precision = SezimalInteger(decimal_precision)
                    subunit = decimal_to_sezimal(subunit.ljust(int(decimal_precision), '0'))
                else:
                    subunit = decimal_to_sezimal(subunit)

            else:
                unit = decimal_to_sezimal(str(unit))

        self._decimal_precision = SezimalInteger(decimal_precision)
        self._sezimal_precision = SezimalInteger(Decimal(len(str(SezimalInteger(14) ** self._decimal_precision))))

        cleaned_unit = validate_clean_sezimal(unit)

        if subunit is None:
            unit = round(Sezimal(cleaned_unit).decimal, int(self._decimal_precision))

            if '.' in str(unit):
                unit, subunit = str(unit).split('.')
                unit = decimal_to_sezimal(unit)
                subunit = decimal_to_sezimal(subunit)
            else:
                unit = decimal_to_sezimal(str(unit))

            cleaned_unit = str(unit)
            cleaned_subunit = str(subunit)

        elif type(subunit) == Decimal:
            subunit = decimal_to_sezimal(str(subunit))
            cleaned_subunit = validate_clean_sezimal(subunit)

        else:
            cleaned_subunit = validate_clean_sezimal(subunit)

        unit = sezimal_to_decimal(unit)
        subunit = sezimal_to_decimal(subunit)
        decimal = round(Decimal(unit) + (Decimal(subunit) / Decimal(f'1e{int(decimal_precision)}')), int(decimal_precision))

        if '.' in str(decimal):
            unit, subunit = str(decimal).split('.')
        else:
            unit = str(decimal)
            subunit = '0'

        unit = decimal_to_sezimal(unit, 0)
        subunit = decimal_to_sezimal(subunit or '0', 0)

        self._unit = SezimalInteger(unit)
        self._subunit = SezimalInteger(subunit or '0')

        super().__init__(decimal)

    @property
    def unit(self):
        return self._unit

    @property
    def subunit(self):
        return self._subunit

    @property
    def decimal_precision(self):
        return self._decimal_precision

    @property
    def unit_symbol(self):
        return self._unit_symbol

    @property
    def subunit_symbol(self):
        return self._subunit_symbol

    @property
    def sezimal(self) -> Sezimal:
        return Sezimal(self._value)

    def __str__(self) -> str:
        if self._sign == -1 and str(self._unit)[0] != '-':
            res = '-'
        else:
            res = ''

        res += self._unit.formatted_number

        if self._subunit or self._decimal_precision != 2:
            res += ';'
            res += self._subunit.formatted_number

            if self._decimal_precision != 2:
                res += ';'
                res += self._decimal_precision.formatted_number

        return res

    @property
    def formatted_number(self):
        return self.__str__()

    @property
    def formatted_hundreth(self):
        integer = sezimal_format(self._integer, sezimal_places=0)
        fixed_part = self._fraction[0:2].zfill(2)
        recurring_part = self._fraction[2:7].zfill(5)
        recurring_part = recurring_part[0:2] + '_' + recurring_part[2:]
        return integer + '.' + fixed_part + '..' + recurring_part

    @property
    def decimal_formatted_number(self):
        if self._subunit or self._decimal_precision:
            return f'{self._unit.decimal_formatted_number}.{self._subunit.decimal_formatted_number.zfill(self._decimal_precision)}'
        else:
            return f'{self._unit.decimal_formatted_number}'

    def __repr__(self) -> str:
        res = f"'{self}'"

        if self._unit_symbol:
            res += f", unit_symbol='{self._unit_symbol}'"

        if self._subunit_symbol:
            res += f", subunit_symbol='{self._subunit_symbol}'"

        return f"SezimalDecimalUnit({res}) == Decimal('{self.decimal_formatted_number}')"

    def __mul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(self.decimal * other_number.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __rmul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(self.decimal * other_number.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __truediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(self.decimal / other_number.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __rtruediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(other_number.decimal / self.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __pow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(self.decimal ** other_number.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __add__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(self.decimal + other_number.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __radd__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(self.decimal + other_number.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __sub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(self.decimal - other_number.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )

    def __rsub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | DecimalUnitSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != SezimalDecimalUnit:
            other_number = SezimalDecimalUnit(
                other_number,
                decimal_precision=self._decimal_precision,
                unit_symbol=self._unit_symbol,
                subunit_symbol=self._subunit_symbol,
            )

        return SezimalDecimalUnit(
            round(other_number.decimal - self.decimal, int(self._decimal_precision)),
            decimal_precision=self._decimal_precision,
            unit_symbol=self._unit_symbol,
            subunit_symbol=self._subunit_symbol,
        )


_numbers.Number.register(Sezimal)
_numbers.Integral.register(Sezimal)
_numbers.Rational.register(Sezimal)

_numbers.Number.register(SezimalInteger)
_numbers.Integral.register(SezimalInteger)

_numbers.Number.register(SezimalFraction)
_numbers.Integral.register(SezimalFraction)

_numbers.Number.register(SezimalDecimalUnit)
_numbers.Integral.register(SezimalDecimalUnit)
_numbers.Rational.register(SezimalDecimalUnit)
