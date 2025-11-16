// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later

// apply custom stylesheets in iframe head
function add_style(elem, name) {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = name;
    link.type = "text/css";
    $(elem).prop('contentDocument').head.append(link);
}

// apply js scripts to iframe body
function add_script(elem, name) {
    const link = document.createElement("script");
    link.src = name;
    link.type = "text/javascript";
    $(elem).prop('contentDocument').body.append(link);
}

// this is used on the rss.xsl feed preview
$("iframe").each(function() {
    $(this).on("load", function() {
        // custom styles
        add_style(this, "css/style.css");
        add_style(this, "css/print.css");

        // external scripts
        add_script(this, "js/sh_main.min.js");
        add_script(this, "lg/lightgallery.min.js");
        add_script(this, "lg/lg-autoplay.min.js");
        add_script(this, "lg/lg-fullscreen.min.js");
        add_script(this, "lg/lg-hash.min.js");
        add_script(this, "lg/lg-rotate.min.js");
        add_script(this, "lg/lg-thumbnail.min.js");
        add_script(this, "lg/lg-video.min.js");
        add_script(this, "lg/lg-zoom.min.js");

        // TODO jQuery not working in iframe?!
        //add_script(this, "js/jquery-3.7.1.min.js");
        //add_script(this, "js/shjs.min.js");
        //add_script(this, "js/lightgallery.min.js");
    });
});

// @license-end
