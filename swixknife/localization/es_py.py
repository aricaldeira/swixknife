

__all__ = ('SezimalLocaleES_PY',)


from .es import SezimalLocaleES


class SezimalLocaleES_PY(SezimalLocaleES):
    LANG = 'es'
    LANGUAGE = 'español de Paraguai'

    DST_NAME = 'Horário de Verano'
    DST_SHORT_NAME = 'HV'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
