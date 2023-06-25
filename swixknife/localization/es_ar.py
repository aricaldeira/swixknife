

__all__ = ('SezimalLocaleES_AR',)


from .es import SezimalLocaleES


class SezimalLocaleES_AR(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Argentina'

    DST_NAME = 'Horário de Verano'
    DST_SHORT_NAME = 'HV'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
