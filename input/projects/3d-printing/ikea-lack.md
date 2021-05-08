title: Ikea Lack Table DIY
description: Another iteration of the DIY Ikea Lack 3D printer shelves
parent: 3d-printing
position: 40
comments: true
flattr: true
---

<span class="listdesc">[...back to 3D-Printing overview](3d-printing.html)</span>

As is common in the 3D printing community, I have built myself a tower of Ikea Lack tables to store my printers in.
It has three levels.
I also included some lights to properly see whats going on, as well as a slide-out table for my small printer.

## Mounting Hardware

There are many solutions available, now more than back when I built this.
Nonetheless I decided to design my own simple brackets to mount the feet of one table to the one below it.

For the middle level of the tower, I added some pieces of wood to make more space, so it can fit my large printer comfortably.

<!--%
lightgallery([
    [ "img/lack-simple-bracket.png", "Design of my mounting bracket" ]
])
%-->

My design files for the mounting bracket [can be found on my Gitea server](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/ikea-lack).

## Slide out table



## Filament holder



My design files for the filament holder [can be found on my Gitea server](https://git.xythobuz.de/thomas/3d-print-designs/src/branch/master/ikea-lack).

## Concrete slab for noise and vibration dampening

Unfortunately, because the Ikea Lack tables are very lightweight and also hollow, they tend to amplify the sound coming from the 3D printers on them.
But there is an easy solution to this: vibration dampening by increasing the mass.
This can be achieved for example by simply creating a large concrete slab.
In my case, it weighs about 17kg.

First, build a simple wooden frame to contain the wet concrete.
I've used cheap 40x15x1000mm wood pieces and cut them to 555mm, screwing them together in the corners.
For the surface below the frame, I've used an old cardboard box.
I've "sealed" the surfaces of the cardboard and the wood pieces with clear flex-o-tape, to avoid the water wicking out of the concrete too fast, and to be able to remove the pieces easily later-on.

<!--%
lightgallery([
    [ "img/ikea_lack_concrete_1.jpg", "Simple wooden frame" ],
    [ "img/ikea_lack_concrete_2.jpg", "Screwed together in the corners" ],
    [ "img/ikea_lack_concrete_3.jpg", "Added some tape to seal the surface" ]
])
%-->

Then I've simply hand-mixed about one half of a 35kg bag of cement/sand mixture with 2l of clear tap-water.
The resulting sludge can then be filled into the frame.
Apply some vibrations to the edges of the frame using a hammer, and using your hand on top of the concrete, to get most of the bubbles out of the mixture and get it to settle properly.
You should then use a piece of wood to really get the surface flat.

Also, be careful: avoid contact of the concrete with your skin, it burns after a while!

<!--%
lightgallery([
    [ "img/ikea_lack_concrete_4.jpg", "Mixing the concrete" ],
    [ "img/ikea_lack_concrete_5.jpg", "Final consistency" ],
    [ "img/ikea_lack_concrete_6.jpg", "Filling the frame" ],
    [ "img/ikea_lack_concrete_7.jpg", "In my first attempt, I just tried to form the surface by hand. It worked, but is not perfect." ],
    [ "img/ikea_lack_concrete_8.jpg", "Closing it up for 24h" ],
    [ "img/ikea_lack_concrete_9.jpg", "Side-view" ]
])
%-->

After about 24h, the frame can already be removed.
Because of the large surface area and the low volume of our piece, it get's hard quite quickly.
And also, we're not using it for large static loads, so we don't have to wait the full 28-days specified by the manufacturer.
The small parts at the edges where the concrete slightly got under the frame can just be broken off by hand.

<!--%
lightgallery([
    [ "img/ikea_lack_concrete_10.jpg", "After 24h, one side removed" ],
    [ "img/ikea_lack_concrete_11.jpg", "The small parts at the edge can just be broken off easily by hand" ],
    [ "img/ikea_lack_concrete_12.jpg", "Final result, right view" ],
    [ "img/ikea_lack_concrete_13.jpg", "Final result, left view" ]
])
%-->

And it works perfectly, the noise of the printer is greatly reduced!

Here are some more photos of the second slab I made.

<!--%
lightgallery([
    [ "img/ikea_lack_concrete_v2_1.jpg", "Frame, with corners for Lack legs" ],
    [ "img/ikea_lack_concrete_v2_2.jpg", "Mixing the concrete" ],
    [ "img/ikea_lack_concrete_v2_3.jpg", "More hard mixing work" ],
    [ "img/ikea_lack_concrete_v2_4.jpg", "Pouring it out" ],
    [ "img/ikea_lack_concrete_v2_5.jpg", "After vibrating it" ]
])
%-->
