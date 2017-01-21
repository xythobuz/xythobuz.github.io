title: Blog
post: Adding full-screen apps to the f.lux whitelist
date: 2017-01-21
comments: true
flattr: true
---

## {{ page["post"] }}
<!--%
from datetime import datetime
date = datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
print "*Posted at %s.*" % date
%-->

The [f.lux utility](https://justgetflux.com) is a Mac OS X application that allows 'warming up' the colors of your monitors at night to reduce strain on the eyes. Of course, this distorts the colors at night, so it of course has the ability to whitelist certain apps. As long as these apps are in the foreground, the f.lux effect is disabled.

F.lux just lives in the system nav bar, so there's no proper GUI that would allow adding or removing apps from the whitelist. Instead, you can only enable or disable whitelisting for the current foreground App. Of course, this gets problematic when the app in question is only in fullscreen-mode and does not allow the mouse pointer to leave the window.

So I've developed a little work-around. Taking a look at the flux preferences file in `~/Library/Preferences/org.herf.Flux.plist`, one can easily see that flux adds an entry there for each whitelisted app, the name of this entry is `disable-` followed by the bundle identifier of the disabled app. The value is True when the app is disabled, and False when not.

So, to add our own apps and games to this, first we need to find out the bundle identifier of our app. You could open the package, locate the plist file and read it manually, or you can ask AppleScript:

    $ osascript -e 'id of app "Hitman Absolution"'
    com.feralinteractive.hitmanabsolution

Now, I first tried modifying the flux preferences plist directly, but that doesn't work. Instead, add your new key, in my case for Hitman Absolution, using defaults:

    defaults write org.herf.Flux disable-com.feralinteractive.hitmanabsolution 1

To enable flux for you app, just run the last command again replacing the 1 at the end with a 0.

