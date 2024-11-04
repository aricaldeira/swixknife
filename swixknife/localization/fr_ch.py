

__all__ = ('SezimalLocaleFR_CH',)


from .fr_fr import SezimalLocaleFR_FR


class SezimalLocaleFR_CH(SezimalLocaleFR_FR):
    LANG = 'fr'
    LANGUAGE = 'français de Suisse'

    CURRENCY_UNIT_SYMBOL = 'fr.'
    CURRENCY_SUBUNIT_SYMBOL = 'c.'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#Y'
    DATE_TIME_FORMAT = '#@W, #d.#m.#Y, #u:#p:#a'
    DEFAULT_TIME_ZONE = 'Europe/Zurich'

