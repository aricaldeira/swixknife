

__all__ = ('SezimalLocalePT_LU',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_LU(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português luxemburguês'

    DEFAULT_TIME_ZONE = 'Europe/Luxembourg'
