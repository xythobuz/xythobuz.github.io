$(document).ready(function() {
    jQuery(window).resize(function() {
        $('#wrap').css('height', $('#nav').css('height'));
    });

    var fontSize = parseInt($('body').css('font-size'), 10);
    var initialFontSize = fontSize;

    $('.inc').on('click', function() {
        fontSize += 1;
        $('#content').css('font-size', fontSize + 'px');
    })
    $('.dec').on('click', function() {
        if (fontSize > 1) {
            fontSize -= 1;
            $('#content').css('font-size', fontSize + 'px');
        }
    })
    $('.reset').on('click', function() {
        if (fontSize != initialFontSize) {
            fontSize = initialFontSize;
            $('#content').css('font-size', initialFontSize + 'px');
        }
    })

    $(document).keypress(function(event) {
        if (event.charCode == '+'.charCodeAt(0)) {
            fontSize += 1;
            $('#content').css('font-size', fontSize + 'px');
        }
        if (event.charCode == '-'.charCodeAt(0)) {
            if (fontSize > 1) {
                fontSize -= 1;
                $('#content').css('font-size', fontSize + 'px');
            }
        }
        if (event.charCode == '0'.charCodeAt(0)) {
            if (fontSize != initialFontSize) {
                fontSize = initialFontSize;
                $('#content').css('font-size', initialFontSize + 'px');
            }
        }
    });
});
