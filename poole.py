#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
#
#    Poole - A damn simple static website generator.
#    Copyright (C) 2012 Oben Sonne <obensonne@googlemail.com>
#
#    This file is part of Poole.
#
#    Poole is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Poole is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Poole.  If not, see <http://www.gnu.org/licenses/>.
#
# =============================================================================

from __future__ import with_statement
from __future__ import print_function

import codecs
import glob
import optparse
import os
from os.path import join as opj
from os.path import exists as opx
import re
import shutil
import sys
import traceback

try:
    import markdown
except ImportError:
    print("abort  : need python-markdown, get it from "
          "http://www.freewisdom.org/projects/python-markdown/Installation")
    sys.exit(1)

# =============================================================================
# Python 2/3 hacks
# =============================================================================

PY3 = sys.version_info[0] == 3

if PY3:
    import builtins
    exec_ = getattr(builtins, "exec")
    import importlib.util
    import importlib.machinery
    def imp_load_source(modname, filename):
        loader = importlib.machinery.SourceFileLoader(modname, filename)
        spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
        module = importlib.util.module_from_spec(spec)
        # The module is always executed and not cached in sys.modules.
        # Uncomment the following line to cache the module.
        # sys.modules[module.__name__] = module
        loader.exec_module(module)
        return module
    import urllib
    def urlparse_urljoin(a, b):
        return urllib.parse.urljoin(a, b)
    from io import StringIO
    from http.server import HTTPServer, SimpleHTTPRequestHandler
else:
    import tempfile
    from StringIO import StringIO
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
    def exec_(code, envdic):
        with tempfile.NamedTemporaryFile() as tf:
            tf.write('# -*- coding: utf-8 -*-\n')
            tf.write(code.encode('utf-8'))
            tf.flush()
            execfile(tf.name, envdic)
    import imp
    def imp_load_source(module_name, module_path):
        return imp.load_source(module_name, module_path)
    import urlparse
    def urlparse_urljoin(a, b):
        return urlparse.urljoin(a, b)

# =============================================================================
# init site
# =============================================================================

EXAMPLE_FILES =  {

"page.html": """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset={{ htmlspecialchars(__encoding__) }}" />
    <title>poole - {{ htmlspecialchars(page["title"]) }}</title>
    <meta name="description" content="{{ htmlspecialchars(page.get("description", "a poole site")) }}" />
    <meta name="keywords" content="{{ htmlspecialchars(page.get("keywords", "poole")) }}" />
    <link rel="stylesheet" type="text/css" href="poole.css" />
</head>
<body>
    <div id="box">
    <div id="header">
         <h1>a poole site</h1>
         <h2>{{ htmlspecialchars(page["title"]) }}</h2>
    </div>
    <div id="menu">
    <!--%
        mpages = [p for p in pages if "menu-position" in p]
        mpages.sort(key=lambda p: int(p["menu-position"]))
        entry = '<span class="%s"><a href="%s">%s</a></span>'
        for p in mpages:
            style = p["title"] == page["title"] and "current" or ""
            print(entry % (style, htmlspecialchars(p["url"]), htmlspecialchars(p["title"])))
    %-->
    </div>
    <div id="content">{{ __content__ }}</div>
    </div>
    <div id="footer">
        Built with <a href="http://bitbucket.org/obensonne/poole">Poole</a>
        &middot;
        Licensed as <a href="http://creativecommons.org/licenses/by-sa/3.0">CC-SA</a>
        &middot;
        <a href="http://validator.w3.org/check?uri=referer">Validate me</a>
    </div>
</body>
</html>
""",

# -----------------------------------------------------------------------------

opj("input", "index.md"): """
title: home
menu-position: 0
---

## Welcome to Poole

In Poole you write your pages in [markdown][md]. It's easier to write
markdown than HTML.

Poole is made for simple websites you just want to get done, without installing
a bunch of requirements and without learning a template engine.

In a build, Poole copies every file from the *input* directory to the *output*
directory. During that process every markdown file (ending with *md*, *mkd*,
*mdown* or *markdown*) is converted to HTML using the project's `page.html`
as a skeleton.

[md]: http://daringfireball.net/projects/markdown/
""",

# -----------------------------------------------------------------------------

opj("input", "logic.md"): """
menu-position: 4
---
Poole has basic support for content generation using Python code inlined in
page files. This is everything but a clear separation of logic and content but
for simple sites this is just a pragmatic way to get things done fast.
For instance the menu on this page is generated by some inlined Python code in
the project's `page.html` file.

Just ignore this feature if you don't need it :)

Content generation by inlined Python code is good to add some zest to your
site. If you use it a lot, you better go with more sophisticated site
generators like [Hyde](http://ringce.com/hyde).
""",

# -----------------------------------------------------------------------------

opj("input", "layout.md"): """
menu-position: 3
---
Every page of a poole site is based on *one global template file*, `page.html`.
All you need to adjust the site layout is to

 * edit the page template `page.html` and
 * extend or edit the style file `input/poole.css`.
""",

opj("input", "blog.md"): """
menu-position: 10
---
Poole has basic blog support. If an input page's file name has a structure like
`page-title.YYYY-MM-DD.post-title.md`, e.g. `blog.2010-02-27.read_this.md`,
Poole recognizes the date and post title and sets them as attributes of the
page. These attributes can then be used to generate a list of blog posts:

<!--%
from datetime import datetime
posts = [p for p in pages if "post" in p] # get all blog post pages
posts.sort(key=lambda p: p.get("date"), reverse=True) # sort post pages by date
for p in posts:
    date = datetime.strptime(p.date, "%Y-%m-%d").strftime("%B %d, %Y")
    print "  * **[%s](%s)** - %s" % (p.post, p.url, date) # markdown list item
%-->

Have a look into `input/blog.md` to see how it works. Feel free to adjust it
to your needs.
""",

# -----------------------------------------------------------------------------

opj("input", "blog.2010-02-22.Doctors_in_my_penguin.md") : """

---
## {{ page["post"] }}

*Posted at
<!--%
from datetime import datetime
print datetime.strptime(page["date"], "%Y-%m-%d").strftime("%B %d, %Y")
%-->*

There is a bank in my eel, your argument is invalid.

More nonsense at <http://automeme.net/>.
""",

# -----------------------------------------------------------------------------

opj("input", "blog.2010-03-01.I_ate_all the pokemans.md"): """

## {{ page["post"] }}

*Posted at <!--{ page["date"] }-->.*

What *are* interior crocodile alligators? We just don't know.

More nonsense at <http://automeme.net/>.
""",

# -----------------------------------------------------------------------------

opj("input", "poole.css"): """
body {
    font-family: sans;
    width: 800px;
    margin: 1em auto;
    color: #2e3436;
}
div#box {
    border: solid #2e3436 1px;
}
div#header, div#menu, div#content, div#footer {
    padding: 1em;
}
div#menu {
    background-color: #2e3436;
    padding: 0.6em 0 0.6em 0;
}
#menu span {
    background-color: #2e3436;
    font-weight: bold;
    padding: 0.6em;
}
#menu span.current {
    background-color: #555753;
}
#menu a {
    color: #fefefc;
    text-decoration: none;
}
div#footer {
    color: gray;
    text-align: center;
    font-size: small;
}
div#footer a {
    color: gray;
    text-decoration: none;
}
pre {
    border: dotted black 1px;
    background: #eeeeec;
    font-size: small;
    padding: 1em;
}

"""
}

def init(project):
    """Initialize a site project."""

    if not opx(project):
        os.makedirs(project)

    if os.listdir(project):
        print("abort  : project dir %s is not empty" % project)
        sys.exit(1)

    os.mkdir(opj(project, "input"))
    os.mkdir(opj(project, "output"))

    for fname, content in EXAMPLE_FILES.items():
        with open(opj(project, fname), 'w') as fp:
            fp.write(content)

    print("success: initialized project")

# =============================================================================
# build site
# =============================================================================

MKD_PATT = r'\.(?:md|mkd|mdown|markdown)$'

class Page(dict):
    """Abstraction of a source page."""

    _template = None # template dictionary
    _opts = None # command line options
    _pstrip = None # path prefix to strip from (non-virtual) page file names

    _re_eom = re.compile(r'^---+ *\r?\n?$')
    _re_vardef = re.compile(r'^([^\n:=]+?)[:=]((?:.|\n )*)', re.MULTILINE)
    _sec_macros = "macros"
    _modmacs = None

    def __init__(self, fname, virtual=None, **attrs):
        """Create a new page.

        Page content is read from `fname`, except when `virtual` is given (a
        string representing the raw content of a virtual page).

        The filename refers to the page source file. For virtual pages, this
        *must* be relative to a projects input directory.

        Virtual pages may contain page attribute definitions similar to real
        pages. However, it probably is easier to provide the attributes
        directly. This may be done using arbitrary keyword arguments.

        """
        super(Page, self).__init__()

        self.update(self._template)
        self.update(attrs)

        self._virtual = virtual is not None

        fname = opj(self._pstrip, fname) if virtual else fname

        self["fname"] = fname

        self["url"] = re.sub(MKD_PATT, ".html", fname)
        self["url"] = self["url"][len(self._pstrip):].lstrip(os.path.sep)
        self["url"] = self["url"].replace(os.path.sep, "/")

        if virtual:
            self.raw = virtual
        else:
            with codecs.open(fname, 'r', self._opts.input_enc) as fp:
                self.raw = fp.readlines()

        # split raw content into macro definitions and real content
        vardefs = ""
        self.source = ""
        for line in self.raw:
            if not vardefs and self._re_eom.match(line):
                vardefs = self.source
                self.source = "" # only macro defs until here, reset source
            else:
                self.source += line

        for key, val in self._re_vardef.findall(vardefs):
            key = key.strip()
            val = val.strip()
            val = re.sub(r' *\n +', ' ', val) # clean out line continuation
            self[key] = val

        basename = os.path.basename(fname)

        fpatt = r'(.+?)(?:\.([0-9]+-[0-9]+-[0-9]+)(?:\.(.*))?)?%s' % MKD_PATT
        title, date, post = re.match(fpatt, basename).groups()
        title = title.replace("_", " ")
        post = post and post.replace("_", " ") or None
        self["title"] = self.get("title", title)
        if date and "date" not in self: self["date"] = date
        if post and "post" not in self: self["post"] = post

        self.html = ""

    def __getattr__(self, name):
        """Attribute-style access to dictionary items."""
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __str__(self):
        """Page representation by file name."""
        return ('%s (virtual)' % self.fname) if self._virtual else self.fname

# -----------------------------------------------------------------------------

def build(project, opts):
    """Build a site project."""

    # -------------------------------------------------------------------------
    # utilities
    # -------------------------------------------------------------------------

    def abort_iex(page, itype, inline, exc):
        """Abort because of an exception in inlined Python code."""
        print("abort  : Python %s in %s failed" % (itype, page))
        print((" %s raising the exception " % itype).center(79, "-"))
        print(inline.encode('utf-8'))
        print(" exception ".center(79, "-"))
        print(exc)
        sys.exit(1)

    # -------------------------------------------------------------------------
    # regex patterns and replacements
    # -------------------------------------------------------------------------

    regx_escp = re.compile(r'\\((?:(?:&lt;|<)!--|{)(?:{|%))') # escaped code
    repl_escp = r'\1'
    regx_rurl = re.compile(r'(?<=(?:(?:\n| )src|href)=")([^#/&%].*?)(?=")')
    repl_rurl = lambda m: urlparse_urljoin(opts.base_url, m.group(1))

    regx_eval = re.compile(r'(?<!\\)(?:(?:<!--|{){)(.*?)(?:}(?:-->|}))', re.S)

    def repl_eval(m):
        """Replace a Python expression block by its evaluation."""

        expr = m.group(1)
        try:
            repl = eval(expr, macros.copy())
        except:
            abort_iex(page, "expression", expr, traceback.format_exc())
        else:
            if PY3:
                if not isinstance(repl, str):
                    repl = str(repl)
            else:
                if not isinstance(repl, basestring): # e.g. numbers
                    repl = unicode(repl)
                elif not isinstance(repl, unicode):
                    repl = repl.decode("utf-8")
            return repl

    regx_exec = re.compile(r'(?<!\\)(?:(?:<!--|{)%)(.*?)(?:%(?:-->|}))', re.S)

    def repl_exec(m):
        """Replace a block of Python statements by their standard output."""

        stmt = m.group(1).replace("\r\n", "\n")

        # base indentation
        ind_lvl = len(re.findall(r'^(?: *\n)*( *)', stmt, re.MULTILINE)[0])
        ind_rex = re.compile(r'^ {0,%d}' % ind_lvl, re.MULTILINE)
        stmt = ind_rex.sub('', stmt)

        # execute
        sys.stdout = StringIO()
        try:
            exec_(stmt, macros.copy())
        except:
            sys.stdout = sys.__stdout__
            abort_iex(page, "statements", stmt, traceback.format_exc())
        else:
            repl = sys.stdout.getvalue()[:-1] # remove last line break
            sys.stdout = sys.__stdout__
            if not PY3:
                if not isinstance(repl, unicode):
                    repl = repl.decode(opts.input_enc)
            return repl

    # -------------------------------------------------------------------------
    # preparations
    # -------------------------------------------------------------------------

    dir_in = opj(project, "input")
    dir_out = opj(project, "output")
    page_html = opj(project, "page.html")

    # check required files and folders
    for pelem in (page_html, dir_in, dir_out):
        if not opx(pelem):
            print("abort  : %s does not exist, looks like project has not been "
                  "initialized" % pelem)
            sys.exit(1)

    # prepare output directory
    for fod in glob.glob(opj(dir_out, "*")):
        if os.path.isdir(fod):
            shutil.rmtree(fod)
        else:
            os.remove(fod)
    if not opx(dir_out):
        os.mkdir(dir_out)

    # macro module
    fname = opj(opts.project, "macros.py")
    macros = imp_load_source("macros", fname).__dict__ if opx(fname) else {}

    macros["__encoding__"] = opts.output_enc
    macros["options"] = opts
    macros["project"] = project
    macros["input"] = dir_in
    macros["output"] = dir_out

    # "builtin" functions for use in macros and templates
    macros["htmlspecialchars"] = htmlspecialchars
    macros["Page"] = Page

    # -------------------------------------------------------------------------
    # process input files
    # -------------------------------------------------------------------------

    Page._template = macros.get("page", {})
    Page._opts = opts
    Page._pstrip = dir_in
    pages = []
    custom_converter = macros.get('converter', {})

    for cwd, dirs, files in os.walk(dir_in if PY3 else dir_in.decode(opts.filename_enc)):
        cwd_site = cwd[len(dir_in):].lstrip(os.path.sep)
        for sdir in dirs[:]:
            if re.search(opts.ignore, opj(cwd_site, sdir)):
                dirs.remove(sdir)
            else:
                os.mkdir(opj(dir_out, cwd_site, sdir))
        for f in files:
            if re.search(opts.ignore, opj(cwd_site, f)):
                pass
            elif re.search(MKD_PATT, f):
                page = Page(opj(cwd, f))
                pages.append(page)
                foo = opj(cwd, f)
                bar = opj(dir_out, f)
                print('info   : copy %s' % bar)
                shutil.copyfile(foo, bar)
            else:
                # either use a custom converter or do a plain copy
                for patt, (func, ext) in custom_converter.items():
                    if re.search(patt, f):
                        f_src = opj(cwd, f)
                        f_dst = opj(dir_out, cwd_site, f)
                        f_dst = '%s.%s' % (os.path.splitext(f_dst)[0], ext)
                        print('info   : convert %s (%s)' % (f_src, func.__name__))
                        func(f_src, f_dst)
                        break
                else:
                    src = opj(cwd, f)
                    try:
                        shutil.copy(src, opj(dir_out, cwd_site))
                    except OSError:
                        # some filesystems like FAT won't allow shutil.copy
                        shutil.copyfile(src, opj(dir_out, cwd_site, f))

    pages.sort(key=lambda p: int(p.get("sval", "0")))

    macros["pages"] = pages

    # -------------------------------------------------------------------------
    # run pre-convert hooks in macro module (named 'once' before)
    # -------------------------------------------------------------------------

    hooks = [a for a in macros if re.match(r'hook_preconvert_|once_', a)]
    for fn in sorted(hooks):
        macros[fn]()

    # -------------------------------------------------------------------------
    # convert pages (markdown to HTML)
    # -------------------------------------------------------------------------

    for page in pages:

        print("info   : convert %s" % page)

        # replace expressions and statements in page source
        macros["page"] = page
        out = regx_eval.sub(repl_eval, page.source)
        out = regx_exec.sub(repl_exec, out)

        # convert to HTML
        page.html = markdown.Markdown(extensions=opts.md_ext).convert(out)

    # -------------------------------------------------------------------------
    # run post-convert hooks in macro module
    # -------------------------------------------------------------------------

    hooks = [a for a in macros if a.startswith("hook_postconvert_")]
    for fn in sorted(hooks):
        macros[fn]()

    # -------------------------------------------------------------------------
    # render complete HTML pages
    # -------------------------------------------------------------------------

    with codecs.open(opj(project, "page.html"), 'r', opts.input_enc) as fp:
        skeleton = fp.read()

    for page in pages:

        print("info   : render %s" % page.url)

        # replace expressions and statements in page.html
        macros["page"] = page
        macros["__content__"] = page.html
        out = regx_eval.sub(repl_eval, skeleton)
        out = regx_exec.sub(repl_exec, out)

        # un-escape escaped python code blocks
        out = regx_escp.sub(repl_escp, out)

        # make relative links absolute
        out = regx_rurl.sub(repl_rurl, out)

        # write HTML page
        fname = page.fname.replace(dir_in, dir_out)
        fname = re.sub(MKD_PATT, ".html", fname)
        with codecs.open(fname, 'w', opts.output_enc) as fp:
            fp.write(out)

    # -------------------------------------------------------------------------
    # remove empty subfolders
    # -------------------------------------------------------------------------

    removeEmptyFolders(dir_out)

    print("success: built project")

def removeEmptyFolders(path):
    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)

    # Dirty OS X Hack
    try:
        os.remove(os.path.join(path, ".DS_Store"))
    except OSError as ex:
        pass

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0:
        print("info   : removing empty folder: ", path)
        os.rmdir(path)

# =============================================================================
# serve site
# =============================================================================

def serve(project, port):
    """Temporary serve a site project."""

    root = opj(project, "output")
    if not os.listdir(project):
        print("abort  : output dir is empty (build project first!)")
        sys.exit(1)

    os.chdir(root)
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# =============================================================================
# options
# =============================================================================

def options():
    """Parse and validate command line arguments."""

    usage = ("Usage: %prog --init [path/to/project]\n"
             "       %prog --build [OPTIONS] [path/to/project]\n"
             "       %prog --serve [OPTIONS] [path/to/project]\n"
             "\n"
             "       Project path is optional, '.' is used as default.")

    op = optparse.OptionParser(usage=usage)

    op.add_option("-i" , "--init", action="store_true", default=False,
                  help="init project")
    op.add_option("-b" , "--build", action="store_true", default=False,
                  help="build project")
    op.add_option("-s" , "--serve", action="store_true", default=False,
                  help="serve project")

    og = optparse.OptionGroup(op, "Build options")
    og.add_option("", "--base-url", default="/", metavar="URL",
                  help="base url for relative links (default: /)")
    og.add_option("" , "--ignore", default=r"^\.|~$", metavar="REGEX",
                  help="input files to ignore (default: '^\\.|~$')")
    og.add_option("" , "--md-ext", default=[], metavar="EXT",
                  action="append", help="enable a markdown extension")
    og.add_option("", "--input-enc", default="utf-8", metavar="ENC",
                  help="encoding of input pages (default: utf-8)")
    og.add_option("", "--output-enc", default="utf-8", metavar="ENC",
                  help="encoding of output pages (default: utf-8)")
    og.add_option("", "--filename-enc", default="utf-8", metavar="ENC",
                  help="encoding of file names (default: utf-8)")
    op.add_option_group(og)

    og = optparse.OptionGroup(op, "Serve options")
    og.add_option("" , "--port", default=8080,
                  metavar="PORT", type="int",
                  help="port for serving (default: 8080)")
    op.add_option_group(og)

    opts, args = op.parse_args()

    if opts.init + opts.build + opts.serve < 1:
        op.print_help()
        op.exit()

    opts.project = args and args[0] or "."

    return opts

# =============================================================================
# template helper functions
# =============================================================================

def htmlspecialchars(s):
    """
    Replace the characters that are special within HTML (&, <, > and ")
    with their equivalent character entity (e.g., &amp;). This should be
    called whenever an arbitrary string is inserted into HTML (so in most
    places where you use {{ variable }} in your templates).

    Note that " is not special in most HTML, only within attributes.
    However, since escaping it does not hurt within normal HTML, it is
    just escaped unconditionally.
    """
    escape = {
        "&": "&amp;",
        '"': "&quot;",
        ">": "&gt;",
        "<": "&lt;",
    }

    # Look up the translation for every character in s (defaulting to
    # the character itself if no translation is available).
    return ''.join([escape.get(c,c) for c in s])

# =============================================================================
# main
# =============================================================================

def main():

    opts = options()

    if opts.init:
        init(opts.project)
    if opts.build:
        build(opts.project, opts)
    if opts.serve:
        serve(opts.project, opts.port)

if __name__ == '__main__':

    main()
