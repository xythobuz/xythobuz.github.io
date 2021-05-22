title: xyAurora90
description: 2S LiPo, 90mm frame, 1103 8000KV motors
parent: quadcopters
position: 30
date: 2017-03-07
update: 2021-05-21
---

<span class="listdesc">[...back to RC-Vehicles overview](quadcopters.html)</span>

<!--%
lightgallery([
    [ "img/xyaurora90_5.png", "Front left view" ],
    [ "img/xyaurora90_2.png", "Top right view" ],
    [ "img/xyaurora90_3.png", "Back right view" ]
])
%-->

Here are some recordings of the FPV footage.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=VFPxYdl7hg0", "img/xyaurora90_firsttest_thumb.jpg", "First Brushless 90mm Quadcopter Testflight" ],
    [ "https://www.youtube.com/watch?v=V3l-RCW24_U", "img/xyaurora90_robocup_thumb.jpg", "Robocup German Open 2017 @Home Area Flyaround" ],
    [ "https://www.youtube.com/watch?v=b4heuNomMTk", "img/xyaurora90_wrong_channel_thumb.jpg", "Wrong FPV Channel" ]
])
%-->

The build started at the end of January 2017 and it was my main copter for flights indoors and outside in the garden for a long time.

Initially I was worried about the **receiver** I'm using.
I have an old modified transmitter with an FrSky DHT module, so I can only use D8-mode FrSky-compatible receivers.
For another copter I've tried the RX-F802 but it had some problems with signal loss and improper failsafe behavior.
But the micro receiver I'm using now, linked below, is working flawlessly.
It would be perfect if it also had telemetry available, that way I could skip the OSD.

Most builds with this frame kit are using the 1104 7000kv **motors** that provide significantly more thrust than the 1103 8000kv I'm using.
I may change over in the future, but currently I'm very happy with the available power.

I've tried a bunch of different **batteries**.
The Turnigy nano-tech 2S 450mAh 25/40C listed below is definitely the best in terms of flight characteristics.
For other batteries, make sure that the C-Rating is high enough.
I had big problems with the StefansLipoShop X-Cube 2S 450mAh 30/60C as well as the Rhino 2S 610mAh 20C.
The Turnigy nano-tech 2S 850mAh 25/40C and the Zippy Compact 2S 850mAh 35C both work well but are a bit too heavy for fast flying.

**Fitting the PCBs** all on a stack under the camera and adding the OSD proved to be difficult.
I had to completely insulate it with shrink wrap and fix it on top of the FC with a drop of hot-glue.
The receiver, also shrink-wrapped, is placed on top of the OSD, using hot-glue, too.
There is just enough room to leave the FPV equipment with connectors to allow easy removal of the propeller-guards and camera.

I've designed and 3D-printed [my own **battery clips**](https://www.thingiverse.com/thing:2086873), based on a design already available on Thingiverse.

Adding an **OSD** to the Camera + VTX combo is easy.
Multiple pin headers connect the two PCBs together, one of them a 3-pin header.
On there is GND, Video and a supply voltage line.
The GND line can easily be identified by checking for connectivity to the negative battery connector pole with a multimeter.
I've then used a scope to find the video signal on the outermost pin.
My dremel could not fit into the gap to only cut the video connection, so I've simply cut the whole 3-pin header and soldered the GND and VCC lines back together, adding two cables and a small connector for the OSD to the two video pins.

Because of some bad experiences with the antenna of my last Cam + VTX combo I've decided to cover the whole clover-leaf antenna in some hot-glue.
This has proven to greatly reduce crash damages in my brushed micro copter build.
But considering the good frame design, the antenna should be well protected even without this.

The original Aurora 90 build also has an **LED strip** added to the back, so I bought the same one (available as a replacement part).
Looking at pictures of other owners online, it can be seen that the original Aurora 90 frame has two nubs in the back to hold the LED strip that are missing on my frame.
So again I had to position the LED strip at the back using a generous amount of hot-glue to protect it from impact damage.

All-in-all I'm very happy with the copter.
A minor point is the **JST battery connector** that is sometimes very hard to disconnect and probably is already maxed out in terms of amperage.
Also, I don't like the way the **camera assembly** is just 'clipped' into the propeller guards.
I'm thinking of saving weight in the future by removing the guards and using a 3D-printed assembly to mount the camera on top of the PCB stack.

I should also mention that I got the **TX03** cam on discount over Christmas, so for a future build I may choose another.
The VTX get's very hot very fast, and the whole camera draws 1A on the 200mW setting.
The picture quality is okay but not great.

## Parts List

<table>
<tr><th>Part</th><th>Description</th><th>Cost</th></tr>

<tr><td style="text-align: right;">Frame</td>
<td><a href="https://www.banggood.com/Eachine-Aurora-90-90MM-Mini-Brushless-FPV-Multirotor-Racing-Frame-35g-Carbon-Fiber-Aluminium-Construction-p-1109742.html?p=3F201911077692015010">Eachine Aurora 90 90MM Mini Brushless FPV Racing Frame RC Drone 27g</a></td>
<td style="text-align: right;">18.99$</td></tr>

<tr><td style="text-align: right;">FC</td>
<td><a href="https://www.banggood.com/CleanFlight-BetaFlight-Micro-F3-Flight-Controller-Built-in-PDB-Buzzer-20X20mm-For-FPV-Racing-p-1094615.html?p=3F201911077692015010">PIKO BLX CleanFlight & BetaFlight Micro F3 Flight Controller Built-in PDB Buzzer Port 20X20mm For RC Drone FPV</a></td>
<td style="text-align: right;">15.99$</td></tr>

<tr><td style="text-align: right;">ESCs</td>
<td><a href="https://www.banggood.com/Racerstar-Mini-RS6Ax4-6A-1-2S-Blheli_S-BB2-4-In-1-ESC-with-5V-BEC-Support-Oneshot125-D-Shot-p-1110025.html?p=3F201911077692015010">Racerstar 20x20mm RS6Ax4 6A 1-2S Blheli_S 4 In 1 ESC with 5V BEC Dshot600</a></td>
<td style="text-align: right;">29.69$</td></tr>

<tr><td style="text-align: right;">Motors</td>
<td><a href="https://www.banggood.com/4X-Racerstar-Racing-Edition-1103-BR1103-8000KV-1-2S-Brushless-Motor-Purple-For-50-80-100-Multirotor-p-1117646.html?p=3F201911077692015010&cur_warehouse=CN">4X Racerstar Racing Edition 1103 BR1103 8000KV 1-2S Brushless Motor Purple For 50 80 100 Multirotor</a></td>
<td style="text-align: right;">31.99$</td></tr>

<tr><td style="text-align: right;">Props</td>
<td><a href="https://www.banggood.com/2-Pairs-Kingkong-45mm-3-Blade-Propeller-0_97mm-Mounting-Hole-For-90mm-150mm-DIY-Frame-Kit-p-1122784.html?p=3F201911077692015010&cur_warehouse=CN">2 Pairs Kingkong 45mm 3-Blade Propeller 0.97mm Mounting Hole For 90mm-150mm DIY Frame Kit</a></td>
<td style="text-align: right;">1.99$</td></tr>

<tr><td style="text-align: right;">Cam</td>
<td><a href="https://www.banggood.com/Eachine-TX03-NTSC-Super-Mini-0-or-25mW-or-50mW-or-200mW-Switchable-AIO-5_8G-72CH-VTX-600TVL-1-or-3-Cmos-FPV-Camera-p-1104884.html?akmClientCountry=DE&p=3F201911077692015010&cur_warehouse=CN">Eachine TX03 NTSC Super Mini 0/25mW/50mW/200mW Switchable AIO 5.8G 72CH VTX 600TVL 1/3 Cmos FPV Camera</a></td>
<td style="text-align: right;">19.99$</td></tr>

<tr><td style="text-align: right;">Rx</td>
<td><a href="https://www.banggood.com/FD800-Tiny-Frsky-8CH-PPM-or-SBUS-Receiver-Compatible-FRSKY-ACCST-X9D(Plus)DJT-or-DFT-or-DHT-For-QX95-QX90--p-1108071.html?akmClientCountry=DE&p=3F201911077692015010&cur_warehouse=CN&ID=527773">FD800 Tiny Frsky 8CH PPM/SBUS Receiver Compatible FRSKY ACCST X9D(Plus)DJT/DFT/DHT For QX95 QX90</a></td>
<td style="text-align: right;">11.99$</td></tr>

<tr><td style="text-align: right;">Bat</td>
<td><a href="https://hobbyking.com/en_us/turnigy-nano-tech-460mah-2s-25-40c-lipo-pack.html">Turnigy nano-tech 460mah 2S 25~40C Lipo Pack</a></td>
<td style="text-align: right;">4.71$</td></tr>

<tr><td style="text-align: right;">LEDs</td>
<td><a href="https://www.banggood.com/Eachine-Aurora-90-100-Mini-FPV-Racer-RC-Drone-Spare-Part-WS2812-LED-Board-LED-Strip-Light-p-1122903.html?akmClientCountry=DE&p=3F201911077692015010&cur_warehouse=CN">Eachine Aurora 90 100 Mini FPV Racer RC Drone Spare Part WS2812 LED Board LED Strip Light</a></td>
<td style="text-align: right;">2.54$</td></tr>

<tr><td style="text-align: right;">Strap</td>
<td><a href="https://www.banggood.com/Realacc-58mm-Battery-Tie-Down-Strap-for-RC-Micro-FPV-Racing-Quadcopter-Multirotor-p-1118296.html?p=3F201911077692015010">Realacc 58mm Battery Tie Down Strap for RC Micro FPV Racing Quadcopter Multirotor</a></td>
<td style="text-align: right;">1.09$</td></tr>

<tr><td></td>
<td style="text-align: right;">Sum</td>
<td style="text-align: right;">138.97$</td></tr>
</table>

Here are some more photos.

<!--%
lightgallery([
    [ "img/xyaurora90_4.png", "Back left view" ],
    [ "img/xyaurora90_1.png", "Bottom view" ]
])
%-->

This write-up was first published on [Rotorbuilds](https://rotorbuilds.com/build/2428).
