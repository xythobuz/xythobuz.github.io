title: i3 CoreXZ AM8
description: Rebuild of my i3 clone with aluminium extrusions, CoreXZ, Klipper
parent: 3d-printing
position: 10
date: 2022-10-08
update: 2023-08-31
comments: true
---

<!--% backToParent() %-->

In February 2022 I finally decided to re-build my [CTC i3 Pro B](ctc-i3.html) with an upgraded frame and better parts.
It took me quite some time, until September of 2022, to finally get it running properly.

<!--%
lightgallery([
    [ "img/am8_front.jpg", "Front view of completed printer"],
    [ "img/am8_left.jpg", "View of PCBs on left side"],
    [ "img/am8_right.jpg", "View of power supplies on right side"],
])
%-->

The following are the new integral components:

 * ["AM8 - Metal Frame for Anet A8" by pheneeny](https://www.thingiverse.com/thing:2263216) on Thingiverse
     * 2040 extrusions and nuts from [Dold Mechatronik](https://www.dold-mechatronik.de/Aluminiumprofil-20x40-I-Typ-Nut-5)
     * [Core XZ AM8 Conversion by 93djen](https://www.printables.com/model/131210-core-xz-anet-am8-conversion) on Printables.
 * [Sherpa Mini Extruder](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder) on GitHub
     * Sourced from [AliExpress](https://de.aliexpress.com/item/1005003671542821.html?gatewayAdapt=glo2deu&mp=1)
 * [NF Crazy Hotend](https://3dprintbeginner.com/nf-crazy-hotend-a-mosqutio-hotend-alternative/)
     * Clone of [Mosquito Hotend](https://www.sliceengineering.com/products/the-mosquito-hotend)
     * Contact [Mellow Store](https://de.aliexpress.com/store/1531088) on AliExpress to source it
 * [SKR Mini E3 v3.0 Mainboard](https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/tree/master/hardware/BTT%20SKR%20MINI%20E3%20V3.0)
 * [Fysetc Mini 128x64 LCD panel V2.1](https://wiki.fysetc.com/Mini12864_Panel/)
     * Cloned version by [BCZAMD on Amazon](https://amzn.to/3MaaJ6T)
 * [Magnetic Heatbed (Mk52 clone)](https://www.hta3d.com/en/magnetic-heated-bed-220x200mm-with-inserted-magnets-24v-similar-mk52-mk3)

Initially I simply wanted to re-use the mechanical parts from my old printer.
But after talking to my friend [Tobias](https://www.prusaprinters.org/social/199673-93djen/about) about the project, he came up with the idea to convert the AM8 into a CoreXZ machine, and also immediately delivered a complete design!
We selected the parts based on what I mostly still had lying around.

Other mechanical / electronical parts, like motors and the heatbed, I planned to re-use from my previous printer.
In the end that plan didn't quite work out and the only parts that are still "original" are my heatbed MOSFET and the webcam, everything else was replaced.

## Frame / CoreXZ

<!--%
lightgallery([
    [ "img/am8_front_top.jpg", "Front top view, without bed"],
    [ "img/am8_front_bottom.jpg", "Front bottom view, without bed"],
])
%-->

This is my first time going from simple i3-style mechanics to something more complicated, like CoreXY or CoreXZ.
It has some advantages and drawbacks.
I really like that leveling the Z-axis, or losing steps on only one of the two Z steppers, is a thing of the past.
Instead, now the rotation of the X-axis is determined by the relative tension of the two long belts.
Tensioning one of the belts, the corresponding side of the X-axis rises or lowers.
By using a simple [3D printed tool](https://www.printables.com/model/115460-belt-tension-gauge-source-file-included) the tension can be measured and dialed in relatively well.
For fine tuning, you can induce an oscillation on the belt with your finger and compare the pitch of the resulting sound.

<!--%
lightgallery([
    [ "img/am8_corexz_1.png", "CAD screenshot of whole CoreXZ AM8"],
    [ "img/am8_corexz_3.png", "CAD screenshot of XZ gearbox"],
])
%-->

At the beginning I had some problems getting the CoreXZ mechanism to work reliably.
It took me far longer than I'd like to admit to find the root issue.
The GT2 belt I ordered was not, in fact, a GT2 belt with 2mm pitch, but a T2.5 belt with 2.5mm pitch, and a slightly different tooth profile (square instead of rounded).
This was close enough so you don't immediately notice a problem, but still caused some slip on the axes.
This resulted in the axis dropping down in Z slightly with every move of the X axis.

## Hotend

<!--%
lightgallery([
    [ "img/am8_bltouch.jpg", "BL Touch clone on hotend" ],
    [ "img/am8_corexz_2.png", "CAD screenshot of extruder / hotend"],
])
%-->

I'm using a [Sherpa Mini Extruder](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder) together with an NF Crazy High-Flow hotend, both ordered from Mellow on AliExpress.
These are put on the x-carriage with only a 5015 fan for the filament, a 4020 fan for the hotend and a BL-Touch for auto-leveling.
This makes for a very lightweight carriage that can reach high accelerations and speeds.
And thanks to the v-rollers in the aluminium extrusion it moves very silently, as well.

<!--%
lightgallery([
    [ "img/am8_hotend.jpg", "Disassembled, clogged hotend"],
    [ "img/am8_heatbreak.jpg", "Disassembled, clogged heatbreak"],
])
%-->

I had some problems initially with the NF Crazy clogging with low layer heights.
This required some disassembly and cleaning of molten plastic.
After experimenting a bit, I found that I could easily hold the filament, with the extruder no longer able to pull it.
This turned out to be caused by the melt-in nut that holds the spring for the lever arm.
It was pulled out slightly from the body of the extruder, therefore causing a larger distance between both rollers.
Pushing in the nut as far as possible was enough to remedy the problem.
Although I suspect it may come back in the future.
Guess I have to re-print the extruder body until then.

## Heatbed

I initially hoped to re-use my old heatbed, but it turned out it is only compatible to 12V.
So I had to order a 24V variant.
I decided to go with this [Mk52 clone magnetic heatbed](https://www.hta3d.com/en/magnetic-heated-bed-220x200mm-with-inserted-magnets-24v-similar-mk52-mk3) from HTA3D.
The magnets in there are apparently good up to 140 degrees C.
I was able to re-use the coated spring-steel-sheet printing surface from my old printer.
It already came with a nice printed housing for the cable connections, and a Thermistor pre-installed.
I asked the vendor, it is an `EPCOS 100K B57560G104F` in Klipper, or option 1 in Marlin.

<!--%
lightgallery([
    [ "img/am8_bed_bottom.jpg", "Heatbed without insulation"],
    [ "img/am8_bed_conn.jpg", "Heatbed wiring"],
    [ "img/am8_bed_insulation.jpg", "Insulated Heatbed"],
])
%-->

Of course I put a piece of [insulation foam](https://www.hta3d.com/en/adhesive-thermal-insulation-for-heatedbed) on the bottom of the bed.
I installed it using some [flat 20mm springs](https://amzn.to/3ChnetC) on my [Y carriage](https://amzn.to/3CHQR8T).

<!--%
lightgallery([
    [ "img/am8_y_carriage.jpg", "Y Carriage without Heatbed"],
    [ "img/am8_bed_pcb.jpg", "Printer with Heatbed installed"],
    [ "img/am8_bed_spring.jpg", "Close view of Heatbed springs"],
])
%-->

## Custom 3D-Printed Parts

To install all the modules and PCBs to the frame I decided to design some simple mounting plates for myself.

<!--%
lightgallery([
    [ "img/am8_mounts_1.jpg", "View of PCB mounts"],
    [ "img/am8_mounts_2.jpg", "View of PSU mounts"],
])
%-->

You can find these files [on my Printables profile](https://www.printables.com/model/291049-mounting-plates-for-am8) or [in my Git repo](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/am8).

## Power Supply Wiring

I added two power supplies to the printer.
One is +5V, solely for powering the Raspberry Pi, and it is always on.
The other is +24V, for running the printer itself. This is switched by a relais module, connected to the Pi.

I'm not entirely comfortable with the 220V wiring, so I <s>added</s> plan to add an enclosure that should prevent any shock hazards from touching.

<!--%
lightgallery([
    [ "img/am8_psu.jpg", "Power supply cabling"],
])
%-->

As a small quality-of-life improvement I put a piece of shrink wrap tubing over the indicator LED of the +24V supply.
I don't understand why the manufacturer decided to put an unbelievably bright blue LED on there... 🤦

In an attempt to avoid any ground loops and power supplies driving each other, I decided not to connect the Pi and the Mainboard using USB.
Instead I ran a cable between them, only connecting GND and the UART Rx and Tx lines.
This is the only place where the grounds of the +5V and +24V supply are connected.
The mainboard is not fed any external +5V.

As I've re-used 12V fans from my old printer, I had to add a small PCB with a 24V -> 12V converter to power them.
I simply used a small LM2596 module soldered onto a perf-board with some connectors.
The mainboard switches GND for all accessories, so using 12V fans is as simple as connecting the negative lead to the mainboard connector, and the positive lead to +12V instead of the mainboard connector.

## LCD Connection

On a whim, I decided to get a [Fysetc 12864](https://wiki.fysetc.com/Mini12864_Panel/) clone.
Only later I realized that it is not really compatible with my chosen mainboard, as it does not have the standard EXP1/EXP2 connectors.
Fortunately this can be [fixed easily](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Maverick_/V0_TopHat_Mini_12864), you just need to connect the required pins to free IO pins of the mainboard.
I decided to ignore the SD card interface, as I won't be using it and the mainboard has one as well.
So only the LCD and rotary encoder pins are required.
My LCD board also has some RGB LEDs, so I decided to wire them up as well.
The other question concerns the cabling.
The standard 2x 10pin ribbon cables are hard to route and prone to interference.
Counting the required pins, and looking at my cable stash, I decided to simply use some Cat5 ethernet cabling.
With 8 cores per cable I only had to use two pieces in parallel.

Configuring it correctly turned out to be a bit tricky.
Initially I thought I had [hardware revision 1.2](https://github.com/FYSETC/FYSETC-Mini-12864-Panel/blob/master/hardware/V1.2/mini12864%E5%8E%9F%E7%90%86%E5%9B%BE.pdf), based on the reviews on Amazon, with plain RGB LEDs on board.
But I couldn't get anything to light up, neither around the encoder nor the LCD backlight.
That's when I took a closer look and saw the WS2811 chips on the LCD PCB (and later also the revision printed on it 😅).
Turns out I actually have [revision 2.1](https://github.com/FYSETC/FYSETC-Mini-12864-Panel/blob/master/hardware/V2.1/Mini12864%EF%BC%88RGB%EF%BC%89V2.1_sch.pdf).

One thing you should check before using a display like this: the RST and KILL pins and their respective resistors.
The push button on the front of the LCD panel can be connected to either the RST or KILL pin.
If you do a custom cabling, like I did, it doesn't really matter which one of these you choose.
But my display only came with R3 installed, which I didn't notice at first.
Because I wired up the KILL pin instead of using RST, I would have needed R4 instead of R3.
I decided to simply switch out the 0Ω-link.
The other resistor, R1, is also important.
It should **not** be populated, otherwise the display will feed +5V back to the GPIOs of the MCU, which are only 3.3V tolerant.

<!--%
lightgallery([
    [ "img/am8_lcd_rst_kill.png", "Schematic of LCD reset / kill pins"],
    [ "img/am8_lcd_pre_op.jpg", "Back of LCD, before reset fix" ],
    [ "img/am8_lcd_post_op.jpg", "Back of LCD, after reset fix" ],
])
%-->

To mount the LCD to my frame I used ["Mini 12864 LCD Display Housing for 2020 V-Slot" by derebbe](https://www.printables.com/model/56150-mini-12864-lcd-display-housing-for-2020-v-slot).
You need to replace the kill button on the panel with a shorter one for this model to work.

<!--%
lightgallery([
    [ "img/am8_lcd_front.jpg", "Front of LCD, with new button" ],
])
%-->

This was the first time I tried to solder to ethernet cable.
It seems to have some kind of coating that makes it not only hard to wet with tin,
it also corroded one of my soldering tips pretty strongly.
Not all connections were good, and I had some issues with the LCD not displaying anything after a short time.

<!--%
lightgallery([
    [ "img/am8_lcd_assy.jpg", "LCD mounted on printer" ],
    [ "img/am8_lcd_cable.jpg", "LCD cabling" ],
])
%-->

For all other cables I tried to route them nicely as well.

<!--%
lightgallery([
    [ "img/am8_mainboard.jpg", "Mainboard with cabling" ],
    [ "img/am8_right_cables.jpg", "Cables on right side" ],
    [ "img/am8_back_cables.jpg", "Cables on back side" ],
    [ "img/am8_left_cables.jpg", "Cables on left side" ],
])
%-->

## Klipper Firmware

After hearing many good things about Klipper from Tobias and others, I really had to try it out myself.
And I have to admit, even though I didn't believe it at first, it's much better than Marlin in many areas, even for non-fancy printers like mine.

I'm using [MainsailOS](https://docs.mainsail.xyz/setup/mainsail-os) on a Raspberry Pi 3B.
Installation and Configuration was really straight-forward with the configuration guides of [Klipper](https://www.klipper3d.org/Config_Reference.html) and [Mainsail](https://docs.mainsail.xyz/setup/mainsailos/first-boot).
I also installed the [Moonraker Telegram Bot](https://github.com/nlef/moonraker-telegram-bot/wiki/installation) according to their installation instructions.

With one of my first print attempts I ran into the "Rescheduled timer in the past" error message.
Turns out there was a [bug in the microcontroller firmware](https://klipper.discourse.group/t/stm32g0-users-should-update-to-latest-klipper/3612), so I had to upgrade that, even though thats apparently not needed normally for all updates.

<!-- https://clay-atlas.com/us/blog/2021/06/30/html-en-copy-text-button/ -->
<script>
function copyEvent(id) {
    var str = document.getElementById(id);
    window.getSelection().selectAllChildren(str);
    document.execCommand("Copy")
}
</script>

[Here](https://git.xythobuz.de/thomas/3d-print-designs/raw/branch/master/configs/i3-AM8/printer.cfg) is my current `printer.cfg` file.
<button type="button" onclick="copyEvent('printercfg')" class="clip-btn">Copy 'printer.cfg' to clipboard</button>

<pre id="printercfg" class="sh_desktop">
<!--%
include_url("https://git.xythobuz.de/thomas/3d-print-designs/raw/branch/master/configs/i3-AM8/printer.cfg")
%-->
</pre>

[Here](https://git.xythobuz.de/thomas/3d-print-designs/raw/branch/master/configs/i3-AM8/moonraker.conf) is my current `moonraker.conf` file.
<button type="button" onclick="copyEvent('moonrakerconf')" class="clip-btn">Copy 'moonraker.conf' to clipboard</button>

<pre id="moonrakerconf" class="sh_desktop">
<!--%
include_url("https://git.xythobuz.de/thomas/3d-print-designs/raw/branch/master/configs/i3-AM8/moonraker.conf")
%-->
</pre>

And [here](https://git.xythobuz.de/thomas/3d-print-designs/raw/branch/master/configs/i3-AM8/PrusaSlicer_config_bundle.ini) is my PrusaSlicer config bundle.
<button type="button" onclick="copyEvent('prusabundle')" class="clip-btn">Copy PrusaSlicer config to clipboard</button>

<pre id="prusabundle" class="sh_desktop">
<!--%
include_url("https://git.xythobuz.de/thomas/3d-print-designs/raw/branch/master/configs/i3-AM8/PrusaSlicer_config_bundle.ini")
%-->
</pre>
