

__all__ = ('SezimalLocaleEN_SHAW_GB',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_gb import SezimalLocaleEN_GB


class SezimalLocaleEN_SHAW_GB(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑚𐑮𐑦𐑑𐑦𐑖 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_TIME_ZONE = 'Europe/London'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '£'
    CURRENCY_SUBUNIT_SYMBOL = 'p'

    DECIMAL_SPEED = 'mph'

    HOLIDAYS = SezimalLocaleEN_GB.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_GB.HOLIDAYS_OTHER_CALENDAR
