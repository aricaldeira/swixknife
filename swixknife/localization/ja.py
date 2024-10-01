

__all__ = ('SezimalLocaleJA',)


from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

from .lokale import SezimalLocale
from ..base import SEPARATOR_DOT, SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleJA(SezimalLocale):
    LANG = 'ja'
    LANGUAGE = '日本語'  # nihongo

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

    FIRST_WEEKDAY = 'SUN'

    WEEKDAY_NAME = [
        '月曜日',  # getsuyōbi
        '火曜日',  # kayōbi
        '水曜日',  # suiyōbi
        '木曜日',  # mokuyōbi
        '金曜日',  # kin’yōbi
        '土曜日',  # doyōbi
        '日曜日',  # nichiyōbi
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        '月',  # getsu
        '火',  # ka
        '水',  # sui
        '木',  # moku
        '金',  # kin
        '土',  # do
        '日',  # nichi
    ]

    WEEKDAY_SYMBOL = [
        '月',  # getsu
        '火',  # ka
        '水',  # sui
        '木',  # moku
        '金',  # kin
        '土',  # do
        '日',  # nichi
    ]

    MONTH_NAME= [
        '一月',   # ichigatsu
        '二月',   # nigatsu
        '三月',   # sangatsu
        '四月',   # shigatsu
        '五月',   # gogatsu
        '六月',   # rokugatsu
        # '7月',    # nanagatsu
        # '8月',    # hachigatsu
        # '9月',    # kugatsu
        # '10月',   # jūgatsu
        # '11月',   # jūichigatsu
        # '12月',   # jūnigatsu
        '六一月',  # muichigatsu
        '六二月',  # munigatsu
        '六三月',  # musangatsu
        '六四月',  # mushigatsu
        '六五月',  # mugogatsu
        '二六月',  # nimugatsu
    ]

    ISO_MONTH_NAME = [
        '一月',   # ichigatsu
        '二月',   # nigatsu
        '三月',   # sangatsu
        '四月',   # shigatsu
        '五月',   # gogatsu
        '六月',   # rokugatsu
        '七月',   # nanagatsu
        '八月',   # hachigatsu
        '九月',   # kugatsu
        '十月',   # jūgatsu
        '十一月',  # jūichigatsu
        '十二月',  # jūnigatsu
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

    ISO_MONTH_ABBREVIATED_NAME = [
        '1月',
        '2月',
        '3月',
        '4月',
        '5月',
        '6月',
        '7月',
        '8月',
        '9月',
        '10月',
        '11月',
        '12月',
    ]

    DATE_FORMAT = '#?Y/#?m/#?d'
    DATE_LONG_FORMAT = '#?Y年#?m月#?d日'
    TIME_FORMAT = '#?u:#?p:#?a'
    DATE_TIME_FORMAT = '#?Y/#?m/#?d #@W #?u:#?p:#?a'
    DATE_TIME_LONG_FORMAT = '#?Y年#?-m月#?-d日#W #?u:#?p:#?a'
    DEFAULT_TIME_ZONE = 'Asia/Tokyo'
    DST_NAME = '夏時間'  # natsu jikan
    DST_SHORT_NAME = 'DST'

    SEASON_NAME = {
        'spring_cross_quarter': '冬から春への半ば',  # fuyu kara haru e no nakaba
        'spring_equinox': '春',                    # haru
        'summer_cross_quarter': '春から夏への半ば',  # haru kara natsu e no nakaba
        'summer_solstice': '夏',                   # natsu
        'autumn_cross_quarter': '夏から秋への半ば',  # natsu kara aki e no nakaba
        'autumn_equinox': '秋',                    # aki
        'winter_cross_quarter': '秋から冬への半ば',  # aki kara fuyu e no nakaba
        'winter_solstice': '冬',                   # fuyu
    }

    MOON_PHASE = {
        'new': '新月',                        # shingetsu
        'waxing_crescent': '上弦の三日月',     # jōgen no mikadzuki
        'first_quarter': '上弦の月',           # jōgen no tsuki
        'waxing_gibbous': '上弦の巨大な月',     # jōgen no kyodaina tsuki
        'full': '満月',                        # man getsu
        'waning_gibbous': '欠けていく巨大な月',  # kakete iku kyodaina tsuki
        'third_quarter': '上弦の月',            # jōgen no tsuki
        'waning_crescent': '欠けていく三日月',   # kakete iku mikadzuki
    }

    #
    # Error messages
    #
    ERROR = 'エラー'
    WEEKDAY_ERROR = '{weekday}は曜日が無効です'
    MONTH_ERROR = '{month}は月が無効です'
    WEEK_NUMBER_SYMBOL = '週'

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
