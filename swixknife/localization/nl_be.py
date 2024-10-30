

__all__ = ('SezimalLocaleNL_BE',)


from .nl import SezimalLocaleNL


class SezimalLocaleNL_BE(SezimalLocaleNL):
    LANG = 'nl'
    LANGUAGE = 'Belgisch Nederlands'

    DEFAULT_TIME_ZONE = 'Europe/Brussels'
