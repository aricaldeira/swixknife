
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
    const txt_translation = localStorage.getItem('sezimal-translation-txt');

    if ((spellout == null) || (spellout == '') || (spellout == false)  || (spellout == 'false')) {
        document.getElementById('toggle_spellout').innerHTML = `[ <span style="text-decoration: line-through;">${txt_translation}</span> ]`
    } else {
        document.getElementById('toggle_spellout').innerHTML = `[ ${txt_translation} ]`
    };

    if (calculation_refresh == true) {
        update_calculation();
    };
};
