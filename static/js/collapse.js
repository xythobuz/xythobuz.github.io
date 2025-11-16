// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
$(function() {
    $("div.collapse").each(function() {
        $(this).on("click", function() {
            $(this).toggleClass("collapseactive");
            var content = $(this).next("div.collapsecontent");

            if ($(content).css("max-height") != "0px") {
                $(content).css("max-height", 0);
                setTimeout(function() {
                    $(content).css("border-width", 0);
                    $(content).css("display", "none");
                }, 120);
            } else {
                $(content).css("display", "block");

                if ($(content).children("iframe").length == 0) {
                    // normally we set the height of the expanded div to the height of the contents
                    $(content).css("max-height", $(content).prop('scrollHeight') + "px");
                } else {
                    // special case for iframes, also get the height of their contents
                    var f = $(content).children("iframe").first();
                    var h = $(f).prop('contentWindow').document.body.scrollHeight;
                    h += 100; // TODO need some padding to avoid scrollbar in iframe?!
                    $(f).css("height", h + "px"); // set iframe height also
                    $(content).css("max-height", h + "px");
                }

                $(content).css("border-width", "2px");
            }
        });
    });
});
// @license-end
