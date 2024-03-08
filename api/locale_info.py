
__all__ = ('locale_info',)

from main import app

from swixknife.localization import sezimal_locale, SezimalLocale
from swixknife import SezimalRange


LOCALE_LIST = [
    'ar_latn',
    'ar',
    'bz_pt',
    'bz',
    'ca',
    'de',
    'el',
    'en_au',
    'en_br',
    'en_ca',
    'en_gb',
    'en_ie',
    'en_in',
    'en_nyoo_speling',
    'en_nz',
    'en_shavian',
    'en_us',
    'en',
    'eo_br',
    'eo',
    'es_ar',
    'es_bo',
    'es_cl',
    'es_co',
    'es_ec',
    'es_mx',
    'es_pe',
    'es_py',
    'es_uy',
    'es',
    'fa_latn',
    'fa',
    'fr_ca',
    'fr_ch',
    'fr_ortograf',
    'fr',
    'ga_clo_gaelach',
    'ga_traditional',
    'ga',
    'gl',
    'gn',
    'he_latn',
    'he',
    'hi_latn',
    'hi',
    'hu',
    'id',
    'it',
    'iu_latn',
    'iu',
    'ja',
    'ko',
    'nl',
    'pl',
    'pt_ao',
    'pt_br',
    'pt_ch',
    'pt_cv',
    'pt_gq',
    'pt_gw',
    'pt_lu',
    'pt_mo',
    'pt_mz',
    'pt_pt',
    'pt_st',
    'pt_tl',
    'pt',
    'ro',
    'ru',
    'sw_traditional',
    'sw',
    'tr',
    'uk',
    'vi',
    'yo',
    'yrl',
    'zh_cn',
    'zh_hans',
    'zh_hant',
    'zh_hk',
    'zh_latn',
    'zh_mo',
    'zh_sg',
    'zh_tw',
    'zh',
]


@app.route('/api/locale-info')
@app.route('/api/locale-info/<string:locale>')
def locale_info(locale: str = None):
    if locale is not None:
        return _locale_info(locale)

    res = {}

    for locale in LOCALE_LIST:
        res[locale] = _locale_info(locale)

    return res


def _locale_info(locale: str = None) -> dict:
    locale = sezimal_locale(locale)

    res = {
        'lang': locale.LANG,
        'language_name': locale.LANGUAGE,
        'from_icu': str(locale.__class__).split('.')[2] == 'lokale',
        'script': {
            'is_rtl': locale.RTL,
            'ideographic_script': locale.IDEOGRAPHIC,
            'localized_digits': locale.DIGITS,
        },
        'number_format': {
            'sezimal_separator': locale.SEZIMAL_SEPARATOR,
            'group_separator': locale.GROUP_SEPARATOR,
            'subgroup_separator': locale.SUBGROUP_SEPARATOR,
            'fraction_group_separator': locale.FRACTION_GROUP_SEPARATOR,
            'fraction_subgroup_separator': locale.FRACTION_SUBGROUP_SEPARATOR,
        },
        'date_time_localization': {
            'default_time_zone': locale.DEFAULT_TIME_ZONE,
            'first_weekday': locale.FIRST_WEEKDAY,
            'day_of_rest': locale.FIRST_WEEKDAY,
            'optional_day_of_rest': locale.OPTIONAL_DAY_OF_REST,
            'weekday_name': locale.WEEKDAY_NAME,
            'weekday_abbreviated_name': locale.WEEKDAY_ABBREVIATED_NAME,
            'month_name': locale.MONTH_NAME,
            'month_abbreviated_name': locale.MONTH_ABBREVIATED_NAME,
            'era_name': locale.ERA_NAME,
            'day_ordinal_suffix': {},
        },
        'date_time_format': {
            'date_format': locale.DATE_FORMAT,
            'date_long_format': locale.DATE_LONG_FORMAT,
            'time_format': locale.TIME_FORMAT,
            'date_time_format': locale.DATE_TIME_FORMAT,
            'date_time_long_format': locale.DATE_TIME_LONG_FORMAT,
            'dst_name': locale.DST_NAME,
            'dst_short_name': locale.DST_SHORT_NAME,
            'iso_date_format': locale.ISO_DATE_FORMAT,
            'iso_time_format': locale.ISO_TIME_FORMAT,
        },
        'astronomic_events': {
            'default_hemisphere': locale.DEFAULT_HEMISPHERE,
            'season_name': locale.SEASON_NAME,
            'moonphase_name': locale.MOON_PHASE,
        },
    }

    for day in SezimalRange(100):
        od = locale.day_ordinal_suffix(day)

        if od:
            res['date_time_localization']['day_ordinal_suffix'][str(day)] = od

    return res
