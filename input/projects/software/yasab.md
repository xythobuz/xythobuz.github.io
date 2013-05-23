title: YASAB AVR Bootloader
title_de: YASAB AVR Bootloader
description: Yet another simple AVR Bootloader with Upload Software for Unix and Android.
parent: software
position: 6
comments: true
flattr: true
github: https://github.com/xythobuz/yasab
compat: yasab
twitter: xythobuz
reddit: true
print: true
---

# YASAB - Yet another simple AVR Bootloader

YASAB is a simple AVR Bootloader, written in C for the [AVR libc][1]. A PC Program sends the data to be programmed with a simple protocol via UART to the AVR. If the bootloader was compiled for the ATmega168, 128x or 256x, it will listen on both USART0 and USART1 for serial communication attempts. [The most recent source code can be found in the Github Repository][2]. The Upload software can easily be used in place of avrdude in makefiles.

Another YASAB compatible Uploader implementation is in my [xyCopter Android App][3], using [Bluetooth][4].

<pre>
yasab /dev/tty.usbserial-A100QOUE test.hex q
Hex File Path   : test.hex
Minimum Address : 0x0
Maximum Address : 0x61E2
Data payload    : 25068 bytes

Pinging bootloader... Stop with CTRL+C
Got response... Acknowledging...
Connection established successfully!
Sending target address...
Sending data length...
100% (25068 / 25068) 195 page(s) written!

Upload finished after 28.0 seconds.
</pre>

[![xyCopter Screenshot][5]][6]

 [1]: http://www.nongnu.org/avr-libc/
 [2]: https://github.com/xythobuz/yasab
 [3]: https://github.com/xythobuz/xyControl/tree/master/tools/xyCopter
 [4]: bluetooth.html
 [5]: img/xyCopterFirmware_small.png
 [6]: img/xyCopterFirmware.png

lang: de

# YASAB - Yet another simple AVR Bootloader

YASAB ist ein einfacher AVR Bootloader, geschrieben in C für die [AVR libc][1]. Von einem PC-Programm aus werden die Daten über ein simples Protokoll per UART an den AVR gesendet. Wurde der Bootloader für den ATmega168, 128x oder 256x kompiliert, wird sowohl auf USART0 als auch auf USART1 Daten erwartet. [Der aktuellste Quellcode findet sich stets im Github Repository][2]. Die Upload Software kann einfach statt avrdude oder ähnlichem in makefiles eingebaut werden.

Außerdem implementiert meine [Android App xyCopter][3] einen YASAB kompatiblen Uploader über [Bluetooth][4].

<pre>
yasab /dev/tty.usbserial-A100QOUE test.hex q
Hex File Path   : test.hex
Minimum Address : 0x0
Maximum Address : 0x61E2
Data payload    : 25068 bytes

Pinging bootloader... Stop with CTRL+C
Got response... Acknowledging...
Connection established successfully!
Sending target address...
Sending data length...
100% (25068 / 25068) 195 page(s) written!

Upload finished after 28.0 seconds.
</pre>

[![xyCopter Screenshot][5]][6]

 [1]: http://www.nongnu.org/avr-libc/
 [2]: https://github.com/xythobuz/yasab
 [3]: https://github.com/xythobuz/xyControl/tree/master/tools/xyCopter
 [4]: bluetooth.html
 [5]: img/xyCopterFirmware_small.png
 [6]: img/xyCopterFirmware.png



