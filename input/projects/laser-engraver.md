title: Laser Engraver
description: Marlin based CNC laser engraver with 3D printed parts
x-parent: projects
git: https://git.xythobuz.de/thomas/marlin/src/branch/laser-engraver
x-date: 2022-11-11
comments: true
---

After dabbling in 3D printing for a couple of years now, I now had to level-up my Makers toolkit.
The next logical step, in my opinion, is laser engraving / laser cutting.
I have to admit, I was initially a bit scared, and still have some respect for the potential hazards posed by the strong and focussed laser beam.
So I decided to go slow and start with a low powered diode laser.

⚠️ Be sure to always use proper laser safety goggles when working with such machines! ⚠️

## Hardware

I know I say this in a lot of articles here, probably in an attempt to justify my hoarding of electronic parts. 😳
But this was even better than most of my previous projects, in the sense that I didn't have to buy any parts at all, except for the 2500mW 450nm laser diode, which I got used from my colleague [Philipp](https://www.phschoen.de/) for just 13€.
The rails I bought many years ago and never used.
The steppers, mainboard, display, fans and cables came from my now disassembled [CTC i3](ctc-i3.html).
Everything else came out of my parts bin.

### Mechanics

The mechanism is based on the ["Cantilever Laser Engraver" by Meatball](https://www.printables.com/model/213526-cantilever-laser-engraver).
This in turn is based on the ["Cantilever Laser Engraver" by GeoDave](https://www.thingiverse.com/thing:4605853).
It uses 2020 aluminium extrusions with V-slot wheels for the X and Y axis.

I really like this simple design that does not require a lot of parts.
It has some problems with twisting of the Y-rail due to the weight hanging from the cantilever arm, but this can easily be solved by supporting the free-hanging side of the X-rail.
Otherwise the length of the axes can be customized freely.

<!--%
lightgallery([
    [ "img/laser_frame.jpg", "Frame of laser engraver, made of 2020 rails" ],
])
%-->

I had to do some modifications to the design files provided by Meatball.

The "Y-Axis Gantry Upper" has enlargened the holes for two of the four wheels, to be able to fit eccentric nuts that provide the required tensioning on the wheels.
The "Y-Axis Gantry Lower" however has normal sized holes.
So when using these parts, the two wheels are not actually moved perpendicular towards the extrusion, but are instead angled sideways.
To avoid this problem I made the two holes in the lower bigger as well and used four instead of two eccentric nuts.
I also slightly increased the distance between the two sets of wheels on the Y-axis, because it was very hard to fit the rail, even with the eccentric nuts as loose as possible.

I also designed custom endstop mounts using M2.5 heat-melt inserts, as well as a support wheel for the free-hanging side of the cantilever arm.

The OpenSCAD and STL files for these parts [can be found on my Printables profile](https://www.printables.com/model/314945-cantilever-laser-engraver-fixes).

### Electronics

As mentioned above I used the electronics, namely mainboard, LCD and fans, from my old 3D printer.

<!--%
lightgallery([
    [ "img/laser_lcd.jpg", "LCD mounted to laser engraver" ],
    [ "img/laser_gt2560.jpg", "GT2560 mainboard of laser engraver" ],
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

## Software

### MCU Firmware

Most DIY laser engravers or CNC machines seem to use the [GRBL firmware](https://github.com/gnea/grbl).
Unfortunately this firmware only runs on Atmega328p MCUs, so I can not use it with the Atmega2560 on the GT2560 mainboard.
There are some GRBL ports, for [ESP32](https://github.com/bdring/Grbl_Esp32) or [STM32](https://github.com/thomast777/grbl32) microcontrollers, but obviously these don't help either in my situation.

So I decided to use the trusty old [Marlin Firmware](https://marlinfw.org/), which was already running previously on my old 3D printers and this mainboard.
Configuring Marlin is pretty straight-forward, there's a [configuration guide](https://marlinfw.org/docs/configuration/configuration.html) but the settings in the two config header files are well commented and pretty much self explanatory.
The only interesting parts are the laser-specific settings in `Configuration_adv.h`, like `LASER_FEATURE` and `LASER_POWER_SYNC`.

Apparently I seem to be the first person that tries to run an Ultimaker Controller 2004 LCD without a Z-Axis.
I had to add a couple of `#ifdef Z_AXIS` in `src/lcd/HD44780/marlinui_HD44780.cpp`.

You can see all the modifications to the configuration I initially made to get the machine running [in this commit](https://git.xythobuz.de/thomas/marlin/commit/41cd87398d539f41c2ebe54b5f675c6c8b5ce04b).
My current Marlin configuration for the laser engraver can be found [on my Gitea instance](https://git.xythobuz.de/thomas/marlin/src/branch/laser-engraver).

### Host Software

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
To get this to work, the "continuous inline power mode" has to be enabled by putting `M3 I` in the G-Code header setting of LaserGRBL.

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

<pre class="sh_python">
#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
    print("Usage:")
    print("    " + sys.argv[0] + " input.nc output.gcode")
    sys.exit(1)

in_file = sys.argv[1]
out_file = sys.argv[2]

power = ""
speed = ""

with open(in_file, 'r') as fi, open(out_file, 'w') as fo:
    for line in fi:
        if line.startswith("S"):
            power = " " + line.rstrip()
        elif line.startswith("F"):
            speed = " " + line.rstrip()
        else:
            s = line.rstrip()
            if line.startswith("G1"):
                s += power
                s += speed
            elif line.startswith("G0"):
                s += power
                if (power != " S0") and (power != ""):
                    print("Warning: G0 move with power not zero!" + power)
            s += "\n"
            fo.write(s)
</pre>

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
I also had to reduce the polling frequency in the LaserGRBL settings to 'Quiet' and disable Soft-Reset to get it to work inside the VirtualBox VM I use to run the program.

Apparently it is also possible to [run LaserGRBL in Wine](https://github.com/arkypita/LaserGRBL/issues/5#issuecomment-873564055) / [with PlayOnLinux](https://github.com/arkypita/LaserGRBL/raw/master/POL_LaserGRBL_setup.sh), but on my Arch system I was not able to get either of these running, due to problems with the required Winetricks.

Also, for all the above tests with LaserGRBL I have imported raster bitmap images and either rastered them, or vectorized them within LaserGRBLs UI.
With bitmaps it is possible to position the resulting G-Code paths with an offset from the zero position of the machine.
This is not possible when using LaserGRBL to import SVG vector paths.
With them, the output will always start at coordinates `(0, 0)`.
You will then have to set the proper offset on the machine itself.

#### Inkscape

Inkscape includes the [G-Code Tools Plugin from the russian-language CNC-Club forums](https://www.cnc-club.ru/forum/viewtopic.php?t=35).
Unfortunately I was not able to find much up-to-date english-language documentation for this.
It is also relatively complicated and unintuitive.

TODO

I was able to get it to generate G-Code from a path, but not with any laser power instructions yet.

#### FreeCAD

FreeCAD has the [Path Workbench](https://wiki.freecadweb.org/Path_Workbench), which can be used to create G-Code instructions for all kinds of CNC machines.
It is not really complete and fool-proof yet, unfortunately.
And it is also not designed for pure 2D machines, like laser engravers, by default.

TODO

I have not yet tested that.

#### Generating G-Code

I also did some experimentation with programatically generating G-Code myself, using a simple Python script.
It's drawing a grid for reference on the base plate of the machine, including numerical position indicators.

<pre class="sh_python">
#!/usr/bin/env python

filename = "grid.gcode"
w = 200
h = 280
d = 10
pwr = 100
speed_g0 = 3000
speed_g1 = 1000

digits = [
    [
        # 0
        (0.0, 0.0),
        (0.0, 1.0),
        (1.0, 1.0),
        (1.0, 0.0),
        (0.0, 0.0)
    ], [
        # 1
        (0.5, 0.0),
        (0.5, 1.0)
    ], [
        # 2
        (0.0, 1.0),
        (1.0, 1.0),
        (1.0, 0.5),
        (0.0, 0.5),
        (0.0, 0.0),
        (1.0, 0.0),
    ], [
        # 3
        (0.0, 1.0),
        (1.0, 1.0),
        (1.0, 0.5),
        (0.0, 0.5),
        (1.0, 0.5),
        (1.0, 0.0),
        (0.0, 0.0),
    ], [
        # 4
        (0.0, 1.0),
        (0.0, 0.5),
        (1.0, 0.5),
        (1.0, 1.0),
        (1.0, 0.0),
    ], [
        # 5
        (1.0, 1.0),
        (0.0, 1.0),
        (0.0, 0.5),
        (1.0, 0.5),
        (1.0, 0.0),
        (0.0, 0.0),
    ], [
        # 6
        (1.0, 1.0),
        (0.0, 1.0),
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 0.5),
        (0.0, 0.5),
    ], [
        # 7
        (0.0, 1.0),
        (1.0, 1.0),
        (1.0, 0.0),
    ], [
        # 8
        (1.0, 0.5),
        (1.0, 1.0),
        (0.0, 1.0),
        (0.0, 0.5),
        (1.0, 0.5),
        (1.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.5),
    ], [
        # 9
        (1.0, 0.5),
        (1.0, 1.0),
        (0.0, 1.0),
        (0.0, 0.5),
        (1.0, 0.5),
        (1.0, 0.0),
        (0.0, 0.0),
    ]
]

font_w = 1.5
font_h = 3.0
font_d = 0.5

def draw_digit(f, i, sx, sy, ox, oy):
    dig = digits[i]
    n = 0
    for p in dig:
        x, y = p
        s = ""

        if n == 0:
            s += "G0 S0 F" + str(speed_g0)
        else:
            s += "G1 S" + str(pwr) + " F" + str(speed_g1)

        s += " X" + str(ox + sx * x)
        s += " Y" + str(oy + sy * y)

        print(s)
        f.write(s + "\n")
        n += 1

    return s

with open(filename, 'w') as f:
    def write(s):
        print(s)
        f.write(s + "\n")

    # header
    write("G90")
    write("M3 I")
    write("M3 S0")

    # first line is not having the power applied
    # so just draw it twice
    # TODO why?
    write("G0 X0 Y0 S0 F" + str(speed_g0))
    write("G1 X0 Y" + str(h) + " S" + str(pwr) + " F" + str(speed_g1))

    # vertical lines
    for x in range(0, w + d, d):
        write("G0 X" + str(x) + " Y0 S0 F" + str(speed_g0))
        write("G1 X" + str(x) + " Y" + str(h) + " S" + str(pwr) + " F" + str(speed_g1))

    # horizontal lines
    for y in range(0, h + d, d):
        write("G0 X0 Y" + str(y) + " S0 F" + str(speed_g0))
        write("G1 X" + str(w) + " Y" + str(y) + " S" + str(pwr) + " F" + str(speed_g1))

    for x in range(0, w, d):
        n = int(x / 1)
        if n >= 10:
            draw_digit(f, int(n / 10), font_w, font_h, font_d + x, font_d)
            draw_digit(f, int(n % 10), font_w, font_h, 2 * font_d + font_w + x, font_d)
        else:
            draw_digit(f, n, font_w, font_h, font_d + x, font_d)

    for y in range(d, h, d):
        n = int(y / 1)
        if n >= 10:
            draw_digit(f, int(n / 10), font_w, font_h, font_d, font_d + y)
            draw_digit(f, int(n % 10), font_w, font_h, 2 * font_d + font_w, font_d + y)
        else:
            draw_digit(f, n, font_w, font_h, font_d, font_d + y)

    # footer
    write("M5")
    write("G0 X0 Y0 F" + str(speed_g0))
</pre>
