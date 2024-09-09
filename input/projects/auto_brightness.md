title: AutoBrightness
description: USB ambient light sensor for DDC/CI backlight control
parent: projects
git: https://git.xythobuz.de/thomas/AutoBrightness
github: https://github.com/xythobuz/AutoBrightness
date: 2024-09-07
update: 2024-09-09
comments: true
---

One of my two ~10 year old 23" 1080p main displays died recently.
So I finally upgraded to two used 27" 1440p displays.
These are now the first displays on my desktop that allow adjustments of the backlight from software.
So I tried to find out how to go about that.

Turns out on laptops both the display backlight intensity and the ambient light sensors are controlled via ACPI, with proper kernel support already available (see eg. the [Arch Wiki](https://wiki.archlinux.org/title/Backlight)).

But on desktops no standard for ambient light sensors seems to be established.
Instead of ACPI, the backlight of some desktop monitors can be controlled using [DDC/CI](https://en.wikipedia.org/wiki/Display_Data_Channel#DDC/CI).

There are some projects, both [hardware](https://www.yoctopuce.com/EN/products/usb-environmental-sensors/yocto-light-v3) and [software](https://github.com/FedeDP/Clight), available for this already.
But as usual I decided to make my own.

## Prototype Hardware

Initially I tought I could just go the most simple route and use an LDR on the ADC of an MCU.
I already had a [Digispark Rev. 3 clone](https://www.az-delivery.de/en/products/digispark-board), LDR, resistor and potentiometer on hand.

But deep down I already knew this would not be good.

<!--%
lightgallery([
    [ "img/autobrightness_ldr_1.jpg", "Front view of AutoBrightness prototype" ],
    [ "img/autobrightness_ldr_2.jpg", "Back view of AutoBrightness prototype" ],
])
%-->

The range of LDRs is far too big to easily measure the human eye dynamic range with an ADC.
You can extend the range by switching different resistor values into your voltage divider using GPIOs, but I didn't want to go that far.
Instead I added a 1M potentiometer to manually adjust the measurement range.

This gave me an opportunity to play around with integer low pass filters using bit shifts, as described [here](https://www.infineon.com/dgdl/Infineon-AN2099_PSoC_1_PSoC_3_PSoC_4_and_PSoC_5LP_Single_Pole_Infinite_Impulse_Response_%28IIR%29_Filters-ApplicationNotes-v11_00-EN.pdf?fileId=8ac78c8c7cdc391c017d072cde6e51bd) (which I got from [here](https://stackoverflow.com/a/38927630)).

So as suspected, the resulting values were not able to measure both a dark room at night and a sunny day.

## Proper Hardware

To get usable values I had to use a "real" sensor.

The final hardware is just a [Digispark Rev. 3 clone](https://www.az-delivery.de/en/products/digispark-board) with a [GY-302 breakout board (for the BH1750 sensor)](https://www.az-delivery.de/en/products/gy-302-bh1750-lichtsensor-lichtstaerke-modul-fuer-arduino-und-raspberry-pi) connected to it.

<!--%
lightgallery([
    [ "img/autobrightness_pcb_1.jpg", "Front view of AutoBrightness device" ],
    [ "img/autobrightness_pcb_2.jpg", "Back view of AutoBrightness device" ],
])
%-->

The [BH1750](https://www.mouser.com/datasheet/2/348/bh1750fvi-e-186247.pdf) is a nice small ambient light sensor and very easy to use.
This is literally the whole driver I wrote.

<pre class="sh_c">
void luxInit(void) {
    twiWrite(LUX_ADDR, OP_POWER_ON); // reset registers
    twiWrite(LUX_ADDR, OP_CONT_0_5X); // continuous measurement at 0.5lx resolution
}

uint16_t luxGet(void) {
    uint16_t val = twiRead(LUX_ADDR); // read measurement
    return val;
}
</pre>

## USB Communication

The Digispark has the USB D+ and D- signals directly connected to GPIOs of the AtTiny85.
So the USB protocol is bit-banged using the [V-USB library](https://github.com/obdev/v-usb).
Because I did not use the Arduino Cores already available, I had to do some [fiddling](https://git.xythobuz.de/thomas/AutoBrightness/commit/d50da00006edd87d9363d83befc8eb5bc9274fb5) to configure the library properly for this device.

The code is based on the [custom-class example](https://github.com/obdev/v-usb/tree/master/examples/custom-class) from V-USB.
This abuses USB control transfers to transmit data.

On the PC side I'm using [PyUSB](https://github.com/pyusb/pyusb) instead of going to libusb directly, as in the example.

<pre class="sh_python">
CUSTOM_RQ_GET = 2 # get ldr value

def is_target_device(dev):
    if dev.manufacturer == "xythobuz.de" and dev.product == "AutoBrightness":
        return True
    return False

dev = usb.core.find(idVendor=0x16c0, idProduct=0x05dc, custom_match=is_target_device)
dev.set_configuration()

r = dev.ctrl_transfer(usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_IN, CUSTOM_RQ_GET, 0, 0, 2)
val = int.from_bytes(r, "little")
</pre>

To run this without root permissions you need to add a udev rule (in eg. `/etc/udev/rules.d/49-autobrightness.rules`).

    SUBSYSTEMS=="usb", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="05dc", ATTRS{manufacturer}=="xythobuz.de", ATTRS{product}=="AutoBrightness", MODE:="0666"

I'm using the shared V-USB vendor and product IDs, so I [have to](https://github.com/obdev/v-usb/blob/master/usbdrv/USB-IDs-for-free.txt) always do the matching using my manufacturer and product strings as well.

## Prototype Client

With the hardware side out of the way the next step was adjusting the display brightness.
I made a [short prototype](https://git.xythobuz.de/thomas/AutoBrightness/commit/6fcab3b981bb5705028e1dd0f3b52e4eed609253) using [ddcutil](https://www.ddcutil.com/) to set the values.

To calculate the resulting values I made some measurements at midday (~500 lux) and night (~50 lux).
And I thought about my habits (the MSI display seems ~10% brighter than the HP).

<pre class="sh_python">
c_in = 0.6, -60.0, # in_a, in_b
calibration = {
    "HPN:HP 27xq:CNK1072BJY": [
        1.0, 30.0, # out_a, out_b
    ],

    "MSI:MSI G27CQ4:": [
        1.0, 20.0, # out_a, out_b
    ],
}

def cal(v, c):
    # out = out_b + out_a * in_a * max(0, in_b + in)
    return c[1] + c[0] * c_in[0] * max(0, c_in[1] + v)
</pre>

This simple formula gives surprisingly good results.
To avoid noticable noisy changes I do some simple low-pass filtering of the sensor values.

<pre class="sh_python">
filter_fact = 0.9

def filter_lux(old, new):
    return (old * filter_fact) + (new * (1.0 - filter_fact))
</pre>

All this just runs once per second.

Unfortunately, using ddcutil to adjust the brightness causes a noticable stutter of the whole system each time the value is changed.
So this is not a good long-term solution.

Telling ddcutil [to directly talk to the I2C bus](https://git.xythobuz.de/thomas/AutoBrightness/commit/b4888f009f3685c036866fa689759ffdbe9227cb) helped a bit, but it still stutters slightly.

To alleviate this a bit I'm now using a [KWin script](https://develop.kde.org/docs/plasma/kwin/) to check for a full-screen app so I can pause brightness updates.

<pre class="sh_javascript">
var win = workspace.activeWindow;
var name = win.caption;
var pid = win.pid;
var state = (win.bufferGeometry == win.output.geometry);
print('{ "name": "' + name + '", "pid": ' + pid + ', "fullscreen": ' + state + ' }');
</pre>

As usual I'm also sending all these values to my local InfluxDB.

<!--%
lightgallery([
    [ "img/autobrightness_influx.png", "Input and Output data in Grafana" ],
])
%-->

## Proper Client

My initial idea for the client was to use the ambient light sensor to also "calibrate" the two displays to each other.
To do this, a white square could be shown on both screens.
Then the sensor can be placed in front of each display to measure their brightness "ramps".
This could then give the `calibration` dictionary shown above.

To determine the `c_in` values the room brightness has to be measured at day and night.

This should automate the process I've done manually to determine the calibration values.

But as you may have noticed, I'm more the prototype kind of guy and don't really do finished products on here.
So...

**To Do** 😅

## License
<a class="anchor" name="license"></a>

The [AutoBrightness project](https://git.xythobuz.de/thomas/AutoBrightness) is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    See <http://www.gnu.org/licenses/>.
