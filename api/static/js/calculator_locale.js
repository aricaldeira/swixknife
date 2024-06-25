
let locales_text = {};

function toggle_locale() {
    document.getElementById('locale-setting').hidden = !document.getElementById('locale-setting').hidden;
    document.getElementById('toggle_locale').hidden = !document.getElementById('toggle_locale').hidden;
};

function update_locale(calculation_refresh = true) {
    const locale = localStorage.getItem('sezimal-calculator-locale');

    if (locale.search('_')) {
        parts = locale.split('_');
        document.getElementById('toggle_locale').innerHTML = '[ ' + parts[0] + ' ]';
    } else if (locale.search('-')) {
        parts = locale.split('-');
        document.getElementById('toggle_locale').innerHTML = '[ ' + parts[0] + ' ]';
    } else {
        document.getElementById('toggle_locale').innerHTML = '[ ' + locale + ' ]';
    };

    if (calculation_refresh == true) {
        update_calculation();
        update_grouping(false);
        update_sezimal_places(false);
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
                    _assign_ids_text(locales_text[locale]);
                    return true;
                }).catch((e) => {
                    return false;
                });
            };
        });
    };
}

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
        } else {
            document.getElementById(element_id).innerHTML = translation[element_id];
        }
    });
};
