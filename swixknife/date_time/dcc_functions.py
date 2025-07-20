#
# DAY COUNT CALENDAR - DCC
#
# Year starts roughly at the week of the March Equinox
#

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction


#
# The leap epoch is corresponding to dates:
#
# DCC+212_014-00-00 00:00:00:00 NT
#
# ISO+1738-03-20 03:13:45 UTC
# SYM+212_014-03-30 04:50:21:30 UTC
# rata die 21_333_305.045_021_30 634_505.134_548_6..1_d
# julian day 122_255_025.345_021_30 = 2_355_929.634_548_6..1_d
#
# LEAP_EPOCH_TIME = Sezimal('21_333_305.045_021_30')  # 634_505.134_548_6..1_d
# LEAP_EPOCH_TIME = Sezimal('21_333_305.1')  # 634_505.1..6_d
LEAP_EPOCH_TIME = Sezimal('21_333_305')  # 634_505.134_548_6..1_d
LEAP_EPOCH = Sezimal('21_333_305')  # 634_505.134_548_6..1_d

#
# The Holocene epoch adjusts the year counting
#
HOLOCENE_EPOCH = SezimalInteger('212_014')  # 17_506_d

#
# Considering the Holocene epoch,
# the actual epoch of the calendar is:
#
# DCC+000_000-00-00
#
# ISO −15_552-03-25
# SYM−000_000-03-25
# rata die -321_430_432 -5_680_532_d
# julian day -220_505_111.3 = -3_959_107.5_d
#

# CYCLE_YEAR_AJUST = SezimalInteger('200_000')  # 15_552_d
# CYCLE_FACTOR = SezimalInteger('420')  # 156_d
CYCLE_FACTOR = SezimalInteger('504')  # 184_d

YEARS_IN_FULL_CYCLE = SezimalInteger('1205')  # 293_d
SHORT_YEARS_IN_FULL_CYCLE = SezimalInteger('101')  # 37_d
DAYS_IN_FULL_CYCLE = SezimalInteger('2_143_240')  # 107_016_d

YEARS_IN_SUB_CYCLE = SezimalInteger('235')  # 95_d
DAYS_IN_SUB_CYCLE = SezimalInteger('424_350')  # 34_698_d

YEARS_IN_CYCLE = SezimalInteger('12')  # 8_d
DAYS_IN_CYCLE = SezimalInteger('21_310')  # 2922_d

DAYS_IN_LONG_YEAR = SezimalInteger('1410')  # 366_d
DAYS_IN_SHORT_YEAR = SezimalInteger('1400')  # 360_d


def is_unleap(year: SezimalInteger) -> bool:
    is_unleap = ((
        (SHORT_YEARS_IN_FULL_CYCLE * year)
        + CYCLE_FACTOR
        ) % YEARS_IN_FULL_CYCLE
    ) < SHORT_YEARS_IN_FULL_CYCLE

    return is_unleap


def is_long_year(year: SezimalInteger) -> bool:
    return not is_unleap(year)


def is_short_year(year: SezimalInteger) -> bool:
    return is_unleap(year)


def _ordinal_to_year(ordinal_date: SezimalInteger | Sezimal) -> SezimalInteger:
    if type(ordinal_date) == SezimalInteger:
        ordinal_date -= LEAP_EPOCH
    else:
        ordinal_date -= LEAP_EPOCH_TIME

    full_cycles = ordinal_date // DAYS_IN_FULL_CYCLE

    if ordinal_date < 0:
        full_cycles = abs(full_cycles - 1)
        ordinal_date += full_cycles * DAYS_IN_FULL_CYCLE
        year = full_cycles * YEARS_IN_FULL_CYCLE * -1
    else:
        ordinal_date -= full_cycles * DAYS_IN_FULL_CYCLE
        year = full_cycles * YEARS_IN_FULL_CYCLE

    sub_cycles = ordinal_date // DAYS_IN_SUB_CYCLE
    ordinal_date -= sub_cycles * DAYS_IN_SUB_CYCLE
    year += sub_cycles * YEARS_IN_SUB_CYCLE

    cycles = ordinal_date // DAYS_IN_CYCLE
    ordinal_date -= cycles * DAYS_IN_CYCLE
    year += cycles * YEARS_IN_CYCLE

    #
    # The first year of each cycle is always short
    #
    if ordinal_date >= DAYS_IN_SHORT_YEAR:
        year += 1
        ordinal_date -= DAYS_IN_SHORT_YEAR

    #
    # The remaining years are always long
    #
    if ordinal_date >= DAYS_IN_LONG_YEAR:
        long_years = ordinal_date // DAYS_IN_LONG_YEAR
        ordinal_date -= long_years * DAYS_IN_LONG_YEAR
        year += long_years

    return SezimalInteger(year + HOLOCENE_EPOCH)


def _year_to_ordinal_first_day(year) -> SezimalInteger | Sezimal:
    year -= HOLOCENE_EPOCH

    full_cycles = year // YEARS_IN_FULL_CYCLE

    if year < 0:
        full_cycles = abs(full_cycles - 1)
        ordinal_date = full_cycles * DAYS_IN_FULL_CYCLE * -1
        year += full_cycles * YEARS_IN_FULL_CYCLE
    else:
        ordinal_date = full_cycles * DAYS_IN_FULL_CYCLE
        year -= full_cycles * YEARS_IN_FULL_CYCLE

    sub_cycles = year // YEARS_IN_SUB_CYCLE
    ordinal_date += sub_cycles * DAYS_IN_SUB_CYCLE
    year -= sub_cycles * YEARS_IN_SUB_CYCLE

    cycles = year // YEARS_IN_CYCLE
    year -= cycles * YEARS_IN_CYCLE
    ordinal_date += cycles * DAYS_IN_CYCLE

    #
    # The first year of the cycle is always short
    #
    if year >= 1:
        ordinal_date += DAYS_IN_SHORT_YEAR
        year -= 1

    ordinal_date += year * DAYS_IN_LONG_YEAR

    ordinal_date += LEAP_EPOCH_TIME

    # return SezimalInteger(ordinal_date)
    return Sezimal(ordinal_date)


def ordinal_date_to_year_month_day(ordinal_date: SezimalInteger | Sezimal) -> (SezimalInteger, SezimalInteger, SezimalInteger, SezimalInteger, SezimalInteger, SezimalInteger):
    #
    # First, we find the year corresponding to the ordinal date
    #
    year = _ordinal_to_year(ordinal_date)

    #
    # We remove all days prior to the start of the year
    #
    ordinal_date -= _year_to_ordinal_first_day(year)

    day_in_year = SezimalInteger(ordinal_date)
    week_in_year = day_in_year // 10

    month = day_in_year // 100
    day = day_in_year % 100

    day_in_week = day % 10

    return year, month, day, day_in_year, week_in_year, day_in_week


def year_month_day_to_ordinal_date(year, month, day) -> SezimalInteger | Sezimal:
    ordinal_date = _year_to_ordinal_first_day(year)
    ordinal_date += month * 100
    ordinal_date += day
    # return SezimalInteger(ordinal_date)
    return Sezimal(ordinal_date)


def year_week_weekday_to_ordinal_date(year, week, weekday) -> SezimalInteger:
    ordinal_date = _year_to_ordinal_first_day(year)
    ordinal_date += week * 10
    ordinal_date += weekday
    return SezimalInteger(ordinal_date)


def mean_tropical_year(date):
    century = date.julian_day - Sezimal('124_313_424.3')
    century /= Sezimal('441_033')
    century = SezimalFraction(century)
    mty = SezimalFraction('1_300_354_300_031_234_215 / 520_000_000_000_000')
    mty -= century * SezimalFraction('142_003_005_341 / 1_000_000_000_000_000_000')
    mty -= (century ** 2) * SezimalFraction('310_131 / 200_000_000_000_000_000')
    mty += (century ** 3) * SezimalFraction('1311 / 2_400_000_000_000_000')
    return mty
