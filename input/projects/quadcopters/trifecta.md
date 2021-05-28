title: Tricopter
description: 3S LiPo, Quanum Trifecta frame, 2204 2300KV motors
parent: quadcopters
position: 60
date: 2016-05-25
---

<!--% backToParent() %-->

As a second attempt for a self-built copter I decided to try and build a Tricopter.
These only have three motors, with the third degree of freedom (yaw) being provided by tilting the back rotor using a servo.

<!--%
lightgallery([
    [ "img/trifecta_photo_1.jpg", "Top view" ],
    [ "img/trifecta_photo_2.jpg", "Front view" ],
    [ "img/trifecta_photo_4.jpg", "Top back right view" ],
    [ "img/trifecta_photo_3.jpg", "Top back left view" ],
    [ "img/trifecta_photo_5.jpg", "Yaw mechanism tilted" ],
    [ "img/trifecta_photo_8.jpg", "Folded up, side view" ]
])
%-->

Here are some recordings of the FPV footage.
Be aware that these videos are recorded from the received signal on the ground.
Not only can you see lots of interference and other HF problems, the loss of quality from the video recorder and the YouTube encoding is also very noticeable.
In real-life, the picture doesn't look *that* bad.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=OyqBxzw04xs", "img/xytrifecta_crash_yaw_thumb.jpg", "Quanum Trifecta Crash Yaw Mechanism"],
    [ "https://www.youtube.com/watch?v=e11Yb5sWEGo", "img/xytrifecta_crash_thumb.jpg", "Quanum Trifecta mysterious crash" ]
])
%-->

I quite like the Trifecta frame.
It can be folded down considerably for easier transportation and storage, while still being surprisingly sturdy.

You need to use a relatively small battery, otherwise the copter is too high up, the back foot not reaching the ground, balancing on the battery.
I printed a longer foot because of that.

I had some problems with the first servo I tried, but after switching to the metal gear servo listed below, the yaw mechanism has worked perfectly.

## Parts List

The prices listed below are just what I found while doing this page some years later, not the real prices I paid back then.

<!--%
tableHelper([ "align-right", "align-last-right", "align-right"],
    [ "Part", "Description", "Cost" ], [
        [ "Frame", ("Quanum Trifecta Mini Foldable Tricopter Frame", "https://hobbyking.com/en_us/quanum-trifecta-mini-foldable-tricopter-frame-kit.html"), "27.67€" ],
        [ "Servo", ("Emax ES09MD Digital Metallgetriebe Mini Servo", "https://www.premium-modellbau.de/emax-es09md-digital-metallgetriebe-mini-servo-15g-0-08s-2-6kg-kugellager-es08md"), "12.90€" ],
        [ "FC", ("AfroFlight Naze32 Rev6 Flight Controller (Acro)", "https://hobbyking.com/en_us/afroflight-naze32-rev6-flight-controller-acro.html"), "23.06€" ],
        [ "ESCs", ("3x ZTW Spider Series 18A OPTO Multi-Rotor ESC 2~4S (BLHeli/SimonK Firmware)", "https://hobbyking.com/de_de/ztw-spider-series-18a-opto-multi-rotor-esc-2-4s-blheli-simonk-firmware.html"), "24.99€" ],
        [ "Motors CW", ("2x Multistar Elite 2204-2300KV Multi-Rotor Motor 3-4S (CW Prop Adapter)", "https://hobbyking.com/en_us/multistar-elite-2204-2300kv-multi-rotor-motor-cw-prop-adapter.html"), "23.90€" ],
        [ "Motors CCW", ("1x Multistar Elite 2204-2300KV Multi-Rotor Motor 3-4S (CCW Prop Adapter)", "https://hobbyking.com/en_us/multistar-elite-2204-2300kv-multi-rotor-motor-ccw-prop-adapter.html"), "12.45€" ],
        [ "Props", ("10 Pairs LDARC 5x4.5x3 5045 5 Inch 3-Blade Propeller CW CCW", "https://www.banggood.com/10-Pairs-LDARC-5x4_5x3-5045-5-Inch-3-Blade-Propeller-CW-CCW-for-RC-FPV-Racing-Drone-p-1067877.html?cur_warehouse=CN&ID=223"), "6.95€" ],
        [ "Cam", ("Sony 700TVL PAL FPV Camera", "https://amzn.to/3i0cUh8"), "15.00€" ],
        [ "VTx", ("SkyZone TS5823 5.8GHz 32CH A/V 200mW Mini FPV Transmitter", "https://hobbyking.com/en_us/skyzone-ts5823-5-8ghz-32ch-a-v-200mw-mini-fpv-transmitter-v2.html"), "17.12€" ],
        [ "OSD", ("Minim OSD v1.1", "https://hobbyking.com/en_us/minim-osd-v1-1.html"), "19.79€" ],
        [ "Rx", ("FrSky D8R-XP 2.4Ghz Receiver (w/telemetry & CPPM)", "https://hobbyking.com/en_us/frsky-d8r-xp-2-4ghz-receiver-w-telemetry-cppm.html"), "25.66€" ],
        [ "Battery", ("Turnigy 1400mAh 3S 40C Lipo Pack w/XT60", "https://hobbyking.com/en_us/turnigy-1400mah-3s-40c-lipo-pack-w-xt60.html?queryID=&objectID=78388"), "13.42€" ],
        [ "OLED", ("128x64 I2C OLED", "https://amzn.to/3usYHMi"), "9.99€" ],
        [ "", "Sum", "232.90€" ]
    ]
)
%-->

Here are some more photos.

<!--%
lightgallery([
    [ "img/trifecta_photo_6.jpg", "Folded up, back view" ],
    [ "img/trifecta_photo_7.jpg", "Folded up, front view" ],
    [ "img/quanum_trifecta_1.jpg", "Front view with Xiaomi Yi" ],
    [ "img/quanum_trifecta_6.jpg", "3D printed electronics mount on top" ],
    [ "img/quanum_trifecta_4.jpg", "3D printed longer back leg, on copter" ],
    [ "img/quanum_trifecta_5.jpg", "3D printed longer back leg" ],
    [ "img/quanum_trifecta_7.jpg", "3D printed electronics mount" ],
    [ "img/quanum_trifecta_8.jpg", "Copter closed up" ],
    [ "img/quanum_trifecta_2.jpg", "Xiaomi Yi 3D printed holder" ],
    [ "img/quanum_trifecta_3.jpg", "Poorly 3D printed camera holder" ]
])
%-->
