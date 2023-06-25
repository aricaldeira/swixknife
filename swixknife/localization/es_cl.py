

__all__ = ('SezimalLocaleES_CL',)


from .es import SezimalLocaleES


class SezimalLocaleES_CL(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Chile'

    DST_NAME = 'Horário de Verano'
    DST_SHORT_NAME = 'HV'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
