

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

from decimal import Decimal
from ..sezimal import Sezimal, SezimalInteger
from ..date_time import SezimalDateTime

from ..units.conversions import KILOMETER_PER_HOUR_TO_VEGA, \
    KILOMETER_TO_CHAMAPADA, PASCAL_TO_DABA, METER_TO_PADA, \
    PERCENTAGE_TO_PERSIXNIFF, MILLIMETER_TO_CHATIPADA


def convert_time(time: int | float, time_zone: str | ZoneInfo = None) -> SezimalDateTime:
    return SezimalDateTime.from_timestamp(time, time_zone=time_zone)


def convert_temperature_kelvin(kelvin: float, gatika: bool = False) -> Sezimal:
    celsius = Sezimal(Decimal(str(kelvin))) - Sezimal(Decimal('273.15'))

    return convert_temperature_celsius(celsius, gatika)


def convert_temperature_celsius(celsius: float | Sezimal, gatika: bool | Sezimal = False) -> Sezimal:
    celsius = Sezimal(Decimal(str(celsius)))

    if gatika:
        gatika = celsius / Sezimal('0.244')
        gatika = round(Sezimal(gatika), 4)
        return gatika

    else:
        return round(celsius, 4)


def convert_speed(speed: float) -> Sezimal:
    return round(Decimal(str(speed)) * KILOMETER_PER_HOUR_TO_VEGA, 0)


def convert_distance(distance: float) -> Sezimal:
    return round((Decimal(str(distance)) / 10_000) * KILOMETER_TO_CHAMAPADA, 0)


def convert_pressure(pressure: float) -> Sezimal:
    return round((Decimal(str(pressure)) * 100) * PASCAL_TO_DABA / 1_0000, 0)


def convert_percentage(percentage: float) -> Sezimal:
    return round(Decimal(str(percentage)) * PERCENTAGE_TO_PERSIXNIFF, 0)


def convert_precipitation(precipitation: float) -> Sezimal:
    return round(Decimal(str(precipitation)) * MILLIMETER_TO_CHATIPADA, 0)
