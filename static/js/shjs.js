// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
$(function() {
    // adapted from https://sourceforge.net/p/shjs/feature-requests/5/#0940
    $("pre[class^='sh_']").each(function() {
        // wrap pre with div._sh and .copy for Copy To Clipboard buttons
        $('<div class="_sh copy"><div class="_sh_lines"></div></div>').insertBefore($(this));
        $(this).appendTo($(this).prev('._sh'));

        // allow skipping line numbers
        if ($(this).attr("data-skip") != undefined) {
            return;
        }

        // split content of pre with linebreaks so we can get total line number
        var content = $.trim($(this).html());
        var lines = content.split('\n');

        // configurable line number offset
        var line_cnt_off = "1";
        if ($(this).attr("data-offset") != undefined) {
            line_cnt_off = $(this).attr("data-offset");
        }
        var max = lines.length + parseInt(line_cnt_off);

        // append line number to span._sh_lines
        for (var line = line_cnt_off; line < max; line++) {
            $(this).prev('._sh_lines').append('<span data-line="' + line + '">' + line + '</span>');
        }
    });

    $("pre:not([class^='sh_']):not([class='ascii'])").each(function() {
        // wrap pre with div._sh
        $('<div class="_sh"></div>').insertBefore($(this));
        $(this).appendTo($(this).prev('._sh'));
    });

    sh_highlightDocument('/js/sh/', '.min.js');
});
// @license-end
