
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'segunda'
    elif weekday == 2:
        return 'tersa'
    elif weekday == 3:
        return 'kwarta'
    elif weekday == 4:
        return 'kinta'
    elif weekday == 5:
        return 'sesta'
    elif weekday == 10:
        return 'sábadu'
    elif weekday == 11:
        return 'dumingu'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'seg'
    elif weekday == 2:
        return 'ter'
    elif weekday == 3:
        return 'kwa'
    elif weekday == 4:
        return 'kin'
    elif weekday == 5:
        return 'ses'
    elif weekday == 10:
        return 'sáb'
    elif weekday == 11:
        return 'dum'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'janeru'
    elif month == 2:
        return 'fevereru'
    elif month == 3:
        return 'marsu'
    elif month == 4:
        return 'abriw'
    elif month == 5:
        return 'mayu'
    elif month == 10:
        return 'juỹu'
    elif month == 11:
        return 'julyu'
    elif month == 12:
        return 'agostu'
    elif month == 13:
        return 'setenbru'
    elif month == 14:
        return 'otubru'
    elif month == 15:
        return 'novenbru'
    elif month == 20:
        return 'dezenbru'


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
        return 'may'
    elif month == 10:
        return 'juỹ'
    elif month == 11:
        return 'jul'
    elif month == 12:
        return 'ago'
    elif month == 13:
        return 'set'
    elif month == 14:
        return 'otu'
    elif month == 15:
        return 'nov'
    elif month == 20:
        return 'dez'


def day_ordinal_suffix(day: SezimalInteger):
    day = SezimalInteger(day)

    if day == 1:
        return 'ᵘ̱'

    return ''


def era_name(year: SezimalInteger):
    year = SezimalInteger(year)

    if year >= 0:
        #
        # Èra Umana Sezimaw
        #
        return 'ÈUS'
    else:
        #
        # Antis da Èra Umana Sezimaw
        #
        return 'aÈUS'
