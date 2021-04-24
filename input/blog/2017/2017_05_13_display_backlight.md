title: Blog
post: DisplayBacklight
date: 2017-05-13
comments: true
flattr: true
github: https://github.com/xythobuz/DisplayBacklight
parent: projects
position: 100
---

DisplayBacklight is an Ambilight-clone made with an Arduino controlled by a macOS machine.

<div class="lightgallery">
    <a href="https://www.youtube.com/watch?v=Sy3Wgt9CKz4">
        <img src="http://img.youtube.com/vi/Sy3Wgt9CKz4/0.jpg" alt="DisplayBacklight - macOS Arduino Ambilight">
    </a>
    <a href="img/ambilight-1.jpg">
        <img src="img/ambilight-1_small.jpg" alt="Photo 1">
    </a>
    <a href="img/ambilight-2.jpg">
        <img src="img/ambilight-2_small.jpg" alt="Photo 2">
    </a>
</div>

### Hardware

The software currently only supports driving RGB-LEDs with the colors from the edge of a screen, so you have to place an RGB LED strip on the outer edges of your computer monitors. Multiple screens are supported using a single LED strip for all of them.

You need an LED strip with individually addressable LEDs like the popular [WS2812 RGB LED strips](https://www.sparkfun.com/products/12025). The data line is connected to pin 2 of the Arduino. The [Adafruit Neo-Pixel library](https://github.com/adafruit/Adafruit_NeoPixel) is used to control the LEDs.

### Protocol

The color data is transmitted using the serial port and the USB-UART converter built into most Arduinos. Communication happens at 115200bps, the LED count is hardcoded in both firmware and host software. First, a magic string, also hardcoded, is sent, followed by 3 bytes containing Red, Green and Blue, for each LED. When the last byte has been received the whole strip is refreshed at once.

### Software

The macOS host software is opening the connection to the serial port, grabbing a screenshot, processing the edges to calculate each LED color and finally sending it to the device.

<div class="lightgallery">
    <a href="img/ambilight-3.png">
        <img src="img/ambilight-3.png" alt="Screenshot">
    </a>
</div>

### License

DisplayBacklight itself is made by Thomas Buck <xythobuz@xythobuz.de> and released under a BSD 2-Clause License. See the accompanying COPYING file.

