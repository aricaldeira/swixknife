
function toggle_base_ten() {
    localStorage.setItem('sezimal-calculator-base', 14);
    update_base();
};

function toggle_base_six() {
    localStorage.setItem('sezimal-calculator-base', 10);
    update_base();
};

function update_base(calculation_refresh = true) {
    if (localStorage.getItem('sezimal-calculator-base') == 14) {
        document.getElementById('sezimal-buttons-table').hidden = true;
        document.getElementById('decimal-buttons-table').hidden = false;
        document.getElementById('display').classList.add('decimal_display');
        document.getElementById('display').classList.remove('display');
        document.getElementById('decimal_display').classList.add('display');
        document.getElementById('decimal_display').classList.remove('decimal_display');
    } else {
        document.getElementById('sezimal-buttons-table').hidden = false;
        document.getElementById('decimal-buttons-table').hidden = true;
        document.getElementById('display').classList.add('display');
        document.getElementById('display').classList.remove('decimal_display');
        document.getElementById('decimal_display').classList.add('decimal_display');
        document.getElementById('decimal_display').classList.remove('display');
    };

    if (calculation_refresh == true) {
        update_calculation();
    };
};
