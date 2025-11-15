// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
$(function() {
    // ensure nav bar does not hide content after resizes
    $(window).on('resize', function() {
        $('#wrap').css('height', $('#nav').css('height'));
    });

    // get initial font size from localstorage, if it exists
    var initialFontSize = 100;
    var fontSize = localStorage.getItem('font-size');
    if (fontSize == null) {
        fontSize = initialFontSize;
    } else {
        fontSize = parseInt(fontSize);
    }

    // apply initial zoom
    $('#content').css('font-size', fontSize + '%');

    // click on 'increase'
    $('.inc').on('click', function() {
        fontSize = parseInt(fontSize) + 10;
        $('#content').css('font-size', fontSize + '%');
        localStorage.setItem('font-size', fontSize);
    })

    // click on 'decrease'
    $('.dec').on('click', function() {
        if (parseInt(fontSize) > 10) {
            fontSize = parseInt(fontSize) - 10;
            $('#content').css('font-size', fontSize + '%');
            localStorage.setItem('font-size', fontSize);
        }
    })

    // click on 'reset'
    $('.reset').on('click', function() {
        if (parseInt(fontSize) != initialFontSize) {
            fontSize = initialFontSize;
            $('#content').css('font-size', initialFontSize + '%');
            localStorage.setItem('font-size', fontSize);
        }
    })

    // keyboard shortcuts
    $(document).on('keypress', function(e) {
        // hotkey for 'increase'
        if (e.key == '+') {
            fontSize = parseInt(fontSize) + 10;
            $('#content').css('font-size', fontSize + '%');
            localStorage.setItem('font-size', fontSize);
        }

        // hotkey for 'decrease'
        if (e.key == '-') {
            if (parseInt(fontSize) > 10) {
                fontSize = parseInt(fontSize) - 10;
                $('#content').css('font-size', fontSize + '%');
                localStorage.setItem('font-size', fontSize);
            }
        }

        // hotkey for 'reset'
        if (e.key == '0') {
            if (parseInt(fontSize) != initialFontSize) {
                fontSize = initialFontSize;
                $('#content').css('font-size', initialFontSize + '%');
                localStorage.setItem('font-size', fontSize);
            }
        }
    });
});
// @license-end
