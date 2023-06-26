

__all__ = ('SezimalLocalePT_ST',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_ST(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português são-tomense'

    DEFAULT_TIME_ZONE = 'Africa/Sao_Tome'
