
function toggle_spellout() {
    const spellout = localStorage.getItem('sezimal-calculator-spellout');

    if ((spellout == null) || (spellout == '') || (spellout == false)  || (spellout == 'false')) {
        localStorage.setItem('sezimal-calculator-spellout', true);
    } else {
        localStorage.setItem('sezimal-calculator-spellout', false);
    };

    update_spellout();
};

function update_spellout(calculation_refresh = true) {
    const spellout = localStorage.getItem('sezimal-calculator-spellout');

    if ((spellout == null) || (spellout == '') || (spellout == false)  || (spellout == 'false')) {
        document.getElementById('toggle_spellout').innerHTML = '[ ≁<i>txt</i> ]'
    } else {
        document.getElementById('toggle_spellout').innerHTML = '[ ∼<i>txt</i> ]'
    };

    if (calculation_refresh == true) {
        update_calculation();
    };
};
