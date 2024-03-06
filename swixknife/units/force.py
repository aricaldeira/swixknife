

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Force/Weight, Pressure, Energy/Work/Heat, Power
#

#
# Force / Weight
#
# Bara = dravya × pada × agrima⁻²
# Bara = dravya × tevara
#
BARA_TO_NEWTON = SezimalFraction('210_554_230_514_213_051 / 2_044_541_313_204_401_200')
NEWTON_TO_BARA = BARA_TO_NEWTON.reciprocal

#
# Energy/Work/Heat
#
# Karya = dravya × pada² × agrima⁻²
# Karya = bara × pada
# Karya = daba × aytan
#
# 1 J = 3.412 karya
# 1 karya = 1 ÷ 3.412 J
#
KARYA_TO_JOULE = SezimalFraction('23_433_452_533_505_041 / 24_224_034_443_110_000_344')
JOULE_TO_KARYA = KARYA_TO_JOULE.reciprocal

#
# Power
#
# Shati = dravya × pada² × agrima⁻³ = dravya × keshe × agrima⁻³
# Shati = karya × agrima⁻¹
# Shati = bara × pada × agrima⁻¹
# Shati = daba × pada³ × agrima⁻¹ = daba × aytan × agrima⁻¹
#
# 1 W = 10.505_252 xat
# 1 xat = 1 ÷ 10.505_252 W
#
SHATI_TO_WATT = SezimalFraction('23_433_452_533_505_041 / 502_150_541_130_054_411')
WATT_TO_SHATI = SHATI_TO_WATT.reciprocal

#
# Pressure
#
# Daba = dravya × pada⁻¹ × agrima⁻²
# Daba = bara × pada⁻² = bara × keshe⁻¹
# Daba = karya × pada⁻³ = karya × aytan⁻¹
#
DABA_TO_PASCAL = SezimalFraction('14_001_522_340_145_312_055_052 / 12_300_335_551_511_421_225')
PASCAL_TO_DABA = DABA_TO_PASCAL.reciprocal

