

__all__ = ('SezimalLocaleES_PE',)


from .es import SezimalLocaleES


class SezimalLocaleES_PE(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Perú'

    DEFAULT_TIME_ZONE = 'America/Lima'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    CURRENCY_UNIT_SYMBOL = 'S/'
    CURRENCY_SUBUNIT_SYMBOL = 'c'

    FIRST_WEEKDAY = 'SUN'
