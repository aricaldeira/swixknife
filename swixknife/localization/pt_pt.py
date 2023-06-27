

__all__ = ('SezimalLocalePT_PT',)


from .pt import SezimalLocalePT


class SezimalLocalePT_PT(SezimalLocalePT):
    LANG = 'pt'
    LANGUAGE = 'português europeu'

    DEFAULT_TIME_ZONE = 'Europe/Lisbon'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern

    HOLIDAYS = {
        #
        # Moving Holydays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        '02-35': '\ufe0f🎉 Carnaval',
        '04-05': '\ufe0f🥀 Sexta-feira Santa',
        '04-11': '\ufe0f🐣 Páscoa',
        '05-45': '\ufe0f🌟 Segunda-feira do Espírito Santo',
        '10-04': '\ufe0f🍷 Corpo de Deus',

        #
        # National Holidays
        # I chose not to convert the dates from their original occurrences,
        # since Holidays from before the adoption of the Gregorian Reform
        # were also not converted
        #
        '01-01': '\ufe0f🕊️  Ano Novo',
        '04-41': '\ufe0f🇵🇹 Dia da Liberdade',
        '05-01': '\ufe0f🐝 Dia do Trabalhador',
        '10-14': '\ufe0f🇵🇹 Dia de Portugal',
        '12-23': '\ufe0f⛪ Assunção de Nossa Senhora',
        '14-05': '\ufe0f🇵🇹 Implantação da República',
        '15-01': '\ufe0f🪦 Todos os Santos',
        '20-01': '\ufe0f🇵🇹 Restauração da Independência',
        '20-12': '\ufe0f⛪ Imaculada Conceição',
        '20-41': '\ufe0f👼🏼 Natal',
    }
