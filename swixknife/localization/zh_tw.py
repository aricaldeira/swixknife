

__all__ = ('SezimalLocaleZH_TW',)


from .zh_hant import SezimalLocaleZH_HANT


class SezimalLocaleZH_TW(SezimalLocaleZH_HANT):
    DEFAULT_TIME_ZONE = 'Asia/Taipei'

    CURRENCY_UNIT_SYMBOL = '圓'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'
