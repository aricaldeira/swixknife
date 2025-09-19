

__all__ = ('SezimalLocaleZH',)


from .zh import SezimalLocaleZH


class SezimalLocaleZH_HANT(SezimalLocaleZH):
    DST_NAME = '夏時制' # xià shí zhì
    DST_SHORT_NAME = '夏時制'

    MOON_PHASE = {
        'new': '新月',               # xīn yuè
        'waxing_crescent': '眉月',   # méi yuè
        'first_quarter': '上弦月',   # shàngxián yuè
        'waxing_gibbous': '上凸月',  # shàngtú yuè
        'full': '滿月',              # mǎn yuè
        'waning_gibbous': '下凸月',  # xiàtú yuè
        'third_quarter': '下弦月',   # xiàxián yuè
        'waning_crescent': '殘月',   # cán yuè
    }

    #
    # Error messages
    #
    ERROR = '錯誤'
    WEEKDAY_ERROR = '{weekday}是無效星期几'
    MONTH_ERROR = '{month}是無效月份'

    ADC_MONTH_NAME = [
        '雙魚座月',
        '鯨魚座月',
        '波江座月',
        '麒麟座月',
        '長蛇座月',
        '獅子座月',
        '室女座月',
        '巨蛇座月',
        '天鷹座月',
        '寶瓶座月',
        '六分儀座月',
    ]

    ADC_MONTH_ABBREVIATED_NAME = [
        '雙魚',
        '鯨魚',
        '波江',
        '麒麟',
        '長蛇',
        '獅子',
        '室女',
        '巨蛇',
        '天鷹',
        '寶瓶',
        '六分儀',
    ]

    ADC_MONTH_SYMBOL = [
        '雙魚',
        '鯨魚',
        '波江',
        '麒麟',
        '長蛇',
        '獅子',
        '室女',
        '巨蛇',
        '天鷹',
        '寶瓶',
        '六分',
    ]

    ADC_WEEK_NAME = [
        '魂週',
        '火週',
        '風週',
        '水週',
        '地週',
        '體週',
    ]

    ADC_WEEK_ABBREVIATED_NAME = [
        '魂',
        '火',
        '風',
        '水',
        '地',
        '體',
    ]

    ADC_WEEK_SYMBOL = [
        '魂',
        '火',
        '風',
        '水',
        '地',
        '體',
    ]
