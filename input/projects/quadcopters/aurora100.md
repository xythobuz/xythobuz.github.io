title: xyBeast
description: 3S LiPo, 100mm frame, 1104 6500KV motors
parent: quadcopters
position: 20
date: 2017-07-17
update: 2021-05-21
---

<span class="listdesc">[...back to RC-Vehicles overview](quadcopters.html)</span>

Not being totally happy with the power available with [my 2S xyAurora90](aurora90.html) I decided to build a 3S Aurora100 in July 2017.

<!--%
lightgallery([
    [ "img/xyaurora100_1.jpg", "Original Setup with AIO cam, Front Top view" ]
])
%-->

Here are some recordings of the FPV footage.
Be aware that these videos are recorded from the received signal on the ground.
Not only can you see lots of interference and other HF problems, the loss of quality from the video recorder and the YouTube encoding is also very noticeable.
In real-life, the picture doesn't look *that* bad.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=MnF7B3rD5VM", "img/xyaurora100_crash_thumb.jpg", "Aurora100 flight with crash" ],
    [ "https://www.youtube.com/watch?v=798ncBkBHos", "img/xyaurora100_owl_thumb.jpg", "Micro Quadcopter attacked by Owl" ]
])
%-->

Initially I tried the 1104 7000KV DYS motors, but they had problems with vibrations I couldn't fix with any soft-mounting solutions I've tried, and after tuning the filters with a blackbox.
I then swapped to the Eachine motors listed below, with them everything works perfectly with stock PID settings.

Also, at first I was using the [Eachine 25mW AIO Cam](https://www.banggood.com/Eachine-AIO-FPV-5_8G-25mW-48CH-VTX-600TVL-CMOS-1-or-4-inch-Camera-For-Aurora-90-100-RC-Drone-FPV-Racing-p-1122902.html?akmClientCountry=DE&p=3F201911077692015010&cur_warehouse=CN) with this build.
However, because I flew often simultaneously with friends, we decided to all switch to RunCams and TBS transmitters, as listed below.

## Parts List

These are the prices as recorded by Rotorbuilds.
To be honest, I have no clue if they are what I paid back when I built this copter.

<!--%
tableHelper([ "align-right", "align-last-right", "align-right"],
    [ "Part", "Description", "Cost" ], [
        [ "Frame", ("Eachine Aurora 100 100MM Mini Brushless FPV Multirotor Racing Frame 14.5g Carbon Fiber", "https://www.banggood.com/Eachine-Aurora-100-100MM-Mini-Brushless-FPV-Multirotor-Racing-Frame-14_5g-Carbon-Fiber-p-1133462.html?p=3F201911077692015010"), "11.99$" ],
        [ "Spare", ("Eachine Aurora 100 Mini Brushless FPV Racer Spare Part 2mm 2.5mm Bottom Plate 3K Carbon Fiber", "https://www.banggood.com/Eachine-Aurora-100-Mini-Brushless-FPV-Racer-Spare-Part-2mm-2_5mm-Bottom-Plate-3K-Carbon-Fiber-p-1144532.html?p=3F201911077692015010&cur_warehouse=CN&ID=529763"), "5.39$" ],
        [ "FC", ("Eachine Minicube 20x20mm F4 OSD Compatible Frsky Flysky DSM RX Blheli_S 10A For Aurora 68 90 100", "https://www.banggood.com/Eachine-Minicube-20x20mm-F4-OSD-Compatible-Frsky-Flysky-DSM-RX-Blheli_S-10A-For-Aurora-68-90-100-p-1165366.html?p=3F201911077692015010"), "60.99$" ],
        [ "Motors", ("4 x Eachine Upgrade Motor 1104 6500KV Brushless Motor 1-3S For Eachine Aurora 90 100 RC Drone FPV Racing", "https://www.banggood.com/Eachine-1104-6500KV-1-3S-Brushless-Motor-For-Eachine-Aurora-90-100-Mini-FPV-Racer-p-1138072.html?p=3F201911077692015010&cur_warehouse=CN"), "35.56$" ],
        [ "Props", ("10 Pairs Racerstar 1935 50mm 5 Blade Racing Propeller 1.5mm Mounting Hole For Micro FPV Frame", "https://www.banggood.com/10-Pairs-Racerstar-1935-50mm-5-Blade-Racing-Propeller-1_5mm-Mounting-Hole-For-Micro-FPV-Frame-p-1129109.html?p=3F201911077692015010"), "8.29$" ],
        [ "Cam", ("", ""), "$" ],
        [ "VTx", ("", ""), "$" ],
        [ "Bats", ("Tattu 450mAh 11.1V 75C 3S1P Lipo Battery Pack- Long Size for H Frame", "https://www.gensace.de/tattu-450mah-11-1v-75c-3s1p-lipo-battery-pack-long-size-for-h-frame.html"), "15.89$" ],
        [ "Misc", ("4 PCS Eachine Propeller Guard For Aurora 100 Mini FPV Racing RC Drone 1102 1103 1104 1105 Brushless Motor", "https://www.banggood.com/4-PCS-Eachine-Propeller-Guard-For-Aurora-100-Mini-FPV-Racing-RC-Drone-1102-1103-1104-1105-Brushless-Motor-p-1143685.html?akmClientCountry=DE&p=3F201911077692015010&cur_warehouse=CN&ID=224"), "2.49$" ],
        [ "", "Sum", "$" ]
    ]
)
%-->

This write-up was first published on [Rotorbuilds](https://rotorbuilds.com/build/5577).
