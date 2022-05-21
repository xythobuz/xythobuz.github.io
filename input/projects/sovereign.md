title: Ansible Server Setup
description: My changes to the 'Sovereign' project
parent: projects
comments: true
flattr: true
git: https://git.xythobuz.de/thomas/sovereign
github: https://github.com/xythobuz/sovereign
date: 2019-01-04
update: 2022-05-22
---

I first started hosting my own web and mail server in [April 2013](/2013_04_02_zaphod.html), with a Debian 6 VPS at Hetzner, with manually configured Apache, Dovecot, Postfix and some other stuff.
I followed random tutorials on the web, mostly not understanding what I'm actually doing and learning as I went along.
But over time this got problematic.
I dist-upgraded to Debian 7, probably in 2014, breaking a bunch of stuff in the process, but was somehow able to still cobble together a working system.
As this was going on over the following years, I grew more scared of touching anything in the system, in fear of breaking my mail setup and impacting daily-life.

So when Hetzner announced in 2018 that they will shut-off the VPS product line I was on in April 2019, I had a dead-line for fixing this mess.
At the same time, of course I continued my progression as a programmer and computer user, which put me in a much better position to take better care of my setup this time around.
By coincidence, I read about the [Sovereign project](https://github.com/sovereign/sovereign) on [that orange page](https://hn.algolia.com/?dateRange=all&page=0&prefix=false&query=github.com%2Fsovereign&sort=byPopularity&type=story).
I decided to fork this, take the pieces that I need, remove stuff that is not useful for my usecases and add other software to it.

The result can be found [on Gitea](https://git.xythobuz.de/thomas/sovereign) or [on GitHub](https://github.com/xythobuz/sovereign).
Please take a look at the [README.md](https://git.xythobuz.de/thomas/sovereign/src/branch/master/README.md) in the repo.
It lists all the included software and where I tested it.

I still host my stuff with Hetzner, now in their [Cloud product line](https://www.hetzner.com/cloud).
Currently I run one instance for the page you're looking at now, one instance for a Wiki and Jitsi for a group of friends and one instance as-needed for testing changes to the scripts.

I also use sovereign to configure some things in my home network.
This is a Linux VM running on my TrueNAS, which runs my IoT setup for my appliances, like [MQTT, Grafana](/influxdb.html) and [Node-RED](/nodered.html).

<!--%
lightgallery([
    [ "img/sovereign_monit.png", "Screenshot of monit on VPS" ],
    [ "img/sovereign_iot.png", "Screenshot of monit on VM" ],
])
%-->
