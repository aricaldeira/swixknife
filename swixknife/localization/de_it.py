

__all__ = ('SezimalLocaleDE_IT',)


from .de_at import SezimalLocaleDE_AT


class SezimalLocaleDE_IT(SezimalLocaleDE_AT):
    LANG = 'de'
    LANGUAGE = 'Südtirolerisches Deutsch'

    DEFAULT_TIME_ZONE = 'Europe/Rome'
