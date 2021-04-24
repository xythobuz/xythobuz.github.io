title: Blog
post: Arduino USB Host CPPM
date: 2016-07-24
comments: true
flattr: true
github: https://github.com/xythobuz/Saitek-X52-PPM
parent: projects
position: 80
---

[This project](https://github.com/xythobuz/Saitek-X52-PPM) allows using an AVR-based Arduino with a USB-Host-Shield to be connected to a [Saitek X52](http://www.saitek.com/uk/prod/x52.html) ([Pro](http://www.saitek.com/uk/prod/x52pro.html)) flight control joystick, generating a CPPM-Signal that can be fed to most common RC transmitters.

<div class="lightgallery">
    <a href="https://www.youtube.com/watch?v=De_Ld6MerNo">
        <img src="http://img.youtube.com/vi/De_Ld6MerNo/0.jpg" alt="Multicopter flight with Saitek X52">
    </a>
    <a href="img/saitek1.jpg">
        <img src="img/saitek1_small.jpg" alt="Whole Setup">
    </a>
    <a href="img/saitek8.jpg">
        <img src="img/saitek8_small.jpg" alt="Modified RC Transmitter">
    </a>
</div>

### Features

All Parameters, like the channel count, CPPM specifications, endpoints, trim and invert, can be changed using the Multi-Function-Display on the Saitek Joystick and stored to the Arduino EEPROM.

A modified host telemetry port (D-Port) of an FrSky TX module can be connected to the hardware serial port so the link quality and voltage will be displayed on the Multi-Function-Display. Obviously, you have to remove the RS232 level-converter from the TX module or use an adaptor to bring the UART to 5V level.

Currently the code only supports the Saitek X52 series, but you could easily adapt the code to work with other joysticks or gamepads.

<div class="lightgallery">
    <a href="img/saitek2.jpg">
        <img src="img/saitek2_small.jpg" alt="Parameter Menu 1">
    </a>
    <a href="img/saitek3.jpg">
        <img src="img/saitek3_small.jpg" alt="Parameter Menu 2">
    </a>
    <a href="img/saitek4.jpg">
        <img src="img/saitek4_small.jpg" alt="Parameter Menu 3">
    </a>
    <a href="img/saitek5.jpg">
        <img src="img/saitek5_small.jpg" alt="Parameter Menu 4">
    </a>
    <a href="img/saitek6.jpg">
        <img src="img/saitek6_small.jpg" alt="Parameter Menu 5">
    </a>
    <a href="img/saitek7.jpg">
        <img src="img/saitek7_small.jpg" alt="Parameter Menu 6">
    </a>
</div>

### License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.

