

__all__ = ('SezimalLocaleES_MX',)


from .es_mx import SezimalLocaleES_MX
from .en_us import SezimalLocaleEN_US

from ..base import SEPARATOR_COMMA, SEPARATOR_DOT


class SezimalLocaleES_US(SezimalLocaleES_MX):
    LANG = 'es'
    LANGUAGE = 'español de los Estados Unidos'

    DEFAULT_TIME_ZONE = 'US/Eastern'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT
    GROUP_SEPARATOR = SEPARATOR_COMMA

    FIRST_WEEKDAY = 'SUN'
    DECIMAL_TEMPERATURE = '°F'
    DECIMAL_SPEED = 'mph'

    HOLIDAYS = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('01-01', '🎆\ufe0f Año Nuevo #sym'),
        ('212_120-11-04', '🇺🇸\ufe0f Día de la Independencia (#i) #sym'),  # Thursday 212_120-11-04 ~ 1776-07-04_dec
        ('10-31', '🇺🇸\ufe0f Juneteenth #sym'),
        ('14-44', '🎃\ufe0f🍬\ufe0f Halloween #sym'),
        ('15-15', '🇺🇸\ufe0f Día de los Veteranos #sym'),
        ('20-41', '🎄\ufe0f Navidad #sym'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('01-23', '🇺🇸\ufe0f Día de Martin Luther King, Jr. #sym'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('02-23', '🇺🇸\ufe0f Día de los Presidientes #sym'),   # Third Monday in February
        ('05-45', '🇺🇸\ufe0f Día de la Comemoración de los Caídos #sym'),      # Last Monday in May
        ('13-01', '🐝\ufe0f Día del Trabajo #sym'),        # First Monday in September
        ('14-12', '🇺🇸\ufe0f Día de Colón #sym'),      # Second Monday in October
        ('15-41', '🦃\ufe0f Día de Acción de Gracias #sym'),  # Fourth Thursday in November
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('ISO-01-01', '🎆\ufe0f Año Nuevo'),
        ('ISO-1776-07-04', '🇺🇸\ufe0f Día de la Independencia (%i)'),  # Thursday 130_304-11-04 ~ 1776-07-04_dec
        ('ISO-06-19', '🇺🇸\ufe0f Juneteenth'),
        ('ISO-10-31', '🎃\ufe0f🍬\ufe0f Halloween'),
        ('ISO-11-11', '🇺🇸\ufe0f Día de los Veteranos'),
        ('ISO-12-25', '🎄\ufe0f Navidad'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('ISO-01-01+MON_3', '🇺🇸\ufe0f Día de Martin Luther King, Jr.'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('ISO-02-01+MON_3', '🇺🇸\ufe0f Día de los Presidientes'),   # Third Monday in February
        ('ISO-05-31-MON', '🇺🇸\ufe0f Día de la Comemoración de los Caídos'),      # Last Monday in May
        ('ISO-09-01+MON', '🐝\ufe0f Día del Trabajo'),        # First Monday in September
        ('ISO-10-01+MON_2', '🇺🇸\ufe0f Día de Colón'),      # Second Monday in October
        ('ISO−11-01+THU_4', '🦃\ufe0f Día de Acción de Gracias'),  # Fourth Thursday in November
    ]
