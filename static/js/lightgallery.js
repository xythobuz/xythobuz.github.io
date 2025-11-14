// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
$(document).ready(function() {
    var settings = {
        allowMediaOverlap: false,
        backdropDuration: 100,
        licenseKey: 'gpl-foobar',
        hideBarsDelay: 2500,
        hideScrollbar: true,
        iframeMaxHeight: "75%",
        iframeMaxWidth: "75%",
        mousewheel: true,
        plugins: [
            lgAutoplay,
            lgFullscreen,
            lgHash,
            lgRotate,
            lgThumbnail,
            lgVideo,
            lgZoom,
        ],
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

    var old_selector = $("div.lightgallery a").toArray();
    var new_selector = $("div.lightgallery_new .border:has(>a>img)").toArray();
    settings.selector = old_selector.concat(new_selector);
    if (settings.selector.length > 0) {
        lightGallery(document.body, settings);
    }

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

        // make thumbnail (and css hover animation) invisible
        $(this).css("opacity", 0);

        const mouse_scale = 5;
        const zoom_fact = 1.0 + (1.0 / mouse_scale);

        // zoom .border div on mouseenter
        border.on("mouseenter", function(e) {
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
            $(this).css("filter", "brightness(75%)");
        });

        // unzoom .border div on mouseleave
        border.on("mouseleave", function(e) {
            // revert changes
            var w = $(this).width();
            var h = $(this).height();
            $(this).css("background-size", w.toString() + "px " + h.toString() + "px");
            $(this).css("background-position", "0px 0px");
            $(this).css("filter", "brightness(100%)");
        });

        // make zoomed thumbnail follow mouse cursor in .border div
        border.on("mousemove", function(e) {
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
});
// @license-end
