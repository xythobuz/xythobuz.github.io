title: Blog
post: Spacenav-Plus for Mac OS X
description: Fork of Linux driver and added software support
date: 2016-05-25
comments: true
flattr: true
github: https://github.com/xythobuz/spacenav-plus
parent: stuff
position: 90
---

**Update from May 2020:**
I've now switched to using Arch Linux full-time, so I'm no longer using my port of spacenav to use my spacemouse.
Fortunately, a spacenav-plus package has recently [appeared in the AUR](https://aur.archlinux.org/packages/spacenav-plus/) and works just fine.
Also, Blender, FreeCAD and OpenSCAD now all support spacenav out-of-the-box without any patches required!

Since I've got my [Fabrikator Mini 3D printer](2016_03_24_marlin_fabrikator_mini.html), I've spent some timer [creating things](http://www.thingiverse.com/xythobuz/designs), mainly with [OpenSCAD](http://www.openscad.org).

I've still got an old [Spacemouse Classic](http://spacemice.org/index.php?title=Spacemouse_Classic) laying around. It's 20 years old at this point and my model connects to a computer using a RS232 serial connection.

<div class="lightgallery">
    <a href="img/spacemouse.jpg">
        <img src="img/spacemouse_small.jpg" alt="My Spacemouse Classic">
    </a>
</div>

This device has originally been [developed by the DLR (Deutsches Zentrum für Luft- und Raumfahrt)](http://www.dlr.de/rmc/rm/en/desktopdefault.aspx/tabid-9467/16255_read-8998/), then found it's way to Logitech and later 3Dconnexion. You can still get [their original drivers](http://www.3dconnexion.de/service/legacy-driver.html) for Windows XP and Linux, but they probably won't run on any modern system.

There is an open-source replacement for the Linux driver, called [spacenav](http://spacenav.sourceforge.net) / [spacenav-plus](https://github.com/BenBergman/spacenav-plus) ([fork](https://github.com/Tehrasha/spacenav-plus)), that can interface the serial Spacemouse Classic on most POSIX systems and even has support for USB based Spacemice, but only on Linux. It also completely emulates the original 3Dconnexion Linux driver interface, using X11 events. Alternatively, the data can be gathered using a simple POSIX file socket.

I've [created my own fork of spacenav-plus](https://github.com/xythobuz/spacenav-plus), modifying the build system to support building on Mac OS X. I've also reimplemented the official 3Dconnexion Mac OS X driver interface, resulting in a 3DconnexionClient.framework that should allow using the spacenav-plus driver with [most supported software](http://www.3dconnexion.de/supported-software/software0.html). I've tested Google Earth and Blender.

Finally I've created/modified [patches for both OpenSCAD and FreeCAD](https://github.com/xythobuz/spacenav-plus#using-it-in-other-programs) to allow them using the spacenav-plus file interface on Mac OS X.

<div class="lightgallery">
    <a href="img/spacemouse_ledstrip.jpg">
        <img src="img/spacemouse_ledstrip_small.jpg" alt="My Spacemouse Classic">
    </a>
</div>

And something interesting I've noticed: even though the Spacemouse Classic is using optical sensors to track movements, it's picking up much noise from the LED strip I've mounted under my work bench. I simply can't use the Spacemouse while this light is plugged in!

