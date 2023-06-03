
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lundo'
    elif weekday == 2:
        return 'mardo'
    elif weekday == 3:
        return 'merkredo'
    elif weekday == 4:
        return 'ĵaŭdo'
    elif weekday == 5:
        return 'vendredo'
    elif weekday == 10:
        return 'sabato'
    elif weekday == 11:
        return 'dimanĉo'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'lun'
    elif weekday == 2:
        return 'mar'
    elif weekday == 3:
        return 'mer'
    elif weekday == 4:
        return 'ĵaŭ'
    elif weekday == 5:
        return 'ven'
    elif weekday == 10:
        return 'sab'
    elif weekday == 11:
        return 'dim'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'januaro'
    elif month == 2:
        return 'februaro'
    elif month == 3:
        return 'marto'
    elif month == 4:
        return 'aprilo'
    elif month == 5:
        return 'majo'
    elif month == 10:
        return 'junio'
    elif month == 11:
        return 'julio'
    elif month == 12:
        return 'aŭgusto'
    elif month == 13:
        return 'septembro'
    elif month == 14:
        return 'oktobro'
    elif month == 15:
        return 'novembro'
    elif month == 20:
        return 'decembro'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'jan'
    elif month == 2:
        return 'feb'
    elif month == 3:
        return 'mar'
    elif month == 4:
        return 'apr'
    elif month == 5:
        return 'maj'
    elif month == 10:
        return 'jun'
    elif month == 11:
        return 'jul'
    elif month == 12:
        return 'aŭg'
    elif month == 13:
        return 'sep'
    elif month == 14:
        return 'okt'
    elif month == 15:
        return 'nov'
    elif month == 20:
        return 'dec'


def day_ordinal_suffix(day: SezimalInteger):
    return 'a'


def era_name(year: SezimalInteger):
    year = SezimalInteger(year)

    if year >= 0:
        #
        # Sesuma Homara Erao
        #
        return 'SHE'
    else:
        #
        # Antaŭ Sesuma Homara Erao
        #
        return 'aSHE'
