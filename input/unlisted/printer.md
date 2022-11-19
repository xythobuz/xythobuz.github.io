title: 3D Printers
description: Live updated images of my 3D printers
parent: none
position: 0
noheader: true
---

# {{ page.title }}

This page contains photos from the Webcams on my 3D printers, live-updated every 5 minutes.

## i3 AM8

<div id="date-am8">
    <noscript>
        <a href="//www.xythobuz.de/printer-am8.jpg">
            <img src="//www.xythobuz.de/printer-am8.jpg" alt="i3 AM8 Webcam Photo">
        </a>
    </noscript>
</div>

<script type="text/javascript">
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
</script>
