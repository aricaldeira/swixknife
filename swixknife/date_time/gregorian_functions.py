

__all__ = ('gregorian_year_month_day_to_ordinal_date', 'ordinal_date_to_gregorian_year_month_day')

from decimal import Decimal

from ..sezimal import SezimalInteger

#
# Those where copied from Python’s original datetime
#

_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

_DAYS_BEFORE_MONTH = [-1]  # -1 is a placeholder for indexing purposes.

dbm = 0

for dim in _DAYS_IN_MONTH[1:]:
    _DAYS_BEFORE_MONTH.append(dbm)
    dbm += dim

del dbm, dim

def _is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def _days_before_year(year):
    "year -> number of days before January 1st of year."
    y = year - 1
    return y*365 + y//4 - y//100 + y//400

def _days_in_month(year, month):
    "year, month -> number of days in that month in that year."
    assert 1 <= month <= 12, month

    if month == 2 and _is_leap(year):
        return 29

    return _DAYS_IN_MONTH[month]

def _days_before_month(year, month):
    "year, month -> number of days in year preceding first day of month."
    assert 1 <= month <= 12, 'month must be in 1..12'

    return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))

def _ymd2ord(year, month, day):
    "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
    assert 1 <= month <= 12, 'month must be in 1..12'

    dim = _days_in_month(year, month)

    assert 1 <= day <= dim, ('day must be in 1..%d' % dim)

    return (_days_before_year(year) +
            _days_before_month(year, month) +
            day)

_DI400Y = _days_before_year(401)    # number of days in 400 years
_DI100Y = _days_before_year(101)    #    "    "   "   " 100   "
_DI4Y   = _days_before_year(5)      #    "    "   "   "   4   "

# A 4-year cycle has an extra leap day over what we'd get from pasting
# together 4 single years.
assert _DI4Y == 4 * 365 + 1

# Similarly, a 400-year cycle has an extra leap day over what we'd get from
# pasting together 4 100-year cycles.
assert _DI400Y == 4 * _DI100Y + 1

# OTOH, a 100-year cycle has one fewer leap day than we'd get from
# pasting together 25 4-year cycles.
assert _DI100Y == 25 * _DI4Y - 1

def _ord2ymd(n):
    "ordinal -> (year, month, day), considering 01-Jan-0001 as day 1."

    # n is a 1-based index, starting at 1-Jan-1.  The pattern of leap years
    # repeats exactly every 400 years.  The basic strategy is to find the
    # closest 400-year boundary at or before n, then work with the offset
    # from that boundary to n.  Life is much clearer if we subtract 1 from
    # n first -- then the values of n at 400-year boundaries are exactly
    # those divisible by _DI400Y:
    #
    #     D  M   Y            n              n-1
    #     -- --- ----        ----------     ----------------
    #     31 Dec -400        -_DI400Y       -_DI400Y -1
    #      1 Jan -399         -_DI400Y +1   -_DI400Y      400-year boundary
    #     ...
    #     30 Dec  000        -1             -2
    #     31 Dec  000         0             -1
    #      1 Jan  001         1              0            400-year boundary
    #      2 Jan  001         2              1
    #      3 Jan  001         3              2
    #     ...
    #     31 Dec  400         _DI400Y        _DI400Y -1
    #      1 Jan  401         _DI400Y +1     _DI400Y      400-year boundary
    n -= 1
    n400, n = divmod(n, _DI400Y)
    year = n400 * 400 + 1   # ..., -399, 1, 401, ...

    # Now n is the (non-negative) offset, in days, from January 1 of year, to
    # the desired date.  Now compute how many 100-year cycles precede n.
    # Note that it's possible for n100 to equal 4!  In that case 4 full
    # 100-year cycles precede the desired day, which implies the desired
    # day is December 31 at the end of a 400-year cycle.
    n100, n = divmod(n, _DI100Y)

    # Now compute how many 4-year cycles precede it.
    n4, n = divmod(n, _DI4Y)

    # And now how many single years.  Again n1 can be 4, and again meaning
    # that the desired day is December 31 at the end of the 4-year cycle.
    n1, n = divmod(n, 365)

    year += n100 * 100 + n4 * 4 + n1

    if n1 == 4 or n100 == 4:
        assert n == 0
        return year-1, 12, 31

    # Now the year is correct, and n is the offset from January 1.  We find
    # the month via an estimate that's either exact or one too large.
    leapyear = n1 == 3 and (n4 != 24 or n100 == 3)

    assert leapyear == _is_leap(year)

    month = (n + 50) >> 5

    preceding = _DAYS_BEFORE_MONTH[month] + (month > 2 and leapyear)

    if preceding > n:  # estimate is too large
        month -= 1
        preceding -= _DAYS_IN_MONTH[month] + (month == 2 and leapyear)

    n -= preceding

    assert 0 <= n < _days_in_month(year, month)

    # Now the year and month are correct, and n is the offset from the
    # start of that month:  we're done!
    return year, month, n+1


def ordinal_date_to_gregorian_year_month_day(ordinal_date):
    if type(ordinal_date).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
        ordinal_date = int(ordinal_date.decimal)

    year, month, day = _ord2ymd(ordinal_date)

    # year = SezimalInteger(Decimal(year))
    # month = SezimalInteger(Decimal(month))
    # day = SezimalInteger(Decimal(day))

    return year, month, day


def gregorian_year_month_day_to_ordinal_date(year, month, day):
    # if type(year).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
    #     year = int(year.decimal)
    #
    # if type(month).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
    #     month = int(month.decimal)
    #
    # if type(day).__name__ in ('Sezimal', 'SezimalInteger', 'SezimalFraction'):
    #     day = int(day.decimal)

    ordinal_date = _ymd2ord(year, month, day)

    ordinal_date = SezimalInteger(Decimal(ordinal_date))

    return ordinal_date


def gregorian_year_to_iso_first_monday_ordinal_date(year):
    first_monday = gregorian_year_month_day_to_ordinal_date(year, 1, 1).decimal
    first_weekday = (first_monday + 6) % 7
    first_monday -= first_weekday

    if first_weekday > 3:
        first_monday += 7

    return first_monday


def gregorian_year_month_day_to_iso_year_week_day(year, month, day):
    first_monday = gregorian_year_to_iso_first_monday_ordinal_date(year)
    ordinal_date = gregorian_year_month_day_to_ordinal_date(year, month, day).decimal

    week, day = divmod(ordinal_date - first_monday, 7)

    if week < 0:
        year -= 1
        first_monday = gregorian_year_to_iso_first_monday_ordinal_date(year)
        week, day = divmod(ordinal_date - first_monday, 7)

    elif week >= 52:
        if ordinal_date >= gregorian_year_to_iso_first_monday_ordinal_date(year + 1):
            year += 1
            week = 0

    week += 1
    day += 1

    return year, int(week), int(day)
