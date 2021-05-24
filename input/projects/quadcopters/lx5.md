title: xyLX5
description: 4S LiPo, 220mm frame, 2205 2300KV motors
parent: quadcopters
position: 10
date: 2017-11-01
update: 2021-05-21
---

<span class="listdesc">[...back to RC-Vehicles overview](quadcopters.html)</span>

At the end of 2017 I had to give in to the urge of building a bigger more powerful copter.
After my first failed attempts with large copters, gaining some experience with smaller frames seemed useful.
But I had built up some skills and was ready for the next step.
So I built a 220mm frame copter with 2205 motors.

Here are some recordings of the FPV footage.
Be aware that these videos are recorded from the received signal on the ground.
Not only can you see lots of interference and other HF problems, the loss of quality from the video recorder and the YouTube encoding is also very noticeable.
In real-life, the picture doesn't look *that* bad.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=5Fv40mtiXZU", "img/xylx5_test_flight_thumb.jpg", "LX5 Quadcopter Test Flight"],
    [ "https://www.youtube.com/watch?v=Xgcp8qG9qD8", "img/xylx5_chase_thumb.jpg", "LX5 Quadcopter chase" ],
    [ "https://www.youtube.com/watch?v=wUiboR8pkoA", "img/xylx5_range_thumb.jpg", "LX5 Quadcopter range" ]
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

<table>
<tr><th>Part</th><th>Description</th><th>Cost</th></tr>

<tr><td style="text-align: right;">Frame</td>
<td><a href="https://geprc.com/product/gep-lx5-frame/">GEP-LX5 Leopard Frame, Green Color</a></td>
<td style="text-align: right;">47.20€</td></tr>

<tr><td style="text-align: right;">FC</td>
<td><a href="https://www.hobbywing.com/goods.php?id=590">Hobbywing XRotor Omnibus F4 Flight Controller</a></td>
<td style="text-align: right;">34.08€</td></tr>

<tr><td style="text-align: right;">ESCs</td>
<td><a href="https://www.hobbywing.com/goods.php?id=588">Hobbywing XRotor Micro 40A 2-5S 4 in 1 ESC</a></td>
<td style="text-align: right;">52.44€</td></tr>

<tr><td style="text-align: right;">Motors</td>
<td><a href="https://www.banggood.com/4X-Emax-RS2205-2300-2205-2300KV-Racing-Edition-CW-or-CCW-Motor-For-RC-FPV-Racing-Drone-p-1032857.html?cur_warehouse=CN">4x Emax RS2205 2300KV CW/CCW Motor</a></td>
<td style="text-align: right;">46.32€</td></tr>

<tr><td style="text-align: right;">Props</td>
<td><a href="https://www.banggood.com/10-Pairs-Racerstar-S5048-PC-3-blade-Propeller-5_0mm-Mounting-Hole-for-RC-Multirotor-FPV-Racing-Drone-p-1169658.html">10 Pairs Racerstar S5048 PC 3-blade Propeller 5.0mm Mounting Hole</a></td>
<td style="text-align: right;">10.48€</td></tr>

<tr><td style="text-align: right;">Cam</td>
<td><a href="https://shop.runcam.com/runcam-micro-sparrow/">RunCam Micro Sparrow 2.1mm</a></td>
<td style="text-align: right;">26.22€</td></tr>

<tr><td style="text-align: right;">VTx</td>
<td><a href="https://www.team-blacksheep.com/products/prod:unify_pro">TBS Unify Pro V3 5V</a></td>
<td style="text-align: right;">44.90€</td></tr>

<tr><td style="text-align: right;">Rx</td>
<td><a href="https://www.frsky-rc.com/product/xsr/">FrSky XSR</a></td>
<td style="text-align: right;">13.98€</td></tr>

<tr><td style="text-align: right;">Battery</td>
<td><a href="https://www.stefansliposhop.de/en/batteries/sls-quantum/sls-quantum-65c/sls-quantum-1300mah-4s1p-14-8v-65c-130c::1602.html">SLS Quantum 1300mAh 4S1P 14,8V 65C/130C</a></td>
<td style="text-align: right;">26.00€</td></tr>

<tr><td></td>
<td style="text-align: right;">Sum</td>
<td style="text-align: right;">301.62€</td></tr>
</table>

I have 3D printed the following parts for this copter:

 * ["GEP LX5" arm guards by Wthompson87](https://www.thingiverse.com/thing:2416095)
 * ["GEP LX TBS Unify Pro VTX Antenna Holder" by SnappyFPV](https://www.thingiverse.com/thing:2544507)
 * ["Adapter for Runcam Micro to Full Size" by phezter](https://www.thingiverse.com/thing:2616057)
 * ["FrSky XSR stack mount with holes for zip ties" by tozes](https://www.thingiverse.com/thing:2171446)
