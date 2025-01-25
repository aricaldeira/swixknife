
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

    if (localStorage.getItem('sezimal-calendar-displayed') === null) {
        if (localStorage.getItem('sezimal-calendar-iso-date-decimal') === 'true') {
            localStorage.setItem('sezimal-calendar-displayed', 'ISO');
            localStorage.removeItem('sezimal-calendar-iso-date-decimal');
        } else if (localStorage.getItem('sezimal-calendar-iso-date-decimal') === 'false') {
            localStorage.setItem('sezimal-calendar-displayed', 'SYM');
            localStorage.removeItem('sezimal-calendar-iso-date-decimal');
        } else {
            localStorage.setItem('sezimal-calendar-displayed', 'SYM');
        };
    };
    document.getElementById('calendar_displayed_select').value = localStorage.getItem('sezimal-calendar-displayed');

    /*
    *  First run locale definition
    */
    var locale = localStorage.getItem('sezimal-calendar-locale');
    if (locale === null) {
        locale = navigator.languages && navigator.languages.length
        ? navigator.languages[0]
        : navigator.language;
        locale = locale.replace('-', '_').toLowerCase();
        localStorage.setItem('sezimal-calendar-locale', locale);
    };
    document.getElementById('calculator-sezimal-locale').value = locale;

    /*
    *  First run time zone definition
    */
    if (localStorage.getItem('sezimal-calendar-time-zone') === null) {
        localStorage.setItem('sezimal-calendar-time-zone', Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC');
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
    document.getElementById('theme_select').value = theme;

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

    if (localStorage.getItem('sezimal-calendar-show-seconds') === null) {
        localStorage.setItem('sezimal-calendar-show-seconds', 'true');
    };
    document.getElementById('show_seconds_input').checked = localStorage.getItem('sezimal-calendar-show-seconds') == 'true';

    if (localStorage.getItem('sezimal-calendar-locale-first-weekday') === null) {
        localStorage.setItem('sezimal-calendar-locale-first-weekday', 'false');
    };
    document.getElementById('locale_first_weekday_input').checked = localStorage.getItem('sezimal-calendar-locale-first-weekday') == 'true';

    /*
    *  First run hemisphere definition
    */
    if (localStorage.getItem('sezimal-calendar-hemisphere') === null) {
        localStorage.setItem('sezimal-calendar-hemisphere', 'locale');
    };
    document.getElementById('hemisphere_select').value = localStorage.getItem('sezimal-calendar-hemisphere');

    /*
    *  First run holidays calendar definition
    */
    if (localStorage.getItem('sezimal-calendar-show-holiday') === null) {
        localStorage.setItem('sezimal-calendar-show-holiday', 'ISO_SEZ_SYM');
    };
    document.getElementById('show_holiday_select').value = localStorage.getItem('sezimal-calendar-show-holiday');

    if (localStorage.getItem('sezimal-calendar-show-holiday-christian') === null) {
        localStorage.setItem('sezimal-calendar-show-holiday-christian', false);
    };
    document.getElementById('religious_calendar_input_christian').checked = (
        (localStorage.getItem('sezimal-calendar-show-holiday-christian') == true)
        || (localStorage.getItem('sezimal-calendar-show-holiday-christian') == 'true')
    );

    // if (localStorage.getItem('sezimal-calendar-show-holiday-orthodox') === null) {
    //     localStorage.setItem('sezimal-calendar-show-holiday-orthodox', false);
    // };
    // document.getElementById('religious_calendar_input_orthodox').checked = (
    //     (localStorage.getItem('sezimal-calendar-show-holiday-orthodox') == true)
    //     || (localStorage.getItem('sezimal-calendar-show-holiday-orthodox') == 'true')
    // );

    if (localStorage.getItem('sezimal-calendar-show-holiday-islamic') === null) {
        localStorage.setItem('sezimal-calendar-show-holiday-islamic', false);
    };
    document.getElementById('religious_calendar_input_islamic').checked = (
        (localStorage.getItem('sezimal-calendar-show-holiday-islamic') == true)
        || (localStorage.getItem('sezimal-calendar-show-holiday-islamic') == 'true')
    );

    if (localStorage.getItem('sezimal-calendar-show-holiday-jewish') === null) {
        localStorage.setItem('sezimal-calendar-show-holiday-jewish', false);
    };
    document.getElementById('religious_calendar_input_jewish').checked = (
        (localStorage.getItem('sezimal-calendar-show-holiday-jewish') == true)
        || (localStorage.getItem('sezimal-calendar-show-holiday-jewish') == 'true')
    );

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(set_coordinates);
    };

    function set_coordinates(position) {
        localStorage.setItem('sezimal-gps-latitude', Math.floor(position.coords.latitude * 10000) / 10000);
        localStorage.setItem('sezimal-gps-longitude', Math.floor(position.coords.longitude * 10000) / 10000);
    };

    document.getElementById('sezimal-latitude-input').value = localStorage.getItem('sezimal-latitude');
    document.getElementById('sezimal-longitude-input').value = localStorage.getItem('sezimal-longitude');

    update_calendar();
};
