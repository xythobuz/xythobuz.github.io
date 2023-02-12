title: Blog
post: Ergodox Infinity Repair
description: Kit-built open-source split ergonomic keyboard
date: 2022-11-28
comments: true
show_in_input_devices: true
---

It occurs to me that I never really wrote about my [Ergodox Infinity](https://deskthority.net/wiki/Infinity_ErgoDox) keyboard on here.
I got it from [Massdrop](https://drop.com/buy/infinity-ergodox) back in October 2016, as a kit with Cherry MX Clear switches and the additional flat plastic wrist rests.

This was my second mechanical keyboard after the [Tex Beetle](tex_beetle.html).
It is a kind-of-ortholinear split keyboard design, of course released as completely free open-source hardware and software.

In June 2017 I replaced most of the included clear keycaps with a [side-lit ABS keycap set](https://drop.com/buy/side-lit-abs-keycap-set), also from Massdrop.
But some keys are from other novelty keycap sets, I don't remember where I got these.

Some time around 2020 or 2021 I also 3D printed the ["Infinity Ergodox Ergonomic Stand" by rubenhak](https://www.thingiverse.com/thing:4079818) and I'm pretty happy with it.

<hr>

Now on to the actual issue that triggered this blog post.
Shortly after adding the tented base I had a little accident with a drink spilled over the keyboard.
Unfortunately it was a sticky sugary drink and it managed to get into a bunch of the switches.
The sugar acted like glue and the keyboard was no longer usable.

I left it on the healing bench for a while, but this didn't help much 😅

Because of the aluminium plate design, properly cleaning the keys requires desoldering them.
It's not a real problem, it's just busy work that takes some time.
But I finally found the motivation to do it.

First I had to remove the keys that were sticky and clean all residue from the plate.
Back when assembling the keyboard I decided to also solder in optional 3mm LEDs for each key.
These had to be unsoldered as well.

<!--%
lightgallery([
    [ "img/ergodox_repair_1.jpg", "PCB, keys to be removed are marked" ],
    [ "img/ergodox_repair_2.jpg", "base plate and PCB, keys removed" ],
])
%-->

The next step was cleaning the Cherry MX switches themselves.
This meant disassembling them, which is pretty easy.
Just pry the two case halves apart, using a small flat screw driver to lift the locking tabs.
Then I put everything in a soapy warm water bath.

<!--%
lightgallery([
    [ "img/ergodox_repair_3.jpg", "Disassembling the switches" ],
    [ "img/ergodox_repair_4.jpg", "Cleaning the switches" ],
    [ "img/ergodox_repair_5.jpg", "Drying the switches" ],
    [ "img/ergodox_repair_6.jpg", "Clean switches assembled again" ],
])
%-->

Now I was able to snap the switches back into the aluminium plate and solder them onto the PCB.
I simply left out the LEDs out of lazyness.
Removing them was kind of destructive and I don't really use them anyway.

<!--%
lightgallery([
    [ "img/ergodox_repair_7.jpg", "Keys mounted again" ],
    [ "img/ergodox_repair_8.jpg", "Keyboard back together" ],
    [ "img/ergodox_repair_9.jpg", "Keyboard on desktop" ],
])
%-->

And after less than two hours my keyboard is finally back in action!

This time I connected the left half to my computer.
I noticed that it was still flashed with my old Mac-style layout.
Apparently I only flashed the right half back when I switched to Arch Linux.
Fortunately I still had the binaries from my last build, so I simply flashed the left half and had my expected layout.

But I also noticed that I am no longer able to compile my [old repo](https://github.com/xythobuz/controller) state, it fails with "multiple definitions" while linking.
I will have to update to the current master of the [upstream firmware](https://github.com/kiibohd/controller) sometime soon.
