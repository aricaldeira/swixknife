

__all__ = ('SezimalLocaleFR_CH',)


from .fr import SezimalLocaleFR


class SezimalLocaleFR_CH(SezimalLocaleFR):
    LANG = 'fr'
    LANGUAGE = 'français de Suisse'

    CURRENCY_UNIT_SYMBOL = 'fr.'
    CURRENCY_SUBUNIT_SYMBOL = 'c.'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    DATE_FORMAT = '#d.#m.#Y'
    DATE_TIME_FORMAT = '#@W, #d.#m.#Y, #u:#p:#a'
    DEFAULT_TIME_ZONE = 'Europe/Zurich'

