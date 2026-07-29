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
import json
from subprocess import check_output

def print_cnsl_error(s, url = None):
    sys.stderr.write("\n")
    sys.stderr.write("warning: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    sys.stderr.write("warning: !!!!!!!                  WARNING                 !!!!!\n")
    sys.stderr.write("warning: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    sys.stderr.write("warning: " + s + "\n")
    if url != None:
        sys.stderr.write("warning: URL: \"" + url + "\"\n")
    sys.stderr.write("warning: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    sys.stderr.write("warning: !!!!!!!                  WARNING                 !!!!!\n")
    sys.stderr.write("warning: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    sys.stderr.write("\n")

# -----------------------------------------------------------------------------
# Python 2/3 hacks
# -----------------------------------------------------------------------------

PY3 = sys.version_info[0] == 3

if PY3:
    import urllib
    import urllib.request
    import urllib.parse
    from urllib.error import HTTPError, URLError

    def urlparse_queryparam(link, param='v'):
        return urllib.parse.parse_qs(urllib.parse.urlparse(link).query)[param][0]

    def urlparse_path(link):
        return urllib.parse.urlparse(link).path

    def url_escape(link):
        return urllib.parse.quote_plus(link)
else:
    import urllib
    import urlparse

    def urlparse_queryparam(link, param='v'):
        return urlparse.parse_qs(urlparse.urlparse(link).query)[param][0]

    def urlparse_path(link):
        return urlparse.urlparse(link).path

    def url_escape(link):
        return urllib.quote_plus(link)

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
# JavaScript licensing
# -----------------------------------------------------------------------------

# https://www.gnu.org/software/librejs/free-your-javascript.html

# example:
# librejs_helper([
#     [ "/js/jquery-2.1.1.min.js", LICENSE ], # for canonical == minified
#     [ "/js/jquery-2.1.1.min.js", LICENSE, "/js/jquery-2.1.1.js" ], # for canonical != minified
# ])
#
# LICENSE can be (name, url) tuple or a pre-defined license.
# only use from this list https://www.gnu.org/software/librejs/manual/html_node/Setting-Your-JavaScript-Free.html#License-tags
#
#   "gpl" or "gpl3"
#   "expat" or "mit"

known_licenses = [
    [ [ "gpl", "gpl3" ], "GNU-GPL-3.0-or-later", "http://www.gnu.org/licenses/gpl-3.0.html" ],
    [ [ "expat", "mit" ], "Expat (MIT)", "http://www.jclark.com/xml/copying.txt" ],
]

def get_known_license(license):
    for l in known_licenses:
        if type(l[0]) == str:
            if license.lower() == l[0].lower():
                return l[1:]
        else:
            for lic in l[0]:
                if license.lower() == lic.lower():
                    return l[1:]
    raise ValueError("unknown license type")

def librejs_helper(modules):
    print('<table id="jslicense-labels1">')
    for m in modules:
        print('<tr>')

        if len(m) == 2:
            minified, license = m
            canonical = minified
        elif len(m) == 3:
            minified, license, canonical = m
        else:
            raise ValueError("invalid number of arguments")

        if type(license) == str:
            license = get_known_license(license)

        minified = [ urlparse_path(minified).split('/')[-1], minified ]
        canonical = [ urlparse_path(canonical).split('/')[-1], canonical ]

        for n in [ minified, license, canonical ]:
            name, link = n
            print('<td><a href="' + link + '">' + name + '</a></td>')

        print('</tr>')
    print('</table>')

# -----------------------------------------------------------------------------
# birthday calculation and other date stuff
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
    age_dec = difference_in_years(get_conf("birthday"), datetime.now())
    age_hex = '0x%X' % age_dec
    return '<abbr title="' + str(age_dec) + '">' + str(age_hex) + '</abbr>'

def page_to_datetime(date):
    if date == None:
        return (None, False)

    padded_date = date + " 12:00:00"
    try:
        date_has_time = False
        dt = datetime.strptime(padded_date, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        date_has_time = True
        dt = datetime.strptime(padded_date[:-9], "%Y-%m-%d %H:%M:%S")
    return (dt, date_has_time)

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
        if len(content[ci]) < len(style):
            # invalid call of table helper!
            print_cnsl_error("invalid table: " + str(len(content[ci])) + "[" + str(ci) + "] != " + str(len(style)))
            continue

        if len(content[ci]) > len(style):
            print("<tr " + content[ci][len(style)] + ">")
        else:
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
            ret += ".svg?logo=git&style=flat\" alt=\"GitHub commit badge\"></a>"
    return ret

def printMenuItem(p, yearsAsHeading = False, showDateSpan = False, showOnlyStartDate = False, nicelyFormatFullDate = False, lastyear = "0", lang = "", showLastCommit = True, hide_description = False, updates_as_heading = False, desc_has_collapse = False):
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
            print("<li class=\"yearheading\">" + str(year) + "</li>")

    dateto = ""
    if p.get("date", "" != ""):
        year = p.get("date", "")[0:4]
        if showOnlyStartDate:
            dateto = " (%s)" % (year)

        if p.get("update", "") != "" and p.get("update", "")[0:4] != year:
            if showDateSpan:
                dateto = " (%s - %s)" % (year, p.get("update", "")[0:4])

        if nicelyFormatFullDate:
            dt, date_has_time = page_to_datetime(p.get("update", p.date))
            dateto = " - " + dt.strftime("%B %d, %Y")

    print("<li>")
    print("<a href=\"" + p.url + "\"><b>" + title + "</b></a>" + dateto)

    if hide_description == False:
        if p.get("description", "") != "":
            description = p.get("description", "")
            if lang != "":
                description = p.get("description_" + lang, description)
            if desc_has_collapse:
                print("<br><span class=\"listdesc collapse_menu\">" + description + "</span>")
            else:
                print("<br><span class=\"listdesc\">" + description + "</span>")

    # TODO can not show commit badge when it is a parent page with collapsable description
    if showLastCommit and not desc_has_collapse:
        link = githubCommitBadge(p)
        if len(link) > 0:
            print("<br>" + link)

    if not desc_has_collapse:
        print("</li>")

    return lastyear

# https://stackoverflow.com/a/56842689
class SortReversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj

def printRecentMenu(count = 5):
    posts = [p for p in pages if "date" in p and p.ordinal == 0]
    posts.sort(key=lambda p: [ SortReversor(p.get("update", p.get("date"))), p["title"] ])

    if count > 0:
        posts = posts[0:count]

    print("<ul class='menulist'>")

    lastyear = "0"
    for p in posts:
        lastyear = printMenuItem(p, count == 0, False, False, True, lastyear, "", False, False, True)

    print("</ul>")

def printBlogMenu(year_min=None, year_max=None):
    posts = [p for p in pages if "post" in p and p.ordinal == 0]
    posts.sort(key=lambda p: [ SortReversor(p.get("date", "9999-01-01")), p["title"] ])

    if year_min != None:
        posts = [p for p in posts if int(p.get("date", "9999-01-01")[0:4]) >= int(year_min)]
    if year_max != None:
        posts = [p for p in posts if int(p.get("date", "9999-01-01")[0:4]) <= int(year_max)]

    print("<ul class='menulist'>")

    lastyear = "0"
    for p in posts:
        lastyear = printMenuItem(p, True, False, False, True, lastyear)

    print("</ul>")

def printProjectsMenu():
    # prints all pages with parent or second_parent 'projects' or 'stuff'.
    # first the ones without date, sorted by position.
    # this first section includes sub-headings for children
    # in a hidden div, expanding when clicking the description.
    # then afterwards those with date, split by year.
    # also supports blog posts with parent.
    enpages = [p for p in pages if p.ordinal == 0]

    # select pages without date
    dpages = [p for p in enpages if p.get("date", "") == ""]
    # only those that have a parent in ['projects', 'stuff']
    mpages = [p for p in dpages if any((x in p.get("parent", "")) or (x in p.get("second_parent", "")) for x in [ 'projects', 'stuff' ])]
    # sort by position
    mpages.sort(key=lambda p: [ int(p.get("position", "999")), p["title"] ])

    print("<ul class='menulist'>")

    # print all pages
    for p in mpages:
        # fetch subpages for these top-level items
        subpages = [sub for sub in enpages if sub.get("parent", "none") == p.get("child-id", "unknown")]
        order = p.get("sort-order", "date")
        if order == "position":
            subpages.sort(key=lambda p: [ p["position"], p["title"] ])
        else:
            subpages.sort(key=lambda p: [ SortReversor(p.get("date", "9999-01-01")), p["title"] ])

        printMenuItem(p, False, False, False, False, "0", "", True, False, False, len(subpages) > 0)

        # print subpages
        if len(subpages) > 0:
            print("<div class='collapsecontent_menu'>")
            print("<ul>")
            for sp in subpages:
                printMenuItem(sp, False, True, True, False, "0", "", False, True)
            print("</ul>")
            print("</div>")
            print("</li>")

            # manually count because this does not appear in page.source
            if not "collapse" in page["page_flags"]:
                page["page_flags"]["collapse"] = 0
            page["page_flags"]["collapse"] += 1

    # slect pages with a date
    dpages = [p for p in enpages if p.get("date", "") != ""]
    # only those that have a parent in ['projects', 'stuff']
    mpages = [p for p in dpages if any((x in p.get("parent", "")) or (x in p.get("second_parent", "")) for x in [ 'projects', 'stuff' ])]
    # sort by date
    mpages.sort(key=lambda p: [ SortReversor(p.get("date", "9999-01-01")), p["title"] ])

    # print all pages
    lastyear = "0"
    for p in mpages:
        # fetch subpages for these top-level items
        subpages = [sub for sub in enpages if sub.get("parent", "none") == p.get("child-id", "unknown")]
        order = p.get("sort-order", "date")
        if order == "position":
            subpages.sort(key=lambda p: [ p["position"], p["title"] ])
        else:
            subpages.sort(key=lambda p: [ SortReversor(p.get("date", "9999-01-01")), p["title"] ])

        lastyear = printMenuItem(p, True, True, False, False, lastyear, "", True, False, False, len(subpages) > 0)

        # print subpages
        if len(subpages) > 0:
            print("<div class='collapsecontent_menu'>")
            print("<ul>")
            for sp in subpages:
                printMenuItem(sp, False, True, True, False, "0", "", False, True)
            print("</ul>")
            print("</div>")
            print("</li>")

            # manually count because this does not appear in page.source
            if not "collapse" in page["page_flags"]:
                page["page_flags"]["collapse"] = 0
            page["page_flags"]["collapse"] += 1

    print("</ul>")

def printMenuGeneric(mpages = None, sortKey = None):
    if mpages == None:
        mpages = [p for p in pages if p.get("parent", "__none__") == page["child-id"] and p.ordinal == 0]
    if sortKey != None:
        mpages.sort(key = sortKey)

    if len(mpages) > 0:
        print("<ul class='menulist'>")
        for p in mpages:
            printMenuItem(p, False, True, True)
        print("</ul>")

def printMenuDate(mpages = None):
    sortKey = lambda p: [ SortReversor(p.get("date", "9999-01-01")), p["title"] ]
    printMenuGeneric(mpages, sortKey)

def printMenuPositional(mpages = None):
    printMenuGeneric(mpages, lambda p: [ int(p["position"]), p["title"] ])

def printMenu(mpages = None):
    order = page.get("sort-order", "date")
    if order == "position":
        printMenuPositional(mpages)
    else:
        printMenuDate(mpages)

def printRobotMenuEnglish():
    mpages = [p for p in pages if p.get("parent", "") == "xyrobot" and p.lang == "en"]
    mpages.sort(key=lambda p: [ int(p["position"]), p["title"] ])

    print("<ul class='menulist'>")
    for p in mpages:
        printMenuItem(p)
    print("</ul>")

def printRobotMenuDeutsch():
    mpages = [p for p in pages if p.get("parent", "") == "xyrobot" and p.lang == "de"]
    mpages.sort(key=lambda p: [ int(p["position"]), p["title"] ])

    print("<ul class='menulist'>")
    for p in mpages:
        printMenuItem(p, False, False, False, False, "0", "de")
    print("</ul>")

def printSteamMenuEnglish():
    mpages = [p for p in pages if p.get("parent", "") == "steam" and ((p.lang == "en") or (p.ordinal == 0))]
    mpages.sort(key=lambda p: [ SortReversor(p.get("date", "9999-01-01")), p["title"] ])

    print("<ul class='menulist'>")
    for p in mpages:
        printMenuItem(p, False, False, False, True)
    print("</ul>")

def printSteamMenuDeutsch():
    mpages = [p for p in pages if p.get("parent", "") == "steam" and ((p.lang == "de") or (p.ordinal == 0))]
    mpages.sort(key=lambda p: [ SortReversor(p.get("date", "9999-01-01")), p["title"] ])

    print("<ul class='menulist'>")
    for p in mpages:
        printMenuItem(p, False, False, False, True)
    print("</ul>")

# -----------------------------------------------------------------------------
# lightgallery helper macro
# -----------------------------------------------------------------------------

# call this macro like this:

# lightgallery([
#     [ "image-link", "description" ], # 2 elements
#     [ "image-link", "thumbnail-link", "description" ], # 3 elements
#     [ "youtube-link", "thumbnail-link", "description" ], # 3 elements
#     [ "audio-link", "mime", "", "description" ], # 4 elements
#     [ "video-link", "mime", "thumbnail-link", "image-link", "description" ], # 5 elements
#     [ "video-link", "mime", "", "", "description" ], # 5 elements
# ])

# it will also auto-generate thumbnails and resize and strip EXIF from images
# using the included web-image-resize script.
# and it can generate video thumbnails and posters with the video-thumb script.
# also, if possible, image and video dimensions are automatically passed to lightgallery.

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

def query_image_size(link):
    # only check local image links
    if not link.startswith('img/'):
        return None

    try:
        path = os.path.join(os.getcwd(), 'static')
        size = check_output(['identify', '-ping', '-format', '%w %h', link], cwd=path)
        (w, h) = [ t(s) for t, s in zip((int, int), size.split()) ]
        sys.stderr.write(link + " is " + str(w) + "-" + str(h) + "\n")
        return (w, h)
    except Exception:
        return None

def query_video_size(link):
    # only check local image links
    if not link.startswith('img/'):
        return None

    try:
        path = os.path.join(os.getcwd(), 'static')
        size = check_output([os.path.join(os.getcwd(), 'video-get-size'), link], cwd=path)
        (w, h) = [ t(s) for t, s in zip((int, int), size.split()) ]
        sys.stderr.write(link + " is " + str(w) + "-" + str(h) + "\n")
        return (w, h)
    except Exception:
        return None

def get_image_size(link):
    # only check local image links
    if not link.startswith('img/'):
        return None

    try:
        path = os.path.join(os.getcwd(), 'static', link + ".txt")
        with open(path, "r") as f: size = f.read()
        (w, h) = [ t(s) for t, s in zip((int, int), size.split()) ]
        return (w, h)
    except Exception:
        size = query_image_size(link)
        if size != None:
            sys.stderr.write("caching size of " + link + "\n")
            with open(path, "w") as f: f.write("%d %d" % size)
        return size

def get_video_size(link):
    # only check local image links
    if not link.startswith('img/'):
        return None

    try:
        path = os.path.join(os.getcwd(), 'static', link + ".txt")
        with open(path, "r") as f: size = f.read()
        (w, h) = [ t(s) for t, s in zip((int, int), size.split()) ]
        return (w, h)
    except Exception:
        size = query_video_size(link)
        if size != None:
            sys.stderr.write("caching size of " + link + "\n")
            with open(path, "w") as f: f.write("%d %d" % size)
        return size

def lightgallery(links):
    if not "lightgallery" in page["page_flags"]:
        page["page_flags"]["lightgallery"] = 0
    page["page_flags"]["lightgallery"] += 1

    print('<div class="lightgallery_new">')

    for l in links:
        if (len(l) == 3) or (len(l) == 2):
            # image or youtube video
            link = img = alt = ""
            style = img2 = ""
            size_str = ''
            if len(l) == 3:
                link, img, alt = l
                if "youtube.com" in link:
                    img2 = '<img src="img/video-play.png" class="picthumb" alt="Media play button">'
                    size_str += ' style="position:relative;"'
            else:
                link, alt = l
                if "youtube.com" in link:
                    img = "https://img.youtube.com/vi/"
                    img += urlparse_queryparam(link)
                    img += "/0.jpg" # full size preview
                    #img += "/default.jpg" # default thumbnail
                    style = ' style="width:300px;" data-poster="' + img + '"'
                    img2 = '<img src="img/video-play.png" class="picthumb" alt="Media play button">'
                    size_str += ' style="position:relative;"'
                elif link.startswith('img/'):
                    x = link.rfind('.')
                    img = link[:x] + '_small' + link[x:]
                else:
                    img = link
                    style = ' style="max-width:300px;max-height:300px;"'

            lightgallery_check_thumbnail(link, img)

            size = get_image_size(link)
            if size != None:
                size_str += ' data-lg-size="' + str(int(size[0])) + '-' + str(int(size[1])) + '"'

            print('<div class="border" data-src="' + link + '"' + size_str + '><a href="' + link + '"><img class="pic" src="' + img + '" alt="' + alt + '"' + style + '>' + img2 + '</a></div>')
        elif len(l) == 4:
            # audio
            link, mime, none, alt = l

            print('<div class="border" data-src="' + link + '" data-iframe="true">')
            print('<audio controls preload="none" style="display:block;"><source src="' + link + '" type="' + mime + '" >Your browser does not support audio.</audio>')
            print('<p class="audio_text"><a href="' + link + '">Download audio</a></p></div>')
        elif len(l) == 5:
            # HTML5 video
            link, mime, thumb, poster, alt = l
            if len(thumb) <= 0:
                x = link.rfind('.')
                thumb = link[:x] + '_thumb.png'
            if len(poster) <= 0:
                x = link.rfind('.')
                poster = link[:x] + '_poster.png'

            lightgallery_check_thumbnail_video(link, thumb, poster)

            size = get_video_size(link)
            size_str = ''
            if size != None:
                size_str = ' data-lg-size="' + str(int(size[0])) + '-' + str(int(size[1])) + '"'

            video_src = "'" + '{"source": [{"src":"' + link + '", "type":"' + mime + '"}], "attributes": {"preload": false, "playsinline": true, "controls": true}}' + "'"
            print('<div class="border" data-video=' + video_src + size_str + ' data-poster="' + poster + '" data-sub-html="' + alt + '"><a href="' + link + '"><img class="pic" src="' + thumb + '" alt="' + alt + '"></a></div>')
        else:
            raise NameError('Invalid number of arguments for lightgallery')

    print('</div>')

# -----------------------------------------------------------------------------
# github helper macros
# -----------------------------------------------------------------------------

def http_request(url, timeout = 5):
    if PY3:
        response = urllib.request.urlopen(url, timeout = timeout)
    else:
        response = urllib.urlopen(url)

    if response.getcode() != 200:
        raise RuntimeError("invalid response code: " + str(response.getcode()))

    data = response.read().decode("utf-8")
    return data

def include_url(urls, data_slice = None, timeout = 2):
    if len(urls) < 2:
        print_cnsl_error("include_url() without fallback option", urls[0])
        timeout = timeout * 3

    for idx, url in enumerate(urls):
        sys.stderr.write('sub    : fetching page "%s"\n' % url)

        try:
            data = http_request(url, timeout if idx == 0 else timeout * 3)
            break
        except Exception as e:
            print_cnsl_error(str(e), url)

            if idx >= (len(urls) - 1):
                sys.stderr.write('sub    : COULD NOT FETCH INCLUDE_URL\n')
                return
            else:
                sys.stderr.write('sub    : fetching fallback page\n')

    # kinda ugly, use 4 spaces for tabs for everything except Makefiles
    data = data.expandtabs(8 if url.lower().endswith("makefile") else 4)

    # try to escape stuff that looks like pooles template language
    data = data.replace("{%", "\\{%")

    if isinstance(data_slice, tuple):
        start, end = data_slice
        if end < start:
            print_cnsl_error("invalid slice: end={} < start={}", end, start)
        else:
            lines = data.split("\n")
            slc = lines[max(0, start - 1) : end]
            data = "\n".join(slc)
            #sys.stderr.write("\n")
            #sys.stderr.write("Selected Slice:\n")
            #sys.stderr.write(str(len(slc)))
            #sys.stderr.write("\n")
            #for l in slc:
            #    sys.stderr.write(l + "\n")
            #sys.stderr.write("\n\n")
    elif isinstance(data_slice, list):
        lines = data.split("\n")
        data = []
        for ds in data_slice:
            start, end = ds
            if end < start:
                print_cnsl_error("invalid slice: end={} < start={}", end, start)
            else:
                slc = lines[max(0, start - 1) : end]
                data.append("\n".join(slc))
        data = "\n\n// ...\n\n".join(data)

    encoded = htmlspecialchars(data)
    print(encoded, end="")

def include_sourcecode_slice(sh_type, data_slice, filename, urls_pre, timeout = 2):
    urls = [ url_pre + filename for url_pre in urls_pre ]
    off = data_slice[0] if data_slice != None else 1

    print('<pre class="sh_' + sh_type + '" data-offset="' + str(off))
    if isinstance(data_slice, list):
        print(' data-skip=1')
    print('">')

    include_url(urls, data_slice, timeout)

    print('</pre>')
    print('<p class="sh_link_upstream">Link to the complete file "<a href="' + urls[0] + '">' + urls[0].split("/")[-1] + '</a>"')
    for idx, fallback in enumerate(urls[1:]):
        print(' (<a href="' + fallback + '">alt ' + str(idx + 1) + '</a>)')
    print('</p>')

    # manually count because this does not appear in page.source
    if not "shjs" in page["page_flags"]:
        page["page_flags"]["shjs"] = 0
    page["page_flags"]["shjs"] += 1

def restRequest(url):
    sys.stderr.write('sub    : fetching REST "%s"\n' % url)

    try:
        data = json.loads(http_request(url))
        return data
    except Exception as e:
        print_cnsl_error(str(e), url)
        sys.stderr.write('sub    : COULD NOT FETCH REST API\n')
        return []

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

    releases.sort(key=lambda x: SortReversor(x["published_at"]))
    r = releases[0]
    release_url = r["html_url"]
    print("Latest release of <a href=\"" + repo_url + "\">" + repo + "</a>: <a href=\"" + release_url + "\">" + r["name"] + "</a> (" + datetime.strptime(r["published_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S") + ")<br>\n")
    print("<span style=\"font-size: x-small\">(at the time of this writing)</span>\n<br>")

    if len(r["assets"]) <= 0:
        print("<br>No release assets have been published on GitHub for that.")
        print("</div>")
        return

    print("<br>Release Assets:")
    print("<ul>")
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

# -----------------------------------------------------------------------------
# multi language support
# -----------------------------------------------------------------------------

# TODO currently i'm moving all .md and .html files to the output top-dir
# TODO ugly legacy. can we change this to False in the future?
move_output_html_to_top = True # .html rendered files

def hook_preconvert_anotherlang():
    MKD_PATT = r'\.(?:md|mkd|mdown|markdown)$'
    _re_lang = re.compile(r'^[\s+]?lang[\s+]?[:=]((?:.|\n )*)', re.MULTILINE)
    vpages = [] # Set of all virtual pages
    for p in pages:
        current_lang = p.get("lang", DEFAULT_LANG) # Page-set or default language
        langs = [] # List of languages for the current page
        page_vpages = {} # Set of virtual pages for the current page
        text_lang = re.split(_re_lang, p.source)
        text_grouped = dict(zip([current_lang,] + \
                                        [lang.strip() for lang in text_lang[1::2]], \
                                        text_lang[::2]))

        lang_count = 0

        for lang, text in (iter(text_grouped.items()) if PY3 else text_grouped.iteritems()):
            sys.stderr.write('lang   : language %s for %s\n' % (lang, p.fname))
            langs.append(lang)

            # extract filename component of path (and modify if needed)
            if lang == current_lang:
                # keep first language path as original, without prefix
                fn = re.sub(MKD_PATT, r"%s\g<0>" % "", p.fname)
            else:
                # other languages get .lang before the file extension (eg. foo.html -> foo.de.html)
                fn = re.sub(MKD_PATT, r".%s\g<0>" % lang, p.fname)

            # only take last component of path (filename without subdirs)
            filename_top = fn.split(os.path.sep)[-1]

            # add other path components back in (without ./input/)
            spath = p.fname.split(os.path.sep)[2:]
            spath[-1] = filename_top
            filename_sub = os.path.sep.join(spath)

            if move_output_html_to_top == False:
                filename = filename_sub
            else:
                filename = filename_top

            # create new virtual Page
            vp = Page(filename, virtual=text, fullpath=filename_sub)

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

            # Keep a running counter of languages for this page, 0 is main
            vp["ordinal"] = lang_count
            lang_count += 1

            page_vpages[lang] = vp

        # Each virtual page has to know about its sister vpages
        for lang, vpage in (iter(page_vpages.items()) if PY3 else page_vpages.iteritems()):
            vpage["lang_links"] = dict([(l, v["url"]) for l, v in (iter(page_vpages.items()) if PY3 else page_vpages.iteritems())])
            vpage["other_lang"] = langs # set other langs and link

        vpages += page_vpages.values()

    # have the new virtual pages replace the original one
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
<?xml-stylesheet href="%s" type="text/xsl"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    xmlns:xhtml="http://www.w3.org/1999/xhtml"
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</urlset>
"""

_SITEMAP_URL = """    <url>
        <xhtml:title>%s</xhtml:title>
        <loc>%s</loc>
        <lastmod>%s</lastmod>
        <changefreq>%s</changefreq>
        <priority>%s</priority>%s
    </url>"""

_SITEMAP_URL_LANG = """
        <xhtml:link rel="alternate" hreflang="%s" href="%s" />"""

def hook_preconvert_sitemap():
    posts = [p for p in pages]

    # sort by update if available, date else, followed by title
    posts.sort(key=lambda p: [ SortReversor(p.get("update", p.get("date", "0001-01-01"))), p["title"] ])

    urls = []
    for p in posts:
        title = p.title
        if "post" in p:
            title = p.post

        url = "%s/%s" % (BASE_URL, p.url)
        freq = p.get("changefreq", "monthly")
        prio = p.get("priority", "0.5")

        update, update_has_time = page_to_datetime(p.get("update", p.get("date", None)))
        date = update if update is not None else datetime.now()
        date_s = datetime.strftime(date, "%Y-%m-%d")

        langs = []
        for lang in p["other_lang"]:
            if lang == p["lang"]:
                continue
            lang_url = "%s/%s" % (BASE_URL, p["lang_links"][lang])
            link = _SITEMAP_URL_LANG % (lang, lang_url)
            langs.append(link)

        additional = ""
        if len(langs) > 0:
            additional = "\n".join(langs)

        item = _SITEMAP_URL % (title, url, date_s, freq, prio, additional)
        urls.append(item)

    style = "/css/sitemap.xsl"
    items = "\n".join(urls)

    sitemap = _SITEMAP % (style, items)

    fp = codecs.open(os.path.join(output, "sitemap.xml"), "w", "utf-8")
    fp.write(sitemap)
    fp.close()

# -----------------------------------------------------------------------------
# counting SHJS and lightGallery occurences
# -----------------------------------------------------------------------------

def hook_preconvert_count_stuff():
    for page in pages:
        if not "lightgallery" in page["page_flags"]:
            page["page_flags"]["lightgallery"] = 0
        page["page_flags"]["lightgallery"] += page.source.count('class="lightgallery')

        if not "shjs" in page["page_flags"]:
            page["page_flags"]["shjs"] = 0
        page["page_flags"]["shjs"] += page.source.count('<pre')

        if not "collapse" in page["page_flags"]:
            page["page_flags"]["collapse"] = 0
        page["page_flags"]["collapse"] += page.source.count('collapsecontent')


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
    posts.sort(key=lambda p: [ SortReversor(p.get("update", p.date)), p["title"] ])

    # only put 20 most recent items in feed
    posts = posts[:20]

    for p in posts:
        title = p.title
        if "post" in p:
            title = p.post

        link = "%s/%s" % (BASE_URL, p.url)

        # TODO very basic way of making image links absolute
        # TODO improve? how?
        desc = p.html.replace("href=\"img", "%s%s%s" % ("href=\"", BASE_URL, "/img"))
        desc = desc.replace("src=\"img", "%s%s%s" % ("src=\"", BASE_URL, "/img"))
        desc = desc.replace("href=\"/img", "%s%s%s" % ("href=\"", BASE_URL, "/img"))
        desc = desc.replace("src=\"/img", "%s%s%s" % ("src=\"", BASE_URL, "/img"))
        desc = htmlspecialchars(desc)

        date, date_has_time = page_to_datetime(p.date)
        update, update_has_time = page_to_datetime(p.get("update", p.date))

        date_s = email.utils.formatdate(time.mktime(date.timetuple()))
        update_s = update.isoformat() + "Z"

        items.append(_RSS_ITEM % (title, link, desc, date_s, update_s, link))

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
