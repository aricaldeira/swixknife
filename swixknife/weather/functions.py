

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

from decimal import Decimal
from ..sezimal import Sezimal, SezimalInteger
from ..date_time import SezimalDateTime

from ..units import decimal_to_sezimal_unit, sezimal_to_sezimal_unit


def convert_time(time: int | float, time_zone: str | ZoneInfo = None) -> SezimalDateTime:
    return SezimalDateTime.from_timestamp(time, time_zone=time_zone)


def convert_temperature_kelvin(kelvin: float, gatika: bool = False) -> Sezimal:
    temperature = decimal_to_sezimal_unit(Decimal(str(kelvin)), 'K', 'tap')

    if gatika:
        temperature = sezimal_to_sezimal_unit(temperature, 'tap', 'XDgtk')

    return round(temperature, 3)


def convert_temperature_celsius(celsius: float | Sezimal, gatika: bool | Sezimal = False) -> Sezimal:
    temperature = decimal_to_sezimal_unit(Decimal(str(celsius)), '°C', 'tap')

    if gatika:
        temperature = sezimal_to_sezimal_unit(temperature, 'tap', 'XDgtk')

    return round(temperature, 2)


def convert_speed(speed: float) -> Sezimal:
    return round(decimal_to_sezimal_unit(Decimal(str(speed)), 'km/h', 'veg'), 0)


def convert_distance(distance: float) -> Sezimal:
    return round(decimal_to_sezimal_unit(Decimal(str(distance)), 'm', 'Xpad'), 0)


def convert_pressure(pressure: float) -> Sezimal:
    return round(decimal_to_sezimal_unit(Decimal(str(pressure)), 'Pa', 'vay'), 0)


def convert_percentage(percentage: float) -> Sezimal:
    return round(decimal_to_sezimal_unit(Decimal(str(percentage)), '%', 'dprt'), 0)


def convert_precipitation(precipitation: float) -> Sezimal:
    return round(decimal_to_sezimal_unit(Decimal(str(precipitation)), 'mm', 'dpad'), 0)


def convert_angle(angle: float) -> Sezimal:
    return round(decimal_to_sezimal_unit(Decimal(str(angle)), 'deg', 'dmdl'), 2)
