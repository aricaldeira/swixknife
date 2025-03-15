

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

    FIRST_WEEKDAY = 'SUN'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    CURRENCY_UNIT_SYMBOL = 'R$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '🎉\ufe0f🎭\ufe0f Carnaval'),
        ('EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavalo #𝑠𝑖𝑚'),
        # ('EASTER-114', '🎉\ufe0f🎭\ufe0f Quarta-feira de Cinzas'),
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Pasio de la Kristo #𝑠𝑖𝑚'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Pasko #𝑠𝑖𝑚'),
        ('EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi #𝑠𝑖𝑚'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Universala Kunfrateco #𝑠𝑖𝑚'),
        ('05-01', '🐝\ufe0f🐜\ufe0f Labortago #𝑠𝑖𝑚'),
        ('15-02', '🪦\ufe0f🕊\ufe0f️ Ĉiuj Animoj #𝑠𝑖𝑚'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️ Kristnaska Antaŭvespero #𝑠𝑖𝑚'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Kristnasko #𝑠𝑖𝑚'),
        ('20-55', '🍾\ufe0f🎆\ufe0f Novjara Antaŭvespero #𝑠𝑖𝑚'),

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
        ('212_144-04-32', '🇧🇷\ufe0f🔺\ufe0f Tiradentoj (#i) #𝑠𝑖𝑚'),                # sábado      212_144-04-32 ~ 1792-04-21_dec
        ('212_540-11-10', '🪖\ufe0f📜\ufe0f Revolucio de 1932 (212󱹭540) (#i) #𝑠𝑖𝑚'),   # sábado      212_540-11-10 ~ 1932-07-09_dec
        ('212_234-13-10', '🇧🇷\ufe0f🕊\ufe0f️ Sendependeco de Brazilo (#i) #𝑠𝑖𝑚'),   # sábado      212_234-13-10 ~ 1822-09-07_dec
        ('213_100-14-22', '⛪\ufe0f👸🏾\ufe0f Nia Sinjorino el Aparesida (#i) #𝑠𝑖𝑚'),     # domingo      213_100-14-22 ~ 1980-10-12_dec
        ('212_425-15-31', '🇧🇷\ufe0f📜\ufe0f Proklamo de la Respubliko (#i) #𝑠𝑖𝑚'),  # sexta-feira 212_425-15-31 ~ 1889-11-15_dec
        ('211_503-15-33', '👨🏾\ufe0f Nigra Konscienco (#i) #𝑠𝑖𝑚'),           # domingo     211_503-15-33 ~ 1695-11-20_dec

        #('212_144-04-33', '🇧🇷\ufe0f🔺\ufe0f Tiradentes #𝑠𝑖𝑚'),                     # domingo,       04-33 ~ 04-21_dec
        #('212_540-11-13', '🪖\ufe0f📜\ufe0f Revolução de 1932 (212.540) (#i) #𝑠𝑖𝑚'),   # terça-feira,   11-13 ~ 07-09_dec
        #('212_234-13-11', '🇧🇷\ufe0f🕊\ufe0f️ Independência do Brasil (#i) #𝑠𝑖𝑚'),   # domingo,       13-11 ~ 09-07_dec
        #('213_100-14-20', '⛪\ufe0f👸🏾\ufe0f Nossa Senhora Aparecida #𝑠𝑖𝑚'),     # sexta-feira      14-20 ~ 10-12_dec
        #('212_425-15-23', '🇧🇷\ufe0f📜\ufe0f Proclamação da República (#i) #𝑠𝑖𝑚'),  # segunda-feira, 15-23 ~ 11-15_dec
        #('211_503-15-32', '👨🏾\ufe0f Consciência Negra #𝑠𝑖𝑚'),                # sábado,        15-32 ~ 11-20_dec
    ] + SezimalLocaleEO.HOLIDAYS

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        # ('ISO+EASTER-120', '🎉\ufe0f🎭\ufe0f Carnaval'),
        ('ISO+EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavalo'),
        # ('ISO+EASTER-114', '🎉\ufe0f🎭\ufe0f Quarta-feira de Cinzas'),
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Pasio de la Kristo'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Pasko'),
        ('ISO+EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f Universala Kunfrateco'),
        ('ISO+05-01', '🐝\ufe0f🐜\ufe0f Labortago'),
        ('ISO+11-02', '🪦\ufe0f🕊\ufe0f️ Ĉiuj Animoj'),
        ('ISO+12-24', '🥂\ufe0f🍽\ufe0f️ Kristnaska Antaŭvespero'),
        ('ISO+12-25', '🌟\ufe0f👼🏼\ufe0f Kristnasko'),
        ('ISO+12-31', '🍾\ufe0f🎆\ufe0f Novjara Antaŭvespero'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO+1792-04-21', '🇧🇷\ufe0f🔺\ufe0f Tiradentoj (%i)'),                     # sábado      212_144-04-32 ~ 1792-04-21_dec
        ('ISO+1932-07-09', '🪖\ufe0f📜\ufe0f Revolucio de 1932 (%i)'),   # sábado      212_540-11-10 ~ 1932-07-09_dec
        ('ISO+1822-09-07', '🇧🇷\ufe0f🕊\ufe0f️ Sendependeco de Brazilo (%i)'),   # sábado      212_234-13-10 ~ 1822-09-07_dec
        ('ISO+1980-10-12', '⛪\ufe0f👸🏾\ufe0f Nia Sinjorino el Aparesida (%i)'),     # domingo      213_100-14-22 ~ 1980-10-12_dec
        ('ISO+1889-11-15', '🇧🇷\ufe0f📜\ufe0f Proklamo de la Respubliko (%i)'),  # sexta-feira 212_425-15-31 ~ 1889-11-15_dec
        ('ISO+1695-11-20', '👨🏾\ufe0f Nigra Konscienco (%i)'),                # domingo     211_503-15-33 ~ 1695-11-20_dec
    ] + SezimalLocaleEO.HOLIDAYS_OTHER_CALENDAR
