

__all__ = ('SezimalLocaleES_MX',)


from .es import SezimalLocaleES


class SezimalLocaleES_MX(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Méjico'

    DEFAULT_TIME_ZONE = 'America/Mexico_City'

    FIRST_WEEKDAY = 'SUN'
