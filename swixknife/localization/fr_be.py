

__all__ = ('SezimalLocaleFR_BE',)


from .fr_fr import SezimalLocaleFR_FR


class SezimalLocaleFR_BE(SezimalLocaleFR_FR):
    LANG = 'fr'
    LANGUAGE = 'français de Belgique'

    DEFAULT_TIME_ZONE = 'Europe/Brussels'
