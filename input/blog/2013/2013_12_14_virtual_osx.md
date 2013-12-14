title: Blog
post: Installing Mavericks as VirtualBox Guest
date: 2013-12-14
comments: true
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

Recently, I set out to get OS X 10.9 running as VirtualBox Guest, with Mavericks as Host. This should be easy enough, right? Just download the Mavericks Installer from the AppStore, get the Image from inside the App Package, as you would do to get a bootable USB Stick. Done!

It turns out that Apple started using strange Aliases in their Install Image with Mountain Lion. You have to do some moving around to get an ISO you can plug into VirtualBox.

If you got the Mavericks Installer in /Applications, run this script to get a bootable ISO on your Desktop.

<pre class="sh_sh">
#!/bin/sh
hdiutil attach /Applications/Install\ OS\ X\ Mavericks.app/Contents/SharedSupport/InstallESD.dmg -noverify -nobrowse -mountpoint /Volumes/install_app
hdiutil convert /Volumes/install_app/BaseSystem.dmg -format UDSP -o /tmp/Mavericks
hdiutil resize -size 8g /tmp/Mavericks.sparseimage
hdiutil attach /tmp/Mavericks.sparseimage -noverify -nobrowse -mountpoint /Volumes/install_build
rm /Volumes/install_build/System/Installation/Packages
cp -rp /Volumes/install_app/Packages /Volumes/install_build/System/Installation/
hdiutil detach /Volumes/install_app
hdiutil detach /Volumes/install_build
hdiutil resize -size `hdiutil resize -limits /tmp/Mavericks.sparseimage | tail -n 1 | awk '{ print $1 }'`b /tmp/Mavericks.sparseimage
hdiutil convert /tmp/Mavericks.sparseimage -format UDTO -o /tmp/Mavericks
rm /tmp/Mavericks.sparseimage
mv /tmp/Mavericks.cdr ~/Desktop/Mavericks.iso
</pre>

[Credits](http://forums.appleinsider.com/t/159955/howto-create-bootable-mavericks-iso)


Hmm, so searching for *Mavericks bootable USB* instead of *Mavericks in VirtualBox* would have brought me to my target much earlier... Who knew? :P
