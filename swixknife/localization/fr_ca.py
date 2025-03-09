

__all__ = ('SezimalLocaleFR_CA',)


from .fr import SezimalLocaleFR


class SezimalLocaleFR_CA(SezimalLocaleFR):
    LANG = 'fr'
    LANGUAGE = 'français canadien'

    DEFAULT_TIME_ZONE = 'America/Montreal'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    SEASON_EMOJI_NORTHERN_HEMISPHERE = {
        'spring_cross_quarter': '❄️\ufe0f\ufe0f〰\ufe0f🌱\ufe0f',
        'spring_equinox': '🌱\ufe0f',
        'summer_cross_quarter': '🌱\ufe0f〰\ufe0f🌞\ufe0f',
        'summer_solstice': '🌞\ufe0f',
        'autumn_cross_quarter': '🌞\ufe0f〰\ufe0f🍁\ufe0f',
        'autumn_equinox': '🍁\ufe0f',
        'winter_cross_quarter': '🍁\ufe0f〰\ufe0f❄️\ufe0f',
        'winter_solstice': '❄️\ufe0f',
    }

    HOLIDAYS = [
        #
        # Moving Holidays
        #
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Vendredi saint #𝑠𝑦𝑚'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Pâques #𝑠𝑦𝑚'),
        ('EASTER+1',   '🐣\ufe0f🌱\ufe0f Lundi de Pâques #𝑠𝑦𝑚'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Jour de l’An #𝑠𝑦𝑚'),
        ('10-40', '🇫🇮\ufe0f Saint-Jean-Baptiste #𝑠𝑦𝑚'),
        ('13-44', '🇨🇦\ufe0f Journée de la vérité et de la réconciliation #𝑠𝑦𝑚'),
        ('15-15', '🪦\ufe0f🪖\ufe0f Jour du Souvenir #𝑠𝑦𝑚'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Noël #𝑠𝑦𝑚'),
        ('20-42', '🎁\ufe0f Lendemain de Noël #𝑠𝑦𝑚'),

        #
        # Fixed day of the week holidays
        #
        ('13-01', '🐝\ufe0f🐜\ufe0f Fête du travail #𝑠𝑦𝑚'),
        ('05-34', '👸\ufe0f🏻\ufe0f Journée nationale des patriotes #𝑠𝑦𝑚'),
        ('12-01', '🇨🇦\ufe0f Premier lundi d’août #𝑠𝑦𝑚'),
        ('14-12', '🙏\ufe0f Action de grâce #𝑠𝑦𝑚'),

        #
        # And the one’s that do have a year of reference
        #
        ('212_351-11-01', '🇨🇦\ufe0f Fête du Canada (#i) #𝑠𝑦𝑚'),
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Vendredi saint'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Pâques'),
        ('ISO+EASTER+1',   '🐣\ufe0f🌱\ufe0f Lundi de Pâques'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f Jour de l’An'),
        ('ISO+06-24', '🇫🇮\ufe0f Saint-Jean-Baptiste'),
        ('ISO+09-30', '🇨🇦\ufe0f Journée de la vérité et de la réconciliation'),
        ('ISO+11-11', '🪦\ufe0f🪖\ufe0f Jour du Souvenir'),
        ('ISO+12-25', '🌟\ufe0f👼🏼\ufe0f Noël'),
        ('ISO+12-26', '🎁\ufe0f Lendemain de Noël'),

        #
        # Fixed day of the week holidays
        #
        ('ISO+09-01+MON', '🐝\ufe0f🐜\ufe0f Fête du travail'),
        ('ISO+05-24-MON', '👸\ufe0f🏻\ufe0f Journée nationale des patriotes'),
        ('ISO+08-01+MON', '🇨🇦\ufe0f Premier lundi d’août'),
        ('ISO+10-01+MON_2', '🙏\ufe0f Action de grâce'),

        #
        # And the one’s that do have a year of reference
        #
        ('ISO+1867-07-01', '🇨🇦\ufe0f Fête du Canada (%i)'),
    ]
