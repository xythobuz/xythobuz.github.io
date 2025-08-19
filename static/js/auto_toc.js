function generate_toc() {
    var output = '<div id="toc">';
    output += '<h3 class="toc">Table of Contents</h3>';
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
        output += '<a href="#' + link + '">' + title + '</a>';
        output += '</li>';

        $(this).before('<a class="anchor al' + this_level + '" name="' + link + '" href="#' + link + '"></a>')

        counters[this_level - 2]++;
    });

    output += '</ul>';
    output += '</div>';
    $("#toc_wrap").html(output);
}

function register_toc_toggle() {
    $("<a>", {
        text: "toggle ToC visibility",
        href: "",
        id: "toc_toggle",
        click: function() {
            $("#toc_wrap").toggle("fast");
            return false;
        },
    }).appendTo('#toc_toggle_wrap');
}

generate_toc();
register_toc_toggle();
