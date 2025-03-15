

__all__ = ('SezimalLocaleEO_US',)


from .eo import SezimalLocaleEO
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleEO_US(SezimalLocaleEO):
    SEZIMAL_SEPARATOR = SEPARATOR_DOT
    GROUP_SEPARATOR = SEPARATOR_COMMA

    DEFAULT_TIME_ZONE = 'America/Chicago'
    FIRST_WEEKDAY = 'SUN'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'
    DECIMAL_TEMPERATURE = '°F'
    DECIMAL_SPEED = 'mph'

    HOLIDAYS = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('01-01', '🎆\ufe0f Novjaro #𝑠𝑦𝑚'),
        ('212_120-11-04', '🇺🇸\ufe0f Tago de Sendependiĝo (#i) #𝑠𝑦𝑚'),  # Thursday 212_120-11-04 ~ 1776-07-04_dec
        ('10-31', '🇺🇸\ufe0f Juneteenth Day #𝑠𝑦𝑚'),
        ('14-44', '🎃\ufe0f🍬\ufe0f Haloveno #𝑠𝑦𝑚'),
        ('15-15', '🇺🇸\ufe0f Tago de Veteranoj #𝑠𝑦𝑚'),
        ('20-41', '🎄\ufe0f Kristnasko #𝑠𝑦𝑚'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('01-23', '🇺🇸\ufe0f Tago de Martin Luther King, Jr. #𝑠𝑦𝑚'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('02-23', '🇺🇸\ufe0f Tago de la Prezidentoj #𝑠𝑦𝑚'),   # Third Monday in February
        ('05-45', '🇺🇸\ufe0f Tago de la Falintoj #𝑠𝑦𝑚'),      # Last Monday in May
        ('13-01', '🐝\ufe0f Labortago #𝑠𝑦𝑚'),        # First Monday in September
        ('14-12', '🇺🇸\ufe0f Kolumbotago #𝑠𝑦𝑚'),      # Second Monday in October
        ('15-41', '🦃\ufe0f Dankotago #𝑠𝑦𝑚'),  # Fourth Thursday in November
    ] + SezimalLocaleEO.HOLIDAYS

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('ISO-01-01', '🎆\ufe0f Novjaro'),
        ('ISO-1776-07-04', '🇺🇸\ufe0f Tago de Sendependiĝo (%i)'),  # Thursday 130_304-11-04 ~ 1776-07-04_dec
        ('ISO-06-19', '🇺🇸\ufe0f Juneteenth Day'),
        ('ISO-10-31', '🎃\ufe0f🍬\ufe0f Haloveno'),
        ('ISO-11-11', '🇺🇸\ufe0f Tago de Veteranoj'),
        ('ISO-12-25', '🎄\ufe0f Kristnasko'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('ISO-01-01+MON_3', '🇺🇸\ufe0f Tago de Martin Luther King, Jr.'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('ISO-02-01+MON_3', '🇺🇸\ufe0f Tago de la Prezidentoj'),   # Third Monday in February
        ('ISO-05-31-MON', '🇺🇸\ufe0f Tago de la Falintoj'),      # Last Monday in May
        ('ISO-09-01+MON', '🐝\ufe0f Labortago'),        # First Monday in September
        ('ISO-10-01+MON_2', '🇺🇸\ufe0f Kolumbotago'),      # Second Monday in October
        ('ISO−11-01+THU_4', '🦃\ufe0f Dankotago'),  # Fourth Thursday in November
    ] + SezimalLocaleEO.HOLIDAYS_OTHER_CALENDAR
