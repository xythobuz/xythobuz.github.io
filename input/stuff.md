title: Stuff
parent: main
position: 40
---

### {{ page.title }}

<!--%
mpages = [p for p in pages if p.get("parent", "") == "stuff" and p.lang == "en"]
mpages.sort(key=lambda p: int(p["position"]))
for p in mpages:
    print "  * **[%s](%s)**" % (p.title, p.url) # markdown list item
%-->

### MacPorts Maintainer

* **[cppcheck](https://trac.macports.org/browser/trunk/dports/devel/cppcheck/Portfile)** static code analysis

