

__all__ = ('SezimalLocaleEN_SHAW_US',)


from .en_shaw import SezimalLocaleEN_SHAW
from .en_us import SezimalLocaleEN_US


class SezimalLocaleEN_SHAW_US(SezimalLocaleEN_SHAW):
    LANG = 'en'
    LANGUAGE = '𐑩𐑥𐑧𐑮𐑦𐑒𐑩𐑯 𐑦𐑙𐑜𐑤𐑦𐑖'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    DEFAULT_TIME_ZONE = 'America/New_York'
    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#m/#d/#Y'
    DATE_LONG_FORMAT = '#M #-d, #Y'
    DATE_FULL_FORMAT = '#@W #m/#d/#Y'
    DATE_FULL_LONG_FORMAT = '#W, #M #-d, #Y'
    DATE_TIME_FORMAT = '#@W #m/#d/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #M #-d, #Y, #u:#p:#a'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    FIRST_WEEKDAY = 'SUN'

    DECIMAL_TEMPERATURE = '°F'
    DECIMAL_SPEED = 'mph'

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

    HOLIDAYS = SezimalLocaleEN_US.HOLIDAYS
    HOLIDAYS_OTHER_CALENDAR = SezimalLocaleEN_US.HOLIDAYS_OTHER_CALENDAR
