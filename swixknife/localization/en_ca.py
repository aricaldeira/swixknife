

__all__ = ('SezimalLocaleEN_CA',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_CA(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Canadian English'

    DEFAULT_TIME_ZONE = 'America/Toronto'
    ISO_TIME_FORMAT = '%I:%M:%S %p'
    ISO_SHORT_TIME_FORMAT = '%I:%M %p'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

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
        'spring_cross_quarter': '❄️〰\ufe0f🌱\ufe0f',
        'spring_equinox': '🌱\ufe0f',
        'summer_cross_quarter': '🌱\ufe0f〰\ufe0f🌞\ufe0f',
        'summer_solstice': '🌞\ufe0f',
        'autumn_cross_quarter': '🌞\ufe0f〰\ufe0f🍁\ufe0f',
        'autumn_equinox': '🍁\ufe0f',
        'winter_cross_quarter': '🍁\ufe0f〰❄️\ufe0f',
        'winter_solstice': '❄️',
    }

    HOLIDAYS = [
        #
        # Moving Holidays
        #
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Good Friday #Sym454'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Easter #Sym454'),
        ('EASTER+1',   '🐣\ufe0f🌱\ufe0f Easter Monday #Sym454'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f New Year’s Day #Sym454'),
        ('13-44', '🇨🇦\ufe0f Truth and Reconciliation Day #Sym454'),
        ('10-40', '🇫🇮\ufe0f Saint-Jean-Baptiste #Sym454'),
        ('15-15', '🪦\ufe0f🪖\ufe0f Rememberance Day #Sym454'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Christmas Day #Sym454'),
        ('20-42', '🎁\ufe0f Boxing Day #Sym454'),

        #
        # Fixed day of the week holidays
        #
        ('13-01', '🐝\ufe0f🐜\ufe0f Labour Day #Sym454'),
        ('05-34', '👸\ufe0f🏻\ufe0f Victoria Day #Sym454'),
        ('12-01', '🇨🇦\ufe0f Civic Holiday #Sym454'),
        ('14-12', '🙏\ufe0f Thanks Giving Day #Sym454'),

        #
        # And the one’s that do have a year of reference
        #
        ('212_351-11-01', '🇨🇦\ufe0f Canada Day (#i) #Sym454'),
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Good Friday'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Easter'),
        ('ISO+EASTER+1',   '🐣\ufe0f🌱\ufe0f Easter Monday'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f New Year’s Day'),
        ('ISO+09-30', '🇨🇦\ufe0f Truth and Reconciliation Day'),
        ('ISO+06-24', '🇫🇮\ufe0f Saint-Jean-Baptiste'),
        ('ISO+11-11', '🪦\ufe0f🪖\ufe0f Rememberance Day'),
        ('ISO+12-25', '🌟\ufe0f👼🏼\ufe0f Christmas Day'),
        ('ISO+12-26', '🎁\ufe0f Boxing Day'),

        #
        # Fixed day of the week holidays
        #
        ('ISO+09-01+MON', '🐝\ufe0f🐜\ufe0f Labour Day'),
        ('ISO+05-24-MON', '👸\ufe0f🏻\ufe0f Victoria Day'),
        ('ISO+08-01+MON', '🇨🇦\ufe0f Civic Holiday'),
        ('ISO+10-01+MON_2', '🙏\ufe0f Thanks Giving Day'),

        #
        # And the one’s that do have a year of reference
        #
        ('ISO+1867-07-01', '🇨🇦\ufe0f Canada Day (%i)'),
    ]
