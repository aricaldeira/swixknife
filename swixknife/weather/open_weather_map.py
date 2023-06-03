
from datetime import datetime as _datetime
from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..date_time import SezimalDate, SezimalTime
from ..units.conversions import KILOMETER_PER_HOUR_TO_VEGA, KILOMETER_TO_CHAMAPADA, PASCAL_TO_DABA, METER_TO_PADA

import pyowm


def get_weather_conditions(api_key: str, location_id: str, language: str = 'en'):
    owm = pyowm.OWM('cd159e0045f3b80a94b7362454790299')
    owm.config['language'] = language or 'en'

    mgr = owm.weather_manager()

    observation = mgr.weather_at_id(int(location_id)).to_dict()

    if 'weather' in observation:
        if 'temperature' in observation['weather']:
            for key in ['temp', 'temp_max', 'temp_min', 'feels_like']:
                if key in observation['weather']['temperature']:
                    observation['weather']['temperature'][key] = _convert_temperature(observation['weather']['temperature'][key] or 0)


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


def _convert_time(timestamp: int, timezone_offset: int):
    timezone_offset = timezone_offset or 0
    dt = _datetime.fromtimestamp(timestamp)
    date = SezimalDate.fromordinal(dt.toordinal())
    return date


def _convert_temperature(kelvin: float, gatika=False):
    celsius = Sezimal(Decimal(str(kelvin))) - Sezimal(Decimal('273.15'))

    if gatika:
        gatika = celsius / Sezimal('0.244')
        gatika = round(Sezimal(gatika), 4)
        return gatika

    else:
        return round(celsius, 4)


def _convert_speed(speed: float):
    speed = Decimal(str(speed))

    return round(speed * KILOMETER_PER_HOUR_TO_VEGA, 2)


def _convert_distance(distance: float):
    distance = Decimal(str(distance))

    return round(distance * METER_TO_PADA, 0)

# def _convert_coordinates(position: float):

