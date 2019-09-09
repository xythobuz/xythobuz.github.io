title: Blog
post: Arch Linux Installation
date: 2019-09-09
comments: true
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

I've now been running Arch Linux on my Desktop for over a year.
After exclusively running Mac OS X for many years before, this was my first real step into a Desktop Linux distribution.
It has been surprisingly painless and I'm very happy with my machine.
Here are all the steps I've ran to install and setup Arch, with some explanations in between.

Of course, take a look at the [Arch Wiki installation guide](https://wiki.archlinux.org/index.php/installation_guide) before doing anything.

### Rotating the Virtual Console

At the time of installing Arch, the first monitor output of my machine was connected to a rotated display.
To be able to work properly, you may want to rotate the Linux virtual console.
This can be done by adding the argument `fbcon=rotate:1` to the kernel boot options.
When the system is booted, you can execute the following command.
Also check out the [kernel documentation](https://www.kernel.org/doc/Documentation/fb/fbcon.txt).

<pre class="sh_sh">
echo 1 > /sys/class/graphics/fbcon/rotate_all
</pre>

### Installation

Boot into the Arch Live USB stick environment.
After getting the time, format your harddisk (see [UEFI & GPT partitioning in Wiki](https://wiki.archlinux.org/index.php/Partitioning#UEFI.2FGPT_example_layout)) and mount the new partitions.

<pre class="sh_sh">
timedatectl set-ntp true
fdisk -l
fdisk /dev/nvme0n1
mkfs.ext4 /dev/nvme0n1p3
mkfs.ext4 /dev/nvme0n1p4
mkfs.fat -F32 /dev/nvme0n1p1
mkswap /dev/nvme0n1p2
swapon /dev/nvme0n1p2

mount /dev/nvme0n1p3 /mnt
mkdir /mnt/boot
mount /dev/nvme0n1p1 /mnt/boot
mkdir /mnt/home
mount /dev/nvme0n1p4 /mnt/home
</pre>

Generate the mirrorlist by speed (see [Mirrorlist in Wiki](https://wiki.archlinux.org/index.php/Mirrors#List_by_speed)).

<pre class="sh_sh">
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup
rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup | tee /etc/pacman.d/mirrorlist
</pre>

Bootstrap the new installation.

<pre class="sh_sh">
pacstrap /mnt base base-devel
genfstab -L /mnt >> /mnt/etc/fstab
arch-chroot /mnt
</pre>

Start setting up the machine (see [Locale in Wiki](https://wiki.archlinux.org/index.php/installation_guide#Locale)).

<pre class="sh_sh">
ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
hwclock --systohc
vi /etc/locale.gen
locale-gen
vi /etc/locale.conf
vi /etc/hostname
vi /etc/hosts
passwd
</pre>

Install some important stuff.

<pre class="sh_sh">
pacman -Syu sudo vim avahi nss-mdns zsh
vim /etc/nsswitch.conf
systemctl enable avahi-daemon.service
</pre>

Create your new user account.

<pre class="sh_sh">
useradd -m -G wheel /usr/bin/zsh thomas
chfn --full-name “Thomas Buck” thomas
passwd thomas
visudo
</pre>

Install systemd-boot and add boot entries (see [systemd-boot in Wiki](https://wiki.archlinux.org/index.php/Systemd-boot#Adding_boot_entries)).

<pre class="sh_sh">
bootctl --path=/boot install
cat /usr/share/systemd/bootctl/arch.conf > /boot/loader/entries/arch.conf
blkid /dev/nvme0n1p3 >> /boot/loader/entries/arch.conf
vim /boot/loader/entries/arch.conf
</pre>

Configure systemd-boot (also see [systemd-boot in Wiki](https://wiki.archlinux.org/index.php/Systemd-boot#Loader_configuration)).

<pre class="sh_sh">
vim /boot/loader/loader.conf
</pre>

Add Intel Microcode to systemd-boot (see [Microcode in Wiki](https://wiki.archlinux.org/index.php/Microcode#systemd-boot)).

<pre class="sh_sh">
pacman -Syu intel-ucode
vim /boot/loader/entries/arch.conf
</pre>

Configure automatic systemd-boot update (see [systemd-boot in Wiki](https://wiki.archlinux.org/index.php/Systemd-boot#Automatic_update)).

<pre class="sh_sh">
mkdir /etc/pacman.d/hooks
vim /etc/pacman.d/hooks/systemd-boot.hook
</pre>

Install NetworkManager (see [NetworkManager in Wiki](https://wiki.archlinux.org/index.php/NetworkManager)).

<pre class="sh_sh">
pacman -Syu networkmanager
systemctl enable NetworkManager
</pre>

<pre class="sh_sh">
vim /etc/systemd/timedsyncd.conf
timedatectl set-ntp true
</pre>

I'm using an nVidia graphics card.

<pre class="sh_sh">
pacman -Syu xorg-server
pacman -Syu nvidia opencl-nvidia

vim /etc/mkinitcpio.conf
vim /boot/loader/entries/arch.conf
# https://wiki.archlinux.org/index.php/NVIDIA#DRM_kernel_mode_setting

vim /etc/pacman.d/hooks/nvidia.hook
# https://wiki.archlinux.org/index.php/NVIDIA#Pacman_hook

mkinitcpio -P
</pre>

Start installing more stuff.

<pre class="sh_sh">
pacman -Syu sddm
systemctl enable sddm

systemctl enable nvidia-persistenced.service
systemctl start nvidia-persistenced.service

pacman -Syu pulseaudio pulseaudio-alsa pulseaudio-bluetooth pulseaudio-zeroconf
pacman -Syu plasma-meta vlc phonon-qt5-gstreamer phonon-qt5-vlc dolphin dolphin-plugins kdialog kfind ark yakuake
pacman -Syu nvidia-settings sddm-kcm
</pre>

All this has been done in the (chrooted) environment of the Live USB stick until now.
Now we reboot into the new installation.

<pre class="sh_sh">
exit
umount -R /mnt
reboot
</pre>

Installing Synergy so I can comfortably continue writing these commands while in the new installation (see [Synergy in Wiki](https://wiki.archlinux.org/index.php/Synergy#Installation)).

<pre class="sh_sh">
pacman -Syu synergy
cp /etc/synergy.conf.example /etc/synergy.conf
vim /etc/synergy.conf
systemctl --user enable --now synergys.service
</pre>

Of course I need an AVR and Arduino toolchain!

<pre class="sh_sh">
pacman -Syu arduino arduino-avr-core avr-gcc avr-binutils avr-libc avrdude
gpasswd -a $USER uucp
gpasswd -a $USER lock
</pre>

I'm using the AUR wrapper 'Bauerbill', taken from the creators TU repo.

<pre class="sh_sh">
vim /etc/pacman.conf
# https://xyne.archlinux.ca/repos/

pacman -Syu bauerbill
vim /etc/makepkg.conf # CFLAGS march=native MAKEFLAGS j, no compression
</pre>

Continue installing even more stuff, like a Webbrowser.

<pre class="sh_sh">
pacman -Syu hunspell hunspell-en hunspell-de firefox
# Install ublock Origin, set DuckDuckGo, etc.
</pre>

Install and configure NTP.

<pre class="sh_sh">
pacman -Syu ntp
vim /etc/ntp.conf
systemctl --user enable --now ntpd.service
</pre>

Some more applications.

<pre class="sh_sh">
bb-wrapper -Syu --aur perl-opengl perl-wx-glcanvas slic3r
pacman -Syu cura
pacman -Syu keepassxc
pacman -Syu mpv youtube-dl
pacman -Syu libreoffice okular picocom
</pre>

OpenSSH server needs to be enabled and started after installation.

<pre class="sh_sh">
pacman -Syu openssh
systemctl enable --now sshd.socket
</pre>

Fonts may require a call to fc-cache to update the font cache.

<pre class="sh_sh">
pacman -Syu breeze-gtk kde-gtk-config
pacman -Syu ttf-droid ttf-inconsolata ttf-liberation ttf-roboto
pacman -Syu ttf-dejavu ttf-bitstream-vera terminus-font
sudo fc-cache
</pre>

Some packets need 32bit libs on x64, so enable multilib.

<pre class="sh_sh">
vim /etc/pacman.conf # enable multilib
pacman -Syu lib32-nvidia-utils wine steam openscad
</pre>

Install Redshift to reduce eyestrain in the evenings (see [Redshift in Wiki](https://wiki.archlinux.org/index.php/Redshift#Manual_setup)).
To autostart on boot, run `redshift-gtk` in the GUI and click on autostart there.

<pre class="sh_sh">
pacman -Syu python-gobject redshift
vim ~/.config/redshift.conf
</pre>

Generate new SSH keys for GitHub etc. and also configure git.

<pre class="sh_sh">
ssh-keygen -t ecdsa -b 521
# generate as many as needed, one for github, one for webserver, one for home use, …
git config --global user.name “Thomas Buck”
git config --global user.email xythobuz@xythobuz.de
pacman -Syu meld
vim ~/.gitconfig # set meld as merge and diff, enable color
</pre>

Install more stuff.

<pre class="sh_sh">
pacman -Syu nmap wget konversation

sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
vim ~/.zshrc

pacman -Syu gvim
curl http://j.mp/spf13-vim3 -L -o - | sh
# http://vim.spf13.com/
</pre>

Install VirtualBox.

<pre class="sh_sh">
pacman -Syu virtualbox virtualbox-host-modules-arch virtualbox-guest-iso
bb-wrapper -Syu --aur virtualbox-ext-oracle
gpasswd -a $USER vboxusers
</pre>

If you are using an SSD, maybe think about enabling TRIM (see [SSD TRIM in Wiki](https://wiki.archlinux.org/index.php/Solid_State_Drive#Periodic_TRIM)).

<pre class="sh_sh">
sudo systemctl enable fstrim.timer

pacman -Syu thermald cpupower
vim /etc/default/cpupower
sudo systemctl enable cpupower.service
</pre>

I was also trying out Opera, but have now settled on Firefox.

<pre class="sh_sh">
pacman -Syu opera opera-ffmpeg-codecs
bb-wrapper -Syu --aur opera-adblock-complete
mkdir .opera
ln -s /usr/share/opera-adblock-complete/urlfilter.ini ~/.opera/urlfilter.ini
</pre>

To get Bluetooth to work you may need some firmware (see [StackExchange Question](https://unix.stackexchange.com/questions/421946/bluetooth-is-not-working-no-adapter-available-arch-linux-kde)).

<pre class="sh_sh">
bb-wrapper -Syu --aur bcm20702a1-firmware
systemctl enable --now bluetooth.service
</pre>

For monitoring needs (in conky), install hddtemp (see [Hddtemp in Wiki](https://wiki.archlinux.org/index.php/Hddtemp#Daemon)).

<pre class="sh_sh">
pacman -Syu hddtemp
systemctl edit hddtemp.service
systemctl enable --now hddtemp.service
</pre>

Install conky, a very cool monitoring tool (see [Conky in Wiki](https://wiki.archlinux.org/index.php/Conky#Autostart)).

<pre class="sh_sh">
bb-wrapper -Syu --aur conky-lua-nv
conky -C > ~/.conkyrc
vim ~/.conkyrc
</pre>

This is my conkyrc at the moment:

    -- vim: ts=4 sw=4 noet ai cindent syntax=lua
    --[[
    Conky, a system monitor, based on torsmo

    Any original torsmo code is licensed under the BSD license

    All code written since the fork of torsmo is licensed under the GPL

    Please see COPYING for details

    Copyright (c) 2004, Hannu Saransaari and Lauri Hakkarainen
    Copyright (c) 2005-2012 Brenden Matthews, Philip Kovacs, et. al. (see AUTHORS)
    All rights reserved.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    ]]

    conky.config = {
        alignment = 'bottom_right',
        xinerama_head = 2,
        background = false,
        border_width = 1,
        cpu_avg_samples = 2,
        default_color = 'white',
        default_outline_color = 'black',
        default_shade_color = 'white',
        draw_borders = false,
        draw_graph_borders = true,
        draw_outline = true,
        draw_shades = false,
        use_xft = true,
        font = 'DejaVu Sans Mono:size=12',
        gap_x = 10,
        gap_y = 10,
        minimum_height = 5,
        minimum_width = 5,
        net_avg_samples = 2,
        no_buffers = true,
        out_to_console = false,
        out_to_stderr = false,
        extra_newline = false,
        own_window = true,
        own_window_class = 'Conky',
        own_window_transparent = true,
        own_window_argb_visual = true,
        own_window_type = 'dock',
        own_window_hints = 'below',
        stippled_borders = 0,
        update_interval = 1.0,
        uppercase = false,
        use_spacer = 'none',
        show_graph_scale = false,
        show_graph_range = false,
        double_buffer = true
    }

    conky.text = [[
    ${texeci 60 curl --silent esp-e33750.fritz.box/values | tidy | grep -A1 -E 'PM10|PM2.5|Temperatur' | grep td | sed 's/<[^>]*>//g' | sed 's/&nbsp;/ /g' | sed 's/PM2.5/PM2.5\t/g' | sed 's/PM10/PM10\t/g' | sed '$!N;s/\n/\t\t/' }
    ${texeci 60 curl --silent esp-e33750.fritz.box/values | tidy | grep -A1 -E 'Luftfeuchte|Luftdruck|Signal' | grep td | sed 's/<[^>]*>//g' | sed 's/&nbsp;/ /g' | sed 's/rel. //g' | sed 's/Signal/Signal\t/g' |sed '$!N;s/\n/\t\t/' }
    $hr
    ${texeci 30 nmap -sn 192.168.178.1/24 -R --dns-servers 192.168.178.1 | awk -F "[ ()]+" '/Nmap scan report for/{print $6 "\t" $5}' | sed 's/^[ \t]*//'}
    $hr
    ${time %F %T %A}
    $sysname $kernel on $machine
    $hr
    ${color grey}Uptime:$color $uptime
    ${color grey}CPU Usage:$color ${freq_g}GHz ${cpu}% ${alignr}${cpubar 8,130}
    ${color grey}RAM Usage:$color $mem $memperc% ${alignr}${membar 8,130}
    ${color grey}Swap Usage:$color $swap $swapperc% ${alignr}${swapbar 8,130}
    $hr
    ${cpugraph cpu1 40,82 7F7F7F FFFFFF} ${cpugraph cpu2 40,82 7F7F7F FFFFFF} ${cpugraph cpu3 40,82 7F7F7F FFFFFF} ${cpugraph cpu4 40,82 7F7F7F FFFFFF}
    ${cpugraph cpu5 40,82 7F7F7F FFFFFF} ${cpugraph cpu6 40,82 7F7F7F FFFFFF} ${cpugraph cpu7 40,82 7F7F7F FFFFFF} ${cpugraph cpu8 40,82 7F7F7F FFFFFF}
    $hr
    ${color grey}CPU:${color} ${hwmon 1 temp 1}°C ${hwmon 1 temp 2}°C ${hwmon 1 temp 3}°C ${hwmon 1 temp 4}°C ${hwmon 1 temp 5}°C
    ${color grey}HDD:${color} ${exec hddtemp /dev/sda | awk '{print $(NF-1)}'}°C ${exec hddtemp /dev/sdb | awk '{print $(NF-1)}'}°C ${exec hddtemp /dev/sdc | awk '{print $(NF-1)}'}°C ${exec hddtemp /dev/sdd | awk '{print $(NF-1)}'}°C ${exec hddtemp /dev/sde | awk '{print $(NF-1)}'}°C ${exec hddtemp /dev/sdf | awk '{print $(NF-1)}'}°C
    ${color grey}GPU:${color} ${nvidia temp}°C ${nvidia gpufreq}MHz ${nvidia memfreq}MHz
    $hr
    ${color grey}File systems:
    ${color grey} /     ${color}${fs_used_perc /}% ${fs_bar 8 /}
    ${color grey} /home ${color}${fs_used_perc /home}% ${fs_bar 8 /home}
    $hr
    ${color grey}Networking:  Download ${alignr}Upload
    ${color grey}eno1        $color ${downspeed eno1} ${alignr}${upspeed eno1}
    ${color grey}enp3s0      $color ${downspeed enp3s0} ${alignr}${upspeed enp3s0}
    $hr
    ${downspeedgraph eno1 40,82 7F7F7F FFFFFF} ${upspeedgraph eno1 40,82 7F7F7F FFFFFF} ${downspeedgraph enp3s0 40,82 7F7F7F FFFFFF} ${upspeedgraph enp3s0 40,82 7F7F7F FFFFFF}
    $hr
    ${color grey}Processes:$color $processes ${alignr}${color grey}Running:$color $running_processes
    ${color grey}Name               PID   CPU%   MEM%
    ${color}${top name 1} ${top pid 1} ${top cpu 1} ${top mem 1}
    ${color}${top name 2} ${top pid 2} ${top cpu 2} ${top mem 2}
    ${color}${top name 3} ${top pid 3} ${top cpu 3} ${top mem 3}
    ${color}${top name 4} ${top pid 4} ${top cpu 4} ${top mem 4}
    ${color}${top name 5} ${top pid 5} ${top cpu 5} ${top mem 5}
    $hr
    ]]

Some nVidia graphics related settings.

<pre class="sh_sh">
sudo nvidia-settings # enable full composition pipeline, store x config
sudo vim /etc/X11/xorg.conf.d/20-nvidia.conf # remove unneeded stuff, add triple buffering
sudo vim /etc/profile.d/kwin.sh # enable triple buffering
# https://wiki.archlinux.org/index.php/NVIDIA/Troubleshooting#Avoid_screen_tearing

# Fix DPI, D0: 96x98, D1: 91x90 --> 96x96
# https://wiki.archlinux.org/index.php/Xorg#Proprietary_NVIDIA_driver
</pre>

I had a BluRay I wanted to rip but couldn't up to this point, because my Desktop is my only device with a BluRay reader.
So the point came to install and use the necessary software.

<pre class="sh_sh">
# MakeMKV BluRay support
# http://www.makemkv.com/forum2/viewtopic.php?f=5&amp;t=1053
bb-wrapper -Syu --aur lib32-glibc makemkv makemkv-libaacs
sudo sh -c “echo sg > /etc/modules-load.d/sg.conf“
modprobe sg
</pre>

At this point of the installation, I needed to change the keyboard layout of my Ergodox.
So I had to install some more development tools.

<pre class="sh_sh">
pacman -Syu arm-none-eabi-binutils arm-none-eabi-gcc arm-none-eabi-newlib dfu-util
pacman -Syu --needed git cmake ninja python libusb ctags gcc lsb-release
pacman -Syu --needed avr-binutils avr-gcc avr-libc
</pre>

Still more stuff to be installed.

<pre class="sh_sh">
pacman -Syu bind-tools
pacman -Syu pcsx2
pacman -Syu xorg-xev
pacman -Syu lsof strace htop
pacman -Syu fuse2 fuseiso
pacman -Syu spectacle
bb-wrapper -Syu --aur opentx-companion betaflight-configurator
bb-wrapper -Syu --aur libspnav spacenavd blender
</pre>

Install CUPS so we can print stuff.

<pre class="sh_sh">
pacman -Syu cups cups-pdf print-manager system-config-printer
systemctl enable --now org.cups.cupsd.service
sudo gpasswd -a $USER sys
</pre>

Enable Color Emojis (see [this Reddit Thread](https://www.reddit.com/r/archlinux/comments/9q8dlj/how_to_better_enable_color_emojis/)).

<pre class="sh_sh">
sudo pacman -S noto-fonts-emoji
sudo vim /etc/fonts/conf.avail/75-noto-color-emoji.conf
sudo ln -sf /etc/fonts/conf.avail/75-noto-color-emoji.conf /etc/fonts/conf.d/
</pre>

Automatically remove old versions of packages in local cache.

<pre class="sh_sh">
sudo pacman -S pacman-contrib
sudo systemctl enable --now paccache.timer
</pre>

Some more stuff that could be useful:

<pre class="sh_sh">
# fix for nextcloud aur build error
export LC_ALL=C

# nas mounts in /etc/fstab
192.168.0.5:/mnt/Excelsus/Media   /mnt/nas_media   nfs noauto,x-systemd.automount,x-systemd.device-timeout=30,_netdev
192.168.0.5:/mnt/Excelsus/Misc    /mnt/nas_misc    nfs noauto,x-systemd.automount,x-systemd.device-timeout=30,_netdev
192.168.0.5:/mnt/Excelsus/Dashcam /mnt/nas_dashcam nfs noauto,x-systemd.automount,x-systemd.device-timeout=30,_netdev

# Auto-update pacman mirrorlist
# https://www.reddit.com/r/archlinux/comments/9xmw3a/what_archlinux_tricks_do_you_know_that_you_wish/
</pre>

This is a nice little tool enabling auto-suggestion of packets when running a command that does not exist.

<pre class="sh_sh">
sudo bb-wrapper -Syu --aur pkgfile
sudo pkgfile -u
sudo systemctl enable --now pkgfile-update.timer
echo "source /usr/share/doc/pkgfile/command-not-found.zsh" > ~/.zsh
</pre>

If you want to keep the kernel modules of the currently running kernel after updating it with pacman, run these commands.
They will add a hook to pacman that copies the modules to a safe location on updates.
This way, you will still be able to use for example new USB devices without having rebooted after an update.

<pre class="sh_sh">
sudo bb-wrapper -Syu --aur kernel-modules-hook
sudo systemctl daemon-reload
sudo systemctl enable linux-modules-cleanup
</pre>

