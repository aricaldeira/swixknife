

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

from .weather import SezimalWeather
from . import functions

import requests
import json


def get_weather_conditions(api_key: str, location: str = None, latitude: float = None, longitude: float = None, language: str = 'en', time_zone: str | ZoneInfo = None) -> dict:
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
                functions.convert_time(observation['current']['last_updated_epoch'], time_zone)

        if 'temp_c' in observation['current']:
            observation['current']['temp_s'] = \
                functions.convert_temperature_celsius(observation['current']['temp_c'])

        if 'feelslike_c' in observation['current']:
            observation['current']['feelslike_s'] = \
                functions.convert_temperature_celsius(observation['current']['feelslike_c'])

        if 'wind_kph' in observation['current']:
            observation['current']['wind_vega'] = \
                functions.convert_speed(observation['current']['wind_kph'])

        if 'gust_kph' in observation['current']:
            observation['current']['gust_vega'] = \
                functions.convert_speed(observation['current']['gust_kph'])

        if 'pressure_mb' in observation['current']:
            observation['current']['pressure_chamadaba'] = \
                functions.convert_speed(observation['current']['pressure_mb'])

        if 'precip_mm' in observation['current']:
            observation['current']['precipitation_chatipada'] = \
                functions.convert_precipitation(observation['current']['precip_mm'])

        if 'humidity' in observation['current']:
            observation['current']['humidity'] = \
                functions.convert_percentage(observation['current']['humidity'])

        if 'cloud' in observation['current']:
            observation['current']['cloud'] = \
                functions.convert_percentage(observation['current']['cloud'])

        if 'vis_km' in observation['current']:
            observation['current']['vis_chamapada'] = \
                functions.convert_distance(observation['current']['vis_km'])

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
