
function toggle_sezimal_digits() {
    const sezimal_digits = localStorage.getItem('sezimal-calculator-sezimal-digits');

    if ((sezimal_digits == null) || (sezimal_digits == '') || (sezimal_digits == false)  || (sezimal_digits == 'false')) {
        localStorage.setItem('sezimal-calculator-sezimal-digits', true);
    } else {
        localStorage.setItem('sezimal-calculator-sezimal-digits', false);
    };

    update_sezimal_digits();
};

function update_sezimal_digits(calculation_refresh = true) {
    const sezimal_digits = localStorage.getItem('sezimal-calculator-sezimal-digits');

    if ((sezimal_digits == null) || (sezimal_digits == '') || (sezimal_digits == false)  || (sezimal_digits == 'false')) {
        document.getElementById('toggle_sezimal_digits').innerHTML = '[ 3 ]'
        document.getElementById('button-sezimal-number-0').innerHTML = '0';
        document.getElementById('button-sezimal-number-1').innerHTML = '1';
        document.getElementById('button-sezimal-number-2').innerHTML = '2';
        document.getElementById('button-sezimal-number-3').innerHTML = '3';
        document.getElementById('button-sezimal-number-4').innerHTML = '4';
        document.getElementById('button-sezimal-number-5').innerHTML = '5';
        document.getElementById('button-sezimal-number-00').innerHTML = '00';
        document.getElementById('button-base-ten').innerHTML = '14';
        // document.getElementById('button-pernif').innerHTML = '%';
        // document.getElementById('button-perarda').innerHTML = '‰';
        // document.getElementById('button-persixarda').innerHTML = '‱';
    } else {
        document.getElementById('toggle_sezimal_digits').innerHTML = '[ 󱸃 ]'
        document.getElementById('button-sezimal-number-0').innerHTML = '󱸀';
        document.getElementById('button-sezimal-number-1').innerHTML = '󱸁';
        document.getElementById('button-sezimal-number-2').innerHTML = '󱸂';
        document.getElementById('button-sezimal-number-3').innerHTML = '󱸃';
        document.getElementById('button-sezimal-number-4').innerHTML = '󱸄';
        document.getElementById('button-sezimal-number-5').innerHTML = '󱸅';
        document.getElementById('button-sezimal-number-00').innerHTML = '󱸀󱸀';
        document.getElementById('button-base-ten').innerHTML = '󱸁󱸄';
        // document.getElementById('button-pernif').innerHTML = '󱺉';
        // document.getElementById('button-perarda').innerHTML = '󱺊';
        // document.getElementById('button-persixarda').innerHTML = '󱺋';
    };

    update_grouping(false);
    update_niftimal(false);
    update_sezimal_places(false);

    if (calculation_refresh == true) {
        update_calculation();
    };
};
