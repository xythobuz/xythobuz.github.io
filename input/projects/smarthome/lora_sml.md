title: Smart Meter Bridge
description: Reading SML power meter data transmitted via LoRa
parent: smarthome
position: 150
git: https://git.xythobuz.de/thomas/esp-env
github: https://github.com/xythobuz/esp-env
date: 2024-07-06
comments: true
---

<!--% backToParent() %-->

A while ago my power net company installed new smart power meters, specifically the [Iskra MT681](https://wiki.volkszaehler.org/hardware/channels/meters/power/edl-ehz/iskraemeco_mt681).
It has a standardized infrared interface to get some data from it.
There are different [designs](https://wiki.volkszaehler.org/hardware/controllers/ir-schreib-lesekopf-ttl-ausgang) available to attach a microcontroller, both open-source and commercial.
I've gone the lazy route and bought one [from eBay](https://www.ebay.de/itm/353940190755).

<!--%
lightgallery([
    [ "img/lora_sml_1.jpg", "IR TTL Reader with magnetic base" ],
])
%-->

Unfortunately the meter is mounted in the basemet of my apartment building, too far for any WiFi signals.
So I decided to try out [LoRa](https://en.wikipedia.org/wiki/LoRa) to transmit the data, using two [Heltec LoRa32](https://heltec.org/project/wifi-lora-32-v3/) dev boards.

<!--%
lightgallery([
    [ "img/lora_sml_2.jpg", "LoRa SML transmitter, outside" ],
    [ "img/lora_sml_3.jpg", "LoRa SML transmitter, inside" ],
])
%-->

The interface to the meter is an infrared UART with 9600 8N1.
Over this port it sends messages in a format called [SML](https://de.wikipedia.org/wiki/Smart_Message_Language).
To decode these I'm using [sml_parser](https://github.com/olliiiver/sml_parser).

<!--%
lightgallery([
    [ "img/lora_sml_4.jpg", "LoRa SML receiver" ],
])
%-->

To get useful data from the meter you have to unlock it with a PIN from the net provider.
Without this PIN you only get the current energy count in `kWh`, the same number you can see on the display.
After unlocking all data, you get the energy count in `1/10th Wh`, so much finer resolution.
And you also get the current power in `W`.

<!--%
lightgallery([
    [ "img/lora_sml_5.jpg", "Testing the transmitter" ],
    [ "img/lora_sml_6.jpg", "Readout of SML messages" ],
])
%-->

For the LoRa PHY I'm using [RadioLib](https://github.com/jgromes/RadioLib/), which already comes integrated into the [unofficial Heltec LoRa 32 library](https://github.com/ropg/heltec_esp32_lora_v3/).

I'm doing lots of deep sleep on the transmitter side, to safe as much battery capacity as possible.
And I had to use the watchdog in the ESP32 and also do an auto-reset when no messages have been received after a while.
So somewhere the code hangs, sometimes.
But with these hacks in place it seems to work well.

The code is integrated into my [ESP-Env project](espenv.html) and [repo](https://git.xythobuz.de/thomas/esp-env).

<!--%
lightgallery([
    [ "img/lora_sml_power.png", "Example of my power usage" ],
    [ "img/lora_sml_battery.png", "Battery usage of the LoRa transmitter" ],
])
%-->

Here you can see a normal weekend for me, going to bed at 4:30 in the morning, and waking up at around 13:00.
The spike with 1.3kW is heating water for coffee.
The other power readings come from tasmota sockets or my NAS UPS.

Also the battery usage of the LoRa transmitter is very low.
I will update when I have to recharge them for the first time.
