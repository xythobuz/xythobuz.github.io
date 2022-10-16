title: MQTT Webinterface
description: Using Bootstrap and JavaScript for universal controls
parent: smarthome
position: 400
git: https://git.xythobuz.de/thomas/lights-web
github: https://github.com/xythobuz/mqtt-lights-web
date: 2022-08-14
comments: true
---

<!--% backToParent() %-->

Both my [ESP-Env sensors and actors](espenv.html) as well as the [Node-RED automation](nodered.html) are interfacing to the network using MQTT.

This allows easy control using for example the [mosquitto_pub](https://mosquitto.org/man/mosquitto_pub-1.html) MQTT command line client.
With these four commands I'm overriding my Node-RED controlled bathroom light automation.

<pre class="sh_sh">
mosquitto_pub -h $HOSTNAME -u $USERNAME -P $PASSWORD -t bathroom/force_light -r -m none
mosquitto_pub -h $HOSTNAME -u $USERNAME -P $PASSWORD -t bathroom/force_light -r -m big
mosquitto_pub -h $HOSTNAME -u $USERNAME -P $PASSWORD -t bathroom/force_light -r -m small
mosquitto_pub -h $HOSTNAME -u $USERNAME -P $PASSWORD -t bathroom/force_light -r -m off
</pre>

At the same time the environment sensors also publish their measurements to the corresponding MQTT topics.

To have a central place where these settings can be viewed and changed, not only for me but also for guests, I decided to write a small interactive web interface.
It interfaces to the MQTT broker using WebSockets.
Unfortunately this only seems to work with Chromium, not Firefox.

<!--%
lightgallery([
    [ "img/mqtt_lights_web_2.png", "Screenshot of Livingroom controls" ],
    [ "img/mqtt_lights_web.png", "Screenshot of Bathroom controls" ],
])
%-->

You can [find the source code on my Gitea](https://git.xythobuz.de/thomas/lights-web).
I also added the installation and setup instructions to my [ansible scripts](sovereign.html).
