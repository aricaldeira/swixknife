

__all__ = ('SezimalLocaleEN_ZA',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_ZA(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'English - South Africa'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Africa/Johannesburg'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'
