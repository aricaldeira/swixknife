

__all__ = ('SezimalLocaleES_CL',)


from .es import SezimalLocaleES


class SezimalLocaleES_CL(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Chile'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'America/Santiago'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0
