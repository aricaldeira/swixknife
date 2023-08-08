

__all__ = ('SezimalLocaleZH',)


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
