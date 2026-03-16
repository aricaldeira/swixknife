

__all__ = ('SezimalLocaleEN_SHAW_MY',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_my import SezimalLocaleEN_MY


class SezimalLocaleEN_SHAW_MY(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑥𐑩𐑤𐑱𐑠𐑩𐑯 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Kuala_Lumpur'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = 'RM'  # Malaysian Ringgit
    CURRENCY_SUBUNIT_SYMBOL = 's'  # sen

    HOLIDAYS = SezimalLocaleEN_MY.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_MY.HOLIDAYS_OTHER_CALENDAR
