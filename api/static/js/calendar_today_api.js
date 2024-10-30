
const LANGUAGE_TAGS = {
    'ar_latn': 'ar-Latn',
    'ar': 'ar',
    'bn_latn': 'bn-Latn',
    'bn': 'bn',
    'bz_br': 'bz-BR',
    'bz_pt': 'bz-PT',
    'bz': 'bz',
    'ca': 'ca',
    'code': 'code',
    'de': 'de',
    'el': 'el',
    'en_au': 'en-AU',
    'en_br': 'en-BR',
    'en_ca': 'en-CA',
    'en_gb': 'en-GB',
    'en_ie': 'en-IE',
    'en_in': 'en-IN',
    'en_nyoo_speling': 'en-NYOO-SPELING',
    'en_nz': 'en-NZ',
    'en_shaw': 'en-Shaw',
    'en_us': 'en-US',
    'en': 'en',
    'eo_br': 'eo-BR',
    'eo': 'eo',
    'es_ar': 'es-AR',
    'es_bo': 'es-BO',
    'es_cl': 'es-CL',
    'es_co': 'es-CO',
    'es_ec': 'es-EC',
    'es_es': 'es-ES',
    'es_mx': 'es-MX',
    'es_pe': 'es-PE',
    'es_py': 'es-PY',
    'es_uy': 'es-UY',
    'es': 'es',
    'fa_latn': 'fa-Latn',
    'fa': 'fa',
    'fr_ca': 'fr-CA',
    'fr_ch': 'fr-CH',
    'fr_ortograf': 'fr-Ortograf',
    'fr': 'fr',
    'ga_clo_gaelach': 'ga-CLO-GAELACH',
    'ga_traditional': 'ga-Traditional',
    'ga': 'ga',
    'gl': 'gl',
    'gn': 'gn',
    'he_latn': 'he-Latn',
    'he': 'he',
    'hi_latn': 'hi-Latn',
    'hi': 'hi',
    'hu': 'hu',
    'id': 'id',
    'iso_dot': 'iso-Dot',
    'iso': 'iso',
    'it': 'it',
    'iu_latn': 'iu-Latn',
    'iu': 'iu',
    'ja': 'ja',
    'kea': 'kea',
    'ko': 'ko',
    'mt': 'mt',
    'nl': 'nl',
    'pl': 'pl',
    'pt_ao': 'pt-AO',
    'pt_br': 'pt-BR',
    'pt_ch': 'pt-CH',
    'pt_cv': 'pt-CV',
    'pt_gq': 'pt-GQ',
    'pt_gw': 'pt-GW',
    'pt_lu': 'pt-LU',
    'pt_mo': 'pt-MO',
    'pt_mz': 'pt-MZ',
    'pt_pt': 'pt-PT',
    'pt_st': 'pt-ST',
    'pt_tl': 'pt-TL',
    'pt': 'pt',
    'ro': 'ro',
    'ru': 'ru',
    'sw_traditional': 'sw-Traditional',
    'sw': 'sw',
    'tr': 'tr',
    'uk': 'uk',
    'vi': 'vi',
    'yo': 'yo',
    'yrl': 'yrl',
    'zh_cn': 'zh-CN',
    'zh_hans': 'zh-Hans',
    'zh_hant': 'zh-Hant',
    'zh_hk': 'zh-HK',
    'zh_latn': 'zh-Latn',
    'zh_mo': 'zh-MO',
    'zh_sg': 'zh-SG',
    'zh_tw': 'zh-TW',
    'zh': 'zh',
}


function update_calendar(direction = '', direction_type = '') {
    let dados = {};
   let expiration = new Date(Date.now() + 604800000);

    const base = localStorage.getItem('sezimal-calendar-base');
    const format_token = localStorage.getItem('sezimal-calendar-format-token');
    const locale = localStorage.getItem('sezimal-calendar-locale');
    const time_zone = localStorage.getItem('sezimal-calendar-time-zone');
    const hour_format = localStorage.getItem('sezimal-calendar-hour-format');
    const hemisphere = localStorage.getItem('sezimal-calendar-hemisphere');

    document.documentElement.lang = LANGUAGE_TAGS[locale];
    document.cookie = `sezimal=${base}|${encodeURI(format_token)}|${locale}|${time_zone}|${hour_format}|${hemisphere};Domain=.sezimal.tauga.online;Path=/;Secure;SameSite=none;Expires=${expiration.toUTCString()}; `;

    if ((locale == 'ar') || (locale == 'fa') || (locale == 'he')) {
        document.documentElement.dir = 'rtl';
    } else {
        document.documentElement.dir = 'ltr';
    };

    dados = {
        base: base,
        format_token: format_token,
        locale: locale,
        time_zone: time_zone,
        hour_format: hour_format,
        hemisphere: hemisphere,
        date: localStorage.getItem('sezimal-calendar-date'),
        view: localStorage.getItem('sezimal-calendar-view'),
        theme: localStorage.getItem('sezimal-calendar-theme'),
        direction: direction,
        direction_type: direction_type,
    };

    fetch('/calendar/process', {
        method: 'post',
        body: JSON.stringify(dados),
        headers: {
            'Accept': 'application/json; charset=UTF-8',
            'Content-Type': 'application/json; charset=UTF-8'
        }
    }).then((response) => {
        return response.json();
    }).then((dados) => {
        // console.log('dados', dados);
        localStorage.setItem('sezimal-calendar-date', dados.date_to_store);
        document.getElementById('calendar_view').innerHTML = dados.view;
        return dados;
    }).then((dados) => {
        if  (document.getElementById('view_script')) {
            document.getElementById('view_script').remove();
        };
        if (dados.script_text) {
            var view_script = null;
            view_script = document.createElement('script');
            view_script.id = 'view_script';
            view_script.type = 'text/javascript';
            view_script.async = false;
            view_script.nounce = 'sezimaw';
            view_script.textContent = dados.script_text;
            console.log('calendar_view', document.getElementById('calendar_view'));
            document.getElementById('calendar_view').appendChild(view_script);
        };
    });
};

function change_view(new_view = 'dayly') {
    localStorage.setItem('sezimal-calendar-view', new_view);
    update_calendar();
};

function change_date(new_date) {
    localStorage.setItem('sezimal-calendar-date', new_date);
    update_calendar();
};

function open_settings() {
    document.getElementById('calendar_settings').hidden = false;
    document.getElementById('calendar_view').hidden = true;
    document.getElementById('calendar_event_view').hidden = true;
};

function apply_settings() {
    localStorage.setItem('sezimal-calendar-locale', document.getElementById('calculator-sezimal-locale').value);
    localStorage.setItem('sezimal-calendar-time-zone', document.getElementById('time_zone_select').value);
    localStorage.setItem('sezimal-calendar-hour-format', document.getElementById('hour_format_select').value);
    localStorage.setItem('sezimal-calendar-hemisphere', document.getElementById('hemisphere_select').value);

    if (document.getElementById('base_select_10').checked) {
        localStorage.setItem('sezimal-calendar-base', 10);
        localStorage.setItem('sezimal-calendar-format-token', '');
    } else if (document.getElementById('base_select_10!').checked) {
        localStorage.setItem('sezimal-calendar-base', 10);
        localStorage.setItem('sezimal-calendar-format-token', '!');
    } else if (document.getElementById('base_select_14').checked) {
        localStorage.setItem('sezimal-calendar-base', 14);
        localStorage.setItem('sezimal-calendar-format-token', '9');
    } else if (document.getElementById('base_select_20').checked) {
        localStorage.setItem('sezimal-calendar-base', 20);
        localStorage.setItem('sezimal-calendar-format-token', '↋');
    };

    if (document.getElementById('theme_select_full_color').checked) {
        localStorage.setItem('sezimal-calendar-theme', 'FULL_COLOR');
    } else if (document.getElementById('theme_select_gray').checked) {
        localStorage.setItem('sezimal-calendar-theme', 'GRAY');
    };

    // document.getElementById('calendar_settings').hidden = true;
    // document.getElementById('calendar_view').hidden = false;
    // update_calendar();
    location.reload();
};


function open_event_window() {
    let dados = {};

    dados = {
        base: localStorage.getItem('sezimal-calendar-base'),
        format_token: localStorage.getItem('sezimal-calendar-format-token'),
        locale: localStorage.getItem('sezimal-calendar-locale'),
        time_zone: localStorage.getItem('sezimal-calendar-time-zone'),
        date: localStorage.getItem('sezimal-calendar-date'),
        view: 'event',
        theme: localStorage.getItem('sezimal-calendar-theme'),
        hour_format: localStorage.getItem('sezimal-calendar-hour-format'),
    };

    fetch('/calendar/event-window', {
        method: 'post',
        body: JSON.stringify(dados),
        headers: {
            'Accept': 'application/json; charset=UTF-8',
            'Content-Type': 'application/json; charset=UTF-8'
        }
    }).then((response) => {
        return response.json();
    }).then((dados) => {
        console.log('dados', dados);

        document.getElementById('calendar_event_view').innerHTML = dados.view;

        if  (document.getElementById('event_view_script')) {
            document.getElementById('event_view_script').remove();
        };
        if (dados.script_text) {
            var view_script = null;
            view_script = document.createElement('script');
            view_script.id = 'event_view_script';
            view_script.type = 'text/javascript';
            view_script.async = false;
            view_script.nounce = 'sezimaw';
            view_script.textContent = dados.script_text;
            console.log('calendar_event_view', document.getElementById('calendar_event_view'));
            document.getElementById('calendar_event_view').appendChild(view_script);
        };

        document.getElementById('calendar_event_view').style = 'display: block;';
    });
};


function save_event() {
    document.getElementById('calendar_event_view').style = 'display: none;';
    if  (document.getElementById('event_view_script')) {
        document.getElementById('event_view_script').remove();
    };
    document.getElementById('calendar_event_view').innerHTML = '';
};

function close_event() {
    document.getElementById('calendar_event_view').style = 'display: none;';
    if  (document.getElementById('event_view_script')) {
        document.getElementById('event_view_script').remove();
    };
    document.getElementById('calendar_event_view').innerHTML = '';
};
