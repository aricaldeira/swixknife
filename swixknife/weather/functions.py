

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

from decimal import Decimal
from ..sezimal import Sezimal, SezimalInteger
from ..date_time import SezimalDateTime

from ..units.length import KILOMETER_PER_HOUR_TO_VEGA, \
    KILOMETER_TO_SHAMAPADA, MILLIMETER_TO_DITIPADA
from ..units.temperature import CELSIUS_TO_TAPA, kelvin_to_celsius, tapa_to_gatika
from ..units.force import PASCAL_TO_DABA
from ..units.proportion import PERCENTAGE_TO_PERSIXNIFF


def convert_time(time: int | float, time_zone: str | ZoneInfo = None) -> SezimalDateTime:
    return SezimalDateTime.from_timestamp(time, time_zone=time_zone)


def convert_temperature_kelvin(kelvin: float, gatika: bool = False) -> Sezimal:
    celsius = kelvin_to_celsius(Sezimal(Decimal(str(kelvin))))

    tapa = celsius * CELSIUS_TO_TAPA

    if gatika:
        return round(tapa_to_gatika(tapa), 3)

    return round(tapa, 3)


def convert_temperature_celsius(celsius: float | Sezimal, gatika: bool | Sezimal = False) -> Sezimal:
    celsius = Sezimal(Decimal(str(celsius)))
    tapa = celsius * CELSIUS_TO_TAPA

    if gatika:
        return round(tapa_to_gatika(tapa), 2)

    return round(tapa, 2)


def convert_speed(speed: float) -> Sezimal:
    return round(Decimal(str(speed)) * KILOMETER_PER_HOUR_TO_VEGA, 0)


def convert_distance(distance: float) -> Sezimal:
    return round((Decimal(str(distance)) / 10_000) * KILOMETER_TO_SHAMAPADA, 0)


def convert_pressure(pressure: float) -> Sezimal:
    return round(Decimal(str(pressure)) * PASCAL_TO_DABA, 0)


def convert_percentage(percentage: float) -> Sezimal:
    return round(Decimal(str(percentage)) * PERCENTAGE_TO_PERSIXNIFF, 0)


def convert_precipitation(precipitation: float) -> Sezimal:
    return round(Decimal(str(precipitation)) * MILLIMETER_TO_DITIPADA, 0)


def convert_angle(angle: float) -> Sezimal:
    return round(Decimal(str(angle)) / Sezimal(1400) * 100, 2)
