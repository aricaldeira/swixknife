
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'segunda-feira'
    elif weekday == 2:
        return 'terça-feira'
    elif weekday == 3:
        return 'quarta-feira'
    elif weekday == 4:
        return 'quinta-feira'
    elif weekday == 5:
        return 'sexta-feira'
    elif weekday == 10:
        return 'sábado'
    elif weekday == 11:
        return 'domingo'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'seg'
    elif weekday == 2:
        return 'ter'
    elif weekday == 3:
        return 'qua'
    elif weekday == 4:
        return 'qui'
    elif weekday == 5:
        return 'sex'
    elif weekday == 10:
        return 'sáb'
    elif weekday == 11:
        return 'dom'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'janeiro'
    elif month == 2:
        return 'fevereiro'
    elif month == 3:
        return 'março'
    elif month == 4:
        return 'abril'
    elif month == 5:
        return 'maio'
    elif month == 10:
        return 'junho'
    elif month == 11:
        return 'julho'
    elif month == 12:
        return 'agosto'
    elif month == 13:
        return 'setembro'
    elif month == 14:
        return 'outubro'
    elif month == 15:
        return 'novembro'
    elif month == 20:
        return 'dezembro'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'jan'
    elif month == 2:
        return 'fev'
    elif month == 3:
        return 'mar'
    elif month == 4:
        return 'abr'
    elif month == 5:
        return 'mai'
    elif month == 10:
        return 'jun'
    elif month == 11:
        return 'jul'
    elif month == 12:
        return 'ago'
    elif month == 13:
        return 'set'
    elif month == 14:
        return 'out'
    elif month == 15:
        return 'nov'
    elif month == 20:
        return 'dez'


def day_ordinal_suffix(day: SezimalInteger):
    day = SezimalInteger(day)

    if day == 1:
        return 'º'

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
