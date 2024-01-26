

__all__ = ('SezimalLocaleGA',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

#
# Information about lenition, eclipsis etc. from Wikitionary;
#
# Using mí/mhí:
#    https://blogs.transparent.com/irish/nios-mo-faoi-na-mionna-more-about-the-months-in-irish/
#    https://blogs.transparent.com/irish/to-%E2%80%9Cmi%E2%80%9D-or-not-to-%E2%80%9Cmi%E2%80%9D-using-the-word-%E2%80%9Cmonth%E2%80%9D-in-irish/
#
# Ordinal suffix:
#    https://en.wikipedia.org/wiki/Date_and_time_notation_in_Ireland
#
# Date format:
#    https://forum.wordreference.com/threads/irish-gaelic-dates.1477128/
#


class SezimalLocaleGA(SezimalLocale):
    LANG = 'ga'
    LANGUAGE = 'Gaeilge'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_COMMA_ABOVE_RIGHT

    WEEKDAY_NAME = [
        'Luan',
        'Máirt',
        'Céadaoin',
        'Déardaoin',
        'Aoine',
        'Satharn',
        'Domhnach',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Lua',
        'Mái',
        'Céa',
        'Déa',
        'Aoi',
        'Saṫ',
        'Doṁ',
    ]

    MONTH_NAME = [
        'Eanáir',
        'Feabhra',
        'Márta',
        'Aibreán',
        'Bealtaine',
        'Meitheamh',
        'Iúil',
        'Lúnasa',
        'Meán Fómhair',
        'Deireadh Fómhair',
        'mí na Samhain',
        'mí na Nollag',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Ean',
        'Fea',
        'Már',
        'Aib',
        'Bea',
        'Mei',
        'Iúi',
        'Lún',
        'MFó',
        'DFó',
        'Saṁ',
        'Nol',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = ' #-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, an #-d#O lá de #$MHÍM #Y, #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Europe/Dublin'

    SEASON_NAME = {
        'spring_cross_quarter': 'Imbolc',
        'spring_equinox': 'Earrach',
        'summer_cross_quarter': 'Bealtaine',
        'summer_solstice': 'Samhradh',
        'autumn_cross_quarter': 'Lúnasa',
        'autumn_equinox': 'Fómhar',
        'winter_cross_quarter': 'Samhain',
        'winter_solstice': 'Geimhreadh',
    }

    MOON_PHASE = {
        'new': 'Gealach Úr',
        'waxing_crescent': 'Corrán Gealaí',
        'first_quarter': 'Gealach Chéad Chethrú',
        'waxing_gibbous': 'Ó Ghealach Chéad Chethrú go Gealach Lán',
        'full': 'Gealach Lán',
        'waning_gibbous': 'Ó Ghealach Lán go Gealach Tríú Chethrú',
        'third_quarter': 'Gealach Tríú Chethrú',
        'waning_crescent': 'Deireadh Gealaí',
    }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []
    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'ᵈ'
        elif day == 2:
            return 'ᵃ'

        return 'ᵘ́'

    def weekday_name(self, weekday: SezimalInteger, mutation: str = '', case: str = '') -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        weekday_name = self.WEEKDAY_NAME[int(weekday.decimal)]

        mutation = mutation.upper()
        case = case.upper()

        #
        # Lenition
        #
        if mutation == 'L':
            if weekday == 1:
                weekday_name = 'Mh' + weekday_name[1:]
            elif weekday == 2:
                weekday_name = 'Ch' + weekday_name[1:]
            elif weekday == 3:
                weekday_name = 'Dh' + weekday_name[1:]
            elif weekday == 5:
                weekday_name = 'Sh' + weekday_name[1:]
            elif weekday == 10:
                weekday_name = 'Dh' + weekday_name[1:]

        #
        # Eclipsis
        #
        elif mutation == 'E':
            if weekday == 2:
                weekday_name = 'g' + weekday_name
            elif weekday == 3:
                weekday_name = 'n' + weekday_name
            elif weekday == 4:
                weekday_name = 'n' + weekday_name
            elif weekday == 10:
                weekday_name = 'n' + weekday_name

        #
        # H-Protesis
        #
        elif mutation == 'H':
            if weekday == 3:
                weekday_name = 'h' + weekday_name

        #
        # Definite article
        #
        elif mutation == 'AN':
            if case in ['', 'N', 'D']:
                if weekday == 1:
                    weekday_name = 'an Mh' + weekday_name[1:]
                elif weekday == 2:
                    weekday_name = 'an Ch' + weekday_name[1:]
                else:
                    weekday_name = 'an ' + weekday_name

            elif case == 'G':
                if weekday == 0:
                    weekday_name = 'an ' + weekday_name[0:-1] + 'in'
                elif weekday == 1:
                    weekday_name = 'na ' + weekday_name
                elif weekday == 2:
                    weekday_name = 'na ' + weekday_name
                elif weekday == 4:
                    weekday_name = 'na h' + weekday_name
                elif weekday == 5:
                    weekday_name = 'an t' + weekday_name[0:-2] + 'irn'
                elif weekday == 10:
                    weekday_name = 'an ' + weekday_name[0:-2] + 'igh'
                else:
                    weekday_name = 'an ' + weekday_name

        elif mutation == 'DÉ':
            if weekday == 4:
                weekday_name = 'Dé ' + self.weekday_name(weekday + 1, 'H', '')
            elif weekday != 3:
                weekday_name = 'Dé ' + self.weekday_name(weekday + 1, '', 'G')
            else:
                weekday_name = 'Dé ' + weekday_name

        else:
            if case == 'G':
                if weekday == 0:
                    weekday_name = weekday_name[0:-1] + 'in'
                elif weekday == 5:
                    weekday_name = weekday_name[0:-2] + 'irn'
                elif weekday == 10:
                    weekday_name = weekday_name[0:-2] + 'igh'

        return weekday_name

    def weekday_abbreviated_name(self, weekday: SezimalInteger, mutation: str = '', case: str = '') -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        weekday_abbreviated_name = self.WEEKDAY_ABBREVIATED_NAME[int(weekday.decimal)]

        mutation = mutation.upper()
        case = case.upper()

        #
        # Lenition
        #
        if mutation == 'L':
            if weekday == 1:
                weekday_abbreviated_name = 'Mh' + weekday_abbreviated_name[1:]
            elif weekday == 2:
                weekday_abbreviated_name = 'Ch' + weekday_abbreviated_name[1:]
            elif weekday == 3:
                weekday_abbreviated_name = 'Dh' + weekday_abbreviated_name[1:]
            elif weekday == 5:
                weekday_abbreviated_name = 'Sh' + weekday_abbreviated_name[1:]
            elif weekday == 10:
                weekday_abbreviated_name = 'Dh' + weekday_abbreviated_name[1:]

        #
        # Eclipsis
        #
        elif mutation == 'E':
            if weekday == 2:
                weekday_abbreviated_name = 'g' + weekday_abbreviated_name
            elif weekday == 3:
                weekday_abbreviated_name = 'n' + weekday_abbreviated_name
            elif weekday == 4:
                weekday_abbreviated_name = 'n' + weekday_abbreviated_name
            elif weekday == 10:
                weekday_abbreviated_name = 'n' + weekday_abbreviated_name

        #
        # H-Protesis
        #
        elif mutation == 'H':
            if weekday == 3:
                weekday_abbreviated_name = 'h' + weekday_abbreviated_name

        #
        # Definite article
        #
        elif mutation == 'AN':
            if case in ('', 'N', 'D'):
                if weekday == 1:
                    weekday_abbreviated_name = 'an Mh' + weekday_abbreviated_name[1:]
                elif weekday == 2:
                    weekday_abbreviated_name = 'an Ch' + weekday_abbreviated_name[1:]
                else:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name

            elif case == 'G':
                if weekday == 0:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name  # [0:-1] + 'in'
                elif weekday == 1:
                    weekday_abbreviated_name = 'na ' + weekday_abbreviated_name
                elif weekday == 2:
                    weekday_abbreviated_name = 'na ' + weekday_abbreviated_name
                elif weekday == 4:
                    weekday_abbreviated_name = 'na h' + weekday_abbreviated_name
                elif weekday == 5:
                    weekday_abbreviated_name = 'an t' + weekday_abbreviated_name  # [0:-2] + 'irn'
                elif weekday == 10:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name[0:-2] + 'igh'
                else:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name

        elif mutation == 'DÉ':
            if weekday == 4:
                weekday_abbreviated_name = 'Dé ' + self.weekday_abbreviated_name(weekday + 1, 'H', '')
            elif weekday != 3:
                weekday_abbreviated_name = 'Dé ' + self.weekday_abbreviated_name(weekday + 1, '', 'G')
            else:
                weekday_abbreviated_name = 'Dé ' + weekday_abbreviated_name

        # else:
        #     if case == 'G':
        #         if weekday == 0:
        #             weekday_abbreviated_name = weekday_abbreviated_name[0:-1] + 'in'
        #         elif weekday == 5:
        #             weekday_abbreviated_name = weekday_abbreviated_name[0:-2] + 'irn'
        #         elif weekday == 10:
        #             weekday_abbreviated_name = weekday_abbreviated_name[0:-2] + 'igh'

        return weekday_abbreviated_name

    def month_name(self, month: SezimalInteger, mutation: str = '', case: str = '') -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month_name = self.MONTH_NAME[int(month.decimal) - 1]

        mutation = mutation.upper()
        case = case.upper()

        #
        # Lenition
        #
        if mutation == 'L':
            if month == 2:
                month_name = 'Fh' + month_name[1:]
            elif month == 3:
                month_name = 'Mh' + month_name[1:]
            elif month == 5:
                month_name = 'Bh' + month_name[1:]
            elif month == 10:
                if case == 'G':
                    month_name = self.month_name(month, '', 'G')
                    month_name = 'Mh' + month_name[1:]
                else:
                    month_name = 'Mh' + month_name[1:]
            elif month == 13:
                month_name = 'Mh' + month_name[1:]
            elif month == 14:
                month_name = 'Dh' + month_name[1:]
            elif month == 15:
                month_name = 'Mh' + month_name[1:]
            elif month == 20:
                month_name = 'Mh' + month_name[1:]

        #
        # Eclipsis
        #
        elif mutation == 'E':
            if month == 1:
                month_name = 'n' + month_name
            elif month == 2:
                month_name = 'bh' + month_name
            elif month == 4:
                month_name = 'n' + month_name
            elif month == 5:
                month_name = 'm' + month_name
            elif month == 11:
                month_name = 'n' + month_name
            elif month == 14:
                month_name = 'n' + month_name

        #
        # H-Protesis
        #
        elif mutation == 'H':
            if month == 1:
                month_name = 'h' + month_name
            elif month == 4:
                month_name = 'h' + month_name
            elif month == 11:
                month_name = 'h' + month_name

        #
        # T-Protesis
        #
        elif mutation == 'T':
            if month == 1:
                month_name = 't' + month_name
            elif month == 4:
                month_name = 't' + month_name
            elif month == 11:
                month_name = 't' + month_name

        #
        # Definite article
        #
        elif mutation == 'AN':
            if case in ('', 'N', 'D'):
                if month == 1:
                    month_name = 'an ' + self.month_name(month, 'T', '')
                elif month == 2:
                    month_name = 'an ' + self.month_name(month, 'L', '')
                elif month == 4:
                    month_name = 'an ' + self.month_name(month, 'T', '')
                elif month == 5:
                    month_name = 'an ' + self.month_name(month, 'L', '')
                elif month == 11:
                    month_name = 'an ' + self.month_name(month, 'T', '')
                else:
                    month_name = 'an ' + month_name

            elif case == 'G':
                if month == 2:
                    month_name = 'na ' + month_name
                elif month == 3:
                    month_name = 'an ' + self.month_name(month, 'L', '')
                elif month == 4:
                    month_name = 'an ' + self.month_name(month, '', 'G')
                elif month == 5:
                    month_name = 'na ' + month_name
                elif month == 10:
                    month_name = 'an ' + self.month_name(month, 'L', 'G')
                else:
                    month_name = 'an ' + month_name

        elif mutation == 'MÍ':
            if month == 2:
                month_name = 'mí na ' + month_name
            elif month == 3:
                month_name = 'mí an ' + self.month_name(month, 'L')
            elif month == 4:
                month_name = 'mí ' + self.month_name(month, '', 'G')
            elif month == 5:
                month_name = 'mí na ' + month_name
            elif month == 10:
                month_name = 'mí an ' + self.month_name(month, 'L', 'G')
            elif month == 13:
                month_name = 'mí ' + self.month_name(month, 'L', '')
            elif month == 14:
                month_name = 'mí ' + self.month_name(month, 'L', '')
            elif month != 15 and month != 20:
                month_name = 'mí ' + month_name

        elif mutation == 'MHÍ':
            month_name = self.month_name(month, 'MÍ', case)
            month_name = 'mh' + month_name[1:]

        else:
            if case == 'G':
                if month == 4:
                    month_name = month_name[:-1] + 'in'
                elif month == 10:
                    month_name = month_name.replace('ea', 'i')
                elif month == 15:
                    month_name = 'Mh' + month_name[1:-3] + 'na'
                elif month == 20:
                    month_name = 'Mh' + month_name[1:]

        return month_name

    def month_abbreviated_name(self, month: SezimalInteger, mutation: str = '', case: str = '') -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month_abbreviated_name = self.MONTH_ABBREVIATED_NAME[int(month.decimal) - 1]

        mutation = mutation.upper()
        case = case.upper()

        #
        # Lenition
        #
        if mutation == 'L':
            if month == 2:
                month_abbreviated_name = 'Fh' + month_abbreviated_name[1:]
            elif month == 3:
                month_abbreviated_name = 'Mh' + month_abbreviated_name[1:]
            elif month == 5:
                month_abbreviated_name = 'Bh' + month_abbreviated_name[1:]
            elif month == 10:
                if case == 'G':
                    month_abbreviated_name = self.month_abbreviated_name(month, '', 'G')
                    month_abbreviated_name = 'Mh' + month_abbreviated_name[1:]
                else:
                    month_abbreviated_name = 'Mh' + month_abbreviated_name[1:]
            elif month == 13:
                month_abbreviated_name = 'Mh' + month_abbreviated_name[1:]
            elif month == 14:
                month_abbreviated_name = 'Dh' + month_abbreviated_name[1:]
            elif month == 15:
                month_abbreviated_name = 'Mh' + month_abbreviated_name[1:]
            elif month == 20:
                month_abbreviated_name = 'Mh' + month_abbreviated_name[1:]

        #
        # Eclipsis
        #
        elif mutation == 'E':
            if month == 1:
                month_abbreviated_name = 'n' + month_abbreviated_name
            elif month == 2:
                month_abbreviated_name = 'bh' + month_abbreviated_name
            elif month == 4:
                month_abbreviated_name = 'n' + month_abbreviated_name
            elif month == 5:
                month_abbreviated_name = 'm' + month_abbreviated_name
            elif month == 11:
                month_abbreviated_name = 'n' + month_abbreviated_name
            elif month == 14:
                month_abbreviated_name = 'n' + month_abbreviated_name

        #
        # H-Protesis
        #
        elif mutation == 'H':
            if month == 1:
                month_abbreviated_name = 'h' + month_abbreviated_name
            elif month == 4:
                month_abbreviated_name = 'h' + month_abbreviated_name
            elif month == 11:
                month_abbreviated_name = 'h' + month_abbreviated_name

        #
        # T-Protesis
        #
        elif mutation == 'T':
            if month == 1:
                month_abbreviated_name = 't' + month_abbreviated_name
            elif month == 4:
                month_abbreviated_name = 't' + month_abbreviated_name
            elif month == 11:
                month_abbreviated_name = 't' + month_abbreviated_name

        #
        # Definite article
        #
        elif mutation == 'AN':
            if case in ('', 'N', 'D'):
                if month == 1:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, 'T', '')
                elif month == 2:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, 'L', '')
                elif month == 4:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, 'T', '')
                elif month == 5:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, 'L', '')
                elif month == 11:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, 'T', '')
                else:
                    month_abbreviated_name = 'an ' + month_abbreviated_name

            elif case == 'G':
                if month == 2:
                    month_abbreviated_name = 'na ' + month_abbreviated_name
                elif month == 3:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, 'L', '')
                elif month == 4:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, '', 'G')
                elif month == 5:
                    month_abbreviated_name = 'na ' + month_abbreviated_name
                elif month == 10:
                    month_abbreviated_name = 'an ' + self.month_abbreviated_name(month, 'L', 'G')
                else:
                    month_abbreviated_name = 'an ' + month_abbreviated_name

        elif mutation == 'MÍ':
            if month == 2:
                month_abbreviated_name = 'mí na ' + month_abbreviated_name
            elif month == 3:
                month_abbreviated_name = 'mí an ' + self.month_abbreviated_name(month, 'L')
            elif month == 4:
                month_abbreviated_name = 'mí ' + self.month_abbreviated_name(month, '', 'G')
            elif month == 5:
                month_abbreviated_name = 'mí na ' + month_abbreviated_name
            elif month == 10:
                month_abbreviated_name = 'mí an ' + self.month_abbreviated_name(month, 'L', 'G')
            elif month == 13:
                month_abbreviated_name = 'mí ' + self.month_abbreviated_name(month, 'L', '')
            elif month == 14:
                month_abbreviated_name = 'mí ' + self.month_abbreviated_name(month, 'L', '')
            elif month != 15 and month != 20:
                month_abbreviated_name = 'mí ' + month_abbreviated_name

        elif mutation == 'MHÍ':
            month_abbreviated_name = self.month_abbreviated_name(month, 'MÍ', case)
            month_abbreviated_name = 'mh' + month_abbreviated_name[1:]

        else:
            if case == 'G':
                # if month == 4:
                #     month_abbreviated_name = month_abbreviated_name[:-1] + 'in'
                # elif month == 10:
                #     month_abbreviated_name = month_abbreviated_name.replace('ea', 'i')
                if month == 15:
                    month_abbreviated_name = 'Mh' + month_abbreviated_name[1:] # + 'na'
                elif month == 20:
                    month_abbreviated_name = 'Mh' + month_abbreviated_name[1:]

        return month_abbreviated_name

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for mutation in ('', 'L', 'E', 'H', 'AN', 'DÉ'):
            for case in ('', 'N', 'G', 'D'):
                if mutation == '' and case == '':
                    continue

                if f'#${mutation}{case}W' in fmt:
                    fmt = fmt.replace(f'#${mutation}{case}W', self.weekday_name(date.weekday, mutation, case))

                if f'#@${mutation}{case}W' in fmt:
                    fmt = fmt.replace(f'#@${mutation}{case}W', self.weekday_abbreviated_name(date.weekday, mutation, case))

        for mutation in ('', 'L', 'E', 'H', 'T', 'AN', 'MÍ', 'MHÍ'):
            for case in ('', 'N', 'G', 'D'):
                if mutation == '' and case == '':
                    continue

                if f'#${mutation}{case}M' in fmt:
                    fmt = fmt.replace(f'#${mutation}{case}M', self.month_name(date.month, mutation, case))

                if f'#@${mutation}{case}M' in fmt:
                    fmt = fmt.replace(f'#@${mutation}{case}M', self.month_abbreviated_name(date.month, mutation, case))

        return fmt
