

__all__ = ('SezimalLocaleFR',)


from .fr import SezimalLocaleFR


class SezimalLocaleFR_CA(SezimalLocaleFR):
    LANG = 'fr'
    LANGUAGE = 'français canadien'

    DEFAULT_TIME_ZONE = 'America/Toronto'

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
