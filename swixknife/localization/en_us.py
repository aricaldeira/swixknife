

__all__ = ('SezimalLocaleEN_US',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_US(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'American English'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    DEFAULT_TIME_ZONE = 'America/New_York'
    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#m/#d/#Y'
    DATE_LONG_FORMAT = '#M #-d, #Y'
    DATE_FULL_FORMAT = '#@W #m/#d/#Y'
    DATE_FULL_LONG_FORMAT = '#W, #M #-d, #Y'
    DATE_TIME_FORMAT = '#@W #m/#d/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #M #-d, #Y, #u:#p:#a'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    FIRST_WEEKDAY = 'SUN'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Summer',
        'autumn_cross_quarter': 'Fall Cross-Quarter',
        'autumn_equinox': 'Fall',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Winter',
    }

    HOLIDAYS = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('01-01', '🎆\ufe0f New Year’s Day #𝑠𝑦𝑚'),
        ('212_120-11-04', '🇺🇸\ufe0f Independence Day (#i) #𝑠𝑦𝑚'),  # Thursday 212_120-11-04 ~ 1776-07-04_dec
        ('212_350-10-23', '🇺🇸\ufe0f Juneteenth Day #𝑠𝑦𝑚'),
        ('14-44', '🎃\ufe0f🍬\ufe0f Halloween #𝑠𝑦𝑚'),
        ('15-15', '🇺🇸\ufe0f Veterans’ Day #𝑠𝑦𝑚'),
        ('20-41', '🎄\ufe0f Christmas’ Day #𝑠𝑦𝑚'),
        # ('202_045-03-20', '☘️\ufe0f St. Patrick’s Day #sym'),
        # ('212_342-05-12', '🇲🇽\ufe0f Ocho de Mayo #sym'),
        # ('212_141-11-24', '🇫🇷\ufe0f Bastille Day'),
        # ('213_001-12-12', '🇯🇵\ufe0f Anniversary of Hiroshima Bombing'),
        # ('213_213-13-13', '🇺🇸\ufe0f Patriot Day'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('01-23', '🇺🇸\ufe0f Martin Luther King, Jr. Day #𝑠𝑦𝑚'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('02-23', '🇺🇸\ufe0f Presidents’ Day #𝑠𝑦𝑚'),   # Third Monday in February
        ('05-45', '🇺🇸\ufe0f Memorial Day #𝑠𝑦𝑚'),      # Last Monday in May
        ('13-01', '🐝\ufe0f Labour Day #𝑠𝑦𝑚'),        # First Monday in September
        ('14-12', '🇺🇸\ufe0f Columbus Day #𝑠𝑦𝑚'),      # Second Monday in October
        ('15-41', '🦃\ufe0f Thanksgiving Day #𝑠𝑦𝑚'),  # Fourth Thursday in November
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('ISO-01-01', '🎆\ufe0f New Year’s Day'),
        ('ISO-1776-07-04', '🇺🇸\ufe0f Independence Day (%i)'),  # Thursday 130_304-11-04 ~ 1776-07-04_dec
        ('ISO-1866-06-19', '🇺🇸\ufe0f Juneteenth Day'),
        ('ISO-10-31', '🎃\ufe0f🍬\ufe0f Halloween'),
        ('ISO-11-11', '🇺🇸\ufe0f Veterans’ Day'),
        ('ISO-12-25', '🎄\ufe0f Christmas’ Day'),
        # ('JUL-0461-03-17', '☘️\ufe0f St. Patrick’s Day'),
        # ('ISO-03-17', '☘️\ufe0f St. Patrick’s Day'),
        # ('ISO-1862-05-05', '🇲🇽\ufe0f Cinco de Mayo'),
        # ('ISO-1789-07-14', '🇫🇷\ufe0f Bastille Day'),
        # ('ISO-1945-08-06', '🇯🇵\ufe0f Anniversary of Hiroshima Bombing'),
        # ('ISO-2001-09-11', '🇺🇸\ufe0f Patriot Day'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('ISO-01-01+MON_3', '🇺🇸\ufe0f Martin Luther King, Jr. Day'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('ISO-02-01+MON_3', '🇺🇸\ufe0f Presidents’ Day'),   # Third Monday in February
        ('ISO-05-31-MON', '🇺🇸\ufe0f Memorial Day'),      # Last Monday in May
        ('ISO-09-01+MON', '🐝\ufe0f Labour Day'),        # First Monday in September
        ('ISO-10-01+MON_2', '🇺🇸\ufe0f Columbus Day'),      # Second Monday in October
        ('ISO−11-01+THU_4', '🦃\ufe0f Thanksgiving Day'),  # Fourth Thursday in November
    ]

    DECIMAL_TEMPERATURE = '°F'
    DECIMAL_SPEED = 'mph'
