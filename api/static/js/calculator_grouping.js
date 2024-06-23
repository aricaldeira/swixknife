
function toggle_grouping() {
    const grouping = localStorage.getItem('sezimal-calculator-grouping');

    if ((grouping == null) || (grouping == '') || (grouping == 4)) {
        localStorage.setItem('sezimal-calculator-grouping', 3);
    } else {
        localStorage.setItem('sezimal-calculator-grouping', 4);
    };

    update_grouping();
};

function update_grouping(calculation_refresh = true) {
    const grouping = localStorage.getItem('sezimal-calculator-grouping');
    const separator = localStorage.getItem('sezimal-calculator-group-separator');
    const sezimal_digits = localStorage.getItem('sezimal-calculator-sezimal-digits');

    if (grouping == 3) {
        if (sezimal_digits == 'true') {
            document.getElementById('toggle_grouping').innerHTML = '[ 󱸃' + separator + '󱸃 ]';
        } else {
            document.getElementById('toggle_grouping').innerHTML = '[ 3' + separator + '3 ]';
        };
    } else {
        if (sezimal_digits == 'true') {
            document.getElementById('toggle_grouping').innerHTML = '[ 󱸄' + separator + '󱸄 ]';
        } else {
            document.getElementById('toggle_grouping').innerHTML = '[ 4' + separator + '4 ]';
        };
    };

    if (calculation_refresh == true) {
        update_calculation();
    };
};
