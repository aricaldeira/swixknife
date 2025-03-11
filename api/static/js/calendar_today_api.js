
const LANGUAGE_TAGS = {
    'ar_latn': 'ar-Latn',
    'ar': 'ar',
    'ar_nu_latn': 'ar-u-nu-Latn',
    'bn_latn': 'bn-Latn',
    'bn': 'bn',
    'bn_nu_latn': 'bn-u-nu-Latn',
    'bz_br': 'bz-BR',
    'bz_pt': 'bz-PT',
    'bz': 'bz',
    'ca': 'ca',
    'code': 'code',
    'da': 'da',
    'de_at': 'de-AT',
    'de_be': 'de-BE',
    'de_de': 'de-DE',
    'de_it': 'de-IT',
    'de_li': 'de-LI',
    'de_lu': 'de-LU',
    'de': 'de',
    'el': 'el',
    'el_colloquial': 'el',
    'en_au': 'en-AU',
    'en_br': 'en-BR',
    'en_ca': 'en-CA',
    'en_gb': 'en-GB',
    'en_gb-metric': 'en-GB-metric',
    'en_ie': 'en-IE',
    'en_il': 'en-IL',
    'en_in': 'en-IN',
    'en_my': 'en-MY',
    'en_nyoo_speling': 'en-NYOO-SPELING',
    'en_nz': 'en-NZ',
    'en_shaw': 'en-Shaw',
    'en_us': 'en-US',
    'en_us-metric': 'en-US-metric',
    'en_za': 'en-ZA',
    'en': 'en',
    'eo_au': 'eo-AU',
    'eo_br': 'eo-BR',
    'eo_ca': 'eo-CA',
    'eo_jp': 'eo-JP',
    'eo_us': 'eo-US',
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
    'es_us': 'es-US',
    'es_uy': 'es-UY',
    'es': 'es',
    'et': 'et',
    'fa_latn': 'fa-Latn',
    'fa': 'fa',
    'fa_nu_latn': 'fa-u-nu-Latn',
    'fi': 'fi',
    'fr_be': 'fr-BE',
    'fr_ca': 'fr-CA',
    'fr_ch': 'fr-CH',
    'fr_fr': 'fr-FR',
    'fr_lu': 'fr-LU',
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
    'hi_nu_latn': 'hi-u-nu-Latn',
    'hu': 'hu',
    'id': 'id',
    'is': 'is',
    'iso_dot': 'iso-Dot',
    'iso': 'iso',
    'it': 'it',
    'iu_latn': 'iu-Latn',
    'iu': 'iu',
    'ja': 'ja',
    'kea': 'kea',
    'kn': 'kn',
    'kn_nu_latn': 'kn-u-nu-Latn',
    'ko': 'ko',
    'lat': 'lat',
    'lb': 'lb',
    'mt': 'mt',
    'nb': 'nb',
    'nl_be': 'nl-BE',
    'nl': 'nl-NL',
    'nn': 'nn',
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
    'sv_fi': 'sv-FI',
    'sv_se': 'sv-SE',
    'sv': 'sv',
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

function _base_data(direction = '', direction_type = '') {
    let dados = {};
    let expiration = new Date(Date.now() + 604800000);

    const base = localStorage.getItem('sezimal-calendar-base');
    const format_token = localStorage.getItem('sezimal-calendar-format-token');
    const locale = localStorage.getItem('sezimal-calendar-locale');
    const time_zone = localStorage.getItem('sezimal-calendar-time-zone');
    const hour_format = localStorage.getItem('sezimal-calendar-hour-format');
    const hemisphere = localStorage.getItem('sezimal-calendar-hemisphere');
    const theme = localStorage.getItem('sezimal-calendar-theme');
    const mobile = (/Mobile|Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent));
    let show_holiday = localStorage.getItem('sezimal-calendar-show-holiday');
    const show_seconds = localStorage.getItem('sezimal-calendar-show-seconds');
    const locale_first_weekday = localStorage.getItem('sezimal-calendar-locale-first-weekday');
    let calendar_displayed = localStorage.getItem('sezimal-calendar-displayed');
    const local_time_zone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    if (calendar_displayed.indexOf('+') != -1) {
        calendar_displayed = calendar_displayed.split('+')[0];
    };

    if (
        (localStorage.getItem('sezimal-calendar-show-holiday-christian') == true)
        || (localStorage.getItem('sezimal-calendar-show-holiday-christian') == 'true')
    ) {
        show_holiday = show_holiday + '_CHR';
    };

    if (
        (localStorage.getItem('sezimal-calendar-show-holiday-orthodox') == true)
        || (localStorage.getItem('sezimal-calendar-show-holiday-orthodox') == 'true')
    ) {
        show_holiday = show_holiday + '_ORT';
    };

    if (
        (localStorage.getItem('sezimal-calendar-show-holiday-islamic') == true)
        || (localStorage.getItem('sezimal-calendar-show-holiday-islamic') == 'true')
    ) {
        show_holiday = show_holiday + '_HIJ';
    };

    if (
        (localStorage.getItem('sezimal-calendar-show-holiday-jewish') == true)
        || (localStorage.getItem('sezimal-calendar-show-holiday-jewish') == 'true')
    ) {
        show_holiday = show_holiday + '_JEW';
    };

    document.documentElement.lang = LANGUAGE_TAGS[locale];
    document.cookie = `sezimal=${base}|${encodeURI(format_token)}|${locale}|${time_zone}|${hour_format}|${hemisphere}|${theme}|${mobile}|${show_holiday}|${show_seconds}|${calendar_displayed}|${locale_first_weekday}|${local_time_zone};Domain=.sezimal.tauga.online;Path=/;Secure;SameSite=none;Expires=${expiration.toUTCString()}; `;

    if ((locale == 'ar') || (locale == 'ar_nu_latn') ||
        (locale == 'fa') || (locale == 'fa_nu_latn') ||
        (locale == 'he')) {
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
        theme: theme,
        date: localStorage.getItem('sezimal-calendar-date'),
        view: localStorage.getItem('sezimal-calendar-view'),
        direction: direction,
        direction_type: direction_type,
        mobile: mobile,
        show_holiday: show_holiday,
        show_seconds: show_seconds,
        calendar_displayed: calendar_displayed,
        locale_first_weekday: locale_first_weekday,
        local_time_zone: local_time_zone,
    };

    return dados;
}

async function update_calendar(direction = '', direction_type = '') {
    let dados = _base_data(direction, direction_type)

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
            document.getElementById('calendar_view').appendChild(view_script);
        };
    });
};

async function change_view(new_view = 'dayly') {
    localStorage.setItem('sezimal-calendar-view', new_view);
    update_calendar();
};

async function change_date(new_date) {
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
    localStorage.setItem('sezimal-calendar-show-seconds', document.getElementById('show_seconds_input').checked);
    localStorage.setItem('sezimal-calendar-locale-first-weekday', document.getElementById('locale_first_weekday_input').checked);
    localStorage.setItem('sezimal-calendar-hemisphere', document.getElementById('hemisphere_select').value);
    localStorage.setItem(
        'sezimal-calendar-show-holiday',
        document.getElementById('show_holiday_select').value
    );
    localStorage.setItem(
        'sezimal-calendar-show-holiday-christian',
        document.getElementById('religious_calendar_input_christian').checked
    );
    // localStorage.setItem(
    //     'sezimal-calendar-show-holiday-orthodox',
    //     document.getElementById('religious_calendar_input_orthodox').checked
    // );
    localStorage.setItem(
        'sezimal-calendar-show-holiday-islamic',
        document.getElementById('religious_calendar_input_islamic').checked
    );
    localStorage.setItem(
        'sezimal-calendar-show-holiday-jewish',
        document.getElementById('religious_calendar_input_jewish').checked
    );

    const calendar_displayed = document.getElementById('calendar_displayed_select').value;

    localStorage.setItem('sezimal-calendar-displayed', calendar_displayed);

    if (calendar_displayed.indexOf('+') == -1) {
        localStorage.setItem('sezimal-calendar-base', 10);
        localStorage.setItem('sezimal-calendar-format-token', '');
    } else if (calendar_displayed.endsWith('+!')) {
        localStorage.setItem('sezimal-calendar-base', 10);
        localStorage.setItem('sezimal-calendar-format-token', '!');
    } else if (calendar_displayed.endsWith('+9')) {
        localStorage.setItem('sezimal-calendar-base', 14);
        localStorage.setItem('sezimal-calendar-format-token', '9');
    } else if (calendar_displayed.endsWith('+↋')) {
        localStorage.setItem('sezimal-calendar-base', 20);
        localStorage.setItem('sezimal-calendar-format-token', '↋');
    } else if (calendar_displayed.endsWith('+c')) {
        localStorage.setItem('sezimal-calendar-base', 10);
        localStorage.setItem('sezimal-calendar-format-token', 'c');
    } else if (calendar_displayed.endsWith('+c!')) {
        localStorage.setItem('sezimal-calendar-base', 10);
        localStorage.setItem('sezimal-calendar-format-token', 'c!');
    } else if (calendar_displayed.endsWith('+c9')) {
        localStorage.setItem('sezimal-calendar-base', 14);
        localStorage.setItem('sezimal-calendar-format-token', 'c9');
    } else if (calendar_displayed.endsWith('+c↋')) {
        localStorage.setItem('sezimal-calendar-base', 20);
        localStorage.setItem('sezimal-calendar-format-token', 'c↋');
    };

    localStorage.setItem('sezimal-calendar-theme', document.getElementById('theme_select').value);

    localStorage.setItem('sezimal-latitude', document.getElementById('sezimal-latitude-input').value);
    localStorage.setItem('sezimal-longitude', document.getElementById('sezimal-longitude-input').value);

    // document.getElementById('calendar_settings').hidden = true;
    // document.getElementById('calendar_view').hidden = false;
    // update_calendar();
    location.reload();
};


async function update_weather() {
    if (
        (
            (!localStorage.getItem('sezimal-latitude'))
            || (!localStorage.getItem('sezimal-longitude'))
        ) &&
        (
            (!localStorage.getItem('sezimal-gps-latitude'))
            || (!localStorage.getItem('sezimal-gps-longitude'))
        )
    ) {
        document.getElementById('weather_view').style = "display: none;";
        document.getElementById('decimal_weather_display').style = "display: none;";
        return;
    };

    document.getElementById('weather_view').style = "display: inline;";

    let dados = _base_data()

    if (dados['base'] != 14) {
        document.getElementById('decimal_weather_display').style = "display: inline;";
    };

    if (
        localStorage.getItem('sezimal-latitude')
        && localStorage.getItem('sezimal-longitude')
    ) {
        dados['latitude'] = localStorage.getItem('sezimal-latitude');
        dados['longitude'] = localStorage.getItem('sezimal-longitude');
    } else {
        dados['latitude'] = localStorage.getItem('sezimal-gps-latitude');
        dados['longitude'] = localStorage.getItem('sezimal-gps-longitude');
    };

    fetch('/weather/process', {
        method: 'post',
        body: JSON.stringify(dados),
        headers: {
            'Accept': 'application/json; charset=UTF-8',
            'Content-Type': 'application/json; charset=UTF-8'
        }
    }).then((response) => {
        return response.json();
    }).then((dados) => {
        document.getElementById('weather_view').innerHTML = dados.view;
        if (dados['base'] != 14) {
            document.getElementById('decimal_weather_display').innerHTML = dados.decimal_weather;
        };
    });
};
