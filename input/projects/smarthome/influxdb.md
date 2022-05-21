title: IoT Software Stack
description: InfluxDB / Grafana / Telegraf
parent: smarthome
position: 200
date: 2019-04-01
update: 2022-05-21
---

Besides the sensor inputs and actor outputs, which are handled by [my ESP-Env firmware](/espenv.html), a complete Smarthome setup also needs some software running on a central server.
This usually consists of a message broker, like [MQTT](https://mqtt.org/).
Some kind of database, preferably for time series data, like [InfluxDB](https://www.influxdata.com/products/influxdb-overview/).
And a way of visualizing that data, like [Grafana](https://grafana.com/).

The installation of all of these tools is in my case [handled by an ansible script](/sovereign.html).
They are running on a VM on my NAS.

I also have some other fun scripts running that feed data into Influx.
This includes [fritzinfluxdb](https://github.com/karrot-dev/fritzinfluxdb), which polls statistics from a Fritz.Box and includes a nice pre-made Grafana dashboard.
Another one is [nut-influxdb-exporter](https://github.com/kiwimato/nut-influxdb-exporter), which logs statistics from the UPS connected to my NAS.

All of my machines also run [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) to feed statistics about stuff like CPU and disk usage.

The [air quality monitor on my balcony](https://luftdaten.info/) also writes into the database, besides their [open sensor community map](https://deutschland.maps.sensor.community/#12/47.6926/9.4136).

<!--%
lightgallery([
    [ "img/grafana_env.png", "Snippet of environmental sensor data" ],
    [ "img/grafana_it.png", "Snippet of computing resources data" ],
])
%-->
