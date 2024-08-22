

__all__ = ('SezimalWeather',)

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalWeather')
ZoneInfo = TypeVar('ZoneInfo', bound='ZoneInfo')

import os

from ..sezimal import Sezimal, SezimalInteger
from ..date_time import SezimalDate, SezimalTime, SezimalDateTime
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from ..user_preferences import user_preferences
from ..json import json


class SezimalWeather:
    def __new__(
        cls,
        locale: str | SezimalLocale = None,
        time_zone: str | ZoneInfo = None,
        use_last_reading: bool = False,
    ) -> Self:
        self = object.__new__(cls)

        if locale:
            if isinstance(locale, SezimalLocale):
                lang = locale.LANG
            else:
                lang = locale
                locale = sezimal_locale(lang)

        else:
            locale = DEFAULT_LOCALE
            lang = locale.LANG

        self.locale = locale
        self.lang = lang
        self.time_zone = time_zone
        self._reference_date_time = None
        self._sunrise_date_time = None
        self._sunset_date_time = None
        self._wind_speed = SezimalInteger(0)
        self._wind_gust = SezimalInteger(0)
        self._wind_direction = Sezimal(0)
        self._humidity = SezimalInteger(0)
        self._pressure = SezimalInteger(0)
        self._pressure_sea_level = SezimalInteger(0)
        self._temperature = SezimalInteger(0)
        self._temperature_sensation = SezimalInteger(0)
        self._temperature_maximum = SezimalInteger(0)
        self._temperature_minimum = SezimalInteger(0)
        self._clouds = SezimalInteger(0)
        self._use_last_reading = use_last_reading

        return self

    @property
    def reference_date_time(self) -> SezimalDateTime:
        return self._reference_date_time

    @property
    def reference_date_time_formatted(self) -> str:
        return self._reference_date_time.format(locale=self.locale)

    @property
    def sunrise_date_time(self) -> SezimalDateTime:
        return self._sunrise_date_time

    @property
    def sunrise_date_time_formatted(self) -> str:
        return self._sunrise_date_time.format(self.locale.TIME_FORMAT, locale=self.locale)

    @property
    def sunset_date_time(self) -> SezimalDateTime:
        return self._sunset_date_time

    @property
    def sunset_date_time_formatted(self) -> str:
        return self._sunrise_date_time.format(self.locale.TIME_FORMAT, locale=self.locale)

    @property
    def wind_speed(self) -> SezimalInteger:
        return self._wind_speed

    @property
    def wind_speed_formatted(self) -> str:
        return self.locale.format_number(self._wind_speed, sezimal_places=0, suffix='veg')

    @property
    def wind_gust(self) -> SezimalInteger:
        return self._wind_gust

    @property
    def wind_gust_formatted(self) -> str:
        return self.locale.format_number(self._wind_gust, sezimal_places=0, suffix='veg')

    @property
    def wind_direction(self) -> Sezimal:
        return self._wind_direction

    @property
    def humidity(self) -> SezimalInteger:
        return self._humidity

    @property
    def humidity_formatted(self) -> str:
        return self.locale.format_number(self._humidity, sezimal_places=0, suffix='‰')

    @property
    def pressure(self) -> SezimalInteger:
        return self._pressure

    @property
    def pressure_formatted(self) -> str:
        return self.locale.format_number(self._pressure, sezimal_places=0, suffix='Cpdn')

    @property
    def pressure_sea_level(self) -> SezimalInteger:
        return self._pressure_sea_level

    @property
    def pressure_sea_level_formatted(self) -> str:
        return self.locale.format_number(self._pressure_sea_level, sezimal_places=0, suffix='Cpdn')

    @property
    def temperature(self) -> SezimalInteger:
        return self._temperature

    @property
    def temperature_formatted(self) -> str:
        return self.locale.format_number(self._temperature, sezimal_places=0, suffix='°S')

    @property
    def temperature_sensation(self) -> SezimalInteger:
        return self._temperature_sensation

    @property
    def temperature_sensation_formatted(self) -> str:
        return self.locale.format_number(self._temperature_sensation, sezimal_places=0, suffix='°S')

    @property
    def temperature_maximum(self) -> SezimalInteger:
        return self._temperature_maximum

    @property
    def temperature_maximum_formatted(self) -> str:
        return self.locale.format_number(self._temperature_maximum, sezimal_places=0, suffix='°S')

    @property
    def temperature_minimum(self) -> SezimalInteger:
        return self._temperature_minimum

    @property
    def temperature_minimum_formatted(self) -> str:
        return self.locale.format_number(self._temperature_minimum, sezimal_places=0, suffix='°S')

    @property
    def clouds(self) -> SezimalInteger:
        return self._clouds

    @property
    def clouds_formatted(self) -> str:
        return self.locale.format_number(self._clouds, sezimal_places=0, suffix='‰')

    @property
    def visibility(self) -> SezimalInteger:
        return self._visibility

    @property
    def visibility_formatted(self) -> str:
        return self.locale.format_number(self._visibility, sezimal_places=0, suffix='Cpad')

    def get_openweathermap_conditions(self, api_key: str = None, latitude: float = None, longitude: float = None):
        from .open_weather_map import get_weather_conditions, fill_sezimal_weather

        if self._use_last_reading \
            and self._get_last_reading('open_weather_map', fill_sezimal_weather):
            return

        lang = self.lang

        if lang == 'bz':
            lang = 'pt-br'

        if not (api_key and latitude and longitude):
            up = user_preferences(self.locale)

            if (not api_key) and 'OPENWEATHERMAP_API_KEY' in up:
                api_key = up['OPENWEATHERMAP_API_KEY']

            if (not latitude) and 'WEATHER_LATITUDE' in up:
                latitude = up['WEATHER_LATITUDE']

            if (not longitude) and 'WEATHER_LONGITUDE' in up:
                longitude = up['WEATHER_LONGITUDE']

        conditions = get_weather_conditions(
            api_key=api_key, latitude=latitude, longitude=longitude,
            time_zone=self.time_zone,
        )

        fill_sezimal_weather(self, conditions)

    def get_weatherapi_conditions(self, api_key: str = None, location: str = None, latitude: float = None, longitude: float = None):
        from .weather_api import get_weather_conditions, fill_sezimal_weather

        if self._use_last_reading \
            and self._get_last_reading('weather_api', fill_sezimal_weather):
            return

        lang = self.lang

        if lang == 'bz':
            lang = 'pt'

        if not (api_key and (location or (latitude and longitude))):
            up = user_preferences(self.locale)

            if (not api_key) and 'WEATHER_API_KEY' in up:
                api_key = up['WEATHER_API_KEY']

            if (not latitude) and 'WEATHER_LATITUDE' in up:
                latitude = up['WEATHER_LATITUDE']

            if (not longitude) and 'WEATHER_LONGITUDE' in up:
                longitude = up['WEATHER_LONGITUDE']

            if (not location) and 'WEATHER_LOCATION' in up:
                location = up['WEATHER_LOCATION']

        conditions = get_weather_conditions(
            api_key=api_key, location=location, latitude=latitude, longitude=longitude,
            language=lang, time_zone=self.time_zone,
        )

        fill_sezimal_weather(self, conditions)

    def _get_last_reading(self, api_type: str, fill_sezimal_weather):
        if not os.path.isfile(os.path.expanduser('~/.sweather.json')):
            return False

        last_reading = json.loads(open(os.path.expanduser('~/.sweather.json'), 'r').read())

        if not 'api_type' in last_reading:
            return False

        if last_reading['api_type'] != api_type:
            return False

        fill_sezimal_weather(self, last_reading)

        return True
