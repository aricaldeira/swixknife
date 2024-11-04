

__all__ = ('SezimalLocaleEO_BR',)


from .eo import SezimalLocaleEO
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleEO_BR(SezimalLocaleEO):
    SEZIMAL_SEPARATOR = SEPARATOR_COMMA
    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    DEFAULT_TIME_ZONE = 'America/Sao_Paulo'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    CURRENCY_UNIT_SYMBOL = 'R$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        ('EASTER-120', '🎉\ufe0f🎭\ufe0f Karnavalo'),
        ('EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavalo'),
        ('EASTER-114', '🎉\ufe0f🎭\ufe0f Cindra Merkredo'),
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Pasio de la Kristo'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Pasko'),
        ('EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Universala Kunfrateco'),
        ('05-01', '🐝\ufe0f🐜\ufe0f Labortago'),
        ('14-20', '⛪\ufe0f👸\ufe0f🏿\ufe0f Nia Sinjorino el Aparesida'),
        ('15-02', '🪦\ufe0f🕊\ufe0f️  Ĉiuj Animoj'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️  Kristnaska Antaŭvespero'),
        ('20-41', '🌟\ufe0f👼\ufe0f🏼\ufe0f Kristnasko'),
        ('20-55', '🍾\ufe0f🎆\ufe0f Novjara Antaŭvespero'),

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
        # ('130_332-04-32', '🇧\ufe0f🇷\ufe0f🔺\ufe0f Tiradentes'),                 # Sabato   130_332-04-32 ~ 1792-04-21_dec
        # ('131_124-11-10', '🪖\ufe0f📜\ufe0f Revolucio de 1932 (3̇1̇4̈)'),    # Sabato   131_124-11-10 ~ 1932-07-09_dec
        # ('130_422-13-10', '🇧\ufe0f🇷\ufe0f🕊\ufe0f️  Sendependeco de Brazilo'),   # Sabato   130_422-13-10 ~ 1822-09-07_dec
        # ('131_013-15-31', '🇧\ufe0f🇷\ufe0f📜\ufe0f Proklamo de la Respubliko'),  # Vendredo 131_013-15-31 ~ 1889-11-15_dec
        # ('130_051-15-33', '👨\ufe0f🏿\ufe0f Nigra Konscienco'),             # Dimanĉo  130_051-15-33 ~ 1695-11-20_dec

        ('130_332-04-33', '🇧\ufe0f🇷\ufe0f🔺\ufe0f Tiradentes'),                      # Dimanĉo, 04-33 ~ 04-21_dec
        ('131_124-11-13', '🪖\ufe0f📜\ufe0f Revolucio de 1932 (3̇1̇4̈) (#i)'),    # Mardo,   11-13 ~ 07-09_dec
        ('130_422-13-11', '🇧\ufe0f🇷\ufe0f🕊\ufe0f️  Sendependeco de Brazilo (#i)'),   # Dimanĉo, 13-11 ~ 09-07_dec
        ('131_013-15-23', '🇧\ufe0f🇷\ufe0f📜\ufe0f Proklamo de la Respubliko (#i)'),  # Lundo,   15-23 ~ 11-15_dec
        ('130_051-15-32', '👨\ufe0f🏿\ufe0f Nigra Konscienco'),                  # Sabato,  15-32 ~ 11-20_dec
    ] + SezimalLocaleEO.HOLIDAYS

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        ('ISO+EASTER-120', '🎉\ufe0f🎭\ufe0f Karnavalo (%d-%b)'),
        ('ISO+EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavalo (%d-%b)'),
        ('ISO+EASTER-114', '🎉\ufe0f🎭\ufe0f Cindra Merkredo (%d-%b)'),
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Pasio de la Kristo (%d-%b)'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Pasko (%d-%b)'),
        ('ISO+EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi (%d-%b)'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f Universala Kunfrateco (%d-%b)'),
        ('ISO+05-01', '🐝\ufe0f🐜\ufe0f Labortago (%d-%b)'),
        ('ISO+10-12', '⛪\ufe0f👸\ufe0f🏿\ufe0f Nia Sinjorino el Aparesida (%d-%b)'),
        ('ISO+11-02', '🪦\ufe0f🕊\ufe0f️  Ĉiuj Animoj (%d-%b)'),
        ('ISO+12-24', '🥂\ufe0f🍽\ufe0f️  Kristnaska Antaŭvespero (%d-%b)'),
        ('ISO+12-25', '🌟\ufe0f👼\ufe0f🏼\ufe0f Kristnasko (%d-%b)'),
        ('ISO+12-31', '🍾\ufe0f🎆\ufe0f Novjara Antaŭvespero (%d-%b)'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %-d for year, month and day, respectively
        #
        ('ISO+1792-04-21', '🇧\ufe0f🇷\ufe0f🔺\ufe0f Tiradentes (%d-%b)'),                      # Sabato   130_332-04-32 ~ 1792-04-21_dec
        ('ISO+1932-07-09', '🪖\ufe0f📜\ufe0f Revolucio de 1932 (3̇1̇4̈) (%d-%b - %i)'),    # Sabato   131_124-11-10 ~ 1932-07-09_dec
        ('ISO+1822-09-07', '🇧\ufe0f🇷\ufe0f🕊\ufe0f️  Sendependeco de Brazilo (%d-%b - %i)'),   # Sabato   130_422-13-10 ~ 1822-09-07_dec
        ('ISO+1889-11-15', '🇧\ufe0f🇷\ufe0f📜\ufe0f Proklamo de la Respubliko (%d-%b - %i)'),  # Vendredo 131_013-15-31 ~ 1889-11-15_dec
        ('ISO+1695-11-20', '👨\ufe0f🏿\ufe0f Nigra Konscienco (%d-%b)'),                  # Dimanĉo 130_051-15-33 ~ 1695-11-20_dec
    ] + SezimalLocaleEO.HOLIDAYS_OTHER_CALENDAR
