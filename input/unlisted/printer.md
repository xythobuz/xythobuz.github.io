title: 3D Printers
description: Live updated images of my 3D printers
parent: none
position: 0
noheader: true
---

# {{ page.title }}

This page contains photos from the Webcams on my 3D printers, live-updated every 5 minutes.

## CTC i3 Pro B

<div id="date-2">
    <noscript>
        <a href="//www.xythobuz.de/printer-2.jpg">
            <img src="//www.xythobuz.de/printer-2.jpg" alt="CTC i3 Pro B">
        </a>
    </noscript>
</div>

<hr>

## Fabrikator Mini V1.5

<div id="date-1">
    <noscript>
        <a href="//www.xythobuz.de/printer.jpg">
            <img src="//www.xythobuz.de/printer.jpg" alt="Fabrikator Mini V1.5">
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
    LastModUsingHeader("//www.xythobuz.de/printer-2.jpg", function(i, u) {
        var img = document.createElement("img");
        img.src = window.URL.createObjectURL(i);
        img.alt = "CTC i3 Pro B";

        var link = document.createElement("a");
        link.href = "//www.xythobuz.de/printer-2.jpg";
        link.appendChild(img);

        var up = document.createElement("p");
        up.appendChild(document.createTextNode("Upload Date: " + u));

        var dt = document.getElementById("date-2");
        dt.appendChild(link);
        dt.appendChild(up);
    });
    LastModUsingHeader("//www.xythobuz.de/printer.jpg", function(i, u) {
        var img = document.createElement("img");
        img.src = window.URL.createObjectURL(i);
        img.alt = "Fabrikator Mini V1.5";

        var link = document.createElement("a");
        link.href = "//www.xythobuz.de/printer.jpg";
        link.appendChild(img);

        var up = document.createElement("p");
        up.appendChild(document.createTextNode("Upload Date: " + u));

        var dt = document.getElementById("date-1");
        dt.appendChild(link);
        dt.appendChild(up);
    });
</script>
