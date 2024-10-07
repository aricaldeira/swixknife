

__all__ = ('SezimalLocalePT_GW',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_GW(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português guineense'

    DEFAULT_TIME_ZONE = 'Africa/Bissau'

    CURRENCY_UNIT_SYMBOL = 'F.CFA'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
    CURRENCY_UNIT_SYMBOL_POSITION = 'L'
