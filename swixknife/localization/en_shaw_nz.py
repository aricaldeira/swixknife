

__all__ = ('SezimalLocaleEN_SHAW_NZ',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_nz import SezimalLocaleEN_NZ


class SezimalLocaleEN_SHAW_NZ(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑯𐑿-𐑟𐑰𐑤𐑩𐑯𐑛 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Pacific/Auckland'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'c'

    HOLIDAYS = SezimalLocaleEN_NZ.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_NZ.HOLIDAYS_OTHER_CALENDAR
