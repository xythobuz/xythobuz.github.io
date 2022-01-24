title: Blog
post: Arch Linux on Medion Crawler E10
description: Installation and keyboard LED setup
date: 2022-01-18
comments: true
---

Together with a friend of mine we installed Arch Linux on her Medion Crawler E10 gaming laptop.
Some quick googling and we found out this seems to be a re-branded Clevo model notebook.
Installation was very straight forward, everything seems to work fine pretty much out-of-the-box.

These are the basic steps we had to take, maybe it helps someone else.
Some parts have been kept short, so always consider the current [Arch Installation Guide](https://wiki.archlinux.org/title/Installation_guide) as well!

Prepare the storage (SSD as cache for HDD, as described [here](https://unix.stackexchange.com/a/443415) / [here](https://lucaswerkmeister.de/posts/2018/05/12/luks-on-lvm/)), with full disk encryption and format the filesystems.

<pre class="sh_sh">
# set disk mode in UEFI to AHCI

fdisk
# /dev/sda1 128GB swap
# /dev/sda2 800GB data
# /dev/nvme0n1p1 300MB EFI
# /dev/nvme0n1p2 475GB data

pvcreate /dev/sda2 /dev/nvme0n1p2
vgcreate RootVG /dev/sda2 /dev/nvme0n1p2
lvcreate -l 100%PVS -n cryptroot RootVG /dev/sda2
lvcreate --type cache-pool -l 100%PVS -n cryptroot_cache RootVG /dev/nvme0n1p2
lvconvert --type cache --cachepool RootVG/cryptroot_cache RootVG/cryptroot

cryptsetup luksFormat --type luks2 /dev/RootVG/cryptroot
cryptsetup open /dev/RootVG/cryptroot root

mkfs.ext4 /dev/mapper/root
mkfs.fat -F32 /dev/nvme0n1p1
mkswap /dev/sda1

mount /dev/mapper/root /mnt
mkdir /mnt/boot
mount /dev/nvme0n1p1 /mnt/boot
swapon /dev/sda1
</pre>

Install everything that's needed.

<pre class="sh_sh">
reflector --verbose --latest 40 --number 15 --sort rate --protocol https --country "Germany" --save /etc/pacman.d/mirrorlist

pacstrap /mnt base base-devel linux linux-firmware

genfstab -U /mnt >> /mnt/etc/fstab

arch-chroot /mnt

ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
hwclock --systohc

pacman -Syu vim git sudo intel-ucode

vim /etc/locale.gen
locale-gen
vim /etc/locale.conf
vim /etc/vconsole.conf
vim /etc/hostname

pacman -Syu networkmanager
systemctl enable NetworkManager

pacman -Syu lvm2
vim /etc/mkinitcpio.conf
mkinitcpio -P

passwd

bootctl install
vim /etc/pacman.d/hooks/100-systemd-boot.hook
vim /boot/loader/loader.conf
vim /boot/loader/entries/arch.conf

useradd -m username_here
passwd username_here
gpasswd -a username_here wheel
visudo

# enable multilib repos & ILoveCandy
vim /etc/pacman.conf

pacman -Syu xorg-server nvidia nvidia-utils nvidia-settings lib32-nvidia-utils sddm pipewire pipewire-alsa pipewire-pulse pipewire-jack lib32-pipewire lib32-pipewire-jack helvum wireplumber sddm-kcm plasma-meta vlc dolphin dolphin-plugins kdialog kfind ark yakuake libreoffice-fresh openssh breeze-gtk kde-gtk-config ttf-droid ttf-inconsolata ttf-liberation ttf-roboto ttf-dejavu ttf-bitstream-vera terminus-font wine steam gvim firefox firefox-i18n-de firefox-ublock-origin cups cups-pdf print-manager system-config-printer pacman-contrib bluez-utils

systemctl enable sddm
systemctl enable sshd
fc-cache
systemctl enable cups
systemctl enable paccache.timer

echo btusb > /etc/modules-load.d/bluetooth.conf
systemctl enable bluetooth.service

# enable DRM kernel mode settings
# in mkinitcpio and bootloader config

pacman -Syu nvidia-prime
# use prime-run for PRIME render offloading

# install AUR helper, we used bauerbill
</pre>

Setup LED keyboard backlight control. As described [here at NovaCustom](https://configurelaptop.eu/clevo-keyboard-backlight-control-for-linux/).

<pre class="sh_sh">
# install dmidecode
sudo dmidecode | grep "Product Name"
# --> CRAWLER E10

# clone pkgbuild from dkms driver
# https://aur.archlinux.org/packages/clevo-xsm-wmi-dkms/
# adjust included patch, replace model name with "CRAWLER E10"

pacman -Syu dkms linux-headers
makepkg
pacman -U pkgname
modprobe clevo-xsm-wmi kb_color=white,white,white, kb_brightness=1
sudo tee /etc/modules-load.d/clevo-xsm-wmi.conf <<< clevo-xsm-wmi

# https://aur.archlinux.org/packages/clevo-xsm-wmi-util/
# for graphical control
</pre>

Afterwards, install required user applications (Gimp, Okular, ...) and configure the KDE desktop to personal preferences. Also check out the [General Recommendations in the Arch Wiki](https://wiki.archlinux.org/title/General_recommendations).
