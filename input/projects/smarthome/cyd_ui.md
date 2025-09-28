title: CYD MQTT Touchscreen UI
description: Using the Cheap-Yellow-Display to control smart home devices
parent: smarthome
second_parent: projects
position: 375
git: https://codeberg.org/xythobuz/esp-env
github: https://github.com/xythobuz/esp-env
date: 2025-09-28
comments: true
---

<!--% backToParent() %-->

After adding more actors to my Smart Home in the form of power sockets running [Tasmota](https://tasmota.github.io/docs/), I had to improve the ways to control all of these devices.
The [Telegram Bot](mqtt_telegram.html) and [Web UI](mqtt_web.html) are a good start, but the Wife Acceptance Factor is pretty low, and they require access to a computer or smartphone.

Recently I learned about the [CYD (cheap yellow display)](https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display), a nice ESP32 dev board with a touchscreen.
This seemed ideal to run a simple user interface to control everything via MQTT.

Here are the results.
When not in use the device shows a stand-by screen with the current time and date.
After pressing the screen a menu is shown.

<!--%
lightgallery([
    [ "img/cyd_3.jpg", "Livingroom unit, on standy screen" ],
    [ "img/cyd_4.jpg", "Livingroom unit, on menu screen" ],
])
%-->

I mounted multiple of these units in different places.
They can be updated easily over-the-air.

<!--%
lightgallery([
    [ "img/cyd_5.jpg", "Workbench unit" ],
    [ "img/cyd_6.jpg", "Bathroom unit" ],
])
%-->

To get the LDR on the device to work properly, so the screen brightness can be adjusted to the environment lighting conditions, you need to modify the hardware a bit.
I removed R19 and replaced R15 with a 100k resistor.
The top board in the following image is in the original state, the bottom board has already been modified.

<!--%
lightgallery([
    [ "img/cyd_2.jpg", "LDR resistor fix, top original, bottom modified" ],
])
%-->

The CYD code has been integrated into my [ESP-Env project](espenv.html) and [repo](https://codeberg.org/xythobuz/esp-env).
