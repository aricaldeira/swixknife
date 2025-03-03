

__all__ = ('SezimalLocaleEN_MY',)


from .en import SezimalLocaleEN


class SezimalLocaleEN_MY(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Malaysian English'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Kuala_Lumpur'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = 'RM'  # Malaysian Ringgit
    CURRENCY_SUBUNIT_SYMBOL = 's'  # sen
