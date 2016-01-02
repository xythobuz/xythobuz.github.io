title: 8x8x8 LED Cube
title_de: 8x8x8 LED Wuerfel
description: AVR LED Cube with Java Software and Music Visualization
parent: projects
position: 10
comments: true
flattr: true
github: https://github.com/xythobuz/LED-Cube
compat: cube
---

# {{ page.title }}

Get the [current Codebase as Zip][1].

<iframe width="640" height="360" src="//www.youtube.com/embed/czxCxTBSgHM" frameborder="0" allowfullscreen></iframe>
[`Youtube Link`](http://www.youtube.com/watch?v=czxCxTBSgHM)

My friends Max (<hutattedonmyarm@me.com>) and Felix built this single-color 8x8x8 LED Cube with me. On this page, you can get the Software as well as Schematics and the PCB Layout licensed under the GPLv3. Have fun!

<div class="yoxview">
    <a href="img/cube14.jpg" class="thumbnail">
        <img src="img/cube14_small.jpg" alt="Photo" title="Prototype Cube">
    </a>
    <a href="img/cube11.jpg" class="thumbnail">
        <img src="img/cube11_small.jpg" alt="Photo" title="PCB Soldering">
    </a>
</div>

## Hardware

**Warning:** Frank mailed me and explained that the FRAM is operating outside of it's absolute maximum ratings. It should get 3.3V, not 5V. I'll probably update the board and schematic, soon. It seems to work, regardless. **Beware!**

An AtMega32 controls 8 8bit Latches. These 64 bits control, via a PNP Transistor, the anodes of 8 LEDs, each.

There are also 8 N-Channel MOSFETs connected to the AtMega32. They each control the cathodes of 64 LEDs on a Y-Plane.

It can talk to a PC via USB with a FT232RL. A 1Mbit FRAM is accessed over TWI (or I2C).

There's also an AtMega8 which acts as a TWI Slave and sends audio data to the AtMega32. This data comes from a MSGEQ7.

An extensive part list can be found in the Github repository, in Hardware, called parts.txt.

<div class="yoxview">
    <a href="img/cube10.jpg" class="thumbnail">
        <img src="img/cube10_small.jpg" alt="Photo" title="Prototype in Action">
    </a>
    <a href="img/cube12.jpg" class="thumbnail">
        <img src="img/cube12_small.jpg" alt="Photo" title="PCB in Action">
    </a>
</div>

## Software

The software is composed of 3 parts. The CubeFirmware for the AtMega32, the AudioFirmware for the AtMega8 and CubeControl, the PC software.

### CubeFirmware

It's main work is to load images from the FRAM or the AtMega8 and display it. It also monitors the serial Port and reacts accordingly.

<div class="yoxview">
    <a href="img/kuehler1.jpg" class="thumbnail">
        <img src="img/kuehler1_small.jpg" alt="Photo" title="Voltage Regulator Mount">
    </a>
    <a href="img/kuehler2.jpg" class="thumbnail">
        <img src="img/kuehler2_small.jpg" alt="Photo" title="Voltage Regulator Mount">
    </a>
</div>

### AudioFirmware

It gets data from the MSGEQ7 and sends it via TWI.

### CubeControl

Depends on [Java3D][10]. It renders a rotatable 3D View of the cube. You can then create animations, load and save them, and upload them to the Cube. It has it's own C Library for Windows and Unix to talk to the serial port.

<div class="yoxview">
    <a href="img/cubecontrol.png" class="thumbnail">
        <img src="img/cubecontrol_small.png" alt="Photo" title="Screenshot">
    </a>
    <a href="img/cubeschem.png" class="thumbnail">
        <img src="img/cubeschem_small.png" alt="Photo" title="Schematic">
    </a>
</div>

### Hardware Emulator

Allows you to test CubeControl without a real Cube. Unix only!

### UploadTest

Small CLI tool to send testdata or stored animations from CubeControl. Unix only!

## Download

Get the whole code, as well as schematics and the PCB layout as PNG and Eagle files, from the [GitHub Repository][15].

<div class="yoxview">
    <a href="img/cube13.jpg" class="thumbnail">
        <img src="img/cube13_small.jpg" alt="Photo" title="PCB">
    </a>
    <a href="img/cube15.jpg" class="thumbnail">
        <img src="img/cube15_small.jpg" alt="Photo" title="Final Cube">
    </a>
</div>

Frank built this Cube, slightly improved the code and made a Slow-Motion movie. You can see the Multiplexing very nice:

<iframe width="640" height="480" src="//www.youtube.com/embed/fezxkVmkyYw" frameborder="0" allowfullscreen></iframe>
[`Youtube Link`](http://www.youtube.com/watch?v=fezxkVmkyYw)

 [1]: https://github.com/xythobuz/LED-Cube/zipball/master
 [10]: http://www.oracle.com/technetwork/java/javase/tech/index-jsp-138252.html
 [15]: https://github.com/xythobuz/LED-Cube

lang: de

# {{ page.title_de }}

Downloade die [aktuelle Codebase als Zip][1].

<iframe width="640" height="360" src="//www.youtube.com/embed/czxCxTBSgHM" frameborder="0" allowfullscreen></iframe>
[`Youtube Direktlink`](http://www.youtube.com/watch?v=czxCxTBSgHM)

Als Schulprojekt und für den Explore-IT Wettbewerb von SAP in Markdorf haben meine zwei Teamkollegen, Max <hutattedonmyarm@me.com> und Felix, zusammen mit mir diesen einfarbigen 8x8x8 LED Cube gebaut. Für Interessierte hier alle Software sowie Schaltplan und Boardlayout unter der GPLv3. Viel Freude damit.

<div class="yoxview">
    <a href="img/cube14.jpg" class="thumbnail">
        <img src="img/cube14_small.jpg" alt="Photo" title="Prototyp Cube">
    </a>
    <a href="img/cube11.jpg" class="thumbnail">
        <img src="img/cube11_small.jpg" alt="Photo" title="Platine löten">
    </a>
</div>

## Hardware

**Achtung:** Frank hat mir gemailt und erklärt, dass das FRAM außerhalb der Spezifikation betrieben wird. Es sollte 3,3V statt 5V bekommen. Ich werde vermutlich bald Schaltplan und Layout updaten. Es scheint aber auch so zu funktionieren. **Vorsicht!**

Ein AtMega32 steuert über einen 8bit Bus 8 Latches. Diese 64 bit steuern über je einen PNP Transistor die Anoden von jeweils 8 übereinander liegenden LEDs.

Des weiteren steuert der Prozessor 8 N-Kanal MOSFETs welche die Kathoden von 64 in einer x-z Ebene liegenden LEDs steuern.

Ausserdem kommuniziert der AtMega32 über einen FT232RL per USB mit einem PC. Über den TWI (I2C) Bus wird auf ein 1MBit FRAM zugegriffen.

Zusätzlich ist ein AtMega8 auf der Platine. Dieser liest über einen MSGEQ7 ein Audiosignal und sendet dieses über TWI an den AtMega32.

Eine ausführlichere Bauteilliste findet sich im Github Repository, im Ordner Hardware als parts.txt.

<div class="yoxview">
    <a href="img/cube10.jpg" class="thumbnail">
        <img src="img/cube10_small.jpg" alt="Photo" title="Prototyp in Aktion">
    </a>
    <a href="img/cube12.jpg" class="thumbnail">
        <img src="img/cube12_small.jpg" alt="Photo" title="Platine in Aktion">
    </a>
</div>

## Software

Die Software besteht aus 3 großen Teilen, die CubeFirmware für den AtMega32, die AudioFirmware für den AtMega8 und CubeControl. Letzteres ist eine Plattformunabhängige Java Software, welche es erlaubt, Animationen für den LED Cube zu erstellen und diese an den Cube zu übertragen. Hierfür wird Java3D benötigt.

### Cube Firmware

Die Hauptaufgabe der CubeFirmware ist es, Animationen aus dem FRAM zu laden und anzuzeigen. Nebenbei wird auf Anfragen per USB gewartet und entsprechend gehandelt. Auf Knopfdruck steuert die CubeFirmware den AtMega8 an, um Audio Daten zu visualisieren.

<div class="yoxview">
    <a href="img/kuehler1.jpg" class="thumbnail">
        <img src="img/kuehler1_small.jpg" alt="Photo" title="Kühlkörper Spannungsregler">
    </a>
    <a href="img/kuehler2.jpg" class="thumbnail">
        <img src="img/kuehler2_small.jpg" alt="Photo" title="Kühlkörper Spannungsregler">
    </a>
</div>

### Audio Firmware

Die AudioFirmware liest den MSGEQ7 aus, um bei entsprechender Anfrage über TWI diese Daten zu übertragen.

### CubeControl

Neben einigen Java Klassen um einen 3D LED Würfel darzustellen und mit diesem zu interagieren, besteht CubeControl auch aus einer Java Native Interface (JNI) Library, welche sowohl unter Windows als auch unter Unix die serielle Kommunikation für CubeControl ermöglicht. Für die 3D Darstellung wird [Java3D][10] benötigt. In der OS X Lion Variante von Java ist dies bereits enthalten, für Windows und Linux muss es separat heruntergeladen werden.

<div class="yoxview">
    <a href="img/cubecontrol.png" class="thumbnail">
        <img src="img/cubecontrol_small.png" alt="Photo" title="Screenshot">
    </a>
    <a href="img/cubeschem.png" class="thumbnail">
        <img src="img/cubeschem_small.png" alt="Photo" title="Schaltplan">
    </a>
</div>

### Hardware Emulator

Ein kleines Projekt, welches unter Unix ein Pseudo Terminal öffnet und die Cube Hardware emuliert. Kann zum testen von CubeControl genutzt werden.

### UploadTest

Ein kleines CLI Tool um Testdaten und mit CubeControl gespeicherte Animationen an den Cube zu senden.

## Download

Im [GitHub Repository][15] findet sich der gesamte Code sowie die Eagle Dateien und Schaltplan und Layout als PNGs.

<div class="yoxview">
    <a href="img/cube13.jpg" class="thumbnail">
        <img src="img/cube13_small.jpg" alt="Photo" title="Platine">
    </a>
    <a href="img/cube15.jpg" class="thumbnail">
        <img src="img/cube15_small.jpg" alt="Photo" title="Fertiger Cube">
    </a>
</div>

Frank hat den Cube nachgebaut, den Code etwas verbessert und dieses Slow-Motion Video gemacht. Man kann sehr schön das Multiplexing verfolgen:

<iframe width="640" height="480" src="//www.youtube.com/embed/fezxkVmkyYw" frameborder="0" allowfullscreen></iframe>
[`Youtube Direktlink`](http://www.youtube.com/watch?v=fezxkVmkyYw)

 [1]: https://github.com/xythobuz/LED-Cube/zipball/master
 [10]: http://www.oracle.com/technetwork/java/javase/tech/index-jsp-138252.html
 [15]: https://github.com/xythobuz/LED-Cube
