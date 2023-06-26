

__all__ = ('SezimalLocaleES_EC',)


from .es import SezimalLocaleES


class SezimalLocaleES_EC(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Ecuador'

    DEFAULT_TIME_ZONE = 'America/Guayaquil'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
