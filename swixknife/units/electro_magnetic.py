

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Electric Current
#
DARA_TO_AMPERE = SezimalFraction('21_040_141_543_345_441 / 4_001_223_431_420_015_054')
AMPERE_TO_DARA = DARA_TO_AMPERE.reciprocal

#
# Electric Charge
#
AVESHA_TO_COULOMB = SezimalFraction('543_113_043_050_305_145 / 5_410_444_451_125_535_023_412')
COULOMB_TO_AVESHA = AVESHA_TO_COULOMB.reciprocal

#
# Electric Potential Difference
#
VIBAVA_TO_VOLT = SezimalFraction('155_121_452_505_541_442 / 20_251_230_533_422_505')
VOLT_TO_VIBAVA = VIBAVA_TO_VOLT.reciprocal

#
# Electrical Resistance
#
PRATIRODA_TO_OHM = SezimalFraction('424_125_300_421_243_401 / 231_513_450_033_532')
OHM_TO_PRATIRODA = PRATIRODA_TO_OHM.reciprocal

#
# Electrical Conductance
#
CHALANA_TO_SIEMENS = SezimalFraction('10_115_244_311_322_115 / 14_503_100_053_453_524_014')
SIEMENS_TO_CHALANA = CHALANA_TO_SIEMENS.reciprocal

#
# Electrical Inductance
#
PRERAKA_TO_HENRY = SezimalFraction('215_243_511_044_002_225 / 4_150_134_441_440_000')
HENRY_TO_PRERAKA = PRERAKA_TO_HENRY.reciprocal

#
# Electrical Capacitance
#
SAMAI_TO_FARAD = SezimalFraction('3_520_551_355_355_435 / 340_002_011_553_504_235_552')
FARAD_TO_SAMAI = SAMAI_TO_FARAD.reciprocal

#
# Magnetic Flux
#
ABIVA_TO_WEBER = SezimalFraction('303_144_201_502_315_013 / 1_431_013_225_041_414_132')
WEBER_TO_ABIVA = ABIVA_TO_WEBER.reciprocal

#
# Magnetic Flux Density
#
VISTARA_TO_TESLA = SezimalFraction('204_052_342_334_413_015_252 / 101_431_220_215_555_311')
TESLA_TO_VISTARA = VISTARA_TO_TESLA.reciprocal

