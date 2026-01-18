

__all__ = ('SezimalLocaleVI',)


from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleVI(SezimalLocale):
    LANG = 'vi'
    LANGUAGE = 'Tiếng Việt'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = '₫'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0

    WEEKDAY_NAME = [
        'thứ hai',
        'thứ ba',
        'thứ tư',
        'thứ năm',
        'thứ sáu',
        'thứ bảy',
        'chủ nhật',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Th2',
        'Th3',
        'Th4',
        'Th5',
        'Th6',
        'Th7',
        'CN',
    ]

    WEEKDAY_SYMBOL = [
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        'C',
    ]

    MONTH_NAME= [
        'tháng giêng',
        'tháng hai',
        'tháng ba',
        'tháng tư',
        'tháng năm',
        'tháng sáu',
        'tháng bảy',
        'tháng tám',
        'tháng chín',
        'tháng mười',
        'tháng mười một',
        'tháng mười hai',
    ]

    MONTH_ABBREVIATED_NAME = [
        'thg 1',
        'thg 2',
        'thg 3',
        'thg 4',
        'thg 5',
        # 'thg 6',
        # 'thg 7',
        # 'thg 8',
        # 'thg 9',
        # 'thg 10',
        # 'thg 11',
        # 'thg 12',
        'thg 10',
        'thg 11',
        'thg 12',
        'thg 13',
        'thg 14',
        'thg 15',
        'thg 20',
    ]

    ISO_MONTH_ABBREVIATED_NAME = [
        'thg 1',
        'thg 2',
        'thg 3',
        'thg 4',
        'thg 5',
        'thg 6',
        'thg 7',
        'thg 8',
        'thg 9',
        'thg 10',
        'thg 11',
        'thg 12',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#d/#m/#Y'
    DATE_FULL_FORMAT = '#d/#m/#Y #@W'
    DATE_FULL_LONG_FORMAT = '#d/#m/#Y #W'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d/#m/#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Ho_Chi_Minh'

    SEASON_NAME = {
        'spring_cross_quarter': 'Từ mùa đông sang mùa xuân',
        'spring_equinox': 'Mùa xuân',
        'summer_cross_quarter': 'Từ mùa xuân sang mùa hè',
        'summer_solstice': 'Mùa hè',
        'autumn_cross_quarter': 'Từ mùa hè sang mùa thu',
        'autumn_equinox': 'Mùa thu',
        'winter_cross_quarter': 'Từ mùa thu sang mùa đông',
        'winter_solstice': 'Mùa đông',
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
    ERROR = 'Lỗi'
    WEEKDAY_ERROR = 'Ngày trong tuần không hợp lệ {weekday}'
    MONTH_ERROR = 'Tháng không hợp lệ {month}'
    WEEK_NUMBER_SYMBOL = 'tuần'
    DAY_NUMBER_SYMBOL = 'ngày'

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
        wan_man_van_grouping: bool = True,
        native_digits: bool = True,
    ) -> str:
        return super().format_decimal_number(
            number,
            decimal_places,
            use_group_separator,
            use_fraction_group_separator,
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
            native_digits,
        )
