

__all__ = ('SezimalLocaleSV_SE',)


from .sv import SezimalLocaleSV


class SezimalLocaleSV_SE(SezimalLocaleSV):
    LANG = 'sv'
    LANGUAGE = 'svenska'

    DEFAULT_TIME_ZONE = 'Europe/Helsinki'
