
// const SHASTADARI_LOGO = '⬢';
const SHASTADARI_LOGO = ' <img src="https://midia.tauga.online/img/sezimal/shastadari-logo-black-on-white-small.svg" width="12rem" /> ';

const prefixed_units = [
    'A',
    'a',
    'A·h',
    'arcmin',
    'arcsec',
    'As',
    'B',
    'b',
    'B/min',
    'B/s',
    'bar',
    'bit',
    'bit/min',
    'bit/s',
    'Bpm',
    'bpm',
    'Bps',
    'bps',
    'Bq',
    'BTU',
    'C',
    'Cal',
    'cal',
    'cd',
    'Da',
    'day',
    'deg',
    'e',
    'erg',
    'eV',
    'F',
    'g·m/s',
    'g·m/s2',
    'g',
    'g/L',
    'g/l',
    'g/m3',
    'Gal',
    'gf',
    'gon',
    'H',
    'h',
    'Hz',
    'J',
    'J·s',
    'J/g',
    'J/Hz',
    'J/K',
    'J/Kg',
    'J/K/kg',
    'J/K/m3',
    'K',
    'L',
    'l',
    'lm',
    'lm/W',
    'm',
    'm/h',
    'm/s',
    'm/s2',
    'm2',
    'm3',
    'min',
    'mol',
    'month',
    'N·s',
    'N',
    'ohm',
    'Pa',
    'psi',
    'rad',
    'S',
    's',
    'spat',
    'sr',
    'T',
    'TNT',
    'Torr',
    'turn',
    'V',
    'W·h',
    'W',
    'Wb',
    'week',
    'year',
    'Ω',
];


function toggle_units(show) {
    if (show) {
        document.getElementById('units').hidden = false;
        document.getElementById('displays').hidden = true;
        document.getElementById('configuration-left').hidden = true;
        document.getElementById('configuration-right').hidden = true;
        document.getElementById('buttons').style = 'visibility: hidden;';
    } else {
        document.getElementById('units').hidden = true;
        document.getElementById('displays').hidden = false;
        document.getElementById('configuration-left').hidden = false;
        document.getElementById('configuration-right').hidden = false;
        document.getElementById('buttons').style = 'visibility: visible;';
        update_calculation();
    };
};

function set_unit_type() {
    const unit_type = document.getElementById('calculator-sezimal-unit-type').value;
    const locale = localStorage.getItem('sezimal-calculator-locale');

    if (unit_type == 'ang') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'agm', '-', 's');
    } else if (unit_type == 'avt') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'avt', '-', 'Hz');
    } else if (unit_type == 'pad') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'E', 'pad', '-', 'ft');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'pad', '-', 'm');
        }
    } else if (unit_type == 'ktr') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'ktr', '-', 'ft2');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'C', 'ktr', '-', 'm2');
        }
    } else if (unit_type == 'ayt') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'T', 'ayt', '-', 'US gal');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'ayt', '-', 'L');
        }
    } else if (unit_type == 'veg') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, '-', 'veg', '-', 'mph');
        } else {
            set_unit_type_sezimal_decimal(unit_type, '-', 'veg', 'k', 'm/h');
        }
    } else if (unit_type == 'tvr') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, '-', 'tvr', '-', 'ft/s2');
        } else {
            set_unit_type_sezimal_decimal(unit_type, '-', 'tvr', '-', 'm/s2');
        }
    } else if (unit_type == 'drv') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'drv', '-', 'lb');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'drv', 'k', 'g');
        }
    } else if (unit_type == 'gnt') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, '-', 'gnt', '-', 'lb/gal');
        } else {
            set_unit_type_sezimal_decimal(unit_type, '-', 'gnt', 'k', 'g/L');
        }
    } else if (unit_type == 'bar') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'bar', '-', 'lb·ft/s2');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'bar', '-', 'N');
        }
    } else if (unit_type == 'pdn') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'pdn', '-', 'psi');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'pdn', 'k', 'Pa');
        }
    } else if (unit_type == 'vrc') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'DX', 'vrc', '-', 'ft·lbf');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'DX', 'vrc', 'k', 'W·h');
        }
    } else if (unit_type == 'xkt') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'xkt', '-', 'hp');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'D', 'xkt', '-', 'W');
        }
    } else if (unit_type == 'svg') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, '-', 'svg', '-', 'lb·ft/s');
        } else {
            set_unit_type_sezimal_decimal(unit_type, '-', 'svg', 'k', 'g·m/s');
        }
    } else if (unit_type == 'agh') {
        set_unit_type_sezimal_decimal(unit_type, 'X', 'agh', '-', 'J·s');
    } else if (unit_type == 'gtk') {
        set_unit_type_sezimal_decimal(unit_type, 'P', 'gtk', '-', 'K');
    } else if (unit_type == 'tap') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, '', 'tap', '', '°F');
        } else {
            set_unit_type_sezimal_decimal(unit_type, '', 'tap', '', '°C');
        }
    } else if (unit_type == 'agn') {
        set_unit_type_sezimal_decimal(unit_type, '', 'agn', '', 'J/K');
    } else if (unit_type == 'kdn') {
        set_unit_type_sezimal_decimal(unit_type, 'XT', 'kdn', 'k', 'Cal');
    } else if (unit_type == 'idn') {
        set_unit_type_sezimal_decimal(unit_type, '', 'idn', '', 'J/K/kg');
    } else if (unit_type == 'tln') {
        set_unit_type_sezimal_decimal(unit_type, '', 'tln', '', 'J/K/m3');
    } else if (unit_type == 'dar') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'dar', '-', 'A');
    } else if (unit_type == 'vdt') {
        set_unit_type_sezimal_decimal(unit_type, 'T', 'vdt', 'm', 'A·h');
    } else if (unit_type == 'atr') {
        set_unit_type_sezimal_decimal(unit_type, 'T', 'atr', '-', 'V');
    } else if (unit_type == 'vrd') {
        set_unit_type_sezimal_decimal(unit_type, 't', 'vrd', '-', 'Ω');
    } else if (unit_type == 'vht') {
        set_unit_type_sezimal_decimal(unit_type, 'T', 'vht', '-', 'S');
    } else if (unit_type == 'dry') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'dry', '-', 'F');
    } else if (unit_type == 'upp') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'upp', '-', 'H');
    } else if (unit_type == 'pvh') {
        set_unit_type_sezimal_decimal(unit_type, 'T', 'pvh', '-', 'Wb');
    } else if (unit_type == 'vtr') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'vtr', '-', 'T');
    } else if (unit_type == 'mdl') {
        set_unit_type_sezimal_decimal(unit_type, 'd', 'mdl', '-', 'pi_rad');
    } else if (unit_type == 'gol') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'gol', '-', 'sr');
    } else if (unit_type == 'pkx') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'pkx', '-', 'cd');
    } else if (unit_type == 'dpk') {
        set_unit_type_sezimal_decimal(unit_type, 't', 'dpk', '-', 'lm');
    } else if (unit_type == 'dxt') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'dxt', '-', 'lm/W');
    } else if (unit_type == 'bht') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'bht', '-', 'mol');
    } else if (unit_type == 'dul') {
        set_unit_type_sezimal_decimal(unit_type, '-', 'dul', '-', 'Da');
    } else if (unit_type == 'spn') {
        set_unit_type_sezimal_decimal(unit_type, 'd', 'spn', '-', '%');
    } else if (unit_type == 'atk') {
        set_unit_type_sezimal_decimal(unit_type, 'DX', 'atk', 'Gi', 'B');
    } else if (unit_type == 'pvn') {
        set_unit_type_sezimal_decimal(unit_type, 'X', 'pvn', 'M', 'bps');
    } else if (unit_type == 'clt') {
        if (locale == 'en_us') {
            set_unit_type_sezimal_decimal(unit_type, 'T', 'clt', '', 'US mpg');
        } else {
            set_unit_type_sezimal_decimal(unit_type, 'C', 'clt', '', 'km/L');
        }
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
    const unit_type = document.getElementById('calculator-sezimal-unit-type').value;
    localStorage.setItem('sezimal-calculator-decimal-unit', select.value);

    if (unit_type == 'ktr') {
        if (select.value == 'm2') {
            document.getElementById('calculator-prefix-decimal').value = '-';
            set_decimal_prefix(document.getElementById('calculator-prefix-decimal'));
        } else if (select.value == 'a') {
            document.getElementById('calculator-prefix-decimal').value = 'h';
            set_decimal_prefix(document.getElementById('calculator-prefix-decimal'));
        }
    };

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

    if (unit_type == 'no-conversion') {
        document.getElementById('toggle_units').innerHTML = '[ ' + SHASTADARI_LOGO + ' ]';
    } else if (unit_type == 'units') {
        document.getElementById('toggle_units').innerHTML = '[  ' + SHASTADARI_LOGO + '  ]';
    } else if (unit_type == 'prefixes') {
        document.getElementById('toggle_units').innerHTML = '[  ' + SHASTADARI_LOGO + '  ]';
    } else {
        document.getElementById('units-title').hidden = false;

        show_decimal_binary_prefix(sezimal_unit, decimal_unit);

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

    if (localStorage.getItem(`sezimal-translation-display-${sezimal_unit.toLocaleLowerCase().replace(' ', '-').replace(' ', '-')}`) != null) {
        sezimal_unit = localStorage.getItem(`sezimal-translation-display-${sezimal_unit.toLocaleLowerCase().replace(' ', '-').replace(' ', '-')}`);
    };
    if (localStorage.getItem(`sezimal-translation-display-${decimal_unit.toLocaleLowerCase().replace(' ', '-').replace(' ', '-')}`) != null) {
        decimal_unit = localStorage.getItem(`sezimal-translation-display-${decimal_unit.toLocaleLowerCase().replace(' ', '-').replace(' ', '-')}`);
    };

    if ((sezimal_unit != '') && (decimal_unit != '')) {
        document.getElementById('toggle_units').innerHTML = '[ ' + sezimal_prefix + sezimal_unit + ' ' + SHASTADARI_LOGO + ' ' + decimal_prefix + decimal_unit + ' ]';
    } else {
        document.getElementById('toggle_units').innerHTML = '[ ' + SHASTADARI_LOGO + ' ]';
    };
};

function show_decimal_binary_prefix(sezimal_unit, decimal_unit) {
    if ((sezimal_unit == 'atk') || (sezimal_unit == 'pvn')) {
        document.getElementById('label-prefix-decimal').hidden = true;
        document.getElementById('label-prefix-decimal-binary').hidden = false;
        document.getElementById('calculator-prefix-decimal').hidden = false;
        document.getElementsByName('optgroup-units-generic-binary')[0].hidden = false;
    } else if ((decimal_unit == '') || (prefixed_units.includes(decimal_unit))) {
        document.getElementById('label-prefix-decimal').hidden = false;
        document.getElementById('label-prefix-decimal-binary').hidden = true;
        document.getElementById('calculator-prefix-decimal').hidden = false;
        document.getElementsByName('optgroup-units-generic-binary')[0].hidden = true;
    } else {
        document.getElementById('label-prefix-decimal').hidden = true;
        document.getElementById('label-prefix-decimal-binary').hidden = true;
        document.getElementById('calculator-prefix-decimal').hidden = true;
        document.getElementById('calculator-prefix-decimal').value = '-';
        document.getElementsByName('optgroup-units-generic-binary')[0].hidden = true;
    };
};

function hide_all_units() {
    document.getElementById('units-title').hidden = true;

    document.getElementById('unit-ang').hidden = true;
    document.getElementById('unit-avt').hidden = true;
    document.getElementById('unit-pad').hidden = true;
    document.getElementById('unit-ktr').hidden = true;
    document.getElementById('unit-ayt').hidden = true;
    document.getElementById('unit-drv').hidden = true;
    document.getElementById('unit-gnt').hidden = true;
    document.getElementById('unit-veg').hidden = true;
    document.getElementById('unit-tvr').hidden = true;
    document.getElementById('unit-bar').hidden = true;
    document.getElementById('unit-pdn').hidden = true;
    document.getElementById('unit-vrc').hidden = true;
    document.getElementById('unit-xkt').hidden = true;
    document.getElementById('unit-svg').hidden = true;
    document.getElementById('unit-agh').hidden = true;
    document.getElementById('unit-gtk').hidden = true;
    document.getElementById('unit-tap').hidden = true;
    document.getElementById('unit-agn').hidden = true;
    document.getElementById('unit-kdn').hidden = true;
    document.getElementById('unit-idn').hidden = true;
    document.getElementById('unit-tln').hidden = true;
    document.getElementById('unit-dar').hidden = true;
    document.getElementById('unit-vdt').hidden = true;
    document.getElementById('unit-atr').hidden = true;
    document.getElementById('unit-vrd').hidden = true;
    document.getElementById('unit-vht').hidden = true;
    document.getElementById('unit-dry').hidden = true;
    document.getElementById('unit-upp').hidden = true;
    document.getElementById('unit-dry').hidden = true;
    document.getElementById('unit-pvh').hidden = true;
    document.getElementById('unit-vtr').hidden = true;
    document.getElementById('unit-mdl').hidden = true;
    document.getElementById('unit-gol').hidden = true;
    document.getElementById('unit-pkx').hidden = true;
    document.getElementById('unit-dpk').hidden = true;
    document.getElementById('unit-dxt').hidden = true;
    document.getElementById('unit-bht').hidden = true;
    document.getElementById('unit-dul').hidden = true;
    document.getElementById('unit-spn').hidden = true;
    document.getElementById('unit-atk').hidden = true;
    document.getElementById('unit-pvn').hidden = true;
    document.getElementById('unit-clt').hidden = true;
};
