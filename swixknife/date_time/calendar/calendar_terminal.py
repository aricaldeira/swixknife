

from .calendar import *
from ..date import SezimalDate
from ..date_time import SezimalDateTime
from ..sun_moon import list_sun_moon
from ..sezimal_functions import system_time_zone
from ...sezimal import SezimalInteger


class SezimalCalendarTerminal(SezimalCalendar):
    COLOR_YEAR = TERMINAL_COLOR_START + '38;5;231' + TERMINAL_COLOR_END

    COLOR_SUMMER = TERMINAL_COLOR_START + '38;5;226;48;5;208' + TERMINAL_COLOR_END
    COLOR_AUTUMN = TERMINAL_COLOR_START + '38;5;52;48;5;223' + TERMINAL_COLOR_END
    COLOR_WINTER = TERMINAL_COLOR_START + '38;5;21;48;5;45' + TERMINAL_COLOR_END
    COLOR_SPRING = TERMINAL_COLOR_START + '38;5;28;48;5;156' + TERMINAL_COLOR_END

    COLOR_DAY_OF_REST = TERMINAL_COLOR_START + '38;5;196' + TERMINAL_COLOR_END
    COLOR_DAY_OF_REST_MARKED = TERMINAL_COLOR_START + '38;5;231;48;5;160' + TERMINAL_COLOR_END

    COLOR_OPTIONAL_DAY_OF_REST = TERMINAL_COLOR_START + '38;5;214' + TERMINAL_COLOR_END
    COLOR_OPTIONAL_DAY_OF_REST_MARKED = TERMINAL_COLOR_START + '38;5;231;48;5;172' + TERMINAL_COLOR_END

    COLOR_MIDQUARTER = TERMINAL_COLOR_START + '38;5;49' + TERMINAL_COLOR_END
    COLOR_MIDQUARTER_MARKED = TERMINAL_COLOR_START + '38;5;16;48;5;49' + TERMINAL_COLOR_END

    COLOR_HOLIDAY = TERMINAL_COLOR_START + '38;5;211' + TERMINAL_COLOR_END
    COLOR_HOLIDAY_MARKED = TERMINAL_COLOR_START + '38;5;16;48;5;211' + TERMINAL_COLOR_END

    COLOR_HOLIDAY_OTHER_CALENDAR = TERMINAL_COLOR_START + '38;5;197' + TERMINAL_COLOR_END
    COLOR_HOLIDAY_OTHER_CALENDAR_MARKED = TERMINAL_COLOR_START + '38;5;16;48;5;197' + TERMINAL_COLOR_END

    COLOR_EVENT = TERMINAL_COLOR_START + '38;5;117' + TERMINAL_COLOR_END
    COLOR_EVENT_MARKED = TERMINAL_COLOR_START + '38;5;16;48;5;117' + TERMINAL_COLOR_END

    COLOR_EVENT_OTHER_CALENDAR = TERMINAL_COLOR_START + '38;5;39' + TERMINAL_COLOR_END
    COLOR_EVENT_OTHER_CALENDAR_MARKED = TERMINAL_COLOR_START + '38;5;16;48;5;39' + TERMINAL_COLOR_END

    COLOR_TODAY = TERMINAL_COLOR_START + '38;5;233;48;5;231' + TERMINAL_COLOR_END

    def _color_template(self, calendar: str) -> str:
        calendar = calendar.replace('[SY]', self.COLOR_YEAR)
        calendar = calendar.replace('[EY]', TERMINAL_COLOR_RESET)

        calendar = calendar.replace('[Sd_00]', '').replace('[Ed_00]', '')

        calendar = self._color_month_season(calendar)
        calendar = self._color_weekday(calendar, self._locale.DAY_OF_REST, self.COLOR_DAY_OF_REST, self.COLOR_DAY_OF_REST_MARKED)
        calendar = self._color_weekday(calendar, self._locale.OPTIONAL_DAY_OF_REST, self.COLOR_OPTIONAL_DAY_OF_REST, self.COLOR_OPTIONAL_DAY_OF_REST_MARKED)
        calendar = self._color_midquarter_day(calendar)
        calendar = self._color_holidays_events(calendar)
        calendar = self._color_holidays_events_other_calendar(calendar)

        for weekday in WEEKDAYS:
            calendar = self._color_weekday(calendar, weekday, '', self.COLOR_TODAY)

        if self._locale.IDEOGRAPHIC:
            calendar = calendar.replace('\ufe0f', ' \ufe0f')
            calendar = calendar.replace(' ', '\u3000')
            calendar = calendar.replace('ISO', 'ＩＳＯ')
            calendar = calendar.replace('(', '（')
            calendar = calendar.replace(')', '）')

        return calendar

    def _color_month_season(self, calendar: str) -> str:
        if self._hemisphere == 'N':
            calendar = calendar.replace('[SM_01]', self.COLOR_WINTER).replace('[EM_01]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_02]', self.COLOR_WINTER).replace('[EM_02]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_03]', self.COLOR_SPRING).replace('[EM_03]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_04]', self.COLOR_SPRING).replace('[EM_04]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_05]', self.COLOR_SPRING).replace('[EM_05]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_10]', self.COLOR_SUMMER).replace('[EM_10]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_11]', self.COLOR_SUMMER).replace('[EM_11]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_12]', self.COLOR_SUMMER).replace('[EM_12]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_13]', self.COLOR_AUTUMN).replace('[EM_13]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_14]', self.COLOR_AUTUMN).replace('[EM_14]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_15]', self.COLOR_AUTUMN).replace('[EM_15]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_20]', self.COLOR_WINTER).replace('[EM_20]', TERMINAL_COLOR_RESET)

        elif self._hemisphere == 'S':
            calendar = calendar.replace('[SM_01]', self.COLOR_SUMMER).replace('[EM_01]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_02]', self.COLOR_SUMMER).replace('[EM_02]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_03]', self.COLOR_AUTUMN).replace('[EM_03]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_04]', self.COLOR_AUTUMN).replace('[EM_04]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_05]', self.COLOR_AUTUMN).replace('[EM_05]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_10]', self.COLOR_WINTER).replace('[EM_10]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_11]', self.COLOR_WINTER).replace('[EM_11]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_12]', self.COLOR_WINTER).replace('[EM_12]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_13]', self.COLOR_SPRING).replace('[EM_13]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_14]', self.COLOR_SPRING).replace('[EM_14]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_15]', self.COLOR_SPRING).replace('[EM_15]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_20]', self.COLOR_SUMMER).replace('[EM_20]', TERMINAL_COLOR_RESET)

        else:
            calendar = calendar.replace('[SM_01]', self.COLOR_SUMMER).replace('[EM_01]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_02]', self.COLOR_SUMMER).replace('[EM_02]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_03]', self.COLOR_SUMMER).replace('[EM_03]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_04]', self.COLOR_SUMMER).replace('[EM_04]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_05]', self.COLOR_SUMMER).replace('[EM_05]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_10]', self.COLOR_SUMMER).replace('[EM_10]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_11]', self.COLOR_SUMMER).replace('[EM_11]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_12]', self.COLOR_SUMMER).replace('[EM_12]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_13]', self.COLOR_SUMMER).replace('[EM_13]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_14]', self.COLOR_SUMMER).replace('[EM_14]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_15]', self.COLOR_SUMMER).replace('[EM_15]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace('[SM_20]', self.COLOR_SUMMER).replace('[EM_20]', TERMINAL_COLOR_RESET)

        return calendar

    def _color_weekday(self, calendar: str, weekday: str, color: str, color_marked: str) -> str:
        if not weekday:
            return calendar

        #
        # Days of rest
        #
        if weekday == WEEKDAY_SUNDAY:
            days = ['11', '22', '33', '44', '55']
            weekday_tag = 'W_11'
        elif weekday == WEEKDAY_SATURDAY:
            days = ['10', '21', '32', '43', '54']
            weekday_tag = 'W_10'
        elif weekday == WEEKDAY_FRIDAY:
            days = ['05', '20', '31', '42', '53']
            weekday_tag = 'W_05'
        elif weekday == WEEKDAY_THURSDAY:
            days = ['04', '15', '30', '41', '52']
            weekday_tag = 'W_04'
        elif weekday == WEEKDAY_WEDNESDAY:
            days = ['03', '14', '25', '40', '51']
            weekday_tag = 'W_03'
        elif weekday == WEEKDAY_TUESDAY:
            days = ['02', '13', '24', '35', '50']
            weekday_tag = 'W_02'
        elif weekday == WEEKDAY_MONDAY:
            days = ['01', '12', '23', '34', '45']
            weekday_tag = 'W_01'

        if color:
            calendar = calendar.replace(f'[S{weekday_tag}]', color).replace(f'[E{weekday_tag}]', TERMINAL_COLOR_RESET)
        else:
            calendar = calendar.replace(f'[S{weekday_tag}]', '').replace(f'[E{weekday_tag}]', '')

        for day in days:
            if color:
                calendar = calendar.replace(f'[Sd_{day}]', color).replace(f'[Ed_{day}]', TERMINAL_COLOR_RESET)
            else:
                calendar = calendar.replace(f'[Sd_{day}]', '').replace(f'[Ed_{day}]', '')

            if color_marked:
                calendar = calendar.replace(f'[SD_{day}]', color_marked).replace(f'[ED_{day}]', TERMINAL_COLOR_RESET)
            else:
                calendar = calendar.replace(f'[SD_{day}]', '').replace(f'[ED_{day}]', '')

        return calendar

    def _color_midquarter_day(self, calendar: str) -> str:
        calendar = calendar.replace('[Sq_30]', self.COLOR_MIDQUARTER).replace('[Eq_30]', TERMINAL_COLOR_RESET)
        calendar = calendar.replace('[SQ_30]', self.COLOR_MIDQUARTER_MARKED).replace('[EQ_30]', TERMINAL_COLOR_RESET)
        return calendar

    def _color_holidays_events(self, calendar: str) -> str:
        for day in SezimalRange(1, 100):
            calendar = calendar.replace(f'[Sh_{str(day).zfill(2)}]', self.COLOR_HOLIDAY).replace(f'[Eh_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace(f'[SH_{str(day).zfill(2)}]', self.COLOR_HOLIDAY_MARKED).replace(f'[EH_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace(f'[Se_{str(day).zfill(2)}]', self.COLOR_EVENT).replace(f'[Ee_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace(f'[SE_{str(day).zfill(2)}]', self.COLOR_EVENT_MARKED).replace(f'[EE_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)

        return calendar

    def _color_holidays_events_other_calendar(self, calendar: str) -> str:
        for day in SezimalRange(1, 100):
            calendar = calendar.replace(f'[Sf_{str(day).zfill(2)}]', self.COLOR_HOLIDAY_OTHER_CALENDAR).replace(f'[Ef_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace(f'[SF_{str(day).zfill(2)}]', self.COLOR_HOLIDAY_OTHER_CALENDAR_MARKED).replace(f'[EF_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace(f'[Sa_{str(day).zfill(2)}]', self.COLOR_EVENT_OTHER_CALENDAR).replace(f'[Ea_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)
            calendar = calendar.replace(f'[SA_{str(day).zfill(2)}]', self.COLOR_EVENT_OTHER_CALENDAR_MARKED).replace(f'[EA_{str(day).zfill(2)}]', TERMINAL_COLOR_RESET)

        return calendar

    def month(self, month: SezimalInteger = None, year: SezimalInteger = None) -> str:
        calendar = '\n' + self._month_template(month, year)
        calendar = self._include_time(calendar)
        calendar = self._include_events(calendar)

        return self._color_template(calendar)

    def _include_time(self, calendar: str) -> str:
        time = self._date_time.time

        time_format = self._time_format
        iso_time_format = self._locale.ISO_TIME_FORMAT

        if self._locale.RTL and self._locale.DIGITS and '?' in time_format:
            iso_time_format = RTL_MARKER + iso_time_format + LTR_MARKER

            if self._use_rtl:
                iso_time_format = '(' + iso_time_format + ' ISO)'

                if time.is_dst:
                    time_format = RTL_MARKER + time_format + ' @V' + LTR_MARKER
                else:
                    time_format = RTL_MARKER + time_format + LTR_MARKER + ' \ufe0f⏰'

            else:
                iso_time_format = '(ISO ' + iso_time_format + ')'

                if time.is_dst:
                    time_format = RTL_MARKER + '@V ' + time_format + LTR_MARKER
                else:
                    time_format = '\ufe0f⏰ ' + RTL_MARKER + time_format + LTR_MARKER

        else:
            iso_time_format = '(ISO ' + iso_time_format + ')'

            if time.is_dst:
                time_format = '@V ' + time_format
            else:
                time_format = '\ufe0f⏰ ' + time_format

        now_time = time.format(time_format, self._locale)
        iso_time = time.format(iso_time_format, self._locale)

        calendar += self._locale.ljust('', 43) + '\n'
        calendar += self._locale.center(now_time, 43) + '\n'
        calendar += self._locale.center(iso_time, 43)

        if self._date_time.time_zone != system_time_zone():
            calendar += '\n'
            calendar += self._locale.center(self._date_time.time_zone, 43)

        return calendar

    def quarter(self, month: SezimalInteger = None, year: SezimalInteger = None) -> str:
        return '\n' + self._color_template(self._quarter_template(month, year))[:-1]

    def year(self):
        return self._color_template(self._year_template())[:-1]

    def list_holidays(self) -> list[str]:
        month = str(self._date_time.month).zfill(2) + '-'

        lines = []

        for dates in (self._holidays, self._holidays_other_calendar, self._events, self._events_other_calendar):
            for month_day in dates:
                if not month_day.startswith(month):
                    continue

                date = SezimalDate(str(self._date_time.year) + '-' + month_day)
                day = date.format(self._day_format, self._locale)
                day = self._locale.rjust(day, 2)

                #
                # The time will be stripped latter, it is here just for sorting purposes
                #
                line = f'{day}|00:00| - {dates[month_day]}'

                #
                # Check for the same occurrence on the same day,
                # but with different calendars
                #
                new_line = line

                for i in range(len(lines)):
                    l = lines[i]
                    if l.startswith(line):
                        new_line = ''
                        break
                    elif line.startswith(l):
                        lines[i] = line
                        new_line = ''
                        break

                if new_line:
                    lines.append(new_line)

        return lines

    def list_astronomical_events(self) -> list[str]:
        events = list_sun_moon(self._date_time.year, self._date_time.month, self._date_time.time_zone)

        if '%' in self._time_format:
            separator = self._time_format.split('%')[1][-1]
        else:
            separator = self._time_format.split('#')[1][-1]

        parts = self._time_format.split(separator)
        time_format = parts[0] + separator + parts[1]

        lines = []

        for date, sun_moon, name in events:
                day = date.format(self._day_format, self._locale)
                day = self._locale.rjust(day, 2)

                #
                # The time will be stripped latter, it is here just for sorting purposes
                #
                if sun_moon == 'sun':
                    line = f'{day}|{time_format}| - #@{self._hemisphere}S #{self._hemisphere}S ({time_format})'
                else:
                    line = f'{day}|{time_format}| - #@{self._hemisphere}L #{self._hemisphere}L ({time_format})'

                lines.append(date.format(line, self._locale))

        return lines

    def _include_events(self, calendar: str) -> str:
        if self._hemisphere == 'S':
            season_moon_emoji = self._date_time.format('#@~SS #@~SL', self._locale)
        else:
            season_moon_emoji = self._date_time.format('#@~NS #@~NL', self._locale)

        text = f'''\n[SY]{self._date_time.format(self._date_format, self._locale)} ― {season_moon_emoji}[EY]
(ISO {self._date_time.format(self._locale.ISO_DATE_FORMAT, self._locale)})

'''

        lines = self.list_holidays()
        lines += self.list_astronomical_events()

        lines = sorted(lines, key=self._locale.sort_key)

        for line in lines:
            parts = line.split('|')
            text += parts[0] + parts[-1] + '\n'

        if self._locale.RTL and self._use_rtl:
            return self._merge_lines(text, calendar)[:-1]
        else:
            return self._merge_lines(calendar, text)[:-1]
