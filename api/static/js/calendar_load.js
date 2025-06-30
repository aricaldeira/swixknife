
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
    var time_zone_from = localStorage.getItem('sezimal-calendar-time-zone-from');
    if ((time_zone_from === null) || (time_zone_from == 'null')) {
        time_zone_from = 'UTC';
        localStorage.setItem('sezimal-calendar-time-zone-from', time_zone_from);
    };
    document.getElementById('time_zone_from_select').value = time_zone_from;
    toggle_time_zone_from();

    var time_zone = localStorage.getItem('sezimal-calendar-time-zone');
    if ((time_zone === null) || (time_zone == 'null')) {
        time_zone = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';
        localStorage.setItem('sezimal-calendar-time-zone', time_zone);
    };
    document.getElementById('time_zone_select').value = time_zone;

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

    var latitude = 0;
    var moon_tilt = 0;

    if (
        (localStorage.getItem('sezimal-latitude') != null)
        && (localStorage.getItem('sezimal-latitude') != 'null')
    ) {
        latitude = parseFloat(localStorage.getItem('sezimal-latitude'));
    } else if (
        (localStorage.getItem('sezimal-gps-latitude') != null)
        && (localStorage.getItem('sezimal-gps-latitude') != 'null')
    ) {
        latitude = parseFloat(localStorage.getItem('sezimal-gps-latitude'));
    };

    if (latitude > 0) {
        if (localStorage.getItem('sezimal-calendar-hemisphere') == 'S') {
            latitude = latitude * -1;
        };
    } else if (latitude < 0) {
        if (localStorage.getItem('sezimal-calendar-hemisphere') == 'N') {
            latitude = latitude * -1;
        };
    };

    if (latitude > 0) {
        moon_tilt = 360 - Math.abs(latitude);
    } else if (latitude < 0) {
        moon_tilt = 90 - Math.abs(latitude);
    };

    document.getElementById('moon-style').innerHTML = `.moon-emoji {
    display: inline-block;
    transform: rotate(${moon_tilt}deg);
}`;


    update_calendar();
};


function toggle_time_zone_from() {
    const from_types = [
        'utc',
        'spm',
        'nt_spm',
        'mt_spm',
        'gpm',
        'nt_gpm',
        'mt_gpm',
        'spm_sez',
        'nt_spm_sez',
        'mt_spm_sez',
        'spm_doz',
        'nt_spm_doz',
        'mt_spm_doz',
    ];

    from_types.map(from_type => {
        var optgroup = document.getElementById(`time_zone_from_${from_type}`);
        optgroup.hidden = true;
        for (let i = 0; i < optgroup.children.length; i++) {
            optgroup.children[i].hidden = true;
        }
    });

    var tzf = document.getElementById('time_zone_from_select').value;

    if ((tzf == '') || (tzf == null)) {
        tzf = 'UTC';
    };

    tzf = tzf.toLowerCase().replaceAll('-', '_');

    var optgroup = document.getElementById(`time_zone_from_${tzf}`);
    optgroup.hidden = false;
    for (let i = 0; i < optgroup.children.length; i++) {
        optgroup.children[i].hidden = false;
    }

    var tz = document.getElementById('time_zone_select').value;

    if ((tzf == 'gpm') || (tzf == 'nt_gpm') || (tzf == 'mt_gpm')) {
        if (tzf == 'gpm') {
            tz = tz.replace('/NT', '/GPM');
            tz = tz.replace('/MT', '/GPM');
        } else if (tzf == 'nt_gpm') {
            tz = tz.replace('/GPM', '/NT');
            tz = tz.replace('/MT', '/NT');
        } else if (tzf == 'mt_gpm') {
            tz = tz.replace('/GPM', '/MT');
            tz = tz.replace('/NT', '/MT');
        } else {
            tz = null;
        };
    } else if ((tzf == 'spm') || (tzf == 'nt_spm') || (tzf == 'mt_spm')) {
        if (tzf == 'spm') {
            tz = tz.replace('/NT', '/SPM');
            tz = tz.replace('/MT', '/SPM');
        } else if (tzf == 'nt_spm') {
            tz = tz.replace('/SPM', '/NT');
            tz = tz.replace('/MT', '/NT');
        } else if (tzf == 'mt_spm') {
            tz = tz.replace('/SPM', '/MT');
            tz = tz.replace('/NT', '/MT');
        } else {
            tz = null;
        };
    } else if ((tzf == 'spm_sez') || (tzf == 'nt_spm_sez') || (tzf == 'mt_spm_sez')) {
        if (tzf == 'spm_sez') {
            tz = tz.replace('/NT', '/SPM');
            tz = tz.replace('/MT', '/SPM');
        } else if (tzf == 'nt_spm_sez') {
            tz = tz.replace('/SPM', '/NT');
            tz = tz.replace('/MT', '/NT');
        } else if (tzf == 'mt_spm_sez') {
            tz = tz.replace('/SPM', '/MT');
            tz = tz.replace('/NT', '/MT');
        } else {
            tz = null;
        };
    } else if ((tzf == 'spm_doz') || (tzf == 'nt_spm_doz') || (tzf == 'mt_spm_doz')) {
        if (tzf == 'spm_doz') {
            tz = tz.replace('/NT', '/SPM');
            tz = tz.replace('/MT', '/SPM');
        } else if (tzf == 'nt_spm_doz') {
            tz = tz.replace('/SPM', '/NT');
            tz = tz.replace('/MT', '/NT');
        } else if (tzf == 'mt_spm_doz') {
            tz = tz.replace('/SPM', '/MT');
            tz = tz.replace('/NT', '/MT');
        } else {
            tz = null;
        };
    };

    document.getElementById('time_zone_select').value = tz;
};
