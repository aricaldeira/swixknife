

__all__ = ('SezimalLocaleES_ES',)


from .es import SezimalLocaleES


class SezimalLocaleES_ES(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de España'

    DATE_LONG_FORMAT = '#-d de #M de #Y'
    DATE_TIME_LONG_FORMAT = '#W, #-d de #M de #Y, #u:#p:#a'
