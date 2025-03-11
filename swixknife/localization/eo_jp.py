

__all__ = ('SezimalLocaleEO_JP',)


from .eo import SezimalLocaleEO
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleEO_JP(SezimalLocaleEO):
    SEZIMAL_SEPARATOR = SEPARATOR_DOT
    GROUP_SEPARATOR = SEPARATOR_COMMA

    DEFAULT_TIME_ZONE = 'Asia/Tokyo'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    CURRENCY_UNIT_SYMBOL = '¥'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0
    FIRST_WEEKDAY = 'SUN'

    HOLIDAYS = [
    ] + SezimalLocaleEO.HOLIDAYS

    HOLIDAYS_OTHER_CALENDAR = [
    ] + SezimalLocaleEO.HOLIDAYS_OTHER_CALENDAR
