title: RC Equipment
description: My gear and the modifications I did to it
parent: quadcopters
position: 80
date: 2015-10-09
update: 2022-05-23
---

<!--% backToParent() %-->

Over the years of flying quadcopters and other stuff I have grown quite the collection of self-made or customized gear.

## Spectator Monitor

When out flying alone or with a partner, often people walk their dogs nearby or families go on a walk together and see us.
This often sparks a conversation.
For these occasions, it turned out to be very useful to have some kind of second screen and receiver with me.

A friend of mine even has a spare cheap set of FPV goggles with him most of the time.

I decided to go a slightly different route.
For my first experiments, I bought the [Quanum DIY FPV Goggle Set](https://hobbyking.com/de_de/quanum-diy-fpv-goggle-set-with-monitor-kit.html).
I didn't really like the box-style of goggles, so I quickly took the monitor from the set and used it stand-alone.

After I switched to proper FatShark goggles, I used the Quanum monitor again, this time for a spectator monitor.

I built a simple wooden box out of left-over parts and hot-glue, with a large cut-out in the front for the monitor.

Inside is not only a [FR632 Diversity Rx](https://hobbyking.com/en_us/fr632-diversity-5-8ghz-48ch-auto-scan-lcd-a-v-fpv-receiver.html) but also an [Eachine ProDVR](https://www.banggood.com/Eachine-ProDVR-Pro-DVR-Video-Audio-Mini-Recorder-for-FPV-Multicopters-for-RC-Drone-FPV-Racing-p-1061196.html?cur_warehouse=CN), 2x 18650 cells, voltage regulators, a fan and a voltmeter.
The channel can be selected on the receiver, with cut-outs on the back.
The DVR can be controlled using external push buttons.
A power switch, as well as a switch to select either the Rx video feed or the DVR video feed, are on the top.

The batteries hold up for maybe 3 sessions with spectators.
I had to add the fan after the first tests because it simply got too hot inside the box and the first DVR died after a while.

The quality of the Quanum monitor is great and it does not switch to a blue-screen when the signal is fading.
The DVR does not work 100% reliable, but considering my FatShark Dominator v3 has a built-in DVR as well, I'm not really dependant on it.

<!--%
lightgallery([
    [ "img/fpv_spectator_screen_1.jpg", "Top view of spectator monitor" ],
    [ "img/fpv_spectator_screen_2.jpg", "Front view of spectator monitor" ],
    [ "img/fpv_spectator_screen_3.jpg", "Charging side view of spectator monitor" ],
    [ "img/fpv_spectator_screen_4.jpg", "Back view of spectator monitor" ],
    [ "img/fpv_spectator_screen_5.jpg", "Fan side view of spectator monitor" ],
    [ "img/fpv_spectator_screen_6.jpg", "Bottom view of spectator monitor" ]
])
%-->

## Customized Transmitter

Many years ago, a long time before I even started getting into Quadcopters, my grandpa bought me a cheap 2.4GHz Transmitter from Conrad Elektronik.
Because this was already available when I started building my own copters, I used it for that as well.
Turns out, it is a Flysky-clone, with it's own shoddy PC software.
So I wrote [my own Mac driver for it](2015_12_20_serialgamepad.html).
After using it with its original receiver for a while, I decided to move into the FrSky ecosystem.
So I swapped out the built-in transmitter for a [FrSky DHT](https://www.frsky-rc.com/product/dht-toggle-switch-2/) with the [TTL mod](http://majek.mamy.to/en/frsky-dht-ttl-mod/) to connect [my own telemetry display](2016_11_05_frsky_telemetry.html).

Also see [the article about my Saitek X52 USB joystick experiments](2016_07_24_usb_host_cppm.html).

<!--%
lightgallery([
    [ "img/arduino_frsky_telemetry_2.jpg", "Arduino FrSky Telemetry Photo 1" ],
    [ "img/arduino_frsky_telemetry_3.jpg", "Arduino FrSky Telemetry Photo 2" ],
    [ "img/arduino_frsky_telemetry_4.jpg", "Arduino FrSky Telemetry Photo 3" ],
    [ "img/flysky4.jpg", "MP-26-DT back" ],
    [ "img/flysky5.jpg", "MP-26-DT mod" ],
    [ "img/flysky6.jpg", "MP-26-DT mod near" ],
    [ "img/saitek8.jpg", "Modified RC Transmitter" ],
    [ "img/saitek1.jpg", "Saitek X52 Whole Setup" ]
])
%-->

## Ammo Can Battery Charging

Having so many high-capacity LiPo batteries around because of this hobby is kinda scary of course, after looking at a bunch of battery fires on YouTube.
So I at least wanted to have some kind of fire-proof enclosure for charging my batteries in.
I decided to go the common ammo-can route for this.

When doing this, it is **very important** to modify the can so it no longer is pressure-tight.
Otherwise you're building something more like a bomb.
Many people remove the seal in the lid for this, but I decided to drill a couple of large holes into the can, as well as a rectangular cutout for the charging cables.

The holes have a piece of mesh glued in front of them, to keep debris out.
And the inner walls of the can have been padded with cardboard, to prevent any chance of short-circuiting on the metal sheet of the can.

<!--%
lightgallery([
    [ "img/ammo_charger_1.jpg", "Front of can, with IMAX B5 charger clone" ],
    [ "img/ammo_charger_2.jpg", "Inside of can" ],
    [ "img/ammo_charger_3.jpg", "Side of can" ],
])
%-->

<!--%
## FPV Monitor

# TODO photos
%-->

## Spectator Monitor 2



<!--%
# TODO photos
%-->

The files for the modified 3D printed case [can be found on my Thingiverse profile](https://www.thingiverse.com/thing:2003324).
