title: Flying Wing
description: 2S LiPo, Soaring Wing, 2206 2200KV motor
parent: quadcopters
position: 40
date: 2016-11-03
comments: true
---

<!--% backToParent() %-->

Only flying with quadcopters became a bit boring after a while, and I wanted to see if the skills I had aquired flying and building them could be transferred to other areas.
So I decided to build a very simple FPV V-Tail Flying Wing model airplane.

<!--%
lightgallery([
    [ "img/flying_wing_1.jpg", "Complete top view" ],
    [ "img/flying_wing_2.jpg", "Closer view of electronics" ],
    [ "img/flying_wing_3.jpg", "Closer view of Rx" ],
    [ "img/flying_wing_4.jpg", "Brace for flaps" ],
    [ "img/flying_wing_5.jpg", "Bottom view" ]
])
%-->

Here are some recordings of the FPV footage.
Be aware that these videos are recorded from the received signal on the ground.
Not only can you see lots of interference and other HF problems, the loss of quality from the video recorder and the YouTube encoding is also very noticeable.
In real-life, the picture doesn't look *that* bad.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=V5Z94si2BPE", "img/flying_wing_tree_crash_thumb.jpg", "Flying Wing Tree Landing" ],
    [ "https://www.youtube.com/watch?v=w2eUHNWF4U8", "img/flying_wing_lowlight_thumb.jpg", "Flying Wing in low light situation" ]
])
%-->

I pretty much used the parts suggested for the frame on the Hobbyking product page.
For FPV, I added a FatShark camera and transmitter kit, also from HobbyKind.

Because I did not really have any idea of what I am doing, the plane is very front-heavy.
It's always a bit of a hassle to get it launched by hand, but after two or three tries it usually flies.
I'm not using any Flight Controller on the plane, and I still haven't even set the trim on my transmitter properly, so I'm always holding the pitch pretty far back.
But, for my limited airplane knowledge, it seems to work relatively fine.

The power is not overwhelming, however, and because of the pusher configuration of the motor, it really is very loud.

It is however very resilient to damage.
I had a bad crash where my receiver just cut out completely, and it dropped straight down onto some unused train tracks.
That caused a huge crack in the middle, basically splitting it in two parts.
With some foam glue it was however very easy to repair.

## Parts List

The prices listed below are just what I found while doing this page some years later, not the real prices I paid back then.

<!--%
tableHelper([ "align-right", "align-last-right", "align-right monospaced"],
    [ "Part", "Description", "Cost" ], [
        [ "Frame", ("Combat/Slope Soaring Wing Kit (EPP Foam w/CF Tube) 1000mm", "https://hobbyking.com/en_us/combat-slope-soaring-wing-kit-epp-foam-w-cf-tube-1000mm.html"), "22.14€" ],
        [ "V-Mixer", ("TURNIGY Ultra Small V-Tail Mixer", "https://hobbyking.com/en_us/turnigy-v-tail-mixer-ultra-small.html?queryID=&objectID=23131"), "4.64€" ],
        [ "ESC", ("HobbyKing 20A (2~4S) ESC 3A UBEC", "https://hobbyking.com/en_us/hobbyking-20a-2-4s-esc-3a-ubec.html"), "9.53€" ],
        [ "Motor", ("rcINpower QAV 2206 2200KV Brushless Motor", "https://hobbyking.com/en_us/qav2206-2200kv-ccw.html"), "9.00€" ],
        [ "Servos", ("2x HobbyKing HK15178 Analog Servo 1.4kg / 0.10sec / 10g", "https://hobbyking.com/en_us/hobbykingtm-hk15178-analog-servo-1-4kg-0-09sec-10g.html"), "4.08€" ],
        [ "Prop", ("", ""), "€" ],
        [ "Cam", ("", ""), "€" ],
        [ "VTx", ("", ""), "€" ],
        [ "Rx", ("FrSky D4R-II 4ch 2.4Ghz ACCST Receiver (w/telemetry)", "https://hobbyking.com/en_us/frsky-d4r-ii-4ch-2-4ghz-accst-receiver-w-telemetry.html"), "21.60€" ],
        [ "Battery", ("", ""), "€" ],
        [ "", "Sum", "€" ]
    ]
)
%-->
