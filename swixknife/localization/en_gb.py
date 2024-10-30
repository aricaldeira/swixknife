

__all__ = ('SezimalLocaleEN_GB',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_GB(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'British English'

    DEFAULT_TIME_ZONE = 'Europe/London'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_HOUR_MINUTE_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '£'
    CURRENCY_SUBUNIT_SYMBOL = 'p'
