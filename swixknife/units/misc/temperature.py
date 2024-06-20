

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Temperature
#
GATIKA_TAPA_SCALE_START = Sezimal('240_234_312')

# GATIKA_TO_KELVIN = SezimalFraction('10_555_444_540_024_220_300_311_044_444_024_243_143 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344')
GATIKA_TO_KELVIN = Sezimal('0.000_002_455_444_231_451_053_242_255_010_330_042_540_340_253_233')
KELVIN_TO_GATIKA = Sezimal('204_132.130_415_510_035_252_550_355_015_010_432_222_454_345_205_115_155')
GATIKA_TO_KELVIN.reciprocal = KELVIN_TO_GATIKA
KELVIN_TO_GATIKA.reciprocal = GATIKA_TO_KELVIN

# TAPA_TO_CELSIUS = SezimalFraction('1_055_544_454_002_422_030_031_104_444_402_424_314_300_000 / 2_245_430_323_350_444_405_535_225_150_451_403_235_403_344')
TAPA_TO_CELSIUS = Sezimal('0.245_544_423_145_105_324_225_501_033_004_254_034_025_323_302_421')
CELSIUS_TO_TAPA = Sezimal('2.041_321_304_155_100_352_525_503_550_150_104_322_224_543_452_051')
TAPA_TO_CELSIUS.reciprocal = CELSIUS_TO_TAPA
CELSIUS_TO_TAPA.reciprocal = TAPA_TO_CELSIUS


def gatika_to_tapa(gtk: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(gtk) in (str, int, float, Decimal):
        gtk = Sezimal(gtk)

    return (gtk - GATIKA_TAPA_SCALE_START) / 100_000


def tapa_to_gatika(tap: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(tap) in (str, int, float, Decimal):
        tap = Sezimal(tap)

    return (tap * 100_000) + GATIKA_TAPA_SCALE_START


def kelvin_to_celsius(kelvin: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(kelvin) in (str, int, float, Decimal):
        kelvin = Sezimal(kelvin)

    gtk = kelvin * KELVIN_TO_GATIKA
    tap = gatika_to_tapa(gtk)

    return tap * TAPA_TO_CELSIUS


def celsius_to_kelvin(celsius: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(celsius) in (str, int, float, Decimal):
        celsius = Sezimal(celsius)

    tap = celsius * CELSIUS_TO_TAPA
    gtk = tapa_to_gatika(tap)

    return gtk * GATIKA_TO_KELVIN


def tapa_to_fahrenheit(tap: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(tap) in (str, int, float, Decimal):
        tap = Sezimal(tap)

    celsius = tap * TAPA_TO_CELSIUS

    return (celsius / 0.32) + 52


def fahrenheit_to_tapa(fahrenheit: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction = 1) -> Sezimal:
    if type(fahrenheit) in (str, int, float, Decimal):
        fahrenheit = Sezimal(fahrenheit)

    return ((fahrenheit - 52) * 0.32) * CELSIUS_TO_TAPA
