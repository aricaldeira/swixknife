
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lunes'
    elif weekday == 2:
        return 'martes'
    elif weekday == 3:
        return 'miércoles'
    elif weekday == 4:
        return 'jueves'
    elif weekday == 5:
        return 'viernes'
    elif weekday == 10:
        return 'sábado'
    elif weekday == 11:
        return 'domingo'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lun'
    elif weekday == 2:
        return 'mar'
    elif weekday == 3:
        return 'mié'
    elif weekday == 4:
        return 'jue'
    elif weekday == 5:
        return 'vie'
    elif weekday == 10:
        return 'sáb'
    elif weekday == 11:
        return 'dom'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'enero'
    elif month == 2:
        return 'febrero'
    elif month == 3:
        return 'marzo'
    elif month == 4:
        return 'abril'
    elif month == 5:
        return 'mayo'
    elif month == 10:
        return 'junio'
    elif month == 11:
        return 'julio'
    elif month == 12:
        return 'agosto'
    elif month == 13:
        return 'septiembre'
    elif month == 14:
        return 'octubre'
    elif month == 15:
        return 'noviembre'
    elif month == 20:
        return 'diciembre'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'ene'
    elif month == 2:
        return 'feb'
    elif month == 3:
        return 'mar'
    elif month == 4:
        return 'abr'
    elif month == 5:
        return 'may'
    elif month == 10:
        return 'jun'
    elif month == 11:
        return 'jul'
    elif month == 12:
        return 'ago'
    elif month == 13:
        return 'sep'
    elif month == 14:
        return 'oct'
    elif month == 15:
        return 'nov'
    elif month == 20:
        return 'dic'


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
        # Antes de la Era Humana Sezimal
        #
        return 'aEHS'
