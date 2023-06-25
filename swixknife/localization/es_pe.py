

__all__ = ('SezimalLocaleES_PE',)


from .es import SezimalLocaleES


class SezimalLocaleES_PE(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Perú'

    DST_NAME = 'Horário de Verano'
    DST_SHORT_NAME = 'HV'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
