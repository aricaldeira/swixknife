

__all__ = ('SezimalLocaleEO_AU',)


from .eo import SezimalLocaleEO
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleEO_AU(SezimalLocaleEO):
    SEZIMAL_SEPARATOR = SEPARATOR_DOT
    GROUP_SEPARATOR = SEPARATOR_COMMA

    DEFAULT_TIME_ZONE = 'Australia/Sydney'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'c'

    HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Paska day according to Symmetry454 original proposal
        #
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Sankta Vendredo #𝑠𝑦𝑚'),
        ('EASTER-1',   '🐣\ufe0f🌱\ufe0f Sankta Sabato #𝑠𝑦𝑚'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Pasko #𝑠𝑦𝑚'),
        ('EASTER+1',   '🐣\ufe0f🌱\ufe0f Paska Lundo #𝑠𝑦𝑚'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Nojaro #𝑠𝑦𝑚'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️  Kristnaska Vespero #𝑠𝑦𝑚'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Kristnasko #𝑠𝑦𝑚'),
        ('20-55', '🍾\ufe0f🎆\ufe0f Novjara Vespero #𝑠𝑦𝑚'),

        #
        # National Holidays
        # that have a year of reference;
        # There are 2 ways of dealing with them:
        #     1. converting the original date to the Sezimal calendar
        #     2. using the original month and day without converting the calendar
        #
        # Using 2 here, but leaving 1 commented for reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using #i as a format tag
        #
        # ('130_324-01-43', '🇦🇺\ufe0f Tago de Aŭstralio (#i)'),  # Sabato 130_324-01-43 ~ 1788-01-26_dec
        # ('131_055-04-33', '🇦🇺\ufe0f Tago de ANZAC (#i)'),      # Dimanĉo   131_055-04-33 ~ 1915-04-25_dec

        ('212_140-01-43', '🇦🇺\ufe0f Tago de Aŭstralio (#i) #𝑠𝑦𝑚'),  # Sabato 01-42 ~ 01-26_desc
        ('212_511-04-33', '🇦🇺\ufe0f Tago de ANZAC (#i) #𝑠𝑦𝑚'),      # Dimanĉo   04-41 ~ 04-25_dec
    ] + SezimalLocaleEO.HOLIDAYS

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Sankta Vendredo #𝑠𝑦𝑚'),
        ('ISO+EASTER-1',   '🐣\ufe0f🌱\ufe0f Sankta Sabato #𝑠𝑦𝑚'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Pasko #𝑠𝑦𝑚'),
        ('ISO+EASTER+1',   '🐣\ufe0f🌱\ufe0f Paska Lundo #𝑠𝑦𝑚'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f Nojaro #𝑠𝑦𝑚'),
        ('ISO+12-24', '🥂\ufe0f🍽\ufe0f️  Kristnaska Vespero #𝑠𝑦𝑚'),
        ('ISO+12-25', '🌟\ufe0f👼🏼\ufe0f Kristnasko #𝑠𝑦𝑚'),
        ('ISO+12-31', '🍾\ufe0f🎆\ufe0f Novjara Vespero #𝑠𝑦𝑚'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO+1788-01-26', '🇦🇺\ufe0f Tago de Aŭstralio (%i)'),  # Saturday 130_324-01-43 ~ 1788-01-26_dec
        ('ISO+1915-04-25', '🇦🇺\ufe0f Tago de ANZAC (%i)'),      # Sunday   130_324-01-43 ~ 1915-04-25_dec
    ] + SezimalLocaleEO.HOLIDAYS_OTHER_CALENDAR
