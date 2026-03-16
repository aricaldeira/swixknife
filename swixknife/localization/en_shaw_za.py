

__all__ = ('SezimalLocaleEN_SHAW_ZA',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_za import SezimalLocaleEN_ZA


class SezimalLocaleEN_SHAW_ZA(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑦𐑙𐑜𐑤𐑦𐑖 - ·𐑕𐑬𐑔 ·𐑨𐑓𐑮𐑦𐑒𐑩'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Africa/Johannesburg'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    HOLIDAYS = SezimalLocaleEN_ZA.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_ZA.HOLIDAYS_OTHER_CALENDAR
