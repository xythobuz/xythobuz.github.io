// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later

// this is used on the rss.xsl feed preview
$("iframe").one("load", function() {
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
        link.async = false; // firefox defaults to async for dynamic script tags
        link.defer = true;
        $(elem).prop('contentDocument').body.append(link);
    }

    // make all links open in parent page instead of iframe
    $(this).contents().find("a").prop("target", "_top");

    // add our custom styles
    add_style(this, "css/style.min.css");
    add_style(this, "css/print.min.css");

    // add external styles
    add_style(this, "lg/lightgallery-bundle.min.css");

    // add external scripts
    add_script(this, "js/jquery-3.7.1.min.js");
    add_script(this, "js/sh_main.min.js");
    add_script(this, "lg/lightgallery.min.js");
    add_script(this, "lg/lg-autoplay.min.js");
    add_script(this, "lg/lg-fullscreen.min.js");
    //add_script(this, "lg/lg-hash.min.js");
    add_script(this, "lg/lg-rotate.min.js");
    add_script(this, "lg/lg-thumbnail.min.js");
    add_script(this, "lg/lg-video.min.js");
    add_script(this, "lg/lg-zoom.min.js");

    // add our custom scripts
    add_script(this, "js/collapse.min.js");
    add_script(this, "js/shjs.min.js");
    add_script(this, "js/lightgallery.min.js");
});

// @license-end
