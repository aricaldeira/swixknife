
const LANGUAGE_TAGS = {
    'ar_latn': 'ar-Latn',
    'ar': 'ar',
    'ar_nu_latn': 'ar-u-nu-Latn',
    'bn_latn': 'bn-Latn',
    'bn': 'bn',
    'bn_nu_latn': 'bn-u-nu-Latn',
    'bz_br': 'bz-BR',
    'bz_pt': 'bz-PT',
    'bz': 'bz',
    'ca': 'ca',
    'code': 'code',
    'da': 'da',
    'de_at': 'de-AT',
    'de_be': 'de-BE',
    'de_de': 'de-DE',
    'de_it': 'de-IT',
    'de_li': 'de-LI',
    'de_lu': 'de-LU',
    'de': 'de',
    'el': 'el',
    'el_colloquial': 'el',
    'en_au': 'en-AU',
    'en_br': 'en-BR',
    'en_ca': 'en-CA',
    'en_gb': 'en-GB',
    'en_gb-metric': 'en-GB-metric',
    'en_ie': 'en-IE',
    'en_in': 'en-IN',
    'en_nyoo_speling': 'en-NYOO-SPELING',
    'en_nz': 'en-NZ',
    'en_shaw': 'en-Shaw',
    'en_us': 'en-US',
    'en_us-metric': 'en-US-metric',
    'en_za': 'en-ZA',
    'en': 'en',
    'eo_br': 'eo-BR',
    'eo': 'eo',
    'es_ar': 'es-AR',
    'es_bo': 'es-BO',
    'es_cl': 'es-CL',
    'es_co': 'es-CO',
    'es_ec': 'es-EC',
    'es_es': 'es-ES',
    'es_mx': 'es-MX',
    'es_pe': 'es-PE',
    'es_py': 'es-PY',
    'es_uy': 'es-UY',
    'es': 'es',
    'et': 'et',
    'fa_latn': 'fa-Latn',
    'fa': 'fa',
    'fa_nu_latn': 'fa-u-nu-Latn',
    'fi': 'fi',
    'fr_be': 'fr-BE',
    'fr_ca': 'fr-CA',
    'fr_ch': 'fr-CH',
    'fr_fr': 'fr-FR',
    'fr_lu': 'fr-LU',
    'fr_ortograf': 'fr-Ortograf',
    'fr': 'fr',
    'ga_clo_gaelach': 'ga-CLO-GAELACH',
    'ga_traditional': 'ga-Traditional',
    'ga': 'ga',
    'gl': 'gl',
    'gn': 'gn',
    'he_latn': 'he-Latn',
    'he': 'he',
    'hi_latn': 'hi-Latn',
    'hi': 'hi',
    'hi_nu_latn': 'hi-u-nu-Latn',
    'hu': 'hu',
    'id': 'id',
    'is': 'is',
    'iso_dot': 'iso-Dot',
    'iso': 'iso',
    'it': 'it',
    'iu_latn': 'iu-Latn',
    'iu': 'iu',
    'ja': 'ja',
    'kea': 'kea',
    'kn': 'kn',
    'kn_nu_latn': 'kn-u-nu-Latn',
    'ko': 'ko',
    'lat': 'lat',
    'lb': 'lb',
    'mt': 'mt',
    'nb': 'nb',
    'nl_be': 'nl-BE',
    'nl': 'nl-NL',
    'nn': 'nn',
    'pl': 'pl',
    'pt_ao': 'pt-AO',
    'pt_br': 'pt-BR',
    'pt_ch': 'pt-CH',
    'pt_cv': 'pt-CV',
    'pt_gq': 'pt-GQ',
    'pt_gw': 'pt-GW',
    'pt_lu': 'pt-LU',
    'pt_mo': 'pt-MO',
    'pt_mz': 'pt-MZ',
    'pt_pt': 'pt-PT',
    'pt_st': 'pt-ST',
    'pt_tl': 'pt-TL',
    'pt': 'pt',
    'ro': 'ro',
    'ru': 'ru',
    'sv_fi': 'sv-FI',
    'sv_se': 'sv-SE',
    'sv': 'sv',
    'sw_traditional': 'sw-Traditional',
    'sw': 'sw',
    'tr': 'tr',
    'uk': 'uk',
    'vi': 'vi',
    'yo': 'yo',
    'yrl': 'yrl',
    'zh_cn': 'zh-CN',
    'zh_hans': 'zh-Hans',
    'zh_hant': 'zh-Hant',
    'zh_hk': 'zh-HK',
    'zh_latn': 'zh-Latn',
    'zh_mo': 'zh-MO',
    'zh_sg': 'zh-SG',
    'zh_tw': 'zh-TW',
    'zh': 'zh',
}

let locales_text = {};
let locales_display = {};

function toggle_locale() {
    document.getElementById('locale-setting').hidden = !document.getElementById('locale-setting').hidden;
    document.getElementById('toggle_locale').hidden = !document.getElementById('toggle_locale').hidden;
    document.getElementById('displays').hidden = !document.getElementById('displays').hidden;
    document.getElementById('configuration-left').hidden = !document.getElementById('configuration-left').hidden;
    document.getElementById('configuration-right').hidden = !document.getElementById('configuration-right').hidden;

    if (document.getElementById('toggle_locale').hidden) {
        document.getElementById('buttons').style = 'visibility: hidden;';
    } else {
        document.getElementById('buttons').style = 'visibility: visible;';
    };

};

function update_locale(calculation_refresh = true) {
    const locale = localStorage.getItem('sezimal-calculator-locale');

    document.documentElement.lang = LANGUAGE_TAGS[locale];

    if (locale.search('_')) {
        parts = locale.split('_');
        document.getElementById('toggle_locale').innerHTML = '[ ' + parts[0] + ' ]';
    } else if (locale.search('-')) {
        parts = locale.split('-');
        document.getElementById('toggle_locale').innerHTML = '[ ' + parts[0] + ' ]';
    } else {
        document.getElementById('toggle_locale').innerHTML = '[ ' + locale + ' ]';
    };

    if (calculation_refresh == true) {
        update_calculation();
        update_grouping(false);
        update_sezimal_places(false);
        update_spellout(false);
        update_niftimal(false);
        update_currency_mode(false);
    };

    load_translation();
};

function set_locale() {
    const locale = document.getElementById('calculator-sezimal-locale').value;
    localStorage.setItem('sezimal-calculator-locale', locale);

    update_locale();
    toggle_locale();
};

function load_translation(first_run = false) {
    let locale = localStorage.getItem('sezimal-calculator-locale');

    if (first_run == true) {
        locale = 'en';
    };

    if ((locale == 'iso') || (locale == 'iso_dot') || (locale == 'code')) {
        locale = 'en';
    };

    if (locale in locales_text) {
        _assign_ids_text(locales_text[locale]);
    } else {
        import(`./locale/${locale}.js`).then((response) => {
            return response[`sezimal_calculator_${locale}_text`];
        }).then((sezimal_calculator_text) => {
            if (locale == 'en') {
                locales_text[locale] = sezimal_calculator_text;
            } else {
                locales_text[locale] = Object.assign({}, locales_text['en']);
                locales_text[locale] = Object.assign(locales_text[locale], sezimal_calculator_text);
            };
            _store_display_translation(locale, locales_text[locale]);
            _assign_ids_text(locales_text[locale]);
        })
        .catch((e) => {
            if (locale.search('_')) {
                import(`./locale/${locale.split('_')[0]}.js`).then((response) => {
                    return response[`sezimal_calculator_${locale.split('_')[0]}_text`];
                }).then((sezimal_calculator_text) => {
                    locales_text[locale] = Object.assign({}, locales_text['en']);
                    locales_text[locale] = Object.assign(locales_text[locale], sezimal_calculator_text);
                    _store_display_translation(locale, locales_text[locale]);
                    _assign_ids_text(locales_text[locale]);
                }).catch((e) => {
                    locales_text[locale] = Object.assign({}, locales_text['en']);
                    _store_display_translation(locale, locales_text[locale]);
                    _assign_ids_text(locales_text[locale]);
                });
            } else {
                locales_text[locale] = Object.assign({}, locales_text['en']);
                _store_display_translation(locale, locales_text[locale]);
                _assign_ids_text(locales_text[locale]);
            };
        });
    };
}

function _store_display_translation(locale, translation) {
    if ((locale === undefined) || (translation === undefined)) {
        return false;
    };

    if (locale !== 'en') {
        locales_display[locale] = Object.assign({}, locales_display['en']);
    } else {
        locales_display[locale] = {};
    };

    let key;

    Object.keys(translation).forEach((element_id) => {
        if (element_id.includes('translation-display-')) {
            key = element_id.replace('translation-display-', '');
            locales_display[locale][key] = translation[element_id];
        };
    });
};

function translate_display(display) {
    const locale = localStorage.getItem('sezimal-calculator-locale');

    if (locales_display[locale] === undefined) {
        return display;
    };

    Object.keys(locales_display[locale]).forEach((key) => {
        display = display.replace(key.replace('-', ' '), locales_display[locale][key]);
    });

    return display;
};

function _assign_ids_text(translation) {
    if (translation === undefined) {
        return false;
    };

    Object.keys(translation).forEach((element_id) => {
        if (element_id.includes('option-')) {
            if (element_id.endsWith('-value')) {
                document.getElementsByName(element_id.replace('-value', '')).forEach((element) => {
                    element.value = translation[element_id];
                });
            } else {
                document.getElementsByName(element_id).forEach((element) => {
                    element.innerHTML = translation[element_id];
                });
            };
        } else if (element_id.includes('optgroup-')) {
            document.getElementsByName(element_id).forEach((element) => {
                element.label = translation[element_id];
            });
        } else if (element_id.includes('translation-')) {
            localStorage.setItem(`sezimal-${element_id}`, translation[element_id]);
            if (element_id == 'translation-txt') {
                update_spellout(false);
            } else if (element_id == 'translation-nif') {
                update_niftimal(false);
            } else {
                document.getElementsByName(element_id.replace('translation-', '')).forEach((element) => {
                    element.innerHTML = translation[element_id];
                });
            };
        } else {
            if (document.getElementById(element_id) == null) {
                // console.log('elemento não encontrado', element_id);
            } else {
                document.getElementById(element_id).innerHTML = translation[element_id];
            };
        }
    });
};
