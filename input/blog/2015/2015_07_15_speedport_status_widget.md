title: Blog
post: Telekom Speedport Status Widget
date: 2015-07-15
comments: true
flattr: true
twitter: xythobuz
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

Manche von uns haben das große Vergnügen, mit einem Speedport Router der Telekom gesegnet zu sein. So steht auch bei uns ein Speedport W723V Typ B.

Zur Zeit habe ich kein großes Vergnügen mit meiner Internetanbindung, daher wäre es angehenm, die Ausgaben der Statusseite des Routers per [GeekTool](http://projects.tynsoe.org/en/geektool/) auf dem Desktop anzuzeigen.

Leider ist die besagte Statusseite nicht nur einfaches HTML, sondern wird mittels Clientseitigem Javascript erzeugt. Groteskerweise setzt der Router je nach Status andere Werte für Variablen im Javascript Code.

Glücklicherweise gibt es einen einfachen Weg diese Seite in einem Headless-Browser auszuführen um die Seite zu *rendern*, nämlich [PhantomJS](http://phantomjs.org). Es genügt ein einfaches `sudo port install phantomjs` zur Installation mittels MacPorts.

Nun brauchen wir ein kleines Javascript um die Seite zu laden und auszuführen ([Quelle](http://superuser.com/a/448517)):

    vim ~/bin/save_page.js

    var system = require('system');
    var page = require('webpage').create();
    page.open(system.args[1], function() {
        console.log(page.content);
        phantom.exit();
    });
    
    :wq

Zu guter letzt noch ein Shellscript, um das Javascript auszuführen und die Ausgabe zu formatieren. Hierzu werden zuerst die unwichtigen Stellen herausgeschnitten, alle HTML-Tags entfernt, leere Zeilen gelöscht und HTML Escape Sequenzen entfernt. Des weiteren werden Leerzeichen hinter Doppelpunkten eingefügt, die erste und zwei Zeilen in der Mitte gelöscht, aufeinanderfolgende Zeilen in Zweierblöcken aneinandergehängt und doppelte Leerzeichen sowie überflüssiger statischer Text entfernt.

Zu guter letzt eine kleine Bash Funktion um die Ausgabe rechtsbündig auszurichten, da das Widget am rechten Rand meines Monitors platziert ist. Das ist natürlich optional.

    vim ~/bin/status.sh
    
    #!/bin/bash
    right() {
        l="$(cat -)";
        s=$(echo -e "$l"| awk ' { if ( length > L ) { L=length} }END{ print L}');
        echo "$l" | while read l;do j=$(((s-${#l})));echo "$(while ((j-->0)); do printf " ";done;)$l";
        done;
    };
    /opt/local/bin/phantomjs /Users/thomas/bin/save_page.js http://speedport.ip/top_status.stm | sed -n '/Internetzugang/,$p' | head -n 34 | sed -E 's/<[^>]*>//g' | sed '/^$/d' | sed -E 's/&[^;]*;//g' | sed 's/:/& /' | tail -n +2 | sed -E '7,8d' | paste -d " " - - | tr -s " " | sed -E 's/Öffentliche WAN-//g' | right
    
    :wq
    chmod a+x ~/bin/status.sh

Die Ausgabe sieht dann so aus:

          DSL-Link: Synchron
    Downstream: 51391 kBit/s
      Upstream: 10048 kBit/s
        IPv4: 87.162.241.165

<div class="yoxview">
    <a href="img/widget1.png" class="thumbnail">
        <img src="img/widget1.png" alt="Screenshot" title="Screenshot 1">
    </a>
    <a href="img/widget2.png" class="thumbnail">
        <img src="img/widget2_small.png" alt="Screenshot" title="Screenshot 2">
    </a>
</div>

