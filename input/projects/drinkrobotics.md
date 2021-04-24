title: DrinkRobotics
description: Collection of various cocktail machine related things
parent: projects
position: 9
---

## Ubabot

Starting in 2017, I did some work for the robot lab of the RWU.
There I got to know cocktail machines and later took part in [drinkrobotics](http://drinkrobotics.de/), where I did some work on our proper, big, cocktail machine Ubabot, [as seen on Hackaday / CCCamp2019](https://web.archive.org/web/20201108013437/https://hackaday.com/2019/08/22/ubabot-mixes-up-50-cocktails-to-quench-cccamp-thirst/).
It originally used relais to power the pumps, but we had a motor driver PCB that we wanted to use instead, [so I wrote a Firmware for it](https://github.com/drinkrobotics/avr_pump_board).
We got an award for this machine at Makerfaire Friedrichshafen, presented it at Makerfaire Hannover, visited the [Verschwörhaus Ulm](https://verschwoerhaus.de/) and various other events over the years.

### CCCamp2019

Here are some photos and videos of our tent at the CCCamp2019 summer hacker camp near Berlin.

[Project page on camp wiki](https://web.archive.org/web/20201025144323/https://events.ccc.de/camp/2019/wiki/Projects:UbaBot). [Hackaday feature](https://web.archive.org/web/20201108013437/https://hackaday.com/2019/08/22/ubabot-mixes-up-50-cocktails-to-quench-cccamp-thirst/).

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/rzQB0l1Imt4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CsiNMK3guS0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div class="lightgallery">
    <a href="img/ubabot_camp19_1.jpg">
        <img src="img/ubabot_camp19_1_small.jpg" alt="Steffen demonstrating the machine for Hackaday">
    </a>
    <a href="img/ubabot_camp19_2.jpg">
        <img src="img/ubabot_camp19_2_small.jpg" alt="Side view of the pumps, from Hackaday">
    </a>
</div>

[Source](https://hackaday.com/2019/08/22/ubabot-mixes-up-50-cocktails-to-quench-cccamp-thirst/), by Mike Szczys.

### Verschwörhaus Ulm

Here are some photos and a video from when we were invited to Verschwörläum 2018 in Ulm.

<iframe src="https://commons.wikimedia.org/wiki/File:Ubabot,_Vslaeum_2018,_Ulm.webm?embedplayer=yes" width="560" height="315" frameborder="0" ></iframe>

<div class="lightgallery">
    <a href="img/ubabot_ulm_7.jpg">
        <img src="img/ubabot_ulm_7_small.jpg" alt="Front view of the machine">
    </a>
    <a href="img/ubabot_ulm_2.jpg">
        <img src="img/ubabot_ulm_2_small.jpg" alt="Side Front view of the machine">
    </a>
    <a href="img/ubabot_ulm_1.jpg">
        <img src="img/ubabot_ulm_1_small.jpg" alt="Back view of the machine. The green PCB is the motor driver with my firmware.">
    </a>
    <a href="img/ubabot_ulm_3.jpg">
        <img src="img/ubabot_ulm_3_small.jpg" alt="A drink is poured">
    </a>
    <a href="img/ubabot_ulm_4.jpg">
        <img src="img/ubabot_ulm_4_small.jpg" alt="A drink is poured">
    </a>
    <a href="img/ubabot_ulm_5.jpg">
        <img src="img/ubabot_ulm_5_small.jpg" alt="A drink is poured">
    </a>
    <a href="img/ubabot_ulm_6.jpg">
        <img src="img/ubabot_ulm_6_small.jpg" alt="A drink is poured">
    </a>
</div>

[Source](https://commons.wikimedia.org/wiki/Category:Ubabot), by [Matti Blume](https://commons.wikimedia.org/wiki/User:MB-one), [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

### Makerfaire Friedrichshafen

In 2017, we rebuilt Ubabot as part of the Maker Challenge of the Makerfaire Friedrichshafen.

<div class="lightgallery">
    <a href="img/ubabot_makerfaire_1.jpg">
        <img src="img/ubabot_makerfaire_1_small.jpg" alt="The winning teams with their cocktail machines">
    </a>
    <a href="img/ubabot_makerfaire_2.jpg">
        <img src="img/ubabot_makerfaire_2_small.jpg" alt="Closer shot of this early Ubabot prototype">
    </a>
</div>

[A video of our machine in action can be found on heise online](https://www.heise.de/make/meldung/Maker-Faire-Bodensee-2017-Cocktails-Cosplay-und-Casemodding-3772515.html#nav_im_wettbewerb_0) (scroll down).

### Stuff

I designed a 3D model for a cap enclosing the large open glass bottles we have for some ingredients. It is a 2-color model that can be printed with a dual-nozzle printer, or you can just leave out the "filling" and print it with a single-nozzle printer. The design [can be found in my Git Repo](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/cocktail-maschine).

<div class="lightgallery">
    <a href="img/drinkrobotics_deckel.png">
        <img src="img/drinkrobotics_deckel_small.png" alt="The 3D design of the bottle cap.">
    </a>
</div>

## Arduino-Cocktail

Also in 2017, as part of some experiments regarding dispensing drinks in a cocktail machine using carbon dioxide, I've built my own small Cubalibre machine.

It is built inside a 12x1l Coke box and powered by a 3S quadcopter LiPo battery.
The liquids are propelled using pressurized Co2 from a Sodastream cartridge with a proper pressure reducer (check eBay).
The dispension is controlled by four solenoid valves, operated using relais.
Custom built 3D printed [bottle cap adapters](https://www.thingiverse.com/thing:2445858) are used to pressurize coke bottles and take out the liquid.
Everything is controlled by an Arduino, with a small OLED display and three buttons as the user interface.

<div class="lightgallery">
    <a href="img/arduino_cocktail_12.jpg">
        <img src="img/arduino_cocktail_12_small.jpg" alt="Front Top view of the machine">
    </a>
    <a href="img/arduino_cocktail_11.jpg">
        <img src="img/arduino_cocktail_11_small.jpg" alt="Top view of the machine">
    </a>
    <a href="img/arduino_cocktail_8.jpg">
        <img src="img/arduino_cocktail_8_small.jpg" alt="Electronics">
    </a>
    <a href="img/arduino_cocktail_7.jpg">
        <img src="img/arduino_cocktail_7_small.jpg" alt="Electronics">
    </a>
    <a href="img/arduino_cocktail_5.jpg">
        <img src="img/arduino_cocktail_5_small.jpg" alt="Solenoid valves">
    </a>
    <a href="img/arduino_cocktail_6.jpg">
        <img src="img/arduino_cocktail_6_small.jpg" alt="Solenoid valves">
    </a>
    <a href="img/arduino_cocktail_9.jpg">
        <img src="img/arduino_cocktail_9_small.jpg" alt="The two boards fit the box neatly.">
    </a>
    <a href="img/arduino_cocktail_10.jpg">
        <img src="img/arduino_cocktail_10_small.jpg" alt="There is still enough room for a battery and the pipework.">
    </a>
    <a href="img/arduino_cocktail_13.jpg">
        <img src="img/arduino_cocktail_13_small.jpg" alt="Back view of the UI">
    </a>
    <a href="img/arduino_cocktail_14.jpg">
        <img src="img/arduino_cocktail_14_small.jpg" alt="My very professional Co2 distribution">
    </a>
    <a href="img/arduino_cocktail_1.jpg">
        <img src="img/arduino_cocktail_1_small.jpg" alt="Some old notes for the project">
    </a>
    <a href="img/arduino_cocktail_2.jpg">
        <img src="img/arduino_cocktail_2_small.jpg" alt="Some old notes for the project">
    </a>
    <a href="img/arduino_cocktail_3.jpg">
        <img src="img/arduino_cocktail_3_small.jpg" alt="Some old notes for the project">
    </a>
    <a href="img/arduino_cocktail_4.jpg">
        <img src="img/arduino_cocktail_4_small.jpg" alt="Some old notes for the project">
    </a>
    <a href="img/co2_pressure_reducer.jpg">
        <img src="img/co2_pressure_reducer_small.jpg" alt="Example of a sodastream compatible Co2 pressure reducer">
    </a>
</div>

The Arduino firmware can be found on [Github](https://github.com/drinkrobotics/Arduino-Cocktail).

This machine has also been presented next to Ubabot at Makerfaires in Friedrichshafen and Hannover.
It was used properly, to actually dispense drinks, at a birthday party.
Unfortunately I don't have any photos or videos of the machine being in use.
Also the Sodastream bottle and pressure reducer were only borrowed from a friend and I no longer have them.
