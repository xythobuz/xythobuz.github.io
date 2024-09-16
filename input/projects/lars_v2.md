title: LARS v2
description: Upgrading the Looping Automated Rhythm Station
parent: projects
git: https://git.xythobuz.de/thomas/drumkit
github: https://github.com/xythobuz/lars
date: 2024-09-07
update: 2024-09-16
comments: true
---

So you may have read about our project [LARS](lars.html).
As mentioned I didn't have any hardware in the end to finish firmware development.
So I slightly updated the circuitry, layed out a new board, had it manufactured in China and assembled at home.

This is LARS v2, the second iteration of the same idea.

<!--%
lightgallery([
    [ "img/lars_v2_1.jpg", "LARS v2" ],
    [ "img/lars2_midi.mp4", "video/mp4", "", "", "LARS v2 playing MIDI example file" ],
])
%-->

It's basically the same device, just with five additional switches.
This allows for some more freedom in the user interface design.
Now the loop mode can mute individual tracks.
There's also USB MIDI support.

<!--%
lightgallery([
    [ "img/lars2_parts.jpg", "LARS v2 PCBs and parts" ],
    [ "img/lars_loop_controls.jpg", "LARS Loop Station controls" ],
])
%-->

As [usual](2024_05_05_auto_project_docs.html) I've added auto-generated [documentation](https://xythobuz.github.io/lars/), including [interactive 3D renders of the PCB](https://xythobuz.github.io/lars/pcb2_pcb.html) and some [usage hints](https://xythobuz.github.io/lars/usage.html).
The [gerber files](https://xythobuz.github.io/lars/plot/fab_pcb2.zip) and [BOM](https://xythobuz.github.io/lars/pcb2.html) to order your own are also available.

Unfortunately I'm kind of in the same situation now as with LARS v1.
I've gone much further with the firmware, it's now mostly usable.
But I've also given the hardware away again, so I can't finish it.

<s>I should assemble another one soon...</s>

## Assembly Guide

You want to build your own LARS v2 and have all the parts ready to go?
Then let's build it!

In general you want to go from SMD / SMT (surface mount) parts to THT (through-hole), going from large to small for the SMD parts, and small to large for the THT parts.

First place the SMD Raspberry Pi Pico module so all pads are properly aligned.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_1.jpg", "Empty PCB" ],
    [ "img/lars_v2_assembly_2.jpg", "Pico placed" ],
])
%-->

Now first solder on one corner, then go through both rows.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_3.jpg", "First Pico corner soldered" ],
    [ "img/lars_v2_assembly_4.jpg", "One Pico row soldered" ],
    [ "img/lars_v2_assembly_5.jpg", "Pico soldering finished" ],
])
%-->

The battery holder snaps in with two plastic clips.
Soldering the pads can be a bit tricky.
Even though there is a hole for the solder to flow through to the pad, you can not see it well.
Try to apply a bit of pressure to get the pads to connect reliably.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_6.jpg", "Battery holder snapped in" ],
    [ "img/lars_v2_assembly_7.jpg", "Battery holder soldered on" ],
])
%-->

Now place all the pushbuttons and solder them in.
Their legs have a snap fit so they will hold on properly.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_8.jpg", "Pushbuttons placed" ],
    [ "img/lars_v2_assembly_9.jpg", "Buttons soldered" ],
])
%-->

Next the resistors.
I'm bending their legs slightly so they stay in place when turning the board over.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_10.jpg", "LED resistors placed" ],
    [ "img/lars_v2_assembly_11.jpg", "LED resistor legs bent" ],
    [ "img/lars_v2_assembly_12.jpg", "LED resistors soldered in" ],
    [ "img/lars_v2_assembly_13.jpg", "Voltage divider resistors done" ],
])
%-->

The diodes and LEDs can be placed next, with the same leg-bending trick as before.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_14.jpg", "Diodes in place" ],
    [ "img/lars_v2_assembly_15.jpg", "LEDs placed" ],
])
%-->

The encoder snaps in as well.
For the switch and OLED, make sure to apply a bit of pressure when turning the board over, so they are firmly in place.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_16.jpg", "Switch, encoder and OLED placed" ],
    [ "img/lars_v2_assembly_17.jpg", "Switch, encoder and OLED soldered" ],
])
%-->

The pins of the MOSFET module screw-terminals fit into the board holes and can be soldered on directly.
For the small logic pins use a bit of the cut-off legs from the LEDs or resistors.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_18.jpg", "MOSFETs in place, top" ],
    [ "img/lars_v2_assembly_19.jpg", "MOSFETS in place, bottom" ],
    [ "img/lars_v2_assembly_20.jpg", "MOSFET terminals soldered" ],
    [ "img/lars_v2_assembly_21.jpg", "MOSFET logic pins soldered" ],
])
%-->

For the regulator I'm using standard pins like they probably came with your Pico.
But you could also use some more of the cut-off legs from the previous steps.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_22.jpg", "Regulator pins prepared" ],
    [ "img/lars_v2_assembly_23.jpg", "Regulator in place" ],
    [ "img/lars_v2_assembly_24.jpg", "Regulators soldered, top" ],
    [ "img/lars_v2_assembly_25.jpg", "Regulators soldered, bottom" ],
])
%-->

The charger pad does not quite fit the connections of the module.
So I'm using two pins per connection in a 90 degree angle.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_26.jpg", "Charger pins prepared" ],
    [ "img/lars_v2_assembly_27.jpg", "Charger module prepared" ],
])
%-->

And that's it.

<!--%
lightgallery([
    [ "img/lars_v2_assembly_28.jpg", "Finished board" ],
])
%-->

Good luck and have fun!
