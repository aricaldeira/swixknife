

__all__ = ('SezimalLocalePT_MZ',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_MZ(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português moçambicano'

    DEFAULT_TIME_ZONE = 'Africa/Maputo'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
