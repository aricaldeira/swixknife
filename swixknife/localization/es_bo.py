

__all__ = ('SezimalLocaleES_BO',)


from .es import SezimalLocaleES


class SezimalLocaleES_BO(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Bolivia'

    DST_NAME = 'Horário de Verano'
    DST_SHORT_NAME = 'HV'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
