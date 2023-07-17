

__all__ = ('SezimalLocaleZH_HK',)


from .zh_hant import SezimalLocaleZH_HANT


class SezimalLocaleZH_HK(SezimalLocaleZH_HANT):
    DEFAULT_TIME_ZONE = 'Asia/Hong_Kong'
