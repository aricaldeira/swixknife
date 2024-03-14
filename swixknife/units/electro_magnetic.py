

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Electric Current
#
DARA_TO_AMPERE = SezimalFraction('1_510_451_504_031_332_555 / 323_025_140_420_332_150_212')
AMPERE_TO_DARA = DARA_TO_AMPERE.reciprocal

#
# Electric Charge
#
AVESHA_TO_COULOMB = SezimalFraction('3_500_500_300_322_033_511 / 34_443_111_124_555_432_142_452')
COULOMB_TO_AVESHA = AVESHA_TO_COULOMB.reciprocal

#
# Electric Potential Difference
#
VIBAVA_TO_VOLT = SezimalFraction('2_141_044_552_420_141_555 / 222_220_322_400_552_010')
VOLT_TO_VIBAVA = VIBAVA_TO_VOLT.reciprocal

#
# Electrical Resistance
#
PRATIRODA_TO_OHM = SezimalFraction('111_133_351_303_345 / 40_450_211_224')
OHM_TO_PRATIRODA = PRATIRODA_TO_OHM.reciprocal

#
# Electrical Conductance
#
CHALANA_TO_SIEMENS = SezimalFraction('40_450_211_224 / 111_133_351_303_345')
SIEMENS_TO_CHALANA = CHALANA_TO_SIEMENS.reciprocal

#
# Electrical Inductance
#
PRERAKA_TO_HENRY = SezimalFraction('111_133_351_303_345 / 2_122_130_400_000')
HENRY_TO_PRERAKA = PRERAKA_TO_HENRY.reciprocal

#
# Electrical Capacitance
#
SAMAI_TO_FARAD = SezimalFraction('304_120_242_301_312_135 / 25_341_014_152_015_130_221_200')
FARAD_TO_SAMAI = SAMAI_TO_FARAD.reciprocal

#
# Magnetic Flux
#
ABIVA_TO_WEBER = SezimalFraction('2_504_230_121_523_205_255 / 13_415_151_444_524_353_023')
WEBER_TO_ABIVA = ABIVA_TO_WEBER.reciprocal

#
# Magnetic Flux Density
#
VISTARA_TO_TESLA = SezimalFraction('1_140_223_114_252_344_522_304 / 345_013_240_310_325_341')
TESLA_TO_VISTARA = VISTARA_TO_TESLA.reciprocal
