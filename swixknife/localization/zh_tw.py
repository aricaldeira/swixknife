

__all__ = ('SezimalLocaleZH_TW',)


from .zh_hant import SezimalLocaleZH_HANT


class SezimalLocaleZH_TW(SezimalLocaleZH_HANT):
    DEFAULT_TIME_ZONE = 'Asia/Taipei'
