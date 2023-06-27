
from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')

import locale as system_locale

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from ..base import SEPARATOR_COMMA, SEPARATOR_UNDERSCORE, \
    sezimal_format, decimal_format


class SezimalLocale:
    LANG = 'en'
    LANGUAGE = 'English'

    #
    # Number formatting
    #
    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_UNDERSCORE
    FRACTION_SUBGROUP_SEPARATOR = ''

    #
    # Date and time
    #
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
        'spring_cross_quarter': '\ufe0f❄️ \ufe0f〰\ufe0f🌱',
        'spring_equinox': '\ufe0f🌱',
        'summer_cross_quarter': '\ufe0f🌱\ufe0f〰\ufe0f🌞',
        'summer_solstice': '\ufe0f🌞',
        'autumn_cross_quarter': '\ufe0f🌞\ufe0f〰\ufe0f🍂',
        'autumn_equinox': '\ufe0f🍂',
        'winter_cross_quarter': '\ufe0f🍂\ufe0f〰\ufe0f❄️ ',
        'winter_solstice': '\ufe0f❄️ ',
    }

    SEASON_EMOJI_SOUTHERN_HEMISPHERE = {
        'autumn_cross_quarter': '\ufe0f🌞\ufe0f〰\ufe0f🍃',
        'autumn_equinox': '\ufe0f🍃',
        'winter_cross_quarter': '\ufe0f🍃\ufe0f〰\ufe0f❄️ ',
        'winter_solstice': '\ufe0f❄️ ',
        'spring_cross_quarter': '\ufe0f❄️ \ufe0f〰\ufe0f🌺',
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

    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'

    #
    # Collation rules
    #
    COLLATION_RULES = ''
    SEZIMAL_COLLATION_RULES = '''
&0<1<2<3<4<5<6<7<8<9<↊<↋<0̈<1̈<2̈<3̈<4̈<5̈<0̄<1̄<2̄<3̄<4̄<5̄<0̄̇<1̄̇<2̄̇<3̄̇<4̄̇<5̄̇<0̄̈<1̄̈<2̄̈<3̄̈<4̄̈<5̄̈
&0<<󱨀<<<⁰<<󱨤<<<₀<<󱩈
&1<<󱨁<<<¹<<󱨥<<<₁<<󱩉
&2<<󱨂<<<²<<󱨦<<<₂<<󱩊
&3<<󱨃<<<³<<󱨧<<<₃<<󱩋
&4<<󱨄<<<⁴<<󱨨<<<₄<<󱩌
&5<<󱨅<<<⁵<<󱨩<<<₅<<󱩍
&6<<0̇<<󱨆<<󱨀̇<<<⁶<<⁰̇<<󱨪<<󱨤̇<<<₆<<₀̇<<󱩎<<󱩈̇
&7<<1̇<<󱨇<<󱨁̇<<<⁷<<¹̇<<󱨫<<󱨥̇<<<₇<<₁̇<<󱩏<<󱩉̇
&8<<2̇<<󱨈<<󱨂̇<<<⁸<<²̇<<󱨬<<󱨦̇<<<₈<<₂̇<<󱩐<<󱩊̇
&9<<3̇<<󱨉<<󱨃̇<<<⁹<<³̇<<󱨭<<󱨧̇<<<₉<<₃̇<<󱩑<<󱩋̇
&↊<<4̇<<󱨊<<󱨄̇<<<⁴̇<<󱨮<<󱨨̇<<<₄̇<<󱩒<<󱩌̇
&↋<<5̇<<󱨋<<󱨅̇<<<⁵̇<<󱨯<<󱨩̇<<<₅̇<<󱩓<<󱩍̇
&0̈<<󱨌<<󱨀̈<<<⁰̈<<󱨰<<󱨤̈<<<₀̈<<󱩔<<󱩈̈
&1̈<<󱨍<<󱨁̈<<<¹̈<<󱨱<<󱨥̈<<<₁̈<<󱩕<<󱩉̈
&2̈<<󱨎<<󱨂̈<<<²̈<<󱨲<<󱨦̈<<<₂̈<<󱩖<<󱩊̈
&3̈<<󱨏<<󱨃̈<<<³̈<<󱨳<<󱨧̈<<<₃̈<<󱩗<<󱩋̈
&4̈<<󱨐<<󱨄̈<<<⁴̈<<󱨴<<󱨨̈<<<₄̈<<󱩘<<󱩌̈
&5̈<<󱨑<<󱨅̈<<<⁵̈<<󱨵<<󱨩̈<<<₅̈<<󱩙<<󱩍̈
&0̄<<󱨒<<󱨀̄<<<⁰̄<<󱨶<<󱨤̄<<<₀̄<<󱩚<<󱩈̄
&1̄<<󱨓<<󱨁̄<<<¹̄<<󱨷<<󱨥̄<<<₁̄<<󱩛<<󱩉̄
&2̄<<󱨔<<󱨂̄<<<²̄<<󱨸<<󱨦̄<<<₂̄<<󱩜<<󱩊̄
&3̄<<󱨕<<󱨃̄<<<³̄<<󱨹<<󱨧̄<<<₃̄<<󱩝<<󱩋̄
&4̄<<󱨖<<󱨄̄<<<⁴̄<<󱨺<<󱨨̄<<<₄̄<<󱩞<<󱩌̄
&5̄<<󱨗<<󱨅̄<<<⁵̄<<󱨻<<󱨩̄<<<₅̄<<󱩟<<󱩍̄
&0̄̇<<󱨘<<󱨀̄̇<<<⁰̄̇<<󱨼<<󱨤̄̇<<<₀̄̇<<󱩠<<󱩈̄̇
&1̄̇<<󱨙<<󱨁̄̇<<<¹̄̇<<󱨽<<󱨥̄̇<<<₁̄̇<<󱩡<<󱩉̄̇
&2̄̇<<󱨚<<󱨂̄̇<<<²̄̇<<󱨾<<󱨦̄̇<<<₂̄̇<<󱩢<<󱩊̄̇
&3̄̇<<󱨛<<󱨃̄̇<<<³̄̇<<󱨿<<󱨧̄̇<<<₃̄̇<<󱩣<<󱩋̄̇
&4̄̇<<󱨜<<󱨄̄̇<<<⁴̄̇<<󱩀<<󱨨̄̇<<<₄̄̇<<󱩤<<󱩌̄̇
&5̄̇<<󱨝<<󱨅̄̇<<<⁵̄̇<<󱩁<<󱨩̄̇<<<₅̄̇<<󱩥<<󱩍̄̇
&0̄̈<<󱨞<<󱨀̄̈<<<⁰̄̈<<󱩂<<󱨤̄̈<<<₀̄̈<<󱩦<<󱩈̄̈
&1̄̈<<󱨟<<󱨁̄̈<<<¹̄̈<<󱩃<<󱨥̄̈<<<₁̄̈<<󱩧<<󱩉̄̈
&2̄̈<<󱨠<<󱨂̄̈<<<²̄̈<<󱩄<<󱨦̄̈<<<₂̄̈<<󱩨<<󱩊̄̈
&3̄̈<<󱨡<<󱨃̄̈<<<³̄̈<<󱩅<<󱨧̄̈<<<₃̄̈<<󱩩<<󱩋̄̈
&4̄̈<<󱨢<<󱨄̄̈<<<⁴̄̈<<󱩆<<󱨨̄̈<<<₄̄̈<<󱩪<<󱩌̄̈
&5̄̈<<󱨣<<󱨅̄̈<<<⁵̄̈<<󱩇<<󱨩̄̈<<<₅̄̈<<󱩫<<󱩍̄̈
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
        dedicated_digits: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
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
            minimum_size,
            prefix,
            suffix,
            positive_format,
            negative_format,
        )

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
    ) -> str:
        group_separator = self.GROUP_SEPARATOR if use_group_separator else ''
        fraction_group_separator = self.FRACTION_GROUP_SEPARATOR if use_fraction_group_separator else ''

        return decimal_format(
            number, decimal_places, self.SEZIMAL_SEPARATOR,
            group_separator, fraction_group_separator,
            typographical_negative,
            minimum_size,
            prefix,
            suffix,
            positive_format,
            negative_format,
        )

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

            return collator.collator.getSortKey

        except:
            pass

        return system_locale.strxfrm

    def moon_phase(self, phase_name: str) -> str:
        if (not phase_name) or (type(phase_name) != str):
            return ''

        if phase_name not in self.MOON_PHASE:
            return ''

        return self.MOON_PHASE[phase_name]
