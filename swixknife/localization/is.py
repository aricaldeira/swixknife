

__all__ = ('SezimalLocaleIS',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleIS(SezimalLocale):
    LANG = 'is'
    LANGUAGE = 'íslenska'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'mánudagur',
        'þriðjudagur',
        'miðvikudagur',
        'fimmtudagur',
        'föstudagur',
        'laugardagur',
        'sunnudagur',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'mán.',
        'þri.',
        'mið.',
        'fim.',
        'fös.',
        'lau.',
        'sun.',
    ]

    MONTH_NAME= [
        'janúar',
        'febrúar',
        'mars',
        'apríl',
        'maí',
        'júní',
        'júlí',
        'ágúst',
        'september',
        'október',
        'nóvember',
        'desember',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan.',
        'feb.',
        'mar.',
        'apr.',
        'maí',
        'jún.',
        'júl.',
        'ágú.',
        'sep.',
        'okt.',
        'nóv.',
        'des.',
    ]

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d. #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d. #M #Y, #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    WEEK_NUMBER_SYMBOL = 'vk'
    DAY_NUMBER_SYMBOL = 'dag.'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Atlantic/Reykjavik'
    TEXT_MONTH_DAY_FORMAT = '#-d. #M'
