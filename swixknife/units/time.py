

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Time and Frequency
#
# ANUGA_TO_SECOND = SezimalFraction('41 / 2_130')
ANUGA_TO_SECOND = Sezimal('0.015_04')
SECOND_TO_ANUGA = Sezimal('31..235_01...')

#
# Avrita = agrima⁻¹
#
# AVRITA_TO_HERTZ = SezimalFraction('2_130 / 41')
AVRITA_TO_HERTZ = Sezimal('31..235_01...')
HERTZ_TO_AVRITA = Sezimal('0.015_04')


#
# Civil time
#
# UTA_TO_HOUR = SezimalFraction('3 / 2')
UTA_TO_HOUR = Sezimal('0.4')
HOUR_TO_UTA = Sezimal('1.3')

# POSHA_TO_MINUTE = SezimalFraction('14 / 13')
POSHA_TO_MINUTE = Sezimal('1.04')
MINUTE_TO_POSHA = Sezimal('0.5..2...')

# AGRIMA_TO_SECOND = SezimalFraction('122 / 43')
AGRIMA_TO_SECOND = Sezimal('1.504')
SECOND_TO_AGRIMA = Sezimal('0.3..123_50...')

# BODA_TO_SECOND = SezimalFraction('41 / 213_000')
BODA_TO_SECOND = Sezimal('0.000_150_4')
SECOND_TO_BODA = Sezimal('3_123..501_23...')

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
