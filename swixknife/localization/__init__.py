

__all__ = ('sezimal_locale', 'DEFAULT_LOCALE')


import locale as system_locale

from .bz import SezimalLocaleBZ
from .ca import SezimalLocaleCA
from .de import SezimalLocaleDE
from .el import SezimalLocaleEL
from .en import SezimalLocaleEN
from .eo import SezimalLocaleEO
from .es import SezimalLocaleES
from .fr import SezimalLocaleFR
from .it import SezimalLocaleIT
from .pl import SezimalLocalePL
from .pt import SezimalLocalePT
from .ro import SezimalLocaleRO
from .ru import SezimalLocaleRU

from .lokale import SezimalLocale


_LOCALES = {
    'bz': SezimalLocaleBZ,
    'ca': SezimalLocaleCA,
    'de': SezimalLocaleDE,
    'el': SezimalLocaleEL,
    'en': SezimalLocaleEN,
    'eo': SezimalLocaleEO,
    'es': SezimalLocaleES,
    'fr': SezimalLocaleFR,
    'it': SezimalLocaleIT,
    'pl': SezimalLocalePL,
    'pt': SezimalLocalePT,
    'ro': SezimalLocaleRO,
    'ru': SezimalLocaleRU,
}


def _get_system_locale():
    locale = system_locale.getlocale()[0]

    if locale == 'C':
        locale = 'en'

    return locale


def sezimal_locale(locale: str = None) -> SezimalLocale:
    if not locale:
        locale = _get_system_locale()

    locale = locale.replace('-', '_')

    original_locale = locale

    locale = locale.lower()

    if locale in _LOCALES:
        return _LOCALES[locale]()

    if len(locale) >= 2:
        locale = locale[:2]

        if locale in _LOCALES:
            return _LOCALES[locale]()

    return _create_locale_from_icu(original_locale) or _create_locale_from_system(original_locale)


def _create_locale_from_icu(locale: str) -> SezimalLocale:
    try:
        import icu
    except:
        return None

    if locale not in icu.Locale.getAvailableLocales():
        return None

    new_locale = SezimalLocale

    loc = icu.Locale(locale)
    dfs = icu.DecimalFormatSymbols(loc)

    new_locale.LANG = locale
    new_locale.LANGUAGE = loc.getDisplayName(loc)

    #
    # Digit separation and grouping
    #
    new_locale.SEZIMAL_SEPARATOR = dfs.getSymbol(dfs.kDecimalSeparatorSymbol)
    new_locale.GROUP_SEPARATOR = dfs.getSymbol(dfs.kGroupingSeparatorSymbol)

    #
    # Weekday and month names
    #
    dfs = icu.DateFormatSymbols(loc)

    new_locale.WEEKDAY_NAME = dfs.getWeekdays()[2:] + [dfs.getWeekdays()[1]]
    new_locale.WEEKDAY_ABBREVIATED_NAME = dfs.getShortWeekdays()[2:] + [dfs.getShortWeekdays()[1]]
    new_locale.MONTH_NAME = dfs.getMonths()
    new_locale.MONTH_ABBREVIATED_NAME = dfs.getShortMonths()

    _LOCALES[locale] = new_locale

    return new_locale()


def _create_locale_from_system(locale: str) -> SezimalLocale:
    new_locale = SezimalLocale
    new_locale.LANG = locale
    new_locale.LANGUAGE = locale

    #
    # Digit separation and grouping
    #
    new_locale.SEZIMAL_SEPARATOR = system_locale.nl_langinfo(system_locale.RADIXCHAR)
    new_locale.GROUP_SEPARATOR = system_locale.nl_langinfo(system_locale.THOUSEP)

    #
    # Weekday and month names
    #
    new_locale.WEEKDAY_NAME = [
        system_locale.nl_langinfo(system_locale.DAY_2),
        system_locale.nl_langinfo(system_locale.DAY_3),
        system_locale.nl_langinfo(system_locale.DAY_4),
        system_locale.nl_langinfo(system_locale.DAY_5),
        system_locale.nl_langinfo(system_locale.DAY_6),
        system_locale.nl_langinfo(system_locale.DAY_7),
        system_locale.nl_langinfo(system_locale.DAY_1),
    ]
    new_locale.WEEKDAY_ABBREVIATED_NAME = [
        system_locale.nl_langinfo(system_locale.ABDAY_2),
        system_locale.nl_langinfo(system_locale.ABDAY_3),
        system_locale.nl_langinfo(system_locale.ABDAY_4),
        system_locale.nl_langinfo(system_locale.ABDAY_5),
        system_locale.nl_langinfo(system_locale.ABDAY_6),
        system_locale.nl_langinfo(system_locale.ABDAY_7),
        system_locale.nl_langinfo(system_locale.ABDAY_1),
    ]
    new_locale.MONTH_NAME = [
        system_locale.nl_langinfo(system_locale.MON_1),
        system_locale.nl_langinfo(system_locale.MON_2),
        system_locale.nl_langinfo(system_locale.MON_3),
        system_locale.nl_langinfo(system_locale.MON_4),
        system_locale.nl_langinfo(system_locale.MON_5),
        system_locale.nl_langinfo(system_locale.MON_6),
        system_locale.nl_langinfo(system_locale.MON_7),
        system_locale.nl_langinfo(system_locale.MON_8),
        system_locale.nl_langinfo(system_locale.MON_9),
        system_locale.nl_langinfo(system_locale.MON_10),
        system_locale.nl_langinfo(system_locale.MON_11),
        system_locale.nl_langinfo(system_locale.MON_12),
    ]
    new_locale.MONTH_ABBREVIATED_NAME = [
        system_locale.nl_langinfo(system_locale.ABMON_1),
        system_locale.nl_langinfo(system_locale.ABMON_2),
        system_locale.nl_langinfo(system_locale.ABMON_3),
        system_locale.nl_langinfo(system_locale.ABMON_4),
        system_locale.nl_langinfo(system_locale.ABMON_5),
        system_locale.nl_langinfo(system_locale.ABMON_6),
        system_locale.nl_langinfo(system_locale.ABMON_7),
        system_locale.nl_langinfo(system_locale.ABMON_8),
        system_locale.nl_langinfo(system_locale.ABMON_9),
        system_locale.nl_langinfo(system_locale.ABMON_10),
        system_locale.nl_langinfo(system_locale.ABMON_11),
        system_locale.nl_langinfo(system_locale.ABMON_12),
    ]

    _LOCALES[locale] = new_locale

    return new_locale()

DEFAULT_LOCALE = sezimal_locale()
