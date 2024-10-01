

__all__ = ('SezimalLocaleEN_ZA',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_ZA(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'English - South Africa'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Africa/Johannesburg'
