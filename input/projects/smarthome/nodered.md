title: Node-RED
description: Point 'n' Click workflow automation
parent: smarthome
position: 300
date: 2021-11-01
update: 2022-05-21
---

[Node-RED](https://nodered.org/) is a great tool for visually creating workflows based on events.
I use it in conjunction with my [ESP-Env sensor and actor hardware](espenv.html) and MQTT to automate my *smart* home.

I plan to extend these workflows as required when I add new hardware to my network.

Here is a simple setup that automatically switches lights in my bathroom according to the sun position, using [node-red-contrib-sunevents](https://github.com/freakent/node-red-contrib-sunevents).

The fan in my window-less bathroom is kept on all the time for now.
In the future I want to add movement sensors to the bathroom and integrate them into this logic, as well as the temperature / humidity sensors I already have in there.
All these devices run my [ESP-Env](/espenv.html) firmware.

<!--%
lightgallery([
    [ "img/nodered_lights.png", "Switching the lights" ],
    [ "img/nodered_fan.png", "Keeping fan always on" ],
    [ "img/nodered_mqtt.png", "Helper function for MQTT" ],
])
%-->

And here are the flows for importing in Node-RED.
<button type="button" onclick="copyEvent('jsonlights')" style="font-size: 1em; margin-left: 1em;">Copy to clipboard</button>

<!-- https://clay-atlas.com/us/blog/2021/06/30/html-en-copy-text-button/ -->
<script>
function copyEvent(id) {
    var str = document.getElementById(id);
    window.getSelection().selectAllChildren(str);
    document.execCommand("Copy")
}
</script>

<pre id="jsonlights">
[
    {
        "id": "490116e54af5ff9a",
        "type": "tab",
        "label": "Bathroom Lights",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "74341bea93cc320d",
        "type": "tab",
        "label": "Bathroom Fan",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "b9932c4c66b18537",
        "type": "tab",
        "label": "Functions",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "5be146a97e98891c",
        "type": "mqtt-broker",
        "name": "iot.fritz.box",
        "broker": "iot.fritz.box",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "5",
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "sessionExpiry": ""
    },
    {
        "id": "4039bc1ca3cd6e11",
        "type": "comment",
        "z": "490116e54af5ff9a",
        "name": "Check for new Sun Events",
        "info": "",
        "x": 150,
        "y": 160,
        "wires": []
    },
    {
        "id": "ce5504b6991f8bf4",
        "type": "inject",
        "z": "490116e54af5ff9a",
        "name": "Every 12h",
        "props": [
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "43200",
        "crontab": "",
        "once": true,
        "onceDelay": "1",
        "topic": "",
        "x": 110,
        "y": 200,
        "wires": [
            [
                "5151002c9539d2d6"
            ]
        ]
    },
    {
        "id": "5151002c9539d2d6",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Set Location",
        "rules": [
            {
                "t": "set",
                "p": "payload.latitude",
                "pt": "msg",
                "to": "47.6",
                "tot": "str"
            },
            {
                "t": "set",
                "p": "payload.longitude",
                "pt": "msg",
                "to": "9.4",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 270,
        "y": 200,
        "wires": [
            [
                "bc6e8bf098875279"
            ]
        ]
    },
    {
        "id": "bc6e8bf098875279",
        "type": "sun events",
        "z": "490116e54af5ff9a",
        "testmode": false,
        "verbose": "N",
        "topic": "",
        "name": "Sun Events",
        "x": 430,
        "y": 200,
        "wires": [
            [
                "4384fcd3b3567c6c",
                "9c21e093193d54e4"
            ]
        ]
    },
    {
        "id": "d8f1896d6ed5ca0d",
        "type": "switch",
        "z": "490116e54af5ff9a",
        "name": "On Sunrise",
        "property": "sunevent",
        "propertyType": "global",
        "rules": [
            {
                "t": "eq",
                "v": "sunrise",
                "vt": "str"
            }
        ],
        "checkall": "false",
        "repair": false,
        "outputs": 1,
        "x": 350,
        "y": 360,
        "wires": [
            [
                "98d848700eaa119d",
                "76965df29f0c2651"
            ]
        ]
    },
    {
        "id": "d17e0c1b295d531a",
        "type": "switch",
        "z": "490116e54af5ff9a",
        "name": "On Sunset",
        "property": "sunevent",
        "propertyType": "global",
        "rules": [
            {
                "t": "eq",
                "v": "sunset",
                "vt": "str"
            }
        ],
        "checkall": "false",
        "repair": false,
        "outputs": 1,
        "x": 350,
        "y": 480,
        "wires": [
            [
                "3e4a16697db5b83d",
                "6df166fb14211461"
            ]
        ]
    },
    {
        "id": "895f005abb0c7a30",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Bathroom Big Light",
        "rules": [
            {
                "t": "set",
                "p": "topic",
                "pt": "msg",
                "to": "bathroom/light_big",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 690,
        "y": 340,
        "wires": [
            [
                "c8246e3ed2f6ac51"
            ]
        ]
    },
    {
        "id": "c8246e3ed2f6ac51",
        "type": "link call",
        "z": "490116e54af5ff9a",
        "name": "",
        "links": [
            "fd3c7a7a7a3b2e99"
        ],
        "timeout": "30",
        "x": 960,
        "y": 420,
        "wires": [
            []
        ]
    },
    {
        "id": "bbd4b1ede10ea09e",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Bathroom Small Light",
        "rules": [
            {
                "t": "set",
                "p": "topic",
                "pt": "msg",
                "to": "bathroom/light_small",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 700,
        "y": 460,
        "wires": [
            [
                "c8246e3ed2f6ac51"
            ]
        ]
    },
    {
        "id": "0516f39aac309884",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Store Sun State",
        "rules": [
            {
                "t": "set",
                "p": "sunevent",
                "pt": "global",
                "to": "payload.sunevent",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 800,
        "y": 200,
        "wires": [
            [
                "23bd87871e2f0ecb"
            ]
        ]
    },
    {
        "id": "86248602292b2932",
        "type": "inject",
        "z": "490116e54af5ff9a",
        "name": "Every 30sec",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "30",
        "crontab": "",
        "once": true,
        "onceDelay": "5",
        "topic": "",
        "payloadType": "date",
        "x": 120,
        "y": 360,
        "wires": [
            [
                "d8f1896d6ed5ca0d",
                "d17e0c1b295d531a"
            ]
        ]
    },
    {
        "id": "98d848700eaa119d",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Turn On",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "on",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 520,
        "y": 340,
        "wires": [
            [
                "895f005abb0c7a30"
            ]
        ]
    },
    {
        "id": "76965df29f0c2651",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Turn Off",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "off",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 520,
        "y": 380,
        "wires": [
            [
                "b7ea8636c374cd25"
            ]
        ]
    },
    {
        "id": "b7ea8636c374cd25",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Bathroom Small Light",
        "rules": [
            {
                "t": "set",
                "p": "topic",
                "pt": "msg",
                "to": "bathroom/light_small",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 700,
        "y": 380,
        "wires": [
            [
                "c8246e3ed2f6ac51"
            ]
        ]
    },
    {
        "id": "3e4a16697db5b83d",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Turn On",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "on",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 520,
        "y": 460,
        "wires": [
            [
                "bbd4b1ede10ea09e"
            ]
        ]
    },
    {
        "id": "6df166fb14211461",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Turn Off",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "off",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 520,
        "y": 500,
        "wires": [
            [
                "8c16ac287cbf877c"
            ]
        ]
    },
    {
        "id": "8c16ac287cbf877c",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Bathroom Big Light",
        "rules": [
            {
                "t": "set",
                "p": "topic",
                "pt": "msg",
                "to": "bathroom/light_big",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 690,
        "y": 500,
        "wires": [
            [
                "c8246e3ed2f6ac51"
            ]
        ]
    },
    {
        "id": "6af17a7135211b49",
        "type": "comment",
        "z": "490116e54af5ff9a",
        "name": "Set Lights",
        "info": "",
        "x": 100,
        "y": 320,
        "wires": []
    },
    {
        "id": "23bd87871e2f0ecb",
        "type": "debug",
        "z": "490116e54af5ff9a",
        "name": "Sun Event Data",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "sunevent",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 980,
        "y": 200,
        "wires": []
    },
    {
        "id": "b3edc5ecdc862850",
        "type": "comment",
        "z": "490116e54af5ff9a",
        "name": "Initialize Sun State",
        "info": "",
        "x": 130,
        "y": 40,
        "wires": []
    },
    {
        "id": "ac6c11189b8f1778",
        "type": "inject",
        "z": "490116e54af5ff9a",
        "name": "Once",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "topic": "",
        "payloadType": "date",
        "x": 90,
        "y": 80,
        "wires": [
            [
                "f66b01b2a01a9c70"
            ]
        ]
    },
    {
        "id": "f66b01b2a01a9c70",
        "type": "change",
        "z": "490116e54af5ff9a",
        "name": "Sunrise Sun State",
        "rules": [
            {
                "t": "set",
                "p": "sunevent",
                "pt": "global",
                "to": "sunrise",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 250,
        "y": 80,
        "wires": [
            []
        ]
    },
    {
        "id": "9c21e093193d54e4",
        "type": "switch",
        "z": "490116e54af5ff9a",
        "name": "Is Sunrise?",
        "property": "payload.sunevent",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "sunrise",
                "vt": "str"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 1,
        "x": 610,
        "y": 240,
        "wires": [
            [
                "0516f39aac309884"
            ]
        ]
    },
    {
        "id": "4384fcd3b3567c6c",
        "type": "switch",
        "z": "490116e54af5ff9a",
        "name": "Is Sunset?",
        "property": "payload.sunevent",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "sunset",
                "vt": "str"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 1,
        "x": 610,
        "y": 200,
        "wires": [
            [
                "0516f39aac309884"
            ]
        ]
    },
    {
        "id": "669b4c826982a274",
        "type": "comment",
        "z": "490116e54af5ff9a",
        "name": "Only store relevant states",
        "info": "",
        "x": 630,
        "y": 160,
        "wires": []
    },
    {
        "id": "e70de37a1b248a25",
        "type": "inject",
        "z": "74341bea93cc320d",
        "name": "Every 1min",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "60",
        "crontab": "",
        "once": true,
        "onceDelay": "10",
        "topic": "",
        "payloadType": "date",
        "x": 130,
        "y": 100,
        "wires": [
            [
                "4375482d5ce5df1c"
            ]
        ]
    },
    {
        "id": "4375482d5ce5df1c",
        "type": "change",
        "z": "74341bea93cc320d",
        "name": "Turn On",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "on",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 300,
        "y": 100,
        "wires": [
            [
                "9f7db20cf89cff6d"
            ]
        ]
    },
    {
        "id": "86f29e0ed5d23b51",
        "type": "comment",
        "z": "74341bea93cc320d",
        "name": "Keep bathroom fan always on",
        "info": "Make sure fan is always turned on.\nNo sensors available yet to do this better.",
        "x": 160,
        "y": 60,
        "wires": []
    },
    {
        "id": "9f7db20cf89cff6d",
        "type": "change",
        "z": "74341bea93cc320d",
        "name": "Bathroom Fan",
        "rules": [
            {
                "t": "set",
                "p": "topic",
                "pt": "msg",
                "to": "bathroom/fan",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 480,
        "y": 100,
        "wires": [
            [
                "2e5626a57c7fdbe1"
            ]
        ]
    },
    {
        "id": "2e5626a57c7fdbe1",
        "type": "link call",
        "z": "74341bea93cc320d",
        "name": "",
        "links": [
            "fd3c7a7a7a3b2e99"
        ],
        "timeout": "30",
        "x": 660,
        "y": 100,
        "wires": [
            []
        ]
    },
    {
        "id": "e6010f1672bac815",
        "type": "mqtt out",
        "z": "b9932c4c66b18537",
        "name": "IoT MQTT",
        "topic": "",
        "qos": "",
        "retain": "",
        "respTopic": "",
        "contentType": "text/plain",
        "userProps": "",
        "correl": "",
        "expiry": "",
        "broker": "5be146a97e98891c",
        "x": 210,
        "y": 160,
        "wires": []
    },
    {
        "id": "8a4031a3be97bf0a",
        "type": "debug",
        "z": "b9932c4c66b18537",
        "name": "Debug Print",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "statusVal": "",
        "statusType": "auto",
        "x": 210,
        "y": 120,
        "wires": []
    },
    {
        "id": "fd3c7a7a7a3b2e99",
        "type": "link in",
        "z": "b9932c4c66b18537",
        "name": "set_mqtt",
        "links": [],
        "x": 55,
        "y": 80,
        "wires": [
            [
                "8a4031a3be97bf0a",
                "e6010f1672bac815",
                "d185ca7a7211b37e"
            ]
        ]
    },
    {
        "id": "db9d2ccfce698ced",
        "type": "comment",
        "z": "b9932c4c66b18537",
        "name": "set_mqtt",
        "info": "",
        "x": 100,
        "y": 40,
        "wires": []
    },
    {
        "id": "d185ca7a7211b37e",
        "type": "link out",
        "z": "b9932c4c66b18537",
        "name": "",
        "mode": "return",
        "links": [],
        "x": 155,
        "y": 80,
        "wires": []
    }
]
</pre>

The Node-RED installation is [handled by an ansible script](/sovereign.html).
