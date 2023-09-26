

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

from .weather import SezimalWeather
from . import functions

import pyowm


def get_weather_conditions(api_key: str, location_id: str, language: str = 'en', time_zone: str | ZoneInfo = None) -> dict:
    owm = pyowm.OWM(api_key)
    owm.config['language'] = language or 'en'

    mgr = owm.weather_manager()

    observation = mgr.weather_at_id(int(location_id)).to_dict()

    if 'reception_time' in observation:
        observation['reception_time'] = \
            functions.convert_time(observation['reception_time'], time_zone=time_zone)

    if 'weather' in observation:
        if 'reference_time' in observation['weather']:
            observation['weather']['reference_time'] = \
                functions.convert_time(observation['weather']['reference_time'], time_zone=time_zone)

        if 'sunset_time' in observation['weather']:
            observation['weather']['sunset_time'] = \
                functions.convert_time(observation['weather']['sunset_time'], time_zone=time_zone)

        if 'sunrise_time' in observation['weather']:
            observation['weather']['sunrise_time'] = \
                functions.convert_time(observation['weather']['sunrise_time'], time_zone=time_zone)

        if 'temperature' in observation['weather']:
            for key in ['temp', 'temp_max', 'temp_min', 'feels_like', 'temp_kf']:
                if key in observation['weather']['temperature']:
                    observation['weather']['temperature'][key] = \
                        functions.convert_temperature_kelvin(observation['weather']['temperature'][key] or 0)

        if 'wind' in observation['weather']:
            if 'speed' in observation['weather']['wind']:
                observation['weather']['wind']['speed'] = \
                    functions.convert_speed(observation['weather']['wind']['speed'])

            if 'gust' in observation['weather']['wind']:
                observation['weather']['wind']['gust'] = \
                    functions.convert_speed(observation['weather']['wind']['gust'])

        if 'pressure' in observation['weather']:
            if 'press' in observation['weather']['pressure']:
                observation['weather']['pressure']['press'] = \
                    functions.convert_pressure(observation['weather']['pressure']['press'])

            if 'sea_level' in observation['weather']['pressure']:
                observation['weather']['pressure']['sea_level'] = \
                    functions.convert_pressure(observation['weather']['pressure']['sea_level'])

        if 'humidity' in observation['weather']:
            observation['weather']['humidity'] = \
                functions.convert_percentage(observation['weather']['humidity'])

        if 'clouds' in observation['weather']:
            observation['weather']['clouds'] = \
                functions.convert_percentage(observation['weather']['clouds'])

        if 'visibility_distance' in observation['weather']:
            observation['weather']['visibility_distance'] = \
                functions.convert_distance(observation['weather']['visibility_distance'])

    # {
    #     'reception_time': 1685035661,
    #     'location': {
    #         'name': 'Sorocaba',
    #         'coordinates': {
    #             'lon': -47.4581,
    #             'lat': -23.5017
    #         },
    #         'ID': 3447399,
    #         'country': 'BR'
    #     },
    #     'weather': {
    #         'reference_time': 1685035661,
    #         'sunset_time': 1685046754,
    #         'sunrise_time': 1685007675,
    #         'clouds': 0,
    #         'rain': {},
    #         'snow': {},
    #         'wind': {
    #             'speed': 2.61,
    #             'deg': 4,
    #             'gust': 4.03
    #         },
    #         'humidity': 45,
    #         'pressure': {
    #             'press': 1019,
    #             'sea_level': 1019
    #         },
    #         'temperature': {
    #             'temp': 299.87,
    #             'temp_kf': None,
    #             'temp_max': 299.87,
    #             'temp_min': 299.87,
    #             'feels_like': 300.05
    #         },
    #         'status': 'Clear',
    #         'detailed_status': 'céu limpo',
    #         'weather_code': 800,
    #         'weather_icon_name': '01d',
    #         'visibility_distance': 10000,
    #         'dewpoint': None,
    #         'humidex': None,
    #         'heat_index': None,
    #         'utc_offset': -10800,
    #         'uvi': None,
    #         'precipitation_probability': None
    #     }
    # }

    return observation


def fill_sezimal_weather(weather: SezimalWeather, conditions: dict):
    if 'weather' in conditions:
        conditions = conditions['weather']

    if 'reference_time' in conditions:
        weather._reference_date_time = conditions['reference_time']

    if 'sunrise_time' in conditions:
        weather._sunrise_date_time = conditions['sunrise_time']

    if 'sunset_time' in conditions:
        weather._sunset_date_time = conditions['sunset_time']

    if 'temperature' in conditions:
        temperature = conditions['temperature']

        if 'temp' in temperature:
            weather._temperature = temperature['temp']

        if 'feels_like' in temperature:
            weather._temperature_sensation = temperature['feels_like']

        if 'temp_max' in temperature:
            weather._temperature_maximum = temperature['temp_max']

        if 'temp_min' in temperature:
            weather._temperature_minimum = temperature['temp_min']

    if 'wind' in conditions:
        wind = conditions['wind']

        if 'speed' in wind:
            weather._wind_speed = wind['speed']

        if 'gust' in wind:
            weather._wind_speed = wind['gust']

        if 'deg' in wind:
            weather._wind_direction = wind['deg']

    if 'humidity' in conditions:
        weather._humidity = conditions['humidity']

    if 'clouds' in conditions:
        weather._clouds = conditions['clouds']

    if 'visibility_distance' in conditions:
        weather._visibility = conditions['visibility_distance']

    if 'pressure' in conditions:
        pressure = conditions['pressure']

        if 'press' in pressure:
            weather._pressure = pressure['press']

        if 'sea_level' in pressure:
            weather._pressure_sea_level = pressure['sea_level']
