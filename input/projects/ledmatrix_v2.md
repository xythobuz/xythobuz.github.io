title: RGB LED Matrix visualizer
description: For HUB75 modules, running on Raspberry Pi and Pico W
parent: projects
git: https://git.xythobuz.de/thomas/rgb-matrix-visualizer
github: https://github.com/xythobuz/rgb-matrix-visualizer
date: 2023-09-05
update: 2024-03-08
comments: true
---

I initially bought a 32x32 RGB LED matrix in 2018.
Back then the idea was to fit it onto a bag, as some kind of wearable device, for 35C3.
But it never really worked out.
So in preparation for CCCamp23 I noticed the LED panel again and decided to order some more of them.

<!--%
lightgallery([
    [ "img/toolbox10_2.jpg", "LED Matrix at Toolbox anniversary. © 2024 Falko." ],
])
%-->

These are the [32x32 4mm pitch RGB LED Matrix Panels from Pimoroni](https://shop.pimoroni.com/products/rgb-led-matrix-panel?variant=35962488650), with either the [Interstate 75 W](https://shop.pimoroni.com/products/interstate-75-w?variant=40453881299027) or the [Adafruit RGB Matrix Bonnet](https://shop.pimoroni.com/products/adafruit-rgb-matrix-bonnet-for-raspberry-pi?variant=2257849155594) to run them with a RP2040 or a Raspberry Pi, respectively.

<!--%
lightgallery([
    [ "img/led_matrix_visual_1.jpg", "Tetris (paused)" ],
    [ "img/cccamp23_matrix_1.jpg", "Someone tries to beat Breakout" ],
    [ "img/led_matrix_3d_1.png", "3D design for panel mounts" ],
])
%-->

Everything runs from a single Python [codebase](https://git.xythobuz.de/thomas/rgb-matrix-visualizer), either simulated in a GUI window on a development PC, on the Raspbian Python interpreter or directly on the Pico MicroPython environment.

<!--%
lightgallery([
    [ "img/led_matrix_gui_1.png", "Screenshot of weather widget" ],
    [ "img/led_matrix_portable_1.jpg", "Portable matrix showing a QR code" ],
    [ "img/led_matrix_portable_2.jpg", "Portable matrix showing battery state" ],
])
%-->

For portability I'm simply using a voltage regulator to connect a 4S LiPo battery.
I made one of them from recycled single-use vape batteries, but I also used some of my RC-model batteries.

<!--%
lightgallery([
    [ "img/led_matrix_portable_3.jpg", "Recycled vape batteries" ],
    [ "img/led_matrix_portable_4.jpg", "Back side of portable matrix" ],
    [ "img/led_matrix_portable_5.jpg", "Pico without voltage regulator" ],
])
%-->

On the software side I wrote some code to show static images, GIF animations, scroll text across the matrix, etc.
I also implemented Snake, Tetris and Breakout, as well as some other utilities, like OTA updating for the Pico, a Telegram bot integration, a weather widget and a service checking if a device is reachable on the network.

<!--%
lightgallery([
    [ "img/led_matrix_visual_2.jpg", "Tetris" ],
    [ "img/led_matrix_visual_3.jpg", "Game of Life" ],
    [ "img/led_matrix_visual_4.jpg", "Aphex Twin logo" ],
])
%-->

Right now the 64x64 panel is placed next to the TV in my livingroom, randomly cycling through some animations and games.

<!--%
lightgallery([
    [ "img/led_matrix_visual_5.jpg", "Animated globe" ],
    [ "img/led_matrix_visual_8.jpg", "Animated Sephiroth" ],
    [ "img/led_matrix_visual_9.jpg", "Animated Cloud" ],
])
%-->

I wasn't really able to get breakout into a playable state before CCCamp23.
But luckily I also got a patch set ([1](https://git.xythobuz.de/thomas/rgb-matrix-visualizer/commit/8e257111464a90a983bd2bc4f6092c12ebf08374), [2](https://git.xythobuz.de/thomas/rgb-matrix-visualizer/commit/8ff126684afb7dfa48a2d7060e390e8233045bb9), [3](https://git.xythobuz.de/thomas/rgb-matrix-visualizer/commit/43d0b92700f2c2a8adf915bb5a020476409e8e08), [4](https://git.xythobuz.de/thomas/rgb-matrix-visualizer/commit/2399961348fefa849d1892cdf5b5001265a28ffd)) from Jannis that fixed the collision behaviour of the ball in breakout!
We met on the camp and had a very nice time together.
And soon afterwards the patches appeared in my inbox and actually made the game playable!
This was really awesome 😊💪
Thanks again!

<!--%
lightgallery([
    [ "img/cccamp23_matrix_2.jpg", "Another player already scored 80 points" ],
    [ "img/led_matrix_build_1.jpg", "64x64 panel in my livingroom" ],
    [ "img/led_matrix_build_5.jpg", "Backside of 64x64 panel" ],
])
%-->

Here are my notes for installing everything on a Raspbian OS.

<pre class="sh_sh">
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip git vim htop
git clone https://github.com/adafruit/Raspberry-Pi-Installer-Scripts
cd Raspberry-Pi-Installer-Scripts
sudo ./rgb-matrix.sh
# Answer y, Bonnet, Quality (and solder the mentioned link on the board)
cd ..

git clone https://git.xythobuz.de/thomas/rgb-matrix-visualizer
sudo pip3 install Pillow bdfparser "qrcode[pil]" evdev

cd Raspberry-Pi-Installer-Scripts/rpi-rgb-led-matrix/bindings/python
pip3 wheel --no-deps -w dist .
sudo pip3 install dist/rgbmatrix-0.0.1-cp39-cp39-linux_armv7l.whl

sudo apt-get install libopenjp2-7

# append isolcpus=3 to /boot/cmdline.txt
cat &lt;&lt;EOF | sudo tee /etc/modprobe.d/blacklist-rgb-matrix.conf
blacklist snd_bcm2835
EOF

sudo update-initramfs -u
sudo reboot

# test python bindings work
cd rgb-matrix-visualizer
sudo ./pi.py

sudo sh -c 'echo enable_uart=1 &gt;&gt; /boot/config.txt'
</pre>

Although I'm currently still having some problems getting the `wetterdienst` dependency running on the Raspberry Pi.

<!--%
lightgallery([
    [ "img/led_matrix_build_2.jpg", "Two small panels and materials for the large matrix" ],
    [ "img/led_matrix_build_3.jpg", "Game of Life on four matrices" ],
    [ "img/led_matrix_3d_3.png", "96x32 frame design" ],
])
%-->

I also want to give a shout-out to [Pimoroni](https://shop.pimoroni.com/).
I managed to rip-off the power connector on one of the panels.
They sent a replacement without any additional cost, but I took the chance and ordered some more spare panels.

<!--%
lightgallery([
    [ "img/led_matrix_build_4.jpg", "Power connector ripped-off from PCB" ],
])
%-->

The modules bought this year have pretty consistent color reproduction.
But compared to the one module I bought five years earlier, there is a very noticable difference.
On these pictures both modules show the same RGB values.

<!--%
lightgallery([
    [ "img/led_matrix_colors_1.jpg", "Color reproduction issue (1)" ],
    [ "img/led_matrix_colors_2.jpg", "Color reproduction issue (2)" ],
])
%-->

I added some simple compensation to mostly adjust for this issue.

<pre class="sh_python">
# For some reason the red and green LEDs on older Pimoroni panels
# are far brighter than on newer panels.
# Adjust this by multiplying rg channels with 0.75 and b channel
# with 0.85, depending on hard-corded coordinate ranges.
class MapperColorAdjust(MapperNull):
    def set_pixel(self, x, y, color):
        # second panel from the left, with 32 <= x,
        # is "old" type with brighter LEDs.
        # rest of panels to the left are less bright.
        # so adjust brightness of other panel channels down.
        if x >= self.gui.panelW:
            color = (int(color[0] * 0.75), int(color[1] * 0.75), color[2] * 0.85)

        self.gui.set_pixel(x, y, color)
</pre>

I also planned to build a large LED matrix based on WS2812 LED strips.
They can be [driven easily with a Raspberry Pi](https://iosoft.blog/2020/09/29/raspberry-pi-multi-channel-ws2812/).

<!--%
lightgallery([
    [ "img/led_matrix_large_5.jpg", "Level shifter for WS2812 strips" ],
    [ "img/led_matrix_large_3.jpg", "Large matrix frame and strips" ],
])
%-->

I was even able to get a basic frame finished before CCCamp23.
But that's where time ran out.

<!--%
lightgallery([
    [ "img/led_matrix_large_1.jpg", "Frame for large matrix, back side" ],
    [ "img/led_matrix_large_2.jpg", "Frame for large matrix, front side" ],
    [ "img/led_matrix_3d_2.png", "Corner piece for large 32x32 matrix" ],
])
%-->

I haven't yet given up that plan completely, but I have to think of a solution for diffusing the light first.
The LEDs are too small and spaced too far apart to look good in this configuration.

## More Pictures
<a class="anchor" name="more_pictures"></a>

<div class="collapse">Some more photographs I didn't use above.</div>
<div class="collapsecontent">
<!--%
lightgallery([
    [ "img/led_matrix_visual_7.jpg", "Animated Nintendo 64 logo" ],
    [ "img/led_matrix_visual_6.jpg", "Empty matrix" ],
    [ "img/led_matrix_large_4.jpg", "LED strips for large matrix" ],
    [ "img/led_matrix_colors_3.jpg", "Color reproduction issue (3)" ],
])
%-->
</div>
