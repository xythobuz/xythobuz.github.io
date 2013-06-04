title: Software
parent: main
position: 3
compat: sw
---

# {{ page.title }}

These are my mostly software-related projects and articles.

<!--%
mpages = [p for p in pages if p.get("parent", "") == "software" and p.lang == "en"]
mpages.sort(key=lambda p: int(p["position"]))
for p in mpages:
    print "  * **[%s](%s)**" % (p.title, p.url) # markdown list item
%-->

lang: de

# {{ page.title }}

Dies sind meine Projekte, deren Schwerpunkt eher im Bereich Software liegen.

<!--%
mpages = [p for p in pages if p.get("parent", "") == "software" and p.lang == "en"]
mpages.sort(key=lambda p: int(p["position"]))
for p in mpages:
    print "  * **[%s](%s)**" % (p.title, p.url) # markdown list item
%-->