

__all__ = ('SezimalLocaleFR_LU',)


from .fr_fr import SezimalLocaleFR_FR


class SezimalLocaleFR_LU(SezimalLocaleFR_FR):
    LANG = 'fr'
    LANGUAGE = 'français de Luxembourg'

    DEFAULT_TIME_ZONE = 'Europe/Luxembourg'
