

__all__ = ('SezimalLocaleYRL',)


from .pt import SezimalLocalePT


class SezimalLocaleYRL(SezimalLocalePT):
    LANG = 'yrl'
    LANGUAGE = 'yẽgatu'

    WEEKDAY_NAME = [
        'murakipi',
        'muraki-mukũi',
        'muraki-musapíri',
        'supapa',
        'yukuaku',
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
        'yasi-mukũi',
        'yasi-musapíri',
        'yasi-irũdi',
        'yasi-pu',
        'yasi-pu-yepe',
        'yasi-pu-mukũi',
        'yasi-pu-musapíri',
        'yasi-pu-irũdi',
        'yasi-yepe-putimaã',
        'yasi-yepe-yepe',
        'yasi-yepe-mukũi',
    ]

    MONTH_ABBREVIATED_NAME = [
        'yye',
        'ymk',
        'ymu',
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

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d #M #Y, #u:#p:#a'

    DEFAULT_TIME_ZONE = 'America/Manaus'
