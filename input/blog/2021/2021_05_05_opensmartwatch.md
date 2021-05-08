title: Blog
post: Open-Smartwatch
date: 2021-05-05
---

Because of [a recent article on Hackaday](https://hackaday.com/2021/04/08/an-open-source-smart-watch-youd-actually-wear/) I was made aware of [the Open-Smartwatch project](https://open-smartwatch.github.io/) from [Paul's 3D Things](https://p3dt.net/).

I have ordered two [watches from AliExpress](https://de.aliexpress.com/item/1005002341342799.html), one for me and one for my SO, as well as some [matching batteries](https://de.aliexpress.com/item/4000121983257.html).

They arrived but unfortunately mine has some problems.
One of the buttons is broken.
It can not be pressed and is permanently stuck.
Possibly because of that (I thought) I have also not been able to get it to work again after I uploaded a self-compiled stock firmware.
It worked once after taking it out of the package, and also once after flashing.
But after that it didn't show anything (the LCD backlight turns on and off as expected, but the screen stays black).

Turns out, the display also had some problems.
It only worked when the flex cable was pressed in a very specific spot, relatively hard.
Unfortunately, while playing around with that, I now also broke the display glass itself.

I'm now waiting for a replacement...

I printed the files from "case-light-round-1.6mm-pcb-printed-straps" in the [3d-files repository](https://github.com/Open-Smartwatch/3d-files/) of Open-Smartwatch.
Because I like it colorful, I decided to print the parts in Orange, Blue and Green PETG filament.

I had some problems getting in the 10mm screws that hold the body together.
The hole in the bottom part was too large, and with not enough depth the screws did not grip properly.
As a work-around, it is possible to use 12mm M2 screws with a washer, but it does not look as nice.

It took quite some filing work to get the buttons to fit and move smoothly, as well as for the wrist strap to feel nice.
But the strap is now surprisingly comfortable.
I also like the look of the screws in the strap!
The latching mechanism is also a bit tricky and took a bit of post-print work to get it to close properly.
But as a first step it seems to work ok.

Just for fun, and because for me it was the easier solution, I re-created the complete case and strap in OpenSCAD.
The hole sizes can now be specified easily, and I tweaked some other small things.
I added button labels to the top piece, added rounded edges to the strap parts and modified the strap mounting piece on the bottom part so all strap pieces are the same and you don't need two special ones.

My design can be found in [the 'openscad' branch of my 3d-files fork](https://github.com/xythobuz/3d-files/tree/openscad).

<!--%
lightgallery([
    [ "img/osw_prints.jpg", "All my prints for the development of my re-design" ],
    [ "img/opensmartwatch_1.jpg", "Original 3D printed case and wrist strap" ],
    [ "img/osw_design_1.png", "Work in progress of my re-design" ],
    [ "img/osw_design_2.png", "Work in progress of my re-design, with colors" ]
])
%-->

I'm looking forward to playing around more with it. The source code can be found in the [open-smartwatch-os repository](https://github.com/Open-Smartwatch/open-smartwatch-os) on GitHub.
I did take a look and it still seems to be relatively small and understandable.

I hope it will actually be possible to show notifications from Android (I'm still using an iPhone currently, but I want to [switch](https://www.indiegogo.com/projects/astro-slide-5g-transformer) soon).

I also plan to create my own watch face, which should not be too much work with the way the OS is currently working.
I'm also looking forward to see how the project will progress and what changes the community will bring to the firmware.
