

__all__ = ('SezimalLocalePT_AO',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_AO(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português angolano'

    DEFAULT_TIME_ZONE = 'Africa/Luanda'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
