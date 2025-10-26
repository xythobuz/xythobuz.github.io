// helper to show or hide scroll-up-button depending on scroll position
function scroll_visibility() {
    if ($(document).scrollTop() > 0) {
        $("#scroll_up").show("fast");
    } else {
        $("#scroll_up").hide("fast");
    }
}

$(document).ready(function() {
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
                const location = window.location.href.split('#')[0];
                window.history.pushState({}, "", location);
            }
            window.scrollTo({ top: 0, behavior: "auto" });
            return true;
        },
    }).appendTo('#scroll_up');
    $("#scroll_up").hide();

    // register handler and set initial state
    scroll_visibility();
    $(window).scroll(scroll_visibility);
});
