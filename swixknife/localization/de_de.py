

__all__ = ('SezimalLocaleDE_DE',)


from .de import SezimalLocaleDE


class SezimalLocaleDE_DE(SezimalLocaleDE):
    LANG = 'de'
    LANGUAGE = 'Deutsch'

    DEFAULT_TIME_ZONE = 'Europe/Berlin'
