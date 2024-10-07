

__all__ = ('SezimalLocaleZH_CN',)


from .zh import SezimalLocaleZH


class SezimalLocaleZH_CN(SezimalLocaleZH):
    DEFAULT_TIME_ZONE = 'Asia/Shanghai'

    CURRENCY_UNIT_SYMBOL = '元'
    CURRENCY_SUBUNIT_SYMBOL = '角'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 1
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'
