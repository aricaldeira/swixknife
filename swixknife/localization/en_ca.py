

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

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO-EASTER-2',   '\ufe0f🕆 🥀 Good Friday (%d/%m)'),
        ('ISO-EASTER',     '\ufe0f🐣🌱 Easter (%d/%m)'),
        ('ISO-EASTER+1',   '\ufe0f🐣🌱 Easter Monday (%d/%m)'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO-01-01', '\ufe0f🕊️ 🌎 New Year’s Day'),
        ('ISO-09-30', '\ufe0f🇨🇦 Truth and Reconciliation Day (%d/%m)'),
        ('ISO-06-24', '\ufe0f🇫🇮 Saint-Jean-Baptiste (%d/%m)'),
        ('ISO-11-11', '\ufe0f🪦🪖 Rememberance Day (%d/%m)'),
        ('ISO-12-25', '\ufe0f🌟👼🏼 Christmas Day'),
        ('ISO-12-26', '\ufe0f🎁 Boxing Day'),

        #
        # Fixed day of the week holidays
        #
        ('ISO-09-01+MON', '\ufe0f🐝🐜 Labour Day (%d/%m)'),
        ('ISO-05-24-MON', '\ufe0f👸🏻 Victoria Day (%d/%m)'),
        ('ISO-08-01+MON', '\ufe0f🇨🇦 Civic Holiday (%d/%m)'),
        ('ISO-10-01+MON_2', '\ufe0f🙏 Thanks Giving Day (%d/%m)'),

        #
        # And the one’s that do have a year of reference
        #
        ('ISO-1867-07-01', '\ufe0f🇨🇦 Canada Day (%d/%m - %i)'),
    ]
