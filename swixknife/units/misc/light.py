

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Luminous intensity (cd = lm/sr)
#
_TO_CANDELA = SezimalFraction('1_500_403_320_034_410_145 / 10_414_300_113_554_241')
CANDELA_TO_ = _TO_CANDELA.reciprocal

#
# Luminous flux (lm = cd·sr)
#
_TO_LUMEN = SezimalFraction('1_500_403_320_034_410_145 / 10_414_300_113_554_241')
LUMEN_TO_ = _TO_LUMEN.reciprocal

#
# Luminous energy (lm·s)
#
_TO_TALBOT = SezimalFraction('1_533_523_241_110_324_321 / 345_310_132_111_212_320')
TALBOT_TO_ = _TO_TALBOT.reciprocal

#
# Luminance (cd/m²)
#
_TO_NIT = SezimalFraction('1_510_032_320_503_133_144_014_400 / 554_014_521_311_024_425')
NIT_TO_ = _TO_NIT.reciprocal

#
# Illuminance (lm/m²)
#
_TO_LUX = SezimalFraction('1_510_032_320_503_133_144_014_400 / 554_014_521_311_024_425')
LUX_TO_ = _TO_LUX.reciprocal
