

__all__ = ('SezimalLocaleES_PY',)


from .es import SezimalLocaleES


class SezimalLocaleES_PY(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Paraguai'

    DEFAULT_TIME_ZONE = 'America/Asuncion'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    CURRENCY_UNIT_SYMBOL = '₲'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0

    FIRST_WEEKDAY = 'SUN'
