
function toggle_sezimal_places() {
    document.getElementById('sezimal-places-setting').hidden = !document.getElementById('sezimal-places-setting').hidden;
    document.getElementById('toggle_sezimal_places').hidden = !document.getElementById('toggle_sezimal_places').hidden;
};

function set_sezimal_places() {
    const sezimal_places = document.getElementById('calculator-sezimal-places').value;
    localStorage.setItem('sezimal-calculator-sezimal-places', sezimal_places);

    update_sezimal_places();
    toggle_sezimal_places();
};

function less_sezimal_places() {
    var sezimal_places = localStorage.getItem('sezimal-calculator-sezimal-places');

    if ((sezimal_places == null) || (sezimal_places == false) || (sezimal_places == 0)) {
        localStorage.setItem('sezimal-calculator-sezimal-places', 0);
    } else {
        sezimal_places = parseInt(sezimal_places.toString(), 6);
        sezimal_places = sezimal_places - 1;
        localStorage.setItem('sezimal-calculator-sezimal-places', parseInt(sezimal_places.toString(6)));
    };

    update_sezimal_places();
};

function more_sezimal_places() {
    var sezimal_places = localStorage.getItem('sezimal-calculator-sezimal-places');

    if (sezimal_places == null) {
        localStorage.setItem('sezimal-calculator-sezimal-places', 1);
    } else if (sezimal_places == 33) {
        localStorage.setItem('sezimal-calculator-sezimal-places', 33);
    } else {
        sezimal_places = parseInt(sezimal_places.toString(), 6);
        sezimal_places = sezimal_places + 1;
        localStorage.setItem('sezimal-calculator-sezimal-places', parseInt(sezimal_places.toString(6)));
    };

    update_sezimal_places();
};

function update_sezimal_places(calculation_refresh = true) {
    var sezimal_places = localStorage.getItem('sezimal-calculator-sezimal-places');
    const sezimal_digits = localStorage.getItem('sezimal-calculator-sezimal-digits');
    let separator;

    if (sezimal_digits == 'true') {
        separator = '󱹭'
    } else {
        separator = document.getElementById('button-sezimal-separator').innerHTML;
    };

    if (sezimal_places == 0) {
        if (sezimal_digits == 'true') {
            document.getElementById('toggle_sezimal_places').innerHTML = '[ 󱸀 ]';
        } else {
            document.getElementById('toggle_sezimal_places').innerHTML = '[ 0 ]';
        };
    } else {
        sezimal_places = sezimal_places.toString();
        sezimal_places = '[ 0' + separator + sezimal_places + ' ]';

        if (sezimal_digits == 'true') {
            sezimal_places = sezimal_places.replace('0', '󱸀');
            sezimal_places = sezimal_places.replace('1', '󱸁');
            sezimal_places = sezimal_places.replace('2', '󱸂');
            sezimal_places = sezimal_places.replace('3', '󱸃');
            sezimal_places = sezimal_places.replace('4', '󱸄');
            sezimal_places = sezimal_places.replace('5', '󱸅');
        };

        document.getElementById('toggle_sezimal_places').innerHTML = sezimal_places;
    };

    if (calculation_refresh == true) {
        update_calculation();
    };
};
