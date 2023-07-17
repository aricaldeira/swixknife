

__all__ = ('SezimalLocaleZH_MO',)


from .zh_hant import SezimalLocaleZH_HANT


class SezimalLocaleZH_MO(SezimalLocaleZH_HANT):
    DEFAULT_TIME_ZONE = 'Asia/Macau'
