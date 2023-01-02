title: Laser Engraver
description: Marlin based CNC laser engraver / cutter with 3D printed parts
parent: projects
git: https://git.xythobuz.de/thomas/marlin/src/branch/laser-engraver
date: 2022-11-25
update: 2023-01-02
comments: true
---

After dabbling in 3D printing for a couple of years now, I had to level-up my Makers toolkit.
The next logical step, in my opinion, is laser engraving / laser cutting.
I have to admit I was initially a bit scared and still have some respect for the potential hazards posed by the strong, focussed laser beam.
So I decided to go slow and start with a low powered 2.5W diode laser.

⚠️ Be sure to always use proper laser safety goggles when working with such machines! ⚠️

<!--%
lightgallery([
    [ "img/laser_tower_1.jpg", "Frontal view in Ikea Lack tower" ],
    [ "img/laser_tree_test.mp4", "video/mp4", "", "", "Cutting a christmas tree decoration" ],
    [ "img/laser_side_1.jpg", "View from left side" ],
    [ "img/laser_side_2.jpg", "View from right side" ],
])
%-->

### Table Of Contents

* [Hardware](laser-engraver.html#hardware)
    * [Mechanics](laser-engraver.html#mechanics)
    * [Electronics](laser-engraver.html#electronics)
* [Software](laser-engraver.html#software)
    * [MCU Firmware](laser-engraver.html#mcu_firmware)
    * [Host Software](laser-engraver.html#host_software)
        * [LaserGRBL](laser-engraver.html#lasergrbl)
        * [Inkscape](laser-engraver.html#inkscape)
        * [FreeCAD](laser-engraver.html#freecad)
        * [Working with G-Code](laser-engraver.html#g_code)
* [Cutting Tests](laser-engraver.html#cutting_tests)
* [Future Improvements](laser-engraver.html#future_improvements)
* [Cutting Parameters](laser-engraver.html#cutting_parameters)
* [More Pictures](laser-engraver.html#more_pictures)

## Hardware
<a class="anchor" name="hardware"></a>

I know I say this in a lot of articles here, probably in an attempt to justify my hoarding of electronic parts. 😳
But this was even better than most of my previous projects, in the sense that I didn't have to buy any parts at all, except for the 2500mW 450nm laser diode, which I got used from my colleague [Philipp](https://www.phschoen.de/) for just 13€.
The rails I bought many years ago and never used.
The steppers, mainboard, display, fans and cables came from my now disassembled [CTC i3](ctc-i3.html).
Everything else came out of my parts bin.

### Mechanics
<a class="anchor" name="mechanics"></a>

The mechanism is based on the ["Cantilever Laser Engraver" by Meatball](https://www.printables.com/model/213526-cantilever-laser-engraver).
This in turn is based on the ["Cantilever Laser Engraver" by GeoDave](https://www.thingiverse.com/thing:4605853).
It uses 2020 aluminium extrusions with V-slot wheels for the X and Y axis.

I really like this simple design that does not require a lot of parts.
It has some problems with twisting of the Y-rail due to the weight hanging from the cantilever arm, but this can easily be solved by supporting the free-hanging side of the X-rail.
Otherwise the length of the axes can be customized freely.

<!--%
lightgallery([
    [ "img/laser_frame.jpg", "Frame of laser engraver, made of 2020 rails" ],
    [ "img/laser_y_gantry.jpg", "Close view of Y gantry mechanism" ],
    [ "img/laser_x_support.jpg", "Close view of X axis support wheel" ],
])
%-->

I had to do some modifications to the design files provided by Meatball.

The "Y-Axis Gantry Upper" has enlargened the holes for two of the four wheels, to be able to fit eccentric nuts that provide the required tensioning on the wheels.
The "Y-Axis Gantry Lower" however has normal sized holes.
So when using these parts, the two wheels are not actually moved perpendicular towards the extrusion, but are instead angled sideways.
To avoid this problem I made the two holes in the lower bigger as well and used four instead of two eccentric nuts.
I also slightly increased the distance between the two sets of wheels on the Y-axis, because it was very hard to fit the rail, even with the eccentric nuts as loose as possible.

I also designed custom endstop mounts using M2.5 heat-melt inserts, as well as a support wheel for the free-hanging side of the cantilever arm and a mount for the Ultimaker Controller 2004 LCD.

The OpenSCAD and STL files for these parts [can be found on my Printables profile](https://www.printables.com/model/314945-cantilever-laser-engraver-fixes).

To fit the whole machine comfortably inside my [Ikea Lack tower](ikea-lack.html) I mounted it on a 18mm mutliplex base plate with 540x440mm.
The 3D printed feet of the Y-axis already have holes for countersunk screws, so I simply used wood screws there.
To mount the mainboard PCB and laser heatsink I made 3.2mm holes for M3 screws and M3 stand-offs, drilling with a 6mm drill from the bottom to approximately half the depth of the base plate, so even cylindrical screw heads don't stand out from below the plate.
I also added a power switch with a simple 3D printed mount.

<!--%
lightgallery([
    [ "img/laser_power_switch.jpg", "Power switch with mount" ],
])
%-->

### Electronics
<a class="anchor" name="electronics"></a>

As mentioned above I used the electronics, namely mainboard, LCD and fans, from my old 3D printer.

<!--%
lightgallery([
    [ "img/laser_electronics.jpg", "GT2560 mainboard and laser control PCB on base plate" ],
    [ "img/laser_lcd.jpg", "LCD mounted to laser engraver" ],
])
%-->

To connect the laser diode TTL input, a PWM capable pin from the microcontroller is required.
To find one, we need to take a look at the schematics for the GT2560 mainboard, which can be found in the [Geeetech Forums](https://www.geeetech.com/forum/viewtopic.php?f=13&t=19092&start=10).

<!--%
lightgallery([
    [ "img/GT2560_1.png", "First page of GT2560 schematics" ],
    [ "img/GT2560_2.png", "Second page of GT2560 schematics" ],
])
%-->

I decided to use `PL4`, the `DIR` pin of one of the now unused stepper drivers.
To connect to it I prepared a little piece of perfboard, to be placed in the slots like a stepstick, with an additional pull-up resistor to the 5V logic voltage present on the same header.
To find the pin number for the Marlin configuration, we can take a look at the [Arduino Mega pin mappings](https://docs.arduino.cc/hacking/hardware/PinMapping2560), which show `PL4` to be Arduino pin `45`.

<!--%
lightgallery([
    [ "img/laser_ttl_pwm.jpg", "TTL PWM input of laser, with pull-up resistor" ],
])
%-->

I'm not only connecting the laser TTL input to the mainboard, I'm also switching the 12V supply as well, by using the MOSFET originally intended for the hotend heater.
This brought a little problem however.
Both connectors of the laser PCB have a ground connection.
And the ground connection is also the one that's switched, when connecting the laser to the power supply.
So even when the MOSFET was turned off the laser still had a ground connection and was powered through the ground pin of the TTL connector, so it could never fully turn off.
So if you do the same, make sure to only connect one of the two ground pins!

The power supply is simply reused from my [Fabrikator Mini](fabrikator-mini.html), it already was placed in the Ikea Lack tower.
To save some space I now mounted it to the top of the next Lack table above the laser, with some strips of perforated metal sheet.
Of course this is kind of problematic, as the rest of the machine is kind of designed to be easily transportable.
I will have to find some kind of small alternative power supply.

<!--%
lightgallery([
    [ "img/laser_psu.jpg", "12V power supply on underside of Ikea Lack" ],
])
%-->

## Software
<a class="anchor" name="software"></a>

There's a surprisingly large amount of software involved in this project.
All just to move a lamp around a bit 💡🤔

### MCU Firmware
<a class="anchor" name="mcu_firmware"></a>

Most DIY laser engravers or CNC machines seem to use the [GRBL firmware](https://github.com/gnea/grbl).
Unfortunately this firmware only runs on Atmega328p MCUs, so I can not use it with the Atmega2560 on the GT2560 mainboard.
There are some GRBL ports, for [ESP32](https://github.com/bdring/Grbl_Esp32) or [STM32](https://github.com/thomast777/grbl32) microcontrollers, but obviously these don't help either in my situation.

So I decided to use the trusty old [Marlin Firmware](https://marlinfw.org/), which was already running previously on my old 3D printers and this mainboard.
Configuring Marlin is pretty straight-forward, there's a [configuration guide](https://marlinfw.org/docs/configuration/configuration.html) but the settings in the two config header files are well commented and pretty much self explanatory.
The only interesting parts are the laser-specific settings in `Configuration_adv.h`, like `LASER_FEATURE` and `LASER_POWER_SYNC`.

Apparently I seem to be the first person that tries to run an Ultimaker Controller 2004 LCD without a Z-Axis.
I had to add a couple of `#ifdef Z_AXIS` in `src/lcd/HD44780/marlinui_HD44780.cpp`.

You can see all the modifications to the configuration I initially made to get the machine running [in this commit](https://git.xythobuz.de/thomas/marlin/commit/41cd87398d539f41c2ebe54b5f675c6c8b5ce04b).

I also did some small changes to show the current laser power on the LCD status screen.
These changes can be seen [in this commit](https://git.xythobuz.de/thomas/marlin/commit/58dbdff1d5b6e365bfd5ae4eeb7b42967688c51e).
I also opened a [pull request](https://github.com/MarlinFirmware/Marlin/pull/25003) to upstream them, which was merged into `bugfix-2.1.x` in November 2022.

Later I learned that Marlin does not allow setting home offsets further than 20mm away from endstops.
So I also [added a custom menu command](https://git.xythobuz.de/thomas/marlin/commit/74cafcd77625003623d3a8a6378a4ff0ac6eda72) that simply executes [`G92`](https://marlinfw.org/docs/gcode/G092.html) `X0 Y0` to set the current position to zero.
Using this I can generate G-Code where the object to cut starts at coordinates `(0, 0)` while being able to position it arbitrarily on the machine itself.

My current Marlin configuration for the laser engraver can be found [on my Gitea instance](https://git.xythobuz.de/thomas/marlin/src/branch/laser-engraver).

### Host Software
<a class="anchor" name="host_software"></a>

Besides the microcontroller firmware, we also need some host software to prepare the G-Code from whatever kind of input file we start out with.
There are two basic approaches for generating paths for the laser engraver.
One is "rasterization", where a bitmap image is turned into commands line-by-line, enabling and disabling the laser at different parts of each line.
This will draw an image similar to how a CRT TV works, which is useful eg. for engraving logos.

The other variant is "vectorization", where either a bitmap is converted to a vector path, or we start out with a vector file format, like svg.
The laser can then follow the outline and optionally also fill between the outlines in some kind of pattern.
This can then be used to cut shapes from objects.

At this point I should also mention [Lightburn](https://lightburnsoftware.com/).
This software is used both for the Laser cutters at [Toolbox Bodensee](https://toolbox-bodensee.de/), as well as by my neighbour, who uses it with an [Ortur Laser Master 2](https://ortur.net/products/laser-master-2-pro).
So I had some contact with it, and I have to admit, it works well and has a lot of functionality.
But it is commercial paid software, not under any free software license, so [it is not an option for me](https://www.gnu.org/proprietary/proprietary.html).

Below I will try to document all different free software packages I tried for laser engraving.

#### LaserGRBL
<a class="anchor" name="lasergrbl"></a>

The first solution I found out about is [LaserGRBL](https://lasergrbl.com/).
It is a Windows-only program, but at least it is open-source / free software.
As the name implies however, it is intended for use with the [GRBL firmware](https://github.com/gnea/grbl).

The G-Code flavor of GRBL is considerably different compared to Marlin, but I was able to get it to work mostly.

For rasterization of bitmap images, GRBL produces G-Code with the laser power levels put inline with the movement commands.

<pre class="sh_gcode">
G0 X25 Y10 S0
G1 X26.5 S150
G0 X28.25 Y10.25 S0
G1 X23 S150
</pre>

Without further modifications, this only moves the toolhead, while keeping the laser off at all times, because Marlin by default does not process the power-level parts of the G-Code lines.
To get this to work, the "continuous inline power mode" has to be enabled by putting `M3 I` in the G-Code header setting of LaserGRBL, as well as at the end of the "Multiple Passes" G-Code section.

<!--%
lightgallery([
    [ "img/lasergrbl_settings.png", "LaserGRBL G-Code settings" ],
])
%-->

Here are the results of my first attempts of engraving a rasterized image into a piece of scrap wood.
The rocket used 6 lines/mm, with default speed and a PWM range of 0-255.
The smirkey used 4 lines/mm, with default speed and a PWM range of 0-150.

<!--%
lightgallery([
    [ "img/laser_raster_result.jpg", "My first cuts of some rasterized images" ],
])
%-->

When trying to engrave vectorized paths, like the outline of an image, LaserGRBL produces different output, however.
The power levels are now put on their own lines, but without any G-Code command, as usual shorthand used by GRBL.

<pre class="sh_gcode">
S0
G0 X14.382 Y14.618
S150
G1 X14.618 Y14.382
S0
G0 X14.618 Y14.618
S150
G1 X14.457 Y14.457
</pre>

Using a simple Python script, we can convert to the same format as used for rasterization.
It simply reads the input file into the output file, skipping every line starting with an uppercase letter 'S', instead appending that to the next line.

I also noticed the speed set in LaserGRBL did not properly apply in Marlin.
This is because, in vector mode, it puts a single "Fxxx" line at the beginning.
Even though Marlin can interpret this in our configuration, there is no G1 mode set before, so Marlin does not know where to apply the speed.
So I am also handling this case in the script as well.
For raster input, LaserGRBL only puts the speed in a single G0 move at the beginning.
So the speed does not apply to the G1 moves afterwards.
This case is not handled yet.

In another vector job, I saw LaserGRBL generate output like the following.

<pre class="sh_gcode">
G0X3Y2
S255
G1Y5F200
X0.7
Y8.347
X8.25
X8.75Y8.847
Y12.347
</pre>

This is the very compact GRBL G-Code dialect, which leaves out spaces and also the modes, as long as they don't change.
So to handle that, I remember the last G0/G1 mode, prepending it as needed to lines, while also adding the missing spaces for better human readable output.

As you can tell there are many different output formats from LaserGRBL and I'm not able to tell when it will generate what.
But my script below should work for all variants I have seen up to now.

<pre class="sh_python">
<!--%
include_url("https://git.xythobuz.de/thomas/gcode-tools/raw/branch/master/tools/convert_lasergrbl.py")
%-->
</pre>

You can also find this script [on my Gitea server](https://git.xythobuz.de/thomas/gcode-tools/src/branch/master/tools/convert_lasergrbl.py).

Here is my first attempt of cutting a vector outline of an image out of a piece of paper.
I used Marlins default speed and a PWM setting of 150 out of 255.

<!--%
lightgallery([
    [ "img/laser_vector_result.jpg", "My first cut of a vector outline" ],
])
%-->

For these tests I have simply used LaserGRBL to produce a G-Code file, which I have then transferred to an SD card for direct use in the engraver.
LaserGRBL also can directly connect to the machine via the serial port.
This has worked for me for a bit, but even though you can set the G-Code flavor to Marlin in the LaserGRBL settings, it does not really work properly.
You can jog the toolhead but homing is not possible.
I also had to reduce the polling frequency in the LaserGRBL settings to 'Quiet' and disable Soft-Reset to get it to work inside the VirtualBox VM I used at first to run the program.

It is also possible to [run LaserGRBL in Wine](https://github.com/arkypita/LaserGRBL/issues/5#issuecomment-873564055) / [with PlayOnLinux](https://github.com/arkypita/LaserGRBL/raw/master/POL_LaserGRBL_setup.sh).
At first I was not able to run this PlayOnLinux script due to Winetricks downloads failing with invalid checksums.
But after trying a couple of days later, with the exact same script, the installation worked fine.
I had to make the same changes to the settings as described for VirtualBox above.
Unfortunately in Wine LaserGRBL hangs when attempting to load rasterized images.
So I went back to the VM for that.

Also for all the above tests with LaserGRBL I have imported raster bitmap images and either rastered them, or vectorized them within LaserGRBLs UI.
With bitmaps it is possible to position the resulting G-Code paths with an offset from the zero position of the machine.
This is not possible when using LaserGRBL to import SVG vector paths.
With them, the output will always start at coordinates `(0, 0)`.
You will then have to set the proper offset on the machine itself, as described in the Marlin section above.

#### Inkscape
<a class="anchor" name="inkscape"></a>

Inkscape includes the [G-Code Tools Plugin from the russian-language CNC-Club forums](https://www.cnc-club.ru/forum/viewtopic.php?t=35).
Unfortunately I was not able to find much up-to-date english-language documentation for this.
It is also relatively complicated and unintuitive.

I was able to get it to generate G-Code from a path, but not with any laser power instructions yet.
This section will be updated if I have more success in the future.
Until then I'm just using Inkscape to export svg files for LaserGRBL.

#### FreeCAD
<a class="anchor" name="freecad"></a>

FreeCAD has the [Path Workbench](https://wiki.freecadweb.org/Path_Workbench), which can be used to create G-Code instructions for all kinds of CNC machines.
It is not really complete and fool-proof yet, unfortunately.
And it is also not designed for pure 2D machines, like laser engravers, by default.

I have not yet tested that.

#### Working with G-Code
<a class="anchor" name="g_code"></a>

One nice feature I saw in LaserGRBL, but was not able to use with Marlin, is the ability to draw the outline of the object to be cut, for positioning of the stock material.
So I quickly made up a small Python script that analyzes a G-Code file, taking the coordinates from all G1 cutting moves and generating their bounding box, which is then drawn on the lowest possible power setting multiple times.
I copy this file to the SD card, start it, and just abort it when I'm done with the preparations.

<pre class="sh_python">
<!--%
include_url("https://git.xythobuz.de/thomas/gcode-tools/raw/branch/master/tools/outline_gcode.py")
%-->
</pre>

You can also find this script [on my Gitea server](https://git.xythobuz.de/thomas/gcode-tools/src/branch/master/tools/outline_gcode.py).

I also did some experimentation with programatically generating G-Code myself, using a simple Python script as well.
It's drawing a grid for reference on the base plate of the machine, including numerical position indicators.

<pre class="sh_python">
<!--%
include_url("https://git.xythobuz.de/thomas/gcode-tools/raw/branch/master/generators/grid_gcode.py")
%-->
</pre>

You can also find this script [on my Gitea server](https://git.xythobuz.de/thomas/gcode-tools/src/branch/master/generators/grid_gcode.py).

I like the idea but unfortunately it has some problems in practice.
When changing the focus level of my laser diode, it's very easy to also change the offset in the X and Y axes.
So the grid is not properly aligned for long.
But it still looks nice.

<!--%
lightgallery([
    [ "img/laser_grid.jpg", "Closer view of grid on base plate" ],
])
%-->

If you look closely, you can see the first run I did with a power setting of 50 / 255.
This was not strong enough, the lines are only faintly visible.
So I did another run with 100 / 255 over it.
This was enough power for nice visible lines, but the laser offset unfortunately shifted slightly between the runs.

As I grew tired of removing, flashing and re-inserting of the SD card, I decided to also write a quick little G-Code sender for the serial port.

<pre class="sh_python">
<!--%
include_url("https://git.xythobuz.de/thomas/gcode-tools/raw/branch/master/tools/send_gcode.py")
%-->
</pre>

You can also find this script [on my Gitea server](https://git.xythobuz.de/thomas/gcode-tools/src/branch/master/tools/send_gcode.py).

Of course it's important to use the proper speed, power and number of iterations for each object to cut.
Not enough power or iterations, or too high of a speed, and the object will still be part of the stock material.
Too much power or iterations and not only the object will be cut, but also the base plate below.

So I first did some tests manually, which is relatively time consuming.
I then made another Python script go generate G-Code for a cutting test, varying speed and number of iterations.

<pre class="sh_python">
<!--%
include_url("https://git.xythobuz.de/thomas/gcode-tools/raw/branch/master/generators/cut_test_gcode.py")
%-->
</pre>

You can also find this script [on my Gitea server](https://git.xythobuz.de/thomas/gcode-tools/src/branch/master/generators/cut_test_gcode.py).

I'm drawing digits again, like in the Grid G-Code generator above.
It seems I need to create some kind of library or so if I continue this route of generating G-Code.

<!--%
lightgallery([
    [ "img/laser_cut_test_1.jpg", "Test sheet being cut" ],
    [ "img/laser_cut_test_3.jpg", "Finished test run" ],
])
%-->

In the pictures above, the 3x3 grid of hearts on the right was made with the laser slightly out of focus.
It was not able to cut through in this run, even with 30 iterations.
I also still had the text not aligned properly.

The 3x1 and 3x3 runs on the left side were made after properly focussing the laser and fixing the text alignment.
Here 200mm/min with 10 iterations was already enough to cut through the 3mm plywood.

## Cutting Tests
<a class="anchor" name="cutting_tests"></a>

For the first 'real' test I decided to cut the assembly jig for the [Pagoda antenna](https://www.maartenbaert.be/quadcopters/antennas/pagoda-antenna/#design-files) by Maarten Baert.
The files are available in dxf and svg format.
I was able to easily import the svg file in LaserGRBL to create G-Code, afterwards converting it to the proper format using my script described above.

<!--%
lightgallery([
    [ "img/laser_pagoda_1.jpg", "Front side of the Pagoda jig sheet" ],
    [ "img/laser_pagoda_2.jpg", "Back side of the Pagoda jig sheet" ],
    [ "img/laser_pagoda_3.jpg", "Assembled Pagoda antenna jig" ],
])
%-->

As in one of my previous tests I used 200mm/min with 10 iterations.
But this was not quite enough to get the parts out easily.
In hindsight I should have used at least 15 iterations.
But the result was still usable, even with only 10 iterations.

Next my SO requested some christmas decoration, so I decided to attempt to cut this [Christmas Tree Ornament](https://www.thingiverse.com/thing:43041) by TomKeddie on Thingiverse.
It is made for 4.8mm plywood, so I scaled it down by a factor of `3.0 / 4.8 = 0.625`.
The design comes as a dxf file, so I imported that in Inkscape and then exported an svg file from that.
This I then imported in LaserGRBL, generated G-Code and converted that using the script above.

<!--%
lightgallery([
    [ "img/laser_tree_test.mp4", "video/mp4", "", "", "Cutting a christmas tree decoration" ],
    [ "img/laser_tree_segments.mp4", "video/mp4", "", "", "Segmented lines while cutting" ],
])
%-->

As you can tell from the second video, what should be single continuous lines has instead sometimes been split up into many small path segments, which LaserGRBL is cutting in non-optimal ordering.
I have not yet found a way to easily clean these paths up.

<!--%
lightgallery([
    [ "img/laser_tree_1.jpg", "Front side of christmas tree sheet" ],
    [ "img/laser_tree_2.jpg", "Back side of christmas tree sheet" ],
    [ "img/laser_tree_3.jpg", "Finished christmas tree ornament" ],
])
%-->

The end-result does not seem to be really affected by this however, although with 200mm/min and 15 iterations the parts were not removable as easily as I hoped.
So I think I either have to adjust the focus better or go up to 20 iterations for the 3mm birch plywood.

## Future Improvements
<a class="anchor" name="future_improvements"></a>

I didn't expect it to be this bad, but cutting wood really produces a noticeable amount of smoke and the smell of burnt wood.
So in the long run I will have to add some kind of air filtration system to my Ikea Lack tower.
Also I now better understand the need for Air Assist on laser cutters.
My small fans don't help much in keeping the light-path free of smoke and soot.
But I will hopefully get away with running it for a while without these additions.

Another obvious improvement is the addition of a Raspberry Pi and a Webcam, to allow remote monitoring of long-running jobs.
I also came across the [LaserWeb project](https://laserweb.yurl.ch/) which seems to be similar in spirit to OctoPrint for 3D printers, but also with the ability of processing vector and bitmap files from within the web interface.
This would be a very useful addition and solve a lot of the software workflow problems illustrated above.
Also theres more than enough room left on my base plate for a SBC.

## Cutting Parameters
<a class="anchor" name="cutting_parameters"></a>

Here are the results of all cutting tests I've made up to now.
I will update this table as soon as I gather new data 🧑‍🔬

<!--%
tableHelper([ "align-right", "align-right", "align-right", "align-right", "align-right", "align-right", "align-right", "align-left", "align-left" ],
    [ "Type", "Material", "Thickness<br><span style=\"font-size: small;\">(in mm)</span>", "Power<br><span style=\"font-size: small;\">(in W)</span>", "PWM<br><span style=\"font-size: small;\">(out of 255)</span>", "Speed<br><span style=\"font-size: small;\">(in mm/min)</span>", "Iterations", "Remarks", "Date" ], [
        [ "<s>Plywood</s>", "<s>Birch</s>", "<s>3</s>", "<s>2.5</s>", "<s>255</s>", "<s>200</s>", "<s>5</s>", "<s>Not possible to remove.</s>", "<s>2022-11-24</s>" ],
        [ "Plywood", "Birch", "3", "2.5", "255", "200", "10", "Difficult to remove.", "2022-11-24" ],
        [ "Plywood", "Birch", "3", "2.5", "255", "200", "15", "Easily removable.", "2022-11-24" ],
        [ "Plywood", "Birch", "3", "2.5", "255", "200", "20", "Freely fell out.", "2022-11-24" ],
        [ "<s>Plywood</s>", "<s>Birch</s>", "<s>3</s>", "<s>2.5</s>", "<s>255</s>", "<s>500</s>", "<s>15</s>", "<s>Not possible to remove.</s>", "<s>2022-11-24</s>" ],
        [ "Plywood", "Birch", "3", "2.5", "255", "500", "20", "Difficult to remove.", "2022-11-24" ],
        [ "Plywood", "Birch", "3", "2.5", "255", "200", "15", "Difficult to remove.", "2022-11-25" ],
    ]
)
%-->

## More Pictures
<a class="anchor" name="more_pictures"></a>

<div class="collapse">Some more photographs I didn't use above.</div>
<div class="collapsecontent">
<!--%
lightgallery([
    [ "img/laser_tower_2.jpg", "Frontal view in Ikea Lack tower" ],
    [ "img/laser_cut_test_2.jpg", "Finished test run" ],
    [ "img/laser_gt2560.jpg", "GT2560 mainboard of laser engraver" ],
])
%-->
</div>
