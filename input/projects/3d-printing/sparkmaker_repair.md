title: Reviving an old Sparkmaker SLA printer
description: Fixing the hardware and creating a free-software slicing workflow
parent: 3d-printing
position: 35
git: https://git.xythobuz.de/thomas/gcode-tools
date: 2023-01-03
update: 2023-02-26
comments: true
---

<!--% backToParent() %-->

Many years ago someone donated his Sparkmaker SLA printer to our local makerspace, the [Toolbox Bodensee](https://toolbox-bodensee.de).
Nobody has touched it for a long time, mostly because we were not keen to work with the poisonous and stinky UV resin required for the printer.
But recently my friend [Philipp](https://www.phschoen.de) and I took the plunge.
Here I describe what we had to do to get it working.

<!--%
lightgallery([
    [ "img/sparkmaker_17.jpg", "Sparkmaker SLA printer" ],
    [ "img/sparkmaker_shelf_1.jpg", "Sparkmaker and tools on shelf" ],
])
%-->

### Table Of Contents

* [Endstop Fix](sparkmaker_repair.html#endstop)
* [Encoder Replacement](sparkmaker_repair.html#encoder)
* [First Slicing Experiments](sparkmaker_repair.html#experiments)
* [SL1 to WOW File Format Converter Script](sparkmaker_repair.html#script)
* [Configuring PrusaSlicer for the Sparkmaker](sparkmaker_repair.html#prusaslicer)
* [Shelf Space (February 2023)](sparkmaker_repair.html#shelf_space)
* [More Pictures](sparkmaker_repair.html#more_pictures)

## Endstop Fix
<a class="anchor" name="endstop"></a>

The printer only has a single axis, Z, with an optical endstop switch at the bottom.
This switch is triggered by a large plastic shim screwed to the Z carriage.
This shim was not centerd properly on this machine.
So when trying to home, the shim collided with the housing of the switch, blocking the axis and threatening to rip off the switch.
To fix this, just loosen the two screws in the shim and adjust the position.
Both the shim and the print bed have some range of adjustment in the Z axis, so take care to adjust the shim in a way to still allow the bed to be properly leveled.

<!--%
lightgallery([
    [ "img/sparkmaker_2.jpg", "Endstop trigger shim" ],
])
%-->

## Encoder Replacement
<a class="anchor" name="encoder"></a>

After only a couple of hours of use, the encoder at the front of the machine stopped working properly.
You can see this in the video below.

<!--%
lightgallery([
    [ "img/sparkmaker_20.mp4", "video/mp4", "", "", "Demo of encoder problem" ],
])
%-->

It stopped moving up, mostly only moving down, regardless of the direction it was turned.
This meant the bed could no longer be lifted to easily remove it.
I decided to replace it with an ALPS encoder ([STEC12E](https://www.reichelt.de/drehimpulsegeber-24-impulse-24-rastungen-vertikal-stec12e08-p73923.html?&nbc=1)) I still had lying around from repairing my oscilloscope a while back.

<!--%
lightgallery([
    [ "img/sparkmaker_3.jpg", "Removing resin basin" ],
    [ "img/sparkmaker_5.jpg", "Mainboard with LCD connector" ],
    [ "img/sparkmaker_6.jpg", "Motor connector" ],
    [ "img/sparkmaker_8.jpg", "UV LED board" ],
])
%-->

This requires removing the base of the housing by unscrewing the outer four hex screws from the top, as well as the three hex screws on the bottom below the Z axis arm.
Now we are allowed access to the encoder board.

<!--%
lightgallery([
    [ "img/sparkmaker_9.jpg", "Encoder board" ],
    [ "img/sparkmaker_10.jpg", "Encoder board backside" ],
    [ "img/sparkmaker_11.jpg", "New encoder next to board" ],
    [ "img/sparkmaker_12.jpg", "Fixed encoder board" ],
])
%-->

The new encoder apparently does not have the same number of pulses per indent, so adjusting it still feels slightly weird.
But it can now be turned normally in both directions, so it is usable again.

<!--%
lightgallery([
    [ "img/sparkmaker_14.jpg", "Closer view of MCU on mainboard" ],
    [ "img/sparkmaker_15.jpg", "Replacing the screws required a tool to push the nuts in" ],
    [ "img/sparkmaker_16.jpg", "Showing some example image on the LCD" ],
])
%-->

With the hardware back in working order I could now focus on the PC software side of things.

## First Slicing Experiments
<a class="anchor" name="experiments"></a>

After getting the hardware back running the next step is generating some sliced files.
Unfortunately the official Sparkmaker website no longer exists and the downloads from there are hard to find.
They included a slicing software of course, but it seems to only run on Windows and Macs and it not open source.
So I had to find some alternative.
Most suggest using [ChituBox](https://www.chitubox.com) or [Lychee Slicer](https://mango3d.io/lychee-slicer-for-sla-3d-printers/), both can be used for free and seem to include presets for the Sparkmaker.

<!--%
lightgallery([
    [ "img/sparkmaker_22.jpg", "Cleaning the LCD screen" ],
    [ "img/sparkmaker_23.jpg", "The Anycubic resin we have been using" ],
])
%-->

Philipp installed ChituBox on his machine and tried it out.
It includes presets for the Sparkmaker that seem to work more or less.
And the software also allows comfortable placement of support structures.
But it didn't work perfectly all the time, we got at least one corrupted file where each slice contained the same garbage picture.

<!--%
lightgallery([
    [ "img/sparkmaker_24.jpg", "Front view of first print" ],
    [ "img/sparkmaker_25.jpg", "Side view of first print" ],
    [ "img/sparkmaker_26.jpg", "Bottom view of first print" ],
])
%-->

Even though one corner was warping strongly, the results of the first print attempt were promising.
It is an SA-profile keycap, sliced with ChituBox with 0.1mm layer height.

## SL1 to WOW File Format Converter Script
<a class="anchor" name="script"></a>

But there is one open-source alternative, [PrusaSlicer](https://github.com/prusa3d/PrusaSlicer), and it has support for SLA slicing for the [Prusa SL1 printer](https://www.prusa3d.com/product/original-prusa-sl1s-speed-3d-printer/).
But it only produces `.sl1` files, their custom file format.
The Sparkmaker, on the other hand, expects `.wow` files.
Fortunately someone already [documented the file format well](https://github.com/bastirichter/Sparkmaker/blob/master/file_format.md).
And there's also a [small GUI utility](https://github.com/Godzil/WoWTools) to visualize and modify pre-sliced `.wow` files.
The Prusa file format was easy to "reverse-engineer", it's just a zip archive containing each slice as a `.png` file, and some settings in `.ini` files.

The route to take was therefore obvious: write a script that takes `.sl1` files and converts them to `.wow`.

<pre class="sh_python">
<!--%
include_url("https://git.xythobuz.de/thomas/gcode-tools/raw/branch/master/tools/convert_sparkmaker.py")
%-->
</pre>

You can find it [on my Gitea server](https://git.xythobuz.de/thomas/gcode-tools/src/branch/master/tools/convert_sparkmaker.py).

This is what running the script looks like.

<pre class="sh_sh">
$ convert_sparkmaker MGMKII_PrintOnePiece.sl1 mgmk2.wow
Internal name: "MGMKII_PrintOnePiece"
Found 414 slices
Using following parameters:
{'exposure_time': 15.0,
 'first_exposure_time': 120.0,
 'first_layer_height': 0.1,
 'layer_height': 0.1,
 'lift_height': 5.0,
 'lift_speed': 30.0,
 'sink_speed': 100.0}
Height: 41.400mm
Estimated print time: 3h 14m 32s
Writing output to "mgmk2.wow"
</pre>

I only noticed after writing this script that [someone already did the same thing two years ago](https://github.com/PolSerg/sparkmaker).

<!--%
lightgallery([
    [ "img/sparkmaker_18.jpg", "First print sliced with PrusaSlicer" ],
    [ "img/sparkmaker_19.jpg", "Post-Curing a printed object" ],
])
%-->

Thanks to the documentation linked above, writing a `.wow` file was very easy.
I'm taking all the settings I can from the included `.ini` files, which are layer height, initial layer height, exposure time and initial exposure time.
The settings referring to the lift of the object after each slice are not present in the file, so my script has useful defaults hard-coded.

The script should also be usable for the Sparkmaker FHD, as it apparently uses the same file format.
Of course the resolution and size need to be adjusted accordingly, both in my script and in the slicer.

I noticed some interesting quirks of the printer firmware.
It does not allow the usual style of inline comments explaining what a line does.
When I tried adding comments to the commands in the G-Code header, the corresponding commands simply were not executed at all, which is obviously very problematic.

Also the firmware does not hestitate to display both success messages at the end of a print, as well as error messages, on the LCD screen itself!
When the LEDs are on this of course hardens the message into the resin.
So G-Code always needs to take care to turn the LEDs off at the end of a print.
For some reason we once managed to have the LEDs turned on with an error message showing.
This requires draining the resin and scraping off any remaining bits.

## Configuring PrusaSlicer for the Sparkmaker
<a class="anchor" name="prusaslicer"></a>

To configure PrusaSlicer I recommend starting out with their built-in profile for the SL1.
Selecting it as the machine automatically switches the program over into "SLA mode", where the support and pad generation work differently compared to the normal FDM mode.
You also need to enable expert mode to see all required settings.

<!--%
lightgallery([
    [ "img/sparkmaker_27.png", "Printer Settings page in PrusaSlicer" ],
    [ "img/sparkmaker_28.png", "Material Settings page in PrusaSlicer" ],
    [ "img/sparkmaker_29.png", "Print Settings page in PrusaSlicer" ],
])
%-->

The most important changes need to happen in the Printer Settings.
There you need to adjust the display size to 854x480, the display size to 98.57x54.99mm, maximum height to 120mm, the orientation to landscape and disable all mirroring.

In the Material Settings I recommend setting the exposure time to 15s and the initial exposure time to 120s.
But this may change depending on the resin you plan to use.

I'm not 100% sure about the display size, and of course this parameter is very important to ensure the printed objects have the correct size.
I initially found [this unfinished project](https://github.com/n0sr3v/SLAcer.js) where the display diagonal is given as 4.6 inch.
With this, and the display size in pixels, I calculated the theoretical display size.

    screen width = 854 * 4.6 / sqrt(854^2 + 480^2) = 4.0099996503 inch = 101.854mm
    screen height = 480 * 4.6 / sqrt(854^2 + 480^2) = 2.25386397207 inch = 57.248mm

This is close, but the resulting objects were not quite perfect.
So I printed a calibration cube at 5mm width, and one at 10mm width, to be able to calibrate the values.
This gave similar correction factors in both axes.

    101.854mm * 0.98 = 99.81692mm
    57.248mm * 0.98 = 56.10304mm

With these I printed another calibration cube, this time with 20mm, to be able to measure it with more accuracy.
Now I got these correction factors, as the cube was still a little bit too small.

    99.8169mm * 0.9875 = 98.56918875mm
    56.103mm * 0.99 = 55.54197mm

Now the X axis measured spot-on at 20mm, but the Y axis still only gave 19.8mm.
So I corrected it again.

    55.54197mm * 0.99 = 54.9865503mm

To be honest, I'm not sure why this calibration took so many attempts, or what I'm doing wrong.
I'm also sure these numbers are still not totally exact, but they seem to be close enough for my purposes.

For the Z axis I arrived at a correction factor of 0.995, which can be set in PrusaSlicer as "Printer scaling correction Z".

You can [download my PrusaSlicer configuration for the Sparkmaker](files/config_sparkmaker.ini) or even for [all of my printers](files/PrusaSlicer_config_bundle.ini), if you're so inclined.

As a test I printed [this model](https://www.printables.com/model/296411-metal-gear-mk-ii-from-game-metal-gear-solid-4), scaled down to 50% with a layer height of 0.1mm.
This took about 3½ hours.
For an early test I'm really happy with the results.
Even scaled down the very fine connections between the body and head are strong enough to hold them together.

<!--%
lightgallery([
    [ "img/sparkmaker_30.jpg", "Calibration cubes in 5mm, 10mm and 20mm" ],
    [ "img/sparkmaker_21.jpg", "Small Metal Gear Mk. II figurine" ],
])
%-->

## Shelf Space (February 2023)
<a class="anchor" name="shelf_space"></a>

I still had some drawer rails and a wooden plate left over from replacing my [Fabrikator Mini](fabrikator-mini.html) with my new [Laser Engraver](laser-engraver.html) in my [Ikea Lack tower](ikea-lack.html).
So I decided to re-use these to properly store the Sparkmaker.

<!--%
lightgallery([
    [ "img/sparkmaker_shelf_1.jpg", "Sparkmaker and tools on shelf" ],
    [ "img/sparkmaker_shelf_2.jpg", "Sparkmaker shelf, right side" ],
    [ "img/sparkmaker_shelf_3.jpg", "Sparkmaker shelf, left side" ],
])
%-->

The [drawer rails](https://amzn.to/41pvjYV) are 300mm long, 45mm high and have a spring mechanism for soft closing.

To fit the drawer parts I had to print six additional spacers.
The design for these can be whipped out very quickly using OpenSCAD:

<pre class="sh_javascript">
od = 12;
id = 5;
h = 5;
$fn = 42;

difference() {
    cylinder(d = od, h = h);

    translate([0, 0, -1])
    cylinder(d = id, h = h + 2);
}
</pre>

<!--%
lightgallery([
    [ "img/sparkmaker_shelf_5.jpg", "Sparkmaker shelf, spacers" ],
])
%-->

For easier pulling I added the ["Solid Drawer Handle" by dodasch](https://www.printables.com/model/308296-solid-drawer-handle), scaled down to a height of 16mm.

<!--%
lightgallery([
    [ "img/sparkmaker_shelf_4.jpg", "Sparkmaker shelf, handle" ],
])
%-->

Like with my laser engraver the power supply is hidden on the top of the shelf unit.

This setup provides enough space for storage of the printer, resin and the usual tools.

I'm now using an air-tight container filled with isopropanol to clean the prints.
The only thing still missing is a good solution for curing / hardening.
I'm thinking of some kind of small turntable and UV lamp or LED strip.
That's still to come, so stay tuned! 🧐

## More Pictures
<a class="anchor" name="more_pictures"></a>

<div class="collapse">Some more photographs I didn't use above.</div>
<div class="collapsecontent">
<!--%
lightgallery([
    [ "img/sparkmaker_1.jpg", "Badly lit look at endstop trigger" ],
    [ "img/sparkmaker_4.jpg", "Badly lit look into printer body" ],
    [ "img/sparkmaker_7.jpg", "Badly lit look at UV LEDs" ],
    [ "img/sparkmaker_13.jpg", "Badly lit look at mainboard" ],
])
%-->
</div>
