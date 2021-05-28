title: Blog
post: Arduino FrSky Telemetry
description: Custom telemetry display for cheap RC remotes
date: 2016-11-05
comments: true
flattr: true
github: https://github.com/xythobuz/FrSky-Telemetry-Arduino
parent: projects
show_in_quadcopters: true
position: 90
---

I've now built multiple model aircraft, all using the FrSky remote control and telemetry system with the FrSky DHT module included in my modified cheap RC transmitter. This system allows transmitting digital data streams and analog voltages from the aircraft back to the transmitter, which can be used to implement a battery voltage gauge and low-voltage alarm. All that's required is a simple voltage divider using two resistors, to bring the battery voltage down into a range the receiver can measure (3.3V).

To output the telemetry data, the FrSky transmitter module has an RS232 serial port. To connect it to an Arduino or TTL-level USB-UART adapter, you need to use an adaptor or [modify your transmitter module, removing the level shifter](http://majek.mamy.to/en/frsky-dht-ttl-mod/).

To display the received data with the Arduino, I'm using [this cheap I2C OLED display from HobbyKing](https://www.hobbyking.com/en_us/multiwii-oled-display-module-i2c-128x64-dot-mwc.html).

<!--%
lightgallery([
    [ "img/arduino_frsky_telemetry_1.png", "Schematic" ]
])
%-->

The FrSky telemetry protocol transmits two ADC values and a serial data stream. Currently, the received serial user data is simply displayed but not used further. One of the two ADC values can be converted to a voltage using a simple algorithm: Just apply two different (known) voltages to the ADC input and note the ADC output value received (it's displayed on the OLED). Then enter these two voltage-value datapairs in to the `options.h` file and all intermediate values will be interpolated. For example:

    // Analog Sample Min Value
    const static int16_t batteryValuesMin[MODEL_COUNT] = {
        231,
        169
    };
    
    // Battery Voltage when Min Value has been reached
    // Voltage is stored with factor 100, so 388 -> 3.88V
    const static int16_t batteryVoltagesMin[MODEL_COUNT] = {
        388,
        900
    };

This means, for Model 1 a value of 231 equals 3.88V, and for Model 2 a value of 169 means 9.00V. As you can see, multiple models with different voltage dividers and battery ranges can be used this way, and each one can have individual alarms set.

<!--%
lightgallery([
    [ "img/arduino_frsky_telemetry_2.jpg", "Photo 1" ],
    [ "img/arduino_frsky_telemetry_3.jpg", "Photo 2" ],
    [ "img/arduino_frsky_telemetry_4.jpg", "Photo 3" ]
])
%-->

I've used an Arduino Pro Mini and could easily fit it, the OLED, beeper, switched and LED into my existing RC transmitter. The sketch should run without changes on any Arduino based on the Atmega328.

### License

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    <xythobuz@xythobuz.de> wrote this file.  As long as you retain this notice
    you can do whatever you want with this stuff. If we meet some day, and you
    think this stuff is worth it, you can buy me a beer in return.   Thomas Buck
    ----------------------------------------------------------------------------

