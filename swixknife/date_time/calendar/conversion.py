
from typing import TypeAlias

import time as _time
import datetime as _datetime
from decimal import Decimal

from ..sezimal_functions import *
from ...sezimal import SezimalInteger


DateConversion: TypeAlias = tuple[
    #
    # The date as an ordinal date,
    # a tuple with year, month and day,
    # and the age in years
    #
    SezimalInteger,
    tuple[int | SezimalInteger, int | SezimalInteger, int | SezimalInteger],
    SezimalInteger,
]


try:
    from convertdate.julian import from_gregorian as gregorian_to_julian, to_gregorian as julian_to_gregorian
    from convertdate.hebrew import from_gregorian as gregorian_to_hebrew, to_gregorian as hebrew_to_gregorian
    from convertdate.islamic import from_gregorian as gregorian_to_hijri, to_gregorian as hijri_to_gregorian
    from convertdate.persian import from_gregorian as gregorian_to_jalali, to_gregorian as jalali_to_gregorian
    from convertdate.indian_civil import from_gregorian as gregorian_to_indian, to_gregorian as indian_to_gregorian

    CAN_CONVERT_CALENDARS = True
except:
    CAN_CONVERT_CALENDARS = False

try:
    from lunardate import LunarDate

    CAN_CONVERT_LUNAR_CALENDAR = True
except:
    CAN_CONVERT_LUNAR_CALENDAR = False


#
# This method was copied and adapted from the dateutil package
#

EASTER_SEZIMAL = 0
EASTER_JULIAN_ORIGINAL = 1
EASTER_JULIAN_REVISED = 2
EASTER_GREGORIAN = 3
EASTER_HEBREW = 4


#
# Convert dates from other calendars into Sezimal dates
# Also converts dates relative to Easter in Sezimal,
# Gregorian, Julian and Hebrew calendars
#
def other_calendar_date_to_ordinal_date(date_time: str, reference_year: SezimalInteger = None) -> DateConversion:
    #
    # Sets a Gregorian/ISO date as a point of reference for
    # other calendars’ conversion
    #
    if not reference_year:
        iso_reference = _datetime.date.today()

        ordinal_date = gregorian_year_month_day_to_ordinal_date(iso_reference.year, iso_reference.month, iso_reference.day)
        year, month, day, *x = ordinal_to_year_month_day(ordinal_date)

        reference_year = year

    if VALID_DATE_STRING.match(date_time) or VALID_MONTH_DAY_STRING.match(date_time):
        return _other_calendar_to_ordinal_date('SEZ-' + date_time, reference_year)

    elif VALID_DATE_OTHER_CALENDAR_STRING.match(date_time) or VALID_MONTH_DAY_OTHER_CALENDAR_STRING.match(date_time):
        return _other_calendar_to_ordinal_date(date_time, reference_year)

    elif VALID_EASTER_DATE_STRING.match(date_time):
        return _easter_calendar_to_ordinal_date(date_time, reference_year)

    raise ValueError(f'Invalid format for calendar date: {date_time}')


def _other_calendar_to_ordinal_date(date_time: str, reference_year: SezimalInteger) -> DateConversion:
    calendar = date_time[0:3]

    if (calendar not in ('SEZ', 'ISO', 'GRE') ) and (not CAN_CONVERT_CALENDARS):
        raise ValueError(f'Can’t convert date {date_time} from specified calendar; please install convertdate')

    date_time = date_time[4:]

    parts = date_time.split('-')

    if len(parts) == 2:
        month, day = parts
        year = None

    else:
        year, month, day = parts

    if calendar == 'SEZ':
        if not year:
            year = reference_year
        else:
            year = SezimalInteger(year)

        month = SezimalInteger(month)
        day = SezimalInteger(day)

        original_year = year
        year = reference_year
        age = year - original_year

        #
        # If the date is on the leap week, and the year is not leap,
        # move date day to the corresponding weekday of the last
        # week of the year
        #
        if month == 20 and day > 44 and (not is_leap(year)):
            day -= 11

        ymd = (year, month, day)

        ordinal_date = year_month_day_to_ordinal(*ymd)

        return ordinal_date, ymd, age

    year_start_ordinal = year_month_day_to_ordinal(reference_year, SezimalInteger('1'), SezimalInteger('1'))

    if is_leap(reference_year):
        year_end_ordinal = year_month_day_to_ordinal(reference_year, SezimalInteger('20'), SezimalInteger('55'))
        year_middle_ordinal = year_start_ordinal + SezimalInteger('505')
    else:
        year_end_ordinal = year_month_day_to_ordinal(reference_year, SezimalInteger('20'), SezimalInteger('44'))
        year_middle_ordinal = year_start_ordinal + SezimalInteger('502')

    iso_reference = _datetime.date.fromordinal(int(year_start_ordinal.decimal))

    if year:
        year = int(year)

    month = int(month)
    day = int(day)

    if calendar == 'ISO' or calendar == 'GRE':
        if not year:
            year = iso_reference.year

        original_year = SezimalInteger(Decimal(year))
        year = iso_reference.year
        age = SezimalInteger(Decimal(year)) - original_year

        ymd = (year, month, day)

        ordinal_date = gregorian_year_month_day_to_ordinal_date(*ymd)

        return ordinal_date, ymd, age

    if calendar == 'JUL':
        if not year:
            year, *x = gregorian_to_julian(iso_reference.year, iso_reference.month, iso_reference.day)

        original_ymd = (year, month, day)
        ymd = (year, month, day)

        iso_date = _datetime.date(*julian_to_gregorian(*original_ymd))
        original_ordinal_date = gregorian_year_month_day_to_ordinal_date(iso_date.year, iso_date.month, iso_date.day)

        age = SezimalInteger(Decimal(iso_reference.year - iso_date.year))

        if age != 0:
            year += int(age.decimal)
            ymd = (year, month, day)
            iso_date = _datetime.date(*julian_to_gregorian(*ymd))

    elif calendar == 'HEB':
        if not year:
            year, *x = gregorian_to_hebrew(iso_reference.year, iso_reference.month, iso_reference.day)

        original_ymd = (year, month, day)
        ymd = (year, month, day)

        iso_date = _datetime.date(*hebrew_to_gregorian(*original_ymd))
        original_ordinal_date = gregorian_year_month_day_to_ordinal_date(iso_date.year, iso_date.month, iso_date.day)

        age = SezimalInteger(Decimal(iso_reference.year - iso_date.year))

        if age != 0:
            year += int(age.decimal)
            ymd = (year, month, day)
            iso_date = _datetime.date(*hebrew_to_gregorian(*ymd))

    elif calendar == 'HIJ':
        if not year:
            year, *x = gregorian_to_hijri(iso_reference.year, iso_reference.month, iso_reference.day)

        original_ymd = (year, month, day)
        ymd = (year, month, day)

        iso_date = _datetime.date(*hijri_to_gregorian(*original_ymd))
        original_ordinal_date = gregorian_year_month_day_to_ordinal_date(iso_date.year, iso_date.month, iso_date.day)

        age = SezimalInteger(Decimal(iso_reference.year - iso_date.year))

        if age != 0:
            year += int(age.decimal)
            ymd = (year, month, day)
            iso_date = _datetime.date(*hijri_to_gregorian(*ymd))

    elif calendar == 'JAL':
        if not year:
            year, *x = gregorian_to_jalali(iso_reference.year, iso_reference.month, iso_reference.day)

        original_ymd = (year, month, day)
        ymd = (year, month, day)

        iso_date = _datetime.date(*jalali_to_gregorian(*original_ymd))
        original_ordinal_date = gregorian_year_month_day_to_ordinal_date(iso_date.year, iso_date.month, iso_date.day)

        age = SezimalInteger(Decimal(iso_reference.year - iso_date.year))

        if age != 0:
            year += int(age.decimal)
            ymd = (year, month, day)
            iso_date = _datetime.date(*jalali_to_gregorian(*ymd))

    elif calendar == 'IND':
        if not year:
            year, *x = gregorian_to_indian(iso_reference.year, iso_reference.month, iso_reference.day)

        original_ymd = (year, month, day)
        ymd = (year, month, day)

        iso_date = _datetime.date(*indian_to_gregorian(*original_ymd))
        original_ordinal_date = gregorian_year_month_day_to_ordinal_date(iso_date.year, iso_date.month, iso_date.day)

        age = SezimalInteger(Decimal(iso_reference.year - iso_date.year))

        if age != 0:
            year += int(age.decimal)
            ymd = (year, month, day)
            iso_date = _datetime.date(*indian_to_gregorian(*ymd))

    ordinal_date = gregorian_year_month_day_to_ordinal_date(iso_date.year, iso_date.month, iso_date.day)

    return ordinal_date, ymd, age


def _easter_calendar_to_ordinal_date(date_time: str, reference_year: SezimalInteger) -> DateConversion:
    calendar = date_time[0:3]

    if calendar == 'ISO' or calendar == 'GRE':
        easter = EASTER_GREGORIAN
        date_time = date_time.replace('ISO-', '')
        date_time = date_time.replace('GRE-', '')

    elif calendar == 'JUL' or 'PASCHA' in date_time or 'PASKHA' in date_time:
        easter = EASTER_JULIAN_REVISED
        date_time = date_time.replace('JUL-', '')

    elif calendar == 'HEB' or 'PESACH' in date_time:
        easter = EASTER_HEBREW
        date_time = date_time.replace('HEB-', '')

    else:
        easter = EASTER_SEZIMAL
        date_time = date_time.replace('SEZ-', '')

    date_time = date_time.replace('PASCHA', 'EASTER')
    date_time = date_time.replace('PASKHA', 'EASTER')
    date_time = date_time.replace('PESACH', 'EASTER')

    if easter == EASTER_GREGORIAN:
        easter_ordinal_date = traditional_easter_ordinal_date(reference_year, method=EASTER_GREGORIAN)
    elif easter == EASTER_JULIAN_REVISED:
        easter_ordinal_date = traditional_easter_ordinal_date(reference_year, method=EASTER_JULIAN_REVISED)
    elif easter == EASTER_HEBREW:
        easter_ordinal_date = traditional_easter_ordinal_date(reference_year, method=EASTER_HEBREW)
    else:
        easter_ordinal_date = year_month_day_to_ordinal(reference_year, 4, 11)

    expression = date_time.replace('EASTER', f"SezimalInteger('{easter_ordinal_date}')")
    ordinal_date = eval(expression)

    iso_ymd = _datetime.date.fromordinal(int(ordinal_date.decimal)).timetuple()[0:3]

    if easter == EASTER_GREGORIAN or easter == EASTER_JULIAN_REVISED:
        ymd = iso_ymd

    # elif easter == EASTER_JULIAN_REVISED:
    #     if CAN_CONVERT_CALENDARS:
    #         ymd = gregorian_to_julian(*iso_ymd)
    #     else:
    #         ymd = iso_ymd

    elif easter == EASTER_HEBREW:
        if CAN_CONVERT_CALENDARS:
            ymd = gregorian_to_hebrew(*iso_ymd)
        else:
            ymd = iso_ymd

    else:
        ymd = (reference_year, SezimalInteger('4'), SezimalInteger('11'))

    return ordinal_date, ymd, SezimalInteger(0)


def traditional_easter_ordinal_date(year: int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction, method: int = EASTER_GREGORIAN) -> SezimalInteger:
    """
    This method was ported from the work done by GM Arts,
    on top of the algorithm by Claus Tondering, which was
    based in part on the algorithm of Ouding (1940), as
    quoted in "Explanatory Supplement to the Astronomical
    Almanac", P.  Kenneth Seidelmann, editor.

    This algorithm implements three different Easter
    calculation methods:

    1. Original calculation in Julian calendar, valid in
       dates after 326 AD
    2. Original method, with date converted to Gregorian
       calendar, valid in years 1583 to 4099
    3. Revised method, in Gregorian calendar, valid in
       years 1583 to 4099 as well

    These methods are represented by the constants:

    * ``EASTER_JULIAN   = 1``
    * ``EASTER_ORTHODOX = 2``
    * ``EASTER_WESTERN  = 3``

    The default method is method 3.

    More about the algorithm may be found at:

    `GM Arts: Easter Algorithms <http://www.gmarts.org/index.php?go=415>`_

    and

    `The Calendar FAQ: Easter <https://www.tondering.dk/claus/cal/easter.php>`_

    """

    year = SezimalInteger(year)
    year -= ISO_YEAR_DIFF

    year = int(year)

    # g - Golden year - 1
    # c - Century
    # h - (23 - Epact) mod 30
    # i - Number of days from March 21 to Paschal Full Moon
    # j - Weekday for PFM (0=Sunday, etc)
    # p - Number of days from March 21 to Sunday on or before PFM
    #     (-6 to 28 methods 1 & 3, to 56 for method 2)
    # e - Extra days to add for method 2 (converting Julian
    #     date to Gregorian date)

    y = year
    g = y % 19
    e = 0

    if method != EASTER_HEBREW:
        if method == EASTER_JULIAN_ORIGINAL or method == EASTER_JULIAN_REVISED:
            # Old method
            i = (19*g + 15) % 30
            j = (y + y//4 + i) % 7

            if method == EASTER_JULIAN_REVISED:
                # Extra dates to convert Julian to Gregorian date
                e = 10

                if y > 1600:
                    e = e + y//100 - 16 - (y//100 - 16)//4

        else:
            # New method
            c = y//100
            h = (c - c//4 - (8*c + 13)//25 + 19*g + 15) % 30
            i = h - (h//28)*(1 - (h//28)*(29//(h + 1))*((21 - g)//11))
            j = (y + y//4 + i + 2 - c + c//4) % 7


        # p can be from -6 to 56 corresponding to dates 22 March to 23 May
        # (later dates apply to method 2, although 23 May never actually occurs)
        p = i - j + e
        d = 1 + (p + 27 + (p + 6)//40) % 31
        m = 3 + (p + 26)//30

    else:
        #
        # Passover
        # code adaptade from:
        # https://webspace.science.uu.nl/~gent0113/easter/addfiles/easter.js
        #
        a = ((12 * y) + 12) % 19
        b = y % 4
        s = (5 * (1979335 - 313 * y) + (765433 * a)) / 492480 + b / 4;
        q = int(s)
        r = s - q
        c = (q + (3 * y) + (5 * b) + 1) % 7
        diff_jg = (y // 100) - (year // 400) - 2
        dmh = q + diff_jg + 92

        p = 0

        if (c == 2) or (c == 4) or (c == 6):
            p = 1  # because of Adu

        if (c == 1) and (a > 6) and (r > 1366/2160):
            p = 2  # because of Gatarad

        if (c == 0) and (a > 11) and (r > 23268/25920):
            p = 1  # because of Batu Thakpad

        dmh = dmh + p
        mh = int((dmh-62) / 30.6)
        d = int(dmh - 62 - (30.6 * mh)) + 1
        m = mh + 2

    return gregorian_year_month_day_to_ordinal_date(int(y), int(m), int(d))
