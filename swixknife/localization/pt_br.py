

__all__ = ('SezimalLocalePT_BR',)


from .pt import SezimalLocalePT


class SezimalLocalePT_BR(SezimalLocalePT):
    _HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '\ufe0f🎉🎭 Carnaval'),
        ('EASTER-115', '\ufe0f🎉🎭 Carnaval'),
        # ('EASTER-114', '\ufe0f🎉🎭 Quarta-feira de Cinzas'),
        ('EASTER-2',   '\ufe0f🕆 🥀 Paixão de Cristo'),
        ('EASTER',     '\ufe0f🐣🌱 Páscoa'),
        ('EASTER+140', '\ufe0f🥖🍷 Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '\ufe0f🕊️ 🌎 Confraternização Universal'),
        ('05-01', '\ufe0f🐝🐜 Dia do Trabalho'),
        ('14-20', '\ufe0f⛪👸🏿 Nossa Senhora Aparecida'),
        ('15-02', '\ufe0f🪦🕊️  Finados'),
        ('20-40', '\ufe0f🥂🍽️  Véspera de Natal'),
        ('20-41', '\ufe0f🌟👼🏼 Natal'),
        ('20-55', '\ufe0f🍾🎆 Véspera de Ano Novo'),

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
        # ('130_332-04-32', '\ufe0f🇧🇷🔺 Tiradentes'),                # sábado      130_332-04-32 ~ 1792-04-21_dec
        # ('131_124-11-10', '\ufe0f🪖📜 Revolução de 1932 (3̇1̇4̈)'),   # sábado      131_124-11-10 ~ 1932-07-09_dec
        # ('130_422-13-10', '\ufe0f🇧🇷🕊️  Independência do Brasil'),  # sábado      130_422-13-10 ~ 1822-09-07_dec
        # ('131_013-15-31', '\ufe0f🇧🇷📜 Proclamação da República'),  # sexta-feira 131_013-15-31 ~ 1889-11-15_dec
        # ('130_051-15-33', '\ufe0f👨🏿 Consciência Negra'),            # domingo    130_051-15-33 ~ 1695-11-20_dec

        ('130_332-04-33', '\ufe0f🇧🇷🔺 Tiradentes'),                     # domingo,       04-33 ~ 04-21_dec
        ('131_124-11-13', '\ufe0f🪖📜 Revolução de 1932 (3̇1̇4̈) (#i)'),   # terça-feira,   11-13 ~ 07-09_dec
        ('130_422-13-11', '\ufe0f🇧🇷🕊️  Independência do Brasil (#i)'),  # domingo,       13-11 ~ 09-07_dec
        ('131_013-15-23', '\ufe0f🇧🇷📜 Proclamação da República (#i)'),  # segunda-feira, 15-23 ~ 11-15_dec
        ('130_051-15-32', '\ufe0f👨🏿 Consciência Negra'),                # sábado,        15-32 ~ 11-20_dec
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        # ('ISO-EASTER-120', '\ufe0f🎉🎭 Carnaval (%d/%m)'),
        ('ISO-EASTER-115', '\ufe0f🎉🎭 Carnaval (%d/%m)'),
        # ('ISO-EASTER-114', '\ufe0f🎉🎭 Quarta-feira de Cinzas (%d/%m)'),
        ('ISO-EASTER-2',   '\ufe0f🕆 🥀 Paixão de Cristo (%d/%m)'),
        ('ISO-EASTER',     '\ufe0f🐣🌱 Páscoa (%d/%m)'),
        ('ISO-EASTER+140', '\ufe0f🥖🍷 Corpus Christi (%d/%m)'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO-01-01', '\ufe0f🕊️ 🌎 Confraternização Universal (%d/%m)'),
        ('ISO-05-01', '\ufe0f🐝🐜 Dia do Trabalho (%d/%m)'),
        ('ISO-10-12', '\ufe0f⛪👸🏿 Nossa Senhora Aparecida (%d/%m)'),
        ('ISO-11-02', '\ufe0f🪦🕊️  Finados (%d/%m)'),
        ('ISO-12-24', '\ufe0f🥂🍽️  Véspera de Natal (%d/%m)'),
        ('ISO-12-25', '\ufe0f🌟👼🏼 Natal (%d/%m)'),
        ('ISO-12-31', '\ufe0f🍾🎆 Véspera de Ano Novo (%d/%m)'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO-1792-04-21', '\ufe0f🇧🇷🔺 Tiradentes (%d/%m)'),                     # sábado      130_332-04-32 ~ 1792-04-21_dec
        ('ISO-1932-07-09', '\ufe0f🪖📜 Revolução de 1932 (3̇1̇4̈) (%d/%m - %i)'),   # sábado      131_124-11-10 ~ 1932-07-09_dec
        ('ISO-1822-09-07', '\ufe0f🇧🇷🕊️  Independência do Brasil (%d/%m - %i)'),  # sábado      130_422-13-10 ~ 1822-09-07_dec
        ('ISO-1889-11-15', '\ufe0f🇧🇷📜 Proclamação da República (%d/%m - %i)'),  # sexta-feira 131_013-15-31 ~ 1889-11-15_dec
        ('ISO-1695-11-20', '\ufe0f👨🏿 Consciência Negra (%d/%m)'),                # domingo     130_051-15-33 ~ 1695-11-20_dec
    ]
