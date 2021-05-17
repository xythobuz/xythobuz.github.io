title: OpenRaider
description: Classic Tomb Raider game engine re-implementation
parent: projects
github: https://git.xythobuz.de/thomas/OpenRaider
date: 2013-12-15
update: 2015-08-13
---

In 2013 I decided to fork the [OpenRaider](http://openraider.sourceforge.net/) project to get it to run on a modern Mac OS X machine.
I also wanted to learn a bit about 3D graphics and OpenGL.
Without planning it, I completely rewrote the whole project in a span of about two years.

<!--%
printLatestRelease("xythobuz", "OpenRaider")
%-->

I wrote some blog posts about OpenRaider.

* [Initial blog post about fork](2014_03_22_openraider.html)
* [Work on font rendering](2014_06_14_trle_font.html)

I also wrote a bit about my progress in some GitHub release notes.

* [Reincarnation, 2013-12-21](https://github.com/xythobuz/OpenRaider/releases/tag/v0.1.1-20131214)
* [Christmas present :D, 2013-12-27](https://github.com/xythobuz/OpenRaider/releases/tag/v0.1.1-20131227)
* [Meta improvements, 2014-03-13](https://github.com/xythobuz/OpenRaider/releases/tag/0.1.2-20140313)
* [Look n Feel n Architecture, 2014-07-27](https://github.com/xythobuz/OpenRaider/releases/tag/0.1.3-20140727)
* [Rewrite, 2015-03-13](https://github.com/xythobuz/OpenRaider/releases/tag/0.1.4-20150313)

You can find the latest state of the project [on my server](https://git.xythobuz.de/thomas/OpenRaider) and [on GitHub](https://github.com/xythobuz/OpenRaider).
Pre-made Mac OS X binaries are available in the [GitHub releases](https://github.com/xythobuz/OpenRaider/releases).

A package for Arch Linux was also available on the AUR, but it has since been removed due to inactivity.
It should however be possible to run OpenRaider on Linux without any issues.

I also tried to get a Windows port working.
It should in theory be possible without too much work, but I didn't know enough about Windows development to get it running back when I tried.

Here are some screenshots from different stages of development.

<!--%
lightgallery([
    [ "img/openraider_screen_1.png", "Main Menu, made with imgui" ],
    [ "img/openraider_screen_2.png", "Debug UI, made with imgui" ],
    [ "img/openraider_screen_3.png", "Skeletal Mesh rendering is currently broken" ],
    [ "img/openraider_screen_4.png", "" ],
    [ "img/openraider_screen_5.png", "" ],
    [ "img/openraider_screen_6.png", "Old quake-style terminal implementation" ],
    [ "img/openraider_screen_7.png", "Old main menu" ],
    [ "img/openraider_old.png", "What I saw when it ran for the first time" ],
    [ "img/openraider_old2.png", "" ],
    [ "img/openraider_sdl2.png", "" ],
    [ "img/openraider_new.png", "" ],
    [ "img/openraider_new2.png", "" ],
    [ "img/trle_1.png", "Uuhh... Yeah..." ],
    [ "img/trle_2.png", "Not too bad...?" ],
    [ "img/trle_3.png", "Woah, progress!" ],
    [ "img/trle_4.png", "Now with proper alignment" ],
    [ "img/trle_5.png", "Trying another font file" ],
    [ "img/trle_6.png", "Fixed the lowercase p!" ],
    [ "img/trle_7.png", "And with custom lps file" ]
])
%-->
