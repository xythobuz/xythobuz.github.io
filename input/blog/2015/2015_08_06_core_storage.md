title: Blog
post: Core Storage Partition resizing
date: 2015-08-06
comments: true
flattr: true
---

Basically, Disk Utility in Yosemite started using Core Storage sometimes when creating new partitions. Unfortunately, if it then encounters a Core Storage Volume, it completely shits its pants and doesn’t do anything anymore.

Presumably, this will be fixed in the next release, El Capitan.

In the meantime, some command line diskutil Foo is required to fix your partition map when Disk Utility does no longer want to do this.

In my case, I wanted to shrink a Core Storage Logical Volume, to make room for a new NTFS partition shared between Mac and Windows. Of course, Windows can’t read the Core Storage Volume, and NTFS inside Core Storage is not even possible anyways.

So, I needed to shrink the volume and add a new one. Between the steps, I tried again and again to use Disk Utility, but it only fucked up things more. So keep it closed and stay with diskutil.

In the end, I had to do something like the following. diskN is the physical disk where everything was located, and diskNsX is the newly created partition.

    diskutil list
    diskutil cs list
    
    diskutil unmountDisk diskN

Sometimes it seems to be possible to revert a Core Storage Volume, so you can go back to Disk Utility. However, this was not possible with my partition. So I continued like this:

    diskutil cs resizeStack LVUUID partsize
    sudo gpt -r show diskN

Then find the start sector of the newly freed space, substract 262144 (= 128MiB) from size (Apple required padding between partitions), and use these numbers for your new partition (yours will differ!):

    sudo gpt add -b 1700605768 -s 1698790088 -t windows diskN
    sudo newfs_exfat -v "Shared" /dev/rdiskNsX
    diskutil repairDisk diskN
    for all partitions: diskutil repairVolume diskNsX

And that’s it. Not as bad as it seemed.

