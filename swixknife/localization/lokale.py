
from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')

import itertools
import locale as system_locale

from decimal import Decimal

from .constants import UNPRINTABLE_CHARACTERS, EMOJI_CHARACTERS, IDEOGRAPHIC_CHARACTERS
from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..functions import SezimalRange
from ..base import SEPARATOR_COMMA, SEPARATOR_UNDERSCORE, \
    SEPARATOR_COMBINING_DOT_ABOVE_RIGHT, \
    RECURRING_DIGITS_NOTATION_SIMPLE, \
    sezimal_format, decimal_format, dozenal_format, \
    niftimal_format
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
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

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

    DATE_FORMAT = '#Y-#m-#d'
    DATE_LONG_FORMAT = '#Y-#m-#d #@W'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#Y-#m-#d #@W #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#Y-#m-#d #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'
    DST_EMOJI = '‍\ufe0f⏰   \ufe0f🌞'

    @property
    def ISO_DATE_FORMAT(self):
        res = self.DATE_FORMAT

        for separator in (
            '_', '.', ',', '˙', 'ʼ',
            '’', "'", '•', '◦', '\u0020', '\u00a0',
            '\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005',
            '\u2006', '\u2007', '\u2008', '\u2009', '\u200a', '\u202f',
            '\u205f', '\U000f1e6c', '\U000f1e6d', '\U000f1e6e', '\U000f1e6f',
            '',
        ):
            res = res.replace(f'#{separator}', '%')

        res = res.replace('y', 'Y')

        return res

    @property
    def ISO_TIME_FORMAT(self):
        itf = self.TIME_FORMAT.replace('#', '%')
        itf = itf.replace('u', 'H')
        itf = itf.replace('p', 'M')
        itf = itf.replace('a', 'S')
        return itf

    @property
    def DATE_SEPARATOR(self):
        if not self.DATE_FORMAT:
            return ''

        separator = self.DATE_FORMAT.lower().replace('#', '')
        separator = separator.replace('?', '')
        separator = separator.replace('!', '')
        separator = separator.replace('y', '')
        separator = separator.replace('m', '')
        separator = separator.replace('d', '')

        if not separator:
            return ''

        return separator[0]

    @property
    def TIME_SEPARATOR(self):
        if not self.TIME_SEPARATOR:
            return ''

        separator = self.TIME_FORMAT.lower().replace('#', '')
        separator = separator.replace('?', '')
        separator = separator.replace('!', '')
        separator = separator.replace('u', '')
        separator = separator.replace('p', '')
        separator = separator.replace('a', '')

        if not separator:
            return ''

        return separator[0]

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'UTC'

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
        'spring_cross_quarter': '\ufe0f❄️\ufe0f〰\ufe0f🌷',
        'spring_equinox': '\ufe0f🌷',
        'summer_cross_quarter': '\ufe0f🌷\ufe0f〰\ufe0f🌞',
        'summer_solstice': '\ufe0f🌞',
        'autumn_cross_quarter': '\ufe0f🌞\ufe0f〰\ufe0f🍂',
        'autumn_equinox': '\ufe0f🍂',
        'winter_cross_quarter': '\ufe0f🍂\ufe0f〰\ufe0f❄️',
        'winter_solstice': '\ufe0f❄️',
    }

    SEASON_EMOJI_SOUTHERN_HEMISPHERE = {
        'autumn_cross_quarter': '\ufe0f🌞\ufe0f〰\ufe0f🍂',
        'autumn_equinox': '\ufe0f🍂',
        'winter_cross_quarter': '\ufe0f🍂\ufe0f〰\ufe0f❄️',
        'winter_solstice': '\ufe0f❄️',
        'spring_cross_quarter': '\ufe0f❄️\ufe0f〰\ufe0f🌺',
        'spring_equinox': '\ufe0f🌺',
        'summer_cross_quarter': '\ufe0f🌺\ufe0f〰\ufe0f🌞',
        'summer_solstice': '\ufe0f🌞',
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
                res = '\N{LRO}' + res + '\N{PDF}'

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
                res = '\N{LRO}' + res + '\N{PDF}'

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
                res = '\N{LRO}' + res + '\N{PDF}'

        return res

    def format_niftimal_number(self,
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        niftimal_places: str | int | Decimal | SezimalInteger = 2,
        use_group_separator: bool = True,
        use_subgroup_separator: bool = False,
        use_fraction_group_separator: bool = False,
        use_fraction_subgroup_separator: bool = False,
        regularized_digits: bool = True,
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
                res = '\N{LRO}' + res + '\N{PDF}'

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

        if start < 0:
            start = self.len(text) + start

        if finish < 0:
            finish = self.len(text) + finish

        sliced_text = ''

        j = start
        for i in SezimalRange(start, finish):
            c = text[int(j.decimal)]
            sliced_text += c
            j += 1

            while self.strip_unprintable_combining(c) == '':
                if len(text) > j.decimal:
                    break

                c = text[int(j.decimal)]
                sliced_text += c
                j += 1

            if int(j.decimal) >= len(text):
                break

        #
        # If the next character is unprintable, get it too
        #
        if len(text) > int(j.decimal):
            c = text[int(j.decimal)]

            if self.strip_unprintable_combining(c) == '':
                sliced_text += c

        return sliced_text

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

    @property
    def LANGUAGE_TAG(self):
        parts = self.__class__.__name__.replace('SezimalLocale', '').split('_')

        if len(parts) == 1:
            return parts[0].lower()

        #
        # Presume that the 2 characters are a country code
        #
        if len(parts[1]) == 2:
            name = parts[0].lower() + '-' + parts[1]

            if len(parts) > 2:
                name += '-' + '-'.join(parts[2:]).capitalize()

            return name

        if len(parts) == 2:
            return parts[0].lower() + '-' + parts[1].capitalize()

        return '-'.join(parts)
