

__all__ = ('SezimalLocaleEN_SHAVIAN',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger

from .en import SezimalLocaleEN

class SezimalLocaleEN_SHAW(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = '𐑦𐑙𐑜𐑤𐑦𐑖'

    WEEKDAY_NAME = [
        '𐑥𐑳𐑯𐑛𐑱',
        '𐑑𐑿𐑟𐑛𐑱',
        '𐑢𐑧𐑯𐑟𐑛𐑱',
        '𐑔𐑻𐑟𐑛𐑱',
        '𐑓𐑮𐑲𐑛𐑱',
        '𐑕𐑨𐑑𐑼𐑛𐑱',
        '𐑕𐑳𐑯𐑛𐑱',
    ]
    WEEKDAY_ABBREVIATED_NAME = [
        '𐑥𐑳𐑯',
        '𐑑𐑿𐑟',
        '𐑢𐑧𐑯',
        '𐑔𐑻𐑟',
        '𐑓𐑮𐑲',
        '𐑕𐑨𐑑',
        '𐑕𐑳𐑯',
    ]

    MONTH_NAME = [
        '𐑡𐑨𐑯𐑘𐑫𐑼𐑦',
        '𐑓𐑧𐑚𐑮𐑫𐑼𐑦',
        '𐑥𐑸𐑗',
        '𐑱𐑐𐑮𐑩𐑤',
        '𐑥𐑱',
        '𐑡𐑵𐑯',
        '𐑡𐑩𐑤𐑲',
        '𐑷𐑜𐑩𐑕𐑑',
        '𐑕𐑧𐑐𐑑𐑧𐑥𐑚𐑼',
        '𐑪𐑒𐑑𐑴𐑚𐑼',
        '𐑯𐑴𐑝𐑧𐑥𐑚𐑼',
        '𐑛𐑦𐑕𐑧𐑥𐑚𐑼',
    ]

    MONTH_ABBREVIATED_NAME = [
        '𐑡𐑨𐑯',
        '𐑓𐑧𐑚',
        '𐑥𐑸𐑗',
        '𐑱𐑐𐑮',
        '𐑥𐑱',
        '𐑡𐑵𐑯',
        '𐑡𐑩𐑤',
        '𐑷𐑜𐑩',
        '𐑕𐑧𐑐',
        '𐑪𐑒𐑑',
        '𐑯𐑴𐑝',
        '𐑛𐑦𐑕',
    ]

    DATE_TIME_LONG_FORMAT = '#W, 𐑞 #-d#O #M #Y, #u:#p:#a'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'
    # AM = '𐑱𐑧𐑥'
    # PM = '𐑐𐑰𐑧𐑥'
    AM = '⸰𐑱𐑥'
    PM = '⸰𐑐𐑥'

    SEASON_NAME = {
        'spring_cross_quarter': '𐑕𐑐𐑮𐑦𐑙 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'spring_equinox': '𐑕𐑐𐑮𐑦𐑙',
        'summer_cross_quarter': '𐑕𐑳𐑥𐑼 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'summer_solstice': '𐑕𐑳𐑥𐑼',
        'autumn_cross_quarter': '𐑷𐑑𐑩𐑥 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'autumn_equinox': '𐑷𐑑𐑩𐑥',
        'winter_cross_quarter': '𐑢𐑦𐑯𐑑𐑼 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'winter_solstice': '𐑢𐑦𐑯𐑑𐑼',
    }

    MOON_PHASE = {
        'new': '𐑯𐑿',
        'waxing_crescent': '𐑢𐑨𐑒𐑕𐑦𐑙 𐑒𐑮𐑧𐑕𐑩𐑯𐑑',
        'first_quarter': '𐑓𐑻𐑕𐑑 𐑒𐑢𐑹𐑑𐑼',
        'waxing_gibbous': '𐑢𐑨𐑒𐑕𐑦𐑙 𐑡𐑦𐑚𐑩𐑕',
        'full': '𐑓𐑫𐑤',
        'waning_gibbous': '𐑢𐑱𐑯𐑦𐑙 𐑡𐑦𐑚𐑩𐑕',
        'third_quarter': '𐑔𐑻𐑛 𐑒𐑢𐑹𐑑𐑼',
        'waning_crescent': '𐑢𐑱𐑯𐑦𐑙 𐑒𐑮𐑧𐑕𐑩𐑯𐑑',
    }

    #
    # Error messages
    #
    ERROR = '𐑧𐑮𐑼'
    WEEKDAY_ERROR = '𐑦𐑯𐑝𐑩𐑤𐑦𐑛 𐑢𐑰𐑒𐑛𐑱 {weekday}'
    MONTH_ERROR = '𐑦𐑯𐑝𐑩𐑤𐑦𐑛 𐑥𐑩𐑯𐑔 {month}'
    WEEK_NUMBER_SYMBOL = '𐑢𐑰𐑒'
    DAY_NUMBER_SYMBOL = '𐑛𐑱'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if str(day).endswith('1'):
            return '𐑕𐑑'
        elif str(day).endswith('2'):
            return '𐑯𐑛'
        elif str(day).endswith('3'):
            return '𐑮𐑛'

        return '𐑔'

    DCC_TERM_NAME = [
        '𐑑𐑼𐑮𐑥‐𐑟𐑰𐑮𐑴',
        '𐑑𐑼𐑮𐑥‐𐑢𐑩𐑯',
        '𐑑𐑼𐑮𐑥‐𐑑𐑵',
        '𐑑𐑼𐑮𐑥‐𐑔𐑮𐑰',
        '𐑑𐑼𐑮𐑥‐𐑓𐑹',
    ]

    DCC_TERM_ABBREVIATED_NAME = [
        '𐑑0',
        '𐑑1',
        '𐑑2',
        '𐑑3',
        '𐑑4',
    ]

    DCC_MONTH_NAME = [
        '𐑥𐑩𐑯𐑔‐𐑟𐑰𐑮𐑴',
        '𐑥𐑩𐑯𐑔‐𐑢𐑩𐑯',
        '𐑥𐑩𐑯𐑔‐𐑑𐑵',
        '𐑥𐑩𐑯𐑔‐𐑔𐑮𐑰',
        '𐑥𐑩𐑯𐑔‐𐑓𐑹',
        '𐑥𐑩𐑯𐑔‐𐑓𐑲𐑝',
        '𐑥𐑩𐑯𐑔‐𐑕𐑦𐑒𐑕',
        '𐑥𐑩𐑯𐑔‐𐑕𐑦𐑒𐑕‐𐑟𐑰𐑮𐑴',
        '𐑥𐑩𐑯𐑔‐𐑕𐑦𐑒𐑕‐𐑑𐑵',
        '𐑥𐑩𐑯𐑔‐𐑕𐑦𐑒𐑕‐𐑔𐑮𐑰',
        '𐑥𐑩𐑯𐑔‐𐑕𐑦𐑒𐑕‐𐑓𐑹',
    ]

    DCC_MONTH_ABBREVIATED_NAME = [
        '𐑥00',
        '𐑥01',
        '𐑥02',
        '𐑥03',
        '𐑥04',
        '𐑥05',
        '𐑥10',
        '𐑥11',
        '𐑥12',
        '𐑥13',
        '𐑥14',
    ]

    DCC_WEEKDAY_NAME = [
        '𐑢𐑰𐑒𐑛𐑱‐𐑟𐑰𐑮𐑴',
        '𐑢𐑰𐑒𐑛𐑱‐𐑢𐑩𐑯',
        '𐑢𐑰𐑒𐑛𐑱‐𐑑𐑵',
        '𐑢𐑰𐑒𐑛𐑱‐𐑔𐑮𐑰',
        '𐑢𐑰𐑒𐑛𐑱‐𐑓𐑹',
        '𐑢𐑰𐑒𐑛𐑱‐𐑓𐑲𐑝',
    ]

    DCC_WEEKDAY_ABBREVIATED_NAME = [
        '𐑢𐑛0',
        '𐑢𐑛1',
        '𐑢𐑛2',
        '𐑢𐑛3',
        '𐑢𐑛4',
        '𐑢𐑛5',
    ]

    DCC_NUMBER = [
        '𐑟𐑰𐑮𐑴',
        '𐑢𐑩𐑯',
        '𐑑𐑵',
        '𐑔𐑮𐑰',
        '𐑓𐑹',
        '𐑓𐑲𐑝',
        '𐑕𐑦𐑒𐑕',
        '𐑕𐑦𐑒𐑕‐𐑟𐑰𐑮𐑴',
        '𐑕𐑦𐑒𐑕‐𐑑𐑵',
        '𐑕𐑦𐑒𐑕‐𐑔𐑮𐑰',
        '𐑕𐑦𐑒𐑕‐𐑓𐑹',
    ]

    DCC_YEAR_COUNT = {
        None: '&>Y 𐑘𐑼𐑟',
        SezimalInteger('1'): '&>Y 𐑘𐑼',
    }

    DCC_TERM_COUNT = {
        None: '&-t 𐑑𐑻𐑥𐑟',
        SezimalInteger('1'): '&-t 𐑑𐑻𐑥',
    }

    DCC_MONTH_COUNT = {
        None: '&-m 𐑥𐑭𐑯𐑔𐑕',
        SezimalInteger('1'): '&-m 𐑥𐑭𐑯𐑔',
    }

    DCC_WEEK_COUNT = {
        None: '&-wM 𐑢𐑰𐑒𐑕',
        SezimalInteger('1'): '&-wM 𐑢𐑰𐑒',
    }

    DCC_WEEK_IN_YEAR_COUNT = {
        None: '&-wY 𐑢𐑰𐑒𐑕',
        SezimalInteger('1'): '&-wY 𐑢𐑰𐑒',
    }

    DCC_DAY_COUNT = {
        None: '&-d 𐑛𐑱𐑟',
        SezimalInteger('1'): '&-d 𐑛𐑱',
    }

    DCC_DAY_IN_YEAR_COUNT = {
        None: '&-dY 𐑛𐑱𐑟',
        SezimalInteger('1'): '&-dY 𐑛𐑱',
    }

    DCC_DAY_IN_WEEK_COUNT = {
        None: '&-dW 𐑛𐑱𐑟',
        SezimalInteger('1'): '&-dW 𐑛𐑱',
    }

    ADC_MONTH_NAME = [
        '𐑐𐑲𐑕𐑰𐑟',
        '𐑕𐑰𐑑𐑩𐑕',
        '𐑦𐑮𐑦𐑛𐑩𐑯𐑩𐑕',
        '𐑥𐑩𐑯𐑭𐑕𐑩𐑮𐑩𐑕',
        '𐑣𐑲𐑛𐑮𐑩',
        '𐑤𐑰𐑴',
        '𐑝𐑻𐑜𐑴',
        '𐑕𐑻𐑐𐑩𐑯𐑕',
        '𐑨𐑒𐑢𐑩𐑤𐑩',
        '𐑩𐑒𐑢𐑧𐑮𐑰𐑩𐑕',
        # '𐑤𐑲𐑚𐑮𐑩',
        '𐑷𐑮𐑲𐑩𐑯',
    ]

    ADC_MONTH_ABBREVIATED_NAME = [
        '𐑐𐑲𐑕',
        '𐑕𐑰𐑑',
        '𐑦𐑮𐑦',
        '𐑥𐑩𐑯',
        '𐑣𐑲𐑛',
        '𐑤𐑰𐑴',
        '𐑝𐑻𐑜',
        '𐑕𐑻𐑐',
        '𐑨𐑒𐑤',
        '𐑩𐑒𐑮',
        # '𐑤𐑲𐑚',
        '𐑷𐑮𐑲',
    ]

    ADC_MONTH_SYMBOL = [
        '𐑐',
        '𐑕',
        '𐑦',
        '𐑥',
        '𐑣',
        '𐑤',
        '𐑝',
        '𐑕',
        '𐑨',
        '𐑩',
        # '𐑤',
        '𐑷',
    ]

    ADC_WEEKDAY_NAME = [
        '𐑕𐑭𐑤',
        # '𐑥𐑻𐑒𐑘𐑼𐑰',
        '𐑝𐑰𐑯𐑩𐑕',
        '𐑥𐑸𐑟',
        '𐑡𐑵𐑐𐑦𐑑𐑼',
        '𐑕𐑨𐑑𐑼𐑯',
        '𐑤𐑵𐑯𐑩',
    ]

    ADC_WEEKDAY_ABBREVIATED_NAME = [
        '𐑕𐑭𐑤',
        # '⸰𐑥𐑻𐑒',
        '𐑝𐑰𐑯',
        '𐑥𐑸𐑟',
        '𐑡𐑵𐑐',
        '𐑕𐑨𐑑',
        '𐑤𐑵𐑯',
    ]

    ADC_WEEKDAY_SYMBOL = [
        '𐑕', # ☉
        # '𐑥', # ☿
        '𐑝', # ♀
        '𐑥', # ♂
        '𐑡', # ♃
        '𐑕', # ♄
        '𐑤', # ○ ☉
    ]

    DCC_DATE_MONTH_DAY_SEPARATOR = ' 𐑯 '
    DCC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, 𐑥𐑩𐑯𐑔 &-m, 𐑛𐑱 &-d'
    DCC_DATE_LONG_FORMAT_ON_DATE_DAYS = '&󱹭>Y, 𐑛𐑱 &-dY'
    DCC_DATE_LONG_FORMAT_ON_DATE_WEEKS = '&󱹭>Y, 𐑢𐑰𐑒 &-wY, 𐑛𐑱 &-dW'
    DCC_DATE_LONG_FORMAT_ON_DATE_MONTHS_WEEKS = '&󱹭>Y, 𐑥𐑩𐑯𐑔 &-m, 𐑢𐑰𐑒 &-wM, 𐑛𐑱 &-dW'
    ADC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, 𐑥𐑩𐑯𐑔 𐑝 &cM, 𐑛𐑱 &-d'
    ADC_DATE_LONG_FORMAT_ON_DATE_WEEKDAY = '&󱹭>Y, 𐑥𐑩𐑯𐑔 𐑝 &cM, 𐑢𐑰𐑒 &wM, 𐑛𐑱 𐑝 &cW'
