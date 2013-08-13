title: AVR Serial Library
title_de: AVR Serial Library
description: Hardware UART library for many AVR MCUs
parent: software
position: 1
comments: true
flattr: true
github: https://github.com/xythobuz/avrSerial
compat: avrserlib
twitter: xythobuz
reddit: true
print: true
---

### {{ page.title }}

The avrSerial Library enables interrupt-driven UART communication on all available UART modules. Each module has it's own receive and transmit buffer. XON/XOFF Flow Control for the receiving end can be enabled. At the moment, the following AtMega types are supported:

    AtMega8
    AtMega16
    AtMega32
    AtMega8515
    AtMega8535
    AtMega323
    AtMega2560
    AtMega2561
    AtMega1280
    AtMega1281
    AtMega640
    AtMega168

To add another processor, just get the register names from the data sheet and put them in the header file.

[Code on GitHub][1]

[Doxygen Documentation (HTML)][2]

[Doxygen Documentation (PDF)][3]

 [1]: https://github.com/xythobuz/avrSerial
 [2]: http://www.xythobuz.org/avrserial/
 [3]: http://www.xythobuz.org/avrserial.pdf

lang: de

### {{ page.title_de }}

Die avrSerial Library ermöglicht Interruptgesteuerte UART kommunikation mit allen verfügbaren UART Modulen. Jedes Modul hat einen eigenen Sende- und Empfangspuffer. XON/XOFF Flow Control kann auf Empfangsseite aktiviert werden. Unterstützt werden momentan folgende AtMega Typen:

    AtMega8
    AtMega16
    AtMega32
    AtMega8515
    AtMega8535
    AtMega323
    AtMega2560
    AtMega2561
    AtMega1280
    AtMega1281
    AtMega640
    AtMega168

Es können jedoch problemlos weitere Prozessoren hinzugefügt werden. Dafür müssen nur die Registernamen aus dem Datenblatt in die Header Datei eingefügt werden.

[Code auf GitHub][1]

[Doxygen Dokumentation (HTML)][2]

[Doxygen Dokumentation (PDF)][3]

 [1]: https://github.com/xythobuz/avrSerial
 [2]: http://www.xythobuz.org/avrserial/
 [3]: http://www.xythobuz.org/avrserial.pdf