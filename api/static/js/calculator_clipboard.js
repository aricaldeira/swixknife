
function copy_to_clipboard(element) {
    let value = element.innerHTML;

    value = value.
        replace('<math>', '').
        replace('</math>', '').
        replace('<mfrac>', '').
        replace('</mfrac>', '').
        replace('</mn><mn>', '⁄').
        replace('<mn>', '').
        replace('</mn>', '')

    navigator.clipboard.writeText(value);
};

const ALLOWED_SEZIMAL_CHARACTERS = [
    '0', '1', '2', '3', '4', '5',
    '󱸀', '󱸁', '󱸂', '󱸃', '󱸄', '󱸅',
    ',', '„', '.', '‥', '󱹮', '󱹯',
    '_', '+', '-', '*', '/', '⁄',
    '󱹱', '󱹲', '󱹳', '󱹴', '󱹵', '󱹶', '󱹷',
];

const ALLOWED_DECIMAL_CHARACTERS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '󱸀', '󱸁', '󱸂', '󱸃', '󱸄', '󱸅',
    ',', '„', '.', '‥', '󱹮', '󱹯',
    '_', '+', '-', '*', '/', '⁄',
    '%', '‰', '‱',
];

document.addEventListener('paste', event => {
    const clipboard_data = event.clipboardData || window.clipboardData;
    let pasted_text = clipboard_data.getData('text/plain');
    let cleaned_text = '';

    if (pasted_text.includes('.') && pasted_text.includes(',')) {
        if (pasted_text.lastIndexOf('.') < pasted_text.lastIndexOf(',')) {
            pasted_text = pasted_text.replace('.', '_');
        } else {
            pasted_text = pasted_text.replace(',', '_');
        };
    };

    pasted_text = pasted_text
        .replace('^', '**')
        .replace(',', '.')
        .replace('„', '..')
        .replace('‥', '..')
        .replace('×', '*')
        .replace('÷', '/')
        .replace('−', '-')
        .replace('󱹬', '_')
        .replace('󱹭', '_')
        .replace('󱹮', '.')
        .replace('󱹯', '..');

    if (localStorage.getItem('sezimal-calculator-base') == 14) {
        [...pasted_text].forEach(c => {
            if (ALLOWED_DECIMAL_CHARACTERS.includes(c)) {
                cleaned_text = cleaned_text + c;
            };
        });
        document.getElementById('decimal_expression').innerHTML = cleaned_text;
    } else {
        [...pasted_text].forEach(c => {
            if (ALLOWED_SEZIMAL_CHARACTERS.includes(c)) {
                cleaned_text = cleaned_text + c;
            };
        });
        document.getElementById('expression').innerHTML = cleaned_text;
    };

    update_calculation();
});
