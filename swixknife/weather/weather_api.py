

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')


from datetime import datetime as _datetime
from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..date_time import SezimalDate, SezimalTime, SezimalDateTime

from ..units.conversions import KILOMETER_PER_HOUR_TO_VEGA, \
    KILOMETER_TO_CHAMAPADA, PASCAL_TO_DABA, METER_TO_PADA, \
    PERCENTAGE_TO_PERSIXNIFF, MILLIMETER_TO_CHATIPADA

from .weather import SezimalWeather

import requests
import json


def get_weather_conditions(api_key: str, location: str = None, latitude: float = None, longitude: float = None, language: str = 'en', time_zone: str | ZoneInfo = None):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}'

    if location:
        url += f'&q={location}'
    else:
        url += f'&q={latitude},{longitude}'

    if language:
        url += f'&lang={language}'

    req = requests.get(url)

    observation = json.loads(req.text)

    if 'current' in observation:
        if 'last_updated_epoch' in observation['current']:
            observation['current']['last_updated_date_time'] = \
                _convert_time(observation['current']['last_updated_epoch'], time_zone)

        if 'temp_c' in observation['current']:
            observation['current']['temp_s'] = \
                _convert_temperature(observation['current']['temp_c'])

        if 'feelslike_c' in observation['current']:
            observation['current']['feelslike_s'] = \
                _convert_temperature(observation['current']['feelslike_c'])

        if 'wind_kph' in observation['current']:
            observation['current']['wind_vega'] = \
                _convert_speed(observation['current']['wind_kph'])

        if 'gust_kph' in observation['current']:
            observation['current']['gust_vega'] = \
                _convert_speed(observation['current']['gust_kph'])

        if 'pressure_mb' in observation['current']:
            observation['current']['pressure_chamadaba'] = \
                _convert_speed(observation['current']['pressure_mb'])

        if 'precip_mm' in observation['current']:
            observation['current']['precipitation_chatipada'] = \
                _convert_precipitation(observation['current']['precip_mm'])

        if 'humidity' in observation['current']:
            observation['current']['humidity'] = \
                _convert_percentage(observation['current']['humidity'])

        if 'cloud' in observation['current']:
            observation['current']['cloud'] = \
                _convert_percentage(observation['current']['cloud'])

        if 'vis_km' in observation['current']:
            observation['current']['vis_chamapada'] = \
                _convert_distance(observation['current']['vis_km'])

    return observation


def fill_sezimal_weather(weather: SezimalWeather, conditions: dict):
    if 'current' in conditions:
        conditions = conditions['current']

    if 'last_updated_date_time' in conditions:
        weather._reference_date_time = conditions['last_updated_date_time']

    if 'temp_s' in conditions:
        weather._temperature = conditions['temp_s']

    if 'feelslike_s' in conditions:
        weather._temperature_sensation = conditions['feelslike_s']

    if 'wind_vega' in conditions:
        weather._wind_speed = conditions['wind_vega']

    if 'gust_vega' in conditions:
        weather._wind_gust = conditions['gust_vega']

    if 'humidity' in conditions:
        weather._humidity = conditions['humidity']

    if 'clouds' in conditions:
        weather._clouds = conditions['clouds']

    if 'vis_chamapada' in conditions:
        weather._visibility = conditions['vis_chamapada']

    if 'pressure_chamadaba' in conditions:
        weather._pressure = conditions['pressure_chamadaba']


def _convert_time(time: int | float, time_zone: str | ZoneInfo = None) -> SezimalDateTime:
    return SezimalDateTime.from_timestamp(time, time_zone=time_zone)


def _convert_temperature(celsius: float, gatika=False) -> Sezimal:
    celsius = Sezimal(Decimal(str(celsius)))

    if gatika:
        gatika = celsius / Sezimal('0.244')
        gatika = round(Sezimal(gatika), 4)
        return gatika

    else:
        return round(celsius, 4)


def _convert_speed(speed: float) -> Sezimal:
    speed = Decimal(str(speed))

    return round(speed * KILOMETER_PER_HOUR_TO_VEGA, 0)


def _convert_distance(distance: float) -> Sezimal:
    distance = Decimal(str(distance)) / 10_000

    return round(distance * KILOMETER_TO_CHAMAPADA, 0)


def _convert_pressure(pressure: float) -> Sezimal:
    pressure = Decimal(str(pressure)) * 100

    return round(pressure * PASCAL_TO_DABA / 1_0000, 0)


def _convert_percentage(percentage: float) -> Sezimal:
    percentage = Decimal(str(percentage))
    return round(percentage * PERCENTAGE_TO_PERSIXNIFF, 0)


def _convert_precipitation(precipitation: float) -> Sezimal:
    distance = Decimal(str(precipitation))

    return round(distance * MILLIMETER_TO_CHATIPADA, 0)
