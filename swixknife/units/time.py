

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Time and Frequency
#
ANUGA_TO_SECOND = SezimalFraction('41 / 2_130')
SECOND_TO_ANUGA = ANUGA_TO_SECOND.reciprocal

#
# Avrita = agrima⁻¹
#
AVRITA_TO_HERTZ = SezimalFraction('41 / 2_130')
HERTZ_TO_AVRITA = AVRITA_TO_HERTZ.reciprocal


#
# Civil time
#
UTA_TO_HOUR = SezimalFraction('2 / 3')
HOUR_TO_UTA = UTA_TO_HOUR.reciprocal

POSHA_TO_MINUTE = SezimalFraction('14 / 13')
MINUTE_TO_POSHA = POSHA_TO_MINUTE.reciprocal

AGRIMA_TO_SECOND = SezimalFraction('122 / 43')
SECOND_TO_AGRIMA = AGRIMA_TO_SECOND.reciprocal

BODA_TO_SECOND = SezimalFraction('41 / 213_000')
SECOND_TO_BODA = BODA_TO_SECOND.reciprocal

UTA_TO_ANUGA = Sezimal('1_000_000')
POSHA_TO_ANUGA = Sezimal('10_000')
AGRIMA_TO_ANUGA = Sezimal('100')
BODA_TO_ANUGA = Sezimal('0.01')

UTA_TO_AGRIMA = Sezimal('10_000')
POSHA_TO_AGRIMA = Sezimal('100')
ANUGA_TO_AGRIMA = Sezimal('0.01')
BODA_TO_AGRIMA = Sezimal('0.000_1')

UTA_TO_DAY = Sezimal('0.01')
POSHA_TO_DAY = Sezimal('0.000_1')
AGRIMA_TO_DAY = Sezimal('0.000_001')
ANUGA_TO_DAY = Sezimal('0.000_000_01')
BODA_TO_DAY = Sezimal('0.000_000_000_1')

