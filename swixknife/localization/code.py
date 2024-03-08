

__all__ = ('SezimalLocaleCODE',)


from .lokale import SezimalLocale
from ..base import SEPARATOR_DOT, SEPARATOR_UNDERSCORE


class SezimalLocaleCODE(SezimalLocale):
    LANG = 'en'
    LANGUAGE = 'English'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    SUBGROUP_SEPARATOR = SEPARATOR_UNDERSCORE

    FRACTION_GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_UNDERSCORE

    DATE_FORMAT = '#y-#m-#d'
    DATE_LONG_FORMAT = '#y-W#wY-#w'
    TIME_FORMAT = '#u:#p:#a#:t'
    DATE_TIME_FORMAT = '#y-#m-#d #u:#p:#a#:t'
    DATE_TIME_LONG_FORMAT = '#y-W#wY-#w #u:#p:#a#:t'
