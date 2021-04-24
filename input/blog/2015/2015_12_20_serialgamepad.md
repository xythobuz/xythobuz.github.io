title: Blog
post: Flysky Mac OS X joystick driver
date: 2015-12-20
comments: true
flattr: true
github: https://github.com/xythobuz/SerialGamepad
parent: projects
position: 50
---

### Hardware

In the last couple of months I’ve finally built a FPV capable Quadcopter. Fortunately, I could use the Transmitter I already had for a number of years. It’s a Modelcraft MP-26-DT, a rebranded Flysky FS-CT6x Transmitter. There are many different versions of this Transmitter on the market, all basically the same, like the HobbyKing HK-T6A.

<div class="lightgallery">
    <a href="img/flysky1.png">
        <img src="img/flysky1.png" alt="FlySky FS-CT6A">
    </a>
    <a href="img/flysky2.jpg">
        <img src="img/flysky2_small.jpg" alt="HK-T6A">
    </a>
    <a href="img/flysky3.jpg">
        <img src="img/flysky3_small.jpg" alt="MP-26-DT">
    </a>
    <a href="img/flysky4.jpg">
        <img src="img/flysky4_small.jpg" alt="MP-26-DT back">
    </a>
    <a href="img/flysky5.jpg">
        <img src="img/flysky5_small.jpg" alt="MP-26-DT mod">
    </a>
    <a href="img/flysky6.jpg">
        <img src="img/flysky6_small.jpg" alt="MP-26-DT mod near">
    </a>
</div>

As you can see, in the back is a small transmitter PCB (in green) marked with FlySky. That’s how I found out it’s just a rebranding. This module only has 4 pins, +5V, GND, PPM Signal and a connection for the bind button. This means you can replace it with most other modules, as I did with the (discontinued) [Fr-Sky DHT](http://www.frsky-rc.com/product/pro.php?pro_id=95).

This line of Transmitters also has a PC-Link port in the back (a 4-pin mini-DIN connector), that’s simply a RS232 port (most probably in TTL logic). The packaging includes a USB-Serial adaptor with this connector and a [Silicon Labs CP2102](https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx) or [Prolific PL2303](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41) chipset. You may need to install the driver for one of these. To find out which one, open the System Information App, find the USB device corresponding to the dongle and check its name.

A (pretty crappy) Visual Basic Windows Software is included to configure the transmitter, called T6config or TXsetup. There are [some alternatives](http://www.mycoolheli.com/t6Alternate.html), like [TurborixConfig for Mac OS X](http://www.zenoshrdlu.com/turborix/).

### Software

With FPV flying becoming more prevalent, many users started connecting their transmitters to their PCs to use them as Joystick in FPV Simulator software like [FPV Freerider](http://fpv-freerider.itch.io/fpv-freerider), [Liftoff](http://www.liftoff-game.com) or [HOTPROPS](http://hotprops-fpv-race.com). The most important thing for this to work is a driver so the Operating System can use the Transmitter as a Joystick. Of course, there’s no driver for my Transmitter or my Operating System...

Fortunately, the configuration software always displays the current stick positions, so the transmitter seems to be sending this continuously. I tried reverse-engineering the data stream myself, but quickly got stuck seeing strange repeating patterns every 12 bytes. Of course, this was later explained as I was using a baudrate of 9600 and the real one is 115200, exactly 12 times my rate. But I got lucky and found [this forum post explaining the data format](http://www.rcgroups.com/forums/showpost.php?p=11384029&postcount=79).

Experimentation revealed that the format slightly differs from the forum post, in that the “7th channel” is, in my case, always the throttle, even when CH3 is set to zero using a hardware switch (which makes more sense, to be honest).

So I wrote a little command line application displaying the current stick positions, called [protocol](https://github.com/xythobuz/SerialGamepad/blob/master/src/protocol.c).

The only thing left is creating a driver that emulates a Human Interface Device. This is where [foohid](https://github.com/unbit/foohid) comes to shine. This fantastic little piece of software is a Kernel Extension that allows Userspace applications to create a virtual HID. Exactly what I was looking for.

For this to work, I had to create a USB HID descriptor, [as described here](http://eleccelerator.com/tutorial-about-usb-hid-report-descriptors/), using [this Windows software](http://www.usb.org/developers/hidpage#HID%20Descriptor%20Tool):

<pre class="sh_c">
static char report_descriptor[36] = {
    0x05, 0x01,                    // USAGE_PAGE (Generic Desktop)
    0x09, 0x05,                    // USAGE (Game Pad)
    0xa1, 0x01,                    // COLLECTION (Application)
    0xa1, 0x00,                    //   COLLECTION (Physical)
    0x05, 0x01,                    //     USAGE_PAGE (Generic Desktop)
    0x09, 0x30,                    //     USAGE (X)
    0x09, 0x31,                    //     USAGE (Y)
    0x09, 0x32,                    //     USAGE (Z)
    0x09, 0x33,                    //     USAGE (Rx)
    0x09, 0x34,                    //     USAGE (Ry)
    0x09, 0x35,                    //     USAGE (Rz)
    0x16, 0x01, 0xfe,              //     LOGICAL_MINIMUM (-511)
    0x26, 0xff, 0x01,              //     LOGICAL_MAXIMUM (511)
    0x75, 0x10,                    //     REPORT_SIZE (16)
    0x95, 0x06,                    //     REPORT_COUNT (6)
    0x81, 0x02,                    //     INPUT (Data,Var,Abs)
    0xc0,                          //     END_COLLECTION
    0xc0                           // END_COLLECTION
};
</pre>

The result can be seen in the creatively-named command line app [foohid](https://github.com/xythobuz/SerialGamepad/blob/master/src/foohid.c). It work’s perfectly and is detected as Joystick in all Games I’ve tried. Flying in FPV Freerider or Liftoff is very fun!

The only thing left was packaging this into a nicer GUI application for ease-of-use. So, I present, [SerialGamepad](https://github.com/xythobuz/SerialGamepad/blob/master/src/foohid.c). Basically the same functionality as the command line apps, packaged into [an Installer package](https://github.com/xythobuz/SerialGamepad/releases) including the foohid dependency, so Users only need to install a single package.

<div class="lightgallery">
    <a href="img/serialgamepad1.png">
        <img src="img/serialgamepad1_small.png" alt="SerialGamepad">
    </a>
    <a href="img/serialgamepad2.png">
        <img src="img/serialgamepad2_small.png" alt="protocol CLI">
    </a>
</div>

Creating the installer package was the last thing I never did before, but fortunately there’s a very good [StackOverflow answer](http://stackoverflow.com/a/11487658) explaining the process. It boils down to [some lines in the Makefile](https://github.com/xythobuz/SerialGamepad/blob/master/Makefile#L46-L66) and a [Distribution.xml file](https://github.com/xythobuz/SerialGamepad/blob/master/Resources/Distribution.xml) detailing the installation wizard contents.

And all my code is under the Beer-Ware license. I hope to get something in return some day :P

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    <xythobuz@xythobuz.de> wrote this file.  As long as you retain this notice
    you can do whatever you want with this stuff. If we meet some day, and you
    think this stuff is worth it, you can buy me a beer in return.   Thomas Buck
    ----------------------------------------------------------------------------

