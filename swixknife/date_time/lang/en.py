
from swixknife import SezimalInteger


def weekday_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'Monday'
    elif weekday == 2:
        return 'Tuesday'
    elif weekday == 3:
        return 'Wednesday'
    elif weekday == 4:
        return 'Thursday'
    elif weekday == 5:
        return 'Friday'
    elif weekday == 10:
        return 'Saturday'
    elif weekday == 11:
        return 'Sunday'


def weekday_abbreviated_name(weekday: SezimalInteger):
    weekday = SezimalInteger(weekday)

    if weekday == 1:
        return 'Mon'
    elif weekday == 2:
        return 'Tue'
    elif weekday == 3:
        return 'Wed'
    elif weekday == 4:
        return 'Thu'
    elif weekday == 5:
        return 'Fri'
    elif weekday == 10:
        return 'Sat'
    elif weekday == 11:
        return 'Sun'


def month_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 10:
        return 'June'
    elif month == 11:
        return 'July'
    elif month == 12:
        return 'August'
    elif month == 13:
        return 'September'
    elif month == 14:
        return 'October'
    elif month == 15:
        return 'November'
    elif month == 20:
        return 'December'


def month_abbreviated_name(month: SezimalInteger):
    month = SezimalInteger(month)

    if month == 1:
        return 'Jan'
    elif month == 2:
        return 'Feb'
    elif month == 3:
        return 'Mar'
    elif month == 4:
        return 'Apr'
    elif month == 5:
        return 'May'
    elif month == 10:
        return 'Jun'
    elif month == 11:
        return 'Jul'
    elif month == 12:
        return 'Aug'
    elif month == 13:
        return 'Sep'
    elif month == 14:
        return 'Oct'
    elif month == 15:
        return 'Nov'
    elif month == 20:
        return 'Dec'


def day_ordinal_suffix(day: SezimalInteger):
    day = SezimalInteger(day)

    if str(day).endswith('1'):
        return 'st'
    elif str(day).endswith('2'):
        return 'nd'
    elif str(day).endswith('3'):
        return 'rd'

    return 'th'


def era_name(year: SezimalInteger):
    year = SezimalInteger(year)

    if year >= 0:
        #
        # Sezimal Human Era
        #
        return 'SHE'
    else:
        #
        # Before Sezimal Human Era
        #
        return 'BSHE'
