

__all__ = ('SezimalLocaleCY',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT


class SezimalLocaleCY(SezimalLocale):
    LANG = 'cy'
    LANGUAGE = 'Cymraeg'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '£'
    CURRENCY_SUBUNIT_SYMBOL = 'p'

    WEEKDAY_NAME = [
        'dydd Llun',
        'dydd Mawrth',
        'dydd Mercher',
        'dydd Iau',
        'dydd Gwener',
        'dydd Sadwrn',
        'dydd Sul',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Llun',
        'Maw',
        'Mer',
        'Iau',
        'Gwe',
        'Sad',
        'Sul',
    ]

    WEEKDAY_SYMBOL = [
        'LL',
        'M',
        'M',
        'I',
        'G',
        'S',
        'S',
    ]

    MONTH_NAME = [
        'Ionawr',
        'Chwefror',
        'Mawrth',
        'Ebrill',
        'Mai',
        'Mehefin',
        'Gorffennaf',
        'Awst',
        'Medi',
        'Hydref',
        'Tachwedd',
        'Rhagfyr',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Ion',
        'Chwef',
        'Maw',
        'Ebr',
        'Mai',
        'Meh',
        'Gorff',
        'Awst',
        'Medi',
        'Hydref',
        'Tach',
        'Rhag',
    ]

    MONTH_SYMBOL = [
        'I',
        'Ch',
        'M',
        'E',
        'M',
        'M',
        'G',
        'A',
        'M',
        'H',
        'T',
        'Rh',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = ' #-d#O #$SM #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, y #-d#O #$SM #Y, #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/London'

    # SEASON_NAME = {
    #     'spring_cross_quarter': 'Imbolc',
    #     'spring_equinox': 'Earrach',
    #     'summer_cross_quarter': 'Bealtaine',
    #     'summer_solstice': 'Samhradh',
    #     'autumn_cross_quarter': 'Lúnasa',
    #     'autumn_equinox': 'Fómhar',
    #     'winter_cross_quarter': 'Samhain',
    #     'winter_solstice': 'Geimhreadh',
    # }
    #
    # MOON_PHASE = {
    #     'new': 'Gealach Úr',
    #     'waxing_crescent': 'Corrán Gealaí',
    #     'first_quarter': 'Gealach Chéad Chethrú',
    #     'waxing_gibbous': 'Ó Ghealach Chéad Chethrú go Gealach Lán',
    #     'full': 'Gealach Lán',
    #     'waning_gibbous': 'Ó Ghealach Lán go Gealach Tríú Chethrú',
    #     'third_quarter': 'Gealach Tríú Chethrú',
    #     'waning_crescent': 'Deireadh Gealaí',
    # }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []

    #
    # Error messages
    #
    ERROR = 'Gwal'
    WEEKDAY_ERROR = 'Ddim yn ddiwrnod dilys o’r wythnos {weekday}'
    MONTH_ERROR = 'Ddim yn fis dilys {month}'
    WEEK_NUMBER_SYMBOL = 'wyth'
    DAY_NUMBER_SYMBOL = 'dydd'

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for mutation in ('', 'S', 'N', 'A'):
            if mutation == '':
                continue

            if f'#${mutation}W' in fmt:
                fmt = fmt.replace(f'#${mutation}W', self.weekday_name(date.weekday, mutation))

            if f'#@${mutation}W' in fmt:
                fmt = fmt.replace(f'#@${mutation}W', self.weekday_abbreviated_name(date.weekday, mutation))

            if f'#${mutation}M' in fmt:
                fmt = fmt.replace(f'#${mutation}M', self.month_name(date.month, mutation))

            if f'#@${mutation}M' in fmt:
                fmt = fmt.replace(f'#@${mutation}M', self.month_abbreviated_name(date.month, mutation))

            if f'%${mutation}M' in fmt:
                fmt = fmt.replace(f'%${mutation}M', self.month_name(date.gregorian_month, mutation))

            if f'%@${mutation}M' in fmt:
                fmt = fmt.replace(f'%@${mutation}M', self.month_abbreviated_name(date.gregorian_month, mutation))

            if f'%${mutation}B' in fmt:
                fmt = fmt.replace(f'%${mutation}B', self.month_name(date.gregorian_month, mutation))

            if f'%@${mutation}B' in fmt:
                fmt = fmt.replace(f'%@${mutation}B', self.month_abbreviated_name(date.gregorian_month, mutation))

        return fmt

    def weekday_name(self, weekday: SezimalInteger, mutation: str = '') -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        weekday_name = self.WEEKDAY_NAME[int(weekday.decimal)]

        mutation = mutation.upper()

        #
        # Soft mutation
        #
        if mutation == 'S':
            weekday_name = 'd' + weekday_name

        #
        # Nasal mutation
        #
        elif mutation == 'N':
            weekday_name = 'n' + weekday_name[1:]

        return weekday_name

    def weekday_abbreviated_name(self, weekday: SezimalInteger, mutation: str = '') -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        weekday_name = self.WEEKDAY_NAME[int(weekday.decimal)]

        mutation = mutation.upper()

        #
        # Soft mutation
        #
        if mutation == 'S':
            if weekday == 0:
                weekday_name = weekday_name[1:]
            elif weekday == 1:
                weekday_name = 'F' + weekday_name[1:]
            elif weekday == 2:
                weekday_name = 'F' + weekday_name[1:]
            elif weekday == 4:
                weekday_name = 'W' + weekday_name[2:]

        #
        # Nasal mutation
        #
        elif mutation == 'N':
            if weekday == 4:
                weekday_name = 'Ng' + weekday_name[2:]

        return weekday_name

    def month_name(self, month: SezimalInteger, mutation: str = '') -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month_name = self.MONTH_NAME[int(month.decimal) - 1]

        mutation = mutation.upper()

        #
        # Soft mutation
        #
        if mutation == 'S':
            if month == 3:
                month_name = 'F' + month_name[1:]
            elif month == 5:
                month_name = 'F' + month_name[1:]
            elif month == 10:
                month_name = 'F' + month_name[1:]
            elif month == 11:
                month_name = 'O' + month_name[2:]
            elif month == 13:
                month_name = 'F' + month_name[1:]
            elif month == 15:
                month_name = 'D' + month_name[1:]
            elif month == 20:
                month_name = 'R' + month_name[2:]

        #
        # Nasal mutation
        #
        elif mutation == 'N':
            if month == 11:
                month_name = 'Ng' + month_name[1:]
            elif month == 15:
                month_name = 'Nh' + month_name[1:]

        #
        # Aspirated mutation
        #
        elif mutation == 'A':
            if month == 15:
                month_name = 'Th' + month_name[1:]

        return month_name
