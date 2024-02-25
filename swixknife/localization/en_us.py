

__all__ = ('SezimalLocaleEN_US',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_US(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'American English'

    DATE_FORMAT = '#m/#d/#Y'
    DATE_LONG_FORMAT = '#M #-d, #Y'
    DATE_TIME_FORMAT = ' #@W #m/#d/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #M #-d, #Y, #u:#p:#a'

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
        ('01-01', '\ufe0f🎆 New Year’s Day'),
        ('130_304-11-04', '\ufe0f🇺🇸 Independence Day (#i)'),  # Thursday 130_304-11-04 ~ 1776-07-04_dec
        ('10-31', '\ufe0f🇺🇸 Juneteenth Day'),
        ('15-15', '\ufe0f🇺🇸 Veterans’ Day'),
        ('20-41', '\ufe0f🎄 Christmas’ Day'),

        #
        # National Holidays
        # that occur on a specific weekday
        #
        ('01-23', '\ufe0f🇺🇸 Martin Luther King, Jr. Day'), # Monday, the 23rd of Jan. ~ Monday, the 15th of Jan.
        # ('01-32', 'Inauguration Day'),
        ('02-23', '\ufe0f🇺🇸 Presidents’ Day'),   # Third Monday in February
        ('05-45', '\ufe0f🇺🇸 Memorial Day'),      # Last Monday in May
        ('13-01', '\ufe0f🐝 Labour Day'),        # First Monday in September
        ('14-12', '\ufe0f🇺🇸 Columbus Day'),      # Second Monday in October
        ('15-40', '\ufe0f🦃 Thanksgiving Day'),  # Fourth Thursday in November
    ]
