

__all__ = ('sezimal_locale', 'DEFAULT_LOCALE', 'SezimalLocale')


import sys
import locale as system_locale
import importlib

from .lokale import SezimalLocale


LOCALE_CACHE = {}


def _get_system_locale():
    if sys.platform == 'android':
        try:
            from jnius import autoclass

            AndroidLocale = autoclass('java.util.Locale')

            return AndroidLocale.getDefault().toString()

        except:
            pass

    locale = system_locale.getlocale()[0]

    if locale == 'C' or (not locale):
        locale = 'en'

    return locale


def sezimal_locale(locale: str | SezimalLocale = None, force_icu=False) -> SezimalLocale:
    if isinstance(locale, SezimalLocale):
        return locale

    if not locale:
        locale = _get_system_locale()

    locale = locale.replace('-', '_')

    if '_' in locale:
        parts = locale.split('_')

        if len(parts) == 2:
            language = parts[0].lower()
            country = parts[1].lower()
            script = ''
            locale_icu = language.lower() + '_' + country.upper()
            locale_os = locale_icu

        else:
            language = parts[0].lower()
            script = parts[1].lower()
            country = parts[2].lower()
            locale_icu = language.lower() + '_' + script.capitalize() + '_' + country.upper()
            locale_os = language.lower() + '_' + country.upper()

    else:
        language = locale
        country = ''
        script = ''
        locale_icu = language
        locale_os = language

    if force_icu:
        return _create_locale_from_icu(locale_icu)

    if locale_icu in LOCALE_CACHE:
        return LOCALE_CACHE[locale_icu]()

    try:
        module = importlib.import_module('swixknife.localization.' + locale_icu.lower())
        locale_class = getattr(module, 'SezimalLocale' + locale_icu.upper())
        LOCALE_CACHE[locale_icu] = locale_class
        return locale_class()

    except:
        pass

    if script and country:
        language_icu = language.lower() + '_' + country.lower()

        if language_icu in LOCALE_CACHE:
            return LOCALE_CACHE[language_icu]()

        try:
            module = importlib.import_module('swixknife.localization.' + language_icu)
            locale_class = getattr(module, 'SezimalLocale' + language_icu.upper())
            LOCALE_CACHE[language_icu] = locale_class
            return locale_class()

        except:
            pass

    if language in LOCALE_CACHE:
        return LOCALE_CACHE[language]()

    try:
        module = importlib.import_module('swixknife.localization.' + language)
        locale_class = getattr(module, 'SezimalLocale' + language.upper())
        LOCALE_CACHE[language] = locale_class
        return locale_class()

    except:
        pass

    return _create_locale_from_icu(locale_icu) or _create_locale_from_system(locale_os)


def _create_locale_from_icu(locale: str) -> SezimalLocale:
    try:
        import icu
    except:
        return None

    if locale not in icu.Locale.getAvailableLocales():
        if '_' in locale:
            locale = locale.split('_')[0]

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

    #
    # Date and time formats
    #
    df = icu.DateFormat.createDateInstance(icu.DateFormat.SHORT, loc)
    df = df.toLocalizedPattern()

    if 'dd' in df:
        df = df.replace('dd', '#d')
    elif 'd' in df:
        df = df.replace('d', '#d')

    if 'MM' in df:
        df = df.replace('MM', '#m')
    elif 'M' in df:
        df = df.replace('M', '#m')

    if 'yy' in df:
        df = df.replace('yy', '#Y')
    elif 'y' in df:
        df = df.replace('y', '#Y')

    if '.' in df:
        df = df.replace('#Y', '#y')

    new_locale.DATE_FORMAT = df

    tf = icu.DateFormat.createTimeInstance(icu.DateFormat.LONG, loc)
    tf = tf.toLocalizedPattern().upper().replace(' Z', '').replace('Z ', '').replace(' A', '').replace('A ', '')

    if tf.startswith('HH'):
        separator = tf[2]
    elif tf.startswith('H'):
        separator = tf[1]
    else:
        separator = ':'

    new_locale.TIME_FORMAT = f'#u{separator}#p{separator}#a'

    new_locale.DATE_LONG_FORMAT = new_locale.DATE_FORMAT + ' #@W'
    new_locale.DATE_TIME_FORMAT = new_locale.DATE_FORMAT + ' ' + new_locale.TIME_FORMAT
    new_locale.DATE_TIME_LONG_FORMAT = new_locale.DATE_LONG_FORMAT + ' ' + new_locale.TIME_FORMAT

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
