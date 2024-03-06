

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Temperature
#

# #
# # This is for 100_dec °C == 212_dec °T
# #
# GATIKA_TO_KELVIN = SezimalFraction('41 / 12_500_000')
# KELVIN_TO_GATIKA = SezimalFraction('12_500_000 / 41')
# GATIKA_TO_KELVIN.reciprocal = KELVIN_TO_GATIKA
# KELVIN_TO_GATIKA.reciprocal = GATIKA_TO_KELVIN
#
# TAPA_TO_CELSIUS = SezimalFraction('41 / 125')
# CELSIUS_TO_TAPA = SezimalFraction('125 / 41')
# TAPA_TO_CELSIUS.reciprocal = CELSIUS_TO_TAPA
# CELSIUS_TO_TAPA.reciprocal = TAPA_TO_CELSIUS
#
# GATIKA_TAPA_SCALE_START = SezimalFraction('131_504_043_000 / 325')

#
# This is for 273.15_dec K == 240_100_404 gtk 4_486_900_dec gtk
# This gives water freezing a precise point on the scale,
# while also giving a nice convertion to Celsius about
# 2.040_143_01 ~ 2.112_462_dec
#
# Specific heat of water is tuned at
# 293.150_547_161_145 K
# 20.000_547_161_145 °C
#
GATIKA_TAPA_SCALE_START = Sezimal('240_100_404')

GATIKA_TO_KELVIN = SezimalFraction('41_143 / 12_523_221_412')
KELVIN_TO_GATIKA = GATIKA_TO_KELVIN.reciprocal

TAPA_TO_CELSIUS = SezimalFraction('132_523_430 / 320_113_505')
CELSIUS_TO_TAPA = TAPA_TO_CELSIUS.reciprocal


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
