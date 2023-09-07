title: xyLX5
description: 4S LiPo, 220mm frame, 2205 2300KV motors
parent: quadcopters
position: 10
date: 2017-11-01
update: 2023-09-08
git: https://git.xythobuz.de/thomas/copter-configs/src/branch/master/5_lx5
comments: true
---

<!--% backToParent() %-->

At the end of 2017 I had to give in to the urge of building a bigger more powerful copter.
After my first failed attempts with large copters, gaining some experience with smaller frames seemed useful.
But I had built up some skills and was ready for the next step.
So I built a 220mm frame copter with 2205 motors.

It has all the bells-and-whistles available at the time, like DShot, Betaflight OSD, Smartaudio, as well as S-Bus and Smartport for two-way communication.

<!--%
lightgallery([
    [ "img/lx5_3.jpg", "Front view" ],
    [ "img/lx5_1.jpg", "Left side view" ],
    [ "img/lx5_2.jpg", "Right side view" ],
    [ "img/lx5_4.jpg", "Left stack closeup view" ],
    [ "img/lx5_5.jpg", "Right stack closeup view" ],
    [ "img/lx5_toolbox_instagram.mp4", "video/mp4", "", "", "Footage of me flying at a cocktail machine related event" ],
])
%-->

Here are some recordings of the FPV footage.
Be aware that these videos are recorded from the received signal on the ground.
Not only can you see lots of interference and other HF problems, the loss of quality from the video recorder and the YouTube encoding is also very noticeable.
In real-life, the picture doesn't look *that* bad.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=5Fv40mtiXZU", "img/xylx5_test_flight_thumb.jpg", "LX5 Quadcopter Test Flight"],
    [ "https://www.youtube.com/watch?v=Xgcp8qG9qD8", "img/xylx5_chase_thumb.jpg", "LX5 Quadcopter chase" ],
    [ "https://www.youtube.com/watch?v=wUiboR8pkoA", "img/xylx5_range_thumb.jpg", "LX5 Quadcopter range" ],
    [ "https://www.youtube.com/watch?v=SRrjPk51ng0", "Flying below a bridge, over a creek" ],
    [ "https://www.youtube.com/watch?v=Zh9_t0R_MWw", "First flights after BF 4.4.1 upgrade" ],
])
%-->

Using a 3D printed baseplate, I mounted the FrSky Rx as the third/top level of the PCB stack.
To fit in the VTx as well, I simply zip-tied it to the bottom side of this plate.

To protect the remote control antennas, I added two zip-ties to the cockpit frame, trimmed to the length of the antennas, and shrinkwrapped the antenna coax cables to the whole zip-tie.
This works very well as crash protection, I never managed to destroy an antenna with this setup.

The VTx Antenna pigtail is comfortably mounted with a special 3D printed piece.
This way, the 5.8GHz Antenna (I'm using a Padoga v2) can easily be changed after crashes and removed for transportation.

For the bottom most level of the PCB stack I used rubber vibration-insulating stand-offs.
I'm not sure if they are really necessary, but they don't seem to hurt either.
Everything else is mounted with rigid spacers.

## Parts List

These are the original prices I paid back when I initially bought the parts.

<!--%
tableHelper([ "align-right", "align-last-right", "align-right monospaced"],
    [ "Part", "Description", "Cost" ], [
        [ "Frame", ("GEP-LX5 Leopard Frame, Green Color", "https://geprc.com/product/gep-lx5-frame/"), "47.20€" ],
        [ "FC", ("Hobbywing XRotor Omnibus F4 Flight Controller", "https://www.hobbywing.com/goods.php?id=590"), "34.08€" ],
        [ "ESCs", ("Hobbywing XRotor Micro 40A 2-5S 4 in 1 ESC", "https://www.hobbywing.com/goods.php?id=588"), "52.44€" ],
        [ "Motors", ("4x Emax RS2205 2300KV CW/CCW Motor", "https://www.banggood.com/4X-Emax-RS2205-2300-2205-2300KV-Racing-Edition-CW-or-CCW-Motor-For-RC-FPV-Racing-Drone-p-1032857.html?cur_warehouse=CN"), "46.32€" ],
        [ "Props", ("10 Pairs Racerstar S5048 PC 3-blade Propeller 5.0mm Mounting Hole", "https://www.banggood.com/10-Pairs-Racerstar-S5048-PC-3-blade-Propeller-5_0mm-Mounting-Hole-for-RC-Multirotor-FPV-Racing-Drone-p-1169658.html"), "10.48€" ],
        [ "Cam", ("RunCam Micro Sparrow 2.1mm", "https://shop.runcam.com/runcam-micro-sparrow/"), "26.22€" ],
        [ "VTx", ("TBS Unify Pro V3 5V", "https://www.team-blacksheep.com/products/prod:unify_pro"), "44.90€" ],
        [ "Rx", ("FrSky XSR", "https://www.frsky-rc.com/product/xsr/"), "13.98€" ],
        [ "Battery", ("SLS Quantum 1300mAh 4S1P 14,8V 65C/130C", "https://www.stefansliposhop.de/en/batteries/sls-quantum/sls-quantum-65c/sls-quantum-1300mah-4s1p-14-8v-65c-130c::1602.html"), "26.00€" ],
        [ "", "Sum", "301.62€" ]
    ]
)
%-->

I have 3D printed the following parts for this copter:

 * ["GEP LX5" arm guards by Wthompson87](https://www.thingiverse.com/thing:2416095)
 * ["GEP LX TBS Unify Pro VTX Antenna Holder" by SnappyFPV](https://www.thingiverse.com/thing:2544507)
 * ["Adapter for Runcam Micro to Full Size" by phezter](https://www.thingiverse.com/thing:2616057)
 * ["FrSky XSR stack mount with holes for zip ties" by tozes](https://www.thingiverse.com/thing:2171446)

You can find my Betaflight configuration dumps [here](https://git.xythobuz.de/thomas/copter-configs/src/branch/master/5_lx5).
