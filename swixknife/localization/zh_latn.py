

__all__ = ('SezimalLocaleZH_LATN',)


from .zh import SezimalLocaleZH


class SezimalLocaleZH_LATN(SezimalLocaleZH):
    LANG = 'zh'
    LANGUAGE = 'zhōngwén'  # 中文

    IDEOGRAPHIC = False

    WEEKDAY_NAME = [
        'xīngqíyī',   # 星期一
        'xīngqí’èr',  # 星期二
        'xīngqísān',  # 星期三
        'xīngqísì',   # 星期四
        'xīngqíwǔ',   # 星期五
        'xīngqíliù',  # 星期六
        'xīngqírì',   # 星期日
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'xq1',   # 周一
        'xq2',   # 周二
        'xq3',   # 周三
        'xq4',   # 周四
        'xq5',   # 周五
        'xq6',  # 周六
        'xqr',  # 周日
    ]

    MONTH_NAME= [
        'yī yuè',        # 一月
        'èr yuè',        # 二月
        'sān yuè',       # 三月
        'sì yuè',        # 四月
        'wǔ yuè',        # 五月
        'liù yuè',       # 六月
        # 'qī yuè',      # 七月
        # 'bā yuè',      # 八月
        # 'jiǔ yuè',     # 九月
        # 'shí yuè',     # 十月
        # 'shíyī yuè',   # 十一月
        # 'shí’èr yuè',  # 十二月
        'liǔyī yuè',     # 六一月
        'liǔ’èr yuè',    # 六二月
        'liǔsān yuè',    # 六三月
        'liǔsì yuè',     # 六四月
        'liǔwǔ yuè',     # 六五月
        'èrliǔ yuè',     # 二六月
    ]

    MONTH_ABBREVIATED_NAME = [
        '1y',
        '2y',
        '3y',
        '4y',
        '5y',
        '10y',
        '11y',
        '12y',
        '13y',
        '14y',
        '15y',
        '20y',
    ]

    DATE_LONG_FORMAT = '#Y nián #m yuè #d rì'
    DATE_TIME_LONG_FORMAT = '#Y nián #-m yuè #-d rì #W #u:#p:#a'
    DST_NAME = 'xià shí zhì'  # 夏时制
    DST_SHORT_NAME = 'xià shí zhì'

    SEASON_NAME = {
        'spring_cross_quarter': 'chūnjì kuà jìdù',  # 春季跨季度
        'spring_equinox': 'chūnfēn',                # 春分
        'summer_cross_quarter': 'xiàjì kuà jìdù',   # 夏季跨季度
        'summer_solstice': 'xiàzhì',                # 夏至
        'autumn_cross_quarter': 'qiūjì kuà jìdù',   # 秋季跨季度
        'autumn_equinox': 'qiūfēn',                 # 秋分
        'winter_cross_quarter': 'dōngjì kuà jìdù',  # 冬季跨季度
        'winter_solstice': 'dōngzhì',               # 冬至
    }

    MOON_PHASE = {
        'new': 'xīn yuè',                   # 新月
        'waxing_crescent': 'méi yuè',       # 眉月
        'first_quarter': 'shàngxián yuè',   # 上弦月
        'waxing_gibbous': 'shàngtú yuè',    # 上凸月
        'full': 'mǎn yuè',                  # 满月
        'waning_gibbous': 'xiàtú yuè',      # 下凸月
        'third_quarter': 'xiàxián yuè',     # 下弦月
        'waning_crescent': 'cán yuè',       # 殘月
    }

    #
    # Error messages
    #
    ERROR = 'Cuòwù'
    WEEKDAY_ERROR = '{weekday} shì wúxiào xīngqí jǐ'
    MONTH_ERROR = '{month} shì wúxiào yuèfèn'
