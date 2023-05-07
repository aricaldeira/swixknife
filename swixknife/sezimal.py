
__all__ = (
    'Sezimal',
    'SezimalInteger',
    'SezimalFraction',
)

from decimal import Decimal, localcontext, getcontext
import re

from typing import TypeVar
import numbers as _numbers

Self = TypeVar('Self', bound='Sezimal')
IntegerSelf = TypeVar('IntegerSelf', bound='SezimalInteger')
FractionSelf = TypeVar('FractionSelf', bound='SezimalFraction')

from .base import validate_clean_sezimal, decimal_to_sezimal, sezimal_to_decimal, sezimal_format, decimal_format


MAX_DECIMAL_PRECISION = 37
getcontext().prec = MAX_DECIMAL_PRECISION
MAX_PRECISION = 120


class Sezimal:
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits']

    def __init__(self, number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        original_decimal = None

        if type(number) == Decimal:
            original_decimal = number
            number = decimal_to_sezimal(str(number))

        elif type(number) == SezimalFraction:
            number = number.sezimal

        elif type(number) == str and ('/' in number or '⁄' in number or '÷' in number):
            number = SezimalFraction(number).sezimal

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
            with localcontext() as context:
                context.prec = MAX_DECIMAL_PRECISION
                self._value = Decimal(sezimal_to_decimal(cleaned_number)) ## .quantize(Decimal(f'1E-{_DECIMAL_PRECISION}'))
                self._value *= self._sign

        else:
            self._value = original_decimal

    def __str__(self) -> str:
        if self._sign == -1:
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
            return f"Sezimal('{self.formatted_number}') == Decimal('{decimal_format(self.decimal, decimal_places=MAX_DECIMAL_PRECISION)}')"

    @property
    def formatted_number(self) -> str:
        return sezimal_format(str(self), sezimal_places=Decimal(self._precision))

    @property
    def decimal(self) -> Decimal:
        return self._value

    def __int__(self) -> int:
        return int(sezimal_to_decimal(self._integer)) * self._sign

    def __float__(self) -> float:
        return float(sezimal_to_decimal(str(self)))

    def __decimal__(self) -> Decimal:
        return self._value

    def __eq__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if self._sign != other_number._sign:
            return False

        precision = max(len(self._integer), len(other_number._integer))

        if self._integer.zfill(precision) != other_number._integer.zfill(precision):
            return False

        precision = max(len(self._fraction), len(other_number._fraction))

        if self._fraction.ljust(precision, '0') != other_number._fraction.ljust(precision, '0'):
            return False

        return True

    def __ne__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
        return not self.__eq__(other_number)

    def __lt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if self == other_number:
            return False

        if self._sign == -1 and other_number._sign == 1:
            return True

        if self._sign == 1 and other_number._sign == -1:
            return False

        precision = max(len(self._integer), len(other_number._integer))

        if self._sign == 1:
            if self._integer.zfill(precision) < other_number._integer.zfill(precision):
                return True

        else:
            if self._integer.zfill(precision) > other_number._integer.zfill(precision):
                return True

        precision = max(len(self._fraction), len(other_number._fraction))

        if self._sign == 1:
            if self._fraction.ljust(precision, '0') < other_number._fraction.ljust(precision, '0'):
                return True

        else:
            if self._fraction.ljust(precision, '0') > other_number._fraction.ljust(precision, '0'):
                return True

        return False

    def __ge__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
        return not self.__lt__(other_number)

    def __gt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if self == other_number:
            return False

        if self._sign == -1 and other_number._sign == 1:
            return False

        if self._sign == 1 and other_number._sign == -1:
            return True

        precision = max(len(self._integer), len(other_number._integer))

        if self._sign == 1:
            if self._integer.zfill(precision) > other_number._integer.zfill(precision):
                return True

        else:
            if self._integer.zfill(precision) < other_number._integer.zfill(precision):
                return True

        precision = max(len(self._fraction), len(other_number._fraction))

        if self._sign == 1:
            if self._fraction.ljust(precision, '0') > other_number._fraction.ljust(precision, '0'):
                return True

        else:
            if self._fraction.ljust(precision, '0') < other_number._fraction.ljust(precision, '0'):
                return True

        return False

    def __le__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
        return not self.__gt__(other_number)

    def __hash__(self):
        return self.decimal.__hash__()

    def __bool__(self) -> bool:
        return self.decimal.__bool__()

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
        MAP = {
            '0': {'0': '0', '1':  '1', '2':  '2', '3':  '3', '4':  '4', '5':  '5', '10': '10', '11': '11', '12': '12', '13': '13', '14': '14'},
            '1': {'0': '1', '1':  '2', '2':  '3', '3':  '4', '4':  '5', '5': '10', '10': '11', '11': '12', '12': '13', '13': '14', '14': '15'},
            '2': {'0': '2', '1':  '3', '2':  '4', '3':  '5', '4': '10', '5': '11', '10': '12', '11': '13', '12': '14', '13': '15', '14': '20'},
            '3': {'0': '3', '1':  '4', '2':  '5', '3': '10', '4': '11', '5': '12', '10': '13', '11': '14', '12': '15', '13': '20', '14': '21'},
            '4': {'0': '4', '1':  '5', '2': '10', '3': '11', '4': '12', '5': '13', '10': '14', '11': '15', '12': '20', '13': '21', '14': '22'},
            '5': {'0': '5', '1': '10', '2': '11', '3': '12', '4': '13', '5': '14', '10': '15', '11': '20', '12': '21', '13': '22', '14': '23'},
        }

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

            sd = MAP[d1][d2]
            sd = MAP[carries][sd]

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
        MAP = {
            '0': {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5'},
            '1': {'0': '1', '1': '0', '2': '1', '3': '2', '4': '3', '5': '4'},
            '2': {'0': '2', '1': '1', '2': '0', '3': '1', '4': '2', '5': '3'},
            '3': {'0': '3', '1': '2', '2': '1', '3': '0', '4': '1', '5': '2'},
            '4': {'0': '4', '1': '3', '2': '2', '3': '1', '4': '0', '5': '1'},
            '5': {'0': '5', '1': '4', '2': '3', '3': '2', '4': '1', '5': '0'},
            '10': {'0': '10', '1':  '5', '2':  '4', '3':  '3', '4':  '2', '5':  '1'},
            '11': {'0': '11', '1': '10', '2':  '5', '3':  '4', '4':  '3', '5':  '2'},
            '12': {'0': '12', '1': '11', '2': '10', '3':  '5', '4':  '4', '5':  '3'},
            '13': {'0': '13', '1': '12', '2': '11', '3': '10', '4':  '5', '5':  '4'},
            '14': {'0': '14', '1': '13', '2': '12', '3': '11', '4': '10', '5':  '5'},
            '15': {'0': '15', '1': '14', '2': '13', '3': '12', '4': '11', '5': '10'},
        }

        BORROWED = {
            '0': '5',
            '1': '0',
            '2': '1',
            '3': '2',
            '4': '3',
            '5': '4',
        }

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
                sd = MAP[d1][d2]

            #
            # Vay presizar enprestar 1?
            #
            else:
                d1 = '1' + d1
                sd = MAP[d1][d2]

                #
                # Trata u enpréstimu nus prósimus díjitus,
                # kuydandu ki u 0 propaga u enpréstimu uma kaza
                # pra frenti
                #
                if len(digits_a) >= i + 1:
                    j = i + 1

                    while j < len(digits_a):
                        if digits_a[j] != '0':
                            digits_a[j] = BORROWED[digits_a[j]]
                            break

                        else:
                            digits_a[j] = BORROWED[digits_a[j]]
                            j += 1

                else:
                    i = len(digits_a)

            i += 1

            subtraction += sd

        if final_precision:
            subtraction = subtraction[0:final_precision] + '.' + subtraction[final_precision:]

        subtraction = subtraction[::-1]

        return subtraction

    def __add__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
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
            res = self.__subtraction(other_number)

            if abs(self) > abs(other_number) and res[0] != '-':
                res = '-' + res

        return Sezimal(res)

    def __radd__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__add__(self)

    def __sub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
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
            res = '-' + res

        return Sezimal(res)

    def __rsub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__sub__(self)

    def __round__(self, precision: IntegerSelf = MAX_PRECISION) -> Self:
        precision = SezimalInteger(precision)

        if self._precision <= int(precision):
            return self

        to_round = self._integer + '.' + self._fraction[:int(precision)]

        if self._sign == -1:
            to_round = '-' + to_round

        to_discard = self._fraction[int(precision):]

        if to_discard[0] in '345':
            adjust = Sezimal(f'1e-{precision}')

        elif to_discard.replace('0', '') == '':
            adjust = Sezimal(0)

        else:
            adjust = Sezimal(f'1e-{precision}') * -1

        rounded = Sezimal(to_round) + adjust

        if rounded._sign != self._sign:
            rounded = Sezimal(0)

        return rounded

    def trunc(self, precision: IntegerSelf = MAX_PRECISION) -> str:
        if precision is None:
            precision = 0

        precision = SezimalInteger(precision)

        if self._precision <= int(precision):
            return self

        to_round = self._integer + '.' + self._fraction[:int(precision)]

        if self._sign == -1:
            to_round = '-' + to_round

        return Sezimal(to_round)

    def is_integer(self) -> bool:
        return self == self.trunc(0)

    def _mult_div_finalizing(self):
        res = round(self, MAX_PRECISION)

        if str(res).endswith('5555'):
            res += Sezimal(f'1E-{decimal_to_sezimal(res._precision)}')

        return res

    def __multiplication(self, other_number: Self) -> str:
        if self == 0 or other_number == 0:
            return '0'

        if other_number == 1:
            return str(self)

        #
        # Multiplies two values;
        # the final sign of the operation is dealt with by the calling method: __mul__
        #
        MAP = {
            '0': {'0': '0', '1': '0', '2':  '0', '3':  '0', '4':  '0', '5':  '0'},
            '1': {'0': '0', '1': '1', '2':  '2', '3':  '3', '4':  '4', '5':  '5'},
            '2': {'0': '0', '1': '2', '2':  '4', '3': '10', '4': '12', '5': '14'},
            '3': {'0': '0', '1': '3', '2': '10', '3': '13', '4': '20', '5': '23'},
            '4': {'0': '0', '1': '4', '2': '12', '3': '20', '4': '24', '5': '32'},
            '5': {'0': '0', '1': '5', '2': '14', '3': '23', '4': '32', '5': '41'},
        }

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
                md = MAP[d1][d2]

                if carries != '0':
                    md = str(Sezimal(md) + carries)

                sums[-1] += md[-1]

                if len(md) != 1:
                    carries = md[0]
                else:
                    carries = '0'

            if carries != '0':
                sums[-1] += carries

        multiplication = Sezimal('0')

        for s in sums:
            if s:
                multiplication += Sezimal(s[::-1])

        multiplication = str(multiplication)

        if final_precision:
            multiplication = multiplication[::-1]

            if len(multiplication) < final_precision + 1:
                multiplication += '0' * (final_precision - len(multiplication) + 1)

            multiplication = multiplication[0:final_precision] + '.' + multiplication[final_precision:]
            multiplication = multiplication[::-1]

        return multiplication

    def __mul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
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

        return Sezimal(res)._mult_div_finalizing()

    def __rmul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__mul__(self)

    def __basic_division(self, dividend: Self, divisor: Self) -> list[Self]:
        remainder = dividend
        quotient = Sezimal('0')

        while remainder >= divisor:
            remainder -= divisor
            quotient += 1

        return quotient, remainder

    def new_division(self, dividend: Self, divisor: Self) -> list[Self]:
        if dividend < divisor:
            return Sezimal(0), dividend

        quotient = Sezimal('0')
        remainder = Sezimal(dividend._digits[0])

        for i in range(1, len(dividend._digits)):
            remainder *= 10
            remainder += Sezimal(dividend._digits[i])

            factor = Sezimal(0)

            while (divisor * (factor + 1)) < remainder:
                factor += 1

            quotient *= 10
            quotient += factor
            remainder -= divisor * factor

        return quotient, remainder

        # Convert quotient and remainder to strings
        remainder_str = ''
        while remainder:
            remainder_str += str(remainder % base)
            remainder //= base

        # Return quotient and remainder as strings
        return quotient_str, int(remainder_str[::-1])

    def __division(self, other_number: Self, max_precision: IntegerSelf = MAX_PRECISION) -> str:
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

        dividend = Sezimal(''.join(digits_a))
        divisor = Sezimal(''.join(digits_b))
        quotient, remainder = self.__basic_division(dividend, divisor)
        max_precision = max(final_precision, max_precision) * 2

        while remainder > 0 and final_precision < max_precision:
            dividend = remainder * 10
            final_precision += 1
            q, remainder = self.__basic_division(dividend, divisor)
            quotient = Sezimal(str(quotient) + str(q))

        division = str(quotient)

        final_precision -= initial_precision

        if final_precision:
            division = division[::-1]

            if len(division) < final_precision + 1:
                division += '0' * (final_precision - len(division) + 1)

            division = division[0:final_precision] + '.' + division[final_precision:]
            division = division[::-1]

        return division

    def __truediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        #
        # Deals with the signs
        #
        if self._sign == 1 and other_number._sign == 1:
            res = self.__division(other_number)

        elif self._sign == 1 and other_number._sign == -1:
            res = self.__division(other_number)
            res = '-' + res

        elif self._sign == -1 and other_number._sign == -1:
            res = self.__division(other_number)

        elif self._sign == -1 and other_number._sign == 1:
            res = self.__division(other_number)
            res = '-' + res

        return Sezimal(res)._mult_div_finalizing()

    def __rtruediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__truediv__(self)

    def __divmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> list[Self]:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        dividend = Sezimal(self._integer)
        divisor = Sezimal(other_number._integer)

        if divisor == 0:
            raise ZeroDivisionError('Division by zero')

        if divisor == 1:
            return dividend, Sezimal(0)

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

    def __floordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        quotient, remainder = self.__divmod__(other_number)
        return quotient

    def __rfloordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__floordiv__(self)

    def __mod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        quotient, remainder = self.__divmod__(other_number)
        return remainder

    def __rmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__mod__(self)

    def factorial(self) -> Self:
        if self == 0 or self == 1:
            return Sezimal(1)

        if self == 2:
            return Sezimal(2)

        integer = Sezimal(self._integer)
        next_integer = integer - 1

        return integer * next_integer.factorial()

    def calculus_exp(self) -> Self:
        result = Sezimal(1)
        term = Sezimal(1)
        i = Sezimal(1)

        while term > 0:
            term *= self * (Sezimal(1) / i)
            result += term
            i += 1

        return result

    def exp(self) -> Self:
        result = self.decimal.exp()
        result = Sezimal(result)
        return result._mult_div_finalizing()

    def calculus_ln(self) -> Self:
        result = Sezimal(0)

        if str(self) in LOGARITHM_TABLE:
            return Sezimal(LOGARITHM_TABLE[str(self)])._mult_div_finalizing()

        term = (self - 1) * (Sezimal(1) / self)

        i = Sezimal(1)

        while i <= 200:
            result += (term ** i) * (Sezimal(1) / i)
            i += 1

        return result

    def ln(self) -> Self:
        result = self.decimal.ln()
        result = Sezimal(result)
        return result._mult_div_finalizing()

    def __calculus_power(self, other_number: Self) -> Self:
        if other_number == 0:
            return Sezimal(1)

        if self == 0:
            return Sezimal(0)

        if other_number < 0:
            return Sezimal(1) / self.__power(other_number * -1)

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

    def __pow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__power(other_number)

    def __rpow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__pow__(self)

    def log(self) -> Self:
        with localcontext() as context:
            context.prec = int(MAX_PRECISION / 2)
            result = self.decimal.ln() / Decimal(6).ln()
            result = Sezimal(result)

        return result._mult_div_finalizing()

    def log2(self) -> Self:
        with localcontext() as context:
            context.prec = int(MAX_PRECISION / 2)
            result = self.decimal.ln() / Decimal(2).ln()
            result = Sezimal(result)

        return result._mult_div_finalizing()

    def log14(self) -> Self:
        with localcontext() as context:
            context.prec = int(MAX_PRECISION / 2)
            result = self.decimal.ln() / Decimal(10).ln()
            result = Sezimal(result)

        return result._mult_div_finalizing()

    def sqrt(self) -> Self:
        return self ** Sezimal('0.3')

    def _find_gcd(self, numerator: Self, denominator: Self) -> Self:
        if denominator == 0:
            return numerator

        return self._find_gcd(denominator, numerator % denominator)

    def as_integer_ratio(self):
        if self.is_integer():
            return SezimalInteger(self), SezimalInteger(1)

        numerator = Sezimal(self._integer + self._fraction)
        denominator = Sezimal(f'1e+{SezimalInteger(Decimal(self._precision))}')

        gcd = self._find_gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd

        return SezimalInteger(numerator), SezimalInteger(denominator)


class SezimalInteger(Sezimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits']

    def __init__(self, number: str | int | float | Decimal | Self | IntegerSelf) -> Self:
        original_decimal = None

        if type(number) == Decimal:
            original_decimal = number
            number = decimal_to_sezimal(str(number))

        cleaned_number = validate_clean_sezimal(number)

        if cleaned_number[0] == '-':
            cleaned_number = cleaned_number[1:]
            self._sign = -1
        else:
            self._sign = 1

        if '.' in cleaned_number:
            self._integer = str(int(cleaned_number.split('.')[0]))
            self._fraction = cleaned_number.split('.')[1].replace('0', '')
        else:
            self._integer = str(int(cleaned_number))
            self._fraction = ''

        self._precision = len(self._fraction)
        self._digits = list(self._integer + self._fraction)

        if self._precision:
            raise ValueError(f'The number {number} has an invalid format for a sezimal integer number')

        #
        # Converts and stores as decimal
        #
        if original_decimal is None:
            self._value = Decimal(sezimal_to_decimal(cleaned_number))
            self._value *= self._sign
        else:
            self._value = original_decimal

    def __repr__(self) -> str:
        return super().__repr__().replace('Sezimal', 'SezimalInteger')

    def __index__(self):
        return int(self._integer, 6)


class SezimalFraction(Sezimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', '_numerator', '_denominator', '_sezimal']

    def __init__(self, numerator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf, denominator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf = None) -> Self:
        if type(numerator) == str:
            if '/' in numerator:
                numerator, denominator = numerator.split('/')
            elif '⁄' in numerator:
                numerator, denominator = numerator.split('⁄')
            elif '÷' in numerator:
                numerator, denominator = numerator.split('÷')

        cleaned_numerator = validate_clean_sezimal(numerator)

        if denominator is None:
            numerator = Sezimal(cleaned_numerator)
            numerator, denominator = numerator.as_integer_ratio()
            cleaned_numerator = str(numerator)
            cleaned_denominator = str(denominator)

        else:
            cleaned_denominator = validate_clean_sezimal(denominator)

        self._numerator = Sezimal(cleaned_numerator)
        self._denominator = Sezimal(cleaned_denominator)
        self._sezimal = self._numerator / self._denominator

        super().__init__(self._sezimal)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @property
    def sezimal(self):
        return self._sezimal

    def __str__(self) -> str:
        if self._sign == -1:
            res = '-'
        else:
            res = ''


        res += str(self._numerator)
        res += '/'
        res += str(self._denominator)

        return res

    def __repr__(self) -> str:
        return f"SezimalFraction('{self._numerator.formatted_number}/{self._denominator.formatted_number}') == {self._sezimal.__repr__()}"


_numbers.Number.register(Sezimal)
_numbers.Integral.register(Sezimal)
_numbers.Rational.register(Sezimal)

_numbers.Number.register(SezimalInteger)
_numbers.Integral.register(SezimalInteger)

_numbers.Number.register(SezimalFraction)
_numbers.Integral.register(SezimalFraction)
