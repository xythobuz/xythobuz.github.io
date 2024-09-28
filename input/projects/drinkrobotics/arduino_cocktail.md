title: Arduino-Cocktail
description: CO₂ driven experimental cocktail machine
parent: drinkrobotics
position: 500
comments: true
github: https://github.com/drinkrobotics/Arduino-Cocktail
date: 2017-07-22
update: 2021-03-25
---

<!--% backToParent() %-->

Also in 2017, as part of some experiments regarding dispensing drinks in a cocktail machine using carbon dioxide, I've built my own small Cubalibre machine.

It is built inside a 12x1l Coke box and powered by a 3S quadcopter LiPo battery.
The liquids are propelled using pressurized CO₂ from a Sodastream cartridge with a proper pressure reducer (check eBay).
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
    [ "img/arduino_cocktail_14.jpg", "My very professional CO₂ distribution" ],
    [ "img/arduino_cocktail_1.jpg", "Some old notes for the project" ],
    [ "img/arduino_cocktail_2.jpg", "Some old notes for the project" ],
    [ "img/arduino_cocktail_3.jpg", "Some old notes for the project" ],
    [ "img/arduino_cocktail_4.jpg", "Some old notes for the project" ],
    [ "img/co2_pressure_reducer.jpg", "Example of a sodastream compatible CO₂ pressure reducer" ]
])
%-->

The Arduino firmware can be found on [Github](https://github.com/drinkrobotics/Arduino-Cocktail).

This machine has also been presented next to Ubabot at Makerfaires in Friedrichshafen and Hannover.
It was used properly, to actually dispense drinks, at a birthday party.
Unfortunately I don't have any photos or videos of the machine being in use.
Also the Sodastream bottle and pressure reducer were only borrowed from a friend and I no longer have them.
