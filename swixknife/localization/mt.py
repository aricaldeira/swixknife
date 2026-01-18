

__all__ = ('SezimalLocaleMT',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleMT(SezimalLocale):
    LANG = 'mt'
    LANGUAGE = 'malti'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNMT_SYMBOL = '€'
    CURRENCY_SUBUNMT_SYMBOL = 'c'
    CURRENCY_UNMT_SYMBOL_POSMTION = 'R'

    WEEKDAY_NAME = [
        'it-tnejn',
        'it-tlieta',
        'i-erbgħa',
        'il-ħamis',
        'il-ġimgħa',
        'is-sibt',
        'il-ħadd',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'tne',
        'tli',
        'erb',
        'ħam',
        'ġim',
        'sib',
        'ħad',
    ]

    MONTH_NAME= [
        'jannar',
        'frar',
        'marzu',
        'april',
        'mejju',
        'ġunju',
        'lulju',
        'awissu',
        'settembru',
        'ottubru',
        'novembru',
        'diċembru',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'fra',
        'mar',
        'apr',
        'mej',
        'ġun',
        'lul',
        'awi',
        'set',
        'ott',
        'nov',
        'diċ',
    ]

    ERA_NAME = [
        #
        # Era Umana Sesimale
        #
        'EUS',
        #
        # Avanti l’Era Umana Sesimale
        #
        'aEUS',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    DATE_FULL_FORMAT = '#@W, #d/#m/#Y'
    DATE_FULL_LONG_FORMAT = '#W, #-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'
    DST_NAME = 'Ora Legale'
    DST_SHORT_NAME = 'OL'
    DEFAULT_TIME_ZONE = 'Europe/Malta'
    WEEK_NUMBER_SYMBOL = 'ġim'
    DAY_NUMBER_SYMBOL = 'jum'

    SEASON_NAME = {
        'spring_cross_quarter': 'Transizione Inverno – Primavera',
        'spring_equinox': 'Ir-rebbiegħa',
        'summer_cross_quarter': 'Transizione Primavera – Estate',
        'summer_solstice': 'Is-sajfs',
        'autumn_cross_quarter': 'Transizione Estate – Autunno',
        'autumn_equinox': 'Il-ħarifa',
        'winter_cross_quarter': 'Transizione Autunno – Inverno',
        'winter_solstice': 'Ix-xitwa',
    }

    MOON_PHASE = {
        'new': 'Nuova',
        'waxing_crescent': 'Crescente',
        'first_quarter': 'Primo Quarto',
        'waxing_gibbous': 'Dal Primo Quarto alla Piena',
        'full': 'Piena',
        'waning_gibbous': 'Dalla Piena all’Ultimo Quarto',
        'third_quarter': 'Ultimo Quarto',
        'waning_crescent': 'Calante',
    }

    #
    # Error messages
    #
    ERROR = 'Errore'
    WEEKDAY_ERROR = 'Giorno della settimana non valido {weekday}'
    MONTH_ERROR = 'Mese non valido {month}'
