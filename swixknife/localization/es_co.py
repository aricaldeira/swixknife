

__all__ = ('SezimalLocaleES_CO',)


from .es import SezimalLocaleES


class SezimalLocaleES_CO(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Colombia'

    DEFAULT_TIME_ZONE = 'America/Bogota'

    FIRST_WEEKDAY = 'SUN'
