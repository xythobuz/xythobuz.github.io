title: Duality
description: Game Boy Color game based on a GTA:SA Arcade machine
parent: projects
git: https://codeberg.org/xythobuz/Duality
github: https://github.com/xythobuz/Duality
date: 2025-08-19
update: 2025-09-01
comments: true
favicon: https://xythobuz.github.io/Duality/favicon.png
auto_toc: true
no_gen_ai: true
additional_css: css/duality.min.css
additional_js: js/duality.min.js emu_js/loader.js
---

## Introduction

I regularly watch the livestreams of fulltime GTA:SA speedrunner [Joshimuz](https://www.twitch.tv/joshimuz/).
A while ago he did a [PS2 Retro Achievements run](https://www.youtube.com/playlist?list=PLv1eoin737hDEcLhbiLIccTPr9qQEaXU9).
As part of these he has to get a Top 5 score in the in-game arcade machine Duality in both the black and white highscore table.
In [Part 10 at 04:02:16](https://youtu.be/PIAo_3YPYO8?t=14536), when Josh starts playing Duality, chat user `Caffie_` mentions how this could be a Game Boy game.
So this inspired me to try to port the game to the Game Boy Color.
Here are the results.

You can either [download the ROM](https://xythobuz.github.io/Duality/duality.gb) or try it out right here, if you have JavaScript enabled, thanks to [EmulatorJS](https://emulatorjs.org/).

<div id="duality_wrap" class="border">
    <div id="duality_game"></div>
    <noscript>Enable JavaScript to play the game right here in your browser.</noscript>
</div>

On PCs use keyboard input with the keys given below. On mobile devices a touch overlay should automatically appear over the emulator.

<!--%
tableHelper([ "align-center monospaced", "align-center monospaced", "align-center" ],
    [ "Button", "Key", "Action" ], [
        [ "D-Pad Left", "Arrow Left", "Rotate Left" ],
        [ "D-Pad Right", "Arrow Right", "Rotate Right" ],
        [ "A", "S", "Accelerate" ],
        [ "B", "A", "Shoot" ],
        [ "Start", "Enter", "Play / Pause" ],
        [ "Select", "Space", "Config / About" ],
    ]
)
%-->

<p style="font-size: smaller; font-style: italic;">
Although you can use EmulatorJS I recommend a native emulator for your target device if you experience stuttering music or bad performance with the emulator on this page.
</p>

Alternatively here's a short gameplay video and some screenshots.

<!--%
lightgallery([
    [ "img/duality_gameplay.webm", "video/webm", "", "", "Gameplay screen recording" ],
])
%-->

<!--%
lightgallery([
    [ "img/duality_ss_menu.png", "Start screen" ],
    [ "img/duality_ss_shoot2.png", "Gameplay" ],
    [ "img/duality_ss_accel.png", "Accelerating" ],
    [ "img/duality_ss_over.png", "Scoring name entry screen" ],
])
%-->

<p></p>
<div class="collapse">Click for more screenshots.</div>
<div class="collapsecontent">
<!--%
lightgallery([
    [ "img/duality_ss_damage.png", "Damaged from black hole" ],
    [ "img/duality_ss_score.png", "Score list" ],
    [ "img/duality_ss_about.png", "About screen" ],
    [ "img/duality_ss_conf.png", "Configuration menu" ],
    [ "img/duality_ss_continue.png", "Continue screen" ],
    [ "img/duality_ss_shoot.png", "Shooting" ],
    [ "img/duality_ss_debug.png", "Debug menu" ],
    [ "img/duality_ss_thanks.png", "Acknowledgements screen" ],
])
%-->
</div>

### Quick Start Guide

Press `Left` or `Right` on the title screen to show either the black or white highscores.
Press `Select` to show the about screen and build info.
In-game press `Start` to pause and resume.
While paused press `Select` to return to the menu.

Collect small white spheres to get +5 white score.
Collect small black spheres to get +5 black score.
The opposite color will reduce your score when collected.
Shooting while you have a white score will reduce it by one.
Large black holes will attract you and damage your ship when touched.
Large white spheres will repel you and replenish your health when touched.
Accelerating will reduce your fuel, which will recharge when not accelerating.
You can shoot large spheres for +10 points.

For a more detailed description of the original game check out the [Duality article on GTA Wiki](https://gta.fandom.com/wiki/Duality) 😛

### Links

The code is of course [freely available](https://codeberg.org/xythobuz/Duality) under the GPL license.
Also check out the automatically generated [project website](https://xythobuz.github.io/Duality) on GitHub Pages.

<!--%
lightgallery([
    [ "https://xythobuz.github.io/Duality/cartridge.png", "cartridge artwork" ],
    [ "img/duality_cart_1.jpg", "flash carts (top)" ],
    [ "img/duality_cart_2.jpg", "flash carts (side)" ],
])
%-->

## Toolchain

Fortunately the Game Boy is probably one of the retro hardware platforms with the best community-created documentation.
The most important piece from this community is [Pan Docs](https://gbdev.io/pandocs/), a living document that has been extended and revised over the years that basically _is_ the reference manual for the platform.

I wrote the whole game in C, which is very easy thanks to the [GBDK-2020](https://github.com/gbdk-2020/gbdk-2020/).
It uses SDCC as the compiler with some custom tools to link the final ROM file.
Additionally it also includes a tool that can convert graphics to the proper hardware sprite tile and map format.
The GBDK also comes with [good documentation](https://gbdk.org/docs/api/) and lots of [examples](https://github.com/gbdk-2020/gbdk-2020/tree/develop/gbdk-lib/examples) that really make it easy to get started.

Over the course of the project my `Makefile` grew relatively big and customized.
Of course I've added the usual stuff like dependency file generation and git version information.
I'm also automatically generating the graphics data with the `png2asset` tool.
To convert sound samples I've modified the `cvtsample.py` tool from the GBDK examples.
And to pre-calculate some speed vector tables for different angles I wrote my own `gen_angles.py` script.

To find out how to convert the graphics assets I'm encoding the mode in the filename of the input images.

<!--%
include_sourcecode_slice(
    "makefile", (146, 168), "Makefile", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

Like with the documentation, the emulation ecosystem for the Game Boy is also very healthy.

  * I've mostly been using [Gearboy](https://github.com/drhelius/Gearboy) which includes some nice visualization tools for the hardware state.
  * To test the Super Game Boy borders I used [SameBoy](https://sameboy.github.io/).
  * A very nice symbolic C debbuger integration is available in [Emulicious](https://emulicious.net/).
  * [GBE+](https://github.com/shonumi/gbe-plus) can also emulate a Game Boy Printer.
  * [NO$GMB](https://problemkaputt.de/gmb.htm) is able to emulate multiple linked Game Boy systems.
  * While testing debugging I also played around with [BGB](https://bgb.bircd.org/) for a bit.
  * And for one especially hard debugging session I used the reverse-time-step feature of [GameRoy](https://github.com/Rodrigodd/gameroy) with good success (to actually see the faulty jump to the wrong bank after it happened).

The Windows-only emulators all ran fine using Wine.

I described the Emulicious debugger integration to Kate (or VSCode I guess) in more detail [in the README](https://codeberg.org/xythobuz/Duality#ide-integration).

## Software

The game is really made for the Game Boy Color (GBC).
On the monochrome Game Boy (DMG) and the Super Game Boy (SGB) it runs at half-speed and the black and white spheres are hard to differentiate.
Or, to put it another way, I was not able to optimize the code enough that it run's at the DMG clock speed of ~1MHz.
So I had to cheat by putting the GBC CPU into a double-clock mode.

<!--%
include_sourcecode_slice(
    "c", (646, 649), "src/main.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

To get some randomness into the gameplay I'm initially showing a splash screen after reset, where the user has to press `Start`.
The timing of this button-press is used to initialize a random number generator that's later used to determine spawning positions of objects in the world map.

<!--%
include_sourcecode_slice(
    "c", (662, 676), "src/main.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

The splash screen in `main.c` also handles the configuration and debug menus (try the Konami code).

The main game loop in `game.c` is pretty straight-forward, like with most game engines.
It basically does the following things:

  1. read key inputs from user
  2. modify player and world state (according to input and time)
  3. draw the output graphics

The world state is kept track of in `obj.c`, where each shot and colored sphere is represented as an entry in an object list.

Background music is played automatically on the pulse channels (1 and 2), as well as the noise channel (4).
Only the sample channel (3) is used for sound effects like shots or explosions.
Both of these are handled by interrupts, so they should never stutter or crackle (instead gameplay slows down).
For timekeeping I'm also configuring the internal timer and handle all of these tasks in the same ISR.

<!--%
include_sourcecode_slice(
    "c", (29, 33), "src/timer.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

One pattern I've used repeatedly is storing (`const`) lists of "things" in ROM to be able to use them easily in other places.
This is used for sprites, background maps, sound samples and music.
For example, this is the start of the list of sprite graphics.

<!--%
include_sourcecode_slice(
    "c", (56, 79), "src/sprite_data.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

By then calling the sprite functions the correct data is automatically loaded into VRAM and used accordingly.
The sprite and map lists are not `const` because the offsets are calculated dynamically when loaded.
The music and sample lists are both `const` though.

<!--%
include_sourcecode_slice(
    "c", (73, 76), "src/sprites.h", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

It's not possible to rotate sprites by arbitrary angles, only the X and Y axis can be flipped individually.
So for each desired rotation a sprite has to be prepared manually.

I decided to split the circle into 16 different angles, or 22.5 degree steps.
When taking advantage of the tile flipping we can get away with five different sprite rotations, from 0 degrees to 90 degrees.

<!--%
lightgallery([
    [ "img/rockshp_spr24.png", "ship spritesheet" ],
])
%-->

To get the proper movement and shot velocity vectors for the current angle I'm also pre-calculating these tables.

<pre class="sh_c" data-skip=1>
const int8_t table_speed_move[table_speed_move_SIZE] = {
    0, 23, // 0.0
    9, 21, // 22.5
    16, 16, // 45.0
    21, 9, // 67.5
    23, 0, // 90.0
    21, -9, // 112.5
    16, -16, // 135.0
    9, -21, // 157.5
    0, -23, // 180.0
    -9, -21, // 202.5
    -16, -16, // 225.0
    -21, -9, // 247.5
    -23, 0, // 270.0
    -21, 9, // 292.5
    -16, 16, // 315.0
    -9, 21, // 337.5
};
</pre>

### Graphics

To easily visualize the data in VRAM here are some screenshots from [Gearboy](https://github.com/drhelius/Gearboy).

There's not enough space to fit all graphics data at once, so I'm loading different subsets in the menu and in-game.

<!--%
lightgallery([
    [ "img/duality_vram_3.png", "menu sprites" ],
    [ "img/duality_vram_2.png", "menu tile data" ],
    [ "img/duality_vram_1.png", "menu background map" ],
    [ "img/duality_vram_4.png", "menu palettes" ],
])
%-->

  1. The first image shows the sprite objects in OAM. These are instances of tiles from the tile data.
  2. Tile data is shown in the upper left part of the second image.
     The middle and lower left parts of the second image contain the tile data for the background maps and window.
     The right half of the second image shows a second bank only available on GBC, which I use for a smaller font.
  3. The third image shows the background map, a large map of tiles that can be scrolled easily.
  4. The fourth image shows the palettes to colorize the tiles on GBC hardware.

<!--%
lightgallery([
    [ "img/duality_vram_7.png", "in-game sprites" ],
    [ "img/duality_vram_6.png", "in-game tile data" ],
    [ "img/duality_vram_5.png", "in-game background map" ],
    [ "img/duality_vram_8.png", "in-game palettes" ],
])
%-->

You can only store a maximum of 40 tile instances in [OAM](https://gbdev.io/pandocs/OAM.html) at once, but there are [more complicated rules](https://gbdev.io/pandocs/OAM.html#object-priority-and-conflicts) on when they appear.
To colorize tiles the GBC adds a palette index to the attributes.

The background map works similar to the OAM in that it indexes the background tile map, but the positions are fixed and [the GBC has attributes](https://gbdev.io/pandocs/Tile_Maps.html#bg-map-attributes-cgb-mode-only) for the map that don't exist on DMG.

### Sound

The background music is simply stored as long lists of notes.
Here are some example excerpts from the score-screen music.

<!--%
include_sourcecode_slice(
    "c", [
        (26, 42),
        (105, 131),
        (159, 177),
        (191, 204),
    ], "src/sound_over.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

`over_notes` and `over_notes2` are the frequencies for the two pulse channels.
`over_drums` has the IDs of different pre-defined settings for the noise channel.

The `snd_play()` function in `sound.c` is then walking through this list after the note duration has elapsed, filling the sound hardware registers as needed.

<!--%
include_sourcecode_slice(
    "c", (37, 219), "src/sound.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

For the sound effect sample player I've transcribed the assembly ISR from the GBDK examples to C, which was a fun little exercise in SM83 assembly.

<!--%
include_sourcecode_slice(
    "c", (88, 184), "src/sample.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

### Banking

Probably the most important topic in Game Boy software development is memory banking.
Take a look at the memory map of the system.

<!--%
tableHelper([ "align-center monospaced", "align-center monospaced", "align-left"],
    [ "Start", "End", "Description" ], [
        [ "0x0000", "0x3FFF", "16 KiB ROM bank 00", "style='font-size: larger; font-weight: bold; line-height: 4lh'" ],
        [ "0x4000", "0x7FFF", "16 KiB ROM Bank 01 – NN", "style='font-size: larger; font-weight: bold; line-height: 4lh'" ],
        [ "0x8000", "0x9FFF", "8 KiB Video RAM (VRAM)", "style='line-height: 2lh'" ],
        [ "0xA000", "0xBFFF", "8 KiB External RAM (SRAM)", "style='font-size: larger; font-weight: bold; line-height: 2lh'" ],
        [ "0xC000", "0xCFFF", "4 KiB Work RAM (WRAM)", "style='line-height: 1lh'" ],
        [ "0xD000", "0xDFFF", "4 KiB Work RAM (WRAM)", "style='line-height: 1lh'" ],
        [ "0xE000", "0xFDFF", "Echo RAM (mirrors WRAM)", "style='line-height: 2lh'" ],
        [ "0xFE00", "0xFE9F", "Object attribute memory (OAM)", "style='font-size: smaller'" ],
        [ "0xFEA0", "0xFEFF", "Not Usable", "style='font-size: small'" ],
        [ "0xFF00", "0xFF7F", "I/O Registers", "style='font-size: smaller'" ],
        [ "0xFF80", "0xFFFE", "High RAM (HRAM)", "style='font-size: smaller'" ],
        [ "0xFFFF", "0xFFFF", "Interrupt Enable register (IE)", "style='font-size: x-small'" ],
    ]
)
%-->

Only the 32KiB ROM bank areas at `0x0000 - 0x7FFF` and the 8KiB RAM at `0xA000 - 0xBFFF` are coming from the cartridge.
The cartridge RAM is usually used to store persistent savegames and configs on a battery backed SRAM.
The code and data live in the first 32KiB.

Of course for many games these 32KiB are not enough, so they use some special hardware in the cartridge to map different memory chips to the same address range, depending on a configuration register.
This is accomplished by Nintendos [Memory Bank Controllers](https://gbdev.io/pandocs/MBCs.html), most commonly (and for this game) the [MBC5](https://gbdev.io/pandocs/MBC5.html).

Each bank has a size of 16KiB, with the first bank (0) always mapped to the first 16KiB of the address space.
The next half of the ROM area is for the switchable bank, which can be selected by writing to the MBC-internal registers.

Fortunately GBDK already contains a bunch of helper functions that make this all a bit easier.
For the ROM banks we have to differentiate the following cases.

  1. const data in a bank
  2. functions in bank 0 (non-banked)
  3. non-static functions in a bank
  4. static functions (in a bank)

Also note that with the GBDK and SDCC every compilation unit (so each `.c` file) can only be part of one bank.
Which unit goes into which bank can be decided automatically (autobanking).

First enable autobanking by passing the proper compiler flag `-Wm-yoA`.
Now, at the start of each `.c` and `.h` files, declare a reference to the bank of this compilation unit.

<pre class="sh_c" data-skip=1>
/* in some_name.c */
BANKREF(some_name)

/* in some_name.h */
BANKREF_EXTERN(some_name)
</pre>

Of course each unit needs a unique `some_name` (does not need to be the filename).

Now you can declare your non-static functions with an attribute to place them in the correct bank.

<pre class="sh_c" data-skip=1>
void foo(void) BANKED;
void bar(void) NONBANKED;
</pre>

When you call a `BANKED` function a trampoline in bank 0 automatically takes care of proper bank switching for you.
Only when calling static functions not marked as `BANKED` (case 4 from above) you need to make sure you're either already in the correct bank (by coming from a `BANKED` function from the same compilation unit), or to switch banks manually (when coming from a `NONBANKED` function).

To easily bank-switch I made some small helper macros.

<!--%
include_sourcecode_slice(
    "c", (25, 27), "src/banks.h", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

`const` data has the same restrictions, so when you need to read `const` data from one bank in a function from another compilation unit you may need to add a small `NONBANKED` helper function.

<!--%
include_sourcecode_slice(
    "c", (209, 215), "src/window.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

Of course you can never directly switch banks inside a function that is not `NONBANKED` as this would replace the currently executed opcodes.

Initially I started out with lots of functions marked as `NONBANKED`, but this turned out to be unnecessary.
By properly modularizing your code and liberally using `BANKED` you can get the compiler to do most of the work for you.

It's also relatively easy to spot banking errors.
Most of the time the VRAM will quickly fill with some regular pattern, like horizontal or vertical lines.
Or a debugger shows you suddenly in the middle of nowhere.
But I also had some devious cases, where the control flow jumped into some legitimate code that caused strange effects (wrong sound effects, no objects appearing, but the game still ran).
These took me a while to figure out, until I noticed a `return` that skipped the final `END_ROM_BANK` of a function, thereby forgetting to switch-back the bank.

RAM banks, in comparison, can be handled more easily.
I'm simply enabling and setting RAM bank 0 at the beginning, before reading the config from there, and always keep it enabled while the game is running.

<!--%
include_sourcecode_slice(
    "c", (51, 72), "src/config.ba0.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

Similar to the `png2asset` calls the RAM bank of a compilation unit is specified in the filename (`foo.baN.c` where N is the RAM bank number).

<!--%
include_sourcecode_slice(
    "makefile", (170, 174), "Makefile", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

This is what the memory usage for my game looks like at the moment.

    Bank         Range                Size     Used  Used%     Free  Free% 
    --------     ----------------  -------  -------  -----  -------  -----
    ROM_0        0x0000 -> 0x3FFF    16384    10466    64%     5918    36%
    ROM_1        0x4000 -> 0x7FFF    16384    16383   100%        1     0%
    ROM_2        0x4000 -> 0x7FFF    16384    16377   100%        7     0%
    ROM_3        0x4000 -> 0x7FFF    16384    16383   100%        1     0%
    ROM_4        0x4000 -> 0x7FFF    16384     5903    36%    10481    64%
    SRAM_0       0xA000 -> 0xBFFF     8192      427     5%     7765    95%
    WRAM_LO      0xC000 -> 0xCFFF     4096     1650    40%     2446    60%

So I'm using five ROM banks in total for code and data (which has to be rounded up to eight banks, or 128KiB, as cartridges only can [speficy ROM bank counts](https://gbdev.io/pandocs/The_Cartridge_Header.html#0148--rom-size) that are a power of two).
And a single SRAM bank (8KiB) for persistent highscores, configs and a savegame, which is the smallest number of [SRAM banks possible](https://gbdev.io/pandocs/The_Cartridge_Header.html#0149--ram-size).
Take care not to fill ROM bank 0 [too close to the limit](https://gbdk.org/docs/api/docs_faq.html#faq_bank_overflow_errors), as the ROM header is not always properly taken into account in all tools.

### Game Boy Printer

The GBDK already comes with a [Game Boy Printer example](https://github.com/gbdk-2020/gbdk-2020/tree/develop/gbdk-lib/examples/gb/gbprinter) which I cleaned up and modified.
Instead of reading a converted image I'm directly getting the tile data from VRAM to print either the window or background map.
The data is read in blocks of two tile rows which are blacked out after transmission as a progress indicator.

<!--%
include_sourcecode_slice(
    "c", (176, 249), "src/gbprinter.c", [
        "https://raw.githubusercontent.com/xythobuz/Duality/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
        "https://codeberg.org/xythobuz/Duality/raw/commit/4315e0f8c17c29cfeb3be8a3eda745ff6a51b450/",
])
%-->

Here is a screencast of printing in the [GBE+](https://github.com/shonumi/gbe-plus) emulator and a copy of the results.

<!--%
lightgallery([
    [ "img/duality_print_anim.webm", "video/webm", "", "", "print screen animation" ],
    [ "img/duality_score_print.png", "digital score printout" ],
])
%-->

And this is a recording of my actual old childhood GB Printer in action.

<!--%
lightgallery([
    [ "img/duality_print_video.webm", "video/webm", "", "", "printing process" ],
    [ "img/duality_score_print.jpg", "physical score printout" ],
])
%-->

## Physical Cartridges

To build physical cartridges I ordered two [flashcarts](https://de.aliexpress.com/item/1005008596849158.html) as well as [cartridge cases](https://de.aliexpress.com/item/1005006340286928.html) in black and white.

Unfortunately the flash carts use FRAM and a custom CPLD implementation to replace the mapper chip.
It seems the timings or voltages or some other electrical or physical parameters are not quite correct.
I can't get them to work in the [GB Interceptor](https://github.com/Staacks/gbinterceptor) for example.
But in my real DMG and GBC they work fine.

I'm using [this clone writer](https://de.aliexpress.com/item/1005007652321830.html), although I wouldn't really recommend it.
It's very slow and can't be updated, probably due to being a chinese clone.
Also the ["upstream repo"](https://github.com/simonkwng/GBFlash) is completely empty.
Unfortunately all other writers supported by [FlashGBX](https://github.com/lesserkuma/FlashGBX) are not really free hardware or software either.

To write to the carts I'm using the `DIY cart with MX29LV640 @ WR` setting of FlashGBX.

I ordered three pieces of the label printed on foil, with the rounded corners cut out, at [Klebefisch](https://www.klebefisch.de/eigenes-motiv/aufkleber-drucken), for 30€ including postage, or about 10€ per label.
The parameters were:

  * White foil
  * Cut outline
  * Not mirrored
  * 42mm by 37mm
  * 1.5mm corner radius

The size and finish of the sticker are great, but unfortunately the print quality is pretty bad with a low resolution (even though I sent high-res files with 2100px x 1850px).

<!--%
lightgallery([
    [ "img/duality_cart_3.jpg", "printed cartridge label" ],
])
%-->

But still the finished cartridges look and feel great!
It's nice to have something physical in hand instead of "just" software.

The cost for these came out to around 15€ per piece from AliExpress, excluding the label and working hours.
There are other manufacturers of new carts for homebrew games, like [insideGadgets](https://shop.insidegadgets.com/product/custom-gameboy-flash-cart/), but surprisingly they are not really much cheaper, even for larger production runs.

It's also possible to manufacture your own cartridge PCBs, but there are some caveats with this.
The main problem is the memory bank controller, in my case the most common `MBC5` from Nintendo.
They are no longer manufactured and can not be sourced new, so you either have to salvage them from original old donor games (which hurts the archivist in me too much) or find some kind of replacement.

Different people came up with implementations based on CPLDs or microcontrollers.
Some of them are even open-source, like the [MBC5 CPLD code from insideGadgets](https://github.com/insidegadgets/Gameboy-MBC5-MBC1-Hybrid) or [Allison's Bootleg Cart](https://abc.decontextualize.com/).
In a [modern design](https://github.com/sillyhatday/GAMEBOY-CPLD-FRAM-2MB) you can use this with an FRAM chip to avoid the need for a backup battery for savegames, although this comes with some timing incompatibilities that may give problems with some games.
You can also [use a design](https://github.com/sillyhatday/GAMEBOY-CPLD-SRAM-2MB) with an SRAM and a coin cell.
Many different flash chips are compatible in theory, though you need to make sure it can handle 5V or add voltage translation circuitry.

Unfortunately, doing some back-of-the-envelope cost calculation, this all comes out as more expensive for small production runs.
It's cheaper and faster to just buy the chinese flash carts.

But to be honest, I'm not sure how much interest people would have in buying physical copies of this game anyway, so I shelved this idea for now.
Of course you can always easily make your own if you'd like.

## Asset Recreation

In order to get some inspiration from the original versions I extracted the relevant assets from the GTA:SA game files, like sprites, backgrounds, sound effects and music.
I then re-created these in scaled-down versions that fit the Game Boy hardware.

Extrating the audio files can be done with [Alci's SAAT GUI FrontEnd](https://www.gtagarage.com/mods/show.php?id=5777).
The graphics can be extracted from `.txd` files with the [TXD Workshop](https://www.gtagarage.com/mods/show.php?id=8320).
Both of these run fine in Wine.

For the menu music I've re-created the San Andreas Theme, the game-over screen uses the victory fanfare from Final Fantasy VII.
Fortunately both of these have spread very widely and there's lots of MIDI interpretations available.
I used [MuseScore](https://musescore.org/en) to convert these MIDI files to sheet music and then transcribed the notes into my note lists in the source code.

The Duality in-game theme song was more difficult.
It consists more of noises and some LFOs instead of clearly defined notes, so transcribing was pretty hard.
In the end I used a trial version of [AnthemScore](https://www.lunaverus.com/) in Wine to get an approximate idea of the notes, but the result is not great.

Here are some direct comparisons.
First the San Andreas Theme, used as menu music.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=7qfbi3HACV8", "San Andreas Theme" ],
    [ "img/duality_music_menu.opus", "audio/ogg", "", "Duality Menu Music" ],
])
%-->

Next the score screen music, which comes from the FF7 victory fanfare.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=rgUksX6eM0Y", "Final Fantasy VII Victory Fanfare" ],
    [ "img/duality_music_score.opus", "audio/ogg", "", "Duality Score Music" ],
])
%-->

And the in-game music, from the original Duality.

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=duiUhk5ZkaA", "Duality Theme" ],
    [ "img/duality_music_game.opus", "audio/ogg", "", "Duality Gameplay Music" ],
])
%-->

## Summary

I started working on this project at the end of May 2025, and basically finished it (to the state described here) at the end of July 2025, so in a span of about two months.
Of course this was only a side-project in my free time, outside my real job that pays the bills.
For this relatively short time I'm pretty happy with the results.

As always there is still lots of room for improvements.

The code needs to be optimized so it runs full-speed on the DMG, maybe by improving object handling and rendering, which has some 𝒪(𝓃²) behavior.

I also started working on a multiplayer mode, but due to me only having a single GBC and DMG to test each, I didn't really progress much there.

And the background map scrolling could be improved.
I played around with mirroring the map when overflowing on the sides, like some kind of endless scrolling, but haven't gotten far unfortunately.

Working on a well-documented and well-designed retro game system like this was really lots of fun.
In the future I hope to also take a closer look at other retro platforms.

## License

[The Duality source code](https://codeberg.org/xythobuz/Duality) is licensed under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html).

    Copyright (C) 2025 Thomas Buck <thomas@xythobuz.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    See <http://www.gnu.org/licenses/>.

Duality uses the [GBDK-2020](https://gbdk.org) libraries and is based on their example code.
The files `sgb_border.c` and `sgb_border.h` are copied directly from their `sgb_border` example.

The `util/cvtsample.py` script is based on a [GBDK example](https://github.com/gbdk-2020/gbdk-2020/blob/develop/gbdk-lib/examples/gb/wav_sample/utils/cvtsample.py).

The [8x8 font](https://github.com/DavidDiPaola/font_vincent) is public domain.

The included cartridge label graphic in `artwork/cart_label.xcf` is based on the ['Cartridge-Label-Templates' by Dinierto](https://github.com/Dinierto/Cartridge-Label-Templates) licensed as CC0.

The included cartridge graphic in `artwork/cartridge.xcf` is based on the ['Front-End-Assets' by Duimon](https://github.com/Duimon/Front-End-Assets).
