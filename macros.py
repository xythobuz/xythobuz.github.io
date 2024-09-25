# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import re
import itertools
import email.utils
import os.path
import time
import codecs
from datetime import datetime

# -----------------------------------------------------------------------------
# Python 2/3 hacks
# -----------------------------------------------------------------------------

PY3 = sys.version_info[0] == 3

if PY3:
    import urllib
    import urllib.request
    def urlparse_foo(link):
        return urllib.parse.parse_qs(urllib.parse.urlparse(link).query)['v'][0]
else:
    import urllib
    import urlparse
    def urlparse_foo(link):
        return urlparse.parse_qs(urlparse.urlparse(link).query)['v'][0]

# -----------------------------------------------------------------------------
# config "system"
# -----------------------------------------------------------------------------

conf = {
    "default_lang": "en",
    "base_url": "https://www.xythobuz.de",

    "birthday": datetime(1994, 1, 22, 0, 0),
    "blog_years_back": 6,
}

def get_conf(name):
    return conf[name]

# -----------------------------------------------------------------------------
# local vars for compatibility
# -----------------------------------------------------------------------------

DEFAULT_LANG = get_conf("default_lang")
BASE_URL = get_conf("base_url")

# -----------------------------------------------------------------------------
# birthday calculation
# -----------------------------------------------------------------------------

from datetime import timedelta
from calendar import isleap

size_of_day = 1. / 366.
size_of_second = size_of_day / (24. * 60. * 60.)

def date_as_float(dt):
    days_from_jan1 = dt - datetime(dt.year, 1, 1)
    if not isleap(dt.year) and days_from_jan1.days >= 31+28:
        days_from_jan1 += timedelta(1)
    return dt.year + days_from_jan1.days * size_of_day + days_from_jan1.seconds * size_of_second

def difference_in_years(start_date, end_date):
    return int(date_as_float(end_date) - date_as_float(start_date))

def own_age():
    return difference_in_years(get_conf("birthday"), datetime.now())

# -----------------------------------------------------------------------------
# sub page helper macro
# -----------------------------------------------------------------------------

def backToParent():
    # check for special parent cases
    posts = []
    if page.get("show_in_quadcopters", "false") == "true":
        posts = [p for p in pages if p.url == "quadcopters.html"]

    # if not, check for actual parent
    if len(posts) == 0:
        url = page.get("parent", "") + ".html"
        posts = [p for p in pages if p.url == url]

    # print if any parent link found
    if len(posts) > 0:
        p = posts[0]
        print('<span class="listdesc">[...back to ' + p.title + ' overview](' + p.url + ')</span>')

# -----------------------------------------------------------------------------
# table helper macro
# -----------------------------------------------------------------------------

def tableHelper(style, header, content):
    print("<table>")
    if (header != None) and (len(header) == len(style)):
        print("<tr>")
        for h in header:
            print("<th>" + h + "</th>")
        print("</tr>")
    for ci in range(0, len(content)):
        if len(content[ci]) != len(style):
            # invalid call of table helper!
            continue
        print("<tr>")
        for i in range(0, len(style)):
            s = style[i]
            td_style = ""

            if "monospaced" in s:
                td_style += " font-family: monospace;"

            if "align-last-right" in s:
                if ci == (len(content) - 1):
                    td_style += " text-align: right;"
                else:
                    if "align-center" in s:
                        td_style += " text-align: center;"
            elif "align-right" in s:
                td_style += " text-align: right;"
            elif "align-center" in s:
                td_style += " text-align: center;"

            td_args = ""
            if td_style != "":
                td_args = " style=\"" + td_style + "\""

            print("<td" + td_args + ">")

            if isinstance(content[ci][i], tuple):
                text, link = content[ci][i]
                print("<a href=\"" + link + "\">" + text + "</a>")
            else:
                text = content[ci][i]
                print(text)
            print("</td>")
        print("</tr>")
    print("</table>")

# -----------------------------------------------------------------------------
# menu helper macro
# -----------------------------------------------------------------------------

def githubCommitBadge(p, showInline = False):
    ret = ""
    if p.get("github", "") != "":
        link = p.get("git", p.github)
        linkParts = p.github.split("/")
        if len(linkParts) >= 5:
            ret += "<a href=\"" + link + "\"><img "
            if showInline:
                ret += "style =\"vertical-align: middle; padding-bottom: 0.25em;\" "
            ret += "src=\"https://img.shields.io/github/last-commit/"
            ret += linkParts[3] + "/" + linkParts[4]
            ret += ".svg?logo=git&style=flat\" /></a>"
    return ret

def printMenuItem(p, yearsAsHeading = False, showDateSpan = False, showOnlyStartDate = False, nicelyFormatFullDate = False, lastyear = "0", lang = "", showLastCommit = True, hide_description = False, indent_count = 0, updates_as_heading = False):
    title = p.title
    if lang != "":
        if p.get("title_" + lang, "") != "":
            title = p.get("title_" + lang, "")
    if title == "Blog":
        title = p.post

    if updates_as_heading:
        year = p.get("update", p.get("date", ""))[0:4]
    else:
        year = p.get("date", "")[0:4]
    if year != lastyear:
        lastyear = year
        if yearsAsHeading:
            print("\n\n#### %s\n" % (year))

    dateto = ""
    if p.get("date", "" != ""):
        year = p.get("date", "")[0:4]
        if showOnlyStartDate:
            dateto = " (%s)" % (year)

        if p.get("update", "") != "" and p.get("update", "")[0:4] != year:
            if showDateSpan:
                dateto = " (%s - %s)" % (year, p.get("update", "")[0:4])

        if nicelyFormatFullDate:
            dateto = " - " + datetime.strptime(p.get("update", p.date), "%Y-%m-%d").strftime("%B %d, %Y")

    indent = "  " * (indent_count + 1)
    print(indent + "* **[%s](%s)**%s" % (title, p.url, dateto))

    if hide_description == False:
        if p.get("description", "") != "":
            description = p.get("description", "")
            if lang != "":
                if p.get("description_" + lang, "") != "":
                    description = p.get("description_" + lang, "")
            print("<br><span class=\"listdesc\">" + description + "</span>")

    if showLastCommit:
        link = githubCommitBadge(p)
        if len(link) > 0:
            print("<br>" + link)

    return lastyear

def printRecentMenu(count = 5):
    posts = [p for p in pages if "date" in p and p.lang == "en"]
    posts.sort(key=lambda p: p.get("update", p.get("date")), reverse=True)

    if count > 0:
        posts = posts[0:count]

    lastyear = "0"
    for p in posts:
        lastyear = printMenuItem(p, count == 0, False, False, True, lastyear, "", False, False, 0, True)

def printBlogMenu(year_min=None, year_max=None):
    posts = [p for p in pages if "post" in p and p.lang == "en"]
    posts.sort(key=lambda p: p.get("date", "9999-01-01"), reverse=True)

    if year_min != None:
        posts = [p for p in posts if int(p.get("date", "9999-01-01")[0:4]) >= int(year_min)]
    if year_max != None:
        posts = [p for p in posts if int(p.get("date", "9999-01-01")[0:4]) <= int(year_max)]

    lastyear = "0"
    for p in posts:
        lastyear = printMenuItem(p, True, False, False, True, lastyear)

def printProjectsMenu():
    # prints all pages with parent 'projects' or 'stuff'.
    # first the ones without date, sorted by position.
    # this first section includes sub-headings for children
    # then afterwards those with date, split by year.
    # also supports blog posts with parent.
    enpages = [p for p in pages if p.lang == "en"]

    # select pages without date
    dpages = [p for p in enpages if p.get("date", "") == ""]
    # only those that have a parent in ['projects', 'stuff']
    mpages = [p for p in dpages if any(x in p.get("parent", "") for x in [ 'projects', 'stuff' ])]
    # sort by position
    mpages.sort(key=lambda p: [int(p.get("position", "999"))])
    # print all pages
    for p in mpages:
        printMenuItem(p)

        # print subpages for these top-level items
        subpages = [sub for sub in enpages if sub.get("parent", "none") == p.get("child-id", "unknown")]
        for sp in subpages:
            printMenuItem(sp, False, True, True, False, "0", "", False, True, 1)

    # slect pages with a date
    dpages = [p for p in enpages if p.get("date", "") != ""]
    # only those that have a parent in ['projects', 'stuff']
    mpages = [p for p in dpages if any(x in p.get("parent", "") for x in [ 'projects', 'stuff' ])]
    # sort by date
    mpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)

    # print all pages
    lastyear = "0"
    for p in mpages:
        lastyear = printMenuItem(p, True, True, False, False, lastyear)

        # print subpages for these top-level items
        subpages = [sub for sub in enpages if sub.get("parent", "none") == p.get("child-id", "unknown")]
        subpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)
        for sp in subpages:
            printMenuItem(sp, False, True, True, False, "0", "", False, True, 1)

def print3DPrintingMenu():
    mpages = [p for p in pages if p.get("parent", "") == "3d-printing" and p.lang == "en"]
    mpages.sort(key=lambda p: int(p["position"]))
    for p in mpages:
        printMenuItem(p, False, True, True)

def printInputDevicesMenu():
    mpages = [p for p in pages if p.get("parent", "") == "input_devices" and p.lang == "en"]
    mpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)
    for p in mpages:
        printMenuItem(p, False, True, True)

def printInputDevicesRelatedMenu():
    mpages = [p for p in pages if p.get("show_in_input_devices", "false") == "true"]
    mpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)
    for p in mpages:
        printMenuItem(p, False, True, True)

def printSmarthomeMenu():
    mpages = [p for p in pages if p.get("parent", "") == "smarthome" and p.lang == "en"]
    mpages.sort(key=lambda p: int(p["position"]))
    for p in mpages:
        printMenuItem(p, False, True, True)

def printQuadcopterMenu():
    mpages = [p for p in pages if p.get("parent", "") == "quadcopters" and p.lang == "en"]
    mpages.sort(key=lambda p: int(p["position"]))
    for p in mpages:
        printMenuItem(p, False, True, True)

def printQuadcopterRelatedMenu():
    mpages = [p for p in pages if p.get("show_in_quadcopters", "false") == "true"]
    mpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)
    for p in mpages:
        printMenuItem(p, False, True, True)

def printRobotMenuEnglish():
    mpages = [p for p in pages if p.get("parent", "") == "xyrobot" and p.lang == "en"]
    mpages.sort(key=lambda p: int(p["position"]))
    for p in mpages:
        printMenuItem(p)

def printRobotMenuDeutsch():
    mpages = [p for p in pages if p.get("parent", "") == "xyrobot" and p.lang == "de"]
    mpages.sort(key=lambda p: int(p["position"]))
    for p in mpages:
        printMenuItem(p, False, False, False, False, "0", "de")

def printSteamMenuEnglish():
    mpages = [p for p in pages if p.get("parent", "") == "steam" and p.lang == "en"]
    mpages.sort(key=lambda p: [p.get("date", "9999-01-01")], reverse = True)
    for p in mpages:
        printMenuItem(p, False, False, False, True)

def printSteamMenuDeutsch():
    # TODO show german pages, or english pages when german not available
    printSteamMenuEnglish()

# -----------------------------------------------------------------------------
# lightgallery helper macro
# -----------------------------------------------------------------------------

# call this macro like this:

# lightgallery([
#     [ "image-link", "description" ],
#     [ "image-link", "thumbnail-link", "description" ],
#     [ "youtube-link", "thumbnail-link", "description" ],
#     [ "video-link", "mime", "thumbnail-link", "image-link", "description" ],
#     [ "video-link", "mime", "", "", "description" ],
# ])

# it will also auto-generate thumbnails and resize and strip EXIF from images
# using the included web-image-resize script.
# and it can generate video thumbnails and posters with the video-thumb script.

def lightgallery_check_thumbnail(link, thumb):
    # only check local image links
    if not link.startswith('img/'):
        return

    # generate thumbnail filename web-image-resize will create
    x = link.rfind('.')
    img = link[:x] + '_small' + link[x:]

    # only run when desired thumb path matches calculated ones
    if thumb != img:
        return

    # generate fs path to images
    path = os.path.join(os.getcwd(), 'static', link)
    img = os.path.join(os.getcwd(), 'static', thumb)

    # no need to generate thumb again
    if os.path.exists(img):
        return

    # run web-image-resize to generate thumbnail
    script = os.path.join(os.getcwd(), 'web-image-resize')
    os.system(script + ' ' + path)

def lightgallery_check_thumbnail_video(link, thumb, poster):
    # only check local image links
    if not link.startswith('img/'):
        return

    # generate thumbnail filenames video-thumb will create
    x = link.rfind('.')
    thumb_l = link[:x] + '_thumb.png'
    poster_l = link[:x] + '_poster.png'

    # only run when desired thumb path matches calculated ones
    if (thumb_l != thumb) or (poster_l != poster):
        return

    # generate fs path to images
    path = os.path.join(os.getcwd(), 'static', link)
    thumb_p = os.path.join(os.getcwd(), 'static', thumb)
    poster_p = os.path.join(os.getcwd(), 'static', poster)

    # no need to generate thumb again
    if os.path.exists(thumb_p) or os.path.exists(poster_p):
        return

    # run video-thumb to generate thumbnail
    script = os.path.join(os.getcwd(), 'video-thumb')
    os.system(script + ' ' + path)

def lightgallery(links):
    global v_ii
    try:
        v_ii += 1
    except NameError:
        v_ii = 0

    videos = [l for l in links if len(l) == 5]
    v_i = -1
    for v in videos:
        link, mime, thumb, poster, alt = v
        v_i += 1
        print('<div style="display:none;" id="video' + str(v_i) + '_' + str(v_ii) + '">')
        print('<video class="lg-video-object lg-html5" controls preload="none">')
        print('<source src="' + link + '" type="' + mime + '">')
        print('<a href="' + link + '">' + alt + '</a>')
        print('</video>')
        print('</div>')
        
    print('<div class="lightgallery">')
    v_i = -1
    for l in links:
        if (len(l) == 3) or (len(l) == 2):
            link = img = alt = ""
            style = img2 = ""
            if len(l) == 3:
                link, img, alt = l
            else:
                link, alt = l
                if "youtube.com" in link:
                    img = "https://img.youtube.com/vi/"
                    img += urlparse_foo(link)
                    img += "/0.jpg" # full size preview
                    #img += "/default.jpg" # default thumbnail
                    style = ' style="width:300px;"'
                    img2 = '<img src="lg/video-play.png" class="picthumb">'
                else:
                    x = link.rfind('.')
                    img = link[:x] + '_small' + link[x:]
            lightgallery_check_thumbnail(link, img)
            print('<div class="border" style="position:relative;" data-src="' + link + '"><a href="' + link + '"><img class="pic" src="' + img + '" alt="' + alt + '"' + style + '>' + img2 + '</a></div>')
        elif len(l) == 5:
            v_i += 1
            link, mime, thumb, poster, alt = videos[v_i]
            if len(thumb) <= 0:
                x = link.rfind('.')
                thumb = link[:x] + '_thumb.png'
            if len(poster) <= 0:
                x = link.rfind('.')
                poster = link[:x] + '_poster.png'
            lightgallery_check_thumbnail_video(link, thumb, poster)
            print('<div class="border" data-poster="' + poster + '" data-sub-html="' + alt + '" data-html="#video' + str(v_i) + '_' + str(v_ii) + '"><a href="' + link + '"><img class="pic" src="' + thumb + '"></a></div>')
        else:
            raise NameError('Invalid number of arguments for lightgallery')
    print('</div>')

# -----------------------------------------------------------------------------
# github helper macros
# -----------------------------------------------------------------------------

import json, sys

def restRequest(url):
    response = urllib.request.urlopen(url) if PY3 else urllib.urlopen(url)
    if response.getcode() != 200:
        sys.stderr.write("\n")
        sys.stderr.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        sys.stderr.write("!!!!!!!                  WARNING                 !!!!!\n")
        sys.stderr.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        sys.stderr.write("invalid response code: " + str(response.getcode()) + "\n")
        sys.stderr.write("url: \"" + url + "\"\n")
        sys.stderr.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        sys.stderr.write("!!!!!!!                  WARNING                 !!!!!\n")
        sys.stderr.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        sys.stderr.write("\n")
        return ""
    data = json.loads(response.read().decode("utf-8"))
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

def include_url(url):
    response = urllib.request.urlopen(url) if PY3 else urllib.urlopen(url)
    if response.getcode() != 200:
        raise Exception("invalid response code", response.getcode())
    data = response.read().decode("utf-8")
    print(data, end="")

# -----------------------------------------------------------------------------
# preconvert hooks
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# multi language support
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

        for lang, text in (iter(text_grouped.items()) if PY3 else text_grouped.iteritems()):
            spath = p.fname.split(os.path.sep)
            langs.append(lang)

            if lang == "en":
                filename = re.sub(MKD_PATT, r"%s\g<0>" % "", p.fname).split(os.path.sep)[-1]
            else:
                filename = re.sub(MKD_PATT, r".%s\g<0>" % lang, p.fname).split(os.path.sep)[-1]

            vp = Page(filename, virtual=text)
            # Copy real page attributes to the virtual page
            for attr in p:
                if not ((attr in vp) if PY3 else vp.has_key(attr)):
                    vp[attr] = p[attr]
            # Define a title in the proper language
            vp["title"] = p["title_%s" % lang] \
                                    if ((("title_%s" % lang) in p) if PY3 else p.has_key("title_%s" % lang)) \
                                    else p["title"]
            # Keep track of the current lang of the virtual page
            vp["lang"] = lang
            page_vpages[lang] = vp

        # Each virtual page has to know about its sister vpages
        for lang, vpage in (iter(page_vpages.items()) if PY3 else page_vpages.iteritems()):
            vpage["lang_links"] = dict([(l, v["url"]) for l, v in (iter(page_vpages.items()) if PY3 else page_vpages.iteritems())])
            vpage["other_lang"] = langs # set other langs and link

        vpages += page_vpages.values()

    pages[:] = vpages

# -----------------------------------------------------------------------------
# compatibility redirect for old website URLs
# -----------------------------------------------------------------------------

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
    fp.write("$loc = '" + get_conf("base_url") + "/index.de.html';\n")
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
            fp.write(_COMPAT % (tmp, get_conf("base_url"), p.url))
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

# -----------------------------------------------------------------------------
# sitemap generation
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# rss feed generation
# -----------------------------------------------------------------------------

_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="%s" type="text/xsl"?>
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
<ttl>720</ttl>
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
    <atom:updated>%s</atom:updated>
    <guid>%s</guid>
</item>
"""

def hook_postconvert_rss():
    items = []

    # all pages with "date" get put into feed
    posts = [p for p in pages if "date" in p]

    # sort by update if available, date else
    posts.sort(key=lambda p: p.get("update", p.date), reverse=True)

    # only put 20 most recent items in feed
    posts = posts[:20]

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

        update = time.mktime(time.strptime("%s 12" % p.get("update", p.date), "%Y-%m-%d %H"))
        update = email.utils.formatdate(update)

        items.append(_RSS_ITEM % (title, link, desc, date, update, link))

    items = "".join(items)

    style = "/css/rss.xsl"
    title = "xythobuz.de Blog"
    link = "%s" % BASE_URL
    feed = "%s/rss.xml" % BASE_URL
    desc = htmlspecialchars("xythobuz Electronics & Software Projects")
    date = email.utils.formatdate()

    rss = _RSS % (style, title, link, feed, desc, date, date, items)

    fp = codecs.open(os.path.join(output, "rss.xml"), "w", "utf-8")
    fp.write(rss)
    fp.close()

# -----------------------------------------------------------------------------
# compatibility redirect for old mobile pages
# -----------------------------------------------------------------------------

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
    fp.write("$loc = '" + get_conf("base_url") + "/index.de.html';\n")
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
            fp.write(_COMPAT_MOB % (tmp, get_conf("base_url"), re.sub(".html", ".html", p.url)))
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

# -----------------------------------------------------------------------------
# displaying filesize for download links
# -----------------------------------------------------------------------------

def hook_postconvert_size():
    file_ext = '|'.join(['pdf', 'zip', 'rar', 'ods', 'odt', 'odp', 'doc', 'xls', 'ppt', 'docx', 'xlsx', 'pptx', 'exe', 'brd', 'plist'])
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
            print("Unable to estimate file size for %s" % matchobj.group(1))
            return '<a href=\"%s\">%s</a>' % (matchobj.group(1), matchobj.group(3))
    _re_url = r'<a href=\"([^\"]*?\.(%s))\">(.*?)<\/a>' % file_ext
    for p in pages:
        p.html = re.sub(_re_url, matched_link, p.html)
