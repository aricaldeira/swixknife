

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
BARA_TO_NEWTON = SezimalFraction('140_044_125_050_401_515_333_102_530_425_051 / 1_342_515_120_344_254_304_101_141_101_043_000')
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
KARYA_TO_JOULE = SezimalFraction('354_130_453_415_323_044_134_335_024_103_120_201 / 404_010_231_220_325_534_323_421_233_142_003_213_000')
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
SHATI_TO_WATT = SezimalFraction('354_130_453_415_323_044_134_335_024_103_120_201 / 11_340_435_211_243_451_150_450_433_124_305_021_300')
WATT_TO_SHATI = SHATI_TO_WATT.reciprocal

#
# Pressure
#
# Daba = dravya × pada⁻¹ × agrima⁻²
# Daba = bara × pada⁻² = bara × keshe⁻¹
# Daba = karya × pada⁻³ = karya × aytan⁻¹
#
DABA_TO_PASCAL = SezimalFraction('14_424_403_550_414_542_314_252_131 / 13_043_300_444_301_044_043_000')
PASCAL_TO_DABA = DABA_TO_PASCAL.reciprocal

SANVEGA_TO_KILOGRAM_METER_PER_SECOND = SezimalFraction('140_044_125_050_401_515_333_102_530_425_051 / 51_325_113_230_013_330_422_513_034_440_430_000')

PRAKEPA_TO_KILOGRAM_SQUARE_METER_PER_SECOND = SezimalFraction('354_130_453_415_323_044_134_335_024_103_120_201 / 21_153_410_441_340_143_331_435_310_122_535_202_130_000')

PRABAVA_TO_NEWTON_SQUARE_METER = SezimalFraction('1_320_311_410_235_012_143_514_352_031_140_443_204_411 / 142_241_113_150_020_344_030_240_442_551_442_101_314_043_000')

TANAVA_TO_NEWTON_PER_METER = SezimalFraction('41_230_050_023_300_330_350_144_350_041 / 3_503_421_135_135_312_253_520_213_000')

UPARI_TO_WATT_PER_SQUARE_METER = SezimalFraction('1_133_234_040_423_211_533_001_310_313_204_525_150_123_110_004 / 2_044_133_514_410_335_455_244_112_040_434_113_454_241_513')
