

__all__ = ('SezimalLocaleES_ES',)


from .es import SezimalLocaleES


class SezimalLocaleES_ES(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de España'

    DATE_LONG_FORMAT = '#-d de #M de #Y'
    DATE_TIME_LONG_FORMAT = '#W, #-d de #M de #Y, #u:#p:#a'

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'
