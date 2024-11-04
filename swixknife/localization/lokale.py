
from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')

import itertools
import locale as system_locale

from decimal import Decimal

from .constants import UNPRINTABLE_CHARACTERS, EMOJI_CHARACTERS, IDEOGRAPHIC_CHARACTERS
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction, SezimalDecimalUnit
from ..functions import SezimalRange
from ..base import SEPARATOR_COMMA, SEPARATOR_UNDERSCORE, \
    SEPARATOR_NARROW_NOBREAK_SPACE, \
    RECURRING_DIGITS_NOTATION_SIMPLE, \
    sezimal_format, decimal_format, dozenal_format, \
    niftimal_format, SEPARATOR_WEDGE, \
    SEPARATOR_DECIMAL_CURRENCY
from ..text import sezimal_spellout


class SezimalLocale:
    LANG = 'en'
    LANGUAGE = 'English'

    #
    # Language script is right to left?
    #
    RTL = False
    #
    # Script is ideographic?
    #
    IDEOGRAPHIC = False
    DIGITS = ''

    #
    # Number formatting
    #
    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    FRACTION_SUBGROUP_SEPARATOR = ''

    RECURRING_DIGITS_NOTATION = RECURRING_DIGITS_NOTATION_SIMPLE

    #
    # Date and time
    #
    FIRST_WEEKDAY = 'MON'
    DAY_OF_REST = 'SUN'
    OPTIONAL_DAY_OF_REST = 'SAT'

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

    @property
    def WEEKDAY_SYMBOL(self) -> list[str]:
        return [self.slice(wdn, 0, 1) for wdn in self.WEEKDAY_ABBREVIATED_NAME]

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

    @property
    def ISO_MONTH_NAME(self) -> list[str]:
        return self.MONTH_NAME

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

    @property
    def ISO_MONTH_ABBREVIATED_NAME(self) -> list[str]:
        return self.MONTH_ABBREVIATED_NAME

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

    ISO_MODE = False
    DATE_SEPARATOR = '-'
    DATE_FORMAT = '#Y-#m-#d'
    DATE_LONG_FORMAT = '#Y-#m-#d'
    TIME_SEPARATOR = ':'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#Y-#m-#d #@W #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#Y-#m-#d #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    DST_EMOJI = '‍\ufe0f⏰   🌞\ufe0f'

    @property
    def ISO_DATE_FORMAT(self):
        return self._to_iso_date_format(self.DATE_FORMAT)

    @property
    def ISO_DATE_LONG_FORMAT(self):
        return self._to_iso_date_format(self.DATE_LONG_FORMAT)

    ISO_TIME_FORMAT = '%H:%M:%S'

    @property
    def SHORT_TIME_FORMAT(self):
        if 'fD' in self.TIME_FORMAT:
            return self.TIME_FORMAT.split('.')[0] + '.0fD'

        parts = self.TIME_FORMAT.split(self.TIME_SEPARATOR)
        stf = self.TIME_SEPARATOR.join(parts[0:2])

        if '%P' in self.TIME_FORMAT:
            stf += ' %P'

        return stf

    def _to_iso_date_format(self, date_format) -> str:
        for separator in (
            '_', '.', ',', '˙', 'ʼ',
            '’', "'", '•', '◦', '\u0020', '\u00a0',
            '\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005',
            '\u2006', '\u2007', '\u2008', '\u2009', '\u200a', '\u202f',
            '\u205f', '\U000f1e6c', '\U000f1e6d', '\U000f1e6e', '\U000f1e6f',
            '',
        ):
            date_format = date_format.replace(f'#{separator}', '%')

        date_format = date_format.replace('!', '')
        date_format = date_format.replace('9', '')
        date_format = date_format.replace('↋', '')
        date_format = date_format.replace('Z', '')
        date_format = date_format.replace('y', 'Y')
        date_format = date_format.replace('O', 'o')
        date_format = date_format.replace('M', 'B')
        date_format = date_format.replace('W', 'A')
        date_format = date_format.replace('@A', 'a')
        date_format = date_format.replace('X', 'Y')
        date_format = date_format.replace('%#', '%')
        date_format = date_format.replace('%@B', '%b')
        date_format = date_format.replace('%>Y', '%Y')
        date_format = date_format.replace('%?>Y', '%?Y')
        date_format = date_format.replace('%sY', '%Y')
        date_format = date_format.replace('%?sY', '%?Y')
        date_format = date_format.replace('@', '')

        return date_format

    @property
    def ISO_SHORT_TIME_FORMAT(self) -> str:
        ihmf = self.ISO_TIME_FORMAT

        if self.RTL:
            ihmf = ihmf.replace('\N{LRI}', '')
            ihmf = ihmf.replace('\N{PDI}', '')

        parts = ihmf.split(self.TIME_SEPARATOR)
        ihmf = self.TIME_SEPARATOR.join(parts[0:2])

        if self.RTL:
            ihmf = '\N{LRI}' + ihmf + '\N{PDI}'

        return ihmf

    @property
    def DATE_ENDIANNESS(self) -> str:
        parts = self.DATE_FORMAT.split(self.DATE_SEPARATOR)

        if not parts[-1]:
            del parts[-1]

        if parts[-1][-1] == 'd' \
            and parts[0][-1] in ('y', 'Y', 'x', 'X'):
            return 'B'

        if parts[0][-1] == 'd' \
            and parts[-1][-1] in ('y', 'Y', 'x', 'X'):
            return 'L'

        return 'M'

    @property
    def YEAR_FORMAT(self) -> str:
        parts = self.DATE_FORMAT.split(self.DATE_SEPARATOR)
        yf = ''

        for i in range(len(parts)):
            if parts[i][-1] in ('y', 'Y', 'X'):
                yf = parts[i]
                break

        return yf

    @property
    def ISO_YEAR_FORMAT(self) -> str:
        return self._to_iso_date_format(self.YEAR_FORMAT)

    @property
    def YEAR_MONTH_FORMAT(self) -> str:
        parts = self.DATE_FORMAT.split(self.DATE_SEPARATOR)

        for i in range(len(parts)):
            if parts[i][-1] == 'd':
                del parts[i]
                break

        return self.DATE_SEPARATOR.join(parts)

    @property
    def ISO_YEAR_MONTH_FORMAT(self) -> str:
        return self._to_iso_date_format(self.YEAR_MONTH_FORMAT)

    def _to_text_short_month_format(self, fmt: str) -> str:
        fmt = fmt.replace('#m', '#@M')
        fmt = fmt.replace('#?m', '#@M')
        fmt = fmt.replace('#9m', '#@M')
        fmt = fmt.replace('#↋m', '#@M')
        fmt = fmt.replace('#@m', '#@M')
        fmt = fmt.replace('#!m', '#@M')
        fmt = fmt.replace('#@!m', '#@M')
        return fmt

    @property
    def DATE_TEXT_SHORT_MONTH_FORMAT(self) -> str:
        return self._to_text_short_month_format(self.DATE_FORMAT)

    @property
    def ISO_DATE_TEXT_SHORT_MONTH_FORMAT(self) -> str:
        return self._to_iso_date_format(self.DATE_TEXT_SHORT_MONTH_FORMAT)

    def _to_text_month_format(self, fmt: str) -> str:
        fmt = fmt.replace('#m', '#M')
        fmt = fmt.replace('#?m', '#M')
        fmt = fmt.replace('#9m', '#M')
        fmt = fmt.replace('#↋m', '#M')
        fmt = fmt.replace('#@m', '#M')
        fmt = fmt.replace('#!m', '#M')
        fmt = fmt.replace('#@!m', '#M')
        return fmt

    @property
    def YEAR_TEXT_MONTH_FORMAT(self) -> str:
        df = self._to_text_month_format(self.DATE_FORMAT)
        parts = df.split(self.DATE_SEPARATOR)

        for i in range(len(parts)):
            if parts[i][-1] == 'd':
                del parts[i]
                break

        return self.DATE_SEPARATOR.join(parts)

    @property
    def YEAR_TEXT_SHORT_MONTH_FORMAT(self) -> str:
        df = self._to_text_short_month_format(self.DATE_FORMAT)
        parts = df.split(self.DATE_SEPARATOR)

        for i in range(len(parts)):
            if parts[i][-1] == 'd':
                del parts[i]
                break

        return self.DATE_SEPARATOR.join(parts)

    @property
    def MONTH_DAY_FORMAT(self) -> str:
        if self.ISO_MODE:
            return self.DATE_FORMAT

        parts = self.DATE_FORMAT.split(self.DATE_SEPARATOR)

        for i in range(len(parts)):
            if parts[i][-1] in ('y', 'Y', 'x', 'X'):
                del parts[i]
                break

        return self.DATE_SEPARATOR.join(parts)

    @property
    def ISO_MONTH_DAY_FORMAT(self) -> str:
        return self._to_iso_date_format(self.MONTH_DAY_FORMAT)

    @property
    def TEXT_MONTH_DAY_FORMAT(self) -> str:
        df = self._to_text_month_format(self.DATE_FORMAT)
        parts = df.split(self.DATE_SEPARATOR)

        if not self.ISO_MODE:
            for i in range(len(parts)):
                if parts[i][-1] in ('y', 'Y', 'x', 'X'):
                    del parts[i]
                    break

        return self.DATE_SEPARATOR.join(parts)

    @property
    def ISO_TEXT_MONTH_DAY_FORMAT(self) -> str:
        return self._to_iso_date_format(self.TEXT_MONTH_DAY_FORMAT)

    def _to_short_day_format(self, fmt: str) -> str:
        fmt = fmt.replace('#d', '#-d')
        fmt = fmt.replace('#?d', '#?-d')
        fmt = fmt.replace('#9d', '#9-d')
        fmt = fmt.replace('#↋d', '#↋-d')
        fmt = fmt.replace('#@d', '#@-d')
        fmt = fmt.replace('#!d', '#!-d')
        fmt = fmt.replace('#@!d', '#@!-d')
        return fmt

    @property
    def TEXT_SHORT_MONTH_DAY_FORMAT(self) -> str:
        df = self._to_text_short_month_format(self.DATE_FORMAT)
        df = self._to_short_day_format(df)
        parts = df.split(self.DATE_SEPARATOR)

        for i in range(len(parts)):
            if parts[i][-1] in ('y', 'Y', 'x', 'X'):
                del parts[i]
                break

        return self.DATE_SEPARATOR.join(parts)

    @property
    def ISO_TEXT_SHORT_MONTH_DAY_FORMAT(self) -> str:
        return self._to_iso_date_format(self.TEXT_SHORT_MONTH_DAY_FORMAT)

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'UTC'
    AM = 'am'
    PM = 'pm'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Summer',
        'autumn_cross_quarter': 'Autumn Cross-Quarter',
        'autumn_equinox': 'Autumn',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Winter',
    }

    #
    # Allowing for the emojis to be different, since
    # the seasons have different characteristics
    # between Northern and Southern Hemispheres, generally speaking
    #
    SEASON_EMOJI_NORTHERN_HEMISPHERE = {
        'spring_cross_quarter': '❄️\ufe0f\ufe0f〰\ufe0f🌷\ufe0f',
        'spring_equinox': '🌷\ufe0f',
        'summer_cross_quarter': '🌷\ufe0f〰\ufe0f🌞\ufe0f',
        'summer_solstice': '🌞\ufe0f',
        'autumn_cross_quarter': '🌞\ufe0f〰\ufe0f🍂\ufe0f',
        'autumn_equinox': '🍂\ufe0f',
        'winter_cross_quarter': '🍂\ufe0f〰\ufe0f❄️\ufe0f',
        'winter_solstice': '❄️\ufe0f',
    }

    SEASON_EMOJI_SOUTHERN_HEMISPHERE = {
        'autumn_cross_quarter': '🌞\ufe0f〰\ufe0f🍂\ufe0f',
        'autumn_equinox': '🍂\ufe0f',
        'winter_cross_quarter': '🍂\ufe0f〰\ufe0f❄️\ufe0f',
        'winter_solstice': '❄️\ufe0f',
        'spring_cross_quarter': '❄️\ufe0f\ufe0f〰\ufe0f🌺\ufe0f',
        'spring_equinox': '🌺\ufe0f',
        'summer_cross_quarter': '🌺\ufe0f〰\ufe0f🌞\ufe0f',
        'summer_solstice': '🌞\ufe0f',
    }

    MOON_PHASE = {
        'new': 'New',
        'waxing_crescent': 'Waxing Crescent',
        'first_quarter': 'First Quarter',
        'waxing_gibbous': 'Waxing Gibbous',
        'full': 'Full',
        'waning_gibbous': 'Waning Gibbous',
        'third_quarter': 'Third Quarter',
        'waning_crescent': 'Waning Crescent',
    }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []

    #
    # Error messages
    #
    ERROR = 'Error'
    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'
    WEEK_NUMBER_SYMBOL = 'w#'
    DAY_NUMBER_SYMBOL = 'd#'

    #
    # Currency symbols and format
    #
    CURRENCY_UNIT_SYMBOL = '¤'
    CURRENCY_SUBUNIT_SYMBOL = '¤'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 2
    CURRENCY_UNIT_SYMBOL_POSITION = 'L'  # Left
    CURRENCY_UNIT_SYMBOL_WITH_SPACE = True
    CURRENCY_SUBUNIT_SYMBOL_WITH_SPACE = True

    @property
    def CURRENCY_SUBUNIT_SYMBOL_POSITION(self):
        return self.CURRENCY_UNIT_SYMBOL_POSITION

    @property
    def CURRENCY_SEPARATOR(self):
        if self.SEZIMAL_SEPARATOR == '.':
            return ';'
        elif self.SEZIMAL_SEPARATOR == '٫':
            return '؛'

        return ';'

    @property
    def CURRENCY_LONG_FORMAT(self):
        if self.CURRENCY_UNIT_SYMBOL_POSITION == 'L':
            if self.CURRENCY_UNIT_SYMBOL_WITH_SPACE:
                res = '{unit_symbol} {unit}'
            else:
                res = '{unit_symbol}{unit}'
        else:
            if self.CURRENCY_UNIT_SYMBOL_WITH_SPACE:
                res = '{unit} {unit_symbol}'
            else:
                res = '{unit}{unit_symbol}'

        res += ' '

        if self.CURRENCY_SUBUNIT_SYMBOL_POSITION == 'L':
            if self.CURRENCY_SUBUNIT_SYMBOL_WITH_SPACE:
                res += '{subunit_symbol} {subunit}'
            else:
                res += '{subunit_symbol}{subunit}'
        else:
            if self.CURRENCY_SUBUNIT_SYMBOL_WITH_SPACE:
                res += '{subunit} {subunit_symbol}'
            else:
                res += '{subunit}{subunit_symbol}'

        return res

    @property
    def CURRENCY_SHORT_FORMAT(self):
        if self.CURRENCY_UNIT_SYMBOL_POSITION == 'L':
            if self.CURRENCY_UNIT_SYMBOL_WITH_SPACE:
                res = '{unit_symbol} {unit}'
            else:
                res = '{unit_symbol}{unit}'

            res += self.CURRENCY_SEPARATOR
            res += '{subunit}'

        else:
            res = '{unit}'
            res += self.CURRENCY_SEPARATOR
            res += '{subunit}'

            if self.CURRENCY_UNIT_SYMBOL_WITH_SPACE:
                res += ' {unit_symbol}'
            else:
                res += '{unit_symbol}'

        return res

    #
    # Collation rules
    #
    COLLATION_RULES = ''
    SEZIMAL_COLLATION_RULES = '''
&0<1<2<3<4<5<6<7<8<9<↊<↋<0̈<1̈<2̈<3̈<4̈<5̈<0̊<1̊<2̊<3̊<4̊<5̊<0̄<1̄<2̄<3̄<4̄<5̄<0̆<1̆<2̆<3̆<4̆<5̆
&0<<󱸀<<<⁰<<󱸤<<<₀<<󱹈
&1<<󱸁<<<¹<<󱸥<<<₁<<󱹉
&2<<󱸂<<<²<<󱸦<<<₂<<󱹊
&3<<󱸃<<<³<<󱸧<<<₃<<󱹋
&4<<󱸄<<<⁴<<󱸨<<<₄<<󱹌
&5<<󱸅<<<⁵<<󱸩<<<₅<<󱹍
&6<<0̇<<󱸆<<󱸀̇<<<⁶<<⁰̇<<󱨪<<󱸤̇<<<₆<<₀̇<<󱩎<<󱹈̇
&7<<1̇<<󱸇<<󱸁̇<<<⁷<<¹̇<<󱨫<<󱸥̇<<<₇<<₁̇<<󱩏<<󱹉̇
&8<<2̇<<󱸈<<󱸂̇<<<⁸<<²̇<<󱨬<<󱸦̇<<<₈<<₂̇<<󱩐<<󱹊̇
&9<<3̇<<󱸉<<󱸃̇<<<⁹<<³̇<<󱨭<<󱸧̇<<<₉<<₃̇<<󱩑<<󱹋̇
&↊<<4̇<<󱸊<<󱸄̇<<<⁴̇<<󱨮<<󱸨̇<<<₄̇<<󱩒<<󱹌̇
&↋<<5̇<<󱸋<<󱸅̇<<<⁵̇<<󱨯<<󱸩̇<<<₅̇<<󱩓<<󱹍̇
&0̈<<󱨌<<󱸀̈<<<⁰̈<<󱨰<<󱸤̈<<<₀̈<<󱩔<<󱹈̈
&1̈<<󱨍<<󱸁̈<<<¹̈<<󱨱<<󱸥̈<<<₁̈<<󱩕<<󱹉̈
&2̈<<󱨎<<󱸂̈<<<²̈<<󱨲<<󱸦̈<<<₂̈<<󱩖<<󱹊̈
&3̈<<󱨏<<󱸃̈<<<³̈<<󱨳<<󱸧̈<<<₃̈<<󱩗<<󱹋̈
&4̈<<󱨐<<󱸄̈<<<⁴̈<<󱨴<<󱸨̈<<<₄̈<<󱩘<<󱹌̈
&5̈<<󱨑<<󱸅̈<<<⁵̈<<󱨵<<󱸩̈<<<₅̈<<󱩙<<󱹍̈
&0̊<<󱨒<<󱸀̊<<<⁰̊<<󱨶<<󱸤̊<<<₀̊<<󱩚<<󱹈̊
&1̊<<󱨓<<󱸁̊<<<¹̊<<󱨷<<󱸥̊<<<₁̊<<󱩛<<󱹉̊
&2̊<<󱨔<<󱸂̊<<<²̊<<󱨸<<󱸦̊<<<₂̊<<󱩜<<󱹊̊
&3̊<<󱨕<<󱸃̊<<<³̊<<󱨹<<󱸧̊<<<₃̊<<󱩝<<󱹋̊
&4̊<<󱨖<<󱸄̊<<<⁴̊<<󱨺<<󱸨̊<<<₄̊<<󱩞<<󱹌̊
&5̊<<󱨗<<󱸅̊<<<⁵̊<<󱨻<<󱸩̊<<<₅̊<<󱩟<<󱹍̊
&0̄<<󱨘<<󱸀̄<<<⁰̄<<󱨼<<󱸤̄<<<₀̄<<󱩠<<󱹈̄
&1̄<<󱨙<<󱸁̄<<<¹̄<<󱨽<<󱸥̄<<<₁̄<<󱩡<<󱹉̄
&2̄<<󱨚<<󱸂̄<<<²̄<<󱨾<<󱸦̄<<<₂̄<<󱩢<<󱹊̄
&3̄<<󱨛<<󱸃̄<<<³̄<<󱨿<<󱸧̄<<<₃̄<<󱩣<<󱹋̄
&4̄<<󱨜<<󱸄̄<<<⁴̄<<󱩀<<󱸨̄<<<₄̄<<󱩤<<󱹌̄
&5̄<<󱨝<<󱸅̄<<<⁵̄<<󱩁<<󱸩̄<<<₅̄<<󱩥<<󱹍̄
&0̆<<󱨞<<󱸀̆<<<⁰̆<<󱩂<<󱸤̆<<<₀̆<<󱩦<<󱹈̆
&1̆<<󱨟<<󱸁̆<<<¹̆<<󱩃<<󱸥̆<<<₁̆<<󱩧<<󱹉̆
&2̆<<󱨠<<󱸂̆<<<²̆<<󱩄<<󱸦̆<<<₂̆<<󱩨<<󱹊̆
&3̆<<󱨡<<󱸃̆<<<³̆<<󱩅<<󱸧̆<<<₃̆<<󱩩<<󱹋̆
&4̆<<󱨢<<󱸄̆<<<⁴̆<<󱩆<<󱸨̆<<<₄̆<<󱩪<<󱹌̆
&5̆<<󱨣<<󱸅̆<<<⁵̆<<󱩇<<󱸩̆<<<₅̆<<󱩫<<󱹍̆
'''

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

    def weekday_symbol(self, weekday: SezimalInteger, case: str = None) -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        return self.WEEKDAY_SYMBOL[int(weekday.decimal)]

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

    def iso_month_name(self, month: SezimalInteger, case: str = None) -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month -= 1

        return self.ISO_MONTH_NAME[int(month.decimal)]

    def iso_month_abbreviated_name(self, month: SezimalInteger, case: str = None) -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month -= 1

        return self.ISO_MONTH_ABBREVIATED_NAME[int(month.decimal)]

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
        sezimal_digits: bool = False,
        sezimal_punctuation: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        recurring_digits_notation: bool | str | int | Decimal | Sezimal | SezimalInteger = False,
        grouping_digits: int = 3,
        keep_original_aspect: bool = False,
        native_digits: bool = True,
    ) -> str:
        group_separator = self.GROUP_SEPARATOR if use_group_separator else ''
        subgroup_separator = self.SUBGROUP_SEPARATOR if use_subgroup_separator else ''
        fraction_group_separator = self.FRACTION_GROUP_SEPARATOR if use_fraction_group_separator else ''
        fraction_subgroup_separator = self.FRACTION_SUBGROUP_SEPARATOR if use_fraction_subgroup_separator else ''

        if recurring_digits_notation and isinstance(recurring_digits_notation, bool):
            recurring_digits_notation = self.RECURRING_DIGITS_NOTATION

        res = sezimal_format(
            number, sezimal_places, self.SEZIMAL_SEPARATOR,
            group_separator, subgroup_separator,
            fraction_group_separator, fraction_subgroup_separator,
            sezimal_digits, sezimal_punctuation, typographical_negative,
            minimum_size,
            prefix,
            suffix,
            positive_format,
            negative_format,
            recurring_digits_notation,
            grouping_digits,
            keep_original_aspect,
        )

        if (not sezimal_digits) and native_digits and self.DIGITS:
            res = self.digit_replace(res)

            if self.RTL:
                res = '\N{LRI}' + res + '\N{PDI}'

        return res

    def format_decimal_number(self,
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        decimal_places: str | int | Decimal | SezimalInteger = 2,
        use_group_separator: bool = True,
        use_fraction_group_separator: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        recurring_digits_notation: bool | str | int | Decimal | Sezimal | SezimalInteger = False,
        keep_original_aspect: bool = False,
        #
        # Lakhs and crores are Indian names for powers of ten
        # https://en.wikipedia.org/wiki/Indian_numbering_system
        #
        lakh_crore_grouping: bool = False,
        #
        # 萬/万: Chinese wàn/ㄨㄢˋ, Japanese まん man, Korean 만 man, Vietnamese vạn
        # https://en.wikipedia.org/wiki/Japanese_numerals#Powers_of_10
        #
        wan_man_van_grouping: bool = False,
        native_digits: bool = True,
    ) -> str:
        group_separator = self.GROUP_SEPARATOR if use_group_separator else ''
        fraction_group_separator = self.FRACTION_GROUP_SEPARATOR if use_fraction_group_separator else ''

        if recurring_digits_notation and isinstance(recurring_digits_notation, bool):
            recurring_digits_notation = self.RECURRING_DIGITS_NOTATION

        res = decimal_format(
            number, decimal_places, self.SEZIMAL_SEPARATOR,
            group_separator, fraction_group_separator,
            typographical_negative,
            minimum_size,
            prefix,
            suffix,
            positive_format,
            negative_format,
            recurring_digits_notation,
            keep_original_aspect,
            lakh_crore_grouping,
            wan_man_van_grouping,
        )

        if native_digits and self.DIGITS:
            res = self.digit_replace(res)

            if self.RTL:
                res = '\N{LRI}' + res + '\N{PDI}'

        return res

    def format_dozenal_number(self,
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        dozenal_places: str | int | Decimal | SezimalInteger = 2,
        use_group_separator: bool = True,
        use_subgroup_separator: bool = False,
        use_fraction_group_separator: bool = False,
        use_fraction_subgroup_separator: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        recurring_digits_notation: bool | str | int | Decimal | Sezimal | SezimalInteger = False,
        native_digits: bool = True,
    ) -> str:
        group_separator = self.GROUP_SEPARATOR if use_group_separator else ''
        subgroup_separator = self.SUBGROUP_SEPARATOR if use_subgroup_separator else ''
        fraction_group_separator = self.FRACTION_GROUP_SEPARATOR if use_fraction_group_separator else ''
        fraction_subgroup_separator = self.FRACTION_SUBGROUP_SEPARATOR if use_fraction_subgroup_separator else ''

        if recurring_digits_notation and isinstance(recurring_digits_notation, bool):
            recurring_digits_notation = self.RECURRING_DIGITS_NOTATION

        res = dozenal_format(
            number, dozenal_places, self.SEZIMAL_SEPARATOR,
            group_separator, subgroup_separator,
            fraction_group_separator, fraction_subgroup_separator,
            typographical_negative,
            minimum_size,
            prefix,
            suffix,
            positive_format,
            negative_format,
            recurring_digits_notation,
        )

        if native_digits and self.DIGITS:
            res = self.digit_replace(res)

            if self.RTL:
                res = '\N{LRI}' + res + '\N{PDI}'

        return res

    def format_niftimal_number(self,
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        niftimal_places: str | int | Decimal | SezimalInteger = 2,
        use_group_separator: bool = True,
        use_subgroup_separator: bool = False,
        use_fraction_group_separator: bool = False,
        use_fraction_subgroup_separator: bool = False,
        regularized_digits: bool = True,
        regularized_letter_digits: bool = False,
        sezimal_digits: bool = False,
        sezimal_punctuation: bool = False,
        financial_digits: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        recurring_digits_notation: bool | str | int | Decimal | Sezimal | SezimalInteger = False,
        native_digits: bool = True,
    ) -> str:
        group_separator = self.GROUP_SEPARATOR if use_group_separator else ''
        subgroup_separator = self.SUBGROUP_SEPARATOR if use_subgroup_separator else ''
        fraction_group_separator = self.FRACTION_GROUP_SEPARATOR if use_fraction_group_separator else ''
        fraction_subgroup_separator = self.FRACTION_SUBGROUP_SEPARATOR if use_fraction_subgroup_separator else ''

        if recurring_digits_notation and isinstance(recurring_digits_notation, bool):
            recurring_digits_notation = self.RECURRING_DIGITS_NOTATION

        res = niftimal_format(
            number, niftimal_places, self.SEZIMAL_SEPARATOR,
            group_separator, subgroup_separator,
            fraction_group_separator, fraction_subgroup_separator,
            regularized_digits,
            regularized_letter_digits,
            sezimal_digits,
            sezimal_punctuation,
            financial_digits,
            typographical_negative,
            minimum_size,
            prefix,
            suffix,
            positive_format,
            negative_format,
            recurring_digits_notation,
        )

        if (not sezimal_digits) and native_digits and self.DIGITS:
            res = self.digit_replace(res)

            if self.RTL:
                res = '\N{LRI}' + res + '\N{PDI}'

        return res

    def format_currency(self,
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction | SezimalDecimalUnit,
        sezimal_places: str | int | Decimal | SezimalInteger = None,
        decimal_places: str | int | Decimal | SezimalInteger = None,
        use_group_separator: bool = True,
        use_subgroup_separator: bool = False,
        sezimal_digits: bool = False,
        sezimal_punctuation: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        unit_symbol: str = None,
        subunit_symbol: str = None,
        grouping_digits: int = 3,
        native_digits: bool = True,
        long_format: bool = False,
        **kwargs
    ) -> str:
        group_separator = self.GROUP_SEPARATOR if use_group_separator else ''
        subgroup_separator = self.SUBGROUP_SEPARATOR if use_subgroup_separator else ''

        if type(number) != SezimalDecimalUnit:
            number = SezimalDecimalUnit(number)

        unit_symbol = unit_symbol or self.CURRENCY_UNIT_SYMBOL
        subunit_symbol = subunit_symbol or self.CURRENCY_SUBUNIT_SYMBOL

        if not decimal_places:
            decimal_places = self.CURRENCY_SUBUNIT_DECIMAL_SIZE

        if not sezimal_places:
            sezimal_places = len(str(SezimalInteger(14) ** decimal_places))

        unit = sezimal_format(
            number.unit, 0, self.SEZIMAL_SEPARATOR,
            group_separator, subgroup_separator, '', '',
            sezimal_digits, sezimal_punctuation, typographical_negative,
            minimum_size,
            grouping_digits=grouping_digits,
        )

        if not sezimal_places:
            minimum_size = 0
        else:
            minimum_size = '0' * int(sezimal_places)
            minimum_size += 'X'

        subunit = sezimal_format(
            number.subunit, 0, self.SEZIMAL_SEPARATOR,
            group_separator, subgroup_separator, '', '',
            sezimal_digits, sezimal_punctuation, typographical_negative,
            minimum_size,
            grouping_digits=grouping_digits,
        )

        if long_format:
            final_format = self.CURRENCY_LONG_FORMAT
        else:
            final_format = self.CURRENCY_SHORT_FORMAT

        if sezimal_punctuation:
            final_format = final_format.replace(
                self.CURRENCY_SEPARATOR,
                SEPARATOR_DECIMAL_CURRENCY,
            )

        res = eval(f"f'{final_format}'")

        if (not sezimal_digits) and native_digits and self.DIGITS:
            res = self.digit_replace(res)

            if self.RTL:
                res = '\N{LRI}' + res + '\N{PDI}'

        return res

    @property
    def sort_key(self) -> callable:
        #
        # Let’s try ICU first
        #
        try:
            import icu

            if self.COLLATION_RULES:
                rules = self.COLLATION_RULES

            else:
                loc = icu.Locale(self.LANG)
                col = icu.Collator.createInstance(loc)
                rules = col.getRules()

            rules += self.SEZIMAL_COLLATION_RULES

            collator = icu.RuleBasedCollator(rules)

            return collator.getSortKey

        except:
            pass

        return system_locale.strxfrm

    def moon_phase(self, phase_name: str) -> str:
        if (not phase_name) or (type(phase_name) != str):
            return ''

        if phase_name not in self.MOON_PHASE:
            return ''

        return self.MOON_PHASE[phase_name]

    def digit_replace(self, text: str) -> str:
        if self.DIGITS:
            for i in range(len(self.DIGITS)):
                text = text.replace(str(i), self.DIGITS[i])

        return text

    def strip_unprintable_combining(self, text: str, ideographic: bool = False) -> str:
        if not text:
            return text

        #
        # Let’s strip the most common unprintable characters,
        # and combining diacritics, so that centre, ljust, rjust
        # work as expected
        #
        text = text.translate(UNPRINTABLE_CHARACTERS)
        text = text.translate(EMOJI_CHARACTERS)

        if self.IDEOGRAPHIC or ideographic:
            text = text.translate(IDEOGRAPHIC_CHARACTERS)

        return text

    def _size_difference(self, text: str, ideographic: bool = False) -> SezimalInteger:
        cleaned_text = self.strip_unprintable_combining(text, ideographic)

        size_difference = len(text) - len(cleaned_text)

        return SezimalInteger(Decimal(str(size_difference)))

    def center(self, text: str, size: str | int | float | Decimal | SezimalInteger | Sezimal | SezimalFraction, fill_char: str = ' ', ideographic: bool = False) -> str:
        size += self._size_difference(text, ideographic)
        return text.center(int(size.decimal), fill_char)

    def ljust(self, text: str, size: str | int | float | Decimal | SezimalInteger | Sezimal | SezimalFraction, fill_char: str = ' ', ideographic: bool = False) -> str:
        size += self._size_difference(text, ideographic)
        return text.ljust(int(size.decimal), fill_char)

    def rjust(self, text: str, size: str | int | float | Decimal | SezimalInteger | Sezimal | SezimalFraction, fill_char: str = ' ', ideographic: bool = False) -> str:
        size += self._size_difference(text, ideographic)
        return text.rjust(int(size.decimal), fill_char)

    def zfill(self, text: str, size: str | int | float | Decimal | SezimalInteger | Sezimal | SezimalFraction, fill_char: str = '0', ideographic: bool = False) -> str:
        size += self._size_difference(text, ideographic)
        return text.rjust(int(size.decimal), fill_char)

    def len(self, text: str, ideographic: bool = False) -> SezimalInteger:
        size = SezimalInteger(Decimal(str(len(text)))) - self._size_difference(text, ideographic)
        return size

    def slice(self, text: str, start: str | int | float | Decimal | SezimalInteger | Sezimal | SezimalFraction = 0, finish: str | int | float | Decimal | SezimalInteger | Sezimal | SezimalFraction = None) -> str:
        if start is None:
            start = SezimalInteger(0)

        if finish is None:
            finish = self.len(text)

        start = SezimalInteger(start)
        finish = SezimalInteger(finish)
        max_size = finish - start

        if start < 0:
            start = self.len(text) + start

        if finish < 0:
            finish = self.len(text) + finish

        sliced_text = ''

        j = start
        size = SezimalInteger(0)

        while size < max_size and j.decimal < len(text):
            c = text[int(j.decimal)]
            sliced_text += c
            size += 1
            j += 1

            while j.decimal < len(text) \
                and self.strip_unprintable_combining(c) == '':
                c = text[int(j.decimal)]
                sliced_text += c
                j += 1

        #
        # If the next character is unprintable, get it too
        #
        if len(text) > int(j.decimal):
            c = text[int(j.decimal)]

            if self.strip_unprintable_combining(c) == '':
                sliced_text += c

        return sliced_text

    UPPERCASE_MAPPING = {}
    LOWERCASE_MAPPING = {}
    TITLE_ALWAYS_LOWERCASE_WORDS = []
    TITLE_ALWAYS_UPPERCASE_WORDS = []

    def upper(self, text: str) -> str:
        return text.translate(self.UPPERCASE_MAPPING).upper()

    def lower(self, text: str) -> str:
        return text.translate(self.LOWERCASE_MAPPING).lower()

    def capitalize(self, text: str) -> str:
        if not text:
            return text

        if self.len(text) == 1:
            return self.upper(text)

        return self.upper(text[0]) + self.lower(text[1:])

    def title(self, text: str) -> str:
        if not text:
            return text

        if self.len(text) == 1:
            return self.upper(text)

        text = self.capitalize(text)

        def _apply_title(txt: str, separator: str = ' ') -> str:
            if separator not in txt:
                return txt

            res = []

            for part in txt.split(separator):
                if not part:
                    res.append(part)
                    continue

                if self.lower(part) in self.TITLE_ALWAYS_LOWERCASE_WORDS:
                    res.append(self.lower(part))
                    continue

                if self.upper(part) in self.TITLE_ALWAYS_UPPERCASE_WORDS:
                    res.append(self.upper(part))
                    continue

                res.append(self.capitalize(part))

            return separator.join(res)

        text = _apply_title(text, ' ')
        text = _apply_title(text, ' ')
        text = _apply_title(text, "'")
        text = _apply_title(text, '’')

        return text

    def spellout(self, number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction, lang: str = None) -> str:
        number = str(number)

        if lang is None:
            lang = self.LANG

        return sezimal_spellout(number, lang)

    @property
    def POSIX_CODE(self):
        parts = self.__class__.__name__.replace('SezimalLocale', '').split('_')

        if len(parts) == 1:
            return parts[0].lower()

        #
        # Presume that the 2 characters are a country code
        #
        if len(parts[1]) == 2:
            name = parts[0].lower() + '_' + parts[1]

            if len(parts) > 2:
                name += '@' + '_'.join(parts[2:]).capitalize()

            return name

        if len(parts) == 2:
            return parts[0].lower() + '@' + parts[1].capitalize()

        return '_'.join(parts)

    CALENDAR = ''

    @property
    def LANGUAGE_TAG(self):
        parts = self.__class__.__name__.replace('SezimalLocale', '').split('_')

        if len(parts) == 1:
            lt = parts[0].lower()

        #
        # Presume that the 2 characters are a country code
        #
        elif len(parts[1]) == 2:
            name = parts[0].lower()

            if len(parts) > 2:
                if parts[-2] == 'NU' and parts[-1] == 'LATN':
                    if parts[1] == 'NU':
                        name += '-u-nu-Latn'
                    else:
                        name += '-' + '-'.join(parts[2:]).capitalize() + '-u-nu-Latn'

                else:
                    name += '-' + '-'.join(parts[2:]).capitalize()

            else:
                name += '-' + parts[1]

            lt = name

        elif len(parts) == 2:
            lt = parts[0].lower() + '-' + parts[1].capitalize()

        else:
            lt = '-'.join(parts)

        if self.CALENDAR:
            lt += '-x-ca-' + self.CALENDAR

        return lt

    JEWISH_CALENDAR_MONTH_NAME = [
        # 'Nisan ניסן',
        # 'Iyyar אייר‎',
        # 'Sivan סיון‎',
        # 'Tammuz תמוז‎',
        # 'Av אב',
        # 'Elul אלול‎',
        # 'Tishri תשרי‎',
        # 'Heshvan חשוון',
        # 'Kislev כסלו',
        # 'Tevet טבת',
        # 'Shevat שבט',
        # 'Adar אדר',
        # 'Adar bet אדר ב׳',
        'Nisan',
        'Iyyar',
        'Sivan',
        'Tammuz',
        'Av',
        'Elul',
        'Tishri',
        'Heshvan',
        'Kislev',
        'Tevet',
        'Shevat',
        'Adar',
        'Adar bet',
    ]

    JEWISH_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Nis',
        'Iyy',
        'Siv',
        'Tam',
        'Av',
        'Elu',
        'Tis',
        'Hes',
        'Kis',
        'Tev',
        'She',
        'Ada',
        'Ad2',
    ]

    HIJRI_CALENDAR_MONTH_NAME = [
        # 'Al-muḥarram المحرم',
        # 'Ṣafar صفر',
        # 'Rabīʿ al-ʾawwal ربيع الأول',
        # 'Rabīʿ al-ʾākhir ربيع الآخر',
        # 'Jumādā al-ʾūlā جمادى الأولى',
        # 'Jumādā al-ʾākhirah جمادى الآخرة',
        # 'Rajab رجب',
        # 'Shaʿbān شعبان',
        # 'Ramaḍān رمضان',
        # 'Shawwāl شوال',
        # 'Ḏū al-qaʿdah ذو القعدة',
        # 'Ḏū al-ḥijjah ذو الحجة',
        'Muḥarram',
        'Ṣafar',
        'Rabīʿ I',
        'Rabīʿ II',
        'Jumādā I',
        'Jumādā II',
        'Rajab',
        'Shaʿbān',
        'Ramaḍān',
        'Shawwāl',
        'Ḏū al-Qiʿdah',
        'Ḏū al-Ḥijjah',
    ]

    HIJRI_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Muḥ',
        'Ṣaf',
        'Rb1',
        'Rb2',
        'Jm1',
        'Jm2',
        'Raj',
        'Shaʿ',
        'Ram',
        'Sha',
        'ḎQʿ',
        'ḎḤj',
    ]

    IRANIAN_CALENDAR_MONTH_NAME = [
        'Farvardin فروردین',
        'Ordibehesht اردیبهشت',
        'Khordad خرداد',
        'Tir تیر',
        'Mordad مرداد',
        'Shahrivar شهریور',
        'Mehr مهر',
        'Aban آبان',
        'Azar آذر',
        'Dey دی',
        'Bahman بهمن',
        'Esfand اسفند',
    ]

    IRANIAN_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Far',
        'Ord',
        'Kho',
        'Tir',
        'Mor',
        'Sha',
        'Meh',
        'Aba',
        'Aza',
        'Dey',
        'Bah',
        'Esf',
    ]

    INDIAN_CALENDAR_MONTH_NAME = [
        'Caitra चैत्र',
        'Vaiśākha वैशाख',
        'Jyeṣṭha ज्येष्ठ',
        'Āṣāḍha आषाढ',
        'Śrāvaṇa श्रावण',
        'Bhādrapada भाद्रपद',
        'Aśvin अश्विन्',
        'Kārtika कार्तिक',
        'Agrahāyaṇa अग्रहायण',
        'Pauṣa पौष',
        'Māgha माघ',
        'Phālguna फाल्गुन',
    ]

    INDIAN_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Cai',
        'Vai',
        'Jye',
        'Āṣā',
        'Śrā',
        'Bhā',
        'Aśv',
        'Kār',
        'Agr',
        'Pau',
        'Māg',
        'Phā',
    ]

    CALENDAR_TYPE = {
        #
        # Civil calendars
        #
        'SEZ': 'Sezimal',
        'SYM': 'Symmetry454',
        'ISO': 'ISO / Gregorian',
        'ISR': 'Israeli',
        'IND': 'Indian National',

        #
        # Religious calendars
        #
        'JUL': 'Orthodox (Julian)',
        'JEW': 'Jewish',
        'HIJ': 'Islamic (Hijri)',
        'IRN': 'Iranian (Solar Hijri)',

        #
        # Easter referencial
        #
        'SEZ+EASTER': 'Sezimal Fixed Easter - 11th of April',
        'SYM+EASTER': 'Symmetry454 Fixed Easter - 7th of April',
        'ISO+EASTER': 'Easter (Gregorian)',
        'JUL+EASTER': 'Orthodox Easter (Julian)',
        'JEW+EASTER': 'Pesach (Passover)',
    }

    CALENDAR_DATE_ERROR = 'Invalid date for the {calendar_type} calendar'
    CALENDAR_TIME_ERROR = 'Invalid time'
    CALENDAR_TIME_AFTER_ERROR = 'Invalid time: event finishing time cannot come before the starting time'

    @property
    def HOUR_FORMAT(self) -> str:
        if hasattr(self, '_hour_format'):
            return self._hour_format

        if '%P' in self.ISO_TIME_FORMAT.upper():
            return '12h'

        return '24h'

    @HOUR_FORMAT.setter
    def HOUR_FORMAT(self, value):
        self._hour_format = value

    def to_short_year_format(self):
        if self.ISO_MODE:
            return

        def _to_short_year_format(fmt) -> str:
            fmt = fmt.replace('#Y', '#>Y')
            fmt = fmt.replace('#!Y', '#!>Y')
            fmt = fmt.replace('#?Y', '#?>Y')
            fmt = fmt.replace('#X', '#>X')
            fmt = fmt.replace('#!X', '#!>X')
            fmt = fmt.replace('#?X', '#?>X')
            fmt = fmt.replace('#y', '#>y')
            fmt = fmt.replace('#!y', '#!>y')
            fmt = fmt.replace('#?y', '#?>y')
            return fmt

        self.DATE_FORMAT = _to_short_year_format(self.DATE_FORMAT)
        self.DATE_LONG_FORMAT = _to_short_year_format(self.DATE_LONG_FORMAT)
        self.DATE_TIME_FORMAT = _to_short_year_format(self.DATE_TIME_FORMAT)
        self.DATE_TIME_LONG_FORMAT = _to_short_year_format(self.DATE_TIME_LONG_FORMAT)

        try:
            self.YEAR_TEXT_MONTH_FORMAT = _to_short_year_format(self.YEAR_TEXT_MONTH_FORMAT)
        except:
            pass

    def _to_other_base(self, base: int, fmt: str = None,
        sezimal_digits: bool = False, text_digits: bool = False) -> str | None:
        def _to_decimal_format(fmt) -> str:
            fmt = fmt.replace('#d', '#9d')
            fmt = fmt.replace('#?d', '#9?d')
            fmt = fmt.replace('#-d', '#9-d')
            fmt = fmt.replace('#?-d', '#9?-d')
            fmt = fmt.replace('#m', '#9m')
            fmt = fmt.replace('#?m', '#9?m')
            fmt = fmt.replace('#Y', '#9sy')
            fmt = fmt.replace('#?Y', '#9?sy')
            fmt = fmt.replace('#y', '#9sy')
            fmt = fmt.replace('#?y', '#9?sy')
            fmt = fmt.replace('#M', '#9M')
            fmt = fmt.replace('#wY', '#9wY')
            fmt = fmt.replace('#w', '#9w')
            fmt = fmt.replace('#X', '#9sy')
            fmt = fmt.replace('#>Y', '#9sy')
            fmt = fmt.replace('#?>Y', '#9?sy')
            fmt = fmt.replace('#>X', '#9sy')
            fmt = fmt.replace('#?>X', '#9?sy')
            fmt = fmt.replace('#>y', '#9sy')
            fmt = fmt.replace('#?>y', '#9?sy')
            return fmt

        def _to_dozenal_format(fmt: str) -> str:
            return _to_decimal_format(fmt).replace('9', '↋')

        def _to_sezimal_digits_format(fmt: str) -> str:
            fmt = fmt.replace('#?', '#')
            fmt = fmt.replace('#d', '#!d')
            fmt = fmt.replace('#-d', '#!-d')
            fmt = fmt.replace('#m', '#!m')
            fmt = fmt.replace('#Y', '#!Y')
            fmt = fmt.replace('#y', '#!y')
            fmt = fmt.replace('#wY', '#!wY')
            fmt = fmt.replace('#w', '#!w')
            fmt = fmt.replace('#X', '#!X')

            fmt = fmt.replace('#>Y', '#!>Y')
            fmt = fmt.replace('#>X', '#!>X')
            fmt = fmt.replace('#>y', '#!>y')

            fmt = fmt.replace('#u', '#!u')
            fmt = fmt.replace('#p', '#!p')
            fmt = fmt.replace('#a', '#!a')
            fmt = fmt.replace('#n', '#!n')
            fmt = fmt.replace('#b', '#!b')
            fmt = fmt.replace('#e', '#!e')
            fmt = fmt.replace('#-u', '#!-u')
            fmt = fmt.replace('#-p', '#!-p')
            fmt = fmt.replace('#-a', '#!-a')
            fmt = fmt.replace('#-n', '#!-n')
            fmt = fmt.replace('#-b', '#!-b')
            fmt = fmt.replace('#-e', '#!-e')

            return fmt

        def _to_niftimal_format(fmt: str) -> str:
            fmt = _to_sezimal_digits_format(fmt)

            if sezimal_digits:
                fmt = fmt.replace('!', '@!')
            elif text_digits:
                fmt = fmt.replace('!', 'Z')
            else:
                fmt = fmt.replace('!', '@')

            return fmt

        if base == 10:
            conversion_function = _to_sezimal_digits_format
        elif base == 14:
            conversion_function = _to_decimal_format
        elif base == 20:
            conversion_function = _to_dozenal_format
        elif base == 100:
            conversion_function = _to_niftimal_format

        if fmt:
            return conversion_function(fmt)

        self.DATE_FORMAT = conversion_function(self.DATE_FORMAT)
        self.DATE_LONG_FORMAT = conversion_function(self.DATE_LONG_FORMAT)
        self.DATE_TIME_FORMAT = conversion_function(self.DATE_TIME_FORMAT)
        self.DATE_TIME_LONG_FORMAT = conversion_function(self.DATE_TIME_LONG_FORMAT)

        try:
            self.YEAR_TEXT_MONTH_FORMAT = conversion_function(self.YEAR_TEXT_MONTH_FORMAT)
        except:
            pass

        if base == 10:
            self.TIME_FORMAT = conversion_function(self.TIME_FORMAT)
            self.DIGITS = []

        elif base == 100:
            self.TIME_FORMAT = conversion_function(self.TIME_FORMAT)
            self.DIGITS = []

        elif base == 14:
            self.DATE_TIME_FORMAT = self.DATE_TIME_FORMAT.replace(self.TIME_FORMAT, self.ISO_TIME_FORMAT)
            self.DATE_TIME_LONG_FORMAT = self.DATE_TIME_LONG_FORMAT.replace(self.TIME_FORMAT, self.ISO_TIME_FORMAT)
            self.TIME_FORMAT = self.ISO_TIME_FORMAT

        elif base == 20:
            self.DIGITS = []
            self.DATE_TIME_FORMAT = self.DATE_TIME_FORMAT.replace(self.TIME_FORMAT, '#3.2fD')
            self.DATE_TIME_LONG_FORMAT = self.DATE_TIME_LONG_FORMAT.replace(self.TIME_FORMAT, '#3.2fD')
            self.TIME_FORMAT = '#3.2fD'

        if base == 14 or base == 20:
            self.MONTH_NAME = self.ISO_MONTH_NAME
            self.MONTH_ABBREVIATED_NAME = self.ISO_MONTH_ABBREVIATED_NAME

    def to_decimal_base(self):
        self._to_other_base(14)

    def to_dozenal_base(self):
        self._to_other_base(20)

    def to_niftimal_base(self, sezimal_digits: bool = False):
        self._to_other_base(100, sezimal_digits=sezimal_digits)

    def to_niftimal_text_base(self):
        self._to_other_base(100, text_digits=True)

    def to_sezimal_digits(self):
        self._to_other_base(10, sezimal_digits=True)

    def to_iso_format(self):
        self.DATE_SEPARATOR = '-'
        self.TIME_SEPARATOR = ':'
        self.GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
        self.FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
        self.ISO_MODE = True

        self.DATE_FORMAT = '#Y-#m-#d'
        self.DATE_LONG_FORMAT = '#Y-#m-#d'
        self.TIME_FORMAT = '#u:#p:#a'
        self.ISO_TIME_FORMAT = '%H:%M:%S'

    CHRISTIAN_HOLIDAYS = [
        ('CHR+01-01',     '🕆\ufe0f Solemnity of Mary, Mother of God'),
        ('CHR+01-06',     '🕆\ufe0f Epiphany'),
        ('CHR+01-06+SUN', '🕆\ufe0f Baptism of the Lord'),
        ('CHR+02-02',     '🕆\ufe0f Candlemas'),
        ('CHR+EASTER-124', '🕆\ufe0f Fat Thursday'),
        ('CHR+EASTER-120', '🕆\ufe0f Shrove Monday'),
        ('CHR+EASTER-115', '🕆\ufe0f Shrove Tuesday'),
        ('CHR+EASTER-114', '🕆\ufe0f Ash Wednesday'),
        ('CHR+EASTER-11',  '🕆\ufe0f Palm Sunday'),
        ('CHR+EASTER-4',   '🕆\ufe0f Holy Wednesday'),
        ('CHR+EASTER-3',   '🕆\ufe0f Maundy Thursday'),
        ('CHR+EASTER-2',   '🕆\ufe0f🥀\ufe0f Good Friday'),
        ('CHR+EASTER-1',   '🕆\ufe0f Holy Saturday'),
        ('CHR+EASTER',     '🕆\ufe0f🐣\ufe0f🌱\ufe0f Easter'),
        ('CHR+EASTER+1',   '🕆\ufe0f Easter Monday'),
        ('CHR+EASTER+11',  '🕆\ufe0f Divine Mercy Sunday'),
        ('CHR+EASTER+103', '🕆\ufe0f Ascension of Jesus'),
        ('CHR+EASTER+121', '🕆\ufe0f Pentecost'),
        ('CHR+EASTER+122', '🕆\ufe0f Whit Monday'),
        ('CHR+EASTER+132', '🕆\ufe0f🛆 Trinity Sunday'),
        ('CHR+EASTER+140', '🕆\ufe0f🥖\ufe0f🍷\ufe0f Corpus Christi'),
        ('CHR+11-01',      '🕆\ufe0f All Saint’s'),
        ('CHR+11-02',      '🕆\ufe0f All Soul’s'),
        ('CHR+12-25-SUN_4','🕆\ufe0f Advent'),
        ('CHR+12-25',      '🕆\ufe0f🌟\ufe0f👼\ufe0f🏼\ufe0f Christmas'),
    ]

    JEWISH_HOLIDAYS = [
        ('JEW+11-15', '🌳\ufe0f💮\ufe0f Tu biShvat'),
        # ('JEW+12-14', '🍷\ufe0f🍬\ufe0f Purim'),  # Adar bet (13) in leap years, Adar (12) in regular years
        ('JEW+13-14', '🍷\ufe0f🍬\ufe0f Purim'),  # Adar bet (13) in leap years, Adar (12) in regular years
        ('JEW+01-15', '🐑\ufe0f🫓\ufe0f Pesach'),
        ('JEW+02-14', '🐑\ufe0f🫓\ufe0f Pesach Sheni'),
        ('JEW+02-18', '🔥\ufe0f Lag baOmer'),
        ('JEW+03-06', '💐\ufe0f📜\ufe0f Shavuot'),
        ('JEW+05-09', '🕍\ufe0f🔥\ufe0f Tisha b’Av'),

        ('JEW+07-01', '🍎\ufe0f🍯\ufe0f Rosh haShaná'),
        ('JEW+07-10', '🤍\ufe0f🙏🏻\ufe0f Yom Kippur'),
        ('JEW+07-15', '🍋\ufe0f⛺\ufe0f Sukkot'),
        ('JEW+07-22', '🙏🏻\ufe0f🌧\ufe0f️ Shemini Atzeret'),
        ('JEW+07-23', '😊📜\ufe0f Simchat Torah'),
        ('JEW+09-25', '🕯\ufe0f🕍\ufe0f Hanukkah'),
    ]

    ISLAMIC_HOLIDAYS = [
        ('HIJ+09-01', '🍯\ufe0f🥙\ufe0f 1st day of Ramaḍān'),
        ('HIJ+09-30', '🍯\ufe0f🥙\ufe0f Laylat ul-Jāʾizah'),
        ('HIJ+10-01-FRI', '🍯\ufe0f🥙\ufe0f Jumuʿat ul-Widāʿ'),
        ('HIJ+10-01', '🍯\ufe0f🥙\ufe0f ʻĪd ul-Fiṭr'),
        ('HIJ+12-10', '🐑\ufe0f🕋\ufe0f ʿĪd ul-ʾAḍḥā'),
    ]
