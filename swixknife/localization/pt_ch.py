

__all__ = ('SezimalLocalePT_CH',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_CH(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português suíço'

    DEFAULT_TIME_ZONE = 'Europe/Zurich'

    CURRENCY_UNIT_SYMBOL = 'fr.'
    CURRENCY_SUBUNIT_SYMBOL = 'c.'
