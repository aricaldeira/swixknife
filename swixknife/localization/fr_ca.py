

__all__ = ('SezimalLocaleFR_CA',)


from .fr import SezimalLocaleFR


class SezimalLocaleFR_CA(SezimalLocaleFR):
    LANG = 'fr'
    LANGUAGE = 'français canadien'

    DEFAULT_TIME_ZONE = 'America/Montreal'

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
        ('ISO-EASTER-2',   '\ufe0f🕆 🥀 Vendredi saint (%d/%m)'),
        # ('ISO-EASTER',     '\ufe0f🐣🌱 Pâques (%d/%m)'),
        ('ISO-EASTER+1',   '\ufe0f🐣🌱 Lundi de Pâques (%d/%m)'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO-01-01', '\ufe0f🕊️ 🌎 Jour de l’An'),
        ('ISO-06-24', '\ufe0f🇫🇮 Saint-Jean-Baptiste (%d/%m)'),
        ('ISO-09-30', '\ufe0f🇨🇦 Journée de la vérité et de la réconciliation (%d/%m)'),
        ('ISO-11-11', '\ufe0f🪦🪖 Jour du Souvenir (%d/%m)'),
        ('ISO-12-25', '\ufe0f🌟👼🏼 Noël'),
        ('ISO-12-26', '\ufe0f🎁 Lendemain de Noël'),

        #
        # Fixed day of the week holidays
        #
        ('ISO-09-01+MON', '\ufe0f🐝🐜 Fête du travail (%d/%m)'),
        ('ISO-05-24-MON', '\ufe0f👸🏻 Journée nationale des patriotes (%d/%m)'),
        ('ISO-08-01+MON', '\ufe0f🇨🇦 Premier lundi d’août (%d/%m)'),
        ('ISO-10-01+MON_2', '\ufe0f🙏 Action de grâce (%d/%m)'),

        #
        # And the one’s that do have a year of reference
        #
        ('ISO-1867-07-01', '\ufe0f🇨🇦 Fête du Canada (%d/%m - %i)'),
    ]
