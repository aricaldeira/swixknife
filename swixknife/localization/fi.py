

__all__ = ('SezimalLocaleFI',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleFI(SezimalLocale):
    LANG = 'fi'
    LANGUAGE = 'suomi'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'maanantai',
        'tiistai',
        'keskiviikko',
        'torstai',
        'perjantai',
        'lauantai',
        'sunnuntai',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'ma',
        'ti',
        'ke',
        'to',
        'pe',
        'la',
        'su',
    ]

    MONTH_NAME= [
        'tammikuu',
        'helmikuu',
        'maaliskuu',
        'huhtikuu',
        'toukokuu',
        'kesäkuu',
        'heinäkuu',
        'elokuu ',
        'syyskuu',
        'lokakuu',
        'marraskuu',
        'joulukuu',
    ]

    MONTH_ABBREVIATED_NAME = [
        'tammik.',
        'helmik.',
        'maalisk.',
        'huhtik.',
        'toukok.',
        'kesäk.',
        'heinäk.',
        'elok.',
        'syysk.',
        'lokak.',
        'marrask.',
        'jouluk.',
    ]

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#y'
    DATE_LONG_FORMAT = '#-d #Mta #y'
    TIME_SEPARATOR = '.'
    TIME_FORMAT = '#u.#p.#a'
    DATE_TIME_FORMAT = '#d.#m.#y #u.#p.#a'
    DATE_TIME_LONG_FORMAT = '#Wna #-d #Mta #y, #u.#p.#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    WEEK_NUMBER_SYMBOL = 'vk'
    DAY_NUMBER_SYMBOL = 'päivä'
    ISO_DATE_LONG_FORMAT = '%-d %b %Y'
    TEXT_MONTH_DAY_FORMAT = '#-d #Mta'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Helsinki'

    SEASON_NAME = {
        'spring_cross_quarter': 'talvi – kevät',
        'spring_equinox': 'kevät',
        'summer_cross_quarter': 'kevät – kesä',
        'summer_solstice': 'kesä',
        'autumn_cross_quarter': 'kesä – syksy',
        'autumn_equinox': 'syksy',
        'winter_cross_quarter': 'syksy – talvi',
        'winter_solstice': 'talvi',
    }
