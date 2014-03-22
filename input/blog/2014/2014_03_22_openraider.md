title: Blog
post: OpenRaider fork
date: 2014-03-22
comments: true
flattr: true
twitter: xythobuz
github: https://github.com/xythobuz/OpenRaider
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

Hier war ja im (nicht mehr ganz) neuen Jahr bisher noch nicht so viel los.

Der Grund hierfür ist eigentlich recht klar. Ich habe viel mehr Zeit, als mir eigentlich lieb ist, in mein neues Pet-Project gesteckt (bisher etwa 90h).

Es geht um meinen Fork des seit 2003 inaktiven [OpenRaider][openraider]-Projekts, zu finden auf [GitHub][github] oder [hier auf meinem Server][zaphod].

Nach einigen kleineren Änderungen, um OpenRaider-1.1 vom alten Sourceforge Projekt zu kompilieren, macht der Ersteindruck doch Freude. Immerhin, es scheint mehr oder weniger gut zu funktionieren.

Sämtliche deprecated function calls wurden ersetzt und das Ergebnis lässt sich schon sehen.

[![Screenshot 1 Old OpenRaider][screen2small]][screen2]
[![Screenshot 2 Old OpenRaider][screen3small]][screen3]

Allerdings war das handgemachte makefile build system noch nie sonderlich schön anzusehen. Außerdem kann man mit SDL1 auch niemanden mehr begeistern.

Deshalb wurden SDL und SDL-TTF durch SDL2 und SDL2-TTF ersetzt, so wie ein komplett neues cmake build system gebaut.
Die Versions Nummer wurde in dem Zug auf 0.1.2 erhöht.

Des weiteren gibt es nun eine mehr oder weniger ausführliche [Doxygen Dokumentation][doxygen].

[![Screenshot SDL2 OpenRaider][screen4small]][screen4]

Das ist ja alles schön und gut, allerdings ist ein Großteil des Codes ein ganz schönes durcheinander. Hier sieht man vermutlich auch schön die Auswirkungen von [BitRot][bitrot].

Darum habe ich einen mehr oder weniger kompletten rewrite begonnen. Der GUI-spezifische Code sollte nun eigentlich komplett sein, als nächstes steht das Portieren des alten Engine-Codes an.

Ich denke allerdings, die neue GUI lässt sich sehen. Das Hauptmenü unterstützt rudimentäre Maus-Steuerung und die Konsole hat eine scrollbare output-history. Sowohl Menü als auch Konsole legen sich als halb-transparentes Overlay über die Spielwelt.

[![Screenshot 1 New OpenRaider][screen5small]][screen5]
[![Screenshot 2 New OpenRaider][screen6small]][screen6]

Der rewrite befindet sich, at the time of this writing, in der [restructure][branch]-Branch.

Ich idle auch die meiste Zeit im IRC-Channel `#OpenRaider` auf freenode. Einen [Webchat][webchat] gibts dafür ebenfalls.

Interesse geweckt? Meine cmake Scripts bauen auf Mac OS X zwar ein wunderhübsches App Bundle, sind aber auf Linux komplett ungetestet. Vielleicht könnte sich jemand die Zeit nehmen, dafür zu sorgen, dass auch dort alles kompiliert?

Im Prinzip spricht auch nichts dagegen OpenRaider auf Windows zu kompilieren. Da bin ich allerdings so wie so komplett überfragt, das ist nicht mein Fachgebiet... :)

Also, bitte schickt Pull-Requests mit Verbesserungen auf [GitHub][github]. Danke!

[![Screenshot Time Tracking][screen1small]][screen1]

Der Time Tracking Screenshot kommt übrigens aus der ganz tollen Mac App [Timing][timing].

 [screen1small]: img/openraider_tracking_small.png
 [screen1]: img/openraider_tracking.png
 [timing]: http://timingapp.com
 [openraider]: http://openraider.sourceforge.net
 [github]: https://github.com/xythobuz/OpenRaider/
 [zaphod]: http://xythobuz.de/git/openraider/
 [screen2small]: img/openraider_old_small.png
 [screen2]: img/openraider_old.png
 [screen3small]: img/openraider_old2_small.png
 [screen3]: img/openraider_old2.png
 [doxygen]: http://xythobuz.github.io/OpenRaider/
 [screen4small]: img/openraider_sdl2_small.png
 [screen4]: img/openraider_sdl2.png
 [bitrot]: http://en.wikipedia.org/wiki/Software_rot
 [screen5small]: img/openraider_new_small.png
 [screen5]: img/openraider_new.png
 [screen6small]: img/openraider_new2_small.png
 [screen6]: img/openraider_new2.png
 [webchat]: http://webchat.freenode.net/?channels=%23OpenRaider
 [branch]: https://github.com/xythobuz/OpenRaider/tree/restructure
