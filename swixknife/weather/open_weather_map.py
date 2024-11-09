

__all__ = ('get_weather_conditions', 'fill_sezimal_weather')


from typing import TypeVar

ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')


from decimal import Decimal
from ..sezimal import SezimalInteger, Sezimal, SezimalFraction
from ..date_time import SezimalDateTime
from ..units import decimal_to_sezimal_unit
from ..json import json
from .weather import SezimalWeather

import os
import requests


def get_weather_conditions(api_key: str, latitude: float = None, longitude: float = None, time_zone: ZoneInfo | str = None) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

    req = requests.get(url)

    observation = json.loads(req.text)

    if 'main' in observation:
        observation['main']['temp'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['temp'])) * 100,
                244,
            ),
            'K', 'tap',
        )
        observation['main']['feels_like'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['feels_like'])) * 100,
                244,
            ),
            'K', 'tap',
        )
        observation['main']['temp_min'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['temp_min'])) * 100,
                244,
            ),
            'K', 'tap',
        )
        observation['main']['temp_max'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['temp_max'])) * 100,
                244,
            ),
            'K', 'tap',
        )
        observation['main']['pressure'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['pressure'])) * 100,
                244,
            ),
            'hPa', 'Xpdn',
        )
        observation['main']['humidity'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['humidity'])) * 100,
                244,
            ),
            '%', 'dspn',
        )
        observation['main']['sea_level'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['sea_level'])) * 100,
                244,
            ),
            'hPa', 'Xpdn',
        )
        observation['main']['grnd_level'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['main']['grnd_level'])) * 100,
                244,
            ),
            'hPa', 'Xpdn',
        )

    if 'visibility' in observation:
        observation['visibility'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['visibility'])),
                1,
            ),
            'm', 'Xpad',
        )

    if 'wind' in observation:
        observation['wind']['speed'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['wind']['speed'])) * 100,
                244,
            ),
            'm/s', 'veg',
        )
        observation['wind']['gust'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['wind']['gust'])) * 100,
                244,
            ),
            'm/s', 'veg',
        )
        observation['wind']['deg'] = decimal_to_sezimal_unit(
            SezimalFraction(
                Decimal(str(observation['wind']['deg'])) * 100,
                244,
            ),
            'deg', 'dmdl',
        )

    if 'dt' in observation:
        observation['dt'] = SezimalDateTime.from_timestamp(
            observation['dt'],
            'UTC',
        ).at_time_zone(time_zone)

    if 'sys' in observation:
        observation['sys']['sunrise'] = SezimalDateTime.from_timestamp(
            observation['sys']['sunrise'],
            'UTC',
        )
        observation['sys']['sunset'] = SezimalDateTime.from_timestamp(
            observation['sys']['sunset'],
            'UTC',
        )

    polution = get_polution(api_key, latitude, longitude)

    if polution:
        for name in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']:
            polution['components'][name] = decimal_to_sezimal_unit(
                SezimalFraction(
                    Decimal(str(polution['components'][name])) * 100,
                    244,
                ),
                'µg/m³', 'dtgnt',
            )

    observation['polution'] = polution
    #
    # Save this reading for future reference
    #
    observation['api_type'] = 'open_weather_map'
    filename = os.path.expanduser(f'~/.sezimal/weather__{str(latitude).replace('.', '_')}__{str(longitude).replace('.', '_')}.json')
    open(filename, 'w').write(json.dumps(observation))

    return observation


def fill_sezimal_weather(weather: SezimalWeather, conditions: dict):
    if 'weather' in conditions:
        weather._emoji = _EMOJI[conditions['weather'][0]['id']]

    if 'temp' in conditions['main']:
        weather._temperature = Sezimal(conditions['main']['temp'])

    if 'feels_like' in conditions['main']:
        weather._temperature_sensation = Sezimal(conditions['main']['feels_like'])

    if 'temp_max' in conditions['main']:
        weather._temperature_maximum = Sezimal(conditions['main']['temp_max'])

    if 'temp_min' in conditions['main']:
        weather._temperature_minimum = Sezimal(conditions['main']['temp_min'])

    if 'wind' in conditions:
        wind = conditions['wind']

        if 'speed' in wind:
            weather._wind_speed = Sezimal(wind['speed'])

        if 'gust' in wind:
            weather._wind_gust = Sezimal(wind['gust'])

        if 'deg' in wind:
            weather._wind_direction = Sezimal(wind['deg'])

    if 'humidity' in conditions['main']:
        weather._humidity = Sezimal(conditions['main']['humidity'])

    if 'visibility' in conditions:
        weather._visibility = Sezimal(conditions['visibility'])

    if 'grnd_level' in conditions['main']:
        weather._pressure = Sezimal(conditions['main']['grnd_level'])

    if 'sea_level' in conditions['main']:
        weather._pressure_sea_level = Sezimal(conditions['main']['sea_level'])

    if 'sys' in conditions:
        weather.sunrise = SezimalDateTime(str(conditions['sys']['sunrise']))
        weather.sunset = SezimalDateTime(str(conditions['sys']['sunset']))

    if 'polution' in conditions:
        polution = conditions['polution']

        weather._air_quality = polution['main']['aqi']


def get_polution(api_key: str, latitude: float = None, longitude: float = None) -> dict:
    url = f'https://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}'

    req = requests.get(url)

    observation = json.loads(req.text)

    if not 'list' in observation:
        return

    observation = observation['list'][0]

    return observation


_EMOJI = {
    # Group 2xx: Thunderstorm
    # 200 	Thunderstorm 	thunderstorm with light rain 	11d
    # 201 	Thunderstorm 	thunderstorm with rain 	11d
    # 202 	Thunderstorm 	thunderstorm with heavy rain 	11d
    # 210 	Thunderstorm 	light thunderstorm 	11d
    # 211 	Thunderstorm 	thunderstorm 	11d
    # 212 	Thunderstorm 	heavy thunderstorm 	11d
    # 221 	Thunderstorm 	ragged thunderstorm 	11d
    # 230 	Thunderstorm 	thunderstorm with light drizzle 	11d
    # 231 	Thunderstorm 	thunderstorm with drizzle 	11d
    # 232 	Thunderstorm 	thunderstorm with heavy drizzle 	11d
    200: '⛈\ufe0f️',
    201: '⛈\ufe0f️🌨\ufe0f️',
    202: '⛈\ufe0f️🌨\ufe0f️🌨\ufe0f️',
    210: '🌩\ufe0f️',
    211: '🌩\ufe0f️',
    212: '🌩\ufe0f️🌩\ufe0f️',
    221: '🌩\ufe0f️🌩\ufe0f️🌩\ufe0f️',
    230: '⛈\ufe0f️',
    231: '⛈\ufe0f️🌨\ufe0f️',
    232: '⛈\ufe0f️🌨\ufe0f️🌨\ufe0f️',

    # Group 3xx: Drizzle
    # 300 	Drizzle 	light intensity drizzle 	09d
    # 301 	Drizzle 	drizzle 	09d
    # 302 	Drizzle 	heavy intensity drizzle 	09d
    # 310 	Drizzle 	light intensity drizzle rain 	09d
    # 311 	Drizzle 	drizzle rain 	09d
    # 312 	Drizzle 	heavy intensity drizzle rain 	09d
    # 313 	Drizzle 	shower rain and drizzle 	09d
    # 314 	Drizzle 	heavy shower rain and drizzle 	09d
    # 321 	Drizzle 	shower drizzle 	09d
    300: '☔\ufe0f️',
    301: '☔\ufe0f️',
    302: '☔\ufe0f️☔\ufe0f️',
    310: '☔\ufe0f️',
    311: '☔\ufe0f️',
    312: '☔\ufe0f️☔\ufe0f️',
    313: '☔\ufe0f️☔\ufe0f️☔\ufe0f️',
    314: '☔\ufe0f️☔\ufe0f️☔\ufe0f️',
    321: '☔\ufe0f️☔\ufe0f️☔\ufe0f️',

    # Group 5xx: Rain
    # 500 	Rain 	light rain 	10d
    # 501 	Rain 	moderate rain 	10d
    # 502 	Rain 	heavy intensity rain 	10d
    # 503 	Rain 	very heavy rain 	10d
    # 504 	Rain 	extreme rain 	10d
    # 511 	Rain 	freezing rain 	13d
    # 520 	Rain 	light intensity shower rain 	09d
    # 521 	Rain 	shower rain 	09d
    # 522 	Rain 	heavy intensity shower rain 	09d
    # 531 	Rain 	ragged shower rain 	09d
    500: '🌦\ufe0f️',
    501: '🌧\ufe0f️',
    502: '🌧\ufe0f️🌧\ufe0f️',
    503: '🌧\ufe0f️🌧\ufe0f️🌧\ufe0f️',
    504: '🌧\ufe0f️🪣\ufe0f️',
    511: '🌧\ufe0f️🧊\ufe0f️',
    520: '🌧\ufe0f️',
    521: '🌧\ufe0f️',
    522: '🌧\ufe0f️🌧\ufe0f️',
    531: '🌧\ufe0f️🌧\ufe0f️🌧\ufe0f️',

    # Group 6xx: Snow
    # 600 	Snow 	light snow 	13d
    # 601 	Snow 	snow 	13d
    # 602 	Snow 	heavy snow 	13d
    # 611 	Snow 	sleet 	13d
    # 612 	Snow 	light shower sleet 	13d
    # 613 	Snow 	shower sleet 	13d
    # 615 	Snow 	light rain and snow 	13d
    # 616 	Snow 	rain and snow 	13d
    # 620 	Snow 	light shower snow 	13d
    # 621 	Snow 	shower snow 	13d
    # 622 	Snow 	heavy shower snow 	13d
    600: '🌨️\ufe0f️',
    601: '🌨️\ufe0f️',
    602: '🌨️\ufe0f️🌨️\ufe0f️',
    611: '🌨️\ufe0f️🧊\ufe0f️💧\ufe0f️',
    612: '🌨️\ufe0f️🧊\ufe0f️💧\ufe0f️',
    613: '🌨️\ufe0f️🧊\ufe0f️💧\ufe0f️',
    615: '🌧\ufe0f️🌨️\ufe0f️',
    616: '🌧\ufe0f️🌨️\ufe0f️',
    620: '🌧\ufe0f️🌨️\ufe0f️',
    621: '🌧\ufe0f️🌨️\ufe0f️',
    622: '🌧\ufe0f️🌨️\ufe0f️🌨️\ufe0f️',

    # Group 7xx: Atmosphere
    # 701 	Mist 	mist 	50d
    # 711 	Smoke 	smoke 	50d
    # 721 	Haze 	haze 	50d
    # 731 	Dust 	sand/dust whirls 	50d
    # 741 	Fog 	fog 	50d
    # 751 	Sand 	sand 	50d
    # 761 	Dust 	dust 	50d
    # 762 	Ash 	volcanic ash 	50d
    # 771 	Squall 	squalls 	50d
    # 781 	Tornado 	tornado 	50d
    701: '😶‍🌫️\ufe0f️',
    711: '😶‍🌫️\ufe0f️',
    721: '😶‍🌫️\ufe0f️',
    731: '💨\ufe0f️🏜️\ufe0f️',
    741: '😶‍🌫️\ufe0f️',
    751: '🏜️\ufe0f️',
    761: '😶‍🌫️\ufe0f️',
    762: '🌋\ufe0f️',
    771: '🌬\ufe0f️',
    781: '🌪\ufe0f️',

    # Group 800: Clear
    # 800 	Clear 	clear sky 	01d
    800: '☀\ufe0f️',

    # Group 80x: Clouds
    # 801 	Clouds 	few clouds: 11-25% 	02d
    # 802 	Clouds 	scattered clouds: 25-50% 	03d
    # 803 	Clouds 	broken clouds: 51-84% 	04d
    # 804 	Clouds 	overcast clouds: 85-100% 	04d
    801: '🌥\ufe0f️',
    802: '☁\ufe0f️',
    803: '☁\ufe0f️☁\ufe0f️',
    804: '☁\ufe0f️☁\ufe0f️☁\ufe0f️',
}
