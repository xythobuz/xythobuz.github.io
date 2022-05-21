title: ESP-Env
description: ESP32 / ESP8266 & BME280 / SHT2x sensor with InfluxDB support
parent: smarthome
git: https://git.xythobuz.de/thomas/esp-env
position: 100
date: 2020-01-06
update: 2022-05-21
---

As a first step into smart home automation, I wanted to place temperature and humidity sensors in most rooms of my flat.
To achieve this, I made some simple ESP8266 boards with an I2C sensor, either SHT21 or BME280, as well as a small 3.3V regulator and a USB connector.
The data is written into an InfluxDB instance on my NAS.

Over time I also added support for ESP32 as well as Arduino Uno Wifi Developer Edition boards, MQTT interfacing, relais control, CCS811 and soil moisture sensor support.

Initially I had a separate project, [esp-relais](https://git.xythobuz.de/thomas/esp-relais), for controlling [this ESP8266 Relais board from Amazon](https://amzn.to/3FQdOXB).
This functionality has since been integrated into esp-env!

<!--%
lightgallery([
    [ "img/espenv_10.jpg", "BME280 bedroom, front" ],
    [ "img/espenv_17.jpg", "SHT21 kitchen, front" ],
])
%-->

The web interface implemented to query the sensor data is very simple.
I am using the following commands to fetch it.

    curl --silent -m 10 esp-livingroom | grep -E 'Location|Temperature|Humidity' | sed 's/Temperature//g' | sed 's/Humidity//g' | sed 's/Location//g' | sed '2s/$/ \xc2\xb0C/' | sed '3s/$/ %/' | sed 's/: //g' | sed '$!N;s/\n/\t/' | sed '$!N;s/\n/\t/'

The result is shown on my desktop using [conky](http://conky.sourceforge.net/docs.html).

<!--%
lightgallery([
    [ "img/espenv_screen.png", "Screenshot of web interface" ],
    [ "img/espenv_desktop.png", "Screenshot of desktop data" ]
])
%-->

Here you can see some samples of the data I have logged since starting this project.
As you can see, after a while the sensor in the kitchen started giving wrong data.
This is the usual behaviour these sensors show after a couple of months to years.
I replaced it, but shortly afterwards removed the kitchen sensor completely.
You can also see some short gaps in the data, this is caused by the ESPs losing their WiFi connection after a while.
I just had to reset them and they started working again.

<!--%
lightgallery([
    [ "img/espenv_1.png", "Humidity data from ca. 7 months" ],
    [ "img/espenv_2.png", "Temperature data from ca. 7 months" ]
])
%-->

Here are some more photos of the PCBs I made.
All of the boards, except one, work fine.
The non-working one is just not connecting to WiFi, regardless of which specific ESP8266 I plug in there.
I have no explanation for this, unfortunately.

<!--%
lightgallery([
    [ "img/espenv_3.jpg", "BME280 livingroom, front" ],
    [ "img/espenv_4.jpg", "BME280 livingroom, front bare PCB" ],
    [ "img/espenv_5.jpg", "BME280 livingroom, back" ],
    [ "img/espenv_6.jpg", "SHT21 bathroom, case" ],
    [ "img/espenv_7.jpg", "SHT21 bathroom, front" ],
    [ "img/espenv_8.jpg", "SHT21 bathroom, back" ],
    [ "img/espenv_9.jpg", "BME280 bedroom, case" ],
    [ "img/espenv_11.jpg", "BME280 bedroom, back" ],
    [ "img/espenv_12.jpg", "BME280 storage, front" ],
    [ "img/espenv_13.jpg", "BME280 storage, back" ],
    [ "img/espenv_14.jpg", "non-working, front" ],
    [ "img/espenv_15.jpg", "non-working, back" ],
    [ "img/espenv_16.jpg", "SHT21 kitchen, case" ],
    [ "img/espenv_18.jpg", "SHT21 kitchen, back" ]
])
%-->

The source code can be found [on my Gitea server](https://git.xythobuz.de/thomas/esp-env).

## License

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    <xythobuz@xythobuz.de> wrote this file.  As long as you retain this notice
    you can do whatever you want with this stuff. If we meet some day, and you
    think this stuff is worth it, you can buy me a beer in return.   Thomas Buck
    ----------------------------------------------------------------------------
