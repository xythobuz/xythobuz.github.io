title: MQTT Telegram Bot
description: Go server to control stuff from anywhere in the world
parent: smarthome
position: 500
git: https://git.xythobuz.de/thomas/lights-telegram
github: https://github.com/xythobuz/mqtt-lights-telegram
date: 2022-08-23
comments: true
---

<!--% backToParent() %-->

After creating my [MQTT Web UI](mqtt_web.html) I had some troubles getting it to work on all devices.
My server at home is using a self-signed SSL certificate.
I imported the certificate authority into my desktop, which Chromium accepts fine there.
But on Android the connection is still considered insecure, even with the CA cert imported, so the JS can not communicate with the MQTT broker.

To work around that problem I decided to create a simple Telegram Bot that can fulfill the same task of switching the lights.

<!--%
lightgallery([
    [ "img/mqtt_telegram.png", "Screenshot of chat with bot" ],
])
%-->

You can [find the source code on my Gitea](https://git.xythobuz.de/thomas/lights-telegram), as well as installation and setup instructions.

This was my first time doing something with Go.
I think the language is interesting and I will probably continue using it in the future.
On one hand it was quite easy to find some suitable libraries that simplified the main tasks of the application greatly!
But also the language features I found out about impressed me.

One good example is reading the config file.
You can simply define a struct that holds all configuration variables, with additional markup to control how it is marshalled and unmarshalled into different formats, in my case yaml.

<pre class="sh_go">
type Mqtt struct {
    Url string `yaml:"url"`
    User string `yaml:"username"`
    Pass string `yaml:"password"`
}

type Registration struct {
    Name string `yaml:"name"`
    Topic string `yaml:"topic"`
    Values []string `yaml:"values"`
}

type Config struct {
    // Telegram Bot API key
    Key string `yaml:"api_key"`

    // Telegram UserID (int64) of admin account
    Admin int64 `yaml:"admin_id"`

    // MQTT credentials
    Mqtt Mqtt

    // Telegram UserIDs (int64) of allowed users
    // (does not need to be modified manually)
    Users []int64 `yaml:"authorized_users"`

    // Available MQTT topics
    // (does not need to be modified manually)
    Registration []Registration
}

// default values
var config = Config {
    Key: "API_KEY_GOES_HERE",
    Admin: 0,
    Mqtt: Mqtt {
        Url: "wss://MQTT_HOST:MQTT_PORT",
        User: "MQTT_USERNAME",
        Pass: "MQTT_PASSWORD",
    },
}
</pre>

Using simple functions to read and write files according to this format, you can then get a file looking something like this.

<pre class="sh_yaml">
api_key: API_KEY_REDACTED
admin_id: ADMIN_ID_REDACTED
mqtt:
    url: wss://iot.fritz.box:8083
    username: USERNAME_REDACTED
    password: PASSWORD_REDACTED
authorized_users: []
registration:
    - name: kitchen
      topic: livingroom/light_kitchen
      values:
        - "on"
        - "off"
    - name: bathroom
      topic: bathroom/force_light
      values:
        - none
        - big
        - small
        - "off"
    - name: pc
      topic: livingroom/light_pc
      values:
        - "on"
        - "off"
    - name: workbench
      topic: livingroom/light_bench
      values:
        - "on"
        - "off"
    - name: box
      topic: livingroom/light_box
      values:
        - "on"
        - "off"
    - name: amp
      topic: livingroom/light_amp
      values:
        - "on"
        - "off"
</pre>

I'm using this file both to store static configuration data, like the API key, as well as runtime configuration data entered by the admin user, like available MQTT topics.

All in all I was able to implement a basic working prototype in less than 500 LOC and in just a single evening!
