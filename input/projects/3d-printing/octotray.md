title: OctoTray
description: Linux PyQt tray application to control OctoPrint
parent: 3d-printing
position: 50
comments: true
github: https://git.xythobuz.de/thomas/OctoTray
date: 2021-05-08
update: 2021-05-13
---

<span class="listdesc">[...back to 3D-Printing overview](3d-printing.html)</span>

To quickly print new stuff on one of my printers, I am using the [OctoPrint](https://octoprint.org) integration of [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer).
Unfortunately, it does not allow me to turn on the printers power supply using the Raspberry Pi.
But it is possible to do that via the [OctoPrint REST API](https://docs.octoprint.org/en/master/api/index.html).
Because of that, I wrote a small tool to trigger the power of my printers that lives in the system tray.
It runs on Linux using the Python Qt5 bindings, but without much work it should be able to run on other platforms with PyQt5 as well.

<!--%
lightgallery([
    [ "img/octotray_3.png", "Screenshot of OctoTray version 0.2" ],
    [ "img/octotray_2.png", "Screenshot of webcam viewer in OctoTray version 0.2" ],
    [ "img/octotray_4.png", "Screenshot of status dialog in OctoTray version 0.2" ],
    [ "img/octotray_1.png", "Screenshot of OctoTray version 0.1" ]
])
%-->

You need to enter the hostnames / IPs and the OctoPrint API keys of your printers at the beginning of the python file in the repo.
The program will automatically detect which method to use to switch the power.
If you are using the [PSU Control OctoPrint Plugin](https://plugins.octoprint.org/plugins/psucontrol/) it will use that to toggle the power.
Otherwise it looks for custom system commands, named "all on" and "all off", as described in the [OctoPrint docs](https://docs.octoprint.org/en/master/configuration/config_yaml.html#system).

To give you an example of the system actions you could use to switch GPIOs from OctoPrint, take a look below at the excerpt of my 'config.yaml' file.

    system:
        actions:
        -   action: all on
            command: gpio -g mode 20 out && gpio -g write 20 0 && gpio -g mode 26 out
                && gpio -g write 26 0
            name: Turn on printer & lights
        -   action: all off
            command: gpio -g write 20 1 && gpio -g mode 20 in && gpio -g write 26 1 &&
                gpio -g mode 26 in
            confirm: You are about to turn off the printer and the lights.
            name: Turn off printer & lights
        -   action: lights on
            command: gpio -g mode 20 out && gpio -g write 20 0
            name: Turn on lights
        -   action: lights off
            command: gpio -g write 20 1 && gpio -g mode 20 in
            name: Turn off lights
        -   action: printer on
            command: gpio -g mode 26 out && gpio -g write 26 0
            name: Turn on printer
        -   action: printer off
            command: gpio -g write 26 1 && gpio -g mode 26 in
            confirm: You are about to turn off the printer.
            name: Turn off printer

You can find the project [on my Gitea server](https://git.xythobuz.de/thomas/OctoTray) or on [GitHub](https://github.com/xythobuz/OctoTray).

I also wrote a bit more about my OctoPrint setups [on this page](octoprint.html).
