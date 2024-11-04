

__all__ = ('SezimalLocaleEN',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT


class SezimalLocaleEN(SezimalLocale):
    LANG = 'en'
    LANGUAGE = 'English'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, the #-d#O #M #Y, #u:#p:#a'


    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if str(day).endswith('1'):
            return 'st'
        elif str(day).endswith('2'):
            return 'nd'
        elif str(day).endswith('3'):
            return 'rd'

        return 'th'
