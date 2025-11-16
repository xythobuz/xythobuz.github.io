// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later

const in_iframe = (window.self !== window.top);
if (in_iframe) {
    var plugins = [
        lgAutoplay,
        lgFullscreen,
        //lgHash,
        lgRotate,
        lgThumbnail,
        lgVideo,
        lgZoom,
    ];
} else {
    var plugins = [
        lgAutoplay,
        lgFullscreen,
        lgHash,
        lgRotate,
        lgThumbnail,
        lgVideo,
        lgZoom,
    ];
}

function init_lg() {
    // configuration for lightgallery
    var settings = {
        allowMediaOverlap: false,
        backdropDuration: 100,
        licenseKey: 'gpl-foobar',
        hideBarsDelay: 2500,
        hideScrollbar: true,
        iframeMaxHeight: "75%",
        iframeMaxWidth: "75%",
        mousewheel: true,
        plugins: plugins,
        speed: 100,
        startAnimationDuration: 100,
        showZoomInOutIcons: true,
        toggleThumb: true, // no effect due to allowMediaOverlap=false
        autoplayVideoOnSlide: true,
        youTubePlayerParams: {
            modestbranding: 1,
            showinfo: 0,
            rel: 0,
            mute: 0,
        },
        galleryId: "0",
    };

    // create a single lightgallery instance for all relevant divs
    var old_selector = $("div.lightgallery a").toArray();
    var new_selector = $("div.lightgallery_new .border:has(>a>img)").toArray();
    settings.selector = old_selector.concat(new_selector);
    if (settings.selector.length > 0) {
        lightGallery(document.body, settings);
    }

    // attach mouse following thumbnail zoom stuff to lightgallery images
    $(".border:has(>a>img) .pic").each(function() {
        // filter out youtube videos with auto thumbnails (they have data-poster in the thumbnail)
        if ($(this).attr("data-poster") != undefined) {
            return;
        }

        // filter out youtube videos with custom thumbnail (they have a sibling .picthumb enxt to thumbnail)
        if ($(this).siblings().hasClass("picthumb")) {
            return;
        }

        var border = $(this).parent().parent();

        // filter out locally hosted videos (they have data-video set in .border div)
        if (border.attr("data-video") != undefined) {
            return;
        }

        // set thumbnail as background image of .border div
        var w = $(this).prop('naturalWidth');
        var h = $(this).prop('naturalHeight');
        if (w > 300) {
            var scale = 300 / w;
            w *= scale;
            h *= scale;
        }
        if (h > 300) {
            var scale = 300 / h;
            w *= scale;
            h *= scale;
        }
        border.css("background-size", w.toString() + "px " + h.toString() + "px");
        border.css("background-position", "0px 0px");
        border.css("background-image", "url(" + $(this).attr('src') + ")");

        // make thumbnail (and css hover animation) invisible, but keep zoom cursor
        $(this).css("opacity", 0);

        var mouse_scale = 5;
        var zoom_fact = 1.0 + (1.0 / mouse_scale);

        // allow zooming the thumbnail when scolling while holding down shift
        border.on('wheel', function(e) {
            var diff = 0;
            if (e.originalEvent.deltaY < 0) {
                if (e.originalEvent.shiftKey) {
                    diff = -1;
                }
            } else if (e.originalEvent.deltaY > 0) {
                if (e.originalEvent.shiftKey) {
                    diff = 1;
                }
            }

            if (diff != 0) {
                mouse_scale += diff;
                if (mouse_scale > 10) {
                    mouse_scale = 10;
                }
                if (mouse_scale < 1) {
                    mouse_scale = 1;
                }

                zoom_fact = 1.0 + (1.0 / mouse_scale);
                $(this).trigger("mouseenter");
                return false;
            }

            return true;
        });

        // zoom .border div on mouseenter
        border.on("mouseenter", function() {
            // zoom thumbnail
            var w = $(this).width();
            var h = $(this).height();
            var bw = w * zoom_fact;
            var bh = h * zoom_fact;
            $(this).css("background-size", bw.toString() + "px " + bh.toString() + "px");

            // keep in center
            var dx = -((w * zoom_fact) - w) / 2;
            var dy = -((h * zoom_fact) - h) / 2;
            $(this).css("background-position", dx.toString() + "px " + dy.toString() + "px");

            // dim thumbnail
            $(this).css("filter", "brightness(0.75)");
        });

        // unzoom .border div on mouseleave
        border.on("mouseleave", function() {
            // revert changes
            var w = $(this).width();
            var h = $(this).height();
            $(this).css("background-size", w.toString() + "px " + h.toString() + "px");
            $(this).css("background-position", "0px 0px");
            $(this).css("filter", "brightness(1.0)");
        });

        // make zoomed thumbnail follow mouse cursor in .border div
        border.on("mousemove", function(e) {
            // edge-case when page is loaded while mouse is already inside thumbnail
            // --> we get mousemove without ever mouseenter-ing
            if ($(this).css("filter") != "brightness(0.75)") {
                $(this).trigger("mouseenter");
            }

            var offset = $(this).offset();
            var w = $(this).width();
            var h = $(this).height();

            // relative mouse offset from center of thumbnail
            var rx = (e.pageX - offset.left) - (w / 2);
            var ry = (e.pageY - offset.top) - (h / 2);

            // compensate zoom to keep in center
            var dx = ((w * zoom_fact) - w) / 2;
            var dy = ((h * zoom_fact) - h) / 2;

            // final thumbnail offset
            var x = (-rx / mouse_scale) - dx;
            var y = (-ry / mouse_scale) - dy;
            $(this).css("background-position", x.toString() + "px " + y.toString() + "px");
        });
    });
}

if (in_iframe) {
    $(init_lg);
} else {
    $(window).on("load", init_lg);
}

// @license-end
