

__all__ = ('SezimalLocaleEO_CA',)


from .eo import SezimalLocaleEO
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleEO_CA(SezimalLocaleEO):
    SEZIMAL_SEPARATOR = SEPARATOR_DOT
    GROUP_SEPARATOR = SEPARATOR_COMMA

    DEFAULT_TIME_ZONE = 'America/Toronto'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    FIRST_WEEKDAY = 'SUN'

    HOLIDAYS = [
        #
        # Moving Holidays
        #
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Sankta Vendredo #𝑠𝑦𝑚'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Pasko #𝑠𝑦𝑚'),
        ('EASTER+1',   '🐣\ufe0f🌱\ufe0f Paska Lundo #𝑠𝑦𝑚'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Novjaro #𝑠𝑦𝑚'),
        ('13-44', '🇨🇦\ufe0f Tago de Vero kaj Repaciĝo #𝑠𝑦𝑚'),
        ('10-40', '🇫🇮\ufe0f Sankta Johano la Baptisto #𝑠𝑦𝑚'),
        ('15-15', '🪦\ufe0f🪖\ufe0f Tago de Rememorado #𝑠𝑦𝑚'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Kristnasko #𝑠𝑦𝑚'),
        ('20-42', '🎁\ufe0f Skatola Tago #𝑠𝑦𝑚'),

        #
        # Fixed day of the week holidays
        #
        ('13-01', '🐝\ufe0f🐜\ufe0f Labortago #𝑠𝑦𝑚'),
        ('05-34', '👸\ufe0f🏻\ufe0f Tago de la Reĝino #𝑠𝑦𝑚'),
        ('12-01', '🇨🇦\ufe0f Civila Feriotago #𝑠𝑦𝑚'),
        ('14-12', '🙏\ufe0f Dankotago #𝑠𝑦𝑚'),

        #
        # And the one’s that do have a year of reference
        #
        ('212_351-11-01', '🇨🇦\ufe0f Tago de Kanado (#i) #𝑠𝑦𝑚'),
    ] + SezimalLocaleEO.HOLIDAYS

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Sankta Vendredo'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Pasko'),
        ('ISO+EASTER+1',   '🐣\ufe0f🌱\ufe0f Paska Lundo'),

        #
        # Public Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f Novjaro'),
        ('ISO+09-30', '🇨🇦\ufe0f Tago de Vero kaj Repaciĝo'),
        ('ISO+06-24', '🇫🇮\ufe0f Sankta Johano la Baptisto'),
        ('ISO+11-11', '🪦\ufe0f🪖\ufe0f Tago de Rememorado'),
        ('ISO+12-25', '🌟\ufe0f👼🏼\ufe0f Kristnasko'),
        ('ISO+12-26', '🎁\ufe0f Skatola Tago'),

        #
        # Fixed day of the week holidays
        #
        ('ISO+09-01+MON', '🐝\ufe0f🐜\ufe0f Labortago'),
        ('ISO+05-24-MON', '👸\ufe0f🏻\ufe0f Tago de la Reĝino'),
        ('ISO+08-01+MON', '🇨🇦\ufe0f Civila Feriotago'),
        ('ISO+10-01+MON_2', '🙏\ufe0f Dankotago'),

        #
        # And the one’s that do have a year of reference
        #
        ('ISO+1867-07-01', '🇨🇦\ufe0f Tago de Kanado (%i)'),
    ] + SezimalLocaleEO.HOLIDAYS_OTHER_CALENDAR
