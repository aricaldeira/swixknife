

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
