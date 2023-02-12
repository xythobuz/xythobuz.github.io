title: Trackball
description: 3D printed mouse replacement with Raspberry Pi Pico and PMW3360
parent: input_devices
git: https://git.xythobuz.de/thomas/Trackball
github: https://github.com/xythobuz/Trackball
date: 2023-02-12
comments: true
---

<!--% backToParent() %-->

For some years I have been using Trackballs from Logitech, first the [M570](https://amzn.to/3XhSuRO) and then the [MX Ergo](https://amzn.to/3xdp3pd).
But of course we could also build our own!

So because [Philipp](https://www.phschoen.de/) and I were already looking into building a keyboard with a trackball included, I decided to first get my feet wet by building a stand-alone version.

<!--%
lightgallery([
    [ "img/trackball_v1_27.jpg", "Front of second version" ],
    [ "img/trackball_v1_33.jpg", "Inside view of second version" ],
    [ "img/trackball_v1_12.jpg", "First completed Trackball" ],
])
%-->

It's made with a PMW3360 optical mouse sensor and a Raspberry Pi Pico.
The case is 3D printed and was designed in OpenSCAD.

<!--%
lightgallery([
    [ "img/trackball_scad_2.png", "Explosion drawing of assembled parts" ],
    [ "img/trackball_scad_1.png", "Close up view of lens distancing and roller holder" ],
])
%-->

As usual the project is released as free and open-source software / hardware.
You can find everything you need to build it yourself in [the git repository](https://git.xythobuz.de/thomas/Trackball)!

### Table Of Contents

 * [Part Selection](trackball_v1.html#part_selection)
 * [3D Design](trackball_v1.html#3d_design)
 * [Firmware Development](trackball_v1.html#firmware_devel)
 * [Wiring](trackball_v1.html#wiring)
 * [Sensor Problems](trackball_v1.html#sensor_problems)
 * [First Prototype](trackball_v1.html#first_prototype)
 * [Improvements](trackball_v1.html#improvements)
 * [User Experience](trackball_v1.html#user_experience)
 * [License](trackball_v1.html#license)
 * [More Pictures](trackball_v1.html#more_pictures)

## Part Selection
<a class="anchor" name="part_selection"></a>

Before embarking on this project some decisions and orders had to be made.

To control everything I decided to go with the [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) / [RP2040](https://www.raspberrypi.com/products/rp2040/) microcontroller board.
It is the hot new thing on the block and I wanted to try out both the hardware and the SDK.
It's also used extensively in the DIY keyboard community and already has great support in lots of open source software.

Another big question was which mouse sensor to use.
There are different types of sensor, either "optical" using an IR LED, or "laser".
Common choices for DIY projects are the [PMW3360](https://www.tindie.com/products/jkicklighter/pmw3360-motion-sensor/) or [PMW3389](https://www.tindie.com/products/jkicklighter/pmw3389-motion-sensor/) optical sensors, or the [ADNS-9800](https://www.tindie.com/products/jkicklighter/adns-9800-laser-motion-sensor/) laser sensor.
All of them are available on breakout boards from JACK Enterprises on Tindie.
Unfortunately the shipping costs to Europe are very high, so I had to find another solution.

Apparently the requirements for trackballs are not as high as for gaming mouses, they are normally used with much lower resolutions.
Because of this, and also because of price and availability, I decided to go for the PMW3360.
The chip can be bought on [AliExpress](https://www.aliexpress.com/w/wholesale-pmw3360.html), including the lens assembly, for around 15€.

To properly use it also requires some kind of breakout board with a voltage regulator, as the sensor needs ~2V supply voltage.
Fortunately the IOs can be used with 3.3V devices like the RP2040.
Many designs can be found [on GitHub](https://github.com/search?q=pmw3360), like ["Ogen" from JeremyBois](https://github.com/JeremyBois/Ogen) or ["PMW3360" from kbjunky](https://github.com/kbjunky/PMW3360).

I decided to go with ["pmw3360-breakout" by jfedor2](https://github.com/jfedor2/pmw3360-breakout).
It is the most minimalistic and it also includes all required files to get the board pre-assembled from [JLCPCB](https://jlcpcb.com/).
With their usual promo I got 5 boards produced and assembled for just 15.65€, including shipping.
This is unbelievable to me.

<!--%
lightgallery([
    [ "img/pmw3360_order.png", "Screenshot of JLCPCB order" ],
    [ "img/pmw3360_breakout_3.jpg", "Top of PMW3360 breakout board" ],
    [ "img/pmw3360_breakout_2.jpg", "Bottom of PMW3360 breakout board, with lens" ],
])
%-->

To be able to call this a trackball, we also need some kind of ball or sphere of course.
Many people go with the smallest regulation billard balls with a diameter of 38mm.
These can be sourced relatively easily and are usualy flat enough, so I got some.
This turned out to be a bit of a problem, however, more on that later.

<!--%
lightgallery([
    [ "img/trackball_v1_16.jpg", "Small billard balls, case" ],
    [ "img/trackball_v1_17.jpg", "Small billard balls" ],
])
%-->

To get the ball rolling smoothly we also need some kind of mount or bearing surface.
There are different options for this, nicely detailed on [Reddit](https://www.reddit.com/r/ErgoMechKeyboards/comments/yyu4ra/trackball_bearings_a_comparison_of_cheap_rollers/) and [GitHub](https://github.com/Wimads/Trackball-mousekeys-add-on-for-Skeletyl) by "Wimads".
Because of this I decided to go with Si3N4 static bearing balls with a diameter of 3mm.
I got 20 [from eBay](https://www.ebay.de/itm/304376943632?var=603428120198) for ~5€.

For the switches I decided to go with Cherry MX keyboard switches, simply because I had them available.
They are not optimal with their long key travel, I plan to change it in the future, but you also kinda get used to them.

<!--%
tableHelper([ "align-right", "align-right", "align-last-right", "align-right monospaced"],
    [ "Part", "Count", "Description", "Cost" ], [
        [ "µC", "1x", ("Raspberry Pi Pico", "https://www.raspberrypi.com/products/raspberry-pi-pico/"), "4.10€" ],
        [ "Sensor", "1x", ("PMW3360 (chip and lens)", "https://www.aliexpress.com/item/4000904265601.html"), "11.83€" ],
        [ "PCB", "1x", ("PMW3360 Breakout Board", "https://github.com/jfedor2/pmw3360-breakout"), "3.13€" ],
        [ "Ball", "1x", ("38mm billard ball", "https://www.ebay.de/itm/222457101403"), "1.37€" ],
        [ "Bearing", "3x", ("Si3N4 3mm sphere", "https://www.ebay.de/itm/304376943632?var=603428120198"), "0.72€" ],
        [ "Switch", "4x", ("Cherry MX compatible", "https://www.aliexpress.com/item/1005003803920093.html"), "1.03€" ],
        [ "Keycap", "4x", "From old keycap set", "0.00€" ],
        [ "Insert", "4x", "M3 od=5mm l=6mm", "0.00€" ],
        [ "Screw", "4x", "M3 l=8mm", "0.00€" ],
        [ "Screw", "8x", "M2 l=6mm", "0.00€" ],
        [ "Screw", "3x", "Grub screw M3 l>=4mm", "0.00€" ],
        [ "", "", "Sum", "22.18€" ]
    ]
)
%-->

*Note*: some parts are only sold in bulk.
Therefore, if you only want to build a single trackball, it will be more expensive than the sum listed above.
What you see on top is the actual price I paid for the parts, reduced to the amount required for a single device.
Also some parts, like screws or 3D printing materials, I consider as normal parts of a workshop, so they are not added to the cost either.

## 3D Design
<a class="anchor" name="3d_design"></a>

The most important part of the 3D design is the mounting of the sensor and lens assembly in relation to the tracking surface, in our case the ball.
The datasheet has lots of dimensional drawings which kind of hide all the important measurements somewhere in there.

<!--%
lightgallery([
    [ "img/pmw3360_dimensions_1.png", "PMW3360 dimensional drawings, 1/6" ],
    [ "img/pmw3360_dimensions_2.png", "PMW3360 dimensional drawings, 2/6" ],
    [ "img/pmw3360_dimensions_3.png", "PMW3360 dimensional drawings, 3/6" ],
])
%-->

I took great care and tried to design everything according to the specifications.

<!--%
lightgallery([
    [ "img/pmw3360_dimensions_4.png", "PMW3360 dimensional drawings, 4/6" ],
    [ "img/pmw3360_dimensions_5.png", "PMW3360 dimensional drawings, 5/6" ],
    [ "img/pmw3360_dimensions_6.png", "PMW3360 dimensional drawings, 6/6" ],
])
%-->

The static bearing balls are push-fit mounted inside the "roller holders".
Printing this part is a bit tricky.
Including the ball it should have a total height of 10mm.
With my FDM printer it was 0.1mm too small, so I added an adjustment parameter in the design.
Later iterations were always printed on SLA printers, where the adjustment had to be set back to zero.

So if you want the distance to be perfect, measure the printed and assembled part and adjust accordingly.
Although I think small deviations shouldn't matter too much.
The sensor has a relatively large range of useable distances.

<!--%
lightgallery([
    [ "img/trackball_scad_2.png", "Explosion drawing of assembled parts" ],
    [ "img/trackball_scad_1.png", "Close up view of lens distancing and roller holder" ],
])
%-->

The roller holders are kept in place with a grub screw for each.
Then the sensor can be screwed into the top housing first, followed by the Pi.
The bottom part is just a lid, without any parts screwed into it.

Unfortunately the design is relatively unwieldy in OpenSCAD.
Even the preview render takes dozens of seconds, with a very sluggish UI afterwards.
Rendering takes ¾ of an hour on my machine.
For development the `$fn` parameter can be set to a lower value.
That helps somewhat.

## Firmware Development
<a class="anchor" name="firmware_devel"></a>

Before designing and printing the complete device I made a small test bed to hold the sensor and ball.

<!--%
lightgallery([
    [ "img/trackball_v1_1.jpg", "First sensor case prototype, with ball" ],
    [ "img/trackball_v1_2.jpg", "First sensor case prototype, no ball" ],
    [ "img/trackball_v1_3.jpg", "Sensor in first case prototype" ],
])
%-->

With this initial "engineering sample" built I could continue with development of the firmware.
This was basically my christmas holiday project in 2022.

Interfacing with the PMW3360 chip is a bit more difficult than I initially expected.
Of course everything is confidential and proprietary, but you can find [leaked datasheets on the internet](https://d3s5r33r268y59.cloudfront.net/datasheets/9604/2017-05-07-18-19-11/PMS0058-PMW3360DM-T2QU-DS-R1.50-26092016._20161202173741.pdf).
It describes everything pretty well, including pinout and electrical characteristics, which were already taken care of in the breakout board.
And it also describes the SPI communication interface.
The only problematic part is the so-called SROM.

<!--%
lightgallery([
    [ "img/pmw3360_datasheet_1.png", "Excerpt of PMW3360 datasheet, Power Up" ],
    [ "img/pmw3360_datasheet_2.png", "Excerpt of PMW3360 datasheet, SROM Download" ],
])
%-->

The chip requires a binary blob to be loaded on every power up, otherwise it won't work.
Fortunately this was also leaked or sniffed (I'm not sure), version 4 is available [here](https://github.com/mrjohnk/PMW3360DM-T2QU/blob/master/Arduino%20Examples/PMW3360DM-polling/SROM_0x04_Arduino.ino) or [here](https://github.com/SunjunKim/PMW3360/blob/master/src/PMW3360.cpp), for example.
So I've included it in my firmware as well.
Not all of the fancy functionality is included in this V4 firmware blob, but it is enough for normal mouse operation.

Contrary to that I'm very happy with the RP2040 / Raspberry Pi Pico ecosystem.
The hardware seems well documented without having to go completely in-depth into the CPU datasheets.
And the SDK similarly seems well thought-out and implemented.

I was especially delighted with the ability to simply use a second Pico as a debugging dongle instead of needing an ST-Link or similar hardware.

<!--%
lightgallery([
    [ "img/trackball_v1_4.jpg", "Debugging with two Pi Picos" ],
])
%-->

For the USB device implementation the Pico SDK includes [TinuyUSB](https://github.com/hathach/tinyusb).
From the Pico SDK I based my work on their [HID Composite example](https://github.com/raspberrypi/pico-examples/tree/master/usb/device/dev_hid_composite) ported from TinyUSB, as well as the [CDC MSC example](https://github.com/hathach/tinyusb/tree/master/examples/device/cdc_msc) directly from TinyUSB.

This was very comfortable to use.
From [a past project](2015_12_20_serialgamepad.html) I'm familiar with the pain of writing custom USB HID descriptors.
Fortunately this is all handled by TinyUSB.
You just need to pass the appropriate delta values for the mouse axes.

I combined the examples to have the device act simultaneously as a human input device, and serial port and mass storage device for debugging.
Of course I only developed and tested the device on my Linux machines initially.
But I have now also tested it with Windows, and it works fine there as well.
All functionality can be accessed without any driver installation.

For the debug mass storage I also had to add some kind of file system.
To do this I used [the FatFs library](https://github.com/abbrev/fatfs).
I simply reserved a bunch of memory in RAM that acts as the disk device.
Before it is mounted by the user, the disk is formatted and filled with the required data.
Then the host can mount it and read the files.

## Wiring
<a class="anchor" name="wiring"></a>

Wiring up the device is very easy, especially because the RP2040 provides great flexibility in its use of the GPIOs and the hardware periphery, in our case SPI.

<!--%
lightgallery([
    [ "img/pi_pico_pinout.png", "Raspberry Pi Pico pinout" ],
])
%-->

The SPI interface of the PMW3360 needs to be connected to one of the SPI interfaces of the Pico.
But which one you use is not important and can easily be changed in the code.
By default it uses the standard SPI0 pins.

<div class="textwrap"><pre>
GPIO 16 (pin 21) MISO -> MISO on PMW3360 board
GPIO 17 (pin 22) CS   -> NCS on PMW3360 board
GPIO 18 (pin 24) SCK  -> SCK on PMW3360 board
GPIO 19 (pin 25) MOSI -> MOSI on PMW3360 board
GPIO 20 (pin 26)      -> MOTION on PMW3360 board
   3.3v (pin 36)      -> VCC on PMW3360 board
    GND (pin 38)      -> GND on PMW3360 board
GPIO 21 (pin 27)      -> Switch (back button)
GPIO 22 (pin 29)      -> Switch (middle button)
GPIO 26 (pin 31)      -> Switch (left button)
GPIO 27 (pin 32)      -> Switch (right button)
</pre></div>

The switches use the internal pull-up resistors in the RP2040 GPIOs.
So they should be wired active-low, with their common connection to GND.

## Sensor Problems
<a class="anchor" name="sensor_problems"></a>

With the firmware mostly done I hoped to be able to use the device immediately.
But it didn't quite work.
When I ran my finger over the lens the sensor moved erratically, but no movement was seen with the white ball I initially tested with.
Only after switching to other colors I noticed that they behave differently.
So there was some investigation required.

Besides the X and Y values you get a bunch of other stuff with each sensor data sample.
I added functionality to dump these and made a small Python script to visualize them.

<!--%
lightgallery([
    [ "img/pmw3360_data_white.png", "Data capture of white ball" ],
    [ "img/pmw3360_data_orange.png", "Data capture of orange ball" ],
])
%-->

With the white ball you see no movement at all, with the right ball there is movement, but there is no immediately obvious difference in the other datapoints.

The PMW3360 also has a "Frame Capture" mode.
This can be used to grab a full picture of what the image sensor is seeing.
Using it overwrites the SROM firmware, so the sensor has to be re-initialized afterwards.
I had some problems with this mode.
For some reason I'm not able to properly reset the sensor after capturing a frame.
It no longer reports the correct SROM ID and only a power-cycle fixes it.
But the frame data can be read properly and I made a Python script to visualize it.

<!--%
lightgallery([
    [ "img/pmw3360_frames.png", "Frame capture with no ball, white ball and orange ball" ],
])
%-->

I'm not sure what exactly is going on with the strange lines visible in the pictures.
I can't find any bug on the visualization side, but I won't rule that out fully.
But like with the data visualization above, there is no obvious difference between the different colored balls.

While producing some pretty pictures, this approach of analyzing the data didn't really bring us any closer to a working trackball.

But then Philipp had the idea that saved the day.
From the factory the PMW3360 sensors come with two small pieces of kapton tape over the optical inlet and outlet holes in the chip package.
Removing them solved all issues.

<!--%
lightgallery([
    [ "img/pmw3360_breakout_1.jpg", "Bottom of PMW3360 breakout board, without lens. Note the kapton tape which needs to be removed!" ],
])
%-->

Now all billard balls work fine, regardless of their colour.
Even the white ball works without any problems.
With the electronics and the firmware ready, we could now move on to refining the mechanics.

## First Prototype
<a class="anchor" name="first_prototype"></a>

The first top case was printed on Philipps [Anycubic Photon Mono 4K](https://www.anycubic.com/products/photon-mono-4k) SLA printer with [Anycubic Standard Resin + Grey](https://amzn.to/3RSLslf).
This turned out to not be the best choice.
The resin is very brittle after curing, so after pressing the switches in for the first time, and pulling on them, small parts of the print immediately broke off.
So I had to super-glue the switches in place.

<!--%
lightgallery([
    [ "img/trackball_v1_6.jpg", "Top of first case print" ],
    [ "img/trackball_v1_7.jpg", "Sensor mounted inside first case print" ],
    [ "img/trackball_v1_5.jpg", "Side of first case print" ],
])
%-->

Also because it's not a thermo plastic, the heat melt inserts can not be placed in the usual way.
We also used super glue for these, which worked great.

<!--%
lightgallery([
    [ "img/trackball_v1_8.jpg", "Philipp soldering the switches" ],
    [ "img/trackball_v1_9.jpg", "Front of completed first version" ],
    [ "img/trackball_v1_10.jpg", "Back side of completed first version" ],
])
%-->

The PETG printed bottom case was very slippery on a hard table surface.
So I cut a piece of self-adhesive spongy rubber to the proper size and put it on the bottom.
This increases friction by a fair amount, but is not yet optimal.
I will have to try out some other materials.

<!--%
lightgallery([
    [ "img/trackball_v1_13.jpg", "Before adding spongy rubber on the bottom" ],
    [ "img/trackball_v1_14.jpg", "After adding spongy rubber on the bottom" ],
])
%-->

And there we go, a finished and working trackball.

<!--%
lightgallery([
    [ "img/trackball_v1_15.jpg", "Looking into sensor of first version" ],
    [ "img/trackball_v1_11.jpg", "First completed Trackball" ],
])
%-->

## Improvements
<a class="anchor" name="improvements"></a>

For the second iteration we didn't do that many changes in the 3D design.
The button orientation has been overhauled.
This time we sat down and actually tried to find good positions using measurements on our hands.
Also the Pi Pico is no longer mounted in the bottom shell, therefore removing the need of long cables to be able to disassemble the device.

This time I printed the top case on my recently acquired [Sparkmaker](sparkmaker_repair.html) SLA printer, with [Anycubic ABS-like Resin black](https://amzn.to/3Xphpmu).

<!--%
lightgallery([
    [ "img/trackball_v1_19.jpg", "Printing the second case" ],
    [ "img/trackball_v1_22.jpg", "Sensor mounted in case" ],
])
%-->

One useful aspect of the PMW3360 lens assembly are the two mounting posts.
They can be heated to firmly keep them in place.

> **Recommendation**: The lens can be permanently secured to the chip package by melting the lens’ guide posts over the chip with heat staking process.
Please refer to the application note *PMS0122‐LM19‐LSI‐AN* for more details.

Instead of the official (confidential 🙄) method I recommend simply heating a screw or other piece of metal for 5 seconds with a lighter, then pressing it lightly on the post.
Make sure everything is clean and the kapto tape removed between sensor and lens.
You can see the before and after in the pictures below.

<!--%
lightgallery([
    [ "img/trackball_v1_20.jpg", "PMW3360 before melting lens posts" ],
    [ "img/trackball_v1_21.jpg", "PMW3360 after melting lens posts" ],
])
%-->

Apart from that nothing much has changed.
The heat melt inserts are still super-glued in place.

<!--%
lightgallery([
    [ "img/trackball_v1_28.jpg", "Left side of second version" ],
    [ "img/trackball_v1_33.jpg", "Inside view of second version" ],
    [ "img/trackball_v1_26.jpg", "Back right of second version" ],
])
%-->

And I used the same rubber mat for the underside.
It works good enough that I didn't yet bother with a replacement.

<!--%
lightgallery([
    [ "img/trackball_v1_24.jpg", "Looking into sensor of second version" ],
    [ "img/trackball_v1_23.jpg", "Underside of second version" ],
])
%-->

## User Experience
<a class="anchor" name="user_experience"></a>

I have been using these Trackballs for about six weeks at the time of this writing.
From a software and electronics perspective they work absolutely fine.
No disconnects, jumping cursor or any strange behaviour was observable.
So I'm very happy with that.

Ufortunately using them is also quite literally painful.
They don't score high in terms of ergonomics, at all.
The second version, with some more thought put into the placement and orientation of the switches, is an improvement, but there's still a long way to go.

But using a device each day that I've built completely myself, from the grounds up in pretty much all aspects, brings me a lot of joy.
I highly recommend it.

## License
<a class="anchor" name="license"></a>

The Trackball is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    See <http://www.gnu.org/licenses/>.

## More Pictures
<a class="anchor" name="more_pictures"></a>

<div class="collapse">Some more photographs I didn't use above.</div>
<div class="collapsecontent">
<!--%
lightgallery([
    [ "img/trackball_v1_25.jpg", "Back right of second version" ],
    [ "img/trackball_v1_18.jpg", "Printing the second case, badly lit" ],
    [ "img/trackball_v1_29.jpg", "Second version, badly lit" ],
    [ "img/trackball_v1_30.jpg", "Second version, badly lit" ],
    [ "img/trackball_v1_31.jpg", "Second version, badly lit" ],
    [ "img/trackball_v1_32.jpg", "Second version, badly lit" ],
])
%-->
</div>
