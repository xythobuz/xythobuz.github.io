title: OctoPrint Setup
description: Setting up OctoPrint and some common improvements
parent: 3d-printing
position: 30
comments: true
flattr: true
---

<span class="listdesc">[...back to 3D-Printing overview](3d-printing.html)</span>

All my 3D printers are connected to a Raspberry Pi running [OctoPrint](https://octoprint.org/).
For ease of use, I suggest downloading and installing a pre-made [OctoPi image](https://octoprint.org/download/).
Here on this page I describe some common steps and improvements I do on each of them.

### Controlling a Power Supply

To turn the power for the 3D printer on and off from within OctoPrint, there are different methods available depending on the setup of your 3D printer.
If you are using a standard fixed-voltage brick power supply, you can use a cheap relais board to switch the power between your supply and the printer.
If however you are using an ATX power supply, you can not only power the Raspberry Pi from the 5V standby rail, you can also turn the rest of the power supply, and therefore the printer, on and off using the corresponding signal of the ATX supply.
By default, the purple cable will carry the 5V standby power, and the green cable needs to be pulled low to turn the supply on.

I've decided to simply use the GPIOs at the top of the Raspberry Pi pinheader normally used for I2C, as they already contain pullup resistors.

[Here are some hints on how to use a relais board with the Raspberry Pi](https://github.com/foosel/OctoPrint/wiki/Controlling-a-relay-board-from-your-RPi#modify-the-5v-relay-board-to-run-off-of-rpi-33v-gpio-pins-sainsmart-5v-relay-from-amazon).

[Here are the instructions to add commands for controlling the printer power](https://github.com/foosel/OctoPrint/wiki/Controlling-a-relay-board-from-your-RPi#manual-way). I'd suggest using this way of adding some system actions to OctoPrint, as these can also be used from the Telegram Plugin for example. This is not the case when using the PSU Control Plugin in OctoPrint.

### Automatically Connect to Printer

[Bernd Zeimetz has a great writeup on how to auto-connect to the serial port](https://bzed.de/post/2017/11/octoprint_autoconnect_printer/) of your 3D printer.
Here is the brief version of it, slightly modified to work with current OctoPrint versions.

Create the script `/home/pi/connect_octoprint.py` with the following contents:

<pre class="sh_python">
#!/home/pi/oprint/bin/python2

OCTOPRINT_URL = 'http://localhost:5000/api/connection'
API_KEY = 'YOUR_API_KEY_HERE'
BAUDRATE = 115200

import requests
import sys

port = sys.argv[1]
headers = {'X-Api-Key': API_KEY}
json = {
    "command": "connect",
    "port": port,
    "baudrate": BAUDRATE,
}

r = requests.post(
    OCTOPRINT_URL,
    json=json,
    headers=headers
)

if (r.status_code == 204):
    sys.exit(0)
else:
    print(r)
    sys.exit(1)
</pre>

Make sure to replace the API Key from your OctoPrint user settings page.
Also change the baudrate if needed.
Don't forget to make the script executable with `chmod a+x connect_octoprint.py`!

Now create the file `/etc/systemd/system/octoprint_connect@.service` with the following contents:

    [Unit]
    Description=Connect printer to OctoPrint automatically
    BindsTo=dev-%i.device
    After=dev-%i.device

    [Service]
    Type=oneshot
    User=pi
    RemainAfterExit=yes
    ExecStart=/home/pi/connect_octoprint.py /dev/%I

To make the new service usable:

<pre class="sh_sh">
sudo systemctl daemon-reload
</pre>

Find out the USB Vendor and Product ID of the 3D printer serial port:

<pre class="sh_sh">
lsusb -v | grep -iE '(^bus|idvendor|idproduct)'
</pre>

Then create the file `/etc/udev/rules.d/3dprinter.rules` and modify its contents with the IDs you got from the previous step:

    KERNEL=="tty*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", \
        TAG+="systemd", ENV{SYSTEMD_WANTS}="octoprint_connect@%k.service"

That should be it.
If it doesn't work, there's some debugging hints in the article linked above, like:

<pre class="sh_sh">
systemctl list-units 'octoprint_connect*'
journalctl -u octoprint_connect@ttyUSB0.service
</pre>

### Physical Power Button

Besides controlling eg. an ATX power supply or a relay connecting the printer to the power supply, I also wanted a push-button connected to the Raspberry Pi that can toggle the power supply using the aforementioned connection on the Pi.
This can be solved using a simple Python script.
For this, we also need to install a small dependency:

<pre class="sh_sh">
sudo apt-get install python3-rpi.gpio
mkdir ~/button-script
vim ~/button-script/power.py
</pre>

and enter something like this:

<pre class="sh_python">
#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

sleep_timeout = 1000
sleep_toggle = 5.0
pin_button = 5
pin_power = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin_button, GPIO.IN)
GPIO.setup(pin_power, GPIO.IN)
GPIO.setup(pin_power, GPIO.OUT, initial=GPIO.input(pin_power))

while True:
    channel = GPIO.wait_for_edge(pin_button, GPIO.FALLING, timeout=sleep_timeout)
    if channel is not None:
        GPIO.output(pin_power, not GPIO.input(pin_power))
        time.sleep(sleep_toggle)

GPIO.cleanup()
</pre>

Of course, you may need to adjust the pin numbers or the logic if you're not using an active-low switch.
Make the script executable and create a bootup-script to autostart it:

<pre class="sh_sh">
chmod a+x ~/button-script/power.py
sudo vim /etc/init.d/octopi-power-button
</pre>

And enter the following:

<pre class="sh_sh">
#!/bin/sh
/home/pi/button-script/power.py &
</pre>

Now also make this script executable, register it for execution on boot, and run it for the current session:

<pre class="sh_sh">
sudo chmod a+x /etc/init.d/octopi-power-button
sudo update-rc.d /etc/init.d/octopi-power-button defaults
sudo /etc/init.d/octopi-power-button
</pre>

Now every time you press the button (with a 5s debounce delay afterwards) the printer power will be toggled.

### Automatic Photo Upload

As you may have seen, all my 3D printer are [uploading a photo every 5 minutes](printer.html) to this webserver.
Achieving this is very simple.
First, you have to ensure that you can do a passwordless key-based ssh login from your Raspberry Pi running OctoPrint to your webserver. For this, you may need to generate an ssh key on your Pi:

<pre class="sh_sh">
ssh-keygen
</pre>

For the prompts just press enter, the defaults are fine.
Then, copy the contents of the newly generated public key in `~/.ssh/id_rsa.pub` to your webserver into the `~/.ssh/authorized_keys` file.
Test the connection and accept the prompt when connecting for the first time, in my case:

<pre class="sh_sh">
ssh thomas@xythobuz.de
</pre>

Now, create a new script somewhere:

<pre class="sh_sh">
mkdir ~/foto-script
vim ~/foto-script/upload.sh
</pre>

and fill it with the following contents:

<pre class="sh_sh">
#!/bin/bash
wget -O printer.jpg http://127.0.0.1:8080/?action=snapshot
scp printer.jpg thomas@xythobuz.de:/var/www/xythobuz/printer.jpg
rm printer.jpg
</pre>

Of course, you may need to adjust the destination path on your webserver.
Finally, add the script as a cronjob using `crontab -e`:

    */5 * * * * sudo -u pi /home/pi/foto-script/upload.sh >/dev/null 2>/dev/null

And that's it. An updated photo will appear on your webserver every 5 minutes.
You can take a look at it [on my website](printer.html).
