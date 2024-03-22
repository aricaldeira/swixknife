

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
BARA_TO_NEWTON = SezimalFraction('2_403_004_511_114_043_553 / 23_350_451_052_312_003_204')
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
KARYA_TO_JOULE = SezimalFraction('1_211_514_105_122_323_333 / 1_231_521_045_023_545_533_312')
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
SHATI_TO_WATT = SezimalFraction('3_154_553_432_555_434_231 / 102_253_050_344_555_124_112')
WATT_TO_SHATI = SHATI_TO_WATT.reciprocal

#
# Pressure
#
# Daba = dravya × pada⁻¹ × agrima⁻²
# Daba = bara × pada⁻² = bara × keshe⁻¹
# Daba = karya × pada⁻³ = karya × aytan⁻¹
#
DABA_TO_PASCAL = SezimalFraction('2_223_134_332_430_431_202_024 / 2_013_050_024_144_331_153')
PASCAL_TO_DABA = DABA_TO_PASCAL.reciprocal

SANVEGA_TO_KILOGRAM_METER_PER_SECOND = SezimalFraction('1_041_132_010_001_115_355 / 330_412_211_304_203_420_514')
KILOGRAM_METER_PER_SECOND_TO_SANVEGA = SANVEGA_TO_KILOGRAM_METER_PER_SECOND.reciprocal

PRAKEPA_TO_KILOGRAM_SQUARE_METER_PER_SECOND = SezimalFraction('2_504_230_121_523_205_255 / 133_421_413_541_254_510_215_440')
KILOGRAM_SQUARE_METER_PER_SECOND_TO_PRAKEPA = PRAKEPA_TO_KILOGRAM_SQUARE_METER_PER_SECOND.reciprocal

PRABAVA_TO_NEWTON_SQUARE_METER = SezimalFraction('512_554_345_012_134_545 / 55_023_203_412_213_354_200_530')
NEWTON_SQUARE_METER_TO_PRABAVA = PRABAVA_TO_NEWTON_SQUARE_METER.reciprocal

TANAVA_TO_NEWTON_PER_METER = SezimalFraction('42_214_241_130_225_252_323 / 3_555_141_452_012_013_022')
NEWTON_PER_METER_TO_TANAVA = TANAVA_TO_NEWTON_PER_METER.reciprocal

UPARI_TO_WATT_PER_SQUARE_METER = SezimalFraction('41_443_005_412_305_105_224 / 111_225_325_031_125_241')
WATT_PER_SQUARE_METER_TO_UPARI = UPARI_TO_WATT_PER_SQUARE_METER.reciprocal
