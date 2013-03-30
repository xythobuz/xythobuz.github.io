title: Blog
post: Odys Genio USB Debugging am Mac
date: 2013-01-31
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

Um das [Odys Genio (Affiliate Link)][1] auch am Mac für USB Debugging nutzen zu können, muss die USB Vendor ID des Genio in die Konfigurationsdatei der Android Debug Bridge eingetragen werden. Hierfür erstmal die VID des Genio im System Profiler ermitteln (bei mir 0x2207). Dann kann diese Nummer, allein in einer einzelnen Zeile, in die Datei ~/.android/adb_usb.ini eingetragen werden. Sollte die Datei nicht existieren, einfach neu anlegen, mit der VID als einzigem Inhalt. Anschließend eventuell das Tablet erneut anschließen, und adb neu starten: 

<pre class="sh_sh">
adb kill-server
adb start-server
</pre>

 [1]: http://www.amazon.de/gp/product/B00A7PZM7E/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00A7PZM7E&linkCode=as2&tag=xythobuzorg-21