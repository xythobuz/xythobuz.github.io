title: Oscilloscope Video Display
description: Converting an analog composite video signal to XYZ
parent: projects
git: https://codeberg.org/xythobuz/osci-video-pcb
github: https://github.com/xythobuz/osci-video-pcb
date: 2025-12-22
comments: true
---

After playing [oscilloscope music](osci_music_player.html) the next obvious question that came up was: can we make it [run Doom](https://canitrundoom.org/)?

Turns out a couple of people already [did that](https://www.youtube.com/watch?v=OU16lIx_pC8), even in [different ways](https://www.youtube.com/watch?v=xZaKlLyikKg).
The last link is just running normal Doom on a modern LCD osci, which seems a bit boring.
Even more involved is modifying the game engine to output vectors, which has been done [here](https://www.mikeayles.com/#scopedoom) or [here, for Quake](https://www.lofibucket.com/articles/oscilloscope_quake.html).

For this project I copied the circuit from the [XYZ converter by MrSlehofer](https://www.youtube.com/watch?v=UZapLL3Qa-I).
The basic idea is to convert a CRT oscilloscope into a grayscale TV, by rastering each NTSC / PAL field line-by-line.
So the X and Y channels contain saw-tooth waveforms, with the X frequency matching the horizontal blank period, and the Y frequency matching the vertical blank period.
When Z is not connected you should therefore see something resembling a rectangular white 4:3 image.
Then Z just needs to have the amplitude of the video signal, which corresponds to the brightness at that moment in time.

Just to test that process out for the first time I turned the PCB into a KiCad design that can be assembled by JLCPCB.
This worked out well.
If you want to order some as well, use the [`production_files` from the repo](https://codeberg.org/xythobuz/osci-video-pcb/src/branch/master/production_files).

<!--%
lightgallery([
    [ "img/osci_video_pcb_1.jpg", "Assembled PCBs from JLCPCB" ],
    [ "img/osci_video_pcb_2.jpg", "Top of assembled PCB" ],
    [ "img/osci_video_pcb_3.jpg", "Bottom of assembled PCB" ],
])
%-->

Initially I had some problems getting the circuit to work at all.
The oscilloscope screen only showed some strange warbling lines or squares.

<!--%
lightgallery([
    [ "img/osci_video_pcb_4.jpg", "First FPV camera test" ],
    [ "img/osci_video_pcb_5.jpg", "Unsatisfying first results" ],
])
%-->

Turns out it is very susceptible to changes in voltage levels.
Depending on the source you use to feed it you may need to adjust some resistance values.
In the end I replaced two resistors with potentiometers.
This allows easy on-the-fly adjustments.
Try a 10k poti for R1, and a 100k Poti for R10.
Big thanks to [Walter (DL2OL)](https://dl2ol.darc.de/) from the [local ham radio club](https://wiki.toolbox-bodensee.de/doku.php?id=amateurfunk:start) co-located at [our makerspace](https://toolbox-bodensee.de/) for helping with tuning the circuit!

<!--%
lightgallery([
    [ "img/osci_video_1.jpg", "First successful test" ],
    [ "img/osci_video_2.jpg", "FPV camera setup" ],
    [ "img/osci_video_3.jpg", "Closeup with noticeable distortion" ],
])
%-->

The next step was to use a Raspberry Pi 1 that I still had lying around, because of the prominent analog video output connector on there.

<!--%
lightgallery([
    [ "img/osci_video_4.jpg", "Test setup with switching power supply" ],
    [ "img/osci_video_5.jpg", "Noisy desktop background" ],
])
%-->

Powering it with switching voltage regulators was not a good idea.
The voltage ripple on the supply lines is very visible on the output image.
So next I used a lab power supply for the video converter PCB, and an official Raspberry Pi USB wall wart for 5V.
I also used the opportunity to switch to a beefier Raspberry Pi 3, after I learned that it still has an AV out on the 3.5mm jack.

<!--%
lightgallery([
    [ "img/osci_video_6.jpg", "Test setup with one lab power supply (12V) and a USB wall wart" ],
    [ "img/osci_video_7.jpg", "Running doom for the first time" ],
    [ "img/osci_video_8.jpg", "Very noisy xterm" ],
])
%-->

Replacing the USB power supply with another big lab power supply and dimming the room lights / providing some shade for the scope screen meant we could finally play for the first time.
[Philipp](https://www.phschoen.de/) and I tried both Doom ([chocolate-doom](https://www.chocolate-doom.org/wiki/index.php/Chocolate_Doom)) and [Tux Racer](https://tuxracer.sourceforge.net/).

<!--%
lightgallery([
    [ "img/osci_video_3.mp4", "video/mp4", "", "", "Doom getting kinda playable" ],
    [ "img/osci_video_4.mp4", "video/mp4", "", "", "Playing Tux Racer" ],
])
%-->

Here's another run where we actually completed the first Doom 1 Episode.
I also brought my old Tektronix scope.
All the scopes we tried don't have any gain control for their Z / brightness input, and the video PCB is also not that finely adjustable.
With the Tektronix scope the voltage ranges and therefore contrast and brightness seem to fit best.

<!--%
lightgallery([
    [ "img/osci_video_5.mp4", "video/mp4", "", "", "Doom finally running well" ],
    [ "img/osci_video_9.jpg", "Test setup with two lab power supplies (12V and 5V)" ],
])
%-->

To have another portable setup for display in the local makerspace I planned to iterate on the case idea from my [Osci Music Player](osci_music_player.html).
The housing should be a plastic kitchen ware container with all required connections routed to panel mount connectors.

Everything was initially planned to be powered by a USB-C PD power supply with 12V for the converter PCB and a step-down converter to power a Raspberry Pi with 5V.
Unfortunately I think some more serious filtering of the regulator outputs would be needed to get acceptable image quality while using step-down converters.

For now I'm simply hooking up some high quality lab power supplies.
Considering the device is always operated near an oscilloscope that should probably not be too restricting.

Though I have to admit, I'm still not quite happy with this raster approach.
The high frequency audio interface of the Osci Music Player hardware could also be used to improve the visual quality of [Michael Ayles' ScopeDoom](https://www.mikeayles.com/#scopedoom).

## More Videos

<div class="collapse">Some more media I didn't use above.</div>
<div class="collapsecontent">
<!--%
lightgallery([
    [ "img/osci_video_1.mp4", "video/mp4", "", "", "First Doom test (1 / 2)" ],
    [ "img/osci_video_2.mp4", "video/mp4", "", "", "First Doom test (2 / 2)" ],
])
%-->
</div>
