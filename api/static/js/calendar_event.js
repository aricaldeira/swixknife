
function open_event_list_window() {
    let dados = _base_data();
    dados['view'] = 'event-list';

    fetch('/calendar/event-list-window', {
        method: 'post',
        body: JSON.stringify(dados),
        headers: {
            'Accept': 'application/json; charset=UTF-8',
            'Content-Type': 'application/json; charset=UTF-8'
        }
    }).then((response) => {
        return response.json();
    }).then((dados) => {
        document.getElementById('calendar_event_list_view').innerHTML = dados.view;

        // if  (document.getElementById('event_list_view_script')) {
        //     document.getElementById('event_list_view_script').remove();
        // };
        // if (dados.script_text) {
        //     var view_script = null;
        //     view_script = document.createElement('script');
        //     view_script.id = 'event_list_view_script';
        //     view_script.type = 'text/javascript';
        //     view_script.async = false;
        //     view_script.nounce = 'sezimaw';
        //     view_script.textContent = dados.script_text;
        //     console.log('calendar_event_list_view', document.getElementById('calendar_event_list_view'));
        //     document.getElementById('calendar_event_list_view').appendChild(view_script);
        // };

        document.getElementById('calendar_event_list_view').style = 'display: block;';
    });
};

function open_event_window() {
    let dados = _base_data();
    dados['view'] = 'event';

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

function new_event() {
    // document.getElementById('calendar_event_view').style = 'display: none;';
    // if  (document.getElementById('event_view_script')) {
    //     document.getElementById('event_view_script').remove();
    // };
    // document.getElementById('calendar_event_view').innerHTML = '';

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

function close_event_list() {
    document.getElementById('calendar_event_list_view').style = 'display: none;';
    // if  (document.getElementById('event_view_list_script')) {
    //     document.getElementById('event_view_list_script').remove();
    // };
    document.getElementById('calendar_event_list_view').innerHTML = '';
};

