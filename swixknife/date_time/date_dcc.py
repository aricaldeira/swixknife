
from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from .dcc_functions import \
    ordinal_date_to_year_month_day, \
    year_month_day_to_ordinal_date, \
    is_leap, is_long_year, is_short_year


from . import date


@classmethod
def from_dcc(cls, year: SezimalInteger, month: SezimalInteger, day: SezimalInteger) -> date.SezimalDate:
    return cls.from_ordinal_date(year_month_day_to_ordinal_date(year, month, day))

date.SezimalDate.from_dcc = from_dcc


@property
def dcc_date(self) -> (SezimalInteger, SezimalInteger, SezimalInteger):
    return self.dcc_year, self.dcc_month, self.dcc_day

date.SezimalDate.dcc_date = dcc_date


@property
def dcc_year(self) -> SezimalInteger:
    return self._dcc_date[0]

date.SezimalDate.dcc_year = dcc_year

@property
def dcc_month(self) -> SezimalInteger:
    return self._dcc_date[1]

date.SezimalDate.dcc_month = dcc_month


@property
def dcc_week(self) -> SezimalInteger:
    return self._dcc_date[2] // 10

date.SezimalDate.dcc_week = dcc_week


@property
def dcc_day(self) -> SezimalInteger:
    return self._dcc_date[2]

date.SezimalDate.dcc_day = dcc_day


@property
def dcc_day_in_year(self) -> SezimalInteger:
    return self._dcc_date[3]

date.SezimalDate.dcc_day_in_year = dcc_day_in_year


@property
def dcc_week_in_year(self) -> SezimalInteger:
    return self._dcc_date[4]

date.SezimalDate.dcc_week_in_year = dcc_week_in_year


@property
def dcc_weekday(self) -> SezimalInteger:
    return self._dcc_date[5]

date.SezimalDate.dcc_weekday = dcc_weekday


@property
def dcc_is_short_year(self) -> bool:
    return is_leap(self.dcc_year)

date.SezimalDate.dcc_is_short_year = dcc_is_short_year


@property
def dcc_is_long_year(self) -> bool:
    return not self.dcc_is_short_year

date.SezimalDate.dcc_is_long_year = dcc_is_long_year


@property
def dcc_term(self) -> SezimalInteger:
    if self.dcc_month == 14:
        return SezimalInteger(4)

    return self.dcc_month // 2

date.SezimalDate.dcc_term = dcc_term


@property
def dcc_day_in_term(self) -> SezimalInteger:
    return self.dcc_day_in_year - (self.dcc_term * 200)

date.SezimalDate.dcc_day_in_term = dcc_day_in_term


@property
def dcc_week_in_term(self) -> SezimalInteger:
    return self.dcc_week_in_year - (self.dcc_term * 20)

date.SezimalDate.dcc_week_in_term = dcc_week_in_term


@property
def dcc_total_days_in_year(self):
    if self.dcc_is_long_year:
        return SezimalInteger(1405)

    return SezimalInteger(1355)

date.SezimalDate.dcc_total_days_in_year = dcc_total_days_in_year


@property
def dcc_total_days_in_term(self):
    if self.dcc_is_long_year and self.dcc_term == 4:
        return SezimalInteger(205)

    return SezimalInteger(155)

date.SezimalDate.dcc_total_days_in_term = dcc_total_days_in_term


@property
def dcc_total_days_in_month(self):
    if self.dcc_month == 14:
        return SezimalInteger(5)

    return SezimalInteger(55)

date.SezimalDate.dcc_total_days_in_month = dcc_total_days_in_month


@property
def dcc_total_days_in_week(self):
    return SezimalInteger(5)

date.SezimalDate.dcc_total_days_in_week = dcc_total_days_in_week


@property
def dcc_total_weeks_in_year(self):
    if self.dcc_is_long_year:
        return SezimalInteger(140)

    return SezimalInteger(135)

date.SezimalDate.dcc_total_weeks_in_year = dcc_total_weeks_in_year


@property
def dcc_total_weeks_in_term(self):
    if self.dcc_is_long_year and self.dcc_term == 4:
        return SezimalInteger(20)

    return SezimalInteger(15)

date.SezimalDate.dcc_total_weeks_in_term = dcc_total_weeks_in_term


def dcc_total_weeks_in_month(self):
    if self.dcc_month == 14:
        return SezimalInteger(0)

    return SezimalInteger(5)

date.SezimalDate.dcc_total_weeks_in_month = dcc_total_weeks_in_month


@property
def dcc_total_months_in_year(self):
    if self.dcc_is_long_year:
        return SezimalInteger(14)

    return SezimalInteger(13)

date.SezimalDate.dcc_total_months_in_year = dcc_total_months_in_year


@property
def dcc_total_months_in_term(self):
    if self.dcc_is_long_year and self.dcc_term == 4:
        return SezimalInteger(2)

    return SezimalInteger(1)

date.SezimalDate.dcc_total_months_in_term = dcc_total_months_in_term


@property
def dcc_total_terms_in_year(self):
    return SezimalInteger(5)

date.SezimalDate.dcc_total_terms_in_year = dcc_total_terms_in_year


@property
def dcc_week_proportion_ellapsed(self) -> Sezimal:
    return self.dcc_weekday / 5

date.SezimalDate.dcc_week_proportion_ellapsed = dcc_week_proportion_ellapsed


@property
def dcc_month_proportion_ellapsed(self) -> Sezimal:
    return self.dcc_day / self.dcc_total_days_in_month

date.SezimalDate.dcc_month_proportion_ellapsed = dcc_month_proportion_ellapsed


@property
def dcc_term_proportion_ellapsed(self) -> Sezimal:
    return self.dcc_day_in_term / self.dcc_total_days_in_term

date.SezimalDate.dcc_term_proportion_ellapsed = dcc_term_proportion_ellapsed


@property
def dcc_year_proportion_ellapsed(self) -> Sezimal:
    return self.dcc_day_in_year / self.dcc_total_days_in_year

date.SezimalDate.dcc_year_proportion_ellapsed = dcc_year_proportion_ellapsed


def dcc_previous(self,
    days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    terms: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
) -> date.SezimalDate:
    res = self

    if not days:
        days = SezimalInteger(0)

    if weeks:
        days += weeks * SezimalInteger(10)

    if days:
        res = res.from_days(res.as_days - days)

    months = SezimalInteger(months or 0)

    if terms:
        months += terms * SezimalInteger(2)

    if months:
        year = res.dcc_year
        month = res.dcc_month - months

        #
        # Advances months considering long and short years
        #
        while month < 0:
            if is_long_year(year - 1):
                month += 15
            else:
                month += 14

            year -= 1

        #
        # Deals with month 14 having only 10 days
        #
        if month == 14 and res.dcc_day > 5:
            day = res.dcc_day % 10
        else:
            day = res.dcc_day

        res = res.from_dcc(year, month, day)

    if years:
        #
        # Deals with short years and month 14
        #
        if is_short_year(res.dcc_year - years) and res.dcc_month == 14:
            month = 13
        else:
            month = res.dcc_month

        day = res.dcc_day
        year = res.dcc_year - years
        res = res.from_dcc(year, month, day)

    return res

date.SezimalDate.dcc_previous = dcc_previous


def dcc_next(self,
    days: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    weeks: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    months: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    terms: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    years: str | int | float | Decimal | Sezimal | SezimalInteger = None,
) -> date.SezimalDate:
    res = self

    if not days:
        days = SezimalInteger(0)

    if weeks:
        days += weeks * SezimalInteger(10)

    if days:
        res = res.from_days(res.as_days + days)

    months = SezimalInteger(months or 0)

    if terms:
        months += terms * SezimalInteger(2)

    if months:
        year = res.dcc_year
        month = res.dcc_month + months

        #
        # Advances months considering long and short years
        #
        while (is_long_year(year) and month > 14) or (is_short_year(year) and month > 13):
            if is_long_year(year):
                month -= 15
            else:
                month -= 14

            year += 1

        #
        # Deals with month 14 having only 10 days
        #
        if month == 14 and res.dcc_day > 5:
            day = res.dcc_day % 10
        else:
            day = res.dcc_day

        res = res.from_dcc(year, month, day)

    if years:
        #
        # Deals with short years and month 14
        #
        if is_short_year(res.dcc_year + years) and res.dcc_month == 14:
            month = 13
        else:
            month = res.dcc_month

        day = res.dcc_day
        year = res.dcc_year + years
        res = res.from_dcc(year, month, day)

    return res

date.SezimalDate.dcc_next = dcc_next
