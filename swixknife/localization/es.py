

__all__ = ('SezimalLocaleES',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleES(SezimalLocale):
    LANG = 'es'
    LANGUAGE = 'español'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    WEEKDAY_NAME = [
        'lunes',
        'martes',
        'miércoles',
        'jueves',
        'viernes',
        'sábado',
        'domingo',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lun',
        'mar',
        'mié',
        'jue',
        'vie',
        'sáb',
        'dom',
    ]

    MONTH_NAME= [
        'enero',
        'febrero',
        'marzo',
        'abril',
        'mayo',
        'junio',
        'julio',
        'agosto',
        'septiembre',
        'octubre',
        'noviembre',
        'diciembre',
    ]

    MONTH_ABBREVIATED_NAME = [
        'ene',
        'feb',
        'mar',
        'abr',
        'may',
        'jun',
        'jul',
        'ago',
        'sep',
        'oct',
        'nov',
        'dic',
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

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O de #M de #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O de #M de #Y, #u:#p:#a'
    DST_NAME = 'Horario de Verano'
    DST_SHORT_NAME = 'HV'
    DEFAULT_TIME_ZONE = 'Europe/Madrid'
    WEEK_NUMBER_SYMBOL = 'sem'
    DAY_NUMBER_SYMBOL = 'día'

    SEASON_NAME = {
        'spring_cross_quarter': 'Transición Invierno – Primavera',
        'spring_equinox': 'Primavera',
        'summer_cross_quarter': 'Transición Primavera – Verano',
        'summer_solstice': 'Verano',
        'autumn_cross_quarter': 'Transición Verano – Otoño',
        'autumn_equinox': 'Otoño',
        'winter_cross_quarter': 'Transición Otoño – Invierno',
        'winter_solstice': 'Invierno',
    }

    MOON_PHASE = {
        'new': 'Nueva',
        'waxing_crescent': 'Creciente',
        'first_quarter': 'Cuarto Creciente',
        'waxing_gibbous': 'De Cuarto Creciente a Llena',
        'full': 'Llena',
        'waning_gibbous': 'De Llena a Cuarto Minguante',
        'third_quarter': 'Cuarto Minguante',
        'waning_crescent': 'Minguante',
    }

    #
    # Error messages
    #
    ERROR = 'Error'
    WEEKDAY_ERROR = 'Dia de la semana no válido {weekday}'
    MONTH_ERROR = 'Mes no válido {month}'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return '.º'

        return ''

    DCC_TERM_NAME = [
        'Bimestre‐Cero',
        'Bimestre‐Uno',
        'Bimestre‐Dos',
        'Bimestre‐Tres',
        'Bimestre‐Cuatro',
    ]

    DCC_TERM_ABBREVIATED_NAME = [
        'B0',
        'B1',
        'B2',
        'B3',
        'B4',
    ]

    DCC_MONTH_NAME = [
        'Mes‐Cero',
        'Mes‐Uno',
        'Mes‐Dos',
        'Mes‐Tres',
        'Mes‐Cuatro',
        'Mes‐Cinco',
        'Mes‐Seis',
        'Mes‐Seisiuno',
        'Mes‐Seisidós',
        'Mes‐Seisitrés',
        'Mes‐Seisicuatro',
    ]

    DCC_WEEKDAY_NAME = [
        'Día‐de‐la‐Semana‐Cero',
        'Día‐de‐la‐Semana‐Uno',
        'Día‐de‐la‐Semana‐Dos',
        'Día‐de‐la‐Semana‐Tres',
        'Día‐de‐la‐Semana‐Cuatro',
        'Día‐de‐la‐Semana‐Cinco',
    ]

    DCC_WEEKDAY_ABBREVIATED_NAME = [
        'DS0',
        'DS1',
        'DS2',
        'DS3',
        'DS4',
        'DS5',
    ]

    DCC_NUMBER = [
        'cero',
        'uno',
        'dos',
        'tres',
        'cuatro',
        'cinco',
        'seis',
        'seisiuno',
        'seisidós',
        'seisitrés',
        'seisicuatro',
    ]

    DCC_YEAR_COUNT = {
        None: '&>Y años',
        SezimalInteger('1'): '&>Y año',
    }

    DCC_TERM_COUNT = {
        None: '&-t bimestres',
        SezimalInteger('1'): '&-t bimestre',
    }

    DCC_MONTH_COUNT = {
        None: '&-m meses',
        SezimalInteger('1'): '&-m mes',
    }

    DCC_WEEK_COUNT = {
        None: '&-wM semanas',
        SezimalInteger('1'): '&-wM semana',
    }

    DCC_WEEK_IN_YEAR_COUNT = {
        None: '&-wY semanas',
        SezimalInteger('1'): '&-wY semana',
    }

    DCC_DAY_COUNT = {
        None: '&-d días',
        SezimalInteger('1'): '&-d día',
    }

    DCC_DAY_IN_YEAR_COUNT = {
        None: '&-dY días',
        SezimalInteger('1'): '&-dY día',
    }

    DCC_DAY_IN_WEEK_COUNT = {
        None: '&-dW días',
        SezimalInteger('1'): '&-dW día',
    }

    DCC_DATE_MONTH_DAY_SEPARATOR = ' y '

    ADC_MONTH_NAME = [
        'pez',
        'ballena',
        'eridano',
        'unicornio',
        'hidra',
        'león',
        'virgo',
        'serpiente',
        'águila',
        'acuario',
        'sextante',
    ]

    ADC_MONTH_ABBREVIATED_NAME = [
        'pez',
        'ball',
        'eri',
        'uni',
        'hid',
        'leó',
        'vir',
        'ser',
        'águ',
        'acu',
        'sex',
    ]

    ADC_MONTH_SYMBOL = [
        'p',
        'b',
        'e',
        'u',
        'h',
        'l',
        'v',
        'sr',
        'ág',
        'aq',
        'sx',
    ]

    ADC_WEEK_NAME = [
        'espíritu',
        'fuego',
        'aire',
        'agua',
        'tierra',
        'cuorpo',
    ]

    ADC_WEEK_ABBREVIATED_NAME = [
        'esp',
        'fue',
        'air',
        'agu',
        'tie',
        'cuo',
    ]

    ADC_WEEK_SYMBOL = [
        'E',
        'F',
        'Ai',
        'Ag',
        'T',
        'C',
    ]

    ADC_WEEKDAY_NAME = [
        'sol',
        'venus',
        'marte',
        'júpiter',
        'saturno',
        'luna',
    ]

    ADC_WEEKDAY_ABBREVIATED_NAME = [
        'sol',
        'ven',
        'mar',
        'júp',
        'sat',
        'lun',
    ]

    DCC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, mes &-m, día &-d'
    DCC_DATE_LONG_FORMAT_ON_DATE_DAYS = '&󱹭>Y, día &-dY'
    DCC_DATE_LONG_FORMAT_ON_DATE_WEEKS = '&󱹭>Y, semana &-wY, día &-dW'
    DCC_DATE_LONG_FORMAT_ON_DATE_MONTHS_WEEKS = '&󱹭>Y, mes &-m, semana &-wM, día &-dW'

    ADC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, mes &$DEM &cM, día &-d'
    ADC_DATE_LONG_FORMAT_ON_DATE_WEEKDAY = '&󱹭>Y, mes &$DEM &cM, semana &$DEW &cW, día &$DED &cD'

    _DE_DEL_DE_LA_MES = [
        'de',     # pez
        'de la',  # ballena
        'del',    # eridano
        'del',    # unicornio
        'de la',  # hidra
        'del',    # león
        'de',     # virgo
        'de la',  # serpiente
        'del',    # águila
        'de',     # acuario
        'del',    # sextante
    ]

    _DE_DEL_DE_LA_SEMANA = [
         'del',    # espíritu
         'del',    # fuego
         'del',    # aire
         'del',    # agua
         'de la',  # tierra
         'del',    # cuorpo
    ]

    _DE_DEL_DE_LA_DIA_SEMANA = [
         'del',    # sol
         'de',     # vênus
         'de',     # marte
         'de',     # júpiter
         'de',     # saturno
         'de la',  # luna
    ]

    def apply_dcc_date_format(self, date: SezimalDate, fmt: str) -> str:
        if f'&$DED' in fmt:
            fmt = fmt.replace(f'&$DED', self._DE_DEL_DE_LA_DIA_SEMANA[int(date.dcc_weekday)])

        if f'&$DEW' in fmt:
            fmt = fmt.replace(f'&$DEW', self._DE_DEL_DE_LA_SEMANA[int(date.dcc_week)])

        if f'&$DEM' in fmt:
            fmt = fmt.replace(f'&$DEM', self._DE_DEL_DE_LA_MES[int(date.dcc_month)])

        return fmt
