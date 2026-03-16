

__all__ = ('SezimalLocaleEN_SHAW_IN',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_in import SezimalLocaleEN_IN


class SezimalLocaleEN_SHAW_IN(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑦𐑯𐑛𐑾𐑯 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_TIME_ZONE = 'Asia/Kolkata'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '₹'
    CURRENCY_SUBUNIT_SYMBOL = 'प'

    HOLIDAYS = SezimalLocaleEN_IN.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_IN.HOLIDAYS_OTHER_CALENDAR

    format_decimal_number = SezimalLocaleEN_IN.format_decimal_number
