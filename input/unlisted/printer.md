title: 3D Printer
description: Live updated images of my 3D printer
parent: none
position: 0
noheader: true
---

# {{ page.title }}

This page contains photos from the Webcam on my 3D printer, live-updated every 5 minutes.

## i3 AM8

<div id="date-am8">
    <noscript>
        <a href="//www.xythobuz.de/printer-am8.jpg">
            <img src="//www.xythobuz.de/printer-am8.jpg" alt="i3 AM8 Webcam Photo">
        </a>
    </noscript>
</div>

<script>
// @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
    function LastModUsingHeader(sFile, callback) {
        try {
            var x = new XMLHttpRequest;
            x.responseType = "blob";
            x.onreadystatechange = function() {
                if (x.readyState === 4 && x.status === 200) {
                    var dt = new Date(x.getResponseHeader('Last-Modified'))
                    callback(x.response, dt.toLocaleString());
                }
            };
            x.open('GET', sFile, true);
            x.send();
        } catch(y) {}
    }
    LastModUsingHeader("//www.xythobuz.de/printer-am8.jpg", function(i, u) {
        var img = document.createElement("img");
        img.src = window.URL.createObjectURL(i);
        img.alt = "i3 AM8 Webcam Photo";

        var link = document.createElement("a");
        link.href = "//www.xythobuz.de/printer-am8.jpg";
        link.appendChild(img);

        var up = document.createElement("p");
        up.appendChild(document.createTextNode("Upload Date: " + u));

        var dt = document.getElementById("date-am8");
        dt.appendChild(link);
        dt.appendChild(up);
    });
// @license-end
</script>
