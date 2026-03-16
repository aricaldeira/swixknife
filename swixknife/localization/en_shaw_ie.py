

__all__ = ('SezimalLocaleEN_SHAW_IE',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_ie import SezimalLocaleEN_IE


class SezimalLocaleEN_SHAW_IE(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑲𐑮𐑦𐑖 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_TIME_ZONE = 'Europe/Dublin'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'

    HOLIDAYS = SezimalLocaleEN_IE.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_IE.HOLIDAYS_OTHER_CALENDAR
