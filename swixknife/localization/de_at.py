

__all__ = ('SezimalLocaleDE_AT',)


from .de import SezimalLocaleDE


class SezimalLocaleDE_AT(SezimalLocaleDE):
    LANG = 'de'
    LANGUAGE = 'Österreiches Deutsch'

    DEFAULT_TIME_ZONE = 'Europe/Vienna'

    UPPERCASE_MAPPING = {
        ord('ß'): 'SS',
    }
    LOWERCASE_MAPPING = {
        ord('ẞ'): 'ss',
    }
