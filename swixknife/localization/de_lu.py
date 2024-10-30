

__all__ = ('SezimalLocaleDE_LU',)


from .de import SezimalLocaleDE


class SezimalLocaleDE_LU(SezimalLocaleDE):
    LANG = 'de'
    LANGUAGE = 'Luxembourgisches Deutsch'

    DEFAULT_TIME_ZONE = 'Europe/Luxembourg'
