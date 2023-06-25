

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
