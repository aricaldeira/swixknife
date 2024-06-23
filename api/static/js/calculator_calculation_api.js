
function button_click(button) {
    update_calculation(button.value);
};

function update_calculation(value = '') {
    let dados = {};

    if (localStorage.getItem('sezimal-calculator-base') == 14) {
        dados = JSON.stringify({
            locale: localStorage.getItem('sezimal-calculator-locale'),
            places: localStorage.getItem('sezimal-calculator-sezimal-places'),
            base: localStorage.getItem('sezimal-calculator-base'),
            sezimal_digits: localStorage.getItem('sezimal-calculator-sezimal-digits'),
            grouping: localStorage.getItem('sezimal-calculator-grouping'),
            spellout: localStorage.getItem('sezimal-calculator-spellout'),
            sezimal_unit: localStorage.getItem('sezimal-calculator-unit'),
            decimal_unit: localStorage.getItem('sezimal-calculator-decimal-unit'),
            niftimal: localStorage.getItem('sezimal-calculator-niftimal'),
            expression: document.getElementById('decimal_expression').innerHTML,
            value: value,
        });
    } else {
        dados = JSON.stringify({
            locale: localStorage.getItem('sezimal-calculator-locale'),
            places: localStorage.getItem('sezimal-calculator-sezimal-places'),
            base: localStorage.getItem('sezimal-calculator-base'),
            sezimal_digits: localStorage.getItem('sezimal-calculator-sezimal-digits'),
            grouping: localStorage.getItem('sezimal-calculator-grouping'),
            spellout: localStorage.getItem('sezimal-calculator-spellout'),
            sezimal_unit: localStorage.getItem('sezimal-calculator-unit'),
            decimal_unit: localStorage.getItem('sezimal-calculator-decimal-unit'),
            niftimal: localStorage.getItem('sezimal-calculator-niftimal'),
            expression: document.getElementById('expression').innerHTML,
            value: value,
        });
    }

    fetch('/calculator/process', {
        method: 'post',
        body: dados,
        headers: {
            'Accept': 'application/json; charset=UTF-8',
            'Content-Type': 'application/json; charset=UTF-8'
        }
    }).then((response) => {
        return response.json();
    }).then((dados) => {
        dados.display = dados.display.replace(',,', '„').replace('..', '‥');
        dados.niftimal_display = dados.niftimal_display.replace(',,', '„').replace('..', '‥');
        dados.decimal_display = dados.decimal_display.replace(',,', '„').replace('..', '‥');

        document.getElementById('expression').innerHTML = dados.expression;
        document.getElementById('decimal_expression').innerHTML = dados.decimal_expression;

        localStorage.setItem('sezimal-calculator-sezimal-separator', dados.separator);
        document.getElementById('button-sezimal-separator').innerHTML = dados.separator;
        document.getElementById('button-decimal-separator').innerHTML = dados.separator;

        localStorage.setItem('sezimal-calculator-group-separator', dados.group_separator);
        update_grouping(false);

        if (dados.show_spellout) {
            document.getElementById('spellout').innerHTML = dados.spellout;
            document.getElementById('spellout_display').hidden = false;
        } else {
            document.getElementById('spellout_display').hidden = true;
        };

        if (localStorage.getItem('sezimal-calculator-base') == 14) {
            set_display_value(dados.display, 'display_number', 32);
            set_display_value(dados.niftimal_display, 'niftimal_display_number', 9);
            set_display_value(dados.decimal_display, 'decimal_display_number', 56);
        } else {
            set_display_value(dados.display, 'display_number', 56);
            set_display_value(dados.niftimal_display, 'niftimal_display_number', 16);
            set_display_value(dados.decimal_display, 'decimal_display_number', 32);
        }
    });
};

function set_display_value(value, display_number_name, font_size) {
    const value_size = Array.from(value).length;
    var number = document.getElementById(display_number_name);

    number.style.fontSize = font_size.toString() + 'px';
    number.innerHTML = value;

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
