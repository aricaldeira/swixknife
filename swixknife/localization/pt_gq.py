

__all__ = ('SezimalLocalePT_GQ',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_GQ(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português guineense'

    DEFAULT_TIME_ZONE = 'Africa/Malabo'
