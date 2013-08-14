title: IB-NAS6210 Linux
title_de: IB-NAS6210 Linux
description: Booting your own Linux on an Icybox NAS6210 box
parent: stuff
position: 20
comments: true
flattr: true
compat: nas
twitter: xythobuz
reddit: true
print: true
---

### {{ page.title }}

1.  root Access (by Jayare)
    *   Install the device like a normal user would
    *   Have at least one user with administrator access (either add one, or use the main account) - in my case this is 'admin' but could be any user with administrator rights
    *   Fire up an SSH connection to box (e.g. putty)
    *   Login with the following details:
    *   [username]\_hipserv2\_raidsonic_[PRODUCTCODE]
    *   so in my case that would be
    *   admin\_hipserv2\_raidsonic_XXXX-XXXX-XXXX-XXXX
    *   It'll echo the ICY BOX version (in my case ICY BOX version 10.0.x) and ask for a password. Enter the regular password for the user.
    *   You'll now be logged in to the ICY BOX with the 'regular' user
    *   sudo -E -s
    *   reenter your regular pwd. It'll give you an 'audit\_log\_user_command(): connection refused' and give you root access
2.  Hardware access (by me, really short version)
    *   This is really long and I'm not in the mood to translate this... Sorry :)
    *   But I saw that googles translator does a really "good" job translating my text...
    *   Try to look at [my article translated to English][1]!

 [1]: http://translate.google.de/translate?sl=de&tl=en&js=n&u=http%3A%2F%2Fwww.xythobuz.de%2Fnas.de.html

lang: de

# {{ page.title_de }}

Diese Anleitung gilt ebenso für den IB-NAS6220. Dieser besitzt 2 HDD Schächte und ein völlig anderes Webinterface. Über dieses ist es möglich, das root Passwort zu ändern (siehe diesen [Forenbeitrag][1]), was evtl. eine Neuinstallation einer Linux Distribution erübrigt.

Der [Icy Box IB-NAS6210][2] (Affiliate Link) hat mit seiner hauseigenen Firmware nur einen beschränkten Funktionsumfang. Es ist kein [AFP][3] oder [DAAP][4] möglich, was als Mac User von großem Nachteil ist. Deshalb muss Linux her, welches auf der verbauten ARM CPU hervorragend läuft. Es ist zwar bereits ein Linux System installiert, leider ist aber der root User nicht zugänglich.

Die Basisplattform des NAS6210 bildet die Kirkwood Plattform, welche auch im [SheevaPlug][5] und im [OpenRD][6] zum Einsatz kommt. Dies erleichtert die Suche nach einer fertigen Linux Distribution.

## Update

Jayare hat mir per E-Mail mitgeteilt, dass er einen Weg gefunden hat, root Zugang zum Installierten Linux System zu bekommen. Dafür folgende Schritte befolgen:

*   Das Gerät normal in Betrieb nehmen.
*   Einen Administrator Account anlegen oder den vorhandenen Haupt Account nutzen. Im folgenden Beispiel lautet der Benutzername admin.
*   Mittels SSH eine Verbindung zum NAS herstellen.
*   Benutzername nach folgendem Schema:
<pre>
[Benutzername]_hipserv2_raidsonic_[Produktcode]
</pre>
*   In unserem Fall:
<pre>
admin_hipserv2_raidsonic_XXXX-XXXX-XXXX-XXXX
</pre>
*   Das Passwort ist das, welches beim erstellen des Benutzers angegeben wurde.
*   Nun hat man eingeschränkte Zugriffsrechte.
*   Der Befehl:
<pre>
sudo -E -s
</pre>
*   Die erneute Eingabe des Passwortes führt zur Ausgabe einer Fehlermeldung.
*   Man hat nun trotzdem root Zugriff.

Dies ähnelt den Methoden, die bei Netgear und Seagate Geräten zum root Zugriff führen. Vielen Dank dafür, Jayare!

## Hardware Modifikation

Um das Starten einer anderen Linux Distribution über USB oder eSata zu ermöglichen, benötigen wir Zugang zum Bootloader [Das U-Boot][7]. Dieser gibt beim Booten Statusmeldungen über den internen Seriellen Port des NAS aus und ermöglicht, den Bootprozess zu unterbrechen. Anschliessend kann ein anderer Kernel und eine passende Ramdisk zum Booten ausgewählt werden. Eine bebilderte Anleitung zum aufspüren des Seriellen Ports findet sich, auf Englisch, [hier][8]. Kurz zusammengefasst müssen die hintere Abdeckung und die hinteren Füße weggeschraubt werden, danach lässt sich die Platine mitsamt der Rückwand heraus schieben. Dabei sollte der Festplattenrahmen vorher entfernt worden sein. Unter dem Lüfter befinden sich einige Steckverbindungen auf der Platine. Davon ist eine 4 polige unbelegt. Dies ist der serielle Anschluss. Er arbeitet mit 3,3V Pegeln. Wenn der Stecker an der oberen linken Ecke sitzt, ist die Belegung wie folgt:

<pre>
(GND) (TX) (RX) (3V3)
</pre>

Ein passender Adapter um den Port an den Computer anzuschliessen ist schnell gemacht. Hierzu habe ich einen FT232R auf meine [DIP Adapterplatine][9] gelötet und wie folgt beschaltet (Klick vergrößert):

[![Schaltplan][10]][11]
[![Fertiger Adapter][12]][13]

## Software

Nun besteht also eine Verbindung zwischen meinem Computer und dem NAS mit 115200bps. Wird letzterer nun gebootet, erscheinen U-Boots Statusmeldungen in meinem Terminal. Früher oder später erscheint ein Countdown. Wird dieser mit dem drücken einer beliebigen Taste unterbrochen, findet man sich in U-Boots Kommandozeile wieder. Hier kann zum Beispiel U-Boots eigenes USB System gestartet werden, damit ein Kernel von einem angeschlossenen USB Stick geladen werden kann. Alternativ kann ein Kernel von einem TFTP Server geladen und gestartet werden. Ausserdem können Umbgebungsvariablen angezeigt, geändert, und im NAND gespeichert werden:

<pre>
printenv
setenv name wert
saveenv
</pre>

Zum Starten eines anderen Kernels muss zunächst die Variable "mainlineLinux" auf "yes" gesetzt werden. Anschliessend ändern wir die "arcNumber" auf "2361". Dies gaukelt dem Debian Linux Kernel ein anderes System vor, da es den NAS6210 nicht kennt und deshalb sonst nicht booten will. Die Originale arcNumber lautet 3104. Nun wird noch "ipaddr" auf die gewünschte NAS IP gesetzt und "serverip" auf die IP des Rechners, der im nächsten Schritt einen TFTP Server startet. Geschrieben werden die Änderungen dann mit saveenv.

<pre>
setenv mainlineLinux yes
setenv arcNumber 2361
setenv ipaddr 192.169.2.107
setenv serverip 192.168.2.101
saveenv
</pre>

Nun wird auf einem Rechner im selben Netzwerk ein TFTP Server gestartet. Ich habe auf meinem Mac [TftpServer][14] verwendet. Dieser muss ein [uImage][15] und eine [uInitrd][16] zur Verfügung stellen. Die verlinkten Dateien sind die des [aktuellen Armel OpenRD Debian Installers][17]. Der Installer wird nun auf dem NAS gebootet:

<pre>
tftpboot 0x01100000 uInitrd
tftpboot 0x00800000 uImage
setenv bootargs console=ttyS0,115200n8 base-installer/initramfs-tools/driver-policy=most
bootm 0x00800000 0x01100000
</pre>

Die Installation kann sowohl auf einem USB-Stick, einem eSATA oder einem internen SATA Laufwerk erfolgen. Ich habe Debian auf einen 8GB USB-Stick installiert. Beim Debian Support gibt es [Hilfe zur Installation][18]. Ist die Installation abgeschlossen, muss U-Boot konfiguriert werden, um sie zu starten. Zuerst die folgenden 2 Zeilen eingeben:

<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootcmd 'setenv bootargs $(bootargs_console); run bootcmd_slk; bootm 0x00800000 0x01100000'
</pre>

Für eine USB-Stick Installation nun folgendes Eingeben:

<pre>
setenv bootcmd_slk 'usb start; ext2load usb 0:1 0x01100000 /uInitrd; ext2load usb 0:1 0x00800000 /uImage'
</pre>

Dieses Kommando funktioniert so nur, wenn /boot auf der ersten, als ext2 formatierten Partition liegt. Ansonsten den Pfad anpassen. Ext3 und 4 werden von U-Boot nicht unterstützt.

Für SATA oder eSATA:

<pre>
setenv bootcmd_slk 'ide reset; ext2load ide 0:1 0x01100000 /uInitrd; ext2load ide 0:1 0x00800000 /uImage'
</pre>

Nun noch ein "saveenv", um das ganze zu speichern. Jetzt reicht "run bootcmd" um die U-Boot Kommandozeile zu verlassen und das neu Installierte Debian zu booten.

## Ein neuer Kernel muss her

Der Standard Kernel von Debian unterstützt den NAS6210 nicht wirklich, weshalb die grüne LED dauernd blinkt und das Gerät nach dem herunterfahren nicht ausgeht. Abhilfe schafft ein selbst kompilierter Linux Kernel mit dem richtigen Patch. Dieser ist auf der oben verlinkten Tutorial Seite zu finden, oder auch [hier][19]. Wer sich die Mühe machen will, kann seinen eigenen Kernel nach [diesem Ausschnitt des Debian Kernel Handbook][20] selbst konfigurieren und kompilieren. Ich habe mir diese Mühe bereits gemacht, und [fertige .deb Pakete erstellt (18MB)][21], welche nur noch mittels diesem Befehl installiert werden müssen:

<pre>
dpkg -i linux-image-3.1.0-rc742_xy42_armel.deb
</pre>

Im /boot Verzeichnis des NAS findet sich nun der neue Kernel als "vmlinuz-3.1.0-rc742" und die neue Ramdisk als "initrd.img-3.1.0-rc742". Diese 2 Dateien müssen nun mittels mkimage in U-Boot Images verwandelt werden:

<pre>
mkimage -A arm -O linux -T kernel -C none -a 0x8000 -n Kernel -d vmlinuz-3.1.0-rc742 uImageN
mkimage -A arm -O linux -T ramdisk -C gzip -a 0x8C800000 -n RamDisk -d initrd.img-3.1.0-rc742 uInitrdN
</pre>

Das erzeugt die Dateien uInitrdN und uImageN, welche gebootet werden müssen. Dazu neu starten und folgendes im U-Boot Prompt eingeben:

<pre>
setenv bootcmd_slk 'usb start; ext2load usb 0:1 0x01100000 /uInitrdN; ext2load usb 0:1 0x00800000 /uImageN'
setenv arcNumber 3104
saveenv
</pre>

Ausserdem wird die arcNumber auf die des NAS6210 gestellt, welche dem neuen Kernel bekannt ist. Falls du nicht auf einen USB-Stick installiert hast, musst du das SATA Kommando von oben entsprechend anpassen.

Das wars! Nun kann beliebige Software installiert werden, um den Server für die eigenen Bedürfnisse anzupassen. Bei mir läuft folgendes:

*   [Netatalk][22]
*   Avahi als Zeroconf Implementation für Netatalk
*   [Apache][23]
*   [MySQL][24]
*   [PHP][25]
*   [forked-daapd][26]
*   [CUPS][27]
*   [Webmin][28]
*   [Transmission für Torrents][29]

## Power Button nutzen

Per E-Mail hat mich Waepu auf seinen Weg aufmerksam gemacht, den Power Button nutzbar zu machen. Dafür muss ein neuer Kernel kompiliert werden. Neben dem oben verlinkten Patch muss folgende kleine Änderung angewendet werden:

<pre class="sh_c">
static unsigned int nas6210_mpp_config[] __initdata = {
  MPP0_NF_IO2,
  MPP1_NF_IO3,
  MPP2_NF_IO4,
  MPP3_NF_IO5,
  MPP4_NF_IO6,
  MPP5_NF_IO7,
  MPP18_NF_IO0,
  MPP19_NF_IO1,

  MPP20_SATA1_ACTn,    /* HD1 LED red */
  MPP21_SATA0_ACTn,    /* HD0 LED red */
  MPP22_GPIO,    /* Power LED red */
  MPP23_GPIO,    /* Power button */

  MPP24_GPIO,    /* Power off device */
  MPP25_GPIO,    /* Power LED green */
  MPP27_GPIO,    /* USB transfer LED */
  MPP28_GPIO,    /* Reset button */
  MPP29_GPIO,    /* USB Copy button */
  0
};
</pre>

Erst wenn im Struct MPP23_GPIO hinzugefügt wird, funktioniert folgendes Bash Script.

<pre class="sh_sh">
#!/bin/sh
echo 23 > /sys/class/gpio/export
while : ; do
  s=`cat /sys/class/gpio/gpio23/value`
  if test "$s" == 0 ; then
    shutdown -h now
    exit 0
  fi
  sleep 1
done
</pre>

Der Button auf MPP23\_GPIO hat eine Art Flip-Flop Funktion. Wenn man den Button für ein paar Sekunden hält, ändert sich der Status von MPP23\_GPIO und bleibt so bis zum Reboot.

Ersetzt man im Kernel MPP20\_SATA1\_ACTn und MPP21\_SATA0\_ACTn durch MPP20\_GPIO und MPP21\_GPIO können per Bash auch die HDD LEDs angesteuert werden. Dann funktioniert jedoch die Anzeige der Festplattenaktivität nicht mehr.

Vielen Dank an Waepu hierfür!

 [1]: http://forum.nas-portal.org/showthread.php?12855-Ib-nas6220-b&p=55718&viewfull=1#post55718
 [2]: http://www.amazon.de/gp/product/B003DODPGG/ref=as_li_qf_sp_asin_tl?ie=UTF8&tag=xythobuzorg-21&linkCode=as2&camp=1638&creative=6742&creativeASIN=B003DODPGG
 [3]: http://de.wikipedia.org/wiki/Apple_Filing_Protocol
 [4]: http://de.wikipedia.org/wiki/Digital_Audio_Access_Protocol
 [5]: http://de.wikipedia.org/wiki/SheevaPlug
 [6]: http://open-rd.org/
 [7]: http://sourceforge.net/projects/u-boot/
 [8]: http://simon.baatz.info/raidsonic-icy-box-ib-nas6210-my-new-sheevaplug/
 [9]: ssop28.de.html
 [10]: img/ft232plansmall.jpg
 [11]: img/ft232plan.jpg
 [12]: img/ft232fertigsmall.jpg
 [13]: img/ft232fertig.jpg
 [14]: http://schimana.net/2008/03/it/tftp-server-fuer-mac-os-x/
 [15]: http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd/uImage
 [16]: http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd/uInitrd
 [17]: http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd/
 [18]: http://www.debian.org/releases/stable/armel/
 [19]: http://simon.baatz.info/downloads/linux-3.1-rc9.nas6210.patch
 [20]: http://kernel-handbook.alioth.debian.org/ch-common-tasks.html
 [21]: files/linuxnas.zip
 [22]: http://netatalk.sourceforge.net/
 [23]: http://httpd.apache.org/
 [24]: http://www.mysql.de/
 [25]: http://www.php.net/
 [26]: https://github.com/jasonmc/forked-daapd
 [27]: http://www.cups.org/
 [28]: http://www.webmin.com/
 [29]: http://www.transmissionbt.com/
