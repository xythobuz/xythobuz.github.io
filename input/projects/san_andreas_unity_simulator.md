title: GTA: San Andreas Unity Drone Simulator
description: Extremely rudimentary quadcopter sim based on SA:Unity
parent: projects
show_in_quadcopters: true
date: 2017-04-01
update: 2017-10-08
github: https://github.com/xythobuz/SanAndreasUnity/tree/sim
comments: true
---

After re-playing GTA:SA, and also because of my general interest in old games, I one day searched GitHub for projects related to GTA San Andreas.
This led me to the [San Andreas Unity project](https://github.com/in0finite/SanAndreasUnity).
I was very much interested in Quadcopters at the time, and I was also looking to gain some experience in working with Unity.
So I decided to attempt and [combine](https://github.com/xythobuz/SanAndreasUnity/tree/sim) the two topics.

Here is a video of the simulator in action.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=xUAy7KBpkOs", "img/gta_sa_unity_sim_thumb.jpg", "GTA: San Andreas - Drone Flight Simulator" ]
])
%-->

The "physics" "simulation" in my code is not working very well.
To reach the state that can be seen in the video above already took a lot of tweaking, and the result is obviously not optimal yet.

Together with my [SerialGamepad project](2015_12_20_serialgamepad.html) I was even able to fly in the SA:Unity sim with my usual quadcopter transmitter.

But my curiosity was satisfied at this point and I had no more interest in working on it further.

Here are some screenshots of San Andreas Unity without my quadcopter modifications.

<!--%
lightgallery([
    [ "img/gta_sa_unity_sim_1.png", "Standing player model" ],
    [ "img/gta_sa_unity_sim_2.png", "Debug UI visible" ],
    [ "img/gta_sa_unity_sim_3.png", "Player in car" ]
])
%-->

My fork of SanAndreasUnity can be found [on GitHub](https://github.com/xythobuz/SanAndreasUnity), the simulator experiments are [in the 'sim' branch](https://github.com/xythobuz/SanAndreasUnity/tree/sim).
