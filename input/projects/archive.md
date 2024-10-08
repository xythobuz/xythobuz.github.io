title: File Archive
description: Some files mirrored for archival purposes
parent: stuff
position: 1000
---

There is this trend of releasing binaries or small utility programs in Web-Forums or loading them onto one-click hosters.  Some years in the future, these forums or hosters probably won't exist anymore, while there is still a need for the software that was provided from there.

Here I'm mirroring/archiving stuff that could get lost.

* * *

* [Radio Wauland (WDR3, 20.12.2011)](files/2011-12-20_Radio_Wauland.mp3) ([more infos](https://netzpolitik.org/2011/radio-wauland-tune-in-turn-on-and-hack-yourself/))

* * *

#### Tomb Raider docs

Here’s some reverse-engineered documentation about the Tomb Raider games found in the depths of the web.

* [Tomb Raider Rosetta Stone](files/TRosettaStone.html)
* TR1 - TR5 file format listing (as [PDF](tr_docs/LevelFormats.pdf) or as [XLS](tr_docs/LevelFormats.xls))
* TR2 TombPC.dat script file format description as [PDF](tr_docs/TombPC_TR2.pdf)
* TRLE WAD file format description as [PDF](tr_docs/TR_WAD_file_format.pdf)
* TRAOD file format description as [HTML](tr_docs/TRAOD_Formats.html)

* * *

#### Leikkuri/Cutter v0.43

Simple utility to modify hardcoded TR4 font table. [Download](files/leikkuri_v043.rar) [Source](http://trep.trlevel.de/en/downloads.html)

* * *

#### XDumb 0.9.9 PS2 HDD utility for Mac OS X

Should work on PPC and Intel, starting from Mac OS X 10.3.9. [Download](files/xdumb.zip) [Source](http://www.theisozone.com/downloads/playstation/ps2-homebrew/xdumb---ps2-hdd-utility-for-mac-users/)

You will also need the corresponding server ELF (0.8.6) for your PS2. [Download](files/hdl dump 0.8.6_hdl_dumx-0.8.6.zip) [Source](http://www.4shared.com/get/bwAA4VN_/hdl_dump_086_hdl_dumx-086.html)

There are also these modified server ELFs, version u0.8.6 and 0.9.1 as well as 0.8.6 with a size fix (160GB HDDs). [Download](files/hdl_dumx_unofficial.zip) [Source](http://psx-scene.com/forums/f98/unofficial-hdld_svr-0-8-6-0-9-1-soft-reset-boot-elf-loading-59236/) [Source](http://psx-scene.com/forums/f98/hdld_svr-elf-w1zard-0f-0z-patched-48bit-lba-support-zer0-x-27874/)

* * *

#### GBDK 2.96 binaries for Mac OS X

Compiled for Snow Leopard, works on Mavericks. Not all examples are buildable. By ProGM. [Download](files/gbdk-2.96-mac.zip) [Source](http://gbdev.gg8.se/forums/viewtopic.php?pid=409#p409)

Be warned though: this release could have problems. One thing I've noticed: the font_min is broken, all 'u's look like 'k's. That's a simple fix, just open `gbdk/lib/small/asxxxx/gb/f_min.o` and change the '15' in line 19 and 23 to '1F'.

