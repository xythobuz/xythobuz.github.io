title: Blog
post: Telekom Speedport Reset Script
date: 2015-07-22
comments: true
flattr: true
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

Ich quäle mich immer noch mit der unfassbar schlechten Weboberfläche meines Telekom Routers herum... Man sollte denken, den Neustart des Routers über die Weboberfläche könnte man mit ein paar einfachen curl Kommandos beginnen. Aber nein, weit gefehlt. Ich musste den Traffic schon mit Wireshark capturen und nachbauen, denn wenn z.B. der Referer nicht stimmt geht gar nix.

Hier also das Ergebnis meiner Anstrengungen :D

    #!/bin/bash
    
    COOKIE_FILE=~/.routerCookie
    ROUTER_PASSWORD=YourTopSecretPassword
    
    echo Logging in...
    curl --silent --location -b $COOKIE_FILE -c $COOKIE_FILE --data-urlencode "login_pwd=1" --data-urlencode "pws=$ROUTER_PASSWORD" --referer "http://speedport.ip/" "http://speedport.ip/cgi-bin/login.cgi"
    
    echo Waiting...
    echo sleep 1
    
    echo Resetting...
    curl --silent -X POST --location -b $COOKIE_FILE -c $COOKIE_FILE --referer "http://speedport.ip/hcti_hilfsmittel_reboot.stm" "http://speedport.ip/cgi-bin/restart.cgi"
    
    echo Deleting stale cookie...
    rm -rf $COOKIE_FILE
    
    echo Done!

Ein Logout ist dabei nicht nötig, der Router vergisst die Session nach dem Neustart.

