// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
$(function() {
    $(".collapse").on("click", function() {
        $(this).toggleClass("collapseactive");
        var content = $(this).next(".collapsecontent");

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
                // used for rss.xsl
                var f = $(content).children("iframe").first();
                var h = $(f).prop('contentWindow').document.body.scrollHeight;

                // limit height to 800px
                if (h > 800) {
                    h = 800;
                } else {
                    h += 50; // TODO need some padding to avoid scrollbar in iframe?!
                }

                $(f).css("height", h + "px"); // set iframe height also
                $(content).css("max-height", h + "px");
            }

            $(content).css("border-width", "2px");
        }
    });

    $(".collapse_menu").on("click", function() {
        $(this).toggleClass("collapseactive_menu");
        var content = $(this).next(".collapsecontent_menu");
        if ($(content).css("max-height") != "0px") {
            $(content).css("max-height", 0);
        } else {
            $(content).css("max-height", $(content).prop('scrollHeight') + "px");
        }
    });
});
// @license-end
