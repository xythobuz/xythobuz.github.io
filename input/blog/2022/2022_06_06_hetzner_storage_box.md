title: Blog
post: BorgBackup in the Cloud
description: Using the Hetzner Storage Box
date: 2022-06-06
comments: true
---

To back up [my NAS](nas_2018.html#06_2022) I was shopping around for different cloud storage providers that I could use with [BorgBackup](https://www.borgbackup.org/).

Here are some yearly prices, calculated for a storage requirement of ~22TB (22.000GB).

<table style="text-align: right;"><tr>
<th><div>Name</div></th>
<th><div>Fixed Price / y</div></th>
<th><div>Free GB</div></th>
<th><div>Cost add. GB / y</div></th>
<th><div>Cost / y</div></th>
</tr><tr>
<th><div>Borgbase Small</div></th>
<td><div>24</div></td>
<td><div>100</div></td>
<td><div>1,2</div></td>
<td><div>26304</div></td>
</tr><tr>
<th><div>Borgbase Medium</div></th>
<td><div>80</div></td>
<td><div>1000</div></td>
<td><div>0,084</div></td>
<td><div>1844</div></td>
</tr><tr>
<th><div>Borgbase Large</div></th>
<td><div>150</div></td>
<td><div>2000</div></td>
<td><div>0,06</div></td>
<td><div>1350</div></td>
</tr><tr>
<th><div>rsync.net &lt;1TB</div></th>
<td><div>0</div></td>
<td><div>0</div></td>
<td><div>0,18</div></td>
<td><div>3960</div></td>
</tr><tr>
<th><div>rsync.net &lt;100TB</div></th>
<td><div>0</div></td>
<td><div>0</div></td>
<td><div>0,096</div></td>
<td><div>2112</div></td>
</tr><tr>
<th><div>rsync.net &gt;100TB</div></th>
<td><div>0</div></td>
<td><div>0</div></td>
<td><div>0,06</div></td>
<td><div>1320</div></td>
</tr><tr>
<th><div>Wasabi Storage</div></th>
<td><div>0</div></td>
<td><div>0</div></td>
<td><div>0,0708</div></td>
<td><div>1557,6</div></td>
</tr><tr>
<th><div>Google Storage Std</div></th>
<td><div>0</div></td>
<td><div>0</div></td>
<td><div>0,276</div></td>
<td><div>6072</div></td>
</tr><tr>
<th><div>Google Storage NL</div></th>
<td><div>0</div></td>
<td><div>0</div></td>
<td><div>0,12</div></td>
<td><div>2640</div></td>
</tr><tr>
<th></th>
<td></td>
<td></td>
<td></td>
<td></td>
</tr><tr>
<th><div>Hetzner 20TB Storage</div></th>
<td><div>526,92</div></td>
<td><div>0</div></td>
<td><div>0,026346</div></td>
<td><div>526,92</div></td>
</tr></table>

As you can tell, most providers I looked at are actually pretty expensive.
One reason for this are their guarantees against data-loss.

One of the rows in the table above is not like the others, and that is the [Hetzner Storage Box](https://www.hetzner.com/storage/storage-box).
These do not provide a dynamically growing storage, like the others.
Instead you get a fixed amount of memory, depending on the amount of money you pay.
The largest available size is 20TB, which is less than the 22TB I calculated with.
But in reality I only need ~16TB currently for backups.

Because this is only used as an offsite backup for me, I decided to go with it for it's far lower price, because I can live with the possibility of losing data when their [DC burns down](https://en.wikipedia.org/wiki/OVHcloud#Incidents) or something 🚒 🧑‍🚒

Ordering a new storage box instance is straight-forward.
You get a username, DNS name and auto-generated password in the Hetzner Web UI.
In there you can also enable different access methods; we need SSH for Borg.

Setting up [SSH authentication](https://docs.hetzner.com/robot/storage-box/backup-space-ssh-keys) and [using Borg](https://community.hetzner.com/tutorials/install-and-configure-borgbackup) are described in the [Hetzner docs](https://docs.hetzner.com/robot/storage-box/).

The workflow is a bit strange, I have to admit.
While you can use Borg or rsync over SSH with the storage box, interactive logins are not possible and you can also not use `ssh-copy-id`.
Instead, commands need to be executed via sftp.
These are the steps I had to do to enable public-key authentication and initialize a borg repo.

<pre class="sh_sh">
cat .ssh/KEY.pub >> storagebox
echo -e "mkdir .ssh \n chmod 700 .ssh \n put storagebox .ssh/authorized_keys \n chmod 600 .ssh/authorized_keys" | sftp USER@USER.your-storagebox.de
rm storagebox
echo -e "mkdir backups \n mkdir backups/NAME" | sftp USER@USER.your-storagebox.de
BORG_RSH='ssh -i /home/USER/.ssh/KEY' borg init --encryption=repokey ssh://USER@USER.your-storagebox.de:23/./backups/NAME
BORG_RSH='ssh -i /home/USER/.ssh/KEY' borg key export ssh://USER@USER.your-storagebox.de:23/./backups/NAME keyfile
mv keyfile SOMEWHERE_SAFE
</pre>

Then I simply adapted my [existing backup scripts](2022_05_16_borg_backup.html) to add a BORG_RSH export.

<pre class="sh_sh">
#!/bin/sh

export BORG_REPO=ssh://USER@USER.your-storagebox.de:23/./backups/NAME
export BORG_PASSPHRASE='PASSWORD'
export BORG_RSH='ssh -i /home/USER/.ssh/KEY'

export BACKUP_PATH=/PATH_TO_BACKUP
export BACKUP_EXCLUDES="      \
    --exclude=/EXCLUDED_PATHS \
"

backup-borg

backup_exit=$?
exit ${backup_exit}
</pre>
