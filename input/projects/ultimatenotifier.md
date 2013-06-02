title: Ultimate Notifier Script
title_de: Ultimate Notifier Script
description: Sending Push Notifications to an iPhone from a Bash Script
parent: software
position: 6
comments: true
flattr: true
compat: notifier
twitter: xythobuz
reddit: true
print: true
---

# {{ page.title }}

The service [Ultimate Notifier][1] allows you to send Push-Notification to your iPhone easily. Based on this, you can write shell scripts that are executed regularly via cron. This could inform you about a changed public IP. To do this, save this script somewhere:

<pre class="sh_sh">
#!/bin/sh

ipfile=".currentip"
service="ifconfig.me"
user="username"
pass="password"
message="IP:"

ip=`curl -s $service`
touch $ipfile
lastip=`cat $ipfile`
if [ "$ip" != "$lastip" ]; then
    echo "New public IP. Sending notification!"
    curl -s "https://www.ultimatenotifier.com/items/User/send/${user}/message=${message}%20${ip}/password=${pass}"
fi
cp /dev/null $ipfile
echo $ip > $ipfile
</pre>

It gets the current public IP via [ifconfig.me][2] and compares it to the IP stored in a file named .currentip. If they differ, a Push-Notification will be sent and the new IP stored.

With the command

<pre>crontab -e</pre>

>You can add a cronfile entry. To execute the script every 30 minutes, use this:

<pre>*/30 * * * * /Users/anon/bin/ipnotify.sh</pre>

You can find the code on [GitHub][3], too!

Of course, you can extend this principle. This script is called every 5 minutes on my server to notify me about eventual problems.

<pre class="sh_sh">
#!/bin/bash

# Checks for Health of Server and sends notifications to iPhone in case of error
# Checks for:
# -	HDD Temperature
# -	HDD Space
# -	CPU Usage
# Sends a notification via UltimateNotifier
# Depends on bash, wget, hddtemp, grep, awk, sed, ps, sort and head.

# ------------------------------
# ------------------------------

# Your UltimateNotifier Password
UNUsername="YourUserName"
UNPassword="YourPassWord"

# Check for free space
hddMountPoint="bay" # greps for this in mounted hdds
maxPercentFull=75 # minimum percentage to send notification

# Check for CPU Usage of processes
maxCpuUsage=750 # Is in tenths of a percent (420 => 42%)

# Checks hdd temperature
# Depends on hddtemp tool
hddDevice="/dev/sda"
maxHddTemp=50

# ------------------------------
# ------------------------------

# Set $message to your Message and then call this...
function sendNotification {
	wget "https://www.ultimatenotifier.com/items/User/send/${UNUsername}/message=${message}/password=${UNPassword}" -O /dev/null -q
	echo "$message"
}

# ------------------------------
# ------------------------------

# Check for hdd temperature
hddTemp=`/usr/sbin/hddtemp ${hddDevice} | awk '{print $4}' | awk -F 'Â°' '{print $1}'`
if [ $hddTemp -gt $maxHddTemp ]; then
	message="Marvin's HDD has reached ${hddTemp}Â°C!"
	sendNotification
fi

# Check for free space on hdd
spaceUsed=`df -h | grep ${hddMountPoint} | awk '{print $5}' | sed 's/%//'`
if [ $spaceUsed -gt $maxPercentFull ]; then
	message="Marvin's HDD is ${spaceUsed}% full!"
	sendNotification
fi

# Check for most cpu intensive process, report if usage too high
processName=`ps -e -o cp,args | sed -e 's/^[ \\t]*//' | awk -F " " '{print $1, $2}' | sed -e '1d' | sort -rn | head -1 | awk '{print $2}'`
processUsage=`ps -e -o cp,args | sed -e 's/^[ \\t]*//' | awk -F " " '{print $1, $2}' | sed -e '1d' | sort -rn | head -1 | awk '{print $1}'`
if [ $processUsage -gt $maxCpuUsage ]; then
	processUsage=`echo "${processUsage} / 10.0" | bc -q`
	message="${processName} needs ${processUsage}% CPU!"
	sendNotification
fi
</pre>

 [1]: http://ultimatenotifier.com
 [2]: http://ifconfig.me
 [3]: https://github.com/xythobuz/Snippets/blob/master/ipnotify.sh

lang: de

# {{ page.title_de }}

Der Dienst [Ultimate Notifier][1] erlaubt es relativ problemlos, zum Beispiel mittels curl Push-Notifications an ein iPhone zu senden. Darauf basierend können Shell Skripte geschrieben werden, welche regelmäßig als Cron-Job gestartet werden. So kann man sich zum Beispiel über eine geänderte Public IP informieren lassen. Dafür muss dieses Skript irgendwo gespeichert werden:

<pre class="sh_sh">
#!/bin/sh

ipfile=".currentip"
service="ifconfig.me"
user="username"
pass="password"
message="IP:"

ip=`curl -s $service`
touch $ipfile
lastip=`cat $ipfile`
if [ "$ip" != "$lastip" ]; then
    echo "New public IP. Sending notification!"
    curl -s "https://www.ultimatenotifier.com/items/User/send/${user}/message=${message}%20${ip}/password=${pass}"
fi
cp /dev/null $ipfile
echo $ip > $ipfile
</pre>

Es liest die aktuelle öffentliche IP mittels curl vom Dienst [ifconfig.me][2] aus und vergleicht diese mit der zwischengespeicherten IP in einer Datei namens .currentip. Unterscheiden sich die IPs, wird eine Push Notification gesendet und die neue IP gespeichert.

Mit dem Befehl

<pre>crontab -e</pre>

Kann ein Eintrag ins cronfile hinzugefügt werden, sodass das Skript regelmäßig gestartet wird. Ein Beispiel, für 30 Minuten:

<pre>*/30 * * * * /Users/anon/bin/ipnotify.sh</pre>

Der Code findet sich auch auf [GitHub][3].

Natürlich kann dieses Prinzip beliebig erweitert werden. Dieses Bash Skript wird auf meinem Server alle 5 Minuten von cron gestartet und berichtet über eventuelle Probleme.

<pre class="sh_sh">
#!/bin/bash

# Checks for Health of Server and sends notifications to iPhone in case of error
# Checks for:
# - HDD Temperature
# - HDD Space
# - CPU Usage
# Sends a notification via UltimateNotifier
# Depends on bash, wget, hddtemp, grep, awk, sed, ps, sort and head.

# ------------------------------
# ------------------------------

# Your UltimateNotifier Password
UNUsername="YourUserName"
UNPassword="YourPassWord"

# Check for free space
hddMountPoint="bay" # greps for this in mounted hdds
maxPercentFull=75 # minimum percentage to send notification

# Check for CPU Usage of processes
maxCpuUsage=750 # Is in tenths of a percent (420 => 42%)

# Checks hdd temperature
# Depends on hddtemp tool
hddDevice="/dev/sda"
maxHddTemp=50

# ------------------------------
# ------------------------------

# Set $message to your Message and then call this...
function sendNotification {
  wget "https://www.ultimatenotifier.com/items/User/send/${UNUsername}/message=${message}/password=${UNPassword}" -O /dev/null -q
  echo "$message"
}

# ------------------------------
# ------------------------------

# Check for hdd temperature
hddTemp=`/usr/sbin/hddtemp ${hddDevice} | awk '{print $4}' | awk -F 'Â°' '{print $1}'`
if [ $hddTemp -gt $maxHddTemp ]; then
  message="Marvin's HDD has reached ${hddTemp}Â°C!"
  sendNotification
fi

# Check for free space on hdd
spaceUsed=`df -h | grep ${hddMountPoint} | awk '{print $5}' | sed 's/%//'`
if [ $spaceUsed -gt $maxPercentFull ]; then
  message="Marvin's HDD is ${spaceUsed}% full!"
  sendNotification
fi

# Check for most cpu intensive process, report if usage too high
processName=`ps -e -o cp,args | sed -e 's/^[ \\t]*//' | awk -F " " '{print $1, $2}' | sed -e '1d' | sort -rn | head -1 | awk '{print $2}'`
processUsage=`ps -e -o cp,args | sed -e 's/^[ \\t]*//' | awk -F " " '{print $1, $2}' | sed -e '1d' | sort -rn | head -1 | awk '{print $1}'`
if [ $processUsage -gt $maxCpuUsage ]; then
  processUsage=`echo "${processUsage} / 10.0" | bc -q`
  message="${processName} needs ${processUsage}% CPU!"
  sendNotification
fi
</pre>

 [1]: http://ultimatenotifier.com/
 [2]: http://ifconfig.me
 [3]: https://github.com/xythobuz/Snippets/blob/master/ipnotify.sh