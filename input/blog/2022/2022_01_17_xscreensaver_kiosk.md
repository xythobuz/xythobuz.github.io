title: Blog
post: XScreenSaver as TV decoration
description: Script for placing fullscreen windows
date: 2022-01-17
---

I got a new TV connected to my PC.
Using xrandr, I made some simple scripts to switch between stand-alone or mirrored mode.
To control media playback comfortably from the desktop monitor, I'm using the nifty little tool [squint](https://github.com/a-ba/squint/), auto-starting and killing it as needed from my aforementioned scripts.

To show some pretty pictures on the TV, I also created the following (pretty hacky) script for moving [XScreenSaver](https://www.jwz.org/xscreensaver/) hacks fullscreen'ed to the TV.

Maybe it helps someone else.

<pre class="sh_sh">
#!/bin/bash

# tv-screen-saver
#
# Show random animations on only one monitor.
#
# Dependencies:
#   - XScreenSaver
#   - wmctrl
#   - xdotool
#
# This script randomly selects a screensaver (hack) from XScreenSaver,
# runs it, moves it to a specific location on the desktop,
# fullscreens it, waits for 5mins, then kills the hack.
# This process is repeated endlessly.
#
# Control the position where the window will be placed by editing the
# MONITOR_PLACE below. The parameters are X-Pos,Y-Pos,Width,Height.
# Use -1 to keep existing values.
#
# Hacks that should be skipped are listed in HACK_BLACKLIST below.
#
# The window focus will be saved and restored when opening a new hack.
#
# Bugs:
# In the timespan of opening a new hack, some keypresses may go to the new
# hack window, if you are currently typing.

TIMEOUT=300
MONITOR_PLACE="3000,-1,-1,-1"
HACKS_DIR=/usr/lib/xscreensaver

HACK_BLACKLIST=("xscreensaver-auth" "xscreensaver-getimage" "xscreensaver-getimage-file" "xscreensaver-getimage-video" "xscreensaver-gfx" "xscreensaver-gl-visual" "xscreensaver-systemd" "xscreensaver-text" "webcollage" "webcollage-helper" "vidwhacker")

HACK_PID=0
FOCUS_WIN=0

# kill running screensaver when user exits with Ctrl+C
trap graceful_exit INT

# make sure screensavers can find required xscreensaver-text and other helpers
PATH=$PATH:$HACKS_DIR

get_random_hack() {
    HACK_NAME=$(ls $HACKS_DIR | shuf -n 1)

    # skip if on blacklist
    for i in ${!HACK_BLACKLIST[@]};
    do
        if [ "$HACK_NAME" == "${HACK_BLACKLIST[$i]}" ]
        then
            get_random_hack
            exit 0
        fi
    done

    echo $HACK_NAME
}

put_on_tv() {
    wmctrl -r 'from the XScreenSaver' -e 0,$MONITOR_PLACE
    wmctrl -r 'from the XScreenSaver' -b toggle,fullscreen
}

save_window_focus() {
    FOCUS_WIN=$(xdotool getactivewindow)
}

restore_window_focus() {
    xdotool windowactivate $FOCUS_WIN
}

graceful_exit() {
    if [ "$HACK_PID" -ne "0" ]
    then
        kill $HACK_PID
    fi
    exit 0
}

while true
do
    save_window_focus

    # run new hack
    HACK=$(get_random_hack)
    echo "Running $HACK for $TIMEOUT seconds"
    $HACKS_DIR/$HACK &
    HACK_PID=$!

    # wait for window to appear
    sleep 0.2
    put_on_tv

    restore_window_focus

    sleep $TIMEOUT
    kill $HACK_PID

    # wait a bit before starting next one
    sleep 0.2
done
</pre>
