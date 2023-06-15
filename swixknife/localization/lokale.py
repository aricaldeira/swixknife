

from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..base import SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE, sezimal_format


class SezimalLocale:
    LANG = 'en'
    LANGUAGE = 'English'
    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME: list[str] = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]

    WEEKDAY_ABBREVIATED_NAME: list[str] = [
        'Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
        'Sun',
    ]

    MONTH_NAME: list[str] = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]

    MONTH_ABBREVIATED_NAME: list[str] = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec',
    ]

    ERA_NAME: list[str] = [
        #
        # Sezimal Human Era
        #
        'SHE',
        #
        # Before Sezimal Human Era
        #
        'BSHE',
    ]

    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'

    def weekday_name(self, weekday: SezimalInteger, case: str = None) -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        return self.WEEKDAY_NAME[int(weekday.decimal)]

    def weekday_abbreviated_name(self, weekday: SezimalInteger, case: str = None) -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        return self.WEEKDAY_ABBREVIATED_NAME[int(weekday.decimal)]

    def month_name(self, month: SezimalInteger, case: str = None) -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month -= 1

        return self.MONTH_NAME[int(month.decimal)]

    def month_abbreviated_name(self, month: SezimalInteger, case: str = None) -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month -= 1

        return self.MONTH_ABBREVIATED_NAME[int(month.decimal)]

    def era_name(self, year: SezimalInteger, case: str = None) -> str:
        year = SezimalInteger(year)

        if year >= 0:
            return self.ERA_NAME[0]

        return self.ERA_NAME[1]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        return ''

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        return fmt

    def format_number(self,
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        sezimal_places: str | int | Decimal | SezimalInteger = 4,
        use_group_separator: bool = True,
        use_subgroup_separator: bool = False,
        use_fraction_group_separator: bool = False,
        use_fraction_subgroup_separator: bool = False,
        dedicated_digits: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0
    ) -> str:
        group_separator = self.GROUP_SEPARATOR if use_group_separator else ''
        subgroup_separator = self.SUBGROUP_SEPARATOR if use_subgroup_separator else ''
        fraction_group_separator = self.FRACTION_GROUP_SEPARATOR if use_fraction_group_separator else ''
        fraction_subgroup_separator = self.FRACTION_SUBGROUP_SEPARATOR if use_fraction_subgroup_separator else ''
        return sezimal_format(
            number, sezimal_places, self.SEZIMAL_SEPARATOR,
            group_separator, subgroup_separator,
            fraction_group_separator, fraction_subgroup_separator,
            dedicated_digits, typographical_negative,
            minimum_size
        )
