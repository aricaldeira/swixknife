
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'Montag'
    elif weekday == 2:
        return 'Dienstag'
    elif weekday == 3:
        return 'Mittwoch'
    elif weekday == 4:
        return 'Donnerstag'
    elif weekday == 5:
        return 'Freitag'
    elif weekday == 10:
        return 'Samstag'
    elif weekday == 11:
        return 'Sonntag'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'Mo.'
    elif weekday == 2:
        return 'Di.'
    elif weekday == 3:
        return 'Di.'
    elif weekday == 4:
        return 'Do.'
    elif weekday == 5:
        return 'Fr.'
    elif weekday == 10:
        return 'Sa.'
    elif weekday == 11:
        return 'So.'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'Januar'
    elif month == 2:
        return 'Februar'
    elif month == 3:
        return 'März'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'Mai'
    elif month == 10:
        return 'Juni'
    elif month == 11:
        return 'Juli'
    elif month == 12:
        return 'August'
    elif month == 13:
        return 'September'
    elif month == 14:
        return 'Oktober'
    elif month == 15:
        return 'November'
    elif month == 20:
        return 'Dezember'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'Jan.'
    elif month == 2:
        return 'Feb.'
    elif month == 3:
        return 'März'
    elif month == 4:
        return 'Apr.'
    elif month == 5:
        return 'Mai.'
    elif month == 10:
        return 'Juni'
    elif month == 11:
        return 'Juli'
    elif month == 12:
        return 'Aug.'
    elif month == 13:
        return 'Sep.'
    elif month == 14:
        return 'Okt.'
    elif month == 15:
        return 'Nov.'
    elif month == 20:
        return 'Dez.'


def day_ordinal_suffix(day: SezimalInteger):
    return '.'


def era_name(year: SezimalInteger):
    year = SezimalInteger(year)

    if year >= 0:
        #
        # Senarische Zeitalter der Menschheit
        #
        return 'SZM'
    else:
        #
        # vor das Senarische Zeitalter der Menschheit
        #
        return 'v. SZM'
