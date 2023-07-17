

__all__ = ('SezimalLocaleJA',)


from .lokale import SezimalLocale
from ..base import SEPARATOR_DOT, SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleJA(SezimalLocale):
    LANG = 'ja'
    LANGUAGE = '日本語'  # nihongo

    IDEOGRAPHIC = True
    DIGITS = '０１２３４５６７８９'

    # SEZIMAL_SEPARATOR = SEPARATOR_DOT
    SEZIMAL_SEPARATOR = '．'

    # GROUP_SEPARATOR = SEPARATOR_COMMA
    GROUP_SEPARATOR = '，'
    SUBGROUP_SEPARATOR = ''

    # FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_GROUP_SEPARATOR = '\u3000'
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

    MONTH_NAME= [
        '１月',   # ichigatsu
        '２月',   # nigatsu
        '３月',   # sangatsu
        '４月',   # shigatsu
        '５月',   # gogatsu
        '１０月',  # rokugatsu
        # '７月',    # nanagatsu
        # '８月',    # hachigatsu
        # '９月',    # kugatsu
        # '１０月',   # jūgatsu
        # '１１月',   # jūichigatsu
        # '１２月',   # jūnigatsu
        '１１月',  # muichigatsu
        '１２月',  # munigatsu
        '１３月',  # musangatsu
        '１４月',  # mushigatsu
        '１５月',  # mugogatsu
        '２０月',  # nimugatsu
    ]

    MONTH_ABBREVIATED_NAME = [
        '１月',
        '２月',
        '３月',
        '４月',
        '５月',
        '１０月',
        '１１月',
        '１２月',
        '１３月',
        '１４月',
        '１５月',
        '２０月',
    ]

    DATE_FORMAT = '#?Y／#?m／#?d'
    DATE_LONG_FORMAT = '#?Y年#?m月#?d日'
    TIME_FORMAT = '#?u：#?p：#?a'
    DATE_TIME_FORMAT = '#?Y／#?m／#?d #@W #?u：#?p：#?a'
    DATE_TIME_LONG_FORMAT = '#?Y年#?-m月#?-d日#W #?u：#?p：#?a'
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
