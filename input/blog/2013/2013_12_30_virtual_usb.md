title: Blog
post: Booting a USB Stick in VirtualBox with a Mac OS X Host
date: 2013-12-30
comments: true
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

You can't just boot from a USB Stick with VirtualBox because it's BIOS does not support USB.
However, you can still get it to boot from USB.
But first, you have to convince OS X not to remount your USB Stick everytime it's `/dev/diskX` file is accessed.

To do this, you need to know the Label of your USB drive (with spaces escaped with `\`) and it's filesystem type (fat32 in this case).

Create the `/etc/fstab` file, if it doesn't exist already, and mark your stick as `noauto`:

<pre class="sh_sh">
sudo touch /etc/fstab
sudo nano /etc/fstab
LABEL=yourUSBstick none fat32 rw,noauto
</pre>

Then create a VirtualBox Disk Image, pointing to the block device file of your USB stick. Use diskutil to find out the device file name.

<pre class="sh_sh">
diskutil list
sudo VBoxManage internalcommands createrawvmdk -filename rawUsbStick.vmdk -rawdisk /dev/diskX
</pre>

Now, run VirtualBox as root

<pre class="sh_sh">
sudo /Applications/VirtualBox.app/Contents/MacOS/VirtualBox
</pre>

Create a new Virtual Machine, using the .vmdk file created before as virtual hard disk drive. Boot it, and...

Done! :)
