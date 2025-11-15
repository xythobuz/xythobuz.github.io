// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later

// helper to show or hide scroll-up-button depending on scroll position
function scroll_visibility() {
    if ($(document).scrollTop() > 0) {
        $("#scroll_up").show("fast");
    } else {
        $("#scroll_up").hide("fast");
    }
}

$(function() {
    // don't show on short pages
    if ($("html").outerHeight() <= $(window).height()) {
        return;
    }

    // add button, initially hidden
    $("<a>", {
        text: "⇑",
        id: "scroll_up_btn",
        click: function() {
            var hash = location.hash.replace("#","");
            if (hash != "") {
                var loc = window.location.href.split('#')[0];
                window.history.pushState({}, "", loc);
            }
            window.scrollTo({ top: 0, behavior: "auto" });
            return true;
        },
    }).appendTo('#scroll_up');
    $("#scroll_up").hide();

    // register handler and set initial state
    scroll_visibility();
    $(window).on("scroll", scroll_visibility);
});
// @license-end
