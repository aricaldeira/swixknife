
document.addEventListener('keydown', function(event) {
    const base_six = localStorage.getItem('sezimal-calculator-base') != 14;
    let button = {
        'value': '',
    };

    if ((event.keyCode == 27) || (event.key == 'c') || (event.key == 'z')) {
        button.value = 'C';
    } else if (event.key == 'b') {
        event.preventDefault();
        if (base_six) {
            toggle_base_ten();
        } else {
            toggle_base_six();
        };
        return;
    } else if (event.key == '(') {
        button.value = '(';
    } else if (event.key == ')') {
        button.value = ')';
    } else if ((event.keyCode == 8) || (event.keyCode == 46)) {
        button.value = '⌫';
    } else if (event.key == '7') {
        if (base_six) {
            button.value = 'e';
        } else {
            button.value = '7';
        }
    } else if (event.key == '8') {
        if (base_six) {
            button.value = 'τ';
        } else {
            button.value = '8';
        }
    } else if (event.key == '9') {
        if (base_six) {
            button.value = '00';
        } else {
            button.value = '9';
        }
    } else if (event.key == '^') {
        button.value = '^';
    } else if ((event.key == '%') || (event.key == '󱹱') || (event.key == '󱹲') || (event.key == '󱹳')) {
        if (base_six) {
            button.value = '󱹱';
        } else {
            button.value = '%';
        }
    } else if (event.key == '6') {
        if (base_six) {
            button.value = 'φ';
        } else {
            button.value = '6';
        }
    } else if ((event.key == '3') || (event.key == '󱸃')) {
        button.value = '3';
    } else if ((event.key == '4') || (event.key == '󱸄')) {
        button.value = '4';
    } else if ((event.key == '5') || (event.key == '󱸅')) {
        button.value = '5';
    } else if (event.key == '*') {
        button.value = '*';
    } else if (event.key == '/') {
        button.value = '/';
    } else if ((event.key == '0') || (event.key == '󱸀')) {
        button.value = '0';
    } else if ((event.key == '1') || (event.key == '󱸁')) {
        button.value = '1';
    } else if ((event.key == '2') || (event.key == '󱸂')) {
        button.value = '2';
    } else if (event.key == '+') {
        button.value = '+';
    } else if (event.key == '-') {
        button.value = '-';
    } else if ((event.key == '.') || (event.key == ',') || (event.key == '󱹮')) {
        button.value = '.';
    // } else if ((event.keyCode == 38) || (event.keyCode == 40)) {
    //     button.value = '±';
    } else if (event.keyCode == 13) {
        button.value = '=';
    };

    if (button.value != '') {
        event.preventDefault();
        button_click(button);
    };
});
