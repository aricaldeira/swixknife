

__all__ = ('SezimalLocaleBZ_PT',)


from .bz import SezimalLocaleBZ


class SezimalLocaleBZ_PT(SezimalLocaleBZ):
    LANG = 'bz'
    LANGUAGE = 'brazileru'
    LANGUAGE_TAG = 'bz-PT'

    DEFAULT_TIME_ZONE = 'Europe/Lisbon'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
