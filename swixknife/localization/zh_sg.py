

__all__ = ('SezimalLocaleZH_SG',)


from .zh import SezimalLocaleZH


class SezimalLocaleZH_SG(SezimalLocaleZH):
    DEFAULT_TIME_ZONE = 'Asia/Singapore'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
    CURRENCY_SUBUNIT_SYMBOL_POSITION = 'R'
