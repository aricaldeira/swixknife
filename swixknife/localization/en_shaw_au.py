

__all__ = ('SezimalLocaleEN_SHAW_AU',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_au import SezimalLocaleEN_AU


class SezimalLocaleEN_SHAW_AU(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑪𐑕𐑑𐑮𐑱𐑤𐑾𐑯 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Australia/Sydney'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'c'

    HOLIDAYS = SezimalLocaleEN_AU.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_AU.HOLIDAYS_OTHER_CALENDAR
