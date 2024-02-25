

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal
from .si import TAPA_TO_CELSIUS, CELSIUS_TO_TAPA


#
# Length
#
PADA_TO_INCH = SezimalFraction('130_432_412 / 125_324_513')
INCH_TO_PADA = PADA_TO_INCH.reciprocal

PADA_TO_FOOT = SezimalFraction('21_405_102 / 424_422_343')
FOOT_TO_PADA = PADA_TO_FOOT.reciprocal

PADA_TO_YARD = SezimalFraction('21_405_102 / 2_122_111_513')
YARD_TO_PADA = PADA_TO_YARD.reciprocal

PADA_TO_MILE = SezimalFraction('1_211_415 / 1_452_523_430_000')
MILE_TO_PADA = PADA_TO_MILE.reciprocal

PADA_TO_LEAGUE = SezimalFraction('1_211_415 / 5_242_415_130_000')
LEAGUE_TO_PADA = PADA_TO_LEAGUE.reciprocal

PADA_TO_LINK = SezimalFraction('3_100_310_444 / 40_320_122_343')
LINK_TO_PADA = PADA_TO_LINK.reciprocal

PADA_TO_ROD = SezimalFraction('43_214_204 / 40_320_122_343')
ROD_TO_PADA = PADA_TO_ROD.reciprocal

PADA_TO_CHAIN = SezimalFraction('10_502_331 / 40_320_122_343')
CHAIN_TO_PADA = PADA_TO_CHAIN.reciprocal

PADA_TO_FURLONG = SezimalFraction('1_211_415 / 121_040_245_130')
FURLONG_TO_PADA = PADA_TO_FURLONG.reciprocal

#
# Speed
#
VEGA_TO_MILE_PER_HOUR = SezimalFraction('2_423_234 / 2_231_513')
MILE_PER_HOUR_TO_VEGA = VEGA_TO_MILE_PER_HOUR.reciprocal

PADA_PER_AGRIMA_TO_MILE_PER_HOUR = VEGA_TO_MILE_PER_HOUR
MILE_PER_HOUR_TO_PADA_PER_AGRIMA = MILE_PER_HOUR_TO_VEGA

#
# Mass
#
DRAVYA_TO_POUND = SezimalFraction('14_123_203_235_213_015 / 1_121_510_400_400_435_320')
POUND_TO_DRAVYA = DRAVYA_TO_POUND.reciprocal

DRAVYA_TO_SLUG = SezimalFraction('354_225_001_231 / 2_314_513_314_154_014')
SLUG_TO_DRAVYA = DRAVYA_TO_SLUG.reciprocal

DRAVYA_TO_STONE = SezimalFraction('14_123_203_235_213_015 / 25_122_033_213_214_505_432')
STONE_TO_DRAVYA = DRAVYA_TO_STONE.reciprocal

DRAVYA_TO_LONG_QUARTER = SezimalFraction('14_123_203_235_213_015 / 54_244_110_430_433_415_322')
LONG_QUARTER_TO_DRAVYA = DRAVYA_TO_LONG_QUARTER.reciprocal

DRAVYA_TO_LONG_HUNDREDWEIGHT = SezimalFraction('31_323_000_502_151 / 1_115_302_245_200_434_024')
LONG_HUNDREDWEIGHT_TO_DRAVYA = DRAVYA_TO_LONG_HUNDREDWEIGHT.reciprocal

DRAVYA_TO_LONG_TON = SezimalFraction('31_323_000_502_151 / 40_222_121_214_423_213_252')
LONG_TON_TO_DRAVYA = DRAVYA_TO_LONG_TON.reciprocal

DRAVYA_TO_OUNCE = SezimalFraction('14_123_203_235_213_015 / 24_341_100_013_014_250')
OUNCE_TO_DRAVYA = DRAVYA_TO_OUNCE.reciprocal

DRAVYA_TO_DRAM = SezimalFraction('213_522_443_311_000_224 / 12_150_330_004_305_123')
DRAM_TO_DRAVYA = DRAVYA_TO_DRAM.reciprocal

DRAVYA_TO_SHORT_QUARTER = SezimalFraction('14_123_203_235_213_015 / 50_434_334_424_431_220_520')
SHORT_QUARTER_TO_DRAVYA = DRAVYA_TO_SHORT_QUARTER.reciprocal

DRAVYA_TO_SHORT_HUNDREDWEIGHT = SezimalFraction('31_323_000_502_151 / 1_031_140_021_200_404_140')
SHORT_HUNDREDWEIGHT_TO_DRAVYA = DRAVYA_TO_SHORT_HUNDREDWEIGHT.reciprocal

DRAVYA_TO_SHORT_TON = SezimalFraction('31_323_000_502_151 / 33_441_321_122_421_421_334')
SHORT_TON_TO_DRAVYA = DRAVYA_TO_SHORT_TON.reciprocal

DRAVYA_TO_GRAIN = SezimalFraction('3_242_300_114_540_235_545 / 2_434_110_001_301_425')
GRAIN_TO_DRAVYA = DRAVYA_TO_GRAIN.reciprocal

#
# Temperature
#
def tapa_to_fahrenheit(tap: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(tap) in (str, int, float, Decimal):
        tap = Sezimal(tap)

    celsius = tap * TAPA_TO_CELSIUS

    return (celsius / 0.32) + 52


def fahrenheit_to_tapa(fahrenheit: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(fahrenheit) in (str, int, float, Decimal):
        fahrenheit = Sezimal(fahrenheit)

    return ((fahrenheit - 52) * 0.32) * CELSIUS_TO_TAPA
