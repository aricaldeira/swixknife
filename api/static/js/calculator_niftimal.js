
function toggle_niftimal() {
    const sezimal_digits = localStorage.getItem('sezimal-calculator-sezimal-digits');
    var niftimal_type = localStorage.getItem('sezimal-calculator-niftimal');

    if ((niftimal_type == null) || (niftimal_type == '') || (niftimal_type == '-')) {
        niftimal_type = '5';
    } else if (niftimal_type == '5') {
        niftimal_type = 'Z';
    } else if (niftimal_type == 'Z') {
        niftimal_type = '-';
    };

    localStorage.setItem('sezimal-calculator-niftimal', niftimal_type);

    update_niftimal();
};

function update_niftimal(calculation_refresh = true) {
    const niftimal_type = localStorage.getItem('sezimal-calculator-niftimal');
    const sezimal_digits = localStorage.getItem('sezimal-calculator-sezimal-digits');
    let nif_translation = localStorage.getItem('sezimal-translation-nif');

    if (nif_translation == null) {
        nif_translation = 'nif';
    }

    if (niftimal_type == '5') {
        if ((sezimal_digits == 'true') || (sezimal_digits == true)) {
            document.getElementById('toggle_niftimal').innerHTML = `[ ${nif_translation} 󱸣 ]`;
        } else {
            document.getElementById('toggle_niftimal').innerHTML = `[ ${nif_translation} 5̆ ]`;
        };
        document.getElementById('niftimal_display').hidden = false;
    } else if (niftimal_type == 'Z') {
        document.getElementById('toggle_niftimal').innerHTML = `[ ${nif_translation} Z ]`
        document.getElementById('niftimal_display').hidden = false;
    } else if ((niftimal_type == null) || (niftimal_type == '') || (niftimal_type == '-')) {
        document.getElementById('toggle_niftimal').innerHTML = `[ <span style="text-decoration: line-through;">${nif_translation}</span> ]`
        document.getElementById('niftimal_display').hidden = true;
    };

    if (calculation_refresh == true) {
        update_calculation();
    };
};
