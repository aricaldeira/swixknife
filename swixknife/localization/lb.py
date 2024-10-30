

__all__ = ('SezimalLocaleLB',)


from .fr_lu import SezimalLocaleFR_LU


class SezimalLocaleFR_LU(SezimalLocaleFR_LU):
    LANG = 'lb'
    LANGUAGE = 'Lëtzebuergesch'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'Méindeg',
        'Dënschdeg',
        'Mëttwoch',
        'Donneschdeg',
        'Freideg',
        'Samschdeg',
        'Sonndeg',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Méi.',
        'Dën.',
        'Mët.',
        'Don.',
        'Fre.',
        'Sam.',
        'Son.',
    ]

    MONTH_NAME= [
        'Januar',
        'Februar',
        'Mäerz',
        'Abrëll',
        'Mee',
        'Juni',
        'Juli',
        'August',
        'September',
        'Oktober',
        'November',
        'Dezember',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Jan.',
        'Feb.',
        'Mäe.',
        'Abr.',
        'Mee',
        'Juni',
        'Juli',
        'Aug.',
        'Sep.',
        'Okt.',
        'Nov.',
        'Dez.',
    ]

    DATE_FORMAT = '#d.#m.#y'
    DATE_LONG_FORMAT = '#-d #M #y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d #M #y, #u:#p:#a'
