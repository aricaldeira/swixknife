

__all__ = ('SezimalLocaleES_BO',)


from .es import SezimalLocaleES


class SezimalLocaleES_BO(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Bolivia'

    DEFAULT_TIME_ZONE = 'America/La_Paz'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    CURRENCY_UNIT_SYMBOL = 'Bs'
    CURRENCY_SUBUNIT_SYMBOL = 'c.'
