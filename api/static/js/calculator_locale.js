
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

    document.documentElement.lang = locale;

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
            return true;
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
                    return true;
                }).catch((e) => {
                    return false;
                });
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
