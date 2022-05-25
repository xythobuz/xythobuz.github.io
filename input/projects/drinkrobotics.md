title: DrinkRobotics
description: Collection of various cocktail machine related things
parent: projects
position: 100
comments: true
---

## Ubabot

Starting in 2017, I did some work for the robot lab of the RWU.
There I got to know cocktail machines and later took part in [drinkrobotics](http://drinkrobotics.de/), where I did some work on our proper, big, cocktail machine Ubabot, [as seen on Hackaday / CCCamp2019](https://web.archive.org/web/20201108013437/https://hackaday.com/2019/08/22/ubabot-mixes-up-50-cocktails-to-quench-cccamp-thirst/).
It originally used relais to power the pumps, but we had a motor driver PCB that we wanted to use instead, [so I wrote a Firmware for it](https://github.com/drinkrobotics/avr_pump_board).
We got an award for this machine at Makerfaire Friedrichshafen, presented it at Makerfaire Hannover, visited the [Verschwörhaus Ulm](https://verschwoerhaus.de/) and various other events over the years.

### CCCamp2019

Here are some photos and videos of our tent at the CCCamp2019 summer hacker camp near Berlin.

[Project page on camp wiki](https://web.archive.org/web/20201025144323/https://events.ccc.de/camp/2019/wiki/Projects:UbaBot). [Hackaday feature](https://web.archive.org/web/20201108013437/https://hackaday.com/2019/08/22/ubabot-mixes-up-50-cocktails-to-quench-cccamp-thirst/).

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=rzQB0l1Imt4", "img/camp_hackaday_small.jpg", "Steffen demonstrating the machine for Hackaday" ],

    [ "https://www.youtube.com/watch?v=CsiNMK3guS0", "img/camp_machine_small.jpg", "One run of the machine at CCCamp2019" ],

    [ "img/ubabot_camp19_1.jpg", "Steffen demonstrating the machine for Hackaday" ],

    [ "img/ubabot_camp19_2.jpg", "Side view of the pumps, from Hackaday" ]
])
%-->

[Source](https://hackaday.com/2019/08/22/ubabot-mixes-up-50-cocktails-to-quench-cccamp-thirst/), by Mike Szczys.

### Verschwörhaus Ulm

Here are some photos and a video from when we were invited to Verschwörläum 2018 in Ulm.

<!--%
lightgallery([
    [ "https://upload.wikimedia.org/wikipedia/commons/c/c3/Ubabot%2C_Vslaeum_2018%2C_Ulm.webm", "video/webm", "img/ulm_machine_small.jpg", "img/ulm_machine.jpg", "The machine in operation" ],

    [ "img/ubabot_ulm_7.jpg", "Front view of the machine" ],
    [ "img/ubabot_ulm_2.jpg", "Side Front view of the machine" ],
    [ "img/ubabot_ulm_1.jpg", "Back view of the machine. The green PCB is the motor driver with my firmware." ],
    [ "img/ubabot_ulm_3.jpg", "A drink is poured" ],
    [ "img/ubabot_ulm_4.jpg", "A drink is poured" ],
    [ "img/ubabot_ulm_5.jpg", "A drink is poured" ],
    [ "img/ubabot_ulm_6.jpg", "A drink is poured" ]
])
%-->

[Source](https://commons.wikimedia.org/wiki/Category:Ubabot), by [Matti Blume](https://commons.wikimedia.org/wiki/User:MB-one), [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

### Makerfaire Friedrichshafen

In 2017, we rebuilt Ubabot as part of the Maker Challenge of the Makerfaire Friedrichshafen.

<!--%
lightgallery([
    [ "img/ubabot_makerfaire_1.jpg", "The winning teams with their cocktail machines" ],
    [ "img/ubabot_makerfaire_2.jpg", "Closer shot of this early Ubabot prototype" ]
])
%-->

[A video of our machine in action can be found on heise online](https://www.heise.de/make/meldung/Maker-Faire-Bodensee-2017-Cocktails-Cosplay-und-Casemodding-3772515.html#nav_im_wettbewerb_0) (scroll down).

### Stuff

I designed a 3D model for a cap enclosing the large open glass bottles we have for some ingredients. It is a 2-color model that can be printed with a dual-nozzle printer, or you can just leave out the "filling" and print it with a single-nozzle printer. The design [can be found in my Git Repo](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/cocktail-maschine).

<!--%
lightgallery([
    [ "img/drinkrobotics_deckel.png", "The 3D design of the bottle cap." ]
])
%-->

## Arduino-Cocktail

Also in 2017, as part of some experiments regarding dispensing drinks in a cocktail machine using carbon dioxide, I've built my own small Cubalibre machine.

It is built inside a 12x1l Coke box and powered by a 3S quadcopter LiPo battery.
The liquids are propelled using pressurized Co2 from a Sodastream cartridge with a proper pressure reducer (check eBay).
The dispension is controlled by four solenoid valves, operated using relais.
Custom built 3D printed [bottle cap adapters](https://www.thingiverse.com/thing:2445858) are used to pressurize coke bottles and take out the liquid.
Everything is controlled by an Arduino, with a small OLED display and three buttons as the user interface.

<!--%
lightgallery([
    [ "img/arduino_cocktail_12.jpg", "Front Top view of the machine" ],
    [ "img/arduino_cocktail_11.jpg", "Top view of the machine" ],
    [ "img/arduino_cocktail_8.jpg", "Electronics" ],
    [ "img/arduino_cocktail_7.jpg", "Electronics" ],
    [ "img/arduino_cocktail_5.jpg", "Solenoid valves" ],
    [ "img/arduino_cocktail_6.jpg", "Solenoid valves" ],
    [ "img/arduino_cocktail_9.jpg", "The two boards fit the box neatly." ],
    [ "img/arduino_cocktail_10.jpg", "There is still enough room for a battery and the pipework." ],
    [ "img/arduino_cocktail_13.jpg", "Back view of the UI" ],
    [ "img/arduino_cocktail_14.jpg", "My very professional Co2 distribution" ],
    [ "img/arduino_cocktail_1.jpg", "Some old notes for the project" ],
    [ "img/arduino_cocktail_2.jpg", "Some old notes for the project" ],
    [ "img/arduino_cocktail_3.jpg", "Some old notes for the project" ],
    [ "img/arduino_cocktail_4.jpg", "Some old notes for the project" ],
    [ "img/co2_pressure_reducer.jpg", "Example of a sodastream compatible Co2 pressure reducer" ]
])
%-->

The Arduino firmware can be found on [Github](https://github.com/drinkrobotics/Arduino-Cocktail).

This machine has also been presented next to Ubabot at Makerfaires in Friedrichshafen and Hannover.
It was used properly, to actually dispense drinks, at a birthday party.
Unfortunately I don't have any photos or videos of the machine being in use.
Also the Sodastream bottle and pressure reducer were only borrowed from a friend and I no longer have them.
