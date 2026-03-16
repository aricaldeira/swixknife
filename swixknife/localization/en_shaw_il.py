

__all__ = ('SezimalLocaleEN_SHAW_IL',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_il import SezimalLocaleEN_IL


class SezimalLocaleEN_SHAW_IL(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑦𐑟𐑮𐑱𐑤𐑦 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Jerusalem'

    CURRENCY_UNIT_SYMBOL = '₪'
    CURRENCY_SUBUNIT_SYMBOL = 'ag'

    FIRST_WEEKDAY = 'SUN'
    DAY_OF_REST = 'SAT'
    OPTIONAL_DAY_OF_REST = 'FRI'

    HOLIDAYS = SezimalLocaleEN_IL.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_IL.HOLIDAYS_OTHER_CALENDAR
