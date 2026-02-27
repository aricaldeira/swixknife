

__all__ = ('SezimalLocaleDE_CH',)


from .de import SezimalLocaleDE


class SezimalLocaleDE_CH(SezimalLocaleDE):
    LANG = 'de'
    LANGUAGE = 'Schweizer Deutsch'

    DEFAULT_TIME_ZONE = 'Europe/Zurich'

    CURRENCY_UNIT_SYMBOL = 'Fr.'
    CURRENCY_SUBUNIT_SYMBOL = 'Rp.'
