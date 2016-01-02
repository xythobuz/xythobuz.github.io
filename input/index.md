title: Home
parent: main
position: 10
flattr: true
compat: home
---

<div style="width: 150px; height: 150px; float: right; border: 2px, solid, #000000; border-radius: 10px; background-image: url(http://www.gravatar.com/avatar/8d18fec40a74782052fb4c007d212475?s=150); margin-left: 2em; margin-bottom: 1em;"></div>

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

%--> year old Information Engineering student from Germany, mostly building stuff with AVR microcontrollers.
All of my projects are released as [Free Software](http://www.gnu.org/philosophy/free-sw.html) on my [GitHub profile](https://github.com/xythobuz), with more informations here. Have fun!

### Recent Blog Posts

<!--%
from datetime import datetime
posts = [p for p in pages if "post" in p] # get all blog post pages
posts.sort(key=lambda p: p.get("date"), reverse=True) # sort post pages by date
for p in posts[0:4]:
    date = datetime.strptime(p.date, "%Y-%m-%d").strftime("%B %d, %Y")
    print "  * **[%s](%s)** - %s" % (p.post, p.url, date) # markdown list item
%-->
  * [more...](blog.html)

### Tweets

<div style="width: 100%; margin-left: auto; margin-right: auto;">
<a class="twitter-timeline" data-dnt="true" href="https://twitter.com/xythobuz" data-widget-id="318732638158471170" data-chrome="noheader nofooter">Tweets by @xythobuz</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</div>
