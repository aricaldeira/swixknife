

__all__ = ('SezimalLocaleZH',)


from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

from .lokale import SezimalLocale
from ..base import SEPARATOR_DOT, SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleZH(SezimalLocale):
    LANG = 'zh'
    LANGUAGE = '中文'  # zhōngwén

    IDEOGRAPHIC = True
    # DIGITS = '０１２３４５６７８９'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT
    # SEZIMAL_SEPARATOR = '．'

    GROUP_SEPARATOR = SEPARATOR_COMMA
    # GROUP_SEPARATOR = '，'
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    # FRACTION_GROUP_SEPARATOR = '\u3000'
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        '星期一',  # xīngqíyī
        '星期二',  # xīngqí’èr
        '星期三',  # xīngqísān
        '星期四',  # xīngqísì
        '星期五',  # xīngqíwǔ
        '星期六',  # xīngqíliù
        '星期日',  # xīngqírì
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        # '周一',  # zhōuyī
        # '周二',  # zhōu’èr
        # '周三',  # zhōusān
        # '周四',  # zhōusì
        # '周五',  # zhōuwǔ
        # '周六',  # zhōuliù
        # '周日',  # zhōurì
        '一',  # zhōuyī
        '二',  # zhōu’èr
        '三',  # zhōusān
        '四',  # zhōusì
        '五',  # zhōuwǔ
        '六',  # zhōuliù
        '日',  # zhōurì
    ]

    MONTH_NAME= [
        '一月',   # yī yuè
        '二月',   # èr yuè
        '三月',   # sān yuè
        '四月',   # sì yuè
        '五月',   # wǔ yuè
        '六月',   # liù yuè
        # '七月',    # qī yuè
        # '八月',    # bā yuè
        # '九月',    # jiǔ yuè
        # '十月',    # shí yuè
        # '十一月',  # shíyī yuè
        # '十二月',  # shí’èr yuè
        '六一月',  # liǔyī yuè
        '六二月',  # liǔ’èr yuè
        '六三月',  # liǔsān yuè
        '六四月',  # liǔsì yuè
        '六五月',  # liǔwǔ yuè
        '二六月',  # èrliǔ yuè
    ]

    MONTH_ABBREVIATED_NAME = [
        '1月',
        '2月',
        '3月',
        '4月',
        '5月',
        '10月',
        '11月',
        '12月',
        '13月',
        '14月',
        '15月',
        '20月',
    ]

    DATE_FORMAT = '#?Y/#?m/#?d'
    DATE_LONG_FORMAT = '#?Y年#?m月#?d日'
    TIME_FORMAT = '#?u:#?p:#?a'
    DATE_TIME_FORMAT = '#?Y/#?m/#?d #@W #?u:#?p:#?a'
    DATE_TIME_LONG_FORMAT = '#?Y年#?-m月#?-d日#W #?u:#?p:#?a'
    DST_NAME = '夏时制'  # xià shí zhì
    DST_SHORT_NAME = '夏时制'

    SEASON_NAME = {
        'spring_cross_quarter': '春季跨季度',  # chūnjì kuà jìdù
        'spring_equinox': '春分',             # chūnfēn
        'summer_cross_quarter': '夏季跨季度',  # xiàjì kuà jìdù
        'summer_solstice': '夏至',            # xiàzhì
        'autumn_cross_quarter': '秋季跨季度',  # qiūjì kuà jìdù
        'autumn_equinox': '秋分',             # qiūfēn
        'winter_cross_quarter': '冬季跨季度',  # dōngjì kuà jìdù
        'winter_solstice': '冬至',            # dōngzhì
    }

    MOON_PHASE = {
        'new': '新月',               # xīn yuè
        'waxing_crescent': '眉月',   # méi yuè
        'first_quarter': '上弦月',   # shàngxián yuè
        'waxing_gibbous': '上凸月',  # shàngtú yuè
        'full': '满月',              # mǎn yuè
        'waning_gibbous': '下凸月',  # xiàtú yuè
        'third_quarter': '下弦月',   # xiàxián yuè
        'waning_crescent': '殘月',   # cán yuè
    }

    #
    # Error messages
    #
    ERROR = '错误'
    WEEKDAY_ERROR = '{weekday}是星期几无效'
    MONTH_ERROR = '{month}是月份无效'

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
        return super().format_number(
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
