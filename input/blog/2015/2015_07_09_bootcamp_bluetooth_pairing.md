title: Blog
post: Automatic Bluetooth Pairing in OS X and Windows
date: 2015-07-09
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

I’m using an Apple Magic Trackpad that is connected to my Computer using Bluetooth. It works under Mac OS X and also under Windows, but it does not pair automatically out-of-the-box. If it was previously paired with OS X, it has to be re-paired under Windows, and also the other way round.

The reason for this is simple. These Bluetooth devices not only identify each other using their MAC addresses, they also share an encryption key that is stored in the Trackpad and the OS, and is generated in the pairing process. If this key is the same on both OS, the Bluetooth device will pair automatically every time.

In OS X, the keys are stored in a plist file and can be retrieved like this:

    sudo defaults read /private/var/root/Library/Preferences/blued.plist

To find the MAC addresses of your adapter and device, alt-click on the bluetooth logo in the OS X menu bar.

In Windows, the key is stored in the registry at:

    HKLM/System/CurrentControlSet/services/BTHPORT/Parameters/Keys/*MAC*

In the Windows 10 Technical Preview, it’s not this exact location, but somewhere else in BTHPORT. You can’t miss it.

You need to take special care when accessing these keys. Start the registry editor using [PsExec from PsTools](https://technet.microsoft.com/de-de/sysinternals/bb897553.aspx):

    psexec -s -i regedit

But you can’t just copy-paste the key from one OS to the other, there is a trick to it. The key is stored backwards in Windows. Because the key is displayed to the user as ASCII-Hex bytes, you have to read the key backwards in pairs of two characters. For example:

    98542FF9 88E19449 475250E1 3943255B (Shown in OS X)
    5B254339 E1505247 4994E188 F92F5498 (Entered in Windows)

Thanks go to [pacnow for figuring this out](https://discussions.apple.com/thread/3113227?start=0&tstart=0). And [Soorma07 even made an Apple Script](https://github.com/Soorma07/OS-X-Bluetooth-Pairing-Value-To-Windows-Value) to automate parts of this process.

