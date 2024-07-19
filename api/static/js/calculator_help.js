
function toggle_help() {
    document.getElementById('help-setting-div').hidden = !document.getElementById('help-setting-div').hidden;
    document.getElementById('toggle_help').hidden = !document.getElementById('toggle_help').hidden;
    document.getElementById('displays').hidden = !document.getElementById('displays').hidden;
    document.getElementById('configuration-left').hidden = !document.getElementById('configuration-left').hidden;
    document.getElementById('configuration-right').hidden = !document.getElementById('configuration-right').hidden;

    if (document.getElementById('toggle_help').hidden) {
        document.getElementById('buttons').style = 'visibility: hidden;';
    } else {
        document.getElementById('buttons').style = 'visibility: visible;';
    };
};
