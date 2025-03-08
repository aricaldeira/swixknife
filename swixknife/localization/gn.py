

__all__ = ('SezimalLocaleGN',)


from .es_py import SezimalLocaleES_PY


class SezimalLocaleGN(SezimalLocaleES_PY):
    LANG = 'gn'
    LANGUAGE = 'avañeꞌẽ'

    FIRST_WEEKDAY = 'SUN'

    WEEKDAY_NAME = [
        'arakõi',
        'araapy',
        'ararundy',
        'arapo',
        'arapoteĩ',
        'arapokõi',
        'arateĩ',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'A2',
        'A3',
        'A4',
        'A5',
        'A6',
        'A7',
        'A1',
    ]

    WEEKDAY_SYMBOL = [
        'A2',
        'A3',
        'A4',
        'A5',
        'A6',
        'A7',
        'A1',
    ]

    MONTH_NAME= [
        'jasyteĩ',
        'jasykõi',
        'jasyapy',
        'jasyrundy',
        'jasypo',
        'jasypoteĩ',
        'jasypokõi',
        'jasypoapy',
        'jasyporundy',
        'jasypa',
        'jasypateĩ',
        'jasypakõi',
    ]

    MONTH_ABBREVIATED_NAME = [
        'J1',
        'J2',
        'J3',
        'J4',
        'J5',
        'J6',
        'J7',
        'J8',
        'J9',
        'J10',
        'J11',
        'J12',
    ]

    MONTH_SYMBOL = [
        'J1',
        'J2',
        'J3',
        'J4',
        'J5',
        'J6',
        'J7',
        'J8',
        'J9',
        'J10',
        'J11',
        'J12',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d #M #Y, #u:#p:#a'

    SEASON_NAME = {
        'spring_cross_quarter': 'Araroꞌy mbyte guive Arapoty peve',
        'spring_equinox': 'Arapoty',
        'summer_cross_quarter': 'Arapoty mbyte guive Arahaku peve',
        'summer_solstice': 'Arahaku',
        'autumn_cross_quarter': 'Arahaku mbyte guive Araroguekúi peve',
        'autumn_equinox': 'Araroguekúi',
        'winter_cross_quarter': 'Araroguekúi mbyte guive Araroꞌy peve',
        'winter_solstice': 'Araroꞌy',
    }

    #
    # https://lenguaguarani.blogspot.com/2016/06/ano-nuevo-guarani-primera-luna-llena-el.html
    #
    MOON_PHASE = {
        'new': 'Pyahu',
        'waxing_crescent': 'Creciente',
        'first_quarter': 'Raꞌy',
        'waxing_gibbous': 'De Cuarto Creciente a Llena',
        'full': 'Guasu',
        'waning_gibbous': 'De Llena a Cuarto Minguante',
        'third_quarter': 'Meg̃ua',
        'waning_crescent': 'Minguante',
    }

    #
    # Error messages
    #
    ERROR = 'Jejavy'
    WEEKDAY_ERROR = 'Arapokõindy ára ndojeporúiva {weekday}'
    MONTH_ERROR = 'Jasy ndojeporúiva {month}'
    WEEK_NUMBER_SYMBOL = 'sem'
    DAY_NUMBER_SYMBOL = 'ara'
