
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lunedì'
    elif weekday == 2:
        return 'martedì'
    elif weekday == 3:
        return 'mercoledì'
    elif weekday == 4:
        return 'giovedì'
    elif weekday == 5:
        return 'venerdì'
    elif weekday == 10:
        return 'sabato'
    elif weekday == 11:
        return 'domenica'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lun'
    elif weekday == 2:
        return 'mar'
    elif weekday == 3:
        return 'mer'
    elif weekday == 4:
        return 'gio'
    elif weekday == 5:
        return 'ven'
    elif weekday == 10:
        return 'sab'
    elif weekday == 11:
        return 'dom'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'gennaio'
    elif month == 2:
        return 'febbraio'
    elif month == 3:
        return 'marzo'
    elif month == 4:
        return 'aprile'
    elif month == 5:
        return 'maggio'
    elif month == 10:
        return 'giugno'
    elif month == 11:
        return 'luglio'
    elif month == 12:
        return 'agosto'
    elif month == 13:
        return 'settembre'
    elif month == 14:
        return 'ottobre'
    elif month == 15:
        return 'novembre'
    elif month == 20:
        return 'dicembre'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'gen'
    elif month == 2:
        return 'feb'
    elif month == 3:
        return 'mar'
    elif month == 4:
        return 'apr'
    elif month == 5:
        return 'mag'
    elif month == 10:
        return 'giu'
    elif month == 11:
        return 'lug'
    elif month == 12:
        return 'ago'
    elif month == 13:
        return 'set'
    elif month == 14:
        return 'ott'
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
        # Era Umana Sesimale
        #
        return 'EUS'
    else:
        #
        # Avanti l’Era Umana Sesimale
        #
        return 'aEUS'
