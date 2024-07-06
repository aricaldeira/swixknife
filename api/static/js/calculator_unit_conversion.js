
const prefixed_units = [
    'A',
    'Ah',
    'As',
    'B',
    'B/min',
    'B/s',
    'BTU',
    'Bpm',
    'Bps',
    'C',
    'F',
    'H',
    'Hz',
    'J',
    'J/K',
    'J/K/kg',
    'J/K/m3',
    'K',
    'L',
    'N',
    'Pa',
    'S',
    'T',
    'TNT',
    'V',
    'W',
    'Wb',
    'Wh',
    'a',
    'arcmin',
    'arcsec',
    'b',
    'bar',
    'bit',
    'bit/min',
    'bit/s',
    'bpm',
    'bps',
    'cal',
    'day',
    'e',
    'eV',
    'erg',
    'g',
    'g/L',
    'g/l',
    'g/m3',
    'gf',
    'gon',
    'h',
    'l',
    'm',
    'm/h',
    'm/s',
    'm/s2',
    'm2',
    'm3',
    'min',
    'month',
    'ohm',
    'psi',
    'rad',
    's',
    'spat',
    'sr',
    'turn',
    'week',
    'year',
    'Ω',
];


function toggle_units(show) {
    if (show) {
        document.getElementById('units').hidden = false;
        document.getElementById('displays').hidden = true;
        // document.getElementById('buttons').hidden = true;
        document.getElementById('buttons').style = 'visibility: hidden;';
    } else {
        document.getElementById('units').hidden = true;
        document.getElementById('displays').hidden = false;
        // document.getElementById('buttons').hidden = false;
        document.getElementById('buttons').style = 'visibility: visible;';
        update_calculation();
    };
};

function set_unit_type() {
    const unit_type = document.getElementById('calculator-sezimal-unit-type').value;

    if (unit_type == 'ang') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'agm', '-', 's');
    } else if (unit_type == 'avt') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'avt', '-', 'Hz');
    } else if (unit_type == 'pad') {
        set_unit_type_sezimal_decimal(unit_type, 'D', 'pad', '-', 'm');
    } else if (unit_type == 'kex') {
        set_unit_type_sezimal_decimal(unit_type, 'D', 'kex', '-', 'm2');
    } else if (unit_type == 'ayt') {
        set_unit_type_sezimal_decimal(unit_type, 'D', 'ayt', '-', 'L');
    } else if (unit_type == 'veg') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'veg', 'k', 'm/h');
    } else if (unit_type == 'tvr') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'tvr', '-', 'm/s2');
    } else if (unit_type == 'drv') {
        set_unit_type_sezimal_decimal(unit_type, 'D', 'drv', 'k', 'g');
    } else if (unit_type == 'gan') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'gan', 'k', 'g/L');
    } else if (unit_type == 'bar') {
        set_unit_type_sezimal_decimal(unit_type, 'D', 'bar', '-', 'N');
    } else if (unit_type == 'dab') {
        set_unit_type_sezimal_decimal(unit_type, 'D', 'dab', 'k', 'Pa');
    } else if (unit_type == 'kry') {
        set_unit_type_sezimal_decimal(unit_type, 'DX', 'kry', 'k', 'Wh');
    } else if (unit_type == 'xat') {
        set_unit_type_sezimal_decimal(unit_type, 'D', 'xat', '-', 'W');
    } else if (unit_type == 'gtk') {
        set_unit_type_sezimal_decimal(unit_type, 'X', 'gtk', '-', 'K');
    } else if (unit_type == 'tap') {
        set_unit_type_sezimal_decimal(unit_type, '', 'tap', '', '°C');
    } else if (unit_type == 'agn') {
        set_unit_type_sezimal_decimal(unit_type, '', 'agn', '', 'J/K');
    } else if (unit_type == 'idn') {
        set_unit_type_sezimal_decimal(unit_type, '', 'idn', '', 'J/K/kg');
    } else if (unit_type == 'tln') {
        set_unit_type_sezimal_decimal(unit_type, '', 'tln', '', 'J/K/m3');
    } else if (unit_type == 'avx') {
        set_unit_type_sezimal_decimal(unit_type, 'X', 'avx', 'm', 'Ah');
    } else if (unit_type == 'dar') {
        set_unit_type_sezimal_decimal(unit_type, 'T', 'dar', '-', 'A');
    } else if (unit_type == 'vbv') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'vbv', '-', 'V');
    } else if (unit_type == 'ptr') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'ptr', '-', 'Ω');
    } else if (unit_type == 'cln') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'cln', '-', 'S');
    } else if (unit_type == 'prk') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'prk', '-', 'H');
    } else if (unit_type == 'sam') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'sam', '-', 'F');
    } else if (unit_type == 'abv') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'abv', '-', 'Wb');
    } else if (unit_type == 'vtr') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'vtr', '-', 'T');
    } else if (unit_type == 'prd') {
        set_unit_type_sezimal_decimal(unit_type, 't', 'prd', '-', 'deg');
    } else if (unit_type == 'gol') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'gol', '-', 'sr');
    } else if (unit_type == 'prt') {
        set_unit_type_sezimal_decimal(unit_type, 'd', 'prt', '-', '%');
    } else if (unit_type == 'atk') {
        set_unit_type_sezimal_decimal(unit_type, 'DX', 'atk', 'Gi', 'B');
    } else if (unit_type == 'pvn') {
        set_unit_type_sezimal_decimal(unit_type, 'X', 'pvn', 'M', 'bps');
    } else {
        set_unit_type_sezimal_decimal(unit_type, '-', '', '-', '');
    };
};

function set_sezimal_unit(select) {
    localStorage.setItem('sezimal-calculator-unit', select.value);
    update_units_conversion();
};

function set_sezimal_prefix(select) {
    localStorage.setItem('sezimal-calculator-prefix', select.value);
    update_units_conversion();
};

function set_decimal_unit(select) {
    localStorage.setItem('sezimal-calculator-decimal-unit', select.value);
    update_units_conversion();
};

function set_decimal_prefix(select) {
    localStorage.setItem('sezimal-calculator-decimal-prefix', select.value);
    update_units_conversion();
};

function set_unit_type_sezimal_decimal(unit_type, sezimal_prefix, sezimal_unit, decimal_prefix, decimal_unit) {
    localStorage.setItem('sezimal-calculator-unit-type', unit_type);
    localStorage.setItem('sezimal-calculator-prefix', sezimal_prefix);
    localStorage.setItem('sezimal-calculator-unit', sezimal_unit);
    localStorage.setItem('sezimal-calculator-decimal-prefix', decimal_prefix);
    localStorage.setItem('sezimal-calculator-decimal-unit', decimal_unit);

    if ((sezimal_prefix == '-') || (sezimal_prefix == null)) {
        sezimal_prefix = '-';
    };
    if ((decimal_prefix == '-') || (decimal_prefix == null)) {
        decimal_prefix = '-';
    };

    hide_all_units();

    if (unit_type == 'units') {
        document.getElementById('unit-units-explanation').hidden = false;
        document.getElementById('toggle_units').innerHTML = '[ ↮ ]';
    } else if (unit_type == 'prefixes') {
        document.getElementById('unit-prefixes-explanation').hidden = false;
        document.getElementById('toggle_units').innerHTML = '[ ↮ ]';
    } else {
        document.getElementById('units-title').hidden = false;

        show_decimal_binary_prefix(sezimal_unit, decimal_unit);

        document.getElementById(`unit-${unit_type}-explanation`).hidden = false;
        document.getElementById(`unit-${unit_type}`).hidden = false;
        document.getElementById('calculator-prefix-sezimal').value = sezimal_prefix;
        document.getElementById(`calculator-sezimal-unit-${unit_type}`).value = sezimal_unit;
        document.getElementById('calculator-prefix-decimal').value = decimal_prefix;
        document.getElementById(`calculator-decimal-unit-${unit_type}`).value = decimal_unit;
    };

    update_units_conversion();
};

function update_units_conversion() {
    let sezimal_prefix = localStorage.getItem('sezimal-calculator-prefix');
    let sezimal_unit = localStorage.getItem('sezimal-calculator-unit');
    let decimal_prefix = localStorage.getItem('sezimal-calculator-decimal-prefix');
    let decimal_unit = localStorage.getItem('sezimal-calculator-decimal-unit');

    show_decimal_binary_prefix(sezimal_unit, decimal_unit);

    if ((sezimal_prefix == '-') || (sezimal_prefix == null)) {
        sezimal_prefix = '';
    };
    if ((decimal_prefix == '-') || (decimal_prefix == null)) {
        decimal_prefix = '';
    };

    if (localStorage.getItem(`sezimal-translation-${sezimal_unit}`) != null) {
        sezimal_unit = localStorage.getItem(`sezimal-translation-${sezimal_unit}`);
    };
    if (localStorage.getItem(`sezimal-translation-${decimal_unit}`) != null) {
        decimal_unit = localStorage.getItem(`sezimal-translation-${decimal_unit}`);
    };

    document.getElementById('toggle_units').innerHTML = '[ ' + sezimal_prefix + sezimal_unit + ' ↔ ' + decimal_prefix + decimal_unit + ' ]';
};

function show_decimal_binary_prefix(sezimal_unit, decimal_unit) {
    if ((sezimal_unit == 'atk') || (sezimal_unit == 'pvn')) {
        document.getElementById('label-prefix-decimal-binary').hidden = false;
        document.getElementById('calculator-prefix-decimal').hidden = false;
        document.getElementsByName('optgroup-units-generic-binary')[0].hidden = false;
    } else if ((decimal_unit == '') || (prefixed_units.includes(decimal_unit))) {
        document.getElementById('label-prefix-decimal').hidden = false;
        document.getElementById('calculator-prefix-decimal').hidden = false;
        document.getElementsByName('optgroup-units-generic-binary')[0].hidden = true;
    } else {
        document.getElementById('label-prefix-decimal').hidden = true;
        document.getElementById('calculator-prefix-decimal').hidden = true;
        document.getElementById('calculator-prefix-decimal').value = '-';
        document.getElementsByName('optgroup-units-generic-binary')[0].hidden = true;
    };
};

function hide_all_units() {
    document.getElementById('unit-units-explanation').hidden = true;
    document.getElementById('unit-prefixes-explanation').hidden = true;
    document.getElementById('units-title').hidden = true;

    document.getElementById('unit-ang-explanation').hidden = true;
    document.getElementById('unit-ang').hidden = true;
    document.getElementById('unit-avt-explanation').hidden = true;
    document.getElementById('unit-avt').hidden = true;
    document.getElementById('unit-pad-explanation').hidden = true;
    document.getElementById('unit-pad').hidden = true;
    document.getElementById('unit-kex-explanation').hidden = true;
    document.getElementById('unit-kex').hidden = true;
    document.getElementById('unit-ayt-explanation').hidden = true;
    document.getElementById('unit-ayt').hidden = true;
    document.getElementById('unit-drv-explanation').hidden = true;
    document.getElementById('unit-drv').hidden = true;
    document.getElementById('unit-gan-explanation').hidden = true;
    document.getElementById('unit-gan').hidden = true;
    document.getElementById('unit-veg-explanation').hidden = true;
    document.getElementById('unit-veg').hidden = true;
    document.getElementById('unit-tvr-explanation').hidden = true;
    document.getElementById('unit-tvr').hidden = true;
    document.getElementById('unit-bar-explanation').hidden = true;
    document.getElementById('unit-bar').hidden = true;
    document.getElementById('unit-dab-explanation').hidden = true;
    document.getElementById('unit-dab').hidden = true;
    document.getElementById('unit-kry-explanation').hidden = true;
    document.getElementById('unit-kry').hidden = true;
    document.getElementById('unit-xat-explanation').hidden = true;
    document.getElementById('unit-xat').hidden = true;
    document.getElementById('unit-gtk-explanation').hidden = true;
    document.getElementById('unit-gtk').hidden = true;
    document.getElementById('unit-tap-explanation').hidden = true;
    document.getElementById('unit-tap').hidden = true;
    document.getElementById('unit-agn-explanation').hidden = true;
    document.getElementById('unit-agn').hidden = true;
    document.getElementById('unit-idn-explanation').hidden = true;
    document.getElementById('unit-idn').hidden = true;
    document.getElementById('unit-tln-explanation').hidden = true;
    document.getElementById('unit-tln').hidden = true;
    document.getElementById('unit-avx-explanation').hidden = true;
    document.getElementById('unit-avx').hidden = true;
    document.getElementById('unit-dar-explanation').hidden = true;
    document.getElementById('unit-dar').hidden = true;
    document.getElementById('unit-vbv-explanation').hidden = true;
    document.getElementById('unit-vbv').hidden = true;
    document.getElementById('unit-ptr-explanation').hidden = true;
    document.getElementById('unit-ptr').hidden = true;
    document.getElementById('unit-cln-explanation').hidden = true;
    document.getElementById('unit-cln').hidden = true;
    document.getElementById('unit-prk-explanation').hidden = true;
    document.getElementById('unit-prk').hidden = true;
    document.getElementById('unit-sam-explanation').hidden = true;
    document.getElementById('unit-sam').hidden = true;
    document.getElementById('unit-abv-explanation').hidden = true;
    document.getElementById('unit-abv').hidden = true;
    document.getElementById('unit-vtr-explanation').hidden = true;
    document.getElementById('unit-vtr').hidden = true;
    document.getElementById('unit-prd-explanation').hidden = true;
    document.getElementById('unit-prd').hidden = true;
    document.getElementById('unit-gol-explanation').hidden = true;
    document.getElementById('unit-gol').hidden = true;
    document.getElementById('unit-prt-explanation').hidden = true;
    document.getElementById('unit-prt').hidden = true;
    document.getElementById('unit-atk-explanation').hidden = true;
    document.getElementById('unit-atk').hidden = true;
    document.getElementById('unit-pvn-explanation').hidden = true;
    document.getElementById('unit-pvn').hidden = true;
};
