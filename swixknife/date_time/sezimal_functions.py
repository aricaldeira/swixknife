

import time as _time
import datetime as _datetime
from zoneinfo import ZoneInfo

try:
    import tzlocal
except:
    tzlocal = None

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..units.conversions import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA, UTA_TO_HOUR
from ..functions import floor, ceil

TIME_SEPARATOR = ":"

#
# Epoch
#
# Julian date -1_0521_5450.3 → -1_930_998.5_dec → -9_999-01-03_dec GREGORIAN
#
EPOCH = SezimalInteger('-2_1014_1212')  # -3_652_424_dec
EPOCH_JULIAN_DATE = Sezimal('-1_0521_5450.3')  # -1_930_998.5_dec

ISO_EPOCH = SezimalInteger('1')
ISO_EPOCH_JULIAN_DATE = Sezimal('1_0052_1320.3')  # 1_721_424.5_dec → 00-12-31_dec GREGORIAN
# ISO_YEAR_DIFF = SezimalInteger('10_0000')  # 7_776_dec
ISO_YEAR_DIFF = SezimalInteger('11_4144')  # 10_000_dec
# ISO_YEAR_DIFF = SezimalInteger('12_0000')  # 10_368_dec
# ISO_YEAR_DIFF = SezimalInteger('13_0000')  # 11_664_dec
# ISO_YEAR_DIFF = SezimalInteger('14_0000')  # 12_960_dec
# ISO_YEAR_DIFF = SezimalInteger('15_0000')  # 14_256_dec
# ISO_YEAR_DIFF = SezimalInteger('20_0000')  # 15_552_dec
ISO_HOLOCENE_YEAR_DIFF = SezimalInteger('11_4144')  # 10_000_dec


#
# For compatibility with Python’s original date and datetime,
# MAXYEAR has to be 1 year less, because:
#
# 23_2331-20-55 (19_999-12-35_dec) SEZIMAL → 10_000-01-02_dec GREGORIAN → 2_1013_5405 (3_652_061_dec) ORDINAL
# 23_2331-20-54 (19_999-12-34_dec) SEZIMAL → 10_000-01-01_dec GREGORIAN → 2_1013_5404 (3_652_060_dec) ORDINAL
#
# This is the actual maximum Python date
# 23_2331-20-53 (19_999-12-33_dec) SEZIMAL →  9_999-12-31_dec GREGORIAN → 2_1013_5403 (3_652_059_dec) ORDINAL
#
# So we use the maximum full year we can use
# 23_2330-20-44 (19_998-12-28_dec) SEZIMAL → 9_998-12-27_dec GREGORIAN → 2_1013_3550 (3_651_690_dec) ORDINAL
#
MIN_ISO_YEAR = ISO_YEAR_DIFF + SezimalInteger('1')
MAX_ISO_YEAR = ISO_YEAR_DIFF + SezimalInteger('11_4144')
MINYEAR = SezimalInteger('1')
MAXYEAR = MAX_ISO_YEAR - SezimalInteger('1')
MAXORDINAL = SezimalInteger('2_1013_3550')


CYCLE_MEAN_YEAR = Sezimal('1405') + (Sezimal('155') / Sezimal('1205'))  # 365_dec + (71_dec / 293_dec)

#
# 13_1230-01-04 SEZIMAL → 1_970-01-01_dec GREGORIAN → 2322_5243 (719_163_dec)
#
POSIX_EPOCH = SezimalInteger('2322_5243')
POSIX_JULIAN_DATE = Sezimal('1_2415_1003.3')

_LEAP_FACTOR = SezimalInteger('402')
# _LEAP_FACTOR = SezimalInteger('1005')

#
# -1 is just a placeholder, so we don’t need to worry about month number 0
#
DAYS_IN_MONTH = [
    SezimalInteger('-1'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
    SezimalInteger('44'),
    SezimalInteger('55'),
    SezimalInteger('44'),
]
DAYS_BEFORE_MONTH = [SezimalInteger('-1')]

days_before_month = SezimalInteger('0')

for days_in_month in DAYS_IN_MONTH[1:]:
    DAYS_BEFORE_MONTH.append(days_before_month)
    days_before_month += days_in_month

del days_before_month, days_in_month


def is_leap(year):
    is_leap = ((SezimalInteger('124') * year) + _LEAP_FACTOR).decimal % SezimalInteger('1205').decimal < SezimalInteger('124').decimal
    return is_leap


def _days_before_year(year):
    "year -> number of days before January 1st of year."
    year -= SezimalInteger('1')

    dby = SezimalInteger('1404').decimal * year.decimal
    weeks = (SezimalInteger('124').decimal * year.decimal) + _LEAP_FACTOR.decimal
    weeks *= SezimalInteger(1).decimal / SezimalInteger('1205').decimal
    dby += SezimalInteger('11').decimal * floor(weeks).decimal

    return dby


def _days_in_month(year, month):
    "year, month -> number of days in that month in that year."
    assert 1 <= month <= 20, month

    if month == 20 and is_leap(year):
        return SezimalInteger('55')

    return DAYS_IN_MONTH[month]


def _days_before_month(month):
    "year, month -> number of days in year preceding first day of month."
    assert 1 <= month <= 20, f'month must be in 1..20: {month}'

    return DAYS_BEFORE_MONTH[month]


def year_month_day_to_ordinal(year, month, day):
    "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
    assert 1 <= month <= 20, f'month must be in 1..20: {month}'

    year -= ISO_YEAR_DIFF

    days_in_month = _days_in_month(year, month)

    assert 1 <= day <= days_in_month, (f'day must be in 1..{days_in_month}: day')

    ordinal_date = _days_before_year(year)
    ordinal_date += _days_before_month(month)
    ordinal_date += day

    return SezimalInteger(ordinal_date)


def _first_day_year(year):
    return _days_before_year(year) + SezimalInteger('1')


def _ordinal_to_year(ordinal_date):
    year = ordinal_date.decimal - ISO_EPOCH.decimal
    year /= CYCLE_MEAN_YEAR.decimal
    year = ceil(year)
    return year


def ordinal_to_year_month_day(ordinal_date):
    #
    # First, we find the year corresponding to the ordinal date
    #
    year = _ordinal_to_year(ordinal_date)

    first_day_year = _first_day_year(year)

    #
    # We now check if the year is correct
    # The start of the year is either on the year or we must increment the year
    #
    if ordinal_date > first_day_year:
        #
        # Check if the ordinal date informed may be
        # on the leap week of December or the next year
        #
        if ordinal_date - first_day_year >= SezimalInteger('1404'):
            first_day_next_year = _first_day_year(year + SezimalInteger('1'))

            #
            # If the given ordinal date is after the next year’s first day,
            # then it is on the next year
            #
            if ordinal_date >= first_day_next_year:
                year += SezimalInteger('1')
                first_day_year = first_day_next_year

    #
    # The year estimate is too far in the future, go back 1 year
    #
    elif first_day_year > ordinal_date:
        year -= SezimalInteger('1')
        first_day_year = _first_day_year(year)

    day_in_year = SezimalInteger(ordinal_date - first_day_year + SezimalInteger('1'))
    week_in_year = SezimalInteger(ceil(day_in_year.decimal / SezimalInteger('11').decimal))
    quarter = SezimalInteger(ceil((SezimalInteger('4').decimal / SezimalInteger('125').decimal) *  week_in_year))
    day_in_quarter = SezimalInteger(day_in_year - (SezimalInteger('231') * (quarter - SezimalInteger('1'))))
    week_in_quarter = SezimalInteger(ceil(day_in_quarter.decimal / SezimalInteger('11').decimal))
    month_in_quarter = SezimalInteger(ceil((SezimalInteger('2').decimal / SezimalInteger('13').decimal) * week_in_quarter))
    month = SezimalInteger((SezimalInteger('3') * (quarter - SezimalInteger('1'))) + month_in_quarter)

    #
    # The day is in the leap week
    #
    if month == SezimalInteger('21'):
        month = SezimalInteger('20')

    day = SezimalInteger(day_in_year - _days_before_month(month))

    year += ISO_YEAR_DIFF

    return year, month, day, day_in_year, week_in_year, quarter, day_in_quarter, week_in_quarter, month_in_quarter


def check_date_fields(year, month, day):
    # if not MINYEAR <= year <= MAXYEAR:
    #     raise ValueError(f'Year must be in {MINYEAR}..{MAXYEAR}', year)

    if not 1 <= month <= 20:
        raise ValueError('Month must be in 1..20', month)

    year -= ISO_YEAR_DIFF

    days_in_month = _days_in_month(year, month)

    if not 1 <= day <= days_in_month:
        raise ValueError(f'Day must be in 1..{days_in_month} for month {year + ISO_YEAR_DIFF}-{str(month).zfill(2)}', day)

    return year, month, day


def system_time_zone():
    if tzlocal:
        return tzlocal.get_localzone_name()

    diff = int(_time.strftime('%z')) // 100

    if diff == 0:
        return 'UTC'

    if diff > 0:
        return 'Etc/GMT-' + str(diff)

    return 'Etc/GMT+' + str(diff * -1)


def date_time_to_agrima(date_time: _datetime.datetime | _datetime.time):
    total_seconds = Decimal(str(date_time.hour * 60 * 60))
    total_seconds += Decimal(str(date_time.minute * 60))
    total_seconds += Decimal(str(date_time.second))
    total_seconds += Decimal(str(date_time.microsecond / 1_000_000))
    total_agrimas = total_seconds * SECOND_TO_AGRIMA
    return total_agrimas


def timestamp_to_ordinal_date_and_agrima(timestamp: int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction, time_zone: str | ZoneInfo = None) -> Sezimal:
    if type(timestamp) in (Sezimal, SezimalInteger, SezimalFraction):
        timestamp = timestamp.decimal

    if not time_zone:
        time_zone = system_time_zone()

    if not isinstance(time_zone, ZoneInfo):
        time_zone = ZoneInfo(time_zone)

    dt = _datetime.datetime.fromtimestamp(float(timestamp), ZoneInfo('UTC')).astimezone(time_zone)
    ordinal_date = Decimal(dt.toordinal())
    agrimas = date_time_to_agrima(dt)

    # tz_offset, dst_offset = tz_agrimas_offset(time_zone, base_date=dt.date())
    #
    # agrimas += tz_offset

    return ordinal_date, agrimas


def tz_agrimas_offset(time_zone: str | ZoneInfo = 'UTC', base_date: str = None):
    if not time_zone:
        time_zone = system_time_zone()

    elif time_zone == 'UTC':
        return Sezimal('0'), Sezimal('0')

    if not isinstance(time_zone, ZoneInfo):
        time_zone = ZoneInfo(time_zone)

    if base_date:
        dt_tz = _datetime.datetime.fromisoformat(f'{base_date}T12:00:00').astimezone(time_zone)
    else:
        dt_tz = _datetime.datetime.now(time_zone)

    td = dt_tz.utcoffset()
    total_seconds = Decimal(str(td.days * 86_400))
    total_seconds += Decimal(str(td.seconds))

    total_agrimas = total_seconds * SECOND_TO_AGRIMA

    td_dst = dt_tz.dst()
    total_seconds_dst = Decimal(str(td_dst.days * 86_400))
    total_seconds_dst += Decimal(str(td_dst.seconds))

    total_agrimas_dst = total_seconds_dst * SECOND_TO_AGRIMA

    return total_agrimas, total_agrimas_dst
