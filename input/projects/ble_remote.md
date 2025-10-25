title: Pico BLE Vape Remote
description: Replacement for S&B Vaporizer app
parent: projects
git: https://codeberg.org/xythobuz/Volcano-Remote
github: https://github.com/xythobuz/Volcano-Remote
date: 2024-12-07
comments: true
---

Like many modern devices, some of the medical vaporizer devices from S&B (the [Crafty](https://www.storz-bickel.com/de/crafty-plus-c), [Venty](https://www.storz-bickel.com/de/venty) and the [Volcano Hybrid](https://www.storz-bickel.com/de/volcanohybrid)) offer Bluetooth connectivity and [an app](https://app.storz-bickel.com/) to control them.

Unfortunately the official mobile apps have / had some problems.
The iOS version is no longer available after Apple decided to remove "drug related" Apps.
So understandably the company no longer developed either their iOS or Android apps, instead releasing a web app that uses the Chrome Bluetooth APIs.

Yet all of these variants are problematic in different ways.
The Android app offers customizable workflows for the Volcano Hybrid.
But the Bluetooth implementation is very wonky, sometimes simply missing steps in the workflow.
And because there's no error checking, the workflow simply continues in a broken state.
The webapp doesn't have this problem, but instead the workflows are no longer customizable, instead just offering a small number of hard-coded pre-defined workflows.

This is not satisfying, of course, and also presented itself as a great opportunity to play around with BLE.

Fortunately the official web app is made with non-minimized an unobfuscated JavaScript, so the BLE protocol for the different devices can easily be reverse engineered.
I wrote a small [script](https://codeberg.org/xythobuz/Volcano-Remote/src/branch/master/web-app/fetch.sh) that helps with downloading and beautifying the official sources.

As a first attempt I implemented the Volcano workflow functionality in Python on the PC.
I had some problems, so I made two implementations, with [bleak](https://bleak.readthedocs.io/en/latest/) and [SimplePyBLE](https://simpleble.readthedocs.io/en/latest/simplepyble/usage.html).
Turns out my difficulties came from having multiple bluetooth adapters on my Linux machine.
Now the scripts both work fine for me.

<!--%
lightgallery([
    [ "img/volcano_remote_pc_2.jpg", "Volcano Remote script in action (old version)" ],
    [ "img/volcano_remote_pc_1.png", "Volcano Remote script in action (current version)" ],
])
%-->

Then I implemented the same thing on a [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#raspberry-pi-pico-w-and-pico-wh), with a [Waveshare Pico LCD 1.3](https://www.waveshare.com/wiki/Pico-LCD-1.3) display.
I first did this in MicroPython but ran into issues as well.
It works fine but I couldn't include all the functionality I wanted.

<!--%
lightgallery([
    [ "img/volcano_remote_micropython.jpg", "Volcano Remote MicroPython prototype" ],
])
%-->

So I made a fourth iteration, this time in C with the plain Pico SDK.
It can interact with the Volcano Hybrid, the Crafty and the Venty.
Everything can be controlled using on-screen menus on the device itself.
It even has a WiFi capable OTA bootloader to support wireless firmware upgrades.

<!--%
lightgallery([
    [ "img/volcano_remote_c_dev.jpg", "Volcano Remote C version in development" ],
    [ "img/volcano_remote_bootloader.jpg", "Volcano Remote WiFi Bootloader" ],
])
%-->

To contain everything I designed a snug little 3D-printed case in OpenSCAD.
It contains the Pico W, a [Pico LiPo Shim](https://shop.pimoroni.com/products/pico-lipo-shim?variant=32369543086163) and a ["80mAh / 20 x 11 x 5mm / 501220" LiPo battery](https://www.ebay.de/itm/255510046348?var=555462939784).
The Pi is mounted with four screws and the battery is held onto it with a drop of hot glue.
Then the LCD board just plugs on top to close it.

<!--%
lightgallery([
    [ "img/volcano_remote_case_1.jpg", "Volcano Remote case assembly" ],
    [ "img/volcano_remote_case_2.jpg", "Volcano Remote case opened" ],
    [ "img/volcano_remote_case_3.jpg", "Volcano Remote case power button" ],
])
%-->

This is what the final result looks like.

<!--%
lightgallery([
    [ "img/volcano_remote_case_4.jpg", "Volcano Remote (final)" ],
])
%-->

I'm quite happy with it, especially the software part.
It has many things I expect from nice modern embedded projects, and I've used a bunch of libraries to achieve these:

  * [Pico SDK](https://github.com/raspberrypi/pico-sdk) for working with the Pico
    * [TinyUSB](https://github.com/hathach/tinyusb) for the USB device implementation
    * [BTstack](https://github.com/bluekitchen/btstack) for the Bluetooth connection
  * [FatFS](https://github.com/abbrev/fatfs) for the USB filesystem
  * [MCUFont](https://github.com/mcufont/mcufont) for rendering text
  * [st7789](https://github.com/hepingood/st7789) for interacting with the LCD
  * [picowota](https://github.com/usedbytes/picowota) bootloader ([modified](https://github.com/xythobuz/picowota) to work with the Flash config storage and LCD)

As usual you can find everything on [Codeberg](https://codeberg.org/xythobuz/Volcano-Remote) and on [GitHub](https://github.com/xythobuz/Volcano-Remote).
