// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
$(function() {
    $("div[class='_sh']").each(function() {
        var button = $('<button/>', {
            type: 'button',
            class: 'clip-btn',
            text: 'Copy to clipboard',
        });
        button.on('click', function() {
            var str = $(this).prev().children('pre').get(0);
            window.getSelection().selectAllChildren(str);
            document.execCommand("Copy")
        });
        $(this).after(button);
    });
});
// @license-end
