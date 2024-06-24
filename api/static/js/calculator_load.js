
function calculator_load() {
    /*
    *  First run base definition
    */
    if (localStorage.getItem('sezimal-calculator-base') === null) {
        localStorage.setItem('sezimal-calculator-base', 10);
    };

    /*
    *  First run locale definition
    */
    var locale = localStorage.getItem('sezimal-calculator-locale');
    if (locale === null) {
        locale = navigator.languages && navigator.languages.length
        ? navigator.languages[0]
        : navigator.language;

        locale = locale.replace('-', '_').toLowerCase();
        localStorage.setItem('sezimal-calculator-locale', locale);
        document.getElementById('calculator-sezimal-locale').value = locale;
    } else {
        document.getElementById('calculator-sezimal-locale').value = locale;
    };

    /*
    *  First run spellout definition
    */
    if (localStorage.getItem('sezimal-calculator-spellout') === null) {
        localStorage.setItem('sezimal-calculator-spellout', true);
    };

    /*
    *  First run sezimal digits definition
    */
    if (localStorage.getItem('sezimal-calculator-sezimal-digits') === null) {
        localStorage.setItem('sezimal-calculator-sezimal-digits', false);
    };

    /*
    *  First run grouping definition
    */
    if (localStorage.getItem('sezimal-calculator-grouping') === null) {
        localStorage.setItem('sezimal-calculator-grouping', 3);
    };

    if (localStorage.getItem('sezimal-calculator-sezimal-separator') === null) {
        localStorage.setItem('sezimal-calculator-sezimal-separator', '.');
        document.getElementById('button-sezimal-separator').innerHTML = '.';
        document.getElementById('button-decimal-separator').innerHTML = '.';
    };

    if (localStorage.getItem('sezimal-calculator-group-separator') === null) {
        localStorage.setItem('sezimal-calculator-group-separator', '\u202f');
    };

    /*
    *  First run niftimal definition
    */
    if (localStorage.getItem('sezimal-calculator-niftimal') === null) {
        localStorage.setItem('sezimal-calculator-niftimal', '-');
    };

    /*
    *  First run sezimal places definition
    */
    if (localStorage.getItem('sezimal-calculator-sezimal-places') === null) {
        localStorage.setItem('sezimal-calculator-sezimal-places', 3);
        document.getElementById('calculator-sezimal-places').value = 3;
    } else {
        document.getElementById('calculator-sezimal-places').value = localStorage.getItem('sezimal-calculator-sezimal-places');
    };

    /*
    *  First run unit type definition
    */
    if (unit_type = localStorage.getItem('sezimal-calculator-unit-type') === null) {
        localStorage.setItem('sezimal-calculator-unit-type', 'units');
        localStorage.setItem('sezimal-calculator-unit', '');
        localStorage.setItem('sezimal-calculator-decimal-unit', '');
    };

    if (navigator.userAgentData != undefined && navigator.userAgentData.mobile) {
        document.querySelector("body").requestFullscreen();
    };

    update_base(false);
    update_locale(false);
    update_spellout(false);
    update_grouping(false);
    update_sezimal_digits(false);
    update_niftimal(false);
    update_sezimal_places(false);
    // update_units(false);

    update_calculation();
};