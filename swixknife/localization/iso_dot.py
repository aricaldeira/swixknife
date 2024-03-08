

__all__ = ('SezimalLocaleISO_DOT',)


from .iso import SezimalLocaleISO
from ..base import SEPARATOR_DOT


class SezimalLocaleISO_DOT(SezimalLocaleISO):
    SEZIMAL_SEPARATOR = SEPARATOR_DOT
