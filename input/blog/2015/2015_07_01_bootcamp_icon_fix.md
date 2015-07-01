title: Blog
post: Bootcamp Icon fix
date: 2015-07-01
comments: true
flattr: true
twitter: xythobuz
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

If you like to give each disk appearing on your Macs desktop it’s own icon, and are a Bootcamp user, you’re probably aware that the Bootcamp drive icon is reset after each reboot. Fortunately, this can be fixed in an easy automated fashion.

The only requirement is NTFS write support. To get this, install osxfuse and ntfs-3g, or enable the built-in NTFS write support ([find details here](http://apple.stackexchange.com/questions/152661/write-to-ntfs-formated-drives-on-yosemite)).

First, set the icon you wish to use like you always would (right-click, Get Info, click on icon, cmd+v to paste new icon). This creates the hidden file `.VolumeIcon.icns` in the root of your disk. Copy it somewhere safe:

    cp /Volumes/TX-55/.VolumeIcon.icns /Users/thomas/Pictures/Icons/VolumeIcon.icns

Next, we need to create a little shell script that copies this file again after it is lost on reboot:

    vim /Users/thomas/bin/fixBootcamp.sh
    
    #!/bin/sh
    cp /Users/thomas/Pictures/Icons/VolumeIcon.icns /Volumes/TX-55/.VolumeIcon.icns
    
    :wq
    chmod a+x /Users/thomas/bin/fixBootcamp.sh

Finally create a LaunchAgent property list:

    vim ~/Library/LaunchAgents/de.xythobuz.fixBootcamp.plist
    
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>de.xythobuz.fixBootcamp</string>
        <key>Program</key>
        <string>/Users/thomas/bin/fixBootcamp.sh</string>
        <key>RunAtLoad</key>
        <true/>
    </dict>
    </plist>
    
    :wq

You can now set this LaunchAgent to be executed on each Login:

    launchctl load ~/Library/LaunchAgents/de.xythobuz.fixBootcamp.plist

To test it without logging out and back in:

    launchctl start de.xythobuz.fixBootcamp

That was easy, right? :) *Tested on OS X Yosemite 10.10.4...*

