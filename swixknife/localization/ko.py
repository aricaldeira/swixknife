

__all__ = ('SezimalLocaleKO',)


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
        '1월',   # il-wol
        '2월',   # i-wol
        '3월',   # sam-wol
        '4월',   # sa-wol
        '5월',   # o-wol
        '10월',  # yu-wol
        # '7월',    # chil-wol
        # '8월',    # pal-wol
        # '9월',    # gu-wol
        # '10월',   # si-wol
        # '11월',   # sip-il-wol
        # '12월',   # sip-i-wol
        '11월',  # yu-il-wol
        '12월',  # yu-i-wol
        '13월',  # yu-sam-wol
        '14월',  # yu-sa-wol
        '15월',  # yu-o-wol
        '20월',  # i-yu-wol
    ]

    MONTH_ABBREVIATED_NAME = [
        '１월',
        '２월',
        '３월',
        '４월',
        '５월',
        '１０월',
        '１１월',
        '１２월',
        '１３월',
        '１４월',
        '１５월',
        '２０월',
    ]

    DATE_FORMAT = '#?Y/#?m/#?d'
    DATE_LONG_FORMAT = '#?Y년 #?m월 #?d일'
    TIME_FORMAT = '#?u:#?p:#?a'
    DATE_TIME_FORMAT = '#?Y/#?m/#?d #@W #?u:#?p:#?a'
    DATE_TIME_LONG_FORMAT = '#?Y년 #?-m월 #?-d일 #W #?u:#?p:#?a'
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
