

__all__ = ('SezimalLocaleEN_BR',)


from .en import SezimalLocaleEN
from .pt_br import SezimalLocalePT_BR


class SezimalLocaleEN_BR(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'English - Brazil'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'America/Sao_Paulo'

    CURRENCY_UNIT_SYMBOL = 'R$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    HOLIDAYS = SezimalLocalePT_BR.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocalePT_BR.HOLIDAYS_OTHER_CALENDAR
