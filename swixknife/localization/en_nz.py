

__all__ = ('SezimalLocaleEN_NZ',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_NZ(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'New Zealand English'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
