

__all__ = ('SezimalLocaleEN_SHAW_CA',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_ca import SezimalLocaleEN_CA


class SezimalLocaleEN_SHAW_CA(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑒𐑩𐑯𐑱𐑛𐑾𐑯 𐑦𐑙𐑜𐑤𐑦𐑖'

    DEFAULT_TIME_ZONE = 'America/Toronto'
    ISO_TIME_FORMAT = '%I:%M:%S %p'
    ISO_SHORT_TIME_FORMAT = '%I:%M %p'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    FIRST_WEEKDAY = 'SUN'

    SEASON_NAME = {
        'spring_cross_quarter': '𐑕𐑐𐑮𐑦𐑙 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'spring_equinox': '𐑕𐑐𐑮𐑦𐑙',
        'summer_cross_quarter': '𐑕𐑳𐑥𐑼 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'summer_solstice': '𐑕𐑳𐑥𐑼',
        'autumn_cross_quarter': '𐑓𐑷𐑤 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'autumn_equinox': '𐑓𐑷𐑤',
        'winter_cross_quarter': '𐑢𐑦𐑯𐑑𐑼 𐑒𐑮𐑪𐑕-𐑒𐑢𐑹𐑑𐑼',
        'winter_solstice': '𐑢𐑦𐑯𐑑𐑼',
    }

    HOLIDAYS = SezimalLocaleEN_CA.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_CA.HOLIDAYS_OTHER_CALENDAR
    SEASON_EMOJI_NORTHERN_HEMISPHERE = SezimalLocaleEN_CA.SEASON_EMOJI_NORTHERN_HEMISPHERE
