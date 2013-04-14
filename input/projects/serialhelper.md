title: Serial Helper
title_de: Serial Helper
description: Reading and Writing a Serial Port from the Command Line
menu-position: 70
comments: true
flattr: true
github: https://github.com/xythobuz/SerialHelper
compat: serialhelper
twitter: xythobuz
reddit: true
print: true
---

# {{ page.title }}

SerialHelper is a Cross-Platform (Windows, Unix systems) Command Line Utility allowing read and write access to serial ports. Additionally, it can list the available serial ports.

[Github Repository][1]

[Download newest source][2]

[Windows Binary (Version 0.5)][3]

<pre>
SerialHelper for Unix version 0.5
This utility allows you to send or recieve data to and from a serial port.
You can also get a list of available serial ports.
It is meant to be used as a tool to allow programs written in other languages access to serial ports.

Getting a list of serial ports:
  serialHelperUnix -s [SearchTerm]
Default Search Term: "tty" or "tty." on a Mac

Sending data to a serial port:
  serialHelperUnix -t "serial port" "Data to send..."
  serialHelperUnix -tf "serial port" /file/to/send

Recieving data from a serial port:
  serialHelperUnix -r "serial port" length

Terminal Mode (send stdin and recieve to stdout):
  serialHelperUnix -rw port
</pre>

 [1]: https://github.com/xythobuz/SerialHelper
 [2]: https://github.com/xythobuz/SerialHelper/zipball/master
 [3]: files/serialHelperWin-0.5.exe

lang: de

# {{ page.title_de }}

SerialHelper ist ein Cross Plattform (Windows, Unix Systeme) Kommandozeilen Programm welches den Zugriff auf serielle Ports ermöglicht. Ausserdem können vorhandene serielle Ports aufgelistet werden.

[Github Repository][1]

[Download aktuellster Sourcecode][2]

[Windows Binary (Version 0.5)][3]

<pre>
SerialHelper for Unix version 0.5
This utility allows you to send or recieve data to and from a serial port.
You can also get a list of available serial ports.
It is meant to be used as a tool to allow programs written in other languages access to serial ports.

Getting a list of serial ports:
  serialHelperUnix -s [SearchTerm]
Default Search Term: "tty" or "tty." on a Mac

Sending data to a serial port:
  serialHelperUnix -t "serial port" "Data to send..."
  serialHelperUnix -tf "serial port" /file/to/send

Recieving data from a serial port:
  serialHelperUnix -r "serial port" length

Terminal Mode (send stdin and recieve to stdout):
  serialHelperUnix -rw port
</pre>

 [1]: https://github.com/xythobuz/SerialHelper
 [2]: https://github.com/xythobuz/SerialHelper/zipball/master
 [3]: files/serialHelperWin-0.5.exe