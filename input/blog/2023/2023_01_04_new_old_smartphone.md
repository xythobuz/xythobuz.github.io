title: Blog
post: Samsung S7 Edge with /e/ OS
description: Completing my switch out of the Apple Walled Garden
date: 2023-01-04
comments: true
---

As a final step in leaving Apple behind I had to get rid of my iPhone SE.
While using it since September 2016 it finally died from multiple organ failure in 2022, after six years.
I already backed the [Astro Slide](https://www.indiegogo.com/projects/astro-slide-5g-transformer) in November 2021, but while it is shipping to the first customers already, I'm pretty far back in line and haven't received mine.

For a while I used a Samsung S22 from my workplace as a replacement, but this was only a temporary solution.
This was my first Android device in a long time, so it helped getting used to the OS again.

Now I've had the fortune of getting a Samsung S7 Edge gifted to me, which is now my daily driver, hopefully until the Astro Slide arrives.
I wouldn't have bought an S7 Edge for myself if I had the choice, the display really feels strange to hold properly.
So the first thing I had to do was [print a case](https://www.printables.com/model/257202-samsung-galaxy-s7-edge-cover).
This really helps.

<!--%
lightgallery([
    [ "img/s7_edge_front.jpg", "Front of S7 Edge with 3D printed case" ],
    [ "img/s7_edge_back.jpg", "Back of S7 Edge with 3D printed case" ],
])
%-->

Of course I also didn't want to run stock Android on a device I own, so I went searching for a good alternative.
I've looked at [LineageOS](https://lineageos.org/) and the [MicroG fork of LineageOS](https://lineage.microg.org/), but my device is unfortunately not (or no longer) supported.

Looking at the [Wikipedia list of Custom-ROMs](https://de.wikipedia.org/wiki/Liste_von_Android-Custom-ROMs) then led me to [/e/ OS](https://e.foundation/e-os/).
This also is a fork of LineageOS, with MicroG replacing all the Google services.
There's not even a Play Store, they have their own App installer that nicely integrates free-software sources from F-Droid as well as Play Store apps.

I'm really happy with the experience.
All Apps I use are available from F-Droid anyway, so this was not at all a problem.
And I really like the included ad / tracker blocking functionality.

But there also was a small issue.
On WiFi everything worked absolutely fine.
But after leaving the house I had some strange connectivity problems.
Many websites loaded fine, but some domains (that surely exist) did not resolve.
I played around with the Private DNS settings, but this didn't change much.

After much searching I finally found a [comprehensive issue report on the /e/ project GitLab](https://gitlab.e.foundation/e/backlog/-/issues/5668).
But I can't register for some reason (they don't like my E-Mail domains), so I'm posting here.

The problem lies with my mobile network provider, Congstar, the cheap brand of Deutsche Telekom / T-Mobile, or to be more specific the APN for this network on the /e/ ROM.
It has some wrong settings.
Apparently the correct settings could be found on the Congstar website, according to the issue report linked above, but the link no longer works.
So here is what I had to change.

    Settings
    Network & Internet
    Mobile Network
    Advanced
    Access Point Names
    congstar Internet
    Change "APN" to "internet.v6.telekom"
    Set both "APN protocol" and "APN roaming protocol" to "IPv4/IPv6"

This fixed the connection issues.

I suspect it is related to the whole IPv4 / IPv6 debacle.
Only recently someone mentioned on Hackernews that [not even GitHub is reachable via IPv6](https://news.ycombinator.com/item?id=33894933).
This is a really sad state of affairs.
I'm not sure there's another example of a technology migration that went as bad as this one, globally speaking.
