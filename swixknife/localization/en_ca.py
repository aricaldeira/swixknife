

__all__ = ('SezimalLocaleEN_CA',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_CA(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Canadian English'

    DEFAULT_TIME_ZONE = 'America/Toronto'

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

    SEASON_EMOJI_NORTHERN_HEMISPHERE = {
        'spring_cross_quarter': '\ufe0f❄️\ufe0f〰\ufe0f🌱',
        'spring_equinox': '\ufe0f🌱',
        'summer_cross_quarter': '\ufe0f🌱\ufe0f〰\ufe0f🌞',
        'summer_solstice': '\ufe0f🌞',
        'autumn_cross_quarter': '\ufe0f🌞\ufe0f〰\ufe0f🍁',
        'autumn_equinox': '\ufe0f🍁',
        'winter_cross_quarter': '\ufe0f🍁\ufe0f〰\ufe0f❄️',
        'winter_solstice': '\ufe0f❄️',
    }
