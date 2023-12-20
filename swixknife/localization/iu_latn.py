

__all__ = ('SezimalLocaleIU_LATN',)


from .en_ca import SezimalLocaleEN_CA


class SezimalLocaleIU_LATN(SezimalLocaleEN_CA):
    LANG = 'iu'
    LANGUAGE = 'inuktitut'

    WEEKDAY_NAME: list[str] = [
        'naggajjau',
        'aippiq',
        'pingatsiq',
        'sitammiq',
        'tallirmiq',
        'sivataarvik',
        'naattiinguja',
    ]

    WEEKDAY_ABBREVIATED_NAME: list[str] = [
        'nag',
        'aip',
        'pin',
        'sit',
        'tal',
        'siv',
        'naa',
    ]

    MONTH_NAME: list[str] = [
        'jaannuari',
        'viivvuari',
        'maatsi',
        'iipuri',
        'mai',
        'juuni',
        'julai',
        'aaggiisi',
        'sitipiri',
        'utupiri',
        'nuvipiri',
        'tisipiri',
    ]

    MONTH_ABBREVIATED_NAME: list[str] = [
        'jaa',
        'vii',
        'maa',
        'iip',
        'mai',
        'juu',
        'jul',
        'aag',
        'sit',
        'utu',
        'nuv',
        'tis',
    ]

