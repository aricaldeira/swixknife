

__all__ = ('SezimalLocaleES_AR',)


from .es import SezimalLocaleES


class SezimalLocaleES_AR(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Argentina'

    DEFAULT_TIME_ZONE = 'America/Buenos_Aires'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
