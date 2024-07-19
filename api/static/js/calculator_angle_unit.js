
const sezimal_prefixed_units = [
    'prd',
    'gol',

    'deg',
    'arcmin',
    'arcsec',
    'gon',
    'rad',
    'turn',

    'spat',
    'sr',
];


const decimal_prefixed_units = [
    'deg',
    'arcmin',
    'arcsec',
    'gon',
    'rad',
    'turn',

    'spat',
    'sr',
];


function toggle_angle_units() {
    document.getElementById('angle-unit-setting').hidden = !document.getElementById('angle-unit-setting').hidden;
    document.getElementById('toggle_angle_units').hidden = !document.getElementById('toggle_angle_units').hidden;
    document.getElementById('display').hidden = !document.getElementById('display').hidden;
    document.getElementById('decimal_display').hidden = !document.getElementById('decimal_display').hidden;
    document.getElementById('configuration-left').hidden = !document.getElementById('configuration-left').hidden;
    document.getElementById('configuration-right').hidden = !document.getElementById('configuration-right').hidden;

    if (document.getElementById('toggle_angle_units').hidden) {
        document.getElementById('buttons').style = 'visibility: hidden;';
    } else {
        document.getElementById('buttons').style = 'visibility: visible;';
    };
};

function set_sezimal_angle_unit(select) {
    localStorage.setItem('sezimal-calculator-angle-unit', select.value);

    if (!sezimal_prefixed_units.includes(select.value)) {
        localStorage.setItem('sezimal-calculator-angle-prefix', '-');
    };

    update_angle_units_conversion();
};

function set_sezimal_angle_prefix(select) {
    localStorage.setItem('sezimal-calculator-angle-prefix', select.value);
    update_angle_units_conversion();
};

function set_decimal_angle_unit(select) {
    localStorage.setItem('sezimal-calculator-decimal-angle-unit', select.value);

    if (!decimal_prefixed_units.includes(select.value)) {
        localStorage.setItem('sezimal-calculator-decimal-angle-prefix', '-');
    };

    update_angle_units_conversion();
};

function set_decimal_angle_prefix(select) {
    localStorage.setItem('sezimal-calculator-decimal-angle-prefix', select.value);
    update_angle_units_conversion();
};


function update_angle_units_conversion() {
    let sezimal_unit = localStorage.getItem('sezimal-calculator-angle-unit');
    let sezimal_prefix = localStorage.getItem('sezimal-calculator-angle-prefix');
    let decimal_unit = localStorage.getItem('sezimal-calculator-decimal-angle-unit');
    let decimal_prefix = localStorage.getItem('sezimal-calculator-decimal-angle-prefix');

    document.getElementById('calculator-sezimal-unit-angle-prd').value = sezimal_unit;
    document.getElementById('calculator-prefix-sezimal-angle').value = sezimal_prefix;
    document.getElementById('calculator-decimal-angle-unit-prd').value = decimal_unit;
    document.getElementById('calculator-prefix-decimal-angle').value = decimal_prefix;

    show_sezimal_decimal_angle_prefix(sezimal_unit, decimal_unit);

    if ((sezimal_prefix == '-') || (sezimal_prefix == null)) {
        sezimal_prefix = '';
    };
    if ((decimal_prefix == '-') || (decimal_prefix == null)) {
        decimal_prefix = '';
    };

    if (localStorage.getItem(`sezimal-translation-display-${sezimal_unit}`) != null) {
        sezimal_unit = localStorage.getItem(`sezimal-translation-display-${sezimal_unit}`);
    };
    if (localStorage.getItem(`sezimal-translation-display-${decimal_unit}`) != null) {
        decimal_unit = localStorage.getItem(`sezimal-translation-display-${decimal_unit}`);
    };

    document.getElementById('toggle_angle_units').innerHTML = '[ ' + sezimal_prefix + sezimal_unit + ' ◕ ' + decimal_prefix + decimal_unit + ' ]';
};


function show_sezimal_decimal_angle_prefix(sezimal_unit, decimal_unit) {
    document.getElementById('label-prefix-sezimal-angle').hidden = !sezimal_prefixed_units.includes(sezimal_unit);
    document.getElementById('calculator-prefix-sezimal-angle').hidden = !sezimal_prefixed_units.includes(sezimal_unit);

    document.getElementById('label-prefix-decimal-angle').hidden = !decimal_prefixed_units.includes(decimal_unit);
    document.getElementById('calculator-prefix-decimal-angle').hidden = !decimal_prefixed_units.includes(decimal_unit);
};
