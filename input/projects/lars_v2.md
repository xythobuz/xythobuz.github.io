title: LARS v2
description: Upgrading the Looping Automated Rhythm Station
parent: projects
git: https://git.xythobuz.de/thomas/drumkit
github: https://github.com/xythobuz/lars
date: 2024-09-07
comments: true
---

So you may have read about our project [LARS](lars.html).
As mentioned I didn't have any hardware in the end to finish firmware development.
So I slightly updated the circuitry, layed out a new board, had it manufactured in China and assembled at home.

This is LARS v2, the second iteration of the same idea.

<!--%
lightgallery([
    [ "img/lars_v2_1.jpg", "LARS v2" ],
    [ "img/lars2_midi.mp4", "video/mp4", "", "", "LARS v2 playing MIDI example file" ],
])
%-->

It's basically the same device, just with five additional switches.
This allows for some more freedom in the user interface design.
Now the loop mode can mute individual tracks.
There's also USB MIDI support.

<!--%
lightgallery([
    [ "img/lars2_parts.jpg", "LARS v2 PCBs and parts" ],
    [ "img/lars_loop_controls.jpg", "LARS Loop Station controls" ],
])
%-->

As [usual](2024_05_05_auto_project_docs.html) I've added auto-generated [documentation](https://xythobuz.github.io/lars/), including [interactive 3D renders of the PCB](https://xythobuz.github.io/lars/pcb2_pcb.html) and some [usage hints](https://xythobuz.github.io/lars/usage.html).
The [gerber files](https://xythobuz.github.io/lars/plot/fab_pcb2.zip) and [BOM](https://xythobuz.github.io/lars/pcb2.html) to order your own are also available.

Unfortunately I'm kind of in the same situation now as with LARS v1.
I've gone much further with the firmware, it's now mostly usable.
But I've also given the hardware away again, so I can't finish it.

I should assemble another one soon...
