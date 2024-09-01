title: Oscilloscope Music Player
description: Properly playing sound files for visualization on an oscilloscope
parent: projects
git: https://git.xythobuz.de/thomas/osci-music-player
date: 2024-02-11
update: 2024-03-08
comments: true
---

Soon our local hackerspace [Toolbox Bodensee](https://toolbox-bodensee.de/) has its [10-year anniversary](https://toolbox-bodensee.de/blog/ankuendigung-tag-der-offenen-tuer-2024/), and it will also be present at the [IBO fair 2024 in Friedrichshafen](https://www.ibo-messe.de/).
Some five or six years ago I already prepared a small setup at one of the Toolbox open-door-days with an oscilloscope and a laptop playing [Jerobeam Fendersons Oscilloscope Music](https://oscilloscopemusic.com/).
But it never looked quite right.
So I decided to tackle the topic again this year.

<!--%
lightgallery([
    [ "img/toolbox10_1.jpg", "© 2024 Falko." ],
    [ "img/toolbox10_3.jpg", "© 2024 Falko." ],
    [ "img/osci_music_7.jpg", "'Reconstruct' with the Osci Music Player" ],
    [ "img/osci_music_2.jpg", "Front of Osci Music Player" ],
    [ "img/osci_music_8.mp4", "video/mp4", "", "", "'Function' with the Osci Music Player" ],
])
%-->

### Table Of Contents

Want to build your own player?
Skip to the [interesting part](osci_music_player.html#hardware) then!

* [Introduction](osci_music_player.html#introduction)
* [Artists](osci_music_player.html#artists)
* [Playback](osci_music_player.html#playback)
* [Oscilloscope Settings](osci_music_player.html#oscisettings)
* [Hardware](osci_music_player.html#hardware)
* [Software](osci_music_player.html#software)

## Introduction
<a class="anchor" name="introduction"></a>

An oscilloscope usually displays one or more waveforms of an electrical signal.
To achieve this a single dot is moved across the screen, with the voltage or amplitude of the signal controlling the vertical deflection (Y axis), and time controlling the horizontal deflection (X axis), meaning the dot automatically moves from left to right with a pre-configured speed.
But most oscilloscopes can also be configured in something called `XY mode`, where the horizontal deflection is no longer controlled by time, but instead by another voltage.
This turnes the oscilloscope into a vector display, where a single dot can be moved across the screen.
Note that the brightness can not be controlled, it is fixed.
Some oscilloscopes have a third input that can be used for that, but this is not needed here.

A common way to achieve digital to analog conversion (DAC) of a signal, with hardware usually available in every household, is using the soundcard of a PC.
The stereo line output channels are basically connected directly to a DAC chip, with only some filtering hardware in between.

Now combining these concepts, one can connect the two audio output channels of a PC or similar device to the two inputs of an oscilloscope in XY mode.
This enables a kind of visualization of music, and was also used in the past in something called "audio vectorscope" to check the balance of the channels.
If you have a mono signal, with both channels having the exact same contents, the scope will display a 45-degree angled line.
If only one channel has contents, and the other is silent, you will see either a horizontal or a vertical line, depending on which channel is active.
When one channel outputs a sine, and the other a cosine, with the same frequency and phase, you will see a circle.

Of course with normal music this doesn't look that interesting.
But what if you were to specifically compose music to look good on such a device?

That's what **Oscilloscope Music** is.

<!--%
lightgallery([
    [ "img/osci_music_9.mp4", "video/mp4", "", "", "'Reconstruct' with the Osci Music Player" ],
])
%-->

## Artists
<a class="anchor" name="artists"></a>

To generate the proper sounds you usually need some kind of software or self-written code.
Many people have already experimented with this, with small scripts running on a PC, or directly on a microcontroller.

In 2016 [Jerobeam Fenderson released an album](https://oscilloscopemusic.com/watch/oscilloscope_music) based on this concept.
He also collaborated with [Hansi Raber](https://github.com/kritzikratzi/) and they released [some software to play and generate this music](https://oscilloscopemusic.com/software/).
You can also find high-quality recordings on [his YouTube channel](https://www.youtube.com/@jerobeamfenderson1).

<!--%
lightgallery([
    [ "img/osci_music_cats_1.mp4", "video/mp4", "", "", "Cats listening to Jerobeam Fenderson" ],
    [ "https://www.youtube.com/watch?v=5WBWIKnr0Os", "Reconstruct - Jerobeam Fenderson" ],
    [ "https://www.youtube.com/watch?v=ywdRQ3zU6Uc", "Function - Jerobeam Fenderson" ],
])
%-->

I also found [Chris Allen on YouTube](https://www.youtube.com/channel/UCSb9_amN9Oh2WJhDTwnG3NA), another artist that offers a [download of the original files](https://bit.ly/OscMusic).

<!--%
lightgallery([
    [ "img/osci_music_cats_2.mp4", "video/mp4", "", "", "Cats listening to Chris Allen" ],
    [ "https://www.youtube.com/watch?v=FTHoDWog8qQ", "Moon Patrol De-Rastered - C. Allen" ],
    [ "https://www.youtube.com/watch?v=_6a_nz4uRd0", "72 Pantera - C. Allen" ],
])
%-->

## Playback
<a class="anchor" name="playback"></a>

So there are some technical challenges involved in playing these properly on an oscilloscope.

First, it is not enough to play these from YouTube or small MP3 files, as the compression algorithms remove too much of the visual contents of the music.
So original WAV file downloads are required.

Second, most audio outputs are `AC coupled` instead of `DC coupled`.
What does that mean?
Audio is normally an AC signal without any DC bias.
The spekaer membrane is more or less constantly moving around it's resting position.
If there were a DC offset, this would mean the membrane has a constant offset to one side, but would then vibrate there as usual.
So the sound waves generated are the same.
That's why normally theres a capacitor in line with the audio signal, blocking the DC contents.
But when you consider our oscilloscope, if you want to draw a straight line with an offset from the center of the screen, this looks like a DC bias on the signal, which would be filtered out by the capacitor, causing the line to appear in the middle of the screen instead.
So the impact of this depends on the image shown. If it is symmetrical around the center of the screen, not much will be distorted, but in other cases the image can be completely unrecognizable.

Third, the audio files have a sample rate of 192kHz.
It's usually assumed that average humans don't hear sounds above 20kHz, so according to Shannon, a sample rate of 40kHz is enough to capture all sounds interesting for humans.
But to draw many interesting shapes in a short time, higher frequencies are needed.
So you need a fast 192kHz DAC and the proper settings in your OS or player software to actually output this without downsampling happening somewhere in the chain.

So how can you achieve these in practice?
Interestingly, most Apple devices have a DC coupled output.
So when using these, you already get pretty close to the intended output.

We also tried a "proper" [Behringer UMC404HD](https://www.behringer.com/product.html?modelCode=P0BK1) USB audio interface from the [Toolbox Sound Studio](https://toolbox-bodensee.de/projekte/tonstudio/), but the output was the worst of all devices tried.
Even using random cheap AC coupled phone or laptop DACs looked way better.

But the best solution came in the form of the [Hifiberry DACs](https://www.hifiberry.com/dacs).
These are DC coupled, support 192kHz and are cheap and easy to get.

Now the image finally looks like in the YouTube videos.
The only problem is, this is supposed to be used and operated at Toolbox events, so it needs to be easy to use and kind of sturdy.

## Oscilloscope Settings
<a class="anchor" name="oscisettings"></a>

To get the proper picture out of your oscilloscope you need to set it up correctly.
Every oscilloscope has its own kind of front panel buttons, but in general they all have more or less the same kind of settings.

You need to set the voltage range of both inputs you're using, usually `CH1` and `CH2`, to the same value, something like `0.5V` or `0.2V`.
This changes the size of the image on the screen, just like changing the volume on the Raspberry Pi does, too.
My script has an option on top for the volume percentage.
You need to adjust these values so the image properly fills your screen, without drawing outside of its borders.
The output of the Pi should be put as high as possible, to reduce the influence of electrical noise.
Then set the proper range of the oscilloscope, which usually has pretty big steps, so do the final fine-adjustment with the percentage in the script.

Both input channels should be set to `DC coupling`.

And you need to put the scope in `XY mode`.

Put the intensity as high as needed, but as low as possible, to maximize the lifetime of the phosphor coating of the tube.

Adjust the focus so you have the sharpest possible image.

Use the horizontal and vertical position controls to center the image on the screen.

In the case of my Tektronix 2215A, the `XY` mode hides as one of the steps of the right-most rotational input, the timebase or `A and B SEC/DIV`.
In the picture below I marked all settings you may need to adjust.

<!--%
lightgallery([
    [ "img/osci_music_6.jpg", "My Tektronix 2215A set up for Oscilloscope Music" ],
])
%-->

## Hardware
<a class="anchor" name="hardware"></a>

We need to consider the environments this device will be used in.
Both at the Toolbox anniversary, as well as the IBO fair, it will be displayed as part of a public show, with many people walking by and maybe stopping for a short time.
And I will not be there all the time, so it will be operated by other Toolbox members (setting it up, turning it on or off), or even the visitors (switching tracks).

With the part selection outlined above, the solution was kind of obvious.
Have a script on the Pi, automatically starting playback of the music files, with a small OLED and some buttons to control playback, and ideally with some kind of UPS for ease of powering the device and properly shutting down to not corrupt the SD card.

<!--%
lightgallery([
    [ "img/osci_music_1.jpg", "Top of Osci Music Player" ],
    [ "img/osci_music_3.jpg", "Insides of Osci Music Player" ],
])
%-->

Here are the parts I used and the prices I paid at the time of building this.

<!--%
tableHelper([ "align-right", "align-last-right", "align-right monospaced"],
    [ "Part", "Description", "Cost" ], [
        [ "Pi", ("Raspberry Pi Zero 2 W", "https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/"), "24.49€" ],
        [ "DAC", ("HiFiBerry DAC+ Zero", "https://www.hifiberry.com/shop/boards/hifiberry-dac-zero/"), "30.99€" ],
        [ "Batt", ("PiSugar 2", "https://www.pisugar.com/"), "35.99€" ],
        [ "OLED", ("SSD1306 I2C 128x64", "https://www.az-delivery.de/en/products/0-96zolldisplay"), "4.40€" ],
        [ "Btns", ("2x 12mm momentary switch", "https://www.amazon.de/dp/B0811QKG1R"), "1.60€" ],
        [ "Conn", ("2x Cinch panel mount", "https://www.amazon.de/dp/B0B4SG1JM6"), "1.60€" ],
        [ "Amp", ("Stereo amplifier module", "https://www.amazon.de/dp/B07KQCKWF8"), "1.40€" ],
        [ "Spkr", ("Stereo speakers", "https://www.amazon.de/dp/B08QFTYB9Z"), "5.00€" ],
        [ "Ext", ("Micro-USB panel mount", "https://www.amazon.de/dp/B06XZ2NFP1"), "7.69€" ],
        [ "BNC", ("Cinch to BNC adapter", "https://www.amazon.de/dp/B08L8YBWMY"), "0.50€" ],
        [ "Pot", ("Volume knob", "https://www.amazon.de/dp/B08214YZDS"), "0.85€" ],
        [ "Cable", "Cinch stereo cable", "~2.00€" ],
        [ "Case", "Lunchbox from supermarket", "~5.00€" ],
        [ "", "Sum", "85.52€" ]
    ]
)
%-->

Of course you also need some bits of copper wire for the internal connections inside the device.
I also used a bunch of male and female 2.54mm pin headers to be able to disconnect stuff.
Also M2.5 spacers to properly mount the PCBs around the Pi Zero, M2 spacers for the OLED, as well as a couple of cable-ties.

<!--%
lightgallery([
    [ "img/osci_music_4.jpg", "Audio output of Osci Music Player" ],
    [ "img/osci_music_5.jpg", "Power input of Osci Music Player" ],
])
%-->

For this project I decided to use a cheap plastic lunchbox as a case.
This worked relatively well.
Just take care with the lid, it was quite hard in my case, causing it to crack when I tried to drill a hole that was too big.
But some superglue saved the day.

## Software
<a class="anchor" name="software"></a>

I've been using the [Raspberry Pi OS (Legacy, 32bit) Lite](https://downloads.raspberrypi.com/raspios_oldstable_lite_armhf/images/raspios_oldstable_lite_armhf-2023-12-06/2023-12-05-raspios-bullseye-armhf-lite.img.xz) image.
Install it [as usual](https://www.raspberrypi.com/software/), set up a user account, wireless network connection and SSH login.

Prepare the environment by installing all required dependencies:

<pre class="sh_sh">
sudo sh -c 'echo "dtoverlay=hifiberry-dac" >> /boot/config.txt'
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3 python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 ffmpeg
curl "http://cdn.pisugar.com/release/pisugar-power-manager.sh" | sudo bash
pip install pisugar luma.oled psutil
sudo usermod -a -G spi,gpio,i2c $USER
</pre>

Reboot after the last command so the new settings take effect and the power manager can do its thing.
If in doubt, also take a look at the [PiSugar 2 manual](https://github.com/PiSugar/PiSugar/wiki/PiSugar2).

<!-- https://clay-atlas.com/us/blog/2021/06/30/html-en-copy-text-button/ -->
<script>
function copyEvent(id) {
    var str = document.getElementById(id);
    window.getSelection().selectAllChildren(str);
    document.execCommand("Copy")
}
</script>

Next put the script that controls playback on the device.
Here is [`~/osci-pi.py`](https://git.xythobuz.de/thomas/osci-music-player/raw/branch/master/osci-pi.py).
<button type="button" onclick="copyEvent('oscipipy')" class="clip-btn">Copy to clipboard</button>

<pre id="oscipipy" class="sh_python">
<!--%
include_url("https://git.xythobuz.de/thomas/osci-music-player/raw/branch/master/osci-pi.py")
%-->
</pre>

And you'll also need [`/etc/systemd/system/osci.service`](https://git.xythobuz.de/thomas/osci-music-player/raw/branch/master/osci.service) to start the script automatically.
Adjust the username and path accordingly.
<button type="button" onclick="copyEvent('osciservice')" class="clip-btn">Copy to clipboard</button>

<pre id="osciservice" class="sh_desktop">
<!--%
include_url("https://git.xythobuz.de/thomas/osci-music-player/raw/branch/master/osci.service")
%-->
</pre>

The `ExecStart` line has the parameters that are passed to the Python script.
This is the path of the directory that contains all the `.wav` files for the songs.
In this top-level folder, I called it `~/music`, put another level of directories named after the artist, then place the files in there.

Finally enable and start the new unit.

<pre class="sh_sh">
sudo systemctl daemon-reload
sudo systemctl enable --now osci.service
</pre>

The device should now start playing the music as soon as the power is turned on.
Before switching the device off, use the on-board button of the PiSugar to properly shutdown the OS, and only then move the power switch to the `Off` position.

You can also check out [the code in its Git repository](https://git.xythobuz.de/thomas/osci-music-player).
