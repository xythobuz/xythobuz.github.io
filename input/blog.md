title: Blog
parent: main
position: 1
changefreq: daily
priority: 0.8
funny: a day in the life of...
compat: blog
---

# Blog Archive

To receive my latest updates, you can subscribe the [RSS Feed! ![RSS Logo][logo]][rss]

<!--%
from datetime import datetime
posts = [p for p in pages if "post" in p] # get all blog post pages
posts.sort(key=lambda p: p.get("date"), reverse=True) # sort post pages by date
for p in posts:
    date = datetime.strptime(p.date, "%Y-%m-%d").strftime("%B %d, %Y")
    print "  * **[%s](%s)** - %s" % (p.post, p.url, date) # markdown list item
%-->

 [rss]: rss.xml
 [logo]: img/rss.png

lang: de

# Blog Archiv

Um über meine neuesten Artikel informiert zu werden, abonniere meinen [RSS Feed! ![RSS Logo][logo]][rss]

<!--%
from datetime import datetime
posts = [p for p in pages if "post" in p] # get all blog post pages
posts.sort(key=lambda p: p.get("date"), reverse=True) # sort post pages by date
for p in posts:
    date = datetime.strptime(p.date, "%Y-%m-%d").strftime("%d %B %Y")
    print "  * **[%s](%s)** - %s" % (p.post, p.url, date) # markdown list item
%-->

 [rss]: rss.xml
 [logo]: img/rss.png