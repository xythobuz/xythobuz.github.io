title: Projects
parent: main
position: 10
---

This page lists all of my projects that are documented on this website.
Some projects have a specific date and time where I worked on them, so they are listed by date below.
Some others are on-going or still recent for other reasons, these are listed first.

<!--%
# prints all pages with parent 'projects' or 'stuff'.
# first the ones without date, sorted by position.
# then afterwards those with date, split by year.
# also supports blog posts with parent.

enpages = [p for p in pages if p.lang == "en"]

dpages = [p for p in enpages if p.get("date", "") == ""]
mpages = [p for p in dpages if any(x in p.get("parent", "") for x in [ 'projects', 'stuff' ])]
mpages.sort(key=lambda p: [int(p.get("position", "999"))])
for p in mpages:
    print "  * **[%s](%s)**" % (p.title, p.url)
    if p.get("description", "") != "":
        print "<br><span class=\"listdesc\">" + p.get("description", "") + "</span>"

dpages = [p for p in enpages if p.get("date", "") != ""]
mpages = [p for p in dpages if any(x in p.get("parent", "") for x in [ 'projects', 'stuff' ])]
mpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)
lastyear = "0"
for p in mpages:
    title = p.title
    if p.title == "Blog":
        title = p.post

    year = p.get("date", "")[0:4]
    if year != lastyear:
        lastyear = year
        print "\n\n#### %s\n" % (year)

    dateto = ""
    if p.get("update", "") != "" and p.get("update", "")[0:4] != year:
        dateto = " (%s - %s)" % (year, p.get("update", "")[0:4])

    print "  * **[%s](%s)**%s" % (title, p.url, dateto)

    if p.get("description", "") != "":
        print "<br><span class=\"listdesc\">" + p.get("description", "") + "</span>"
%-->
