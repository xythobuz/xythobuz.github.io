title: Blog
parent: main
position: 20
changefreq: daily
priority: 0.8
compat: blog
noheader: true
---

# Blog Archive

To receive my latest updates, you can subscribe to the [RSS Feed! ![RSS Logo][logo]][rss]

<!--%
from datetime import datetime
posts = [p for p in pages if "post" in p] # get all blog post pages
posts.sort(key=lambda p: p.get("date", "9999-01-01"), reverse=True) # sort post pages by date
lastyear = "0"
for p in posts:
    year = p.get("date", "")[0:4]
    if year != lastyear:
        lastyear = year
        print "\n\n#### %s\n" % (year)

    date = datetime.strptime(p.date, "%Y-%m-%d").strftime("%B %d, %Y")
    print "  * **[%s](%s)** - %s" % (p.post, p.url, date)

    if p.get("description", "") != "":
        print "<br><span class=\"listdesc\">" + p.get("description", "") + "</span>"
%-->

 [rss]: rss.xml
 [logo]: img/rss.png
