title: Home
parent: main
position: 1
flattr: true
compat: home
noheader: true
---

# Hi there!

<img id="index-avatar" src="img/ava.jpg">

I'm a <!--%
from datetime import datetime
from datetime import timedelta
from calendar import isleap

size_of_day = 1. / 366.
size_of_second = size_of_day / (24. * 60. * 60.)

def date_as_float(dt):
    days_from_jan1 = dt - datetime(dt.year, 1, 1)
    if not isleap(dt.year) and days_from_jan1.days >= 31+28:
        days_from_jan1 += timedelta(1)
    return dt.year + days_from_jan1.days * size_of_day + days_from_jan1.seconds * size_of_second

start_date = datetime(1994,1,22,0,0)
end_date = datetime.now()
difference_in_years = date_as_float(end_date) - date_as_float(start_date)

print int(difference_in_years)

%--> year old software developer from Germany.
All of my projects are released as free or open-source software on [my Gitea Server](https://git.xythobuz.de/thomas), [my GitHub profile](https://github.com/xythobuz) and here on my website. Have fun!

To receive my latest updates, you can subscribe to the <a href="rss.xml"><img src="img/rss.png">RSS Feed</a>.

### Recent Posts and Updates

<!--%
printRecentMenu(10)
%-->
