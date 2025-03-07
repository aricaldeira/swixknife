

import time as _time
import datetime as _datetime
from zoneinfo import ZoneInfo
import re


try:
    import tzlocal
except:
    tzlocal = None

from decimal import Decimal

from ..base import sezimal_context
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..units import decimal_to_sezimal_unit
from ..functions import floor, ceil
from .gregorian_functions import gregorian_year_month_day_to_ordinal_date


VALID_DATE_STRING = re.compile(r'^[+-−]?[0-5]{6}-[0-5]{2}-[0-5]{2}$|^[+-−]?[0-5]{3}_[0-5]{3}-[0-5]{2}-[0-5]{2}$|^[+-−]?[0-5]{2}_[0-5]{4}-[0-5]{2}-[0-5]{2}$')
VALID_TIME_STRING = re.compile(r'^[0-5]{2}:[0-5]{2}:[0-5]{2}(\.[0-5]{0,12})?( .*)?$')
VALID_PARTIAL_TIME_STRING = re.compile(r'^[0-5]{2}:[0-5]{2}$')
VALID_DATE_TIME_STRING = re.compile(r'^[+-−]?[0-5]{6}-[0-5]{2}-[0-5]{2}[ T][0-5]{2}:[0-5]{2}:[0-5]{2}(\.[0-5]{0,12})?( .*)?$|^[+-−]?[0-5]{3}_[0-5]{3}-[0-5]{2}-[0-5]{2} [0-5]{2}:[0-5]{2}:[0-5]{2}(\.[0-5]{0,12})?( .*)?$|^[+-−]?[0-5]{2}_[0-5]{4}-[0-5]{2}-[0-5]{2}[ T][0-5]{2}:[0-5]{2}:[0-5]{2}(\.[0-5]{0,12})?( .*)?$')
VALID_DATE_PARTIAL_TIME_STRING = re.compile(r'^[+-−]?[0-5]{6}-[0-5]{2}-[0-5]{2}[ T][0-5]{2}:[0-5]{2}$|^[+-−]?[0-5]{3}_[0-5]{3}-[0-5]{2}-[0-5]{2}[ T][0-5]{2}:[0-5]{2}$|^[+-−]?[0-5]{2}_[0-5]{4}-[0-5]{2}-[0-5]{2}[ T][0-5]{2}:[0-5]{2}$')

#
# Some expressions to validate holidays and events
# using other calendars
#
VALID_MONTH_DAY_STRING = re.compile(r'^[0-5]{2}-[0-5]{2}$')
VALID_DATE_OTHER_CALENDAR_STRING = re.compile(r'^SEZ[+-−]?[0-5]{6}-[0-5]{2}-[0-5]{2}((\-|\+|\±)(MON|TUE|WED|THU|FRI|SAT|SUN)(\_[0-5]{1,2})?)?$|^SEZ[+-−]?[0-5]{3}_[0-5]{3}-[0-5]{2}-[0-5]{2}((\-|\+|\±)(MON|TUE|WED|THU|FRI|SAT|SUN)(\_[0-5]{1,2})?)?$|^SEZ[+-−]?[0-5]{2}_[0-5]{4}-[0-5]{2}-[0-5]{2}((\-|\+|\±)(MON|TUE|WED|THU|FRI|SAT|SUN)(\_[0-5]{1,2})?)?$|^(SYM|ISO|GRE|JUL|HEB|JEW|ISR|HIJ|IRN|IND|LUN|CHR|ORT)[+-−]?[0-9]{4,5}-[0-9]{2}-[0-9]{2}((\-|\+|\±)(MON|TUE|WED|THU|FRI|SAT|SUN)(\_[0-9]{1,2})?)?$')
VALID_MONTH_DAY_OTHER_CALENDAR_STRING = re.compile(r'^SEZ[+-−][0-5]{2}-[0-5]{2}((\-|\+|\±)(MON|TUE|WED|THU|FRI|SAT|SUN)(\_[0-5]{1,2})?)?$|^(SYM|ISO|GRE|JUL|HEB|JEW|ISR|HIJ|IRN|IND|LUN|CHR|ORT)[+-−][0-9]{2}-[0-9]{2}((\-|\+|\±)(MON|TUE|WED|THU|FRI|SAT|SUN)(\_[0-9]{1,2})?)?$')
VALID_EASTER_DATE_STRING = re.compile(r'(SEZ[+-−])?(EASTER|PESACH|PASCHA|PASKHA)([+-][0-5]{1,4})?|((SYM|ISO|GRE|JUL|HEB|JEW|CHR|ORT)[+-−])?(EASTER|PESACH|PASCHA|PASKHA)([+-][0-9]{1,4})?')

#
# ISO Epoch
#
ISO_EPOCH = SezimalInteger('1')
ISO_EPOCH_JULIAN_DAY = Sezimal('100_521_320.3')  # 1_721_424.5_dec → 00-12-31_dec GREGORIAN

#
# Using the same Epoch as the ISO calendar,
# the implementation matches the Symmetry454 Calendar
# as created by Dr. Irv Bromberg
#
# EPOCH = ISO_EPOCH
# EPOCH_JULIAN_DAY = ISO_EPOCH_JULIAN_DAY
# ISO_YEAR_DIFF = 0
# ISO_HOLOCENE_YEAR_DIFF = 0

#
# Holocene Epoch
#
# Julian day -105_215_450.3 → -1_930_998.5_dec → -9_999-01-02_dec ISO
#
# The one day difference (actually it should be -9_999-01-01_dec ISO)
# compensates the fact that the ordinal date / Rada Die starts
# with 1, not zero
#
# EPOCH = SezimalInteger('-210_141_212')  # -3_652_424_dec
# EPOCH_JULIAN_DAY = Sezimal('-105_215_450.3')  # -1_930_998.5_dec
# ISO_YEAR_DIFF = SezimalInteger('114_144')  # 10_000_dec
# ISO_HOLOCENE_YEAR_DIFF = SezimalInteger('114_144')  # 10_000_dec

#
# Sezimal Holocene Epoch
#
# Julian day -220_511_131.3 → -3_959_551.5_dec → -15_553-01-06_dec ISO
#
# The one day difference (actually it should be -15_553-01-05_dec ISO)
# compensates the fact that the ordinal date / Rada Die starts
# with 1, not zero
#
EPOCH = SezimalInteger('-321_425_235')  # -5_680_976_dec
EPOCH_JULIAN_DAY = Sezimal('-220_503_514.3')  # -3_959_550.5_dec
ISO_YEAR_DIFF = SezimalInteger('200_000')  # 15_552_dec
ISO_HOLOCENE_YEAR_DIFF = SezimalInteger('114_144')  # 10_000_dec


#
# The epoch defined on the comments just below
# lines Sezimal year 0 with the year, on the Holocene Era,
# where the Perihelion coincides with the Northern Hemisphere
# Summer Solstice
#
# EPOCH = SezimalInteger('-202_510_230')  # -3_492_810_dec
# EPOCH_JULIAN_DAY = Sezimal('-101_544_505.3')  # -1_771_385.5_dec
# ISO_YEAR_DIFF = SezimalInteger('112_135')  # 9_563_dec
# ISO_HOLOCENE_YEAR_DIFF = SezimalInteger('112_135')  # 9_563_dec
#
# The epoch defined on the comments just below
# lines Sezimal year __1__ with the year, on the Holocene Era,
# where the Perihelion coincides with the Northern Hemisphere
# Summer Solstice
#
# EPOCH = SezimalInteger('-202_512_034')  # -3_493_174_dec
# EPOCH_JULIAN_DAY = Sezimal('-101_550_313.3')  # -1_771_749.5_dec
# ISO_YEAR_DIFF = SezimalInteger('112_134')  # 9_562_dec
# ISO_HOLOCENE_YEAR_DIFF = SezimalInteger('112_134')  # 9_562_dec
#

#
# For compatibility with Python’s original date and datetime,
# MAXYEAR has to be 1 year less, because:
#
# 314_143-20-55 (25_551-12-35_dec) SEZIMAL → 10_000-01-02_dec GREGORIAN → 210_135_405 (3_652_061_dec) ORDINAL
# 314_143-20-54 (25_551-12-34_dec) SEZIMAL → 10_000-01-01_dec GREGORIAN → 210_135_404 (3_652_060_dec) ORDINAL
#
# This is the actual maximum Python date
# 314_143-20-53 (25_551-12-33_dec) SEZIMAL →  9_999-12-31_dec GREGORIAN → 210_135_403 (3_652_059_dec) ORDINAL
#
# So we use the maximum full year we can use
# 314_142-20-44 (25_550-12-28_dec) SEZIMAL → 9_998-12-27_dec GREGORIAN → 210_133_550 (3_651_690_dec) ORDINAL
#
MIN_ISO_YEAR = ISO_YEAR_DIFF + SezimalInteger('1')
MAX_ISO_YEAR = SezimalInteger('232_332')
MINYEAR = SezimalInteger('1')
MAXYEAR = MAX_ISO_YEAR - SezimalInteger('1')
MAXORDINAL = SezimalInteger('210_133_550')


CYCLE_MEAN_YEAR = Sezimal('1_405') + (Sezimal('155') / Sezimal('1_205'))  # 365_dec + (71_dec / 293_dec)

#
# 131_230-01-04 SEZIMAL → 1_970-01-01_dec GREGORIAN → 23_225_243 (719_163_dec)
#
POSIX_EPOCH = SezimalInteger('23_225_243')
POSIX_JULIAN_DATE = Sezimal('124_151_003.3')

_LEAP_FACTOR = SezimalInteger('402')  # 146_dec
# _LEAP_FACTOR = SezimalInteger('1_005')  # 221_dec

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
    if year <= 0:
        year = abs(year) + 1

    leap = year
    leap *= SezimalInteger('124')  # 52_dec
    leap += _LEAP_FACTOR  # 146_dec or 221_dec, see prior constant definition

    #
    # The modulo is much faster using Decimal
    #
    leap = leap.decimal
    leap %= SezimalInteger('1_205').decimal  # 293_dec

    is_leap = leap < SezimalInteger('124').decimal  # 52_dec

    return is_leap


def _days_before_year(year):
    "year -> number of days before January 1st of year."
    year -= SezimalInteger('1')

    dby = SezimalInteger('1_404').decimal * year.decimal
    weeks = (SezimalInteger('124').decimal * year.decimal) + _LEAP_FACTOR.decimal
    weeks *= SezimalInteger(1).decimal / SezimalInteger('1_205').decimal
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

    assert 1 <= day <= days_in_month, f'day must be in 1..{days_in_month}: {day}, month {month}, year {year + ISO_YEAR_DIFF}'

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
        if ordinal_date - first_day_year >= SezimalInteger('1_404'):
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
    total_seconds = Decimal(str(date_time.hour)) * 60 * 60
    total_seconds += Decimal(str(date_time.minute)) * 60
    total_seconds += Decimal(str(date_time.second))
    total_seconds += Decimal(str(date_time.microsecond)) / 1_000_000
    total_agrimas = decimal_to_sezimal_unit(total_seconds, 's', 'agm')
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


def tz_agrimas_offset(time_zone: str | ZoneInfo = 'UTC', base_gregorian_date: str | _datetime.datetime | _datetime.date = None):
    if not time_zone:
        time_zone = system_time_zone()

    elif time_zone == 'UTC':
        return Sezimal('0'), Sezimal('0')

    if not isinstance(time_zone, ZoneInfo):
        time_zone = ZoneInfo(time_zone)

    if base_gregorian_date is not None:
        dt_tz = _datetime.datetime.fromisoformat(f'{base_gregorian_date}T12:00:00').astimezone(time_zone)
    else:
        dt_tz = _datetime.datetime.now(time_zone)

    td = dt_tz.utcoffset()
    total_seconds = Decimal(str(td.days * 86_400))
    total_seconds += Decimal(str(td.seconds))

    total_agrimas = decimal_to_sezimal_unit(total_seconds, 's', 'agm')

    td_dst = dt_tz.dst()
    total_seconds_dst = Decimal(str(td_dst.days * 86_400))
    total_seconds_dst += Decimal(str(td_dst.seconds))

    total_agrimas_dst = decimal_to_sezimal_unit(total_seconds_dst, 's', 'agm')

    return total_agrimas, total_agrimas_dst


def tz_days_offset(time_zone: str | ZoneInfo = 'UTC', base_gregorian_date: str | _datetime.datetime | _datetime.date = None):
    total_agrimas, total_agrimas_dst = tz_agrimas_offset(time_zone, base_gregorian_date)

    return total_agrimas / 1_000_000, total_agrimas_dst / 1_000_000


def mars_sol(julian_day: Sezimal) -> Sezimal:
    #
    # Ref. https://en.wikipedia.org/wiki/Timekeeping_on_Mars#Mars_Sol_Date
    #
    # MARS_SOL_EPOCH = 2_405_522.002_877_9_dec
    # This is 130_550-01-01 30:03:12.520_354_244_205(014_402_545_442_033_201_055_341_404_131)
    # Equivalent to Gregorian/ISO 1873-12-29 12:03:36.466559
    #
    # MARS_SOL_EPOCH = Sezimal('123_320_402.000_312_520_354_244_205_014_402_545_442_033_201_055_341_404_131')
    # MARS_SOL_EPOCH = Sezimal('123_320_402.000_312_520_354_244_205_014_402_545_442_033_201_055_341_404_131')
    MARS_SOL_EPOCH = SezimalFraction('41_325_224_024_251_343 / 255_100_052')

    #
    # Julian day 131_315-01-01 30:00:00 = 2000-01-01 12:00:00_dec
    #
    JULIAN_DATE_131_315 = Sezimal('124_313_425')

    #
    # 37_dec seconds + 32.184_dec seconds
    # in 86_400_dec seconds in a day
    #
    # TAI_UTC_OFFSET = (Decimal('37') + Decimal('32.184')) / Decimal('86_400')
    TAI_UTC_OFFSET = SezimalFraction('5001 / 44_534_000')

    #
    # Length of Mars sol in shaditibodas = 1_005_534_344_243_221_121 ~ 88_775.244_dec seconds
    # Lenght of Earth day in shaditibodas = 1_000_000_000_122_215_525 ~ 86_400.002_dec seconds
    #
    # MARS_SOL_IN_DAYS = SezimalFraction('1_005_534_344_243_221_121', '1_000_000_000_122_215_525')
    # MARS_SOL_IN_DAYS = Sezimal(Decimal('1.027_491_252'))
    MARS_SOL_IN_DAYS = SezimalFraction('41_253_401_553 / 40_450_211_224')

    #
    # Formula from:
    # http://marsclock.com/
    #
    julian_day = SezimalFraction(julian_day) + TAI_UTC_OFFSET - JULIAN_DATE_131_315
    # sol = julian_day - SezimalFraction(4.3)
    sol = julian_day - SezimalFraction('13 / 2')
    sol /= MARS_SOL_IN_DAYS
    sol += Sezimal('543_220')  # 44_796_dec
    # sol -= Decimal('0.000_96')  # adjustment from Mars24
    # sol -= SezimalFraction('3 / 22_245')  # adjustment from Mars24

    #
    # For reference:
    # 1 Mars sol = SezimalFraction('25_341_305 / 25_051_412') Earth day
    # 1 sol = 1.005_534_344_243_221_121 day
    #

    return sol

#
# Leap seconds to TAI “time zone”
# Date in Python ordinal date, seconds to add
#
sezimal_context.use_ultra_precision()

_TAI_LEAP_SECONDS = {
    736_330: Sezimal('31.5..514_02'),     # 213200-20-44 - ISO-2017-01-01 - 37 s
    735_780: Sezimal('31.2..35_01'),      # 213155-11-03 - ISO-2015-07-01 - 36 s
    734_685: Sezimal('30.5..2'),          # 213152-10-44 - ISO-2012-07-01 - 35 s
    733_408: Sezimal('30..205_43'),       # 213145-01-04 - ISO-2009-01-01 - 34 s
    732_312: Sezimal('25.4..530_41'),     # 213141-20-44 - ISO-2006-01-01 - 33 s
    729_755: Sezimal('25..140_25'),       # 213130-20-53 - ISO-1999-01-01 - 32 s
    729_206: Sezimal('24.4..235_01'),     # 213125-11-02 - ISO-1997-07-01 - 31 s
    728_659: Sezimal('24..1'),            # 213124-01-01 - ISO-1996-01-01 - 30 s
    728_110: Sezimal('23.3..543_20...'),  # 213122-10-42 - ISO-1994-07-01 - 29 s
    727_745: Sezimal('23..041_53'),       # 213121-10-41 - ISO-1993-07-01 - 28 s
    727_380: Sezimal('22.3..251_40...'),  # 213120-11-03 - ISO-1992-07-01 - 27 s
    726_833: Sezimal('22..012_35'),       # 213115-01-02 - ISO-1991-01-01 - 26 s
    726_468: Sezimal('21.3'),             # 213114-01-01 - ISO-1990-01-01 - 25 s
    725_737: Sezimal('20..543_20'),       # 213111-20-53 - ISO-1988-01-01 - 24 s
    724_823: Sezimal('20.2..304_15'),     # 213105-11-01 - ISO-1985-07-01 - 23 s
    724_092: Sezimal('15.5..140_25'),     # 213103-10-42 - ISO-1983-07-01 - 22 s
    723_727: Sezimal('15.2..012_35'),     # 213102-10-41 - ISO-1982-07-01 - 21 s
    723_362: Sezimal('14..4'),            # 213101-11-03 - ISO-1981-07-01 - 20 s
    722_815: Sezimal('14.1..320_54'),     # 213100-01-02 - ISO-1980-01-01 - 19 s
    722_450: Sezimal('13..415_30...'),    # 213055-01-01 - ISO-1979-01-01 - 18 s
    722_085: Sezimal('13.1..025_14'),     # 213053-20-44 - ISO-1978-01-01 - 17 s
    721_720: Sezimal('12..350_12'),       # 213052-20-43 - ISO-1977-01-01 - 16 s
    721_354: Sezimal('12.0..3'),          # 213051-20-52 - ISO-1976-01-01 - 15 s
    720_989: Sezimal('11..320_54'),       # 213051-01-03 - ISO-1975-01-01 - 14 s
    720_624: Sezimal('11.0..041_53'),     # 213050-01-02 - ISO-1974-01-01 - 13 s
    720_259: Sezimal('10..251_40...'),    # 213045-01-01 - ISO-1973-01-01 - 12 s
    720_075:  Sezimal('5.5..350_12'),     # 213044-10-43 - ISO-1972-07-01 - 11 s
    719_893:  Sezimal('5..2'),            # 213043-20-43 - ISO-1972-01-01 - 10 s
}

sezimal_context.back_to_regular_precision()


def _tai_offset(base_gregorian_date: _datetime.datetime | _datetime.date) -> SezimalInteger:
    ordinal_date = base_gregorian_date.toordinal()

    for od in _TAI_LEAP_SECONDS:
        if ordinal_date >= od:
            return _TAI_LEAP_SECONDS[od], Sezimal(0)

    return Sezimal(0), Sezimal(0)
