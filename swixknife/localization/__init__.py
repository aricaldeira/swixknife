

__all__ = ('sezimal_locale', 'DEFAULT_LOCALE', 'SezimalLocale')


import locale as system_locale
import importlib

from .lokale import SezimalLocale


LOCALE_CACHE = {}


def _get_system_locale():
    locale = system_locale.getlocale()[0]

    if locale == 'C' or (not locale):
        locale = 'en'

    return locale


def sezimal_locale(locale: str | SezimalLocale = None) -> SezimalLocale:
    if isinstance(locale, SezimalLocale):
        return locale

    if not locale:
        locale = _get_system_locale()

    locale = locale.replace('-', '_')

    original_locale = locale

    locale = locale.lower()

    if locale in LOCALE_CACHE:
        return LOCALE_CACHE[locale]()

    if len(locale) >= 2:
        if locale[:2] in LOCALE_CACHE:
            return LOCALE_CACHE[locale[:2]]()

    try:
        module = importlib.import_module('swixknife.localization.' + locale)
        locale_class = getattr(module, 'SezimalLocale' + locale.upper())
        LOCALE_CACHE[locale] = locale_class
        return locale_class()

    except:
        try:
            module = importlib.import_module('swixknife.localization.' + locale[:2])
            locale_class = getattr(module, 'SezimalLocale' + locale[:2].upper())
            LOCALE_CACHE[locale[:2]] = locale_class
            return locale_class()

        except:
            pass

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

    LOCALE_CACHE[locale] = new_locale

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

    LOCALE_CACHE[locale] = new_locale

    return new_locale()

DEFAULT_LOCALE = sezimal_locale()
