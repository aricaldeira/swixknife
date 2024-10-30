

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
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_HOUR_MINUTE_FORMAT = '%I:%M %P'
    AM = '𐑱𐑧𐑥'
    PM = '𐑐𐑰𐑧𐑥'

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
    WEEK_NUMBER_SYMBOL = '𐑢𐑒#'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if str(day).endswith('1'):
            return '𐑕𐑑'
        elif str(day).endswith('2'):
            return '𐑯𐑛'
        elif str(day).endswith('3'):
            return '𐑮𐑛'

        return '𐑔'
