

__all__ = ('SezimalLocaleEN_IL',)


from .lokale import SezimalLocale
from .he_latn import SezimalLocaleHE_LATN


class SezimalLocaleEN_IL(SezimalLocaleHE_LATN):
    LANG = 'en'
    LANGUAGE = 'Israeli English'

    WEEKDAY_NAME = SezimalLocale.WEEKDAY_NAME
    WEEKDAY_ABBREVIATED_NAME = SezimalLocale.WEEKDAY_ABBREVIATED_NAME
    WEEKDAY_SYMBOL = SezimalLocale.WEEKDAY_SYMBOL

    MONTH_NAME = SezimalLocale.MONTH_NAME
    MONTH_ABBREVIATED_NAME = SezimalLocale.MONTH_ABBREVIATED_NAME
    MONTH_SYMBOL = SezimalLocale.MONTH_SYMBOL
