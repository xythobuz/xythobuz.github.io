title: Blog
post: CaseLights
date: 2015-12-30
comments: true
flattr: true
twitter: xythobuz
github: https://github.com/xythobuz/CaseLights
parent: projects
position: 60
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

### Background

I’ve recently (accidentally) bought a dead-simple [12V RGB LED strip](http://www.hobbyking.com/hobbyking/store/__28515__LED_Red_Green_Blue_RGB_Strip_50cm_w_Flying_Lead.html), aiming to mount it on my Quadcopter, thinking it would be made of individually addressable LEDs. Of course, I didn’t read the description and was wrong. So, what to do?

As you [may remember](http://xythobuz.de/2015_01_31_hackintosh.html), I’ve built a new computer in January with a very spacious case. It already had [two UV lights](http://www.aquatuning.de/modding/kathoden/13168/revoltec-kaltlicht-kathode-30cm-twin-set-uv-rev.-2) that were controlled manually using a switch in a PCI slot. Both the RGB LED strip and my computer seem to be a match made in heaven :P

Incidentally, there’s still a unused RS232 port directly on my Motherboard that I never wired to the outside. That could be used to talk to an Arduino controlling the RGB LEDs and the UV lights. And there are plenty of free 12V rails of course.

### Hardware

So I bought a five-pack of cheap [Arduino Pro Mini](https://www.arduino.cc/en/Main/ArduinoBoardProMini) clones from china. I still had some [IRF530 N-Channel MOSFETS](https://arduinodiy.wordpress.com/2012/05/02/using-mosfets-with-ttl-levels/) left over from the [LED-Cube](http://xythobuz.de/ledcube.html) that can be used for this. And I needed to build a small [RS232-TTL converter](http://picprojects.org.uk/projects/simpleSIO/ssio.htm) (using 2N3904 and 2N3906 as Transistors).

<div class="yoxview">
    <a href="img/CaseLights-schem.png" class="thumbnail">
        <img src="img/CaseLights-schem_small.png" alt="Schematic" title="Basic Schematic">
    </a>
    <a href="img/CL_Test1.jpg" class="thumbnail">
        <img src="img/CL_Test1_small.jpg" alt="Photo" title="First Test">
    </a>
    <a href="img/CL_Test2.jpg" class="thumbnail">
        <img src="img/CL_Test2_small.jpg" alt="Photo" title="First Test near">
    </a>
    <a href="img/CL_Test3.jpg" class="thumbnail">
        <img src="img/CL_Test3_small.jpg" alt="Photo" title="First Test working">
    </a>
    <a href="img/CL_Final1.jpg" class="thumbnail">
        <img src="img/CL_Final1_small.jpg" alt="Photo" title="Final Board">
    </a>
    <a href="img/CL_Final2.jpg" class="thumbnail">
        <img src="img/CL_Final2_small.jpg" alt="Photo" title="Board in Case">
    </a>
    <a href="img/CL_Final3.jpg" class="thumbnail">
        <img src="img/CL_Final3_small.jpg" alt="Photo" title="Finished Case">
    </a>
    <a href="img/CL_gif.gif" class="thumbnail">
        <img src="img/CL_gif_small.gif" alt="GIF" title="Animation Test">
    </a>
</div>

### Software

Here’s the protocol used to communicate over RS232. It is line-based ASCII and only supports two commands:

    RGB r g b
    UV x

Where r, g and b are ASCII decimal values from 0 to 255 and x can be ASCII 0 or 1.

Currently the user can only turn the UV lights on or off using the CaseLights App. In the future, I may implement some automatism based on the time of day or something like this.

The RGB Lights can be set to some static colors, with a modifiable brightness. Alternatively, a simple color-fade in RGB or HSV color space can be selected.

Using the included [JSystemInfoKit](https://github.com/jBot-42/JSystemInfoKit), different things like CPU/GPU/RAM/VRAM usage or hardware temperatures can be visualized with colors from red, over yellow, to green.

And finally, a display output device connected to the Mac can be selected. The CaseLights App will then create a Screenshot 10-times per second and display the average color.

<div class="yoxview">
    <a href="img/CaseLights.png" class="thumbnail">
        <img src="img/CaseLights_small.png" alt="Screenshot" title="CaseLights App">
    </a>
</div>

You can find all Arduino and Mac code in the [CaseLights GitHub repository](https://github.com/xythobuz/CaseLights).

