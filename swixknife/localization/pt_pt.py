

__all__ = ('SezimalLocalePT_PT',)


from .pt import SezimalLocalePT


class SezimalLocalePT_PT(SezimalLocalePT):
    LANG = 'pt'
    LANGUAGE = 'português europeu'

    DEFAULT_TIME_ZONE = 'Europe/Lisbon'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern

    _HOLIDAYS = [
        #
        # Moving Holydays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        ('EASTER-115', '\ufe0f🎉 Carnaval'),
        ('EASTER-2',   '\ufe0f🥀 Sexta-feira Santa'),
        ('EASTER',     '\ufe0f🐣 Páscoa'),
        ('EASTER+140', '\ufe0f🥖 Corpo de Deus'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '\ufe0f⛪ Santa Mãe de Deus'),
        ('05-01', '\ufe0f🐝 Dia do Trabalhador'),
        ('12-23', '\ufe0f⛪ Assunção de Nossa Senhora'),
        ('15-01', '\ufe0f🪦 Todos os Santos'),
        ('20-12', '\ufe0f⛪ Imaculada Conceição'),
        ('20-41', '\ufe0f👼🏼 Natal'),

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
        # ('131_234-04-41', '\ufe0f🇵🇹 Dia da Liberdade (#i)'),              # quinta-feira 131_234-04-41 ~ 1974-04-25_dec
        # ('125_340-10-13', '\ufe0f🇵🇹 Dia de Portugal (#i)'),               # terça-feira  125_340-10-13 ~ 1580-06-10_dec
        # ('131_050-14-03', '\ufe0f🇵🇹 Implantação da República (#i)'),      # quarta-feira 131_050-14-03 ~ 1910-10-05_dec
        # ('125_520-15-54', '\ufe0f🇵🇹 Restauração da Independência (#i)'),  # sábado       125_520-15-54 ~ 1640-12-01_dec

        ('131_234-04-41', '\ufe0f🇵🇹 Dia da Liberdade (#i)'),              # quinta-feira,  04-41 ~ 04-25_dec
        ('125_340-10-14', '\ufe0f🇵🇹 Dia de Portugal (#i)'),               # quarta-feira,  10-14 ~ 06-10_dec
        ('131_050-14-05', '\ufe0f🇵🇹 Implantação da República (#i)'),      # sexta-feira,   14-05 ~ 10-05_dec
        ('125_520-20-01', '\ufe0f🇵🇹 Restauração da Independência (#i)'),  # segunda-feira, 20-01 ~ 12-01_dec
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO+EASTER-115', '\ufe0f🎉 Carnaval (%d/%m)'),
        ('ISO+EASTER-2',   '\ufe0f🥀 Sexta-feira Santa (%d/%m)'),
        ('ISO+EASTER',     '\ufe0f🐣 Páscoa (%d/%m)'),
        ('ISO+EASTER+140', '\ufe0f🥖 Corpo de Deus (%d/%m)'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '\ufe0f⛪ Santa Mãe de Deus (%d/%m)'),
        ('ISO+05-01', '\ufe0f🐝 Dia do Trabalhador (%d/%m)'),
        ('ISO+08-15', '\ufe0f⛪ Assunção de Nossa Senhora (%d/%m)'),
        ('ISO+11-02', '\ufe0f🪦 Todos os Santos (%d/%m)'),
        ('ISO+12-08', '\ufe0f⛪ Imaculada Conceição (%d/%m)'),
        ('ISO+12-25', '\ufe0f👼🏼 Natal (%d/%m)'),

        #
        # National Holidays
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO+1974-04-25', '\ufe0f🇵🇹 Dia da Liberdade (%d/%m - %i)'),
        ('ISO+1580-06-10', '\ufe0f🇵🇹 Dia de Portugal (%d/%m - %i)'),
        ('ISO+1910-10-05', '\ufe0f🇵🇹 Implantação da República (%d/%m - %i)'),
        ('ISO+1640-12-01', '\ufe0f🇵🇹 Restauração da Independência (%d/%m - %i)'),
    ]

