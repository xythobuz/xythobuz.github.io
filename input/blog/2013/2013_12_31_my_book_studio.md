title: Blog
post: Replace a Western Digital MyBook Studio Hard Disk Drive
date: 2013-12-31
comments: true
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

I had some problems trying to disassemble and replace a Western Digital My Book Studio external hard disk drive.

There are four screws on the outside, one of them under a warranty label. I guess with a Heatgun or something similar you could remove the label without destroying it.

But the case is still closed rock-solid after removing the screws. That's thanks to some metal-clips around the edge.
Use a flathead screwdriver to carefully wiggle the inner case approx. 1cm out of the outer shell.

Even if it doesn't feel this way, there are no more clips after sliding as seen in the second picture.
Just use a long screwdriver as a lever to completely slide the inner case out of it's shell.

The hard drive itself is not mechanically connected to the inner case. Just slide it out, playing with the black rubber things in the corners to get it loose.

Now remove the two screws connecting the SATA adaptor to the hard drive, and it's metal holder screwed to the hard drive and place them on your new disk.
Then follow the same steps in reverse to put it back together.

### But beware!

The My Book Studio uses hardware encryption with it's SATA adaptor. This means, you won't be able to read the data already on the drive using SATA.

Also, the data on the replacement drive won't be readable in the enclosure. So get off your data before switching the drives, and put your new data on it afterwards!

<div class="lightgallery">
    <a href="img/wd-1.jpg">
        <img src="img/wd-1_small.jpg" alt="Only four screws outside">
    </a>
    <a href="img/wd-2.jpg">
        <img src="img/wd-2_small.jpg" alt="Slide the case open">
    </a>
    <a href="img/wd-3.jpg">
        <img src="img/wd-3_small.jpg" alt="There are no clips. Just use some force!">
    </a>
    <a href="img/wd-4.jpg">
        <img src="img/wd-4_small.jpg" alt="Slide out the HDD to it's printed side">
    </a>
    <a href="img/wd-5.jpg">
        <img src="img/wd-5_small.jpg" alt="Done">
    </a>
</div>
