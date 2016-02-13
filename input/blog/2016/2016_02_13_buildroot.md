title: Blog
post: iMX233-OLinuXino-Micro Buildroot Image
date: 2016-02-13
comments: true
flattr: true
github: https://github.com/xythobuz/camcorder-buildroot
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

For my FPV Groundstation, I was looking for a cheap way to record the analog video received. Unfortunately, I don’t have much space left in this box, so I thought of the Raspberry Pi Zero. Too bad that it is not available anywhere in the world, only two shops in Europe are receiving shipments every two weeks that are sold-out immediately.

So I went looking for an alternative, and found the [iMX233-OlinuXino-Nano](https://www.olimex.com/Products/OLinuXino/iMX233/iMX233-OLinuXino-NANO/open-source-hardware). Taking a closer look at this series, there’s also the [iMX233-OLinuXino-Micro](https://www.olimex.com/Products/OLinuXino/iMX233/iMX233-OLinuXino-MICRO/open-source-hardware) that has a TV-Out, which would allow me to view a status message about the recording on my Groundstation-Display.

Basically, [Olimex admits that they have no idea how this TV Out stuff works](https://www.olimex.com/forum/index.php?topic=23.msg59#msg59). Thanks a lot!

Turns out, there was [a buggy driver available for 2.6.x Linux Kernels](https://github.com/xobs/linux-2.6.28.mx233-falconwing/blob/master/arch/arm/mach-stmp3xxx/tvenc.c), but not for the current mainline.

Even better, my idea was to record the video from a [cheap USB Video Grabber](http://linuxtv.org/wiki/index.php/Easycap). It works, but the 500MHz CPU of the OLinuXino seems to be too slow to keep up with even recording this datastream (not transcoding!).

## Booting with SDHC cards

Buildroot supports the OLinuXino out-of-the-box, but is using the Freescale-Provided MXS-Bootlets as Bootloader. Unfortunately, this thing was not able to read the SDHC card it was stored on, even though it already ran. But it turns out, current U-Boot supports this Platform without using the MXS-Bootlets as Stage1. I [followed this tutorial](https://www.eewiki.net/display/linuxonarm/iMX233-OLinuXino) to get U-Boot working.

## Result

You can get the results [from GitHub](https://github.com/xythobuz/camcorder-buildroot) or [my Server](http://xythobuz.de/git/camcorder-buildroot/). Follow the instructions in the README.md to create your own Image using the current 4.4.x mainline Linux Kernel and flash it.

<div class="yoxview">
    <a href="img/olinuxino.jpg" class="thumbnail">
        <img src="img/olinuxino_small.jpg" alt="Photo" title="Photo of OLinuXino Setup">
    </a>
</div>

## Bootlog

<pre>
HTLCLC

U-Boot 2016.01 (Feb 12 2016 - 14:14:51 +0100)

CPU:   Freescale i.MX23 rev1.4 at 454 MHz
BOOT:  SSP SD/MMC #0
DRAM:  64 MiB
MMC:   MXS MMC: 0
*** Warning - bad CRC, using default environment

In:    serial
Out:   serial
Err:   serial
Net:   Net Initialization Skipped
No ethernet found.
Hit any key to stop autoboot:  0
switch to partitions #0, OK
mmc0 is current device
SD/MMC found on device 0
Checking for: /boot/uEnv.txt ...
19 bytes read in 94 ms (0 Bytes/s)
Loaded environment from /boot/uEnv.txt
Checking if uname_r is set in /boot/uEnv.txt...
loading /boot/vmlinuz-olinuxino ...
3581468 bytes read in 1246 ms (2.7 MiB/s)

unable to find imx23-olinuxino.dtb ...
booting legacy ...
debug: [console=ttyAMA0,115200 root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait fixrtc] ...
debug: [bootz 0x42000000] ...
Kernel image @ 0x42000000 [ 0x000000 - 0x367ec8 ]

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 4.4.1 (thomas@debian-vm) (gcc version 4.9.3 (Buildroot 2016.02-rc1) ) #1 Fri Feb 12 23:47:24 CET 2016
[    0.000000] CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=0005317f
[    0.000000] CPU: VIVT data cache, VIVT instruction cache
[    0.000000] Machine model: i.MX23 Olinuxino Low Cost Board
[    0.000000] Memory policy: Data cache writeback
[    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 16256
[    0.000000] Kernel command line: console=ttyAMA0,115200 root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait fixrtc
[    0.000000] PID hash table entries: 256 (order: -2, 1024 bytes)
[    0.000000] Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
[    0.000000] Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
[    0.000000] Memory: 57812K/65536K available (4904K kernel code, 163K rwdata, 1576K rodata, 172K init, 219K bss, 7724K reserved, 0K cma-reserved)
[    0.000000] Virtual kernel memory layout:
[    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
[    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
[    0.000000]     vmalloc : 0xc4800000 - 0xff800000   ( 944 MB)
[    0.000000]     lowmem  : 0xc0000000 - 0xc4000000   (  64 MB)
[    0.000000]     modules : 0xbf000000 - 0xc0000000   (  16 MB)
[    0.000000]       .text : 0xc0008000 - 0xc065c7d4   (6482 kB)
[    0.000000]       .init : 0xc065d000 - 0xc0688000   ( 172 kB)
[    0.000000]       .data : 0xc0688000 - 0xc06b0f00   ( 164 kB)
[    0.000000]        .bss : 0xc06b0f00 - 0xc06e7e78   ( 220 kB)
[    0.000000] SLUB: HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
[    0.000000] NR_IRQS:16 nr_irqs:16 16
[    0.000000] clocksource: mxs_timer: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 911346093 ns
[    0.000000] sched_clock: 32 bits at 100 Hz, resolution 10000000ns, wraps every 21474836475000000ns
[    0.000000] Console: colour dummy device 80x30
[    0.070000] Calibrating delay loop... 227.32 BogoMIPS (lpj=1136640)
[    0.080000] pid_max: default: 32768 minimum: 301
[    0.080000] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.080000] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
[    0.080000] CPU: Testing write buffer coherency: ok
[    0.080000] Setting up static identity map for 0x40008400 - 0x40008458
[    0.080000] devtmpfs: initialized
[    0.100000] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.100000] pinctrl core: initialized pinctrl subsystem
[    0.100000] NET: Registered protocol family 16
[    0.100000] DMA: preallocated 256 KiB pool for atomic coherent allocations
[    0.130000] Serial: AMBA PL011 UART driver
[    0.140000] 80070000.serial: ttyAMA0 at MMIO 0x80070000 (irq = 17, base_baud = 0) is a PL011 rev2
[    0.290000] console [ttyAMA0] enabled
[    0.320000] mxs-dma 80004000.dma-apbh: initialized
[    0.330000] mxs-dma 80024000.dma-apbx: initialized
[    0.340000] SCSI subsystem initialized
[    0.340000] usbcore: registered new interface driver usbfs
[    0.350000] usbcore: registered new interface driver hub
[    0.350000] usbcore: registered new device driver usb
[    0.360000] Linux video capture interface: v2.00
[    0.360000] pps_core: LinuxPPS API ver. 1 registered
[    0.370000] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.370000] PTP clock support registered
[    0.380000] Advanced Linux Sound Architecture Driver Initialized.
[    0.390000] clocksource: Switched to clocksource mxs_timer
[    0.440000] NET: Registered protocol family 2
[    0.450000] TCP established hash table entries: 1024 (order: 0, 4096 bytes)
[    0.460000] TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
[    0.460000] TCP: Hash tables configured (established 1024 bind 1024)
[    0.470000] UDP hash table entries: 256 (order: 0, 4096 bytes)
[    0.480000] UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
[    0.480000] NET: Registered protocol family 1
[    0.490000] futex hash table entries: 256 (order: -1, 3072 bytes)
[    0.550000] jitterentropy: Initialization failed with host not compliant with requirements: 2
[    0.570000] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 249)
[    0.570000] io scheduler noop registered
[    0.580000] io scheduler deadline registered
[    0.580000] io scheduler cfq registered (default)
[    0.590000] 8006c000.serial: ttyAPP0 at MMIO 0x8006c000 (irq = 147, base_baud = 1500000) is a 8006c000.serial
[    0.600000] mxs-auart 8006c000.serial: Found APPUART 3.0.0
[    0.610000] [drm] Initialized drm 1.1.0 20060810
[    0.620000] usbcore: registered new interface driver asix
[    0.620000] usbcore: registered new interface driver ax88179_178a
[    0.630000] usbcore: registered new interface driver cdc_ether
[    0.640000] usbcore: registered new interface driver smsc95xx
[    0.640000] usbcore: registered new interface driver net1080
[    0.650000] usbcore: registered new interface driver cdc_subset
[    0.660000] usbcore: registered new interface driver zaurus
[    0.660000] usbcore: registered new interface driver cdc_ncm
[    0.670000] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.670000] usbcore: registered new interface driver usb-storage
[    0.690000] ci_hdrc ci_hdrc.0: EHCI Host Controller
[    0.690000] ci_hdrc ci_hdrc.0: new USB bus registered, assigned bus number 1
[    0.720000] ci_hdrc ci_hdrc.0: USB 2.0 started, EHCI 1.00
[    0.720000] hub 1-0:1.0: USB hub found
[    0.730000] hub 1-0:1.0: 1 port detected
[    0.740000] mousedev: PS/2 mouse device common for all mice
[    0.750000] stmp3xxx-rtc 8005c000.rtc: rtc core: registered 8005c000.rtc as rtc0
[    0.750000] i2c /dev entries driver
[    0.760000] usbcore: registered new interface driver usbtv
[    0.770000] stmp3xxx_rtc_wdt stmp3xxx_rtc_wdt: initialized watchdog with heartbeat 19s
[    0.780000] 80010000.ssp supply vmmc not found, using dummy regulator
[    0.820000] mxs-mmc 80010000.ssp: initialized
[    0.820000] ledtrig-cpu: registered to indicate activity on CPUs
[    0.840000] mxs-dcp 80028000.dcp: Failed to register sha1 hash!
[    0.840000] mxs-dcp: probe of 80028000.dcp failed with error -22
[    0.860000] usbcore: registered new interface driver usbhid
[    0.860000] usbhid: USB HID core driver
[    0.870000] mmc0: host does not support reading read-only switch, assuming write-enable
[    0.890000] mmc0: new high speed SDHC card at address 59b4
[    0.890000] mmcblk0: mmc0:59b4 USD   30.0 GiB
[    0.900000] NET: Registered protocol family 10
[    0.910000]  mmcblk0: p1 p2
[    0.920000] sit: IPv6 over IPv4 tunneling driver
[    0.930000] NET: Registered protocol family 17
[    0.940000] stmp3xxx-rtc 8005c000.rtc: setting system clock to 1970-01-01 00:00:06 UTC (6)
[    0.950000] ALSA device list:
[    0.960000]   No soundcards found.
[    0.960000] uart-pl011 80070000.serial: no DMA platform data
[    1.000000] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    1.010000] VFS: Mounted root (ext4 filesystem) readonly on device 179:2.
[    1.020000] devtmpfs: mounted
[    1.030000] Freeing unused kernel memory: 172K (c065d000 - c0688000)
[    1.190000] EXT4-fs (mmcblk0p2): re-mounted. Opts: data=ordered
Starting logging: OK
Starting mdev...
Initializing random number generator... [    2.190000] random: dd urandom read with 6 bits of entropy available
done.
Starting network...

Welcome to the CamCorder
olinuxino login:
</pre>

