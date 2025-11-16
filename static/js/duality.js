// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later

dw = document.getElementById("duality_wrap");
dw.addEventListener('resize', function(event) {
    event.target.style.width = `${event.target.clientWidth}px`;
    event.target.style.height = `${event.target.clientWidth * 160 / 144}px`;
});

EJS_language = '';
EJS_player = "#duality_game";
EJS_core = "gb";
EJS_pathtodata = "emu_js/";
EJS_gameUrl = "https://xythobuz.github.io/Duality/duality.gb";
EJS_alignStartButton = "center";
EJS_backgroundImage = "https://xythobuz.github.io/Duality/cartridge.png";
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    EJS_backgroundColor = "#111111";
} else {
    EJS_backgroundColor = "#DDDDDD";
}
EJS_defaultControls = {
    0: {
        0: {
            'value': 'a',
            'value2': 'BUTTON_2'
        },
        2: {
            'value': 'space',
            'value2': 'SELECT'
        },
        3: {
            'value': 'enter',
            'value2': 'START'
        },
        4: {
            'value': 'up arrow',
            'value2': 'DPAD_UP'
        },
        5: {
            'value': 'down arrow',
            'value2': 'DPAD_DOWN'
        },
        6: {
            'value': 'left arrow',
            'value2': 'DPAD_LEFT'
        },
        7: {
            'value': 'right arrow',
            'value2': 'DPAD_RIGHT'
        },
        8: {
            'value': 's',
            'value2': 'BUTTON_1'
        }
    },
    1: {},
    2: {},
    3: {}
};
EJS_startButtonName = "Start Duality";

// @license-end
