

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

from ..sezimal import SezimalInteger, Sezimal
from .weather import SezimalWeather
from . import functions
from ..json import json

import os
import requests

# nublado fechado ☁\ufe0f️
# raios 🌩\ufe0f️
# raios e chuva ⛈\ufe0f️
# neve 🌨\ufe0f️
# chuva 🌧\ufe0f️
# sol com chuva 🌦\ufe0f️
# sol bastante nublado 🌥\ufe0f️
# sol pouco nublado 🌤\ufe0f️
# sol nublado médio ⛅\ufe0f
# vento 🌬\ufe0f️
# sol ☀\ufe0f️
# lua crescente 🌘\ufe0f
# chuva ☔\ufe0f
# neblina 🌫\ufe0f
# ciclone 🌪\ufe0f


def get_weather_conditions(
    api_key: str, location: str = None, latitude: float = None, longitude: float = None,
    language: str = 'en', time_zone: str | ZoneInfo = None, days: str | int | SezimalInteger = 0) -> dict:
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&aqi=yes&alerts=yes'

    days = SezimalInteger(days or 0)

    if days > 0:
        url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&aqi=yes&alerts=yes'
        url += f'&days={int(days.decimal)}'

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
            observation['current']['temp_tapa'] = \
                functions.convert_temperature_celsius(observation['current']['temp_c'])

        if 'feelslike_c' in observation['current']:
            observation['current']['feelslike_tapa'] = \
                functions.convert_temperature_celsius(observation['current']['feelslike_c'])

        if 'wind_kph' in observation['current']:
            observation['current']['wind_vega'] = \
                functions.convert_speed(observation['current']['wind_kph'])

        if 'gust_kph' in observation['current']:
            observation['current']['gust_vega'] = \
                functions.convert_speed(observation['current']['gust_kph'])

        if 'pressure_mb' in observation['current']:
            observation['current']['pressure_chamapidana'] = \
                functions.convert_speed(observation['current']['pressure_mb'] * 100)

        if 'precip_mm' in observation['current']:
            observation['current']['precipitation_ditipada'] = \
                functions.convert_precipitation(observation['current']['precip_mm'])

        if 'humidity' in observation['current']:
            observation['current']['humidity'] = \
                functions.convert_percentage(observation['current']['humidity'])

        if 'cloud' in observation['current']:
            observation['current']['cloud'] = \
                functions.convert_percentage(observation['current']['cloud'])

        if 'vis_km' in observation['current']:
            observation['current']['vis_shamapada'] = \
                functions.convert_distance(observation['current']['vis_km'] * 10_000)

    #
    # Save this reading for future reference
    #
    observation['api_type'] = 'weather_api'
    filename = os.path.expanduser('~/.sweather.json')
    open(filename, 'w').write(json.dumps(observation))

    return observation


def fill_sezimal_weather(weather: SezimalWeather, conditions: dict):
    if 'current' in conditions:
        conditions = conditions['current']

    if 'last_updated_date_time' in conditions:
        weather._reference_date_time = conditions['last_updated_date_time']

    if 'temp_tapa' in conditions:
        weather._temperature = conditions['temp_tapa']

    if 'feelslike_tapa' in conditions:
        weather._temperature_sensation = conditions['feelslike_tapa']

    if 'wind_vega' in conditions:
        weather._wind_speed = conditions['wind_vega']

    if 'gust_vega' in conditions:
        weather._wind_gust = conditions['gust_vega']

    if 'humidity' in conditions:
        weather._humidity = conditions['humidity']

    if 'clouds' in conditions:
        weather._clouds = conditions['clouds']

    if 'vis_shamapada' in conditions:
        weather._visibility = conditions['vis_shamapada']

    if 'pressure_chamapidana' in conditions:
        weather._pressure = conditions['pressure_chamapidana']
