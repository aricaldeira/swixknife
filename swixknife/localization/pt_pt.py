

__all__ = ('SezimalLocalePT_PT',)


from .pt import SezimalLocalePT


class SezimalLocalePT_PT(SezimalLocalePT):
    LANG = 'pt'
    LANGUAGE = 'português europeu'

    DEFAULT_TIME_ZONE = 'Europe/Lisbon'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
