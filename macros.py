import re
import itertools
import email.utils
import os.path
import time
from datetime import datetime

DEFAULT_LANG = "en"
BASE_URL = "http://www.xythobuz.de"

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
    fp.write("$loc = 'index.de.html';\n")
    fp.write("if (isset($_GET['p'])) {\n")
    fp.write("    if (isset($_GET['lang'])) {\n")
    fp.write("        $_GET['p'] .= EN;\n")
    fp.write("    }\n")
    fp.write("    switch($_GET['p']) {\n")
    for p in pages:
        if p.get("compat", "") != "":
            tmp = p["compat"]
            if p.get("lang", DEFAULT_LANG) == DEFAULT_LANG:
                tmp = tmp + "EN"
            fp.write(_COMPAT % (tmp, options.base_url.rstrip('/'), p.url))
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
        urls.append(_SITEMAP_URL % (options.base_url.rstrip('/'), p.url, date, p.get("changefreq", "monthly"), p.get("priority", "0.5")))
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
    posts = [p for p in pages if "post" in p] # get all blog post pages
    posts.sort(key=lambda p: p.date, reverse=True)
    for p in posts:
        title = p.post
        link = "%s/%s" % (BASE_URL, p.url)
        desc = htmlspecialchars(p.get("description", "Electronics & Software Projects"))
        date = time.mktime(time.strptime("%s 12" % p.date, "%Y-%m-%d %H"))
        date = email.utils.formatdate(date)
        items.append(_RSS_ITEM % (title, link, desc, date, link))

    items = "".join(items)

    title = "xythobuz.de Blog"
    link = "%s/blog.html" % BASE_URL
    feed = "%s/rss.xml" % BASE_URL
    desc = htmlspecialchars("xythobuz Electronics & Software Projects")
    date = email.utils.formatdate()

    rss = _RSS % (title, link, feed, desc, date, date, items)

    fp = open(os.path.join(output, "rss.xml"), 'w')
    fp.write(rss)
    fp.close()
