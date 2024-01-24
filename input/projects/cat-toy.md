title: Cat Toy
description: Laser pointer on two servos with Raspberry Pi Pico W
parent: projects
git: https://git.xythobuz.de/thomas/CatToy
github: https://github.com/xythobuz/CatToy
date: 2023-04-22
comments: true
---

I never wanted to own pets.
Having to look after an aquarium when I was a child was more then enough to put me off of this thought.
Nonetheless, for complicated reasons beyond the scope of this article, I now find myself living with two cats.
This requires some adjustments to my flat. 👷

<!--%
lightgallery([
    [ "img/cats_1.jpg", "Ares sitting on my 3D printer" ],
    [ "img/cats_2.jpg", "Aphrodite sitting on my 3D printer" ],
    [ "img/cats_3.jpg", "Aphrodite sitting on my laser engraver" ],
    [ "img/cats_4.jpg", "Ares and Aphrodite sharing my printer tower" ],
])
%-->

Obviously I had to come up with some kind of gadget to help me keep them occupied.

<!--%
lightgallery([
    [ "img/cat_toy.mp4", "video/mp4", "", "", "Demonstration video" ],
    [ "img/cat_toy_2.jpg", "Servos and laser diode" ],
    [ "img/cat_toy_1.jpg", "View inside box" ],
])
%-->

So on the afternoon of easter monday I took a plunge into my parts bins and built this device.
Getting to an initial workable prototype, both hardware and software wise, only took about 4 to 6 hours.
It consists of two RC micro servos and a laser pointer diode mounted to each other.
They are controlled by an RP2040 on a Raspberry Pi Pico board.
The servos were spare parts for a model aircraft build.
The laser diodes I bought a whole bunch of from china a long time ago.
The batteries came out of a cheap chinese headlamp.

If you were to buy all the parts, the shopping list could look something like this:

<!--%
tableHelper([ "align-right", "align-right", "align-right", "align-left", "align-right monospaced" ],
    [ "Description", "Type", "Count", "Link", "Price" ], [
        [ "MCU", "Raspberry Pi Pico W", "1x", "<a href=\"https://www.berrybase.de/raspberry-pi-pico-w-rp2040-wlan-mikrocontroller-board\">BerryBase</a>", "6.90€" ],
        [ "Servo", "MG90S", "2x", "<a href=\"https://www.roboter-bausatz.de/p/mg90s-micro-servo-motor\">Roboter-Bausatz</a>", "7.90€" ],
        [ "Laser Diode", "650nm 5V 5mW", "1x", "<a href=\"https://www.radiomag.com.de/product/mini-650nm-6mm-5v-5mw-laser-dot-diode-module-head-wl-red-laser-led_58363.html\">Radiomag</a>", "1.40€" ],
        [ "Battery", "18650 Li-Ion 3.7V 2900mAh", "2x", "<a href=\"https://www.akkuteile.de/en/bak-n18650cnp-2500mah-3-6-3-7v-li-ion-battery-20a-discharge-current_100846_3093\">AkkuTeile</a>", "9.38€" ],
        [ "Holder", "18650 holder", "2x", "<a href=\"https://www.akkuteile.de/en/battery-holder-for-1x-18650-cell-with-connector_400422_1454\">AkkuTeile</a>", "2.58€" ],
        [ "DC-DC", "LM2596 step-down module", "1x", "<a href=\"https://www.makershop.de/module/step-downup/lm2596-step-down/\">MakerShop</a>", "1.70€" ],
        [ "Sum", "", "", "", "~30.00€" ]
    ]
)
%-->

I also added a power switch, a push button and an LED (with resistor) as a physical user interface.
To measure the battery voltage I used a simple voltage divider made out of an 18kΩ and a 10kΩ resistor.
There's also a micro USB connector and some male and femal dupont connectors as well as some copper wire in there.
It's not really economical to buy these in single quantities, so I didn't list them above.

The case of the device is made out of a recycled cardboard box, with some holes poked into it and some hot glue.
I really like this method of prototyping electronics.
It's easily available, quick, cheap and relatively sturdy.

<!--%
lightgallery([
    [ "img/cat_toy_3.jpg", "Buttons" ],
    [ "img/cat_toy_4.jpg", "PCB" ],
])
%-->

This time I used [MicroPython](https://docs.micropython.org/en/latest/rp2/quickref.html) again to build the software.
Is it my second time using it, after [the MCH2022 cocktail machine badge app](2022_07_29_MCH2022.html#app).
It was a little bit more complicated to first get my head around it, compared to the usual C/C++ firmwares, and I was not able to figure out an easy way for OTA firmware updates yet.
But in the end it was much quicker to build a working prototype with it.
I recommend using [rshell](https://github.com/dhylands/rshell), there's also a small script for it [in my repo](https://git.xythobuz.de/thomas/CatToy/src/branch/master/copy.sh) to use it to copy the firmware to the device.

The RP2040 continues to be a delight to work with!
I really like the available tools and documentation.
Getting started with a working firmware prototype was unbelievably quick, even including "advanced" features like WiFi and an HTTP interface.
All without any strange Cloud IDEs or similar stuff (*cough* Arduino).

<!--%
lightgallery([
    [ "img/cat_toy_web.png", "Webinterface of the Cat Toy" ],
])
%-->

The laser diode is PWM controlled and I only run it at 10%, and on top of that with 3.3V instead of 5V.
It is still more than bright enough.
The webinterface also shows the console output of the script, which is very useful for debugging issues that happen while no USB cable to a PC is connected.
Everything can be controlled using the webinterface.
For ease of use, the LED in the box blinks the index number of the currently selected set of servo angle limits.
With a short button press, the selected index is cycled through.
With a long button press, the currently selected index is used to start movements and turn on the diode.
By configuring different limits, the movements of the laser dot can be constrained, depending on where the device is placed, so the cats don't run into furniture or similar stuff.

Of course this concept could be extended much further.
On the technical side, a nice 3D-printed enclosure would go a long way.
There are [a couple of examples](https://www.printables.com/search/models?q=laser+cat+toy) out there for inspiration.
Currently the servos are simply commanded some random angles in a specified range.
This could be "linearized" so the laser dot is moving similar distances everywhere on the ground, by including the height of the device above ground in the calculation.
If this were to be paired with some kind of webcam, maybe with vision detection, the capabilities of the system could be greatly enhanced, for example to avoid shining the dot onto the cats body, where it doesn't notice it usually.
Also, remotely controlling the device via eg. a Telegram Bot interface could be useful to play with the cats while not at home.
And of course the webinterface could be made to look much prettier.
But I don't think I will implement any of this to be honest, it already does the job well enough for me 😅
