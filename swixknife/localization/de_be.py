

__all__ = ('SezimalLocaleDE_BE',)


from .de import SezimalLocaleDE


class SezimalLocaleDE_BE(SezimalLocaleDE):
    LANG = 'de'
    LANGUAGE = 'Belgisches Deutsch'

    DEFAULT_TIME_ZONE = 'Europe/Brussels'
