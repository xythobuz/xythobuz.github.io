title: Hardware
parent: main
position: 4
compat: hw
---

# {{ page.title }}

These are my mostly hardware-related projects and articles.

<!--%
mpages = [p for p in pages if p.get("parent", "") == "hardware" and p.lang == "en"]
mpages.sort(key=lambda p: int(p["position"]))
for p in mpages:
    print "  * **[%s](%s)**" % (p.title, p.url) # markdown list item
%-->

lang: de

# {{ page.title }}

Dies sind meine Projekte, deren Schwerpunkt eher im Bereich Hardware liegen.

<!--%
mpages = [p for p in pages if p.get("parent", "") == "hardware" and p.lang == "en"]
mpages.sort(key=lambda p: int(p["position"]))
for p in mpages:
    print "  * **[%s](%s)**" % (p.title, p.url) # markdown list item
%-->