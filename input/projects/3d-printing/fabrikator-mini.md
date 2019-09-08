title: Fabrikator Mini
description: My modifications for the TinyBoy Fabrikator Mini
parent: 3d-printing
position: 10
comments: true
flattr: true
---

<span style="font-size: small;">[...back to 3D-Printing overview](3d-printing.html)</span>

# {{ page.title }}

**More content coming soon!**

I bought the [Fabrikator Mini V1.5 from HobbyKing](https://hobbyking.com/en_us/fabrikator-mini-3d-printer-transparent-eu-230v-v1-5.html) in about March 2016.
So that's pretty much exactly three and a half years ago, at the time of this writing.
I'm unbelievably happy with this printer and how it held up over the years.

So first, some background.
It is a clone of the educational [TinyBoy printer](http://www.tinyboy.net/), the frame entirely made from acrylic sheets, with a print area of only 80x80x80mm.
As a result, only very slow print speeds of about 20mm/s are feasible. I guess that's one of the reasons it delivers such surprisingly good print results.

Of course, as with every printer, there were some rough spots and problems, but with a bunch of modifications and different parts this machine is now firmly holding this place as my go-to workhorse printer.

TODO photos

### Power Supply Replacement

I did not really trust the stock power supply and I also needed more power available for further modifications.
So one of the first steps was replacing the power supply.
I did opt for one of the generic large chinese 12V supplies offered on eBay, I chose the 20A version.
To make it at least a bit safer, I cut, bent and screwed a piece of brass sheet over the 220V input terminals and added a power-button.
On the output side I did keep the old connector from the stock power supply.
I also added a 12V indicator LED I still had lying around.
In my configuration, the power supply is always turned on, powering the Raspberry Pi that controls the printer power via a relay board. See below.

TODO photos

### Heatbed Replacement

One of the first problems I ran into were with the printing surface.
In its stock configuration, the Fabrikator Mini has an acrylic sheet with blue painters masking tape on top as its print surface.
This works, but I was not entirely happy with the adhesion of PLA and the need to frequently replace the tape or even use stuff like glue or hairspray to keep the prints firmly in place.
So I did a search on eBay, and found a vendor offering replacement aluminum heatbeds specifically for the Fabrikator Mini. They were made `tinyfab.xyz`, they now have their own [webshop listing the heatbed](https://www.tinyfab.xyz/product-page/mini-fabrikator-v1-1-5-alu-heatbed). Unfortunately, it no longer seems to be available.
I've also bough a 80mm wide kapton tape roll and have been using this as a print surface on the aluminum heatbed ever since, only replacing it when needed after I damaged it on print removal.
Depending on how you solder the power supply wires to the heatbed, it can either run in a 15W or a 60W configuration.
I found the 15W setting to be painfully slow in reaching usable temperatures, so I have been using the 60W variant basically from the beginning.
Of course, as mentioned before, I used a beefier power supply for this that can handle the load. I did not however replace the DC connector on the printer or use a MOSFET or anything special. Both the connector and the (in stock unused) heatbed MOSFET seem to be able to handle the load in my configuration, even for very long prints.
I did have some problems with properly routing the cables for the heatbed, a couple of times the cable broke where it flexed the most after many prints. I've drilled a bigger hole into the bottom acrylic plate, used flexible silicon cables, a bunch of cable-ties and gaffer tape on the heatbed underside and it now seems to hold up well.

TODO photos

### Mesh Bed Leveling

Even though it probably shouldn't be necessary for such a small printbed, I did still have some first layer adhesion issues with the aluminum printbed. Especially one corner seems to be a bit bent. So I enabled Mesh Bed Leveling in my Marlin Firwmare (see below) and also wrote a little [GUI Tool to assist the leveling process](https://git.xythobuz.de/thomas/Bed-Leveling-Utility). It is also on [GitHub](https://github.com/xythobuz/Bed-Leveling-Utility).

Here is my latest measured mesh, for example. Also be aware that these values differ significantly between a hot and a cold bed, so always do the leveling on a fully heated bed!

           0        1        2        3
    0 -0.12500 -0.07500 -0.10000 -0.10000
    1 -0.12500 -0.10000 -0.12500 -0.10000
    2 -0.07500 -0.12500 -0.12500 -0.10000
    3 -0.10000 -0.12500 -0.12500 -0.15000

And this is really just an example! Do not just copy these values to your printer, they will differ of course.

### Temperature Issues

With all of this added load, and even in its stock configuration, the Fabrikator Mini electronics and stepper motors run very hot.
So hot that I did not feel comfortable leaving it like this.
So I've downloaded and designed small fan-mounts for the X and YZ stepper motors and added small heatsinks to each motor and to the extruder stepper.
Of course, I also tried reducing the stepper motor reference voltages first, to run the motors with less current, but even on the lowest setting without skipped steps I still felt the motors and drivers were too hot.
With all of these changes, the printer is now definitely louder than before, but it also runs noticeably cooler.
I've wired all the additional fans in parallel with the stock hotend-cooling fan, so they turn on above 50 degrees Celsius in the stock firmware as well as my self-configured Marlin.
Here are the link to the fan mount designs:

 * [X-Axis motor fan by SgtMunger](https://www.thingiverse.com/thing:1090263)
 * [Y-Axis motor fan](https://www.thingiverse.com/thing:1454399)
 * [Z-Axis motor fan](https://www.thingiverse.com/thing:1531538)

TODO photos

### Z-Axis Noise and Wobble

Right from the start I noticed a very painful high-pitched squealing noise coming from the Z-axis whenever it moved.
Even with lubrication I was not able to resolve this.
But I noticed that it became unhearable as soon as I touched the tip of the axis that reaches out of the top acrylic plate.
Of course, the axis has two fixpoints in the stock configuration, the motor at the bottom, and the nut in the z-carriage, and a mechanical system like this should not be fixed in position at the top as long as it is not perfectly aligned (which it isn't in reality, of course).
So even though it's not advisable, and in theory should cause z-wobble in the printed parts, I did design a small insert for the top acrylic plate that aligns the z-axis to its center at the top.
[It is available on Thingiverse](https://www.thingiverse.com/thing:1600007).
It does in fact stop the noise, and fortunately I cannot notice or measure any z-wobble in the printed parts.

TODO photo

### Part Cooling Fan

Even though print results were already pretty good, there was still some sagging noticeable on sections with long bridges, and also some stringing issues.
Of course, the only real solution for these issues with PLA is a part cooling fan.
As there is not a lot of room available, there aren't many options, especially if the part cooling fan should be independently controllable from the 3D printer controller.
Fortunately, [plasticmonk already designed a very good fan mount solution](https://www.thingiverse.com/thing:1469078), allowing a standard 5015 radial fan to be mounted to the bottom two screws of the hotend fan.

TODO photo
TODO wiring hotend heatbed part-fan hotend-fan

### TODO

* Firmware
* Feet
* Display mount
* Spool mount
* Webcam Mount
* Raspberry Pi mount
* Relais board mount
* Slicing Profiles
* Print Results Pictures

