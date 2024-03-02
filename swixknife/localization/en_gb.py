

__all__ = ('SezimalLocaleEN_GB',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_GB(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'British English'

    DEFAULT_TIME_ZONE = 'Europe/London'
