

__all__ = ('SezimalLocaleEN_IE',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_IE(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Irish English'

    DEFAULT_TIME_ZONE = 'Europe/Dublin'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_HOUR_MINUTE_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
