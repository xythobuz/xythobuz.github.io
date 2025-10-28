// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
function generate_toc() {
    var output = '<div id="toc">';
    output += '<h3 class="toc">Table of Contents <a id="toc_close">❎</a></h3>';
    output += '<ul>';
    var level = 0;
    var counters = [ 1, 1, 1 ];

    $("#content").children("h2, h3, h4").each(function() {
        var this_level = parseInt($(this).prop("tagName").slice(1));
        if (level <= 0) level = this_level;
        if (this_level > level) {
            output += '<ul>';
        } else if (this_level < level) {
            output += '</ul>';
            counters[level - 2] = 1;
        }
        level = this_level;

        var title = '';
        var link = '';
        for (var lvl = 2; lvl <= this_level; lvl++) {
            if (lvl > 2) {
                title += ".";
                link += ".";
            }
            title += counters[lvl - 2] - ((lvl < this_level) ? 1 : 0);
            link += counters[lvl - 2] - ((lvl < this_level) ? 1 : 0);
        }

        title += ') ';
        title += $(this).text();

        link += '_';
        link += $('<span>').text($(this).text().toLowerCase().split(' ').join('_')).html();

        output += '<li>';
        output += '<a class="toc_btn" href="#' + link + '">' + title + '</a>';
        output += '</li>';

        $(this).before('<a class="anchor al' + this_level + '" name="' + link + '" href="#' + link + '"></a>')

        counters[this_level - 2]++;
    });

    output += '</ul>';
    output += '</div>';
    $("#toc_wrap").html(output);

    $("#toc_close").on("click", function() {
        $("#toc_wrap").toggle("fast");
        return false;
    });
}

function register_toc_toggle() {
    $("<a>", {
        text: "toggle visibility of Table of Contents",
        href: "",
        id: "toc_toggle",
        click: function() {
            $("#toc_wrap").toggle("fast");
            return false;
        },
    }).appendTo('#toc_toggle_wrap');
}

function listen_for_anchor_scrolls() {
    var scroll_timeout = 0;

    // don't update hash while scrolling for 1s after toc click
    function prevent_auto_anchor() {
        scroll_timeout = Date.now() + 1000;
        return true;
    }
    $(".toc_btn").each(function() {
        $(this).on("click", prevent_auto_anchor)
    });
    $("#scroll_up").on("click", prevent_auto_anchor);

    $(window).on("scroll", function() {
        if (Date.now() < scroll_timeout) {
            return;
        }

        // remove hash when scrolled to top
        if ($(document).scrollTop() < 50) {
            const location = window.location.href.split('#')[0];
            history.replaceState({}, "", location);
            return;
        }

        // check all headings and set hash if we scrolled past
        $("#content").children("h2, h3, h4").each(function() {
            const top = $(this)[0].getBoundingClientRect().top;
            if ((top > 50) && (top < 200)) {
                const location = window.location.href.split('#')[0];
                const link = $(this).prev().attr("name");
                history.replaceState({}, "", location + '#' + link);
            }
        });
    });
}

generate_toc();
register_toc_toggle();
listen_for_anchor_scrolls();
// @license-end
