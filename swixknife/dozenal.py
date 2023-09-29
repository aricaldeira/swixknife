#
# __all__ = (
#     'Dozenal',
#     'DozenalInteger',
#     'DozenalFraction',
# )
#
#
# from decimal import Decimal, localcontext, getcontext
#
# from typing import TypeVar
# import numbers as _numbers
#
# Self = TypeVar('Self', bound='Dozenal')
# IntegerSelf = TypeVar('IntegerSelf', bound='DozenalInteger')
# FractionSelf = TypeVar('FractionSelf', bound='DozenalFraction')
#
#     # decimal_to_dozenal, dozenal_to_decimal, \
# from .base import validate_clean_dozenal, \
#     dozenal_format, decimal_format
#
# MAX_DECIMAL_PRECISION = 37
# getcontext().prec = MAX_DECIMAL_PRECISION
# MAX_PRECISION = 120
#
#
# class Dozenal:
#     __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', 'reciprocal']
#
#     def __init__(self, number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         original_decimal = None
#
#         if type(number) == Decimal:
#             original_decimal = number
#             number = decimal_to_dozenal(str(number))
#
#         elif type(number) == DozenalFraction:
#             number = number.dozenal
#
#         elif type(number) == str and ('/' in number or '⁄' in number or '÷' in number):
#             number = DozenalFraction(number).dozenal
#
#         cleaned_number = validate_clean_dozenal(number)
#
#         if cleaned_number[0] == '-':
#             cleaned_number = cleaned_number[1:]
#             self._sign = -1
#         else:
#             self._sign = 1
#
#         if '.' in cleaned_number:
#             self._integer = str(int(cleaned_number.split('.')[0]))
#             self._fraction = cleaned_number.split('.')[1]
#         else:
#             self._integer = str(int(cleaned_number))
#             self._fraction = ''
#
#         self._precision = len(self._fraction)
#         self._digits = list(self._integer + self._fraction)
#
#         #
#         # Converts and stores as decimal
#         #
#         if original_decimal is None:
#             with localcontext() as context:
#                 context.prec = MAX_DECIMAL_PRECISION
#                 self._value = Decimal(dozenal_to_decimal(cleaned_number)) ## .quantize(Decimal(f'1E-{_DECIMAL_PRECISION}'))
#                 self._value *= self._sign
#
#         else:
#             self._value = original_decimal
#
#     def __str__(self) -> str:
#         if self._sign == -1:
#             res = '-' + self._integer
#         else:
#             res = self._integer
#
#         if self._precision:
#             res += '.'
#             res += self._fraction
#
#         return res
#
#     def __repr__(self) -> str:
#         if not self._fraction:
#             return f"Dozenal('{self.formatted_number}') == Decimal('{decimal_format(self.decimal, decimal_places=0)}')"
#         else:
#             return f"Dozenal('{self.formatted_number}') == Decimal('{decimal_format(self.decimal, decimal_places=MAX_DECIMAL_PRECISION)}')"
#
#     @property
#     def formatted_number(self) -> str:
#         return dozenal_format(str(self), dozenal_places=Decimal(self._precision))
#
#     @property
#     def decimal(self) -> Decimal:
#         return self._value
#
#     @property
#     def decimal_formatted_number(self) -> str:
#         if not self._fraction:
#             return decimal_format(str(self._value), decimal_places=0)
#         else:
#             return decimal_format(str(self._value), decimal_places=MAX_DECIMAL_PRECISION)
#
#     @property
#     def sezimal(self) -> str:
#         if not self._fraction:
#             return sezimal_format(self, sezimal_places=0, group_separator='')
#         else:
#             return sezimal_format(self, group_separator='')
#
#     @property
#     def sezimal_formatted_number(self) -> str:
#         if not self._fraction:
#             return sezimal_format(self, sezimal_places=0)
#         else:
#             return sezimal_format(self)
#
#     @property
#     def niftimal(self) -> str:
#         if not self._fraction:
#             return niftimal_format(self, niftimal_places=0, group_separator='')
#         else:
#             return niftimal_format(self, group_separator='')
#
#     @property
#     def niftimal_formatted_number(self) -> str:
#         if not self._fraction:
#             return niftimal_format(self, niftimal_places=0)
#         else:
#             return niftimal_format(self)
#
#     def __int__(self) -> int:
#         return int(dozenal_to_decimal(self._integer)) * self._sign
#
#     def __trunc__(self) -> IntegerSelf:
#         return DozenalInteger(self._integer) * self._sign
#
#     def __float__(self) -> float:
#         return float(dozenal_to_decimal(str(self)))
#
#     def __decimal__(self) -> Decimal:
#         return self._value
#
#     def __compare__(self, other_number: Self) -> IntegerSelf:
#         #
#         # If the sign of both numbers are not equal,
#         # they can be compared only by their sign
#         #
#         if self._sign != other_number._sign:
#             return self._sign
#
#         #
#         # The signs are the same, let’s check the numbers
#         #
#         precision = max(self._precision, other_number._precision)
#
#         this = str(self._integer) + str(self._fraction).ljust(precision, '0')
#         other = str(other_number._integer) + str(other_number._fraction).ljust(precision, '0')
#
#         length = max(len(this), len(other))
#
#         this = this.rjust(length, '0')
#         other = other.rjust(length, '0')
#
#         if this == other:
#             return 0
#
#         if self._sign == 1:
#             return 1 if this > other else -1
#         else:
#             return -1 if this > other else 1
#
#     def __eq__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return self.__compare__(other_number) == 0
#
#     def __ne__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
#         return not self.__eq__(other_number)
#
#     def __lt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return self.__compare__(other_number) < 0
#
#     def __ge__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
#         return not self.__lt__(other_number)
#
#     def __gt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return self.__compare__(other_number) > 0
#
#     def __le__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> bool:
#         return not self.__gt__(other_number)
#
#     def __hash__(self):
#         return self.decimal.__hash__()
#
#     def __bool__(self) -> bool:
#         return not self == 0
#
#     def __pos__(self) -> Self:
#         return Dozenal(self)
#
#     def __neg__(self) -> Self:
#         return Dozenal(self * -1)
#
#     def __abs__(self) -> Self:
#         if self._sign == 1:
#             return Dozenal(self)
#
#         return Dozenal(self * -1)
#
#     def __addition(self, other_number: Self) -> str:
#         if other_number == 0:
#             return str(self)
#
#         #
#         # Adds two values;
#         # the final sign of the operation is dealt with by the calling method: __add__ or __sub__
#         #
#         MAP = {
#             '0': {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '↊': '↊', '↋': '↋', '10': '10', '11': '11', '12': '12', '13': '13', '14': '14', '15': '15', '16': '16', '17': '17', '18': '18', '19': '19', '1↊': '1↊'},
#             '1': {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '↊', '↊': '↋', '↋': '10', '10': '11', '11': '12', '12': '13', '13': '14', '14': '15', '15': '16', '16': '17', '17': '18', '18': '19', '19': '1↊', '1↊': '1↋'},
#             '2': {'0': '2', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8', '7': '9', '8': '↊', '9': '↋', '↊': '10', '↋': '11', '10': '12', '11': '13', '12': '14', '13': '15', '14': '16', '15': '17', '16': '18', '17': '19', '18': '1↊', '19': '1↋', '1↊': '20'},
#             '3': {'0': '3', '1': '4', '2': '5', '3': '6', '4': '7', '5': '8', '6': '9', '7': '↊', '8': '↋', '9': '10', '↊': '11', '↋': '12', '10': '13', '11': '14', '12': '15', '13': '16', '14': '17', '15': '18', '16': '19', '17': '1↊', '18': '1↋', '19': '20', '1↊': '21'},
#             '4': {'0': '4', '1': '5', '2': '6', '3': '7', '4': '8', '5': '9', '6': '↊', '7': '↋', '8': '10', '9': '11', '↊': '12', '↋': '13', '10': '14', '11': '15', '12': '16', '13': '17', '14': '18', '15': '19', '16': '1↊', '17': '1↋', '18': '20', '19': '21', '1↊': '22'},
#             '5': {'0': '5', '1': '6', '2': '7', '3': '8', '4': '9', '5': '↊', '6': '↋', '7': '10', '8': '11', '9': '12', '↊': '13', '↋': '14', '10': '15', '11': '16', '12': '17', '13': '18', '14': '19', '15': '1↊', '16': '1↋', '17': '20', '18': '21', '19': '22', '1↊': '23'},
#             '6': {'0': '6', '1': '7', '2': '8', '3': '9', '4': '↊', '5': '↋', '6': '10', '7': '11', '8': '12', '9': '13', '↊': '14', '↋': '15', '10': '16', '11': '17', '12': '18', '13': '19', '14': '1↊', '15': '1↋', '16': '20', '17': '21', '18': '22', '19': '23', '1↊': '24'},
#             '7': {'0': '7', '1': '8', '2': '9', '3': '↊', '4': '↋', '5': '10', '6': '11', '7': '12', '8': '13', '9': '14', '↊': '15', '↋': '16', '10': '17', '11': '18', '12': '19', '13': '1↊', '14': '1↋', '15': '20', '16': '21', '17': '22', '18': '23', '19': '24', '1↊': '25'},
#             '8': {'0': '8', '1': '9', '2': '↊', '3': '↋', '4': '10', '5': '11', '6': '12', '7': '13', '8': '14', '9': '15', '↊': '16', '↋': '17', '10': '18', '11': '19', '12': '1↊', '13': '1↋', '14': '20', '15': '21', '16': '22', '17': '23', '18': '24', '19': '25', '1↊': '26'},
#             '9': {'0': '9', '1': '↊', '2': '↋', '3': '10', '4': '11', '5': '12', '6': '13', '7': '14', '8': '15', '9': '16', '↊': '17', '↋': '18', '10': '19', '11': '1↊', '12': '1↋', '13': '20', '14': '21', '15': '22', '16': '23', '17': '24', '18': '25', '19': '26', '1↊': '27'},
#             '↊': {'0': '↊', '1': '↋', '2': '10', '3': '11', '4': '12', '5': '13', '6': '14', '7': '15', '8': '16', '9': '17', '↊': '18', '↋': '19', '10': '1↊', '11': '1↋', '12': '20', '13': '21', '14': '22', '15': '23', '16': '24', '17': '25', '18': '26', '19': '27', '1↊': '28'},
#             '↋': {'0': '↋', '1': '10', '2': '11', '3': '12', '4': '13', '5': '14', '6': '15', '7': '16', '8': '17', '9': '18', '↊': '19', '↋': '1↊', '10': '1↋', '11': '20', '12': '21', '13': '22', '14': '23', '15': '24', '16': '25', '17': '26', '18': '27', '19': '28', '1↊': '29'},
#         }
#
#         digits_a = list(self._digits)
#         digits_b = list(other_number._digits)
#
#         #
#         # Normalizes the fractional part between the two values,
#         #
#         if self._precision > other_number._precision:
#             digits_b += list('0' * (self._precision - other_number._precision))
#             final_precision = self._precision
#
#         elif other_number._precision > self._precision:
#             digits_a += list('0' * (other_number._precision - self._precision))
#             final_precision = other_number._precision
#
#         else:
#             final_precision = self._precision
#
#         digits_a = digits_a[::-1]
#         digits_b = digits_b[::-1]
#
#         adition = ''
#         carries = '0'
#
#         for i in range(max(len(digits_a), len(digits_b))):
#             if i + 1 <= len(digits_a):
#                 d1 = digits_a[i]
#             else:
#                 d1 = '0'
#
#             if i + 1 <= len(digits_b):
#                 d2 = digits_b[i]
#             else:
#                 d2 = '0'
#
#             sd = MAP[d1][d2]
#             sd = MAP[carries][sd]
#
#             adition += sd[-1]
#
#             if len(sd) > 1:
#                 carries = sd[0]
#             else:
#                 carries = '0'
#
#         if carries != '0':
#             adition += carries
#
#         if final_precision:
#             adition = adition[0:final_precision] + '.' + adition[final_precision:]
#
#         adition = adition[::-1]
#
#         return adition
#
#     def __subtraction(self, other_number: Self) -> str:
#         if other_number == 0:
#             return str(self)
#
#         #
#         # Subtracts the lesser value from the greater one;
#         # the final sign of the operation is dealt with by the calling method: __add__ or __sub__
#         #
#         MAP = {
#             '0': {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '↊': '↊', '↋': '↋'},
#             '1': {'0': '1', '1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '↊': '9', '↋': '↊'},
#             '2': {'0': '2', '1': '1', '2': '0', '3': '1', '4': '2', '5': '3', '6': '4', '7': '5', '8': '6', '9': '7', '↊': '8', '↋': '9'},
#             '3': {'0': '3', '1': '2', '2': '1', '3': '0', '4': '1', '5': '2', '6': '3', '7': '4', '8': '5', '9': '6', '↊': '7', '↋': '8'},
#             '4': {'0': '4', '1': '3', '2': '2', '3': '1', '4': '0', '5': '1', '6': '2', '7': '3', '8': '4', '9': '5', '↊': '6', '↋': '7'},
#             '5': {'0': '5', '1': '4', '2': '3', '3': '2', '4': '1', '5': '0', '6': '1', '7': '2', '8': '3', '9': '4', '↊': '5', '↋': '6'},
#             '6': {'0': '6', '1': '5', '2': '4', '3': '3', '4': '2', '5': '1', '6': '0', '7': '1', '8': '2', '9': '3', '↊': '4', '↋': '5'},
#             '7': {'0': '7', '1': '6', '2': '5', '3': '4', '4': '3', '5': '2', '6': '1', '7': '0', '8': '1', '9': '2', '↊': '3', '↋': '4'},
#             '8': {'0': '8', '1': '7', '2': '6', '3': '5', '4': '4', '5': '3', '6': '2', '7': '1', '8': '0', '9': '1', '↊': '2', '↋': '3'},
#             '9': {'0': '9', '1': '8', '2': '7', '3': '6', '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0', '↊': '1', '↋': '2'},
#             '↊': {'0': '↊', '1': '9', '2': '8', '3': '7', '4': '6', '5': '5', '6': '4', '7': '3', '8': '2', '9': '1', '↊': '0', '↋': '1'},
#             '↋': {'0': '↋', '1': '↊', '2': '9', '3': '8', '4': '7', '5': '6', '6': '5', '7': '4', '8': '3', '9': '2', '↊': '1', '↋': '0'},
#             '10': {'0': '10', '1': '↋', '2': '↊', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3', '↊': '2', '↋': '1'},
#             '11': {'0': '11', '1': '10', '2': '↋', '3': '↊', '4': '9', '5': '8', '6': '7', '7': '6', '8': '5', '9': '4', '↊': '3', '↋': '2'},
#             '12': {'0': '12', '1': '11', '2': '10', '3': '↋', '4': '↊', '5': '9', '6': '8', '7': '7', '8': '6', '9': '5', '↊': '4', '↋': '3'},
#             '13': {'0': '13', '1': '12', '2': '11', '3': '10', '4': '↋', '5': '↊', '6': '9', '7': '8', '8': '7', '9': '6', '↊': '5', '↋': '4'},
#             '14': {'0': '14', '1': '13', '2': '12', '3': '11', '4': '10', '5': '↋', '6': '↊', '7': '9', '8': '8', '9': '7', '↊': '6', '↋': '5'},
#             '15': {'0': '15', '1': '14', '2': '13', '3': '12', '4': '11', '5': '10', '6': '↋', '7': '↊', '8': '9', '9': '8', '↊': '7', '↋': '6'},
#             '16': {'0': '16', '1': '15', '2': '14', '3': '13', '4': '12', '5': '11', '6': '10', '7': '↋', '8': '↊', '9': '9', '↊': '8', '↋': '7'},
#             '17': {'0': '17', '1': '16', '2': '15', '3': '14', '4': '13', '5': '12', '6': '11', '7': '10', '8': '↋', '9': '↊', '↊': '9', '↋': '8'},
#             '18': {'0': '18', '1': '17', '2': '16', '3': '15', '4': '14', '5': '13', '6': '12', '7': '11', '8': '10', '9': '↋', '↊': '↊', '↋': '9'},
#             '19': {'0': '19', '1': '18', '2': '17', '3': '16', '4': '15', '5': '14', '6': '13', '7': '12', '8': '11', '9': '10', '↊': '↋', '↋': '↊'},
#             '1↊': {'0': '1↊', '1': '19', '2': '18', '3': '17', '4': '16', '5': '15', '6': '14', '7': '13', '8': '12', '9': '11', '↊': '10', '↋': '↋'},
#             '1↋': {'0': '1↋', '1': '1↊', '2': '19', '3': '18', '4': '17', '5': '16', '6': '15', '7': '14', '8': '13', '9': '12', '↊': '11', '↋': '10'},
#         }
#
#         BORROWED = {
#             '0': '↋',
#             '1': '0',
#             '2': '1',
#             '3': '2',
#             '4': '3',
#             '5': '4',
#             '6': '5',
#             '7': '6',
#             '8': '7',
#             '9': '8',
#             '↊': '9',
#             '↋': '↊',
#         }
#
#         digits_a = list(self._digits)
#         digits_b = list(other_number._digits)
#
#         #
#         # Normalizes the fractional part between the two values,
#         #
#         if self._precision > other_number._precision:
#             digits_b += list('0' * (self._precision - other_number._precision))
#             final_precision = self._precision
#
#         elif other_number._precision > self._precision:
#             digits_a += list('0' * (other_number._precision - self._precision))
#             final_precision = other_number._precision
#
#         else:
#             final_precision = self._precision
#
#         digits_a = digits_a[::-1]
#         digits_b = digits_b[::-1]
#
#         if abs(self) < abs(other_number):
#             d = digits_a
#             digits_a = digits_b
#             digits_b = d
#
#         subtraction = ''
#
#         i = 0
#         while i < len(digits_a):
#             d1 = digits_a[i]
#
#             if i + 1 <= len(digits_b):
#                 d2 = digits_b[i]
#             else:
#                 d2 = '0'
#
#             if d1 >= d2:
#                 sd = MAP[d1][d2]
#
#             #
#             # Vay presizar enprestar 1?
#             #
#             else:
#                 d1 = '1' + d1
#                 sd = MAP[d1][d2]
#
#                 #
#                 # Trata u enpréstimu nus prósimus díjitus,
#                 # kuydandu ki u 0 propaga u enpréstimu uma kaza
#                 # pra frenti
#                 #
#                 if len(digits_a) >= i + 1:
#                     j = i + 1
#
#                     while j < len(digits_a):
#                         if digits_a[j] != '0':
#                             digits_a[j] = BORROWED[digits_a[j]]
#                             break
#
#                         else:
#                             digits_a[j] = BORROWED[digits_a[j]]
#                             j += 1
#
#                 else:
#                     i = len(digits_a)
#
#             i += 1
#
#             subtraction += sd
#
#         if final_precision:
#             subtraction = subtraction[0:final_precision] + '.' + subtraction[final_precision:]
#
#         subtraction = subtraction[::-1]
#
#         return subtraction
#
#     def __add__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         #
#         # Deals with the signs, and does the adition or subtraction accordingly
#         #
#         if self._sign == 1 and other_number._sign == 1:
#             res = self.__addition(other_number)
#
#         elif self._sign == 1 and other_number._sign == -1:
#             res = self.__subtraction(other_number)
#
#             if abs(other_number) > abs(self) and res[0] != '-':
#                 res = '-' + res
#
#         elif self._sign == -1 and other_number._sign == -1:
#             res = self.__addition(other_number)
#             res = '-' + res
#
#         elif self._sign == -1 and other_number._sign == 1:
#             res = other_number.__subtraction(self)
#
#             if abs(self) > abs(other_number) and res[0] != '-':
#                res = '-' + res
#
#         return Dozenal(res)
#
#     def __radd__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return other_number.__add__(self)
#
#     def __sub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         #
#         # Deals with the signs, and does the adition or subtraction accordingly
#         #
#         if self._sign == 1 and other_number._sign == 1:
#             res = self.__subtraction(other_number)
#
#             if abs(other_number) > abs(self) and res[0] != '-':
#                 res = '-' + res
#
#         elif self._sign == 1 and other_number._sign == -1:
#             res = self.__addition(other_number)
#
#         elif self._sign == -1 and other_number._sign == -1:
#             res = self.__subtraction(other_number)
#
#             if abs(self) > abs(other_number) and res[0] != '-':
#                 res = '-' + res
#
#         elif self._sign == -1 and other_number._sign == 1:
#             res = self.__addition(other_number)
#             res = '-' + res
#
#         return Dozenal(res)
#
#     def __rsub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return other_number.__sub__(self)
#
#     def __round_half_up__(self, precision: IntegerSelf, last_digit: str, next_digit: str, to_discard: str) -> Self:
#         adjust = Dozenal(0)
#
#         if next_digit == '6':
#             if to_discard.replace('0', '') != '':
#                 adjust = Dozenal(f'1e-{precision}') * self._sign
#             elif last_digit in '13579↋':
#                 adjust = Dozenal(f'1e-{precision}') * self._sign
#
#         elif next_digit in '789↊↋':
#             adjust = Dozenal(f'1e-{precision}') * self._sign
#
#         return adjust
#
#     def __round_half_down__(self, precision: IntegerSelf, last_digit: str, next_digit: str, to_discard: str) -> Self:
#         adjust = Dozenal(0)
#
#         if next_digit == '6':
#             if to_discard.replace('0', '') != '':
#                 adjust = Dozenal(f'1e-{precision}') * self._sign
#
#         elif next_digit in '789↊↋':
#             adjust = Dozenal(f'1e-{precision}') * self._sign
#
#         return adjust
#
#     def __round__(self, precision: IntegerSelf = MAX_PRECISION) -> Self:
#         precision = DozenalInteger(precision)
#
#         if self._precision <= int(precision):
#             return self
#
#         to_round = self._integer + '.' + self._fraction[:int(precision)]
#
#         if self._sign == -1:
#             to_round = '-' + to_round
#
#         if precision == 0:
#             last_digit = self._integer[-1]
#             next_digit = self._fraction[0]
#             to_discard = self._fraction[1:]
#
#         else:
#             last_digit = self._fraction[int(precision) - 1]
#             next_digit = self._fraction[int(precision)]
#             to_discard = self._fraction[int(precision) + 1:]
#
#         adjust = self.__round_half_up__(precision, last_digit, next_digit, to_discard)
#
#         rounded = Dozenal(to_round) + adjust
#
#         if rounded._sign != self._sign:
#             rounded = Dozenal(0)
#
#         return rounded
#
#     def trunc(self, precision: IntegerSelf = MAX_PRECISION) -> Self:
#         if precision is None:
#             precision = 0
#
#         precision = DozenalInteger(precision)
#
#         if self._precision <= int(precision):
#             return self
#
#         to_round = self._integer + '.' + self._fraction[:int(precision)]
#
#         if self._sign == -1:
#             to_round = '-' + to_round
#
#         return Dozenal(to_round)
#
#     def is_integer(self) -> bool:
#         return self == self.trunc(0)
#
#     def _mult_div_finalizing(self):
#         res = round(self, MAX_PRECISION)
#
#         if str(res).endswith('↋↋↋↋'):
#             res += Dozenal(f'1E-{decimal_to_dozenal(res._precision)}')
#
#         return res
#
#     def __multiplication(self, other_number: Self) -> str:
#         if self == 0 or other_number == 0:
#             return '0'
#
#         if other_number == 1:
#             return str(self)
#
#         #
#         # Multiplies two values;
#         # the final sign of the operation is dealt with by the calling method: __mul__
#         #
#         MAP = {
#             '0': {'0': '0', '1': '0', '2':  '0', '3':  '0', '4':  '0', '5':  '0'},
#             '1': {'0': '0', '1': '1', '2':  '2', '3':  '3', '4':  '4', '5':  '5'},
#             '2': {'0': '0', '1': '2', '2':  '4', '3': '10', '4': '12', '5': '14'},
#             '3': {'0': '0', '1': '3', '2': '10', '3': '13', '4': '20', '5': '23'},
#             '4': {'0': '0', '1': '4', '2': '12', '3': '20', '4': '24', '5': '32'},
#             '5': {'0': '0', '1': '5', '2': '14', '3': '23', '4': '32', '5': '41'},
#         }
#
#         digits_a = list(self._digits)[::-1]
#         digits_b = list(other_number._digits)[::-1]
#         final_precision = self._precision + other_number._precision
#         sums = []
#
#         i = 0
#         for d1 in digits_a:
#             carries = '0'
#             sums.append('0' * i)
#             i += 1
#
#             for d2 in digits_b:
#                 md = MAP[d1][d2]
#
#                 if carries != '0':
#                     md = str(Dozenal(md) + carries)
#
#                 sums[-1] += md[-1]
#
#                 if len(md) != 1:
#                     carries = md[0]
#                 else:
#                     carries = '0'
#
#             if carries != '0':
#                 sums[-1] += carries
#
#         multiplication = Dozenal('0')
#
#         for s in sums:
#             if s:
#                 multiplication += Dozenal(s[::-1])
#
#         multiplication = str(multiplication)
#
#         if final_precision:
#             multiplication = multiplication[::-1]
#
#             if len(multiplication) < final_precision + 1:
#                 multiplication += '0' * (final_precision - len(multiplication) + 1)
#
#             multiplication = multiplication[0:final_precision] + '.' + multiplication[final_precision:]
#             multiplication = multiplication[::-1]
#
#         return multiplication
#
#     def __mul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         #
#         # Deals with the signs
#         #
#         if self._sign == 1 and other_number._sign == 1:
#             res = self.__multiplication(other_number)
#
#         elif self._sign == 1 and other_number._sign == -1:
#             res = self.__multiplication(other_number)
#             res = '-' + res
#
#         elif self._sign == -1 and other_number._sign == -1:
#             res = self.__multiplication(other_number)
#
#         elif self._sign == -1 and other_number._sign == 1:
#             res = self.__multiplication(other_number)
#             res = '-' + res
#
#         return Dozenal(res)._mult_div_finalizing()
#
#     def __rmul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return other_number.__mul__(self)
#
#     def __basic_division(self, dividend: Self, divisor: Self) -> tuple[Self]:
#         remainder = dividend
#         quotient = Dozenal('0')
#
#         while remainder >= divisor:
#             remainder -= divisor
#             quotient += 1
#
#         return quotient, remainder
#
#     def new_division(self, dividend: Self, divisor: Self) -> tuple[Self]:
#         if dividend < divisor:
#             return Dozenal(0), dividend
#
#         quotient = Dozenal('0')
#         remainder = Dozenal(dividend._digits[0])
#
#         for i in range(1, len(dividend._digits)):
#             remainder *= 10
#             remainder += Dozenal(dividend._digits[i])
#
#             factor = Dozenal(0)
#
#             while (divisor * (factor + 1)) < remainder:
#                 factor += 1
#
#             quotient *= 10
#             quotient += factor
#             remainder -= divisor * factor
#
#         return quotient, remainder
#
#         # # Convert quotient and remainder to strings
#         # remainder_str = ''
#         # while remainder:
#         #     remainder_str += str(remainder % base)
#         #     remainder //= base
#         #
#         # # Return quotient and remainder as strings
#         # return quotient_str, int(remainder_str[::-1])
#
#     def __division(self, other_number: Self, max_precision: IntegerSelf = MAX_PRECISION) -> str:
#         #
#         # Divides two values;
#         # the final sign of the operation is dealt with by the calling method: __div__
#         #
#         if other_number == 0:
#             raise ZeroDivisionError('Division by zero')
#
#         if self == 0:
#             return '0'
#
#         if other_number == 1:
#             return str(self)
#
#         max_precision = int(DozenalInteger(max_precision))
#
#         digits_a = list(self._digits)
#         digits_b = list(other_number._digits)
#
#         #
#         # Normalizes the fractional part between the two values,
#         #
#         if self._precision > other_number._precision:
#             digits_b += list('0' * (self._precision - other_number._precision))
#             final_precision = self._precision
#
#         elif other_number._precision > self._precision:
#             digits_a += list('0' * (other_number._precision - self._precision))
#             final_precision = other_number._precision
#
#         else:
#             final_precision = self._precision
#
#         initial_precision = final_precision
#
#         dividend = Dozenal(''.join(digits_a))
#         divisor = Dozenal(''.join(digits_b))
#         quotient, remainder = self.__basic_division(dividend, divisor)
#         max_precision = max(final_precision, max_precision) * 2
#
#         while remainder > 0 and final_precision < max_precision:
#             dividend = remainder * 10
#             final_precision += 1
#             q, remainder = self.__basic_division(dividend, divisor)
#             quotient = Dozenal(str(quotient) + str(q))
#
#         division = str(quotient)
#
#         final_precision -= initial_precision
#
#         if final_precision:
#             division = division[::-1]
#
#             if len(division) < final_precision + 1:
#                 division += '0' * (final_precision - len(division) + 1)
#
#             division = division[0:final_precision] + '.' + division[final_precision:]
#             division = division[::-1]
#
#         return division
#
#     def __truediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         #
#         # Calculate the reciprocal first
#         #
#         if hasattr(other_number, 'reciprocal'):
#             reciprocal = other_number.reciprocal
#         else:
#             reciprocal = Dozenal('1').__division(other_number) * other_number._sign
#
#         return self * reciprocal
#
#         # #
#         # # Deals with the signs
#         # #
#         # if self._sign == 1 and other_number._sign == 1:
#         #     res = self.__division(other_number)
#         #
#         # elif self._sign == 1 and other_number._sign == -1:
#         #     res = self.__division(other_number)
#         #     res = '-' + res
#         #
#         # elif self._sign == -1 and other_number._sign == -1:
#         #     res = self.__division(other_number)
#         #
#         # elif self._sign == -1 and other_number._sign == 1:
#         #     res = self.__division(other_number)
#         #     res = '-' + res
#         #
#         # return Dozenal(res)._mult_div_finalizing()
#
#     def __rtruediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return other_number.__truediv__(self)
#
#     def __divmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> tuple[Self]:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         dividend = Dozenal(self._integer)
#         divisor = Dozenal(other_number._integer)
#
#         if divisor == 0:
#             raise ZeroDivisionError('Division by zero')
#
#         if divisor == 1:
#             return dividend, Dozenal(0)
#
#         quotient, remainder = self.__basic_division(dividend, divisor)
#
#         if self._sign == 1 and other_number._sign == 1:
#             pass
#
#         elif self._sign == 1 and other_number._sign == -1:
#             quotient *= -1
#             remainder *= -1
#
#             if remainder != 0:
#                 quotient -= 1
#                 remainder = dividend + (quotient * divisor)
#
#         elif self._sign == -1 and other_number._sign == -1:
#             remainder *= -1
#
#         elif self._sign == -1 and other_number._sign == 1:
#             quotient *= -1
#
#             if remainder != 0:
#                 quotient -= 1
#                 remainder = (dividend + (quotient * divisor)) * -1
#
#         return quotient, remainder
#
#     def __floordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         quotient, remainder = self.__divmod__(other_number)
#         return quotient
#
#     def __rfloordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return other_number.__floordiv__(self)
#
#     def __mod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         quotient, remainder = self.__divmod__(other_number)
#         return remainder
#
#     def __rmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return other_number.__mod__(self)
#
#     def factorial(self) -> Self:
#         if self == 0 or self == 1:
#             return Dozenal(1)
#
#         if self == 2:
#             return Dozenal(2)
#
#         integer = Dozenal(self._integer)
#         next_integer = integer - 1
#
#         return integer * next_integer.factorial()
#
#     def calculus_exp(self) -> Self:
#         result = Dozenal(1)
#         term = Dozenal(1)
#         i = Dozenal(1)
#
#         while term > 0:
#             term *= self * (Dozenal(1) / i)
#             result += term
#             i += 1
#
#         return result
#
#     def exp(self) -> Self:
#         result = self.decimal.exp()
#         result = Dozenal(result)
#         return result._mult_div_finalizing()
#
#     # def calculus_ln(self) -> Self:
#     #     result = Dozenal(0)
#     #
#     #     if str(self) in LOGARITHM_TABLE:
#     #         return Dozenal(LOGARITHM_TABLE[str(self)])._mult_div_finalizing()
#     #
#     #     term = (self - 1) * (Dozenal(1) / self)
#     #
#     #     i = Dozenal(1)
#     #
#     #     while i <= 200:
#     #         result += (term ** i) * (Dozenal(1) / i)
#     #         i += 1
#     #
#     #     return result
#
#     def ln(self) -> Self:
#         result = self.decimal.ln()
#         result = Dozenal(result)
#         return result._mult_div_finalizing()
#
#     def __calculus_power(self, other_number: Self) -> Self:
#         if other_number == 0:
#             return Dozenal(1)
#
#         if self == 0:
#             return Dozenal(0)
#
#         if other_number < 0:
#             return Dozenal(1) / self.__power(other_number * -1)
#
#         if other_number.is_integer():
#             result = self
#
#             while other_number > 1:
#                 result *= self
#                 other_number -= 1
#
#         else:
#             result = self.ln() * other_number
#             result = result.exp()
#
#         return result
#
#     def __power(self, other_number: Self) -> Self:
#         #
#         # When the exponent is an integer,
#         # avoid loosing precision in the decimal conversion,
#         #
#         if other_number.is_integer():
#             result = self
#
#             negative = other_number < 0
#
#             if negative:
#                 other_number *= -1
#
#             while other_number > 1:
#                 result *= self
#                 other_number -= 1
#
#             if negative:
#                 return 1 / result
#
#             return result
#
#         result = self.decimal ** other_number.decimal
#         result = Dozenal(result)
#         return result._mult_div_finalizing()
#
#     def __pow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return self.__power(other_number)
#
#     def __rpow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf) -> Self:
#         if type(other_number) != Dozenal:
#             other_number = Dozenal(other_number)
#
#         return other_number.__pow__(self)
#
#     def log(self) -> Self:
#         with localcontext() as context:
#             context.prec = int(MAX_PRECISION / 2)
#             result = self.decimal.ln() / Decimal(6).ln()
#             result = Dozenal(result)
#
#         return result._mult_div_finalizing()
#
#     def log2(self) -> Self:
#         with localcontext() as context:
#             context.prec = int(MAX_PRECISION / 2)
#             result = self.decimal.ln() / Decimal(2).ln()
#             result = Dozenal(result)
#
#         return result._mult_div_finalizing()
#
#     def log14(self) -> Self:
#         with localcontext() as context:
#             context.prec = int(MAX_PRECISION / 2)
#             result = self.decimal.ln() / Decimal(10).ln()
#             result = Dozenal(result)
#
#         return result._mult_div_finalizing()
#
#     def sqrt(self) -> Self:
#         return self ** Dozenal('0.3')
#
#     def _find_gcd(self, numerator: Self, denominator: Self) -> Self:
#         if denominator == 0:
#             return numerator
#
#         return self._find_gcd(denominator, numerator % denominator)
#
#     def as_integer_ratio(self):
#         if self.is_integer():
#             return DozenalInteger(self), DozenalInteger(1)
#
#         numerator = Dozenal(self._integer + self._fraction)
#         denominator = Dozenal(f'1e+{DozenalInteger(Decimal(self._precision))}')
#
#         gcd = self._find_gcd(numerator, denominator)
#         numerator //= gcd
#         denominator //= gcd
#
#         return DozenalInteger(numerator), DozenalInteger(denominator)
#
#
# class DozenalInteger(Dozenal):
#     __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits']
#
#     def __init__(self, number: str | int | float | Decimal | Self | IntegerSelf) -> Self:
#         original_decimal = None
#
#         if type(number) == Decimal:
#             original_decimal = number
#             number = decimal_to_dozenal(str(number))
#
#         cleaned_number = validate_clean_dozenal(number)
#
#         if cleaned_number[0] == '-':
#             cleaned_number = cleaned_number[1:]
#             self._sign = -1
#         else:
#             self._sign = 1
#
#         if '.' in cleaned_number:
#             self._integer = str(int(cleaned_number.split('.')[0]))
#             # self._fraction = cleaned_number.split('.')[1].replace('0', '')
#             self._fraction = ''
#         else:
#             self._integer = str(int(cleaned_number))
#             self._fraction = ''
#
#         self._precision = len(self._fraction)
#         self._digits = list(self._integer + self._fraction)
#
#         if self._precision:
#             raise ValueError(f'The number {number} has an invalid format for a dozenal integer number')
#
#         #
#         # Converts and stores as decimal
#         #
#         if original_decimal is None:
#             self._value = Decimal(dozenal_to_decimal(cleaned_number))
#             self._value *= self._sign
#         else:
#             self._value = original_decimal
#
#     def __repr__(self) -> str:
#         return super().__repr__().replace('Dozenal', 'DozenalInteger')
#
#     def __index__(self):
#         return int(self._integer, 6)
#
#
# class DozenalFraction(Dozenal):
#     __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', '_numerator', '_denominator', '_dozenal']
#
#     def __init__(self, numerator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf, denominator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf = None) -> Self:
#         if type(numerator) == str:
#             if '/' in numerator:
#                 numerator, denominator = numerator.split('/')
#             elif '⁄' in numerator:
#                 numerator, denominator = numerator.split('⁄')
#             elif '÷' in numerator:
#                 numerator, denominator = numerator.split('÷')
#
#         elif type(numerator) == Decimal:
#             numerator = decimal_to_dozenal(str(numerator))
#
#         cleaned_numerator = validate_clean_dozenal(numerator)
#
#         if denominator is None:
#             numerator = Dozenal(cleaned_numerator)
#             numerator, denominator = numerator.as_integer_ratio()
#             cleaned_numerator = str(numerator)
#             cleaned_denominator = str(denominator)
#
#         elif type(denominator) == Decimal:
#             denominator = decimal_to_dozenal(str(denominator))
#             cleaned_denominator = validate_clean_dozenal(denominator)
#
#         else:
#             cleaned_denominator = validate_clean_dozenal(denominator)
#
#         self._numerator = Dozenal(cleaned_numerator)
#         self._denominator = Dozenal(cleaned_denominator)
#         self._dozenal = self._numerator / self._denominator
#
#         super().__init__(self._dozenal)
#
#     @property
#     def numerator(self):
#         return self._numerator
#
#     @property
#     def denominator(self):
#         return self._denominator
#
#     @property
#     def dozenal(self):
#         return self._dozenal
#
#     def __str__(self) -> str:
#         if self._sign == -1:
#             res = '-'
#         else:
#             res = ''
#
#
#         res += str(self._numerator)
#         res += '/'
#         res += str(self._denominator)
#
#         return res
#
#     def __repr__(self) -> str:
#         return f"DozenalFraction('{self._numerator.formatted_number}/{self._denominator.formatted_number}') == {self._dozenal.__repr__()}"
#
#
# _numbers.Number.register(Dozenal)
# _numbers.Integral.register(Dozenal)
# _numbers.Rational.register(Dozenal)
#
# _numbers.Number.register(DozenalInteger)
# _numbers.Integral.register(DozenalInteger)
#
# _numbers.Number.register(DozenalFraction)
# _numbers.Integral.register(DozenalFraction)
