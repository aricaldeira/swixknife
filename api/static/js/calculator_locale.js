
function toggle_locale() {
    document.getElementById('locale-setting').hidden = !document.getElementById('locale-setting').hidden;
    document.getElementById('toggle_locale').hidden = !document.getElementById('toggle_locale').hidden;
};

function set_locale() {
    const locale = document.getElementById('calculator-sezimal-locale').value;
    localStorage.setItem('sezimal-calculator-locale', locale);

    update_locale();
    toggle_locale();
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
};
