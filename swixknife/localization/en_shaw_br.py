

__all__ = ('SezimalLocaleEN_SHAW_BR',)


from .en_shaw import SezimalLocaleEN_SHAW
from .pt_br import SezimalLocalePT_BR


class SezimalLocaleEN_SHAW_BR(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑦𐑙𐑜𐑤𐑦𐑖 - 𐑚𐑮𐑩𐑟𐑦𐑤'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'America/Sao_Paulo'
    FIRST_WEEKDAY = 'SUN'

    CURRENCY_UNIT_SYMBOL = 'R$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    HOLIDAYS = SezimalLocalePT_BR.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocalePT_BR.HOLIDAYS_OTHER_CALENDAR
