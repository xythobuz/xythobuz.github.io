title: Gieß-o-mat
description: DIY fertilizer mixer and plant watering machine
parent: projects
position: 6
github: https://git.xythobuz.de/thomas/giess-o-mat
date: 2021-03-29
update: 2021-05-01
---

Since moving into my own flat in 2019 I started growing quite a bunch of plants.
It started with carnivorous plants and some decorative stuff on the balcony (also good for the insects!).
Last year some herbs like basil were added.
And this year I also have quite a selection of different Paprika/Chili strains growing, as well as some Tobacco.

So it seemed natural to build a machine that can help me with watering the plants and mixing in some fertilizer solution into the water once in a while.

<!--%
lightgallery([
    [ "img/giessomat_1.jpg", "Front of the UI unit" ],
    [ "img/giessomat_3.jpg", "Side view of the machine" ],
    [ "https://www.youtube.com/watch?v=q-sjvPYs-EQ", "img/giessomat_thumbnail_small.png", "Demo Video" ]
])
%-->

## Overview

The machine consists of a 5l watertank.
A solenoid valve controls the mains-water-line inlet to the tank.
Small amounts of fertilizer mixture can be added to the tank using peristaltic pumps.
The whole system is mounted high-up on the top of my plant shelf.
That way, gravity is feeding the water from the tank to the outlets, controlled by more solenoid valves.
Of course, the outlet valves can also be replaced by pumps, so everything can be mounted level, or the machine below the plants.

Even though the software uses float-switches to measure the fill-height in the tank, maximum safety timeouts are implemented for every action, so the chances of flooding the house are minimized.
Still, I always manually close the mains-water-inlet with a proper hand-controlled valve after using the machine and open it only when needed, just in case!

(I'm a software developer by trade, so I'm relatively confident the software works, but I don't trust my plumbing skills too much...) 😊

<!--%
lightgallery([
    [ "img/giessomat_web.png", "Screenshot of the web interface" ]
])
%-->

The web interface is using JS and Websockets to dynamically update the page, showing the same output that is visible on the physical display.
Keypad button presses can be executed that way as well.
Also, the debug logs that are normally provided on the serial port are also sent out to clients connected via the web interface.

## Implementation

The machine is using two microcontrollers, an [Arduino Nano clone](https://amzn.to/3sQ4Otl) and an [ESP32](https://amzn.to/3xmDh6k).

The Arduino provides the user interface, using a 20x4 LCD from a now-obsolete Sparkfun project called [SerialLCD](https://www.sparkfun.com/products/retired/9568).
It is connected to the Arduino via serial.
Input is done using a cheap 3x4 Keymatrix directly conencted to the Arduino GPIOs.
I also added a power switch and some voltmeters for the different voltage regulators and a main power switch.
All this is mounted in a simple 3D-printed frontpanel.

<!--%
lightgallery([
    [ "img/giessomat_2.jpg", "Back of the UI unit" ],
    [ "img/giessomat_6.jpg", "Front of UI PCB" ],
    [ "img/giessomat_7.jpg", "Back of UI PCB" ]
])
%-->

The actual control is done on an ESP32 which is connected to two [4-channel relais boards](https://amzn.to/2QW0Sty).
Using these, it controls five valves (one inlet and four outlets) as well as three pumps for the fertilizers.
For the outlet valves I'm using cheap small chinese solenoid valves.
For the inlet, I'm using a more expensive metal solenoid valve from Germany that is able to resist the mains-water-pressure (up to 8bar) that I still had from my cocktail machine experiments.
Two float switches are used to tell the fill-height of the water tank.
The ESP32 also provides a simple web interface to allow the same controls as from the user interface.

<!--%
lightgallery([
    [ "img/giessomat_4.jpg", "Top view of the machine" ],
    [ "img/giessomat_14.jpg", "Front of controller PCB" ],
    [ "img/giessomat_15.jpg", "Back of controller PCB" ]
])
%-->

Both UI and controller are connected to each other using I2C.
All relevant signals are transmitted with a simple DB-9 cable.

All this is mounted on an old piece of shelf-board, using some custom designed 3D printed parts.
The water tank is realized using a generic 5l liquid tank, with two holes drilled for the fill switches. The holders for the fertilizer bottles, as well as the bottlecaps, are specifically designed to fit my 1l fertilizer bottles.

I designed all the 3D printed parts with OpenSCAD.
You can find [the files](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/giessomat) on my Gitea.

<!--%
lightgallery([
    [ "img/giessomat_3d_2.png", "User Interface" ],
    [ "img/giessomat_3d_1.png", "Bottlecap for Fertilizer" ],
    [ "img/giessomat_3d_3.png", "Fertilizer bottle mount" ],
    [ "img/giessomat_3d_9.png", "Watertank holder" ],
    [ "img/giessomat_3d_4.png", "Hose sieve/filter" ],
    [ "img/giessomat_3d_5.png", "Hose fix for pumps" ],
    [ "img/giessomat_3d_6.png", "Light-proofing for hose hole" ],
    [ "img/giessomat_3d_7.png", "Large valve mount" ],
    [ "img/giessomat_3d_8.png", "Small valve mount" ]
])
%-->

Most of the parts I had lying around in the workshop.
I only had to buy the outlet valves after realizing one of the big valves I still had was no longer working.
Also the pumps, hoses and hose-adapters had to be bought.

<!--%
lightgallery([
    [ "img/giessomat_8.jpg", "Front of switch PCB" ],
    [ "img/giessomat_9.jpg", "Back of switch PCB" ],
    [ "img/giessomat_16.jpg", "Front of valve PCB" ],
    [ "img/giessomat_17.jpg", "Back of valve PCB" ],
    [ "img/giessomat_5.jpg", "Float switch and valve used" ],
    [ "img/giessomat_12.jpg", "Front of pump" ],
    [ "img/giessomat_13.jpg", "Back of pump" ]
])
%-->

The software can easily be configured to run with more or less fertilizers and outlets, as much as the ESP32 GPIOs can provide.
Alternatively, you can also use an Arduino for the controller instead of the ESP, losing the web interface.
Or you can also compile the software to run both UI and control on one Arduino, as long as it has enough GPIOs for your needs (or an ESP, but I haven't tested that).
You can of course also just leave out the UI and use solely the web interface on the ESP. See the [README.md of the project](https://git.xythobuz.de/thomas/giess-o-mat/src/branch/master/README.md) for more details.

Doing some programming, it would also be possible to use some kind of port-extender or run also the UI on an ESP.
And of course also the now-obsolete SerialLCD could be replaced with something different without too much work.

<!--%
lightgallery([
    [ "img/giessomat_10.jpg", "Interconnect PCB and debug power switch, front side" ],
    [ "img/giessomat_11.jpg", "Interconnect PCB and debug power switch, back side" ]
])
%-->

## Future Extensions

I have now been running capacitive ground moisture level sensors in a couple of my plants for around a year, logging the data using my [ESP-Env project](https://git.xythobuz.de/thomas/esp-env) to an [InfluxDB](https://www.influxdata.com/) instance running on my NAS, with a [Grafana](https://grafana.com/) UI running on there as well.
I used the [cheap chinese models](https://amzn.to/3sLG8SB) up to now, and they have not proven very useful.
They of course don't corrode as fast as the resistive-measurement-based sensors, but they still age because of the permanent water contact.
I tried to work-around that by using [Plastik70](http://www.kontaktchemie.com/koc/KOCproductdetail.csp?division=&product=PLASTIK%2070&ilang=en&plang=en) in liberal amounts with multiple coatings on the sensor, but even with that they show quite considerable drift over a couple of months.
The data is good enough to see when I watered the plants, but it is difficult to determine a value where automatic watering should occur.
Because of that, I have not yet added completely automated watering into the system.
It still has to be started manually via the user interface.

<!--%
lightgallery([
    [ "img/giessomat_grafana_1.png", "Data of new sensors" ],
    [ "img/giessomat_grafana_2.png", "Data after about half a year" ]
])
%-->

If you look closely you can also see some glitches in the data where my ESP had problems and did not store new values.
Also consider that in the timeframes seen in the graph above, I always watered the plants manually as soon as the soil felt dry about 3cm deep.

But recently I got a different sensor from a colleague of mine, which is from another project called [Giesomat](https://www.ramser-elektro.at/shop/bausaetze-und-platinen/giesomat-kapazitiver-bodenfeuchtesensor-erdfeuchtesensor-mit-beschichtung/).
The similar name was totally incidental, I only heard of it after naming my own project like this.
I will test it and report the results here sometime in the future.

Also, it would of course be possible to design a custom PCB for the hardware.
But to be quite honest, I don't see the appeal in that currently.
It would lose the ability to use a different number of pumps and valves, as needed by the specific application.
And building all this up on perf-boards is really not much work.

## Links

You can find [all the source code for the device itself](https://git.xythobuz.de/thomas/giess-o-mat) (both the UI and the Controller) as well as the OpenSCAD [design files for the 3D printed parts](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/giessomat) on my [Gitea instance](https://git.xythobuz.de).

## License

Giess-o-mat is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

    Copyright (c) 2021 Thomas Buck <thomas@xythobuz.de>

    Giess-o-mat is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Giess-o-mat is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Giess-o-mat.  If not, see <https://www.gnu.org/licenses/>.
