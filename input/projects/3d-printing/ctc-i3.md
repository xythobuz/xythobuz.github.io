title: CTC i3 Pro B
description: My modifications for the CTC i3 Pro B
parent: 3d-printing
position: 20
comments: true
flattr: true
---

<span class="listdesc">[...back to 3D-Printing overview](3d-printing.html)</span>

The CTC i3 Pro B is a very cheap chinese Prusa i3 clone.
I bought it a couple of years ago for about 110 Euros.
The frame and motor mountings are made out of pieces of laser cut wood.
Because of this, the frame flexes a lot, which is the main reason I would not recommend this machine today.
Nonetheless, this is my main printer.
I have used it a lot over the years and also modified many things on it.

The Y Axis mainly consists of M8 threaded rods and smooth rods, driven by a belt.
The Z Axis also is made with smooth rods and driven by M8 threaded rods.
The X Axis only has smooth rods and is also driven by a belt.

As a first step, I replaced the M8 rods of the Z-Axis with proper ACME thread T8 lead screws.
Of course, to use these, I had to also get T8 nuts and print different Z-Carriages.

I also replaced all the ball bearings with [IGUS RJ4JP-01-08 polymer bushings](https://amzn.to/33FZDSz), replaced the fans and added [silent TMC2100 stepper motor drivers](https://reprap.org/wiki/TMC2100) to reduce noise.

<!--%
lightgallery([
    [ "img/ctc_i3_front.jpg", "Front view of CTC i3 Pro B" ],
    [ "img/ctc_i3_side.jpg", "Side view of CTC i3 Pro B" ],
    [ "img/ctc_i3_board.jpg", "Mainboard of CTC i3 Pro B" ]
])
%-->

## Power Supply Replacement

One of the first things I did was replacing the power supply with an ATX PC PSU.
To mount it to the printer frame, I used ["Anet A8 ATX mount" by corsara](https://www.thingiverse.com/thing:2256502).
This not only provides +12V to the printer itself, but can also power a Raspberry Pi with the +5V Standby power that is always available.
That way, the Pi can use a GPIO to turn on/off the printer power using the green "Power On" signal of the ATX standard power supply connector.
The standby power cable is purple.
See [Wikipedia](https://en.wikipedia.org/wiki/ATX#Power_supply) for details.

<!--%
lightgallery([
    [ "img/ctc_i3_psu.jpg", "ATX power supply mounted on CTC i3 Pro B" ]
])
%-->

## Heatbed Replacement



<!--%
lightgallery([
    [ "img/ctc_i3_bed.jpg", "Side view of printbed with insulation" ]
])
%-->

## Print Surface

For the printing surface, I have tried many different options over the years.
My first printer originally came with blue painters tape, which did not survive for long.
My first replacement there was Kapton tape, which I am still using on the Fabrikator Mini.

For the CTC i3, my first attempt was using a plate of borosilicate glass, which I kept for a couple of years.
Even though it has its problems with getting the first layer to stick and also needs clamps that reduce the available space, I was able to use it pretty successfully with PLA and TPE, as long as the first layer area was large enough or i was using a brim.
But with PETG, I had serious problems getting the first layer to stick.

Next, I tried [this UEETEK BuildTak clone](https://amzn.to/3ofM1qD).
It works very well, the first layer sticks unbelievably strong to the rough surface.
It even works too well.
It is often difficult to get the print removed. I found myself orienting prints so the first layer area is as small as possible, so I could get it removed more easily.
Even though that worked pretty well, and eliminated all first layer issues, I now had the issue of getting prints off without destroying them or the build surface.

Because of that, I next got the [ERYONE magnetic build surface](https://amzn.to/33GLq84).
The magnetic mounting works very well and the steel sheet sticks to the magnetic plate strongly.
The surface has a sheet of maybe-fake-or-not PEI on top. This works relatively well for now, I would compare it to the Kapton sheet or the glass plate, prints don't stick too well, but with a large surface or brim it seems to work.

But it is still not perfect.
As a next step, I plan to combine the magnetic plate with the fake BuildTak.
I hope this may combine the positive aspects, having a first layer that sticks well, but still can be removed.
But I have not tried that yet.

TODO photos

## MOSFET for Heatbed



<!--%
lightgallery([
    [ "img/ctc_i3_fet.jpg", "MOSFET board mounted to side of CTC i3 Pro B" ]
])
%-->

## Y-Axis Replacement

To upgrade the Y-Axis and get rid of the wood pieces keeping the X distance, I printed the Y-axis files from the original Prusa i3 design.
They can be found [in the master branch of the GitHub repo](https://github.com/prusa3d/Original-Prusa-i3/tree/master/Printed-Parts/scad), as in "y-corners.scad", "y-motor.scad" and so on.
I got this idea from a YouTube video that I can no longer find unfortunately.

With these parts, the Y-axis distance are kept simply by two more M8 threaded rods.
Putting it all together so the smooth rods are exactly parallel and the bed travels smoothly is a bit tricky, but can be done with some playing around.

<!--%
lightgallery([
    [ "img/ctc_i3_y_belt.jpg", "Y-Axis belt tensioner of original Prusa i3 design" ],
    [ "img/ctc_i3_y_corner.jpg", "Y-Axis corner pieces of original Prusa i3 design" ]
])
%-->

## Y-Carriage Replacement

Originally the Y-Carriage, which carries the heatbed, was also made out of thin wood, flexing a lot.
When trying to achieve a print bed that is as level as possible, this is not good.
So I simply got a properly sized piece of aluminium from ebay, drilled the holes for some small printed bearing holders and mounted the heatbed to it.
This was easy and has worked very well as a replacement.

TODO photos

## Y-Axis Webcam Mount

With the replaced Y-axis, it was easy to design a simple bracket that screws onto the front M8 rods.
With another piece of M8 rod, I mounted a webcam.
First, while I was still using an Orange Pi instead of a Raspberry Pi, I mounted the Orange Pi camera there.
Later, after the switch to the Raspi, I also switched the camera to a Logitech C270.
I also added another print that can hold a piece of LED strip under the camera, so you have more light for the picture.

The design files can be found [on my Gitea server](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/opi-pc-plus).

<!--%
lightgallery([
    [ "img/ctc_i3_cam.jpg", "Webcam mount with lights" ]
])
%-->

## Z-Carriages / X-Axis Replacement

Relatively early after getting my printer I replaced the Z-Carriages and the X-Axis.
For this, I used ["Smooth X-axis for Prusa i3 with Leadscrews" by MazaaFIN](https://www.thingiverse.com/thing:1103976).
However, I only printed the right Z-Carriage.
For the left one, I used ["X Axis motor mount for Anet A8 or Prusa i3" by Randino](https://www.thingiverse.com/thing:2328353), because the X endstop switch mount better fit my next replacement.
For the Z endstop, I have used ["Prusa i3 ANET A8, Z Endstop Adjuster." by flyingferret](https://www.thingiverse.com/thing:1479176) which can be tuned finely and works great.

So my X-Axis is a bit of a mix-up, but it seems to work well and I have not had the need to replace anything else there since.

<!--%
lightgallery([
    [ "img/ctc_i3_x_left.jpg", "Left side Z-Carriage" ],
    [ "img/ctc_i3_x_right.jpg", "Right side Z-Carriage" ]
])
%-->

## X-Carriage Replacement

I replaced the X-Carriage with the great ["Customizable direct drive extruder for E3D v6 hotend for Prusa i3 / Wilson / Geeetech" by gtcdma](https://www.thingiverse.com/thing:1383913).
It is a well-designed and sturdy hotend mount with a direct extruder.
It is written in OpenSCAD, so I modified it a bit, making my own custom filament and hotend fan mounts.
To mount a capacitive bed leveling sensor to it, I used ["Mount for capacitieve sensor 19mm" by Slavulj](https://www.thingiverse.com/thing:1607619).

The files can also produce a dual-extrusion design.
I tried it as well and ran it for a while.
But I have since reverted it to a single hotend.
I was not really using the dual-color feature and it has the usual problems of two hotends mounted side-by-side on the same height.
The second, unused, nozzle tends to collide with the print causing many different problems.
But other than that and with some tuning it worked well and I was getting some good two-color prints.

If you use a strong spring for the extruder arm to get a high contact force without slip on the extruder, I suggest printing it with PETG at least, because the PLA I was using originally warped after a while, causing the filament to jump out of the extruder gear.

For the extruder motor, I used a NEMA17 with only half the usual height to increase clearance to the top frame brace, which is described below.

My modified design files [can be found on my Gitea server](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/i3-e3d-v6-direct-extruder).

<!--%
lightgallery([
    [ "img/ctc_i3_extruder.jpg", "Front view of the Extruder" ],
    [ "img/ctc_i3_extruder2.jpg", "Bottom view of the Extruder" ],
    [ "img/i3_hotend_extruder_1.png", "Side view of design" ],
    [ "img/i3_hotend_extruder_2.png", "Front view of design" ]
])
%-->

## Z-Axis Top Fix



<!--%
lightgallery([
    [ "img/ctc_i3_top_left.jpg", "Top left Z bracket" ],
    [ "img/ctc_i3_top_right.jpg", "Top right Z bracket" ]
])
%-->

## Frame Braces



## Raspberry Pi Addon



<!--%
lightgallery([
    [ "img/ctc_i3_pi.jpg", "Raspberry Pi mounted on CTC i3 Pro B" ]
])
%-->

## Power Button



<!--%
lightgallery([
    [ "img/ctc_i3_power.jpg", "Power Button for OctoPrint" ],
])
%-->

## Slicing Profiles



## Print Results Pictures


