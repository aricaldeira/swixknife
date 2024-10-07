

__all__ = ('SezimalLocalePT_CV',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_CV(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português cabo-verdiano'

    DEFAULT_TIME_ZONE = 'Atlantic/Cape_Verde'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'
