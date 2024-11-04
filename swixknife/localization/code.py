

__all__ = ('SezimalLocaleCODE',)


from .iso_dot import SezimalLocaleISO_DOT
from ..base import SEPARATOR_UNDERSCORE


class SezimalLocaleCODE(SezimalLocaleISO_DOT):
    GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    FRACTION_GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
