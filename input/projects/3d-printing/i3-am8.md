title: i3 AM8
description: Rebuild of my i3 clone with aluminium extrusions, CoreXZ, Klipper
x-parent: 3d-printing
x-position: 25
x-date: 2022-02-01
x-update: 2022-06-10
x-comments: true
---

<!--% backToParent() %-->

In February 2022 I finally decided to re-build my [CTC i3 Pro B](ctc-i3.html) with an upgraded frame and better parts.
The following are the new integral components:

 * ["AM8 - Metal Frame for Anet A8" by pheneeny](https://www.thingiverse.com/thing:2263216) on Thingiverse
     * 2040 extrusions and nuts from [Dold Mechatronik](https://www.dold-mechatronik.de/Aluminiumprofil-20x40-I-Typ-Nut-5)
     * [Core XZ AM8 Conversion by 93djen](https://www.prusaprinters.org/prints/131210-core-xz-anet-am8-conversion) on PrusaPrinters.
 * [Sherpa Mini Extruder](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder) on GitHub
     * Sourced from [AliExpress](https://de.aliexpress.com/item/1005003671542821.html?gatewayAdapt=glo2deu&mp=1)
 * [NF Crazy Hotend](https://3dprintbeginner.com/nf-crazy-hotend-a-mosqutio-hotend-alternative/)
     * Clone of [Mosquito Hotend](https://www.sliceengineering.com/products/the-mosquito-hotend)
     * Contact [Mellow Store](https://de.aliexpress.com/store/1531088) on AliExpress to source it
 * [SKR Mini E3 v3.0 Mainboard](https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/tree/master/hardware/BTT%20SKR%20MINI%20E3%20V3.0)
 * [Fysetc Mini 128x64 LCD panel V2.1](https://wiki.fysetc.com/Mini12864_Panel/)
     * Cloned version by [BCZAMD on Amazon](https://amzn.to/3MaaJ6T)

Initially I simply wanted to re-use the mechanical parts from my old printer.
But after talking to my friend [Tobias](https://www.prusaprinters.org/social/199673-93djen/about) about the project, he came up with the idea to convert the AM8 into a CoreXZ machine, and also immediately delivered a complete design!
We selected the parts based on what I mostly still had lying around.

<!--%
lightgallery([
    [ "img/am8_corexz_1.png", "CAD screenshot of whole CoreXZ AM8"],
    [ "img/am8_corexz_2.png", "CAD screenshot of extruder / hotend"],
    [ "img/am8_corexz_3.png", "CAD screenshot of XZ gearbox"],
])
%-->

Other mechanical / electronical parts, like motors and the heatbed, I re-used from my previous printer.

## Custom 3D-Printed Parts

Mounts for PSUs, MOSFET, Mainboard, Pi, Relais.

TODO links, photos

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

TODO problems with encoder, kill button pullups?!

TODO photo(s) of cabling

<!--%
lightgallery([
    [ "img/am8_lcd_assy.jpg", "LCD mounted on printer" ],
])
%-->
