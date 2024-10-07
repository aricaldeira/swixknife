
function toggle_grouping() {
    const grouping = localStorage.getItem('sezimal-calculator-grouping');
    const punctuation = localStorage.getItem('sezimal-calculator-sezimal-punctuation');

    if ((grouping == null) || (grouping == '') || (grouping == 3) || (grouping == '3')) {
        if ((punctuation == null) || (punctuation == '')) {
            localStorage.setItem('sezimal-calculator-sezimal-punctuation', true);
        } else if ((punctuation == true) || (punctuation == 'true')) {
            localStorage.setItem('sezimal-calculator-sezimal-punctuation', false);
        } else if ((punctuation == false) || (punctuation == 'false')) {
            localStorage.setItem('sezimal-calculator-grouping', 4);
        };
    } else {
        localStorage.setItem('sezimal-calculator-sezimal-punctuation', true);
        localStorage.setItem('sezimal-calculator-grouping', 3);
    };

    update_sezimal_places(false);
    update_grouping();
};

function update_grouping(calculation_refresh = true) {
    const grouping = localStorage.getItem('sezimal-calculator-grouping');
    const sezimal_digits = localStorage.getItem('sezimal-calculator-sezimal-digits');
    const sezimal_punctuation = localStorage.getItem('sezimal-calculator-sezimal-punctuation');
    const currency_mode = localStorage.getItem('sezimal-calculator-currency-mode');
    let separator;
    let decimal_separator;

    if (sezimal_punctuation == 'true') {
        separator = '󱹬';
        if (currency_mode == 'true') {
            document.getElementById('button-sezimal-separator').innerHTML = '󱹶';
        } else {
            document.getElementById('button-sezimal-separator').innerHTML = '󱹮';
        }
    } else {
        separator = localStorage.getItem('sezimal-calculator-group-separator');
        decimal_separator = document.getElementById('button-decimal-separator').innerHTML;

        if (currency_mode == 'true') {
            if (decimal_separator == '.') {
                decimal_separator = ';';
            } else if (decimal_separator == '٫') {
                decimal_separator = '؛';
            } else {
                decimal_separator = ';';
            };
        };

        document.getElementById('button-sezimal-separator').innerHTML = decimal_separator;
    }

    if (grouping == 3) {
        if (sezimal_digits == 'true') {
            document.getElementById('toggle_grouping').innerHTML = '[ 󱸃' + separator + '󱸃 ]';
        } else {
            document.getElementById('toggle_grouping').innerHTML = '[ 3' + separator + '3 ]';
        };
    } else {
        if (sezimal_digits == 'true') {
            document.getElementById('toggle_grouping').innerHTML = '[ 󱸄' + separator + '󱸄 ]';
        } else {
            document.getElementById('toggle_grouping').innerHTML = '[ 4' + separator + '4 ]';
        };
    };

    if (calculation_refresh == true) {
        update_calculation();
    };
};
