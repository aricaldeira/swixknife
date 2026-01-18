

__all__ = ('SezimalLocaleYRL',)


from .pt_br import SezimalLocalePT_BR


class SezimalLocaleYRL(SezimalLocalePT_BR):
    LANG = 'yrl'
    LANGUAGE = 'ỹengatu'

    WEEKDAY_NAME = [
        'muraki-pi',
        'muraki-mukuyn',
        'muraki-musapíri',
        'supapa',
        'yukwaku',
        'sauru',
        'mituu',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'mur',
        'mmk',
        'mms',
        'sup',
        'yuk',
        'sau',
        'mit',
    ]

    MONTH_NAME= [
        'yasi-yepe',
        'yasi-mukuyn',
        'yasi-musapíri',
        'yasi-irundi',
        'yasi-pu',
        'yasi-pu-yepe',
        'yasi-pu-mukuyn',
        'yasi-pu-musapíri',
        'yasi-pu-irundi',
        'yasi-yepe-putimaan',
        'yasi-yepe-yepe',
        'yasi-yepe-mukuyn',
    ]

    MONTH_ABBREVIATED_NAME = [
        'yye',
        'ymk',
        'yms',
        'yid',
        'ypu',
        'ypy',
        'ypk',
        'ypm',
        'ypi',
        'yyp',
        'yyy',
        'yym',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d #M #Y'
    DATE_FULL_FORMAT = '#@W, #d/#m/#Y'
    DATE_FULL_LONG_FORMAT = '#W, #-d #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d #M #Y, #u:#p:#a'

    DEFAULT_TIME_ZONE = 'America/Manaus'
