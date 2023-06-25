

__all__ = ('SezimalLocaleEN_AU',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_AU(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Autralian English'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
