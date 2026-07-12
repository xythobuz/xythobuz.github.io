title: Blog
post: E-Scooter Battery Build
description: Replacement 13S6P Li-Ion AliExpress Kit for my Xiaomi Mi 2
date: 2026-07-04
update: 2026-07-12
comments: true
---

## Background

For some years now I own a Xiaomi Mi 2 scooter.
Of course I flashed it with SHFW using the ST-Link method, which then allows using the normal SHFW Android app to do all updating and configuring.

This worked perfectly fine for about 2500km.
Then the internal battery was noticeably degraded and I could no longer reach home from work in winter.

So I got one of the last [Rita adapters](https://e-scooters.embedden.com/shop/accessories/rita-adapter-for-xiaomi/) before the product was discontinued, which allows connecting an external battery with differing voltage for range extension.

<!--%
lightgallery([
    [ "img/scooter_bat_16.jpg", "Rita adapter (Gen 6) for Xiaomi" ],
    [ "img/scooter_bat_17.jpg", "Rita adapter installed in my scooter" ],
])
%-->

A colleague of mine bought a 13S6P battery on AliExpress which he didn't end up using, so I got that from him.
Unfortunately it was total crap, and died much much quicker.
After only a handful of trips, I could again not reach work anymore.

Still not having learned my lesson, I got a "new" internal Xiaomi scooter battery from AliExpress as well, which was just as bad and died in just a couple of trips.

<!--%
lightgallery([
    [ "img/scooter_bat_18.jpg", "13S battery from AliExpress on my scooter" ],
    [ "img/scooter_bat_19.jpg", "BMS of the cheap AliExpress battery" ],
    [ "img/scooter_bat_20.jpg", "10S battery from AliExpress" ],
])
%-->

So finally I decided to build my own.

## Build

In my scooter config I've set a maximum current of 28A, so I decided to get a DIY battery kit from AliExpress with nominal support for 30A, in a 13S6P configuration.
30A divided by 6 cells in parallel gives a discharge current of 5A per cell.

Looking around online I decided to go with [nkon.nl](https://www.nkon.nl/) as they are a well-known large supplier of cells in Europe.
There I found the [`INR18650-M29`](https://www.nkon.nl/en/inr18650-m29-2850mah-10a.html) cells from LG, which support a surge discharge current of 10A and continuous discharge of 6A, according to [their datasheet](https://akkuplus.de/mediafiles/Datenblatt/LG/LG_INR18650M29.pdf).

<!--%
lightgallery([
    [ "img/scooter_bat_1.jpg", "80x 18650 cells in their shipping carton" ],
    [ "img/scooter_bat_2.jpg", "AliExpress battery kit parts" ],
])
%-->

As mentioned above, I checked the internal cell resistance, but you don't necessarily have to do that, as long as you use cells from one batch.

<!--%
lightgallery([
    [ "img/scooter_bat_3.jpg", "Ohm-meter at work" ],
    [ "img/scooter_bat_4.jpg", "Checking all internal cell resistances" ],
])
%-->

Now just stick them all into the carrier and attach the paper rings to the positive poles, to protect from shorts with the negative pole around the perimeter of each cell.

<!--%
lightgallery([
    [ "img/scooter_bat_5.jpg", "Half of the cells being assembeld in their carrier" ],
    [ "img/scooter_bat_6.jpg", "All cells in their carrier" ],
    [ "img/scooter_bat_7.jpg", "All celss in their carrier, with BMS" ],
    [ "img/scooter_bat_8.jpg", "Attaching paper rings to + poles" ],
])
%-->

Then do the spot welding.
I recommend doing some testing first on an unused cell, which is how I arrived at the settings mentioned above.
I ended up with four welds per cell pole.

<!--%
lightgallery([
    [ "img/scooter_bat_9.jpg", "Starting the spot-welding" ],
    [ "img/scooter_bat_10.jpg", "Close-up view of some spot-welds" ],
    [ "img/scooter_bat_11.jpg", "Covering the finished welds with paper" ],
    [ "img/scooter_bat_12.jpg", "Wrapping the cells with tape for stability" ],
])
%-->

The whole thing was covered with more insulating paper, and some battery fibre tape to hold the cells firmly in place.

<!--%
lightgallery([
    [ "img/scooter_bat_13.jpg", "BMS attached to the nickel strips" ],
    [ "img/scooter_bat_14.jpg", "Assembled battery box, top" ],
    [ "img/scooter_bat_15.jpg", "Assembled battery box, side" ],
])
%-->

The BMS can also be welded, just the (dis)charge leads need to be soldered.
Use thick wires for that, rated for the current.
Therefore you will also need a beefy soldering iron to get them soldered to the PCB without unnecessary heating of other components.

## Tools Used

Fortunately I have some access to tools at work.

So I used their [RS Pro RSBM-3300 Battery Tester](https://de.rs-online.com/web/p/batterie-tester/1804810) to check the  charge state and internal resistance of each cell.
This turned out to be unnecessary though, as all cells came from the same batch and had matching voltages and resistances.

For spot welding I used the [FNIRSI SWM-10](https://www.fnirsi.com/products/swm-10).
The settings I was happy with are:

* Preheat: `3ms`
* Pulse: `15ms`
* Interval: `10ms`
* Dots: `3`

Although all around I don't like this spot welder very much.
It's made with a single very beefy lithium cell inside, that seems to just be shorted for welding, which is fine.
But the charging and safety monitoring of this cell seems problematic.
It was deep-discharged by itself after some time on the shelf, and when left to charge it stopped the charge at a cell voltage of 4.3V, which is overcharging the cell.
So be careful with that, if you own the device yourself.
Some people online suggest only using it with slow USB chargers with `500mA` or so.

It also took around three or four recharges of the spot-welder battery to finish this project.

## Bill of Materials

These are the consumables I bought, with the price I paid at the time.

<!--%
tableHelper([ "align-right", "align-right monospaced", "align-right monospaced", "align-right monospaced" ],
    [ "Part", "Amount", "Unit-Cost", "Total-Cost" ], [
        [ ("INR18650-M29 2850mAh - 10A", "https://www.nkon.nl/en/inr18650-m29-2850mah-10a.html"), "78x", "1.06€", "82.68€"],
        [ ("48V 30A 13S 6P 18650 Battery Holder E-bike Battery Case Box BMS for E-scooter Electric Bike Battery Housings with Welding Nickel", "https://de.aliexpress.com/item/1005008724048062.html"), "1x", "24.59€", "24.59€" ],
        [ ("XT60 Battery Connector Male & Female Bullet Connector Plugs with Sheath Housing for RC Battery Motor FPV XT-60 Adapter Silicone (L)", "https://de.aliexpress.com/item/1005010596832228.html"), "1x", "4.69€", "4.69€" ],
        [ ("High Viscosity Stripe Fiber Tape, Non-Marking Tape, Battery Bundling, Wear-Resistant, Waterproof, and High-Temperature Resistant (50mm)", "https://de.aliexpress.com/item/1005009381533331.html"), "1x", "3.55€", "3.55€" ],
        [ ("5m 18650 Battery Electrical Insulating Adhesive Paper Thickness Battery Pack Insulator Gasket Tape Warp Electrode Insulated Pads (65mm)", "https://de.aliexpress.com/item/1005010613670195.html"), "1x", "3.29€", "3.29€" ],
        [ ("400 Pieces of Self-Adhesive Solid/Hollow 18650 Battery Insulation Pads, 18650 Battery Insulation Rings, 18650 High-Density Paper, Insulation Pad Circles, Single-Sided Adhesive Batteries (Hollow)", "https://de.aliexpress.com/item/1005009644859705.html"), "1x", "1.59€", "1.59€" ],
        [ ("ANL Fuse Holder Bolt-on Fuse Automotive Fuse Holders Fusible Link with fuse 40A 60A 80A 100A 200A 250A 300A Fuses AMP (2x 40A)", "https://de.aliexpress.com/item/1005005885492561.html"), "1x", "4.99€", "4.99€" ],
        [ "Sum", "", "", "125.38€" ]
    ]
)
%-->

With these 2.85Ah cells, arranged as 6 in parallel, the resulting capacity of the pack is `17Ah`.
And the 13 strings of these in series give a nominal voltage of `48V`.

# Fuse Update

After building the battery I noticed that UL certified batteries are required to have a fuse or some other mechanism to prevent thermal runaway events.
The BMS has short-circuit-protection, but I guess adding an actual fuse may help in some cases.
So I bought some [40A fuses and a matching fuse block](https://de.aliexpress.com/item/1005005885492561.html) from AliExpress.
Turns out they are way bigger than I expected.
Reading the specs before buying may be helpful, lesson learned.

<!--%
lightgallery([
    [ "img/scooter_bat_21.jpg", "DC Fuse Block" ],
    [ "img/scooter_bat_22.jpg", "DC Fuse with heat shrink tube" ],
])
%-->

So I just skipped the fuse block and wired the fuse directly into the positive wire.

<!--%
lightgallery([
    [ "img/scooter_bat_23.jpg", "Original wiring inside battery" ],
    [ "img/scooter_bat_24.jpg", "Positive wire cut, with screw lugs" ],
])
%-->

It's a bit tight, but with some M5x12 screws to mount the cables I was able to make it fit.

<!--%
lightgallery([
    [ "img/scooter_bat_25.jpg", "Fuse connected with heat shrink tubing" ],
    [ "img/scooter_bat_26.jpg", "Fuse inside battery" ],
])
%-->

I also took this opportunity and replaced the original six Philips M2.5x16 screws with ones that have internal hex heads.
