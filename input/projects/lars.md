title: LARS - Looping Automated Rhythm Station
description: Loopstation drumkit with hand-made solenoids and RP2040
parent: projects
git: https://git.xythobuz.de/thomas/drumkit
github: https://github.com/xythobuz/lars
date: 2024-03-25
comments: true
---

For the recent birthday party of one of our [DrinkRobotics](drinkrobotics.html) and musician friends, [Kauzerei](https://github.com/kauzerei) had the great idea to build a DIY drummachine as a present, to allow them to play the bass without having to gather a jam session group.
He recruited me for some electronics design brainstorming and to write the firmware.

<!--%
lightgallery([
    [ "img/lars_3.jpg", "LARS drum and controller. © 2024 Kauzerei." ],
    [ "img/lars_7.jpg", "LARS logo" ],
    [ "img/lars_10.jpg", "LARS actually running" ],
])
%-->

It is mainly made out of repurposed old parts from the recycling bin.
The drum body consists of a tambourine with a 3D printed frame attached, with three hand-wound solenoids mounted on there.
The positioning and different hammers create some (slightly) differing sounds.

<!--%
lightgallery([
    [ "img/lars_8.jpg", "Solenoids mounted to frame" ],
    [ "img/lars_4.jpg", "LARS on table. © 2024 Kauzerei." ],
])
%-->

The electronics are made with a Raspberry Pi Pico (or Pico W in this case, although WiFi or BT are not used yet).
This keeps the future option of a USB Midi input open.
The user interface consists of four buttons, each with an LED above, and a clickable rotary encoder, as well as a power switch and an 128x64 SSD1306 OLED display.
To drive the solenoids, three step-up converters create ~16V from the single Li-Ion 18650 cell.
Their output is then switched to the solenoids using MOSFETs.
A small TP4056 module handles recharging the battery.

<!--%
lightgallery([
    [ "img/lars_14.png", "Schematic" ],
    [ "img/lars_11.jpg", "Step up converters" ],
    [ "img/lars_12.jpg", "LED and button for panel mounting" ],
])
%-->

All of this is mounted on a custom hand-etched PCB.

<!--%
lightgallery([
    [ "img/lars_15.png", "PCB layout" ],
    [ "img/lars_13.jpg", "PCB with photoresist, before etching" ],
    [ "img/lars_9.jpg", "Side view of case/pcb sandwich" ],
])
%-->

We only came three hours late to the birthday party due to finishing the LARS hardware, and I spent some more time at the party putting some final work into the firmware.
It actually was functionally usable on the party evening, even before everyone was too drunk to care 🥴

<!--%
lightgallery([
    [ "img/lars_16.png", "PCB 3D render back" ],
    [ "img/lars_17.png", "PCB 3D render front" ],
])
%-->

Unfortunately there was no time yet to take good pictures or a video of LARS in action.

As usual all 3D print files, PCB layout design and firmware source code is [available in the repo](https://git.xythobuz.de/thomas/drumkit).
You can also order the PCB pre-fabricated from an online supplier, the repo includes a script to generate the gerber files.

The software is not quite finished yet, but without access to the hardware I'm not really able to work on it further.

[For now](lars_v2.html)...

## More Pictures
<a class="anchor" name="more_pictures"></a>

<div class="collapse">Some more photographs I didn't use above.</div>
<div class="collapsecontent">
<!--%
lightgallery([
    [ "img/lars_1.jpg", "LARS front panel. © 2024 Kauzerei." ],
    [ "img/lars_2.jpg", "LARS on table. © 2024 Kauzerei." ],
    [ "img/lars_5.jpg", "LARS on table. © 2024 Kauzerei." ],
    [ "img/lars_6.jpg", "LARS on table. © 2024 Kauzerei." ],
])
%-->
</div>
