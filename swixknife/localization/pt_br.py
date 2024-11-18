

__all__ = ('SezimalLocalePT_BR',)


from .pt import SezimalLocalePT


class SezimalLocalePT_BR(SezimalLocalePT):
    HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '🎉\ufe0f🎭\ufe0f Carnaval'),
        ('EASTER-115', '🎉\ufe0f🎭\ufe0f Carnaval #sim'),
        # ('EASTER-114', '🎉\ufe0f🎭\ufe0f Quarta-feira de Cinzas'),
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Paixão de Cristo #sim'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Páscoa #sim'),
        ('EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi #sim'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Confraternização Universal #sim'),
        ('05-01', '🐝\ufe0f🐜\ufe0f Dia do Trabalho #sim'),
        ('15-02', '🪦\ufe0f🕊\ufe0f️  Finados #sim'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️  Véspera de Natal #sim'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Natal #sim'),
        ('20-55', '🍾\ufe0f🎆\ufe0f Véspera de Ano Novo #sim'),

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
        ('212_144-04-32', '🇧🇷\ufe0f🔺\ufe0f Tiradentes (#i) #sim'),                # sábado      212_144-04-32 ~ 1792-04-21_dec
        ('212_540-11-10', '🪖\ufe0f📜\ufe0f Revolução de 1932 (212.540) (#i) #sim'),   # sábado      212_540-11-10 ~ 1932-07-09_dec
        ('212_234-13-10', '🇧🇷\ufe0f🕊\ufe0f️ Independência do Brasil (#i) #sim'),   # sábado      212_234-13-10 ~ 1822-09-07_dec
        ('213_100-14-22', '⛪\ufe0f👸🏿\ufe0f Nossa Senhora Aparecida (#i) #sim'),     # domingo      213_100-14-22 ~ 1980-10-12_dec
        ('212_425-15-31', '🇧🇷\ufe0f📜\ufe0f Proclamação da República (#i) #sim'),  # sexta-feira 212_425-15-31 ~ 1889-11-15_dec
        ('211_503-15-33', '👨🏿\ufe0f Consciência Negra (#i) #sim'),           # domingo     211_503-15-33 ~ 1695-11-20_dec

        #('212_144-04-33', '🇧🇷\ufe0f🔺\ufe0f Tiradentes #sim'),                     # domingo,       04-33 ~ 04-21_dec
        #('212_540-11-13', '🪖\ufe0f📜\ufe0f Revolução de 1932 (212.540) (#i) #sim'),   # terça-feira,   11-13 ~ 07-09_dec
        #('212_234-13-11', '🇧🇷\ufe0f🕊\ufe0f️ Independência do Brasil (#i) #sim'),   # domingo,       13-11 ~ 09-07_dec
        #('213_100-14-20', '⛪\ufe0f👸🏿\ufe0f Nossa Senhora Aparecida #sim'),     # sexta-feira      14-20 ~ 10-12_dec
        #('212_425-15-23', '🇧🇷\ufe0f📜\ufe0f Proclamação da República (#i) #sim'),  # segunda-feira, 15-23 ~ 11-15_dec
        #('211_503-15-32', '👨🏿\ufe0f Consciência Negra #sim'),                # sábado,        15-32 ~ 11-20_dec
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        # ('ISO+EASTER-120', '🎉\ufe0f🎭\ufe0f Carnaval'),
        ('ISO+EASTER-115', '🎉\ufe0f🎭\ufe0f Carnaval'),
        # ('ISO+EASTER-114', '🎉\ufe0f🎭\ufe0f Quarta-feira de Cinzas'),
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Paixão de Cristo'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Páscoa'),
        ('ISO+EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f Confraternização Universal'),
        ('ISO+05-01', '🐝\ufe0f🐜\ufe0f Dia do Trabalho'),
        ('ISO+11-02', '🪦\ufe0f🕊\ufe0f️  Finados'),
        ('ISO+12-24', '🥂\ufe0f🍽\ufe0f️  Véspera de Natal'),
        ('ISO+12-25', '🌟\ufe0f👼🏼\ufe0f Natal'),
        ('ISO+12-31', '🍾\ufe0f🎆\ufe0f Véspera de Ano Novo'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO+1792-04-21', '🇧🇷\ufe0f🔺\ufe0f Tiradentes (%i)'),                     # sábado      212_144-04-32 ~ 1792-04-21_dec
        ('ISO+1932-07-09', '🪖\ufe0f📜\ufe0f Revolução de 1932 (1̈5̈0̄/540) (%i)'),   # sábado      212_540-11-10 ~ 1932-07-09_dec
        ('ISO+1822-09-07', '🇧🇷\ufe0f🕊\ufe0f️ Independência do Brasil (%i)'),   # sábado      212_234-13-10 ~ 1822-09-07_dec
        ('ISO+1980-10-12', '⛪\ufe0f👸🏿\ufe0f Nossa Senhora Aparecida (%i)'),     # domingo      213_100-14-22 ~ 1980-10-12_dec
        ('ISO+1889-11-15', '🇧🇷\ufe0f📜\ufe0f Proclamação da República (%i)'),  # sexta-feira 212_425-15-31 ~ 1889-11-15_dec
        ('ISO+1695-11-20', '👨🏿\ufe0f Consciência Negra (%i)'),                # domingo     211_503-15-33 ~ 1695-11-20_dec
    ]
