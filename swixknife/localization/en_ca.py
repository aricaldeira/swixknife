

__all__ = ('SezimalLocaleEN_CA',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_CA(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Canadian English'

    DEFAULT_TIME_ZONE = 'America/Toronto'
    ISO_TIME_FORMAT = '%I:%M:%S %p'
    ISO_HOUR_MINUTE_FORMAT = '%I:%M %p'

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
        'spring_cross_quarter': '❄️〰🌱',
        'spring_equinox': '🌱',
        'summer_cross_quarter': '🌱〰🌞',
        'summer_solstice': '🌞',
        'autumn_cross_quarter': '🌞〰🍁',
        'autumn_equinox': '🍁',
        'winter_cross_quarter': '🍁〰❄️',
        'winter_solstice': '❄️',
    }

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('EASTER-2',   '🕆🥀 Good Friday #Sym454'),
        ('EASTER',     '🐣🌱 Easter #Sym454'),
        ('EASTER+1',   '🐣🌱 Easter Monday #Sym454'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊️ 🌎 New Year’s Day #Sym454'),
        ('13-44', '🇨🇦 Truth and Reconciliation Day #Sym454'),
        ('10-40', '🇫🇮 Saint-Jean-Baptiste #Sym454'),
        ('15-15', '🪦🪖 Rememberance Day #Sym454'),
        ('20-41', '🌟👼🏼 Christmas Day #Sym454'),
        ('20-42', '🎁 Boxing Day #Sym454'),

        #
        # Fixed day of the week holidays
        #
        ('13-01', '🐝🐜 Labour Day #Sym454'),
        ('05-34', '👸🏻 Victoria Day #Sym454'),
        ('12-01', '🇨🇦 Civic Holiday #Sym454'),
        ('14-12', '🙏 Thanks Giving Day #Sym454'),

        #
        # And the one’s that do have a year of reference
        #
        ('212_351-11-01', '🇨🇦 Canada Day (#i) #Sym454'),
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO+EASTER-2',   '🕆🥀 Good Friday (%d/%m)'),
        ('ISO+EASTER',     '🐣🌱 Easter (%d/%m)'),
        ('ISO+EASTER+1',   '🐣🌱 Easter Monday (%d/%m)'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊️ 🌎 New Year’s Day'),
        ('ISO+09-30', '🇨🇦 Truth and Reconciliation Day (%d/%m)'),
        ('ISO+06-24', '🇫🇮 Saint-Jean-Baptiste (%d/%m)'),
        ('ISO+11-11', '🪦🪖 Rememberance Day (%d/%m)'),
        ('ISO+12-25', '🌟👼🏼 Christmas Day'),
        ('ISO+12-26', '🎁 Boxing Day'),

        #
        # Fixed day of the week holidays
        #
        ('ISO+09-01+MON', '🐝🐜 Labour Day (%d/%m)'),
        ('ISO+05-24-MON', '👸🏻 Victoria Day (%d/%m)'),
        ('ISO+08-01+MON', '🇨🇦 Civic Holiday (%d/%m)'),
        ('ISO+10-01+MON_2', '🙏 Thanks Giving Day (%d/%m)'),

        #
        # And the one’s that do have a year of reference
        #
        ('ISO+1867-07-01', '🇨🇦 Canada Day (%d/%m - %i)'),

        ('HEB+11-15', '🌳💮 Tu biShvat (%d/%m/%Y)'),
        ('HEB+12-14', '🍷🍬 Purim (%d/%m/%Y)'),
        ('HEB+01-15', '🐑🫓 Pesach (%d/%m/%Y)'),
        ('HEB+02-14', '🐑🫓 Pesach Sheni (%d/%m/%Y)'),
        ('HEB+02-18', '🔥 Lag baOmer (%d/%m/%Y)'),
        ('HEB+03-06', '💐📜 Shavuot (%d/%m/%Y)'),
        ('HEB+05-09', '🕍🔥 Tisha b’Av (%d/%m/%Y)'),

        ('HEB+07-01', '🍎🍯 Rosh haShaná (%d/%m/%Y)'),
        ('HEB+07-10', '🤍🙏🏻 Yom Kippur (%d/%m/%Y)'),
        ('HEB+07-15', '🍋⛺ Sukkot (%d/%m/%Y)'),
        ('HEB+07-22', '🙏🏻🌧️ Shemini Atzeret (%d/%m/%Y)'),
        ('HEB+07-23', '😊📜 Simchat Torah (%d/%m/%Y)'),
        ('HEB+09-25', '🕯🕍 Hanukkah (%d/%m/%Y)'),
    ]
