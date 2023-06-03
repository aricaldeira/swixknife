
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'Segunda-Feira'
    elif weekday == 2:
        return 'Terça-Feira'
    elif weekday == 3:
        return 'Quarta-Feira'
    elif weekday == 4:
        return 'Quinta-Feira'
    elif weekday == 5:
        return 'Sexta-Feira'
    elif weekday == 10:
        return 'Sábado'
    elif weekday == 11:
        return 'Domingo'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'Seg'
    elif weekday == 2:
        return 'Ter'
    elif weekday == 3:
        return 'Qua'
    elif weekday == 4:
        return 'Qui'
    elif weekday == 5:
        return 'Sex'
    elif weekday == 10:
        return 'Sáb'
    elif weekday == 11:
        return 'Dom'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'Janeiro'
    elif month == 2:
        return 'Fevereiro'
    elif month == 3:
        return 'Março'
    elif month == 4:
        return 'Abril'
    elif month == 5:
        return 'Maio'
    elif month == 10:
        return 'Junho'
    elif month == 11:
        return 'Julho'
    elif month == 12:
        return 'Agosto'
    elif month == 13:
        return 'Setembro'
    elif month == 14:
        return 'Outubro'
    elif month == 15:
        return 'Novembro'
    elif month == 20:
        return 'Dezembro'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'Jan'
    elif month == 2:
        return 'Fev'
    elif month == 3:
        return 'Mar'
    elif month == 4:
        return 'Abr'
    elif month == 5:
        return 'Mai'
    elif month == 10:
        return 'Jun'
    elif month == 11:
        return 'Jul'
    elif month == 12:
        return 'Ago'
    elif month == 13:
        return 'Set'
    elif month == 14:
        return 'Out'
    elif month == 15:
        return 'Nov'
    elif month == 20:
        return 'Dez'


def day_ordinal_suffix(day: SezimalInteger):
    day = SezimalInteger(day)

    if day == 1:
        return '.º'

    return ''


def era_name(year: SezimalInteger):
    year = SezimalInteger(year)

    if year >= 0:
        #
        # Era Humana Sezimal
        #
        return 'EHS'
    else:
        #
        # Antes da Era Humana Sezimal
        #
        return 'aEHS'
