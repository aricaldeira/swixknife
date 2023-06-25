

__all__ = ('SezimalLocaleES_UY',)


from .es import SezimalLocaleES


class SezimalLocaleES_UY(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Uruguai'

    DST_NAME = 'Horário de Verano'
    DST_SHORT_NAME = 'HV'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
