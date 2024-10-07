

__all__ = ('SezimalLocaleGL',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleGL(SezimalLocale):
    LANG = 'gl'
    LANGUAGE = 'galego'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    WEEKDAY_NAME = [
        'luns',
        'martes',
        'mércores',
        'xoves',
        'venres',
        'sábado',
        'domingo',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lun',
        'mar',
        'mér',
        'xov',
        'ven',
        'sáb',
        'dom',
    ]

    MONTH_NAME= [
        'xaneiro',
        'febreiro',
        'marzo',
        'abril',
        'maio',
        'xuño',
        'xullo',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'decembro',
    ]

    MONTH_ABBREVIATED_NAME = [
        'xan',
        'feb',
        'mar',
        'abr',
        'mai',
        'xuñ',
        'xul',
        'ago',
        'set',
        'out',
        'nov',
        'dec',
    ]

    ERA_NAME = [
        #
        # Era Humana Sezimal
        #
        'EHS',
        #
        # Antes de la Era Humana Sezimal
        #
        'aEHS',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O de #M de #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O de #M de #Y, #u:#p:#a'
    DST_NAME = 'Horario de Verán'
    DST_SHORT_NAME = 'HV'
    DEFAULT_TIME_ZONE = 'Europe/Madrid'

    SEASON_NAME = {
        'spring_cross_quarter': 'Transición Inverno – Primavera',
        'spring_equinox': 'Primavera',
        'summer_cross_quarter': 'Transición Primavera – Verán',
        'summer_solstice': 'Verán',
        'autumn_cross_quarter': 'Transición Verán – Outono',
        'autumn_equinox': 'Outono',
        'winter_cross_quarter': 'Transición Outono – Inverno',
        'winter_solstice': 'Inverno',
    }

    MOON_PHASE = {
        'new': 'Nova',
        'waxing_crescent': 'Crecente',
        'first_quarter': 'Cuarto Crecente',
        'waxing_gibbous': 'De Cuarto Crecente a Chea',
        'full': 'Chea',
        'waning_gibbous': 'De Chea a Cuarto Minguante',
        'third_quarter': 'Cuarto Minguante',
        'waning_crescent': 'Minguante',
    }

    #
    # Error messages
    #
    ERROR = 'Erro'
    WEEKDAY_ERROR = 'Día da semana non válido {weekday}'
    MONTH_ERROR = 'Mes non válido {month}'
    WEEK_NUMBER_SYMBOL = 'sem'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'º'

        return ''
