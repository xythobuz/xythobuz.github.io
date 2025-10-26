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
});
