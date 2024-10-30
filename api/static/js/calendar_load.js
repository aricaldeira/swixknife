
function calendar_load() {
    /*
    *  First run base definition
    */
    var base = localStorage.getItem('sezimal-calendar-base');
    var format_token = localStorage.getItem('sezimal-calendar-format-token');
    if (base === null) {
        base = '10';
        format_token = '';
        localStorage.setItem('sezimal-calendar-base', '10');
        localStorage.setItem('sezimal-calendar-format-token', '');
    };

    if (base == '10') {
        if (format_token == '!') {
            document.getElementById('base_select_10!').setAttribute('checked', 'checked');
        } else {
            document.getElementById('base_select_10').setAttribute('checked', 'checked');
        };
    } else if (base == '14') {
        document.getElementById('base_select_14').setAttribute('checked', 'checked');
    } else if (base == '20') {
        document.getElementById('base_select_20').setAttribute('checked', 'checked');
    };

    /*
    *  First run locale definition
    */
    var locale = localStorage.getItem('sezimal-calendar-locale');
    if (locale === null) {
        locale = navigator.languages && navigator.languages.length
        ? navigator.languages[0]
        : navigator.language;

        console.log('locale detectado', locale);

        locale = locale.replace('-', '_').toLowerCase();
        localStorage.setItem('sezimal-calendar-locale', locale);
    };
    document.getElementById('calculator-sezimal-locale').value = locale;

    /*
    *  First run time zone definition
    */
    if (localStorage.getItem('sezimal-calendar-time-zone') === null) {
        localStorage.setItem('sezimal-calendar-time-zone', Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC');

        console.log('fuso horário detectado', Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC');
    };
    document.getElementById('time_zone_select').value = localStorage.getItem('sezimal-calendar-time-zone');

    /*
    *  First run theme definition
    */
    var theme = localStorage.getItem('sezimal-calendar-theme');
    if (theme === null) {
        localStorage.setItem('sezimal-calendar-theme', 'FULL_COLOR');
        theme = 'FULL_COLOR';
    };

    if (theme == 'FULL_COLOR') {
        document.getElementById('theme_select_full_color').setAttribute('checked', 'checked');
    } else if (theme == 'GRAY') {
        document.getElementById('theme_select_gray').setAttribute('checked', 'checked');
    };

    /*
    *  First run view definition
    */
    if (localStorage.getItem('sezimal-calendar-view') === null) {
        localStorage.setItem('sezimal-calendar-view', 'yearly');
    };

    /*
    *  First run clock definition
    */
    if (localStorage.getItem('sezimal-calendar-hour-format') === null) {
        localStorage.setItem('sezimal-calendar-hour-format', 'locale');
    };
    document.getElementById('hour_format_select').value = localStorage.getItem('sezimal-calendar-hour-format');

    /*
    *  First run hemisphere definition
    */
    if (localStorage.getItem('sezimal-calendar-hemisphere') === null) {
        localStorage.setItem('sezimal-calendar-hemisphere', 'locale');
    };
    document.getElementById('hemisphere_select').value = localStorage.getItem('sezimal-calendar-hemisphere');

    update_calendar();
};
