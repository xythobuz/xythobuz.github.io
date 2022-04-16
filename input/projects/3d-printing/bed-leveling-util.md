title: Bed Leveling Utility
description: Python wxWidgets Marlin Mesh Bed Leveling helper
parent: 3d-printing
position: 60
comments: true
git: https://git.xythobuz.de/thomas/Bed-Leveling-Utility
github: https://github.com/xythobuz/Bed-Leveling-Utility
date: 2016-06-07
update: 2016-06-12
---

<!--% backToParent() %-->

This is a manual Mesh Bed Leveling GUI utility for 3D printers with Marlin Firmware.

<!--%
lightgallery([
    [ "img/bed_leveling_util.png", "Screenshot of Bed-Leveling-Utility" ],
])
%-->

At the time of me writing this program, Marlin had a bug that caused the manual mesh bed leveling process to not work using the connected LCD display, leaving G-Codes sent over the serial port as the only option.
Because manually inserting these in a terminal program proved to be very tedious, and none of the G-Code senders I've tested had the features I wanted (mainly easily configurable step sizes), I wrote this simple little program.

After starting the program, select the serial port connected to your printer, the correct baudrate for communicating with it and press Connect.
The X, Y and Z value displayed are periodically polled from the printer and are not very accurate.
Zc is what is manipulated using the up- and down-arrow buttons or keys.
The value shown there will be more accurate.

Before starting with the leveling procedure, the current Mesh info has to be polled from the printer.
This will happen automatically after connecting.
When ready, press Start, then adjust the Z-height for each measuring point and press Next or the right-arrow key to move on.
After you're finished, you should store the new mesh data in the EEPROM using the Save button.

You will need pySerial (>= v3.0) and wxPython for the program to work.

This has been developed and tested on a Mac OS X 10.10.5 machine with Python 2.7 and dependencies installed with MacPorts, connected to a modified Fabrikator Mini V1.5 with Marlin 1.1.0-RC6.

The source code can be found [on my Gitea server](https://git.xythobuz.de/thomas/Bed-Leveling-Utility) as well as [on GitHub](https://github.com/xythobuz/Bed-Leveling-Utility/).
