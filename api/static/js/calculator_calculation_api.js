
const per_symbols = ['%', '‰', '‱', '󱹰', '󱹱', '󱹲', '󱹳', '󱹴', '󱹵'];

function button_click(button) {
    update_calculation(button.value);
};

function update_calculation(value = '') {
    let dados = {};
    let sezimal_prefix = localStorage.getItem('sezimal-calculator-prefix');
    let sezimal_unit = localStorage.getItem('sezimal-calculator-unit');
    let decimal_prefix = localStorage.getItem('sezimal-calculator-decimal-prefix');
    let decimal_unit = localStorage.getItem('sezimal-calculator-decimal-unit');

    let sezimal_angle_prefix = localStorage.getItem('sezimal-calculator-angle-prefix');
    let sezimal_angle_unit = localStorage.getItem('sezimal-calculator-angle-unit');
    let decimal_angle_prefix = localStorage.getItem('sezimal-calculator-decimal-angle-prefix');
    let decimal_angle_unit = localStorage.getItem('sezimal-calculator-decimal-angle-unit');

    if ((sezimal_prefix == '-') || (sezimal_prefix == null)) {
        sezimal_prefix = '';
    };
    if ((decimal_prefix == '-') || (decimal_prefix == null)) {
        decimal_prefix = '';
    };
    if ((sezimal_angle_prefix == '-') || (sezimal_angle_prefix == null)) {
        sezimal_angle_prefix = '';
    };
    if ((decimal_angle_prefix == '-') || (decimal_angle_prefix == null)) {
        decimal_angle_prefix = '';
    };

    // if (localStorage.getItem(`sezimal-translation-${sezimal_unit}`) != null) {
    //     sezimal_unit = localStorage.getItem(`sezimal-translation-${sezimal_unit}`);
    // };
    // if (localStorage.getItem(`sezimal-translation-${decimal_unit}`) != null) {
    //     decimal_unit = localStorage.getItem(`sezimal-translation-${decimal_unit}`);
    // };

    dados = {
        locale: localStorage.getItem('sezimal-calculator-locale'),
        currency_mode: localStorage.getItem('sezimal-calculator-currency-mode'),
        places: localStorage.getItem('sezimal-calculator-sezimal-places'),
        base: localStorage.getItem('sezimal-calculator-base'),
        sezimal_digits: localStorage.getItem('sezimal-calculator-sezimal-digits'),
        sezimal_punctuation: localStorage.getItem('sezimal-calculator-sezimal-punctuation'),
        grouping: localStorage.getItem('sezimal-calculator-grouping'),
        spellout: localStorage.getItem('sezimal-calculator-spellout'),
        sezimal_unit: sezimal_prefix + sezimal_unit,
        decimal_unit: decimal_prefix + decimal_unit,
        sezimal_angle_unit: sezimal_angle_prefix + sezimal_angle_unit,
        decimal_angle_unit: decimal_angle_prefix + decimal_angle_unit,
        niftimal: localStorage.getItem('sezimal-calculator-niftimal'),
        expression: document.getElementById('expression').innerHTML,
        value: value,
    };

    if (localStorage.getItem('sezimal-calculator-base') == 14) {
        dados.expression = document.getElementById('decimal_expression').innerHTML;
    };

    fetch('/calculator/process', {
        method: 'post',
        body: JSON.stringify(dados),
        headers: {
            'Accept': 'application/json; charset=UTF-8',
            'Content-Type': 'application/json; charset=UTF-8'
        }
    }).then((response) => {
        return response.json();
    }).then((dados) => {
        document.getElementById('expression').innerHTML = dados.expression;
        document.getElementById('decimal_expression').innerHTML = dados.decimal_expression;

        localStorage.setItem('sezimal-calculator-sezimal-separator', dados.separator);

        if (dados.sezimal_punctuation) {
            if (dados.currency_mode) {
                document.getElementById('button-sezimal-separator').innerHTML = '󱹶';
            } else {
                document.getElementById('button-sezimal-separator').innerHTML = '󱹮';
            }
        } else {
            if (dados.currency_mode) {
                document.getElementById('button-sezimal-separator').innerHTML = dados.currency_separator;
            } else {
                document.getElementById('button-sezimal-separator').innerHTML = dados.separator;
            }
        };
        update_sezimal_places(false);

        document.getElementById('button-decimal-separator').innerHTML = dados.separator;

        localStorage.setItem('sezimal-calculator-group-separator', dados.group_separator);
        update_grouping(false);

        localStorage.setItem('sezimal-calculator-currency-unit-symbol', dados.currency_unit_symbol);
        update_currency_mode(false);

        if (dados.show_spellout) {
            document.getElementById('spellout').innerHTML = dados.spellout;
            document.getElementById('spellout_display').hidden = false;
        } else {
            document.getElementById('spellout_display').hidden = true;
        };

        if (localStorage.getItem('sezimal-calculator-base') == 14) {
            set_display_value(dados.display, sezimal_prefix + sezimal_unit, 'display_number', 32);
            set_display_value(dados.niftimal_display, sezimal_prefix + sezimal_unit, 'niftimal_display_number', 15);
            set_display_value(dados.decimal_display, decimal_prefix + decimal_unit, 'decimal_display_number', 56);
        } else {
            set_display_value(dados.display, sezimal_prefix + sezimal_unit, 'display_number', 56);
            set_display_value(dados.niftimal_display, sezimal_prefix + sezimal_unit, 'niftimal_display_number', 24);
            set_display_value(dados.decimal_display, decimal_prefix + decimal_unit, 'decimal_display_number', 32);
        }
    });
};

function set_display_value(value, unit, display_number_name, font_size) {
    const value_size = Array.from(
        value.
            replace('<math>', '').
            replace('</math>', '').
            replace('<mfrac>', '').
            replace('</mfrac>', '').
            replace('<mn>', '').
            replace('</mn>', '')
    ).length;
    var number = document.getElementById(display_number_name);

    number.style.fontSize = font_size.toString() + 'px';

    if (unit != '') {
        if (per_symbols.includes(unit)) {
            number.innerHTML = translate_display(value) + unit;
        } else {
            number.innerHTML = translate_display(value) + '&zwnj; ' + translate_display(unit);
        };
    } else {
        number.innerHTML = translate_display(value);
    };

    if ((font_size == 56) || (font_size == 32)) {
        const width = number.getBoundingClientRect().width;
        font_size = parseFloat(window.getComputedStyle(number).fontSize) * 0.63;
        var max_characters = Math.round(width / font_size, 0);

        while (value_size > max_characters) {
            font_size = (font_size / 0.63) * 0.9;
            number.style.fontSize = font_size.toString() + 'px';
            font_size = font_size * 0.63;
            max_characters = Math.round(width / font_size, 0);
        };
    };
};
