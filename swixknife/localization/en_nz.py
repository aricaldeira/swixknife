

__all__ = ('SezimalLocaleEN_NZ',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_NZ(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'New Zealand English'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Pacific/Auckland'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_HOUR_MINUTE_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '$'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
