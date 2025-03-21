

__all__ = ('SezimalLocaleEO_TR',)


from .eo import SezimalLocaleEO
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleEO_TR(SezimalLocaleEO):
    SEZIMAL_SEPARATOR = SEPARATOR_COMMA
    GROUP_SEPARATOR = SEPARATOR_DOT

    DEFAULT_TIME_ZONE = 'Europe/Istanbul'
    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    CURRENCY_UNIT_SYMBOL = '₺'
    CURRENCY_SUBUNIT_SYMBOL = 'kr'
    CURRENCY_SUBUNIT_SYMBOL_POSITION = 'R'

    HOLIDAYS = [
        ('SYM+01-01', '🎆\ufe0f Novjaro'),
        ('SYM+05-01', '🛠️\ufe0f✊\ufe0f Tago de Laboro kaj Solidareco'),

        # ('ISO+1915-03-18', '🇹🇷\ufe0f🛑\ufe0f Memortago de Martiroj kaj la Venko de Ĉanakale (%i)'),
        # ('ISO+1920-04-23', '🇹🇷\ufe0f👧\ufe0f Tago de Infanoj kaj Nacia Suvereneco (%i)'),
        # ('ISO+1919-05-19', '🇹🇷\ufe0f Tago de Junularo, Memoro de Atatürk kaj Sporto (%i)'),
        # ('ISO+2016-07-15', '🇹🇷\ufe0f🕊️\ufe0f Tago de Demokratio kaj Nacia Unueco (%i)'),
        # ('ISO+1922-08-30', '🇹🇷\ufe0f🏆\ufe0f Venktago (%i)'),
        # ('ISO+1923-10-29', '🇹🇷\ufe0f🎇\ufe0f Tago de la Respubliko (%i)'),
        # ('ISO+1938-11-10', '🇹🇷\ufe0f🫡\ufe0f Memortago de Atatürk (%i)'),

        ('HIJ+SYM+10-01', '🕌\ufe0f🍬\ufe0f Sukerfesto'),
        ('HIJ+SYM+10-02', '🕌\ufe0f🍬\ufe0f Sukerfesto'),
        ('HIJ+SYM+10-03', '🕌\ufe0f🍬\ufe0f Sukerfesto'),
        ('HIJ+SYM+12-10', '🕌\ufe0f🐏\ufe0f Oferfesto'),
        ('HIJ+SYM+12-11', '🕌\ufe0f🐏\ufe0f Oferfesto'),
        ('HIJ+SYM+12-12', '🕌\ufe0f🐏\ufe0f Oferfesto'),
        ('HIJ+SYM+12-13', '🕌\ufe0f🐏\ufe0f Oferfesto'),
    ] + SezimalLocaleEO.HOLIDAYS

    HOLIDAYS_OTHER_CALENDAR = [
        ('ISO+01-01', '🎆\ufe0f Novjaro'),
        ('ISO+05-01', '🛠️\ufe0f✊\ufe0f Tago de Laboro kaj Solidareco'),

        ('ISO+1915-03-18', '🇹🇷\ufe0f🛑\ufe0f Memortago de Martiroj kaj la Venko de Ĉanakale (%i)'),
        ('ISO+1920-04-23', '🇹🇷\ufe0f👧\ufe0f Tago de Infanoj kaj Nacia Suvereneco (%i)'),
        ('ISO+1919-05-19', '🇹🇷\ufe0f Tago de Junularo, Memoro de Atatürk kaj Sporto (%i)'),
        ('ISO+2016-07-15', '🇹🇷\ufe0f🕊️\ufe0f Tago de Demokratio kaj Nacia Unueco (%i)'),
        ('ISO+1922-08-30', '🇹🇷\ufe0f🏆\ufe0f Venktago (%i)'),
        ('ISO+1923-10-29', '🇹🇷\ufe0f🎇\ufe0f Tago de la Respubliko (%i)'),
        ('ISO+1938-11-10', '🇹🇷\ufe0f🫡\ufe0f Memortago de Atatürk (%i)'),

        ('HIJ+ISO+10-01', '🕌\ufe0f🍬\ufe0f Sukerfesto'),
        ('HIJ+ISO+10-02', '🕌\ufe0f🍬\ufe0f Sukerfesto'),
        ('HIJ+ISO+10-03', '🕌\ufe0f🍬\ufe0f Sukerfesto'),
        ('HIJ+ISO+12-10', '🕌\ufe0f🐏\ufe0f Oferfesto'),
        ('HIJ+ISO+12-11', '🕌\ufe0f🐏\ufe0f Oferfesto'),
        ('HIJ+ISO+12-12', '🕌\ufe0f🐏\ufe0f Oferfesto'),
        ('HIJ+ISO+12-13', '🕌\ufe0f🐏\ufe0f Oferfesto'),
    ] + SezimalLocaleEO.HOLIDAYS_OTHER_CALENDAR
