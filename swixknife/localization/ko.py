

__all__ = ('SezimalLocaleKO',)


from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

from .lokale import SezimalLocale
from ..base import SEPARATOR_DOT, SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleKO(SezimalLocale):
    LANG = 'ko'
    LANGUAGE = '한국어'  # han’gugeo

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

    CURRENCY_UNIT_SYMBOL = '₩'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0

    FIRST_WEEKDAY = 'SUN'

    WEEKDAY_NAME = [
        '월요일',  # wol-yoil
        '화요일',  # hwa-yoil
        '수요일',  # su-yoil
        '목요일',  # mog-yoil
        '금요일',  # geum-yoil
        '토요일',  # to-yoil
        '일요일',  # il-yoil
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        '월',  # wol
        '화',  # hwa
        '수',  # su
        '목',  # mog
        '금',  # geum
        '토',  # to
        '일',  # il
    ]

    MONTH_NAME= [
        '일월',   # il-wol
        '이월',   # i-wol
        '삼월',   # sam-wol
        '사월',   # sa-wol
        '오월',   # o-wol
        '육월',  # yu-wol
        # '7월',    # chil-wol
        # '8월',    # pal-wol
        # '9월',    # gu-wol
        # '10월',   # si-wol
        # '11월',   # sip-il-wol
        # '12월',   # sip-i-wol
        '육일월',  # yu-il-wol
        '육이월',  # yu-i-wol
        '육삼월',  # yu-sam-wol
        '육사월',  # yu-sa-wol
        '육오월',  # yu-o-wol
        '이육월',  # i-yu-wol
    ]

    ISO_MONTH_NAME= [
         '일월',  # il-wol
         '이월',  # i-wol
         '삼월',  # sam-wol
         '사월',  # sa-wol
         '오월',  # o-wol
         '육월',  # yu-wol
         '칠월',  # chil-wol
         '팔월',  # pal-wol
         '구월',  # gu-wol
         '십월',  # si-wol
        '십일월',  # sip-il-wol
        '십이월',  # sip-i-wol
    ]

    MONTH_ABBREVIATED_NAME = [
        '1월',
        '2월',
        '3월',
        '4월',
        '5월',
        '10월',
        '11월',
        '12월',
        '13월',
        '14월',
        '15월',
        '20월',
    ]

    ISO_MONTH_ABBREVIATED_NAME = [
        '1월',   # il-wol
        '2월',   # i-wol
        '3월',   # sam-wol
        '4월',   # sa-wol
        '5월',   # o-wol
        '6월',  # yu-wol
        '7월',    # chil-wol
        '8월',    # pal-wol
        '9월',    # gu-wol
        '10월',   # si-wol
        '11월',   # sip-il-wol
        '12월',   # sip-i-wol
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#Y/#m/#d'
    DATE_LONG_FORMAT = '#Y년 #M #-d일'
    DATE_FULL_FORMAT = '#Y/#m/#d #@W'
    DATE_FULL_LONG_FORMAT = '#Y년 #M #-d일 #W'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#Y/#m/#d #@W #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#Y년 #M #-d일 #W #u:#p:#a'
    DEFAULT_TIME_ZONE = 'Asia/Seoul'
    DST_NAME = '일광 절약 시간제'  # ilgwang jeol-yag siganje
    DST_SHORT_NAME = 'DST'

    SEASON_NAME = {
        'spring_cross_quarter': '겨울부터 봄까지',   # gyeoul-buteo bom-kkaji
        'spring_equinox': '봄',                   # bom
        'summer_cross_quarter': '봄부터 여름까지',   # bom-buteo yeoleum-kkaji
        'summer_solstice': '여름',                 # yeoleum
        'autumn_cross_quarter': '여름부터 가을까지',  # yeoleum-buteo ga-eul-kkaji
        'autumn_equinox': '가을',                  # ga-eul
        'winter_cross_quarter': '가을부터 겨울까지',  # ga-eul-buteo gyeoul-kkaji
        'winter_solstice': '겨울',                 # gyeoul
    }

    MOON_PHASE = {
        'new': '신월',                       # sin-wol
        'waxing_crescent': '초승달',         # choseungdal
        'first_quarter': '1분기 달',         # ilbungi dal
        'waxing_gibbous': '만월',            # man-wol
        'full': '보름달',                    # boleumdal
        'waning_gibbous': '약해지는 만월',     # yag haejineun man-wol
        'third_quarter': '3분기 달',          # sambungi dal
        'waning_crescent': '약 해지는 초승달',  # yag haejineun choseungdal
    }

    #
    # Error messages
    #
    ERROR = '오류'
    WEEKDAY_ERROR = '{weekday}잘못된 평일'
    MONTH_ERROR = '{month}잘못된 달'
    WEEK_NUMBER_SYMBOL = '주'
    DAY_NUMBER_SYMBOL = '일'

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
