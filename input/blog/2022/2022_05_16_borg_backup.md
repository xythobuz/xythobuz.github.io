title: Blog
post: BorgBackup automation scripts
description: Distributed, encrypted, deduplicated and compressed backups
date: 2022-05-16
comments: true
---

I have been using [BorgBackup](https://www.borgbackup.org/) for a while now to backup my machines to external drives and a NAS.
For more convenience I created a set of scripts to automate this process.

The first part is a script doing the actual backup process by calling borg.
This is inspired by [the example script in the documentation](https://borgbackup.readthedocs.io/en/stable/quickstart.html#automating-backups).

<pre class="sh_sh">
#!/bin/sh

# ~/bin/backup-borg

# Helper script for automated borg backups.
# BACKUP_PATH, BACKUP_EXCLUDES, BORG_REPO and BORG_PASSPHRASE
# should already be set in environment from calling script!

if [[ -z "$BACKUP_PATH" ]]; then
    echo "Please set BACKUP_PATH before calling"
    exit 1
fi
if [[ -z "$BACKUP_EXCLUDES" ]]; then
    echo "Please set BACKUP_EXCLUDES before calling"
    exit 1
fi
if [[ -z "$BORG_REPO" ]]; then
    echo "Please set BORG_REPO before calling"
    exit 1
fi
# $BORG_PASSPHRASE is allowed to be empty

# some helpers and error handling:
info() { printf "\n%s\n%s\n\n" "$( date )" "$*" >&2; }
trap 'echo $( date ) Backup interrupted >&2; exit 2' INT TERM

info "Starting backup"

# Backup the most important directories into an archive named after
# the machine this script is currently running on:

borg create              \
    --verbose            \
    --list               \
    --filter E           \
    --stats              \
    --progress           \
    --show-version       \
    --show-rc            \
    --compression lz4    \
    --exclude-caches     \
    $BACKUP_EXCLUDES     \
                         \
    ::'{hostname}-{now}' \
    $BACKUP_PATH

backup_exit=$?

info "Pruning repository"

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. The '{hostname}-' prefix is very important to
# limit prune's operation to this machine's archives and not apply to
# other machines' archives also:

borg prune                 \
    --verbose              \
    --list                 \
    --prefix '{hostname}-' \
    --progress             \
    --show-version         \
    --show-rc              \
    --keep-daily    7      \
    --keep-weekly   4      \
    --keep-monthly  6

prune_exit=$?

info "Compacting repository"

# Also do a compact after each prune, to free space
borg compact       \
    --verbose      \
    --progress     \
    --show-version \
    --show-rc

compact_exit=$?

# use highest exit code as global exit code
bp_exit=$(( backup_exit > prune_exit ? backup_exit : prune_exit ))
global_exit=$(( bp_exit > compact_exit ? bp_exit : compact_exit ))

if [ ${global_exit} -eq 1 ];
then
    info "Backup finished with a warning"
fi

if [ ${global_exit} -gt 1 ];
then
    info "Backup finished with an error"
fi

exit ${global_exit}
</pre>

Run the following commands to create a new repository and export it's key.
This key needs to be stored somewhere safe, along with the password you set in the first command.

    borg init --encryption=repokey /path/to/repo
    borg key export /path/to/repo key-file-name

I have multiple different borg repositories on various disks and machines.
For each combination of backup input and output location, I created another script, calling the previous one with the proper values for location, excludes and repository password.

<pre class="sh_sh">
#!/bin/sh

# ~/bin/backup-root-extern

export BORG_REPO=/mnt/backup/borg-linux-root
export BORG_PASSPHRASE='REDACTED'

export BACKUP_PATH=/
export BACKUP_EXCLUDES="    \
    --exclude=/home/*       \
    --exclude=/var/cache/*  \
    --exclude=/var/tmp/*    \
    --exclude=/media/*      \
    --exclude=/mnt/*        \
    --exclude=/dev/*        \
    --exclude=/proc/*       \
    --exclude=/sys/*        \
    --exclude=/tmp/*        \
    --exclude=/run/*        \
    --exclude=/lost+found/* \
"

backup-borg

backup_exit=$?
exit ${backup_exit}
</pre>

For convenience, I created yet another script that does all the backups into the same locations / machine.

<pre class="sh_sh">
#!/bin/sh

# ~/bin/backup-extern

sudo backup-root-extern
root_exit=$?

sudo backup-home-extern
home_exit=$?

sudo backup-data-extern
data_exit=$?

# use highest exit code as global exit code
rh_exit=$(( root_exit > home_exit ? root_exit : home_exit ))
global_exit=$(( rh_exit > data_exit ? rh_exit : data_exit ))

if [ ${global_exit} -eq 1 ];
then
    echo "One or Multiple Backups finished with a warning"
fi

if [ ${global_exit} -gt 1 ];
then
    echo "One or Multiple Backups finished with an error"
fi

exit ${global_exit}
</pre>

Which can easily be combined with the following script, which tries to mount one of the external backup disks I rotate through.

<pre class="sh_sh">
#!/bin/bash

# ~/bin/mount-backup

( sudo mount -U xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /mnt/backup -t ext4 ||
  sudo mount -U xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /mnt/backup -t ext4
) && echo ok
</pre>

I can now simply plug in a backup disk and run "mount-backup && backup-extern" to run a new backup.

I'm also [using these scripts for Cloud backups](2022_06_06_hetzner_storage_box.html).
