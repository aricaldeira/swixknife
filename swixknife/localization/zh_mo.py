

__all__ = ('SezimalLocaleZH_MO',)


from .zh_hant import SezimalLocaleZH_HANT


class SezimalLocaleZH_MO(SezimalLocaleZH_HANT):
    DEFAULT_TIME_ZONE = 'Asia/Macau'

    CURRENCY_UNIT_SYMBOL = '元'
    CURRENCY_SUBUNIT_SYMBOL = '毫'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 1
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'
