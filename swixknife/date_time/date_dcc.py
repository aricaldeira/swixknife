
import re

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..localization import SezimalLocale
from .dcc_functions import \
    ordinal_date_to_year_month_day, \
    year_month_day_to_ordinal_date, \
    is_long_year, is_short_year
from .format_tokens import DCC_DATE_NUMBER_FORMAT_TOKENS, \
    DCC_YEAR_NUMBER_FORMAT_TOKENS, \
    DCC_DATE_TEXT_FORMAT_TOKEN


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
def dcc_list_weeks_in_month(self) -> [SezimalInteger]:
    if self.dcc_month == 14:
        return [140]

    return [
        self.dcc_month * 10,
        self.dcc_month * 10 + 1,
        self.dcc_month * 10 + 2,
        self.dcc_month * 10 + 3,
        self.dcc_month * 10 + 4,
        self.dcc_month * 10 + 5,
    ]

date.SezimalDate.dcc_list_weeks_in_month = dcc_list_weeks_in_month


@property
def dcc_weekday(self) -> SezimalInteger:
    return self._dcc_date[5]

date.SezimalDate.dcc_weekday = dcc_weekday


@property
def dcc_is_short_year(self) -> bool:
    return is_short_year(self.dcc_year)

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
def dcc_month_in_term(self) -> SezimalInteger:
    return self.dcc_month - (self.dcc_term * 2)

date.SezimalDate.dcc_month_in_term = dcc_month_in_term


@property
def dcc_total_days_in_year(self):
    if self.dcc_is_long_year:
        return SezimalInteger(1410)

    return SezimalInteger(1400)

date.SezimalDate.dcc_total_days_in_year = dcc_total_days_in_year


@property
def dcc_total_days_in_term(self):
    if self.dcc_is_long_year and self.dcc_term == 4:
        return SezimalInteger(210)

    return SezimalInteger(200)

date.SezimalDate.dcc_total_days_in_term = dcc_total_days_in_term


@property
def dcc_total_days_in_month(self):
    if self.dcc_month == 14:
        return SezimalInteger(10)

    return SezimalInteger(100)

date.SezimalDate.dcc_total_days_in_month = dcc_total_days_in_month


@property
def dcc_total_days_in_week(self):
    return SezimalInteger(10)

date.SezimalDate.dcc_total_days_in_week = dcc_total_days_in_week


@property
def dcc_total_weeks_in_year(self):
    if self.dcc_is_long_year:
        return SezimalInteger(141)

    return SezimalInteger(140)

date.SezimalDate.dcc_total_weeks_in_year = dcc_total_weeks_in_year


@property
def dcc_total_weeks_in_term(self):
    if self.dcc_is_long_year and self.dcc_term == 4:
        return SezimalInteger(21)

    return SezimalInteger(20)

date.SezimalDate.dcc_total_weeks_in_term = dcc_total_weeks_in_term


@property
def dcc_total_weeks_in_month(self):
    if self.dcc_month == 14:
        return SezimalInteger(1)

    return SezimalInteger(10)

date.SezimalDate.dcc_total_weeks_in_month = dcc_total_weeks_in_month


@property
def dcc_total_months_in_year(self):
    if self.dcc_is_long_year:
        return SezimalInteger(15)

    return SezimalInteger(14)

date.SezimalDate.dcc_total_months_in_year = dcc_total_months_in_year


@property
def dcc_total_months_in_term(self):
    if self.dcc_is_long_year and self.dcc_term == 4:
        return SezimalInteger(3)

    return SezimalInteger(2)

date.SezimalDate.dcc_total_months_in_term = dcc_total_months_in_term


@property
def dcc_total_terms_in_year(self):
    return SezimalInteger(5)

date.SezimalDate.dcc_total_terms_in_year = dcc_total_terms_in_year


@property
def dcc_week_proportion_ellapsed(self) -> Sezimal:
    return self.dcc_weekday / 10

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


_ADC_MONTH_SYMBOL = {
    0: '󱺀',
    1: '󱺁',
    2: '󱺂',
    3: '󱺃',
    4: '󱺄',
    5: '󱺅',
   10: '󱺆',
   11: '󱺇',
   12: '󱺈',
   13: '󱺉',
   14: '󱺊',
}

_ADC_WEEK_SYMBOL = {
    0: '󱺐',
    1: '󱺑',
    2: '󱺒',
    3: '󱺓',
    4: '󱺔',
    5: '󱺕',
}

_ADC_WEEKDAY_SYMBOL = {
    0: '󱺖',
    1: '󱺗',
    2: '󱺘',
    3: '󱺙',
    4: '󱺚',
    5: '󱺛',
}


def _apply_dcc_formats(self, fmt: str = None, locale: str | SezimalLocale = None) -> str:
    #
    # Locale’s date separator
    #
    if '&DS' in fmt:
        if locale:
            fmt = fmt.replace('&DS', locale.DCC_DATE_SEPARATOR)
        else:
            fmt = fmt.replace('&DS', '‐')

    if '&DYMS' in fmt:
        if locale:
            fmt = fmt.replace('&DYMS', locale.DCC_DATE_YEAR_MONTH_SEPARATOR)
        else:
            fmt = fmt.replace('&DYMS', ', ')

    if '&DMDS' in fmt:
        if locale:
            fmt = fmt.replace('&DMDS', locale.DCC_DATE_MONTH_DAY_SEPARATOR)
        else:
            fmt = fmt.replace('&DMDS', ', ')

    #
    # Year’s explicit sign
    #
    if '&+' in fmt:
        if self.dcc_year >= 0:
            fmt = fmt.replace('&+', '+')
        else:
            fmt = fmt.replace('&+', '')

    for token, value, count in (
        ('dY', 'dcc_day_in_year', 'DCC_DAY_IN_YEAR_COUNT'),
        ('dW', 'dcc_weekday', 'DCC_DAY_IN_WEEK_COUNT'),
        ('wY', 'dcc_week_in_year', 'DCC_WEEK_IN_YEAR_COUNT'),
        ('y', 'dcc_year', 'DCC_YEAR_COUNT'),
        ('Y', 'dcc_year', 'DCC_YEAR_COUNT'),
        ('t', 'dcc_term', 'DCC_TERM_COUNT'),
        ('m', 'dcc_month', 'DCC_MONTH_COUNT'),
        ('w', 'dcc_week', 'DCC_WEEK_COUNT'),
        ('d', 'dcc_day', 'DCC_DAY_COUNT'),
    ):
        value = getattr(self, value)
        count = getattr(locale, count)

        for fmttk in ('', '!', '@', '!@', '9', '↋', 'c', 'c!', 'c9', 'c↋'):
            tk = f'&{fmttk}{token}C'

            if tk in fmt:
                if value in count:
                    tkfmt = count[value]
                else:
                    tkfmt = count[None]

                tkfmt = tkfmt.replace('&', '&' + fmttk)

                fmt = fmt.replace(tk, tkfmt)

    #
    # Let’s deal first with the numeric formats
    #
    for regex, token, base, zero, character, value_name, \
        size, size_niftimal, size_decimal in DCC_DATE_NUMBER_FORMAT_TOKENS:
        if not regex.findall(fmt):
            continue

        if base in ['@', '@!', 'Z']:
            value = self._apply_number_format(token, value_name, size_niftimal, locale)
        elif base in ['9', '9?', '↋', '↋?', 'c9', 'c↋']:
            value = self._apply_number_format(token, value_name, size_decimal, locale)
        else:
            value = self._apply_number_format(token, value_name, size, locale)

        if locale and locale.RTL:
            value = '\N{LRI}' + value + '\N{PDI}'

        fmt = regex.sub(value, fmt)

    #
    # Formatted year number
    #
    for regex, token, base, separator, character, value_name in DCC_YEAR_NUMBER_FORMAT_TOKENS:
        if not regex.findall(fmt):
            continue

        year = getattr(self, value_name, 0)

        if 'X' in character and not separator:
            separator = '\U000f1e6d'  # Arda separator

        if base in ['', '!', '?', 'c', 'c!']:
            if '>' in character:
                if value_name in ('year', 'dcc_year') \
                    and year >= '213100' and year < '214000':
                    year -= 213_000
                elif value_name == 'gregorian_year' \
                    and year >= '13100' and year <= '14000':
                    year -= 13_000

            year = locale.format_number(
                year,
                sezimal_digits='!' in base,
                use_group_separator=True,
                sezimal_places=0,
            )

        elif base in ['@', '@!', 'Z', 'Z?']:
            year = locale.format_niftimal_number(
                year,
                sezimal_digits='!' in base,
                regularized_digits='@' in base,
                use_group_separator=True,
                niftimal_places=0,
            )

        elif base in ['9', '9?', 'c9']:
            year = locale.format_decimal_number(
                year - 200_000,
                use_group_separator=True,
                decimal_places=0,
            )

        elif base in ['↋', '↋?', 'c↋']:
            year = locale.format_dozenal_number(
                year - 200_000,
                use_group_separator=True,
                dozenal_places=0,
            )

        if '?' in base:
            year = locale.digit_replace(year)

        if separator:
            if separator[0] == '\\' and len(separator) >= 2:
                separator = separator[1:]

            if separator != locale.GROUP_SEPARATOR:
                year = year.replace(locale.GROUP_SEPARATOR, separator)

        if locale and locale.RTL:
            year = '\N{LRI}' + year + '\N{PDI}'

        fmt = regex.sub(year, fmt)

    #
    # And now, the text formats
    #
    for base, size, case, term_month_week in DCC_DATE_TEXT_FORMAT_TOKEN.findall(fmt):
        regex = re.compile(fr'&{base}{size}{case}{term_month_week}')

        if 'c' in base:
            if term_month_week == 'T':
                if size == '@':
                    text = locale.dcc_term_abbreviated_name(self.dcc_month)
                else:
                    text = locale.dcc_term_name(self.dcc_month)
            elif term_month_week == 'M':
                if size == '@':
                    text = locale.adc_month_abbreviated_name(self.dcc_month)
                else:
                    text = locale.adc_month_name(self.dcc_month)
            elif term_month_week == 'W':
                if size:
                    text = locale.adc_week_abbreviated_name(self.dcc_week)
                else:
                    text = locale.adc_week_name(self.dcc_week)
            else:
                if size:
                    text = locale.adc_weekday_abbreviated_name(self.dcc_weekday)
                else:
                    text = locale.adc_weekday_name(self.dcc_weekday)
        else:
            if term_month_week == 'T':
                if size == '@':
                    text = locale.dcc_term_abbreviated_name(self.dcc_term)
                else:
                    text = locale.dcc_term_name(self.dcc_term)
            elif term_month_week == 'M':
                if size == '@':
                    text = locale.dcc_month_abbreviated_name(self.dcc_month)
                else:
                    text = locale.dcc_month_name(self.dcc_month)
            else:
                if size:
                    text = locale.dcc_weekday_abbreviated_name(self.dcc_weekday)
                else:
                    text = locale.dcc_weekday_name(self.dcc_weekday)

        if size == '1':
            text = locale.dcc_weekday_symbol(self.dcc_weekday)
        elif size == '2':
            text = locale.slice(text, 0, 2)
        elif size == '3':
            text = locale.slice(text, 0, 3)

        if case == '!':
            text = locale.upper(text) if locale else text.upper()
        elif case == '?':
            text = locale.lower(text) if locale else text.lower()
        elif case == '>':
            if locale:
                text = locale.upper(text[0]) + locale.lower(text[1:])
            else:
                text = text[0].upper() + text[1:].lower()

        fmt = regex.sub(text, fmt)

    if '&O' in fmt:
        fmt = fmt.replace('&O', locale.dcc_day_ordinal_suffix(self.dcc_day))

    if '&iM' in fmt:
        fmt = fmt.replace('&iM', locale.ADC_MONTH_ICON[int(self.dcc_month)])

    if '&iW' in fmt:
        fmt = fmt.replace('&iW', locale.ADC_WEEK_ICON[int(self.dcc_week)])

    if '&iD' in fmt:
        fmt = fmt.replace('&iD', locale.ADC_WEEKDAY_ICON[int(self.dcc_weekday)])

    fmt = locale.apply_dcc_date_format(self, fmt)

    return fmt

date.SezimalDate._apply_dcc_formats = _apply_dcc_formats
