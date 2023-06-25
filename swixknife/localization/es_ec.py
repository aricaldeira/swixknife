

__all__ = ('SezimalLocaleES_EC',)


from .es import SezimalLocaleES


class SezimalLocaleES_EC(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Ecuador'

    DST_NAME = 'Horário de Verano'
    DST_SHORT_NAME = 'HV'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
