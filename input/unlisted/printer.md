title: 3D Printers
description: Live updated images of my 3D printers
parent: none
position: 0
---

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
    } catch(y) {  }
}
</script>

# {{ page.title }}

This page contains photos from the Webcams on my 3D printers, live-updated every 5 minutes.

## Fabrikator Mini V1.5

<div id="date-1">
    <noscript>
        <img src="printer.jpg" alt="Fabrikator Mini V1.5">
    </noscript>
</div>

<script type="text/javascript">
    var rt = LastModUsingHeader("printer.jpg", function(i, u) {
        var img = document.createElement("img");
        img.src = window.URL.createObjectURL(i);
        img.alt = "Fabrikator Mini V1.5";

        var up = document.createElement("p");
        up.appendChild(document.createTextNode("Upload Date: " + u));

        var dt = document.getElementById("date-1");
        dt.appendChild(img);
        dt.appendChild(up);
    });
</script>

<hr>

## CTC i3 Pro B

<div id="date-2">
    <noscript>
        <img style="transform: rotate(180deg);" src="printer-2.jpg" alt="CTC i3 Pro B">
    </noscript>
</div>

<script type="text/javascript">
    var rt = LastModUsingHeader("printer-2.jpg", function(i, u) {
        var img = document.createElement("img");
        img.src = window.URL.createObjectURL(i);
        img.alt = "CTC i3 Pro B";
        img.style = "transform: rotate(180deg);";

        var up = document.createElement("p");
        up.appendChild(document.createTextNode("Upload Date: " + u));

        var dt = document.getElementById("date-2");
        dt.appendChild(img);
        dt.appendChild(up);
    });
</script>

