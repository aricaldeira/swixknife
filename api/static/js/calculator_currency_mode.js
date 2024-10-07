
function toggle_currency_mode() {
    const currency_mode = localStorage.getItem('sezimal-calculator-currency-mode');

    if ((currency_mode == null) || (currency_mode == '') || (currency_mode == false)  || (currency_mode == 'false')) {
        localStorage.setItem('sezimal-calculator-currency-mode', true);
    } else {
        localStorage.setItem('sezimal-calculator-currency-mode', false);
    };

    update_currency_mode();
};

function update_currency_mode(calculation_refresh = true) {
    const currency_mode = localStorage.getItem('sezimal-calculator-currency-mode');
    const currency_unit_symbol = localStorage.getItem('sezimal-calculator-currency-unit-symbol');

    if ((currency_mode == null) || (currency_mode == '') || (currency_mode == false)  || (currency_mode == 'false')) {
        document.getElementById('toggle_currency_mode').innerHTML = `[ <span style="color: #666;">${currency_unit_symbol}</span> ]`;
    } else {
        document.getElementById('toggle_currency_mode').innerHTML = `[ ${currency_unit_symbol} ]`;
    };

    update_grouping(false);
    update_sezimal_places(false);

    if (calculation_refresh == true) {
        update_calculation();
    };
};
