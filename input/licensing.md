title: Software Licensing
---

All written words on the pages of this website, the actual content of the sites, is licensed under the [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/).

My own Python and JavaScript code is licensed under the [GPLv3](http://www.gnu.org/licenses/gpl-3.0.html), just like the static website generator [Poole](https://hg.sr.ht/~obensonne/poole) I'm using.

Everything can be found [in the Git repo](https://codeberg.org/xythobuz/website).

## JavaScript

This is the [LibreJS compatible](https://www.gnu.org/software/librejs/free-your-javascript.html) JavaScript licensing information.

I'm using [jQuery](https://github.com/jquery/jquery), [SHJS](https://shjs.sourceforge.net/) and [lightGallery](https://github.com/sachinchoolur/lightGallery) on all pages.
I'm also tracking your website visits with self-hosted [Fathom analytics](https://github.com/usefathom/fathom).
For [Duality](duality.html) I'm also using [EmulatorJS](https://github.com/EmulatorJS/EmulatorJS).

These are all licensed as GPLv3 or MIT.

<!--%
librejs_helper([
    # jQuery
    [ "js/jquery-3.7.1.min.js", "MIT", "js/jquery-3.7.1.js" ],

    # Own code
    [ "js/auto_toc.js", "gpl3" ],
    [ "js/collapse.js", "gpl3" ],
    [ "js/copy.js", "gpl3" ],
    [ "js/lightgallery.js", "gpl3" ],
    [ "js/resize.js", "gpl3" ],
    [ "js/scroller.js", "gpl3" ],
    [ "js/shjs.js", "gpl3" ],

    # Lightgallery
    [ "lg/lightgallery.min.js", "gpl3" ],
    [ "lg/lg-autoplay.min.js", "gpl3" ],
    [ "lg/lg-fullscreen.min.js", "gpl3" ],
    [ "lg/lg-hash.min.js", "gpl3" ],
    [ "lg/lg-rotate.min.js", "gpl3" ],
    [ "lg/lg-thumbnail.min.js", "gpl3" ],
    [ "lg/lg-video.min.js", "gpl3" ],
    [ "lg/lg-zoom.min.js", "gpl3" ],

    # Fathom tracking
    [ "js/tracking.js", "MIT", "https://github.com/usefathom/fathom/blob/master/assets/src/js/components/SiteSettings.js#L121-L134" ],

    # SHJS
    [ "js/sh_main.min.js", "gpl3", "js/sh_main.js" ],

    # SHJS languages converted from GNU source highlight
    [ "js/sh/sh_gcode.min.js", "gpl3", "js/sh/sh_gcode.js" ],
    [ "js/sh/sh_go.min.js", "gpl3", "js/sh/sh_go.js" ],
    [ "js/sh/sh_yaml.min.js", "gpl3", "js/sh/sh_yaml.js" ],
    [ "js/sh/sh_desktop.min.js", "gpl3", "js/sh/sh_desktop.js" ],

    # SHJS languages from official distribution
    [ "js/sh/sh_bison.min.js", "gpl3", "js/sh/sh_bison.js" ],
    [ "js/sh/sh_caml.min.js", "gpl3", "js/sh/sh_caml.js" ],
    [ "js/sh/sh_changelog.min.js", "gpl3", "js/sh/sh_changelog.js" ],
    [ "js/sh/sh_c.min.js", "gpl3", "js/sh/sh_c.js" ],
    [ "js/sh/sh_cpp.min.js", "gpl3", "js/sh/sh_cpp.js" ],
    [ "js/sh/sh_csharp.min.js", "gpl3", "js/sh/sh_csharp.js" ],
    [ "js/sh/sh_css.min.js", "gpl3", "js/sh/sh_css.js" ],
    [ "js/sh/sh_diff.min.js", "gpl3", "js/sh/sh_diff.js" ],
    [ "js/sh/sh_flex.min.js", "gpl3", "js/sh/sh_flex.js" ],
    [ "js/sh/sh_glsl.min.js", "gpl3", "js/sh/sh_glsl.js" ],
    [ "js/sh/sh_haxe.min.js", "gpl3", "js/sh/sh_haxe.js" ],
    [ "js/sh/sh_html.min.js", "gpl3", "js/sh/sh_html.js" ],
    [ "js/sh/sh_java.min.js", "gpl3", "js/sh/sh_java.js" ],
    [ "js/sh/sh_javascript_dom.min.js", "gpl3", "js/sh/sh_javascript_dom.js" ],
    [ "js/sh/sh_javascript.min.js", "gpl3", "js/sh/sh_javascript.js" ],
    [ "js/sh/sh_latex.min.js", "gpl3", "js/sh/sh_latex.js" ],
    [ "js/sh/sh_ldap.min.js", "gpl3", "js/sh/sh_ldap.js" ],
    [ "js/sh/sh_log.min.js", "gpl3", "js/sh/sh_log.js" ],
    [ "js/sh/sh_lsm.min.js", "gpl3", "js/sh/sh_lsm.js" ],
    [ "js/sh/sh_m4.min.js", "gpl3", "js/sh/sh_m4.js" ],
    [ "js/sh/sh_makefile.min.js", "gpl3", "js/sh/sh_makefile.js" ],
    [ "js/sh/sh_oracle.min.js", "gpl3", "js/sh/sh_oracle.js" ],
    [ "js/sh/sh_pascal.min.js", "gpl3", "js/sh/sh_pascal.js" ],
    [ "js/sh/sh_perl.min.js", "gpl3", "js/sh/sh_perl.js" ],
    [ "js/sh/sh_php.min.js", "gpl3", "js/sh/sh_php.js" ],
    [ "js/sh/sh_prolog.min.js", "gpl3", "js/sh/sh_prolog.js" ],
    [ "js/sh/sh_properties.min.js", "gpl3", "js/sh/sh_properties.js" ],
    [ "js/sh/sh_python.min.js", "gpl3", "js/sh/sh_python.js" ],
    [ "js/sh/sh_ruby.min.js", "gpl3", "js/sh/sh_ruby.js" ],
    [ "js/sh/sh_scala.min.js", "gpl3", "js/sh/sh_scala.js" ],
    [ "js/sh/sh_sh.min.js", "gpl3", "js/sh/sh_sh.js" ],
    [ "js/sh/sh_slang.min.js", "gpl3", "js/sh/sh_slang.js" ],
    [ "js/sh/sh_sml.min.js", "gpl3", "js/sh/sh_sml.js" ],
    [ "js/sh/sh_spec.min.js", "gpl3", "js/sh/sh_spec.js" ],
    [ "js/sh/sh_sql.min.js", "gpl3", "js/sh/sh_sql.js" ],
    [ "js/sh/sh_tcl.min.js", "gpl3", "js/sh/sh_tcl.js" ],
    [ "js/sh/sh_xml.min.js", "gpl3", "js/sh/sh_xml.js" ],
    [ "js/sh/sh_xorg.min.js", "gpl3", "js/sh/sh_xorg.js" ],

    # Emulator.js
    [ "emu_js/loader.js", "gpl3" ],
    [ "emu_js/emulator.min.js", "gpl3" ],

    # TODO unknown license?!
    #[ "emu_js/compression/extractzip.js", "" ],
    #[ "emu_js/compression/extract7z.js", "" ],
    #[ "emu_js/compression/libunrar.js", "" ],
])
%-->

I think [LibreJS](https://www.gnu.org/software/librejs/) is a really good idea.
Unfortunately it is not well maintained or documented.
I had some trouble getting it to work on my website.
Apart from the very specific license names (Expat instead of MIT) the method of declaring licenses used on this page does no longer work.
Due to async fetching of scripts they each have to include their own licensing information.
