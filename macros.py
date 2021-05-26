import re
import itertools
import email.utils
import os.path
import time
import codecs
from datetime import datetime

DEFAULT_LANG = "en"
BASE_URL = "https://www.xythobuz.de"

# -----------------------------------------------------------------------------
# menu helper macro
# -----------------------------------------------------------------------------

def printMenuItem(p, yearsAsHeading = False, showDateSpan = False, showOnlyStartDate = False, nicelyFormatFullDate = False, lastyear = "0", lang = ""):
    title = p.title
    if lang != "":
        if p.get("title_" + lang, "") != "":
            title = p.get("title_" + lang, "")
    if p.title == "Blog":
        title = p.post

    year = p.get("date", "")[0:4]
    if year != lastyear:
        lastyear = year
        if yearsAsHeading:
            print "\n\n#### %s\n" % (year)

    dateto = ""
    if p.get("date", "" != ""):
        year = p.get("date", "")[0:4]
        if showOnlyStartDate:
            dateto = " (%s)" % (year)

        if p.get("update", "") != "" and p.get("update", "")[0:4] != year:
            if showDateSpan:
                dateto = " (%s - %s)" % (year, p.get("update", "")[0:4])

        if nicelyFormatFullDate:
            dateto = " - " + datetime.strptime(p.date, "%Y-%m-%d").strftime("%B %d, %Y")

    print "  * **[%s](%s)**%s" % (title, p.url, dateto)

    if p.get("description", "") != "":
        description = p.get("description", "")
        if lang != "":
            if p.get("description_" + lang, "") != "":
                description = p.get("description_" + lang, "")
        print "<br><span class=\"listdesc\">" + description + "</span>"

    return lastyear

def printRecentMenu(count = 5):
    posts = [p for p in pages if "date" in p]
    posts.sort(key=lambda p: p.get("date"), reverse=True)
    for p in posts[0:count]:
        printMenuItem(p, False, False, False, True)

def printBlogMenu():
    posts = [p for p in pages if "post" in p]
    posts.sort(key=lambda p: p.get("date", "9999-01-01"), reverse=True)
    lastyear = "0"
    for p in posts:
        lastyear = printMenuItem(p, True, False, False, True, lastyear)

def printProjectsMenu():
    # prints all pages with parent 'projects' or 'stuff'.
    # first the ones without date, sorted by position.
    # then afterwards those with date, split by year.
    # also supports blog posts with parent.
    enpages = [p for p in pages if p.lang == "en"]

    dpages = [p for p in enpages if p.get("date", "") == ""]
    mpages = [p for p in dpages if any(x in p.get("parent", "") for x in [ 'projects', 'stuff' ])]
    mpages.sort(key=lambda p: [int(p.get("position", "999"))])
    for p in mpages:
        printMenuItem(p)

    dpages = [p for p in enpages if p.get("date", "") != ""]
    mpages = [p for p in dpages if any(x in p.get("parent", "") for x in [ 'projects', 'stuff' ])]
    mpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)
    lastyear = "0"
    for p in mpages:
        lastyear = printMenuItem(p, True, True, False, False, lastyear)

def print3DPrintingMenu():
    mpages = [p for p in pages if p.get("parent", "") == "3d-printing" and p.lang == "en"]
    mpages.sort(key=lambda p: int(p["position"]))
    for p in mpages:
        printMenuItem(p, False, True, True)

def printQuadcopterMenu():
    mpages = [p for p in pages if p.get("parent", "") == "quadcopters" and p.lang == "en"]
    mpages.sort(key=lambda p: int(p["position"]))
    for p in mpages:
        printMenuItem(p, False, True, True)
# -----------------------------------------------------------------------------
# lightgallery helper macro
# -----------------------------------------------------------------------------

# call this macro like this
# lightgallery([
#     [ "image-link", "description" ],
#     [ "image-link", "thumbnail-link", "description" ],
#     [ "youtube-link", "thumbnail-link", "description" ],
#     [ "video-link", "mime", "thumbnail-link", "image-link", "description" ]
# ])

def lightgallery(links):
    videos = [l for l in links if len(l) == 5]
    v_i = 0
    for v in videos:
        link, mime, thumb, poster, alt = v
        v_i += 1
        print '<div style="display:none;" id="video' + str(v_i) + '">'
        print '<video class="lg-video-object lg-html5" controls preload="none">'
        print '<source src="' + link + '" type="' + mime + '">'
        print 'Your browser does not support HTML5 video.'
        print '</video>'
        print '</div>'
        
    print '<div class="lightgallery">'
    v_i = 0
    for l in links:
        if (len(l) == 3) or (len(l) == 2):
            link = img = alt = ""
            if len(l) == 3:
                link, img, alt = l
            else:
                link, alt = l
                x = link.rfind('.')
                img = link[:x] + '_small' + link[x:]
            print '<div class="border" data-src="' + link + '"><a href="' + link + '"><img class="pic" src="' + img + '" alt="' + alt + '"></a></div>'
        elif len(l) == 5:
            v_i += 1
            link, mime, thumb, poster, alt = v
            print '<div class="border" data-poster="' + poster + '" data-sub-html="' + alt + '" data-html="#video' + str(v_i) + '"><a href="' + link + '"><img class="pic" src="' + thumb + '"></a></div>'
        else:
            raise NameError('Invalid number of arguments for lightgallery')
    print '</div>'

# -----------------------------------------------------------------------------
# github helper macros
# -----------------------------------------------------------------------------

import urllib, json

def restRequest(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

def restReleases(user, repo):
    s = "https://api.github.com/repos/"
    s += user
    s += "/"
    s += repo
    s += "/releases"
    return restRequest(s)

def printLatestRelease(user, repo):
    repo_url = "https://github.com/" + user + "/" + repo
    print("<div class=\"releasecard\">")
    print("Release builds for " + repo + " are <a href=\"" + repo_url + "/releases\">available on GitHub</a>.<br>\n")

    releases = restReleases(user, repo)
    if len(releases) <= 0:
        print("No release has been published on GitHub yet.")
        print("</div>")
        return

    releases.sort(key=lambda x: x["published_at"], reverse=True)
    r = releases[0]
    release_url = r["html_url"]
    print("Latest release of <a href=\"" + repo_url + "\">" + repo + "</a>, at the time of this writing: <a href=\"" + release_url + "\">" + r["name"] + "</a> (" + datetime.strptime(r["published_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S") + ")\n")

    if len(r["assets"]) <= 0:
        print("<br>No release assets have been published on GitHub for that.")
        print("</div>")
        return

    print("<ul>")
    print("Release Assets:")
    for a in r["assets"]:
        size = int(a["size"])
        ss = " "
        if size >= (1024 * 1024):
            ss += "(%.1f MiB)" % (size / (1024.0 * 1024.0))
        elif size >= 1024:
            ss += "(%d KiB)" % (size // 1024)
        else:
            ss += "(%d Byte)" % (size)

        print("<li><a href=\"" + a["browser_download_url"] + "\">" + a["name"] + "</a>" + ss)
    print("</ul></div>")

# -----------------------------------------------------------------------------
# preconvert hooks
# -----------------------------------------------------------------------------

def hook_preconvert_anotherlang():
    MKD_PATT = r'\.(?:md|mkd|mdown|markdown)$'
    _re_lang = re.compile(r'^[\s+]?lang[\s+]?[:=]((?:.|\n )*)', re.MULTILINE)
    vpages = [] # Set of all virtual pages
    for p in pages:
        current_lang = DEFAULT_LANG # Default language
        langs = [] # List of languages for the current page
        page_vpages = {} # Set of virtual pages for the current page
        text_lang = re.split(_re_lang, p.source)
        text_grouped = dict(zip([current_lang,] + \
                                        [lang.strip() for lang in text_lang[1::2]], \
                                        text_lang[::2]))

        for lang, text in text_grouped.iteritems():
            spath = p.fname.split(os.path.sep)
            langs.append(lang)

            if lang == "en":
                filename = re.sub(MKD_PATT, "%s\g<0>" % "", p.fname).split(os.path.sep)[-1]
            else:
                filename = re.sub(MKD_PATT, ".%s\g<0>" % lang, p.fname).split(os.path.sep)[-1]

            vp = Page(filename, virtual=text)
            # Copy real page attributes to the virtual page
            for attr in p:
                if not vp.has_key(attr):
                    vp[attr] = p[attr]
            # Define a title in the proper language
            vp["title"] = p["title_%s" % lang] \
                                    if p.has_key("title_%s" % lang) \
                                    else p["title"]
            # Keep track of the current lang of the virtual page
            vp["lang"] = lang
            # Fix post name if exists
            if vp.has_key("post"):
                if lang == "en":
                    vp["post"] = vp["post"][:]
                else:
                    vp["post"] = vp["post"][:-len(lang) - 1]
            page_vpages[lang] = vp

        # Each virtual page has to know about its sister vpages
        for lang, vpage in page_vpages.iteritems():
            vpage["lang_links"] = dict([(l, v["url"]) for l, v in page_vpages.iteritems()])
            vpage["other_lang"] = langs # set other langs and link

        vpages += page_vpages.values()

    pages[:] = vpages



_COMPAT = """        case "%s":
            $loc = "%s/%s";
            break;
"""

_COMPAT_404 = """        default:
            $loc = "%s";
            break;
"""

def hook_preconvert_compat():
    fp = open(os.path.join(options.project, "output", "index.php"), 'w')
    fp.write("<?\n")
    fp.write("// Auto generated xyCMS compatibility index.php\n")
    fp.write("$loc = 'https://www.xythobuz.de/index.de.html';\n")
    fp.write("if (isset($_GET['p'])) {\n")
    fp.write("    if (isset($_GET['lang'])) {\n")
    fp.write("        $_GET['p'] .= 'EN';\n")
    fp.write("    }\n")
    fp.write("    switch($_GET['p']) {\n")
    for p in pages:
        if p.get("compat", "") != "":
            tmp = p["compat"]
            if p.get("lang", DEFAULT_LANG) == DEFAULT_LANG:
                tmp = tmp + "EN"
            fp.write(_COMPAT % (tmp, "https://www.xythobuz.de", p.url))
            fp.write("\n")
    fp.write(_COMPAT_404 % "/404.html")
    fp.write("    }\n")
    fp.write("}\n")
    fp.write("if ($_SERVER['SERVER_PROTOCOL'] == 'HTTP/1.1') {\n")
    fp.write("    if (php_sapi_name() == 'cgi') {\n")
    fp.write("        header('Status: 301 Moved Permanently');\n")
    fp.write("    } else {\n")
    fp.write("        header('HTTP/1.1 301 Moved Permanently');\n")
    fp.write("    }\n")
    fp.write("}\n");
    fp.write("header('Location: '.$loc);\n")
    fp.write("?>")
    fp.close()



_SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</urlset>
"""

_SITEMAP_URL = """
<url>
    <loc>%s/%s</loc>
    <lastmod>%s</lastmod>
    <changefreq>%s</changefreq>
    <priority>%s</priority>
</url>
"""

def hook_preconvert_sitemap():
    date = datetime.strftime(datetime.now(), "%Y-%m-%d")
    urls = []
    for p in pages:
        urls.append(_SITEMAP_URL % (BASE_URL, p.url, date, p.get("changefreq", "monthly"), p.get("priority", "0.5")))
    fname = os.path.join(options.project, "output", "sitemap.xml")
    fp = open(fname, 'w')
    fp.write(_SITEMAP % "".join(urls))
    fp.close()


# -----------------------------------------------------------------------------
# postconvert hooks
# -----------------------------------------------------------------------------

_RSS = """<?xml version="1.0"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>%s</title>
<link>%s</link>
<atom:link href="%s" rel="self" type="application/rss+xml" />
<description>%s</description>
<language>en-us</language>
<pubDate>%s</pubDate>
<lastBuildDate>%s</lastBuildDate>
<docs>http://blogs.law.harvard.edu/tech/rss</docs>
<generator>Poole</generator>
%s
</channel>
</rss>
"""

_RSS_ITEM = """
<item>
    <title>%s</title>
    <link>%s</link>
    <description>%s</description>
    <pubDate>%s</pubDate>
    <guid>%s</guid>
</item>
"""

def hook_postconvert_rss():
    items = []
    posts = [p for p in pages if "date" in p]
    posts.sort(key=lambda p: p.date, reverse=True)
    posts = posts[:10]
    for p in posts:
        title = p.title
        if "post" in p:
            title = p.post
        link = "%s/%s" % (BASE_URL, p.url)
        desc = p.html.replace("href=\"img", "%s%s%s" % ("href=\"", BASE_URL, "/img"))
        desc = desc.replace("src=\"img", "%s%s%s" % ("src=\"", BASE_URL, "/img"))
        desc = desc.replace("href=\"/img", "%s%s%s" % ("href=\"", BASE_URL, "/img"))
        desc = desc.replace("src=\"/img", "%s%s%s" % ("src=\"", BASE_URL, "/img"))
        desc = htmlspecialchars(desc)
        date = time.mktime(time.strptime("%s 12" % p.date, "%Y-%m-%d %H"))
        date = email.utils.formatdate(date)
        items.append(_RSS_ITEM % (title, link, desc, date, link))

    items = "".join(items)

    title = "xythobuz.de Blog"
    link = "%s" % BASE_URL
    feed = "%s/rss.xml" % BASE_URL
    desc = htmlspecialchars("xythobuz Electronics & Software Projects")
    date = email.utils.formatdate()

    rss = _RSS % (title, link, feed, desc, date, date, items)

    fp = codecs.open(os.path.join(output, "rss.xml"), "w", "utf-8")
    fp.write(rss)
    fp.close()

_COMPAT_MOB = """        case "%s":
            $loc = "%s/%s";
            break;
"""

_COMPAT_404_MOB = """        default:
            $loc = "%s";
            break;
"""

def hook_postconvert_mobilecompat():
    directory = os.path.join(output, "mobile")
    if not os.path.exists(directory):
        os.makedirs(directory)
    fp = codecs.open(os.path.join(directory, "index.php"), "w", "utf-8")
    fp.write("<?\n")
    fp.write("// Auto generated xyCMS compatibility mobile/index.php\n")
    fp.write("$loc = 'https://www.xythobuz.de/index.de.html';\n")
    fp.write("if (isset($_GET['p'])) {\n")
    fp.write("    if (isset($_GET['lang'])) {\n")
    fp.write("        $_GET['p'] .= 'EN';\n")
    fp.write("    }\n")
    fp.write("    switch($_GET['p']) {\n")
    for p in pages:
        if p.get("compat", "") != "":
            tmp = p["compat"]
            if p.get("lang", DEFAULT_LANG) == DEFAULT_LANG:
                tmp = tmp + "EN"
            fp.write(_COMPAT_MOB % (tmp, "https://www.xythobuz.de", re.sub(".html", ".html", p.url)))
            fp.write("\n")
    fp.write(_COMPAT_404_MOB % "/404.mob.html")
    fp.write("    }\n")
    fp.write("}\n")
    fp.write("if ($_SERVER['SERVER_PROTOCOL'] == 'HTTP/1.1') {\n")
    fp.write("    if (php_sapi_name() == 'cgi') {\n")
    fp.write("        header('Status: 301 Moved Permanently');\n")
    fp.write("    } else {\n")
    fp.write("        header('HTTP/1.1 301 Moved Permanently');\n")
    fp.write("    }\n")
    fp.write("}\n");
    fp.write("header('Location: '.$loc);\n")
    fp.write("?>")
    fp.close()

def hook_postconvert_size():
    file_ext = '|'.join(['pdf', 'zip', 'rar', 'ods', 'odt', 'odp', 'doc', 'xls', 'ppt', 'docx', 'xlsx', 'pptx', 'exe', 'brd', 'mp3', 'mp4', 'plist'])
    def matched_link(matchobj):
        try:
            path = matchobj.group(1)
            if path.startswith("http") or path.startswith("//") or path.startswith("ftp"):
                return '<a href=\"%s\">%s</a>' % (matchobj.group(1), matchobj.group(3))
            elif path.startswith("/"):
                path = path.strip("/")
            path = os.path.join("static/", path)
            size = os.path.getsize(path)
            if size >= (1024 * 1024):
                return  "<a href=\"%s\">%s</a>&nbsp;(%.1f MiB)" % (matchobj.group(1), matchobj.group(3), size / (1024.0 * 1024.0))
            elif size >= 1024:
                return  "<a href=\"%s\">%s</a>&nbsp;(%d KiB)" % (matchobj.group(1), matchobj.group(3), size // 1024)
            else:
                return  "<a href=\"%s\">%s</a>&nbsp;(%d Byte)" % (matchobj.group(1), matchobj.group(3), size)
        except:
            print "Unable to estimate file size for %s" % matchobj.group(1)
            return '<a href=\"%s\">%s</a>' % (matchobj.group(1), matchobj.group(3))
    _re_url = '<a href=\"([^\"]*?\.(%s))\">(.*?)<\/a>' % file_ext
    for p in pages:
        p.html = re.sub(_re_url, matched_link, p.html)
