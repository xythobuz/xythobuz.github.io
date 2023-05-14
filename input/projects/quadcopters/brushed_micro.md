title: Brushed Micro
description: 1S LiPo brushed copter with 3D printed frame
parent: quadcopters
position: 50
date: 2016-10-09
update: 2022-05-24
git: https://git.xythobuz.de/thomas/copter-configs/src/branch/master/2_brushed
comments: true
---

<!--% backToParent() %-->

Because I did not really feel comfortable with the large size of both [my first copter](x666.html) and [my tricopter](trifecta.html), I decided to build a very small and lightweight 1S brushed quadcopter.
The frame is 3D printed, but because it did not fit [my 3D printer at the time](fabrikator-mini.html) I had to order it online.

<!--%
lightgallery([
    [ "img/brushed_micro_1.jpg", "Front view" ],
    [ "img/brushed_micro_2.jpg", "Rear view" ],
    [ "img/brushed_micro_3.jpg", "Bottom view" ]
])
%-->

Here are some recordings of the FPV footage.
Be aware that these videos are recorded from the received signal on the ground.
Not only can you see lots of interference and other HF problems, the loss of quality from the video recorder and the YouTube encoding is also very noticeable.
In real-life, the picture doesn't look *that* bad.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=t0mPxgY_MKY", "img/xybrushed_test_thumb.jpg", "Brushed Copter Test Flight" ]
])
%-->

As you can probably tell from the pictures, I was a bit scared about my first AIO cam with a soldered-on antenna.
After I had to re-solder a new one once, I covered it in copious amounts of hotglue, to avoid crash damage.
It seems to work.

To mount the battery to the frame I used a small piece of 3M Dual Lock on both the copter and all of my batteries.

## Parts List

The prices listed below are just what I found while doing this page some years later, not the real prices I paid back then.

<!--%
tableHelper([ "align-right", "align-last-right", "align-right monospaced"],
    [ "Part", "Description", "Cost" ], [
        [ "Frame", ("Oskie Micro Frame v1", "https://oscarliang.com/oskie-micro-frame-v1/"), "10.00€" ],
        [ "FC", ("Sp Racing F3 Evo Brushed", "https://www.eachine.com/Eachine-32bits-F3-Brushed-Flight-Control-Board-With-NMOS-transistors-Based-On-SP-RACING-F3-EVO-p-558.html"), "10.24€" ],
        [ "Rx", ("RX-F802", "https://www.banggood.com/DIY-RX-F802-7CH-Receiver-for-FRSKY-X9D-X9D-Plus-Transmitter-DJI-DFT-DHT-p-989610.html?cur_warehouse=CN"), "19.97€" ],
        [ "Motors", ("4x 8.5mm x 20mm Brushed Motor", "https://amzn.to/3yVjwWq"), "12.99€" ],
        [ "Props", ("55mm Brushed Props", "https://amzn.to/3GgJeGE"), "8.99€" ],
        [ "Cam", ("FX797T", "https://de.aliexpress.com/item/32711051980.html?gatewayAdapt=glo2deu"), "22.71€" ],
        [ "Battery", ("Turnigy nano-tech 1S 750mAh", "https://hobbyking.com/en_us/turnigy-nano-tech-750mah-1s-35-70c-lipo-pack-fits-nine-eagles-solo-pro-180.html?___store=en_us"), "4.06€" ],
        [ "", "Sum", "88.96€" ]
    ]
)
%-->

You can find my Betaflight configuration dumps [here](https://git.xythobuz.de/thomas/copter-configs/src/branch/master/2_brushed).
