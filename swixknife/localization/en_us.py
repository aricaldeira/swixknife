

__all__ = ('SezimalLocaleEN_US',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_US(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'American English'

    DATE_FORMAT = '#m/#d/#Y'
    DATE_LONG_FORMAT = '#M #-d, #Y'
    DATE_TIME_FORMAT = ' #@W #m/#d/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #M #-d, #Y, #u:#p:#a'

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

    HOLIDAYS = {
        '01-01': '\ufe0f🎆 New Year’s Day',
        '01-23': '\ufe0f🇺🇸 Martin Luther King, Jr. Day',
        # '01-32': 'Inauguration Day',
        '02-23': '\ufe0f🇺🇸 Presidents’ Day',
        '05-45': '\ufe0f🇺🇸 Memorial Day',
        '10-31': '\ufe0f🇺🇸 Juneteenth Day',
        '11-04': '\ufe0f🇺🇸 Independence Day',
        '13-01': '\ufe0f🐝 Labour Day',
        '14-12': '\ufe0f🇺🇸 Columbus Day',
        '15-15': '\ufe0f🇺🇸 Veterans’ Day',
        '15-40': '\ufe0f🦃 Thanksgiving Day',
        '20-41': '\ufe0f🎄 Christmas’ Day',
    }
