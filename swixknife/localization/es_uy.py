

__all__ = ('SezimalLocaleES_UY',)


from .es import SezimalLocaleES


class SezimalLocaleES_UY(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Uruguai'

    DEFAULT_TIME_ZONE = 'America/Montevideo'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
