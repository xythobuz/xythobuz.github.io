title: Blog
post: iStick Pico 25 OLED Replacement
description: Repairing an aging dim 510 box mod display
date: 2024-09-16
comments: true
---

Years ago I bought a cheap chinese E-Cigarette 510 box mod, the Eleaf iStick Pico 25.
It's running the ArcticFox custom firmware which sadly seems to be [no longer available](https://nfeteam.org/).
I never really used it for anything, but for [reasons](https://vapeengineering.de/) I want to get it going again.
Unfortunately the display is so dim that it can no longer be used.
So I wanted to repair the device.

I found [this comment on Reddit](https://old.reddit.com/r/Vaping/comments/4t5w0k/the_screen_of_my_eleaf_pico_is_fading_every_day/jz009z6/) explaining that it's just a standard SSD1306 128x32 0.91" OLED display.
[This guy](https://old.reddit.com/r/Vaping/comments/18d9kkq/brand_new_istick_pico_75w_with_a_dim_screen/krzd9ix/) says initially Eleaf used ribbon cable connectors, making the replacement easy, and one shouldn't try without them.
But actually soldering on a replacement is very easy.

First open the device and carefully remove the plastic display mount and desolder the ribbon cable.

<!--%
lightgallery([
    [ "img/istick_pico_oled_replacement_1.jpg", "Old display, top view" ],
    [ "img/istick_pico_oled_replacement_2.jpg", "Display holder removed" ],
])
%-->

The most difficult part for me was getting the [replacement OLED](https://www.az-delivery.de/en/products/0-91-zoll-i2c-oled-display) removed from the breakout board.
I used some lighter fuel to dissolve the glue and carefully levered and cut it off, trying not to break the glass or destroy the ribbon PCB.

<!--%
lightgallery([
    [ "img/istick_pico_oled_replacement_3.jpg", "Replacement display" ],
])
%-->

Then just solder it on like any other SMD part.

<!--%
lightgallery([
    [ "img/istick_pico_oled_replacement_4.jpg", "Repair done" ],
])
%-->

Works great!
