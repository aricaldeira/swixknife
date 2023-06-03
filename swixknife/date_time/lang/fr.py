
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lundi'
    elif weekday == 2:
        return 'mardi'
    elif weekday == 3:
        return 'mercredi'
    elif weekday == 4:
        return 'jeudi'
    elif weekday == 5:
        return 'vendredi'
    elif weekday == 10:
        return 'samedi'
    elif weekday == 11:
        return 'dimanche'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lundi'
    elif weekday == 2:
        return 'mardi'
    elif weekday == 3:
        return 'mercr.'
    elif weekday == 4:
        return 'jeudi'
    elif weekday == 5:
        return 'vendr.'
    elif weekday == 10:
        return 'sam.'
    elif weekday == 11:
        return 'dim.'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'janvier'
    elif month == 2:
        return 'février'
    elif month == 3:
        return 'mars'
    elif month == 4:
        return 'avril'
    elif month == 5:
        return 'mai'
    elif month == 10:
        return 'juin'
    elif month == 11:
        return 'juillet'
    elif month == 12:
        return 'août'
    elif month == 13:
        return 'septembre'
    elif month == 14:
        return 'octobre'
    elif month == 15:
        return 'novembre'
    elif month == 20:
        return 'décembre'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'janv.'
    elif month == 2:
        return 'févr.'
    elif month == 3:
        return 'mars'
    elif month == 4:
        return 'avr.'
    elif month == 5:
        return 'mai'
    elif month == 10:
        return 'juin'
    elif month == 11:
        return 'juill.'
    elif month == 12:
        return 'août'
    elif month == 13:
        return 'sept.'
    elif month == 14:
        return 'oct.'
    elif month == 15:
        return 'nov.'
    elif month == 20:
        return 'déc.'


def day_ordinal_suffix(day: SezimalInteger):
    day = SezimalInteger(day)

    if day == 1:
        return 'ᵉʳ'

    return ''


def era_name(year: SezimalInteger):
    year = SezimalInteger(year)

    if year >= 0:
        #
        # Ère Humaine Sezimale
        #
        return 'ÈHS'
    else:
        #
        # Avant l’Ère Humaine Sezimale
        #
        return 'av. l’ÈHS'
