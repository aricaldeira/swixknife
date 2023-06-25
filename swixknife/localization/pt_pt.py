

__all__ = ('SezimalLocalePT_PT',)


from .pt import SezimalLocalePT


class SezimalLocalePT_PT(SezimalLocalePT):
    LANG = 'pt'
    LANGUAGE = 'português europeu'

    DST_NAME = 'Horário de Inverno'
    DST_SHORT_NAME = 'HI'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
