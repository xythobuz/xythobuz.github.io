title: Bluetooth UART (BTM-222)
title_de: Bluetooth UART (BTM-222)
description: PCB for the BTM-222 and 5V level converters
parent: xyrobot
position: 0
comments: true
flattr: true
compat: bt
---

### {{ page.title }}

Here's the Layout of a BTM-222 Bluetooth PCB, following the [Roboternetz Guidelines Mini Format][1]. The circuit comes from [Robotfreak][2], but is basically the minimal circuit described in the [datasheet (370kB)][3].

[![PCB Top][4]][5]
[![PCB Bottom][6]][7]
[![Circuit diagram][8]][9]
[![Layout][10]][11]

[Layout and Circuit Diagram as Eagle files (54kB)][12].

<table border="1">
  <tr><th>ID</th><th>Value</th><th>Shop</th></tr>
  <tr><td>R1</td><td>200k Ohm</td><td>-</td></tr>
  <tr><td>R2</td><td>5k Ohm Poti</td><td><a href="http://www.conrad.de/ce/de/product/430722/">Conrad</a></td></tr>
  <tr><td>R3 - R10</td><td>1k Ohm</td><td>-</td></tr>
  <tr><td>Q1 - Q4</td><td>BC547 NPN</td><td><a href="http://www.conrad.de/ce/de/product/155012/">Conrad</a></td></tr>
  <tr><td>IC1</td><td>LM317(LZ)</td><td><a href="http://www.conrad.de/ce/de/product/155585/">Conrad</a></td></tr>
  <tr><td>IC2</td><td>BTM 222</td><td><a href="http://shop.ulrichradig.de/aktive-Bauelemente/Module/Bluetooth-Module-BTM222.html">Ulrich Radig</a></td></tr>
  <tr><td>LED 1+2</td><td>LED 5mm</td><td>-</td></tr>
</table>

Soldering the standard parts should be no problem. You should use a find soldering iron to connect each pin of the BTM-222, one after another. A 31mm long piece of wire can be used as antenna.

### Interfacing the BTM-222

Before using the BTM-222 you have to configure it. You can change the speed, data format, name, PIN and some other things. You have to connect the hardware serial interface of the BTM-222 to a PC and issue the AT-Commands documented in the datasheet. It is very important to use only '\r' as Line-End-Character. Using '\n' or "\r\n" will result in error messages from the module.

 [1]: http://www.rn-wissen.de/index.php/RN-Definitionen
 [2]: http://www.robotfreak.de/blog/mikrocontroller/preiswerte-bluetooth-anbindung/44
 [3]: files/btm222.pdf
 [4]: img/BT_Top_small.jpg
 [5]: img/BT_Top.jpg
 [6]: img/BT_Bot_small.jpg
 [7]: img/BT_Bot.jpg
 [8]: img/bt_plan_small.png
 [9]: img/bt_plan.png
 [10]: img/BT_Layout_small.png
 [11]: img/BT_Layout.png
 [12]: files/bluetooth.zip

lang: de

### {{ page.title_de }}

Hier das Layout einer Adapterplatine für den BTM-222 Bluetooth IC im [Roboternetz Mini Format][1]. Die Schaltung stammt von [Robotfreak][2], entspricht aber im Prinzip der Minimalbeschaltung aus dem [Datenblatt][3].

[![Platine oben][4]][5]
[![Platine unten][6]][7]
[![Schaltplan][8]][9]
[![Layout][10]][11]

[Layout und Schaltplan als Eagle Dateien][12].

<table border="1">
  <tr><th>ID</th><th>Wert</th><th>Shop</th></tr>
  <tr><td>R1</td><td>200k Ohm</td><td>-</td></tr>
  <tr><td>R2</td><td>5k Ohm Poti</td><td><a href="http://www.conrad.de/ce/de/product/430722/">Conrad</a></td></tr>
  <tr><td>R3 - R10</td><td>1k Ohm</td><td>-</td></tr>
  <tr><td>Q1 - Q4</td><td>BC547 NPN</td><td><a href="http://www.conrad.de/ce/de/product/155012/">Conrad</a></td></tr>
  <tr><td>IC1</td><td>LM317(LZ)</td><td><a href="http://www.conrad.de/ce/de/product/155585/">Conrad</a></td></tr>
  <tr><td>IC2</td><td>BTM 222</td><td><a href="http://shop.ulrichradig.de/aktive-Bauelemente/Module/Bluetooth-Module-BTM222.html">Ulrich Radig</a></td></tr>
  <tr><td>LED 1+2</td><td>LED 5mm</td><td>-</td></tr>
</table>

Das löten der Standard-Bauteile sollte kein Problem darstellen. Beim BTM-222 empfiehlt es sich, mit einem feinen Lötkolben jeden Pin einzeln anzulöten. Als Antenne kann ein 3,1cm langer Draht verwendet werden.

### Ansteuerung des BTM-222

Vor der ersten Verwendung muss das BTM-222 Modul konfiguriert werden. Dort werden Geschwindigkeit, Format, Name, PIN und weitere Einstellungen getroffen. Dabei muss das Modul per Hardware-Schnittstelle an einen Computer angeschlossen werden. Nun können die im Datenblatt dokumentierten AT Befehle eingegeben werden. Sehr wichtig hierbei ist, dass das Modul als Zeilenendzeichen nur '\r' erwartet. Wird '\n' oder "\r\n" verwendet quittiert das Modul jegliche Eingabe mit Error.

 [1]: http://www.rn-wissen.de/index.php/RN-Definitionen
 [2]: http://www.robotfreak.de/blog/mikrocontroller/preiswerte-bluetooth-anbindung/44
 [3]: files/btm222.pdf
 [4]: img/BT_Top_small.jpg
 [5]: img/BT_Top.jpg
 [6]: img/BT_Bot_small.jpg
 [7]: img/BT_Bot.jpg
 [8]: img/bt_plan_small.png
 [9]: img/bt_plan.png
 [10]: img/BT_Layout_small.png
 [11]: img/BT_Layout.png
 [12]: files/bluetooth.zip
