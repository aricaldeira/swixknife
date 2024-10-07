

__all__ = ('SezimalLocalePT_MO',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_MO(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português macaense'

    DEFAULT_TIME_ZONE = 'Europe/Macau'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'a'
