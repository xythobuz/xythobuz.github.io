title: Blog
post: Auto-generated project docs with 3D preview
description: For KiCad PCBs and STL files, made with mdBook
date: 2024-05-05
---

A recurring problem I ran into with my projects is documentation.
Especially with 3D printed parts or PCBs it's often required to generate preview images or PDFs so someone interested can take a look without having to clone the repo and install some development tools to open the original files.
Doing this manually is time-consuming and repetitive.
So it should be automated.

I've come across a couple of similar projects recently, like [this](https://hackaday.com/2024/05/04/giving-your-kicad-pcb-repository-pretty-pictures/) or [these](https://hackaday.com/2024/03/11/share-your-projects-kicad-automations-and-pretty-renders/).
But they mostly spit out non-interactive images.
So I've decided to go a slightly different and more interactive route.

<!--%
lightgallery([
    [ "img/github_pages_sch.png", "2D KiCad board visualization" ],
    [ "img/github_pages_pcb.png", "3D KiCad board visualization" ],
    [ "img/github_pages_stl.png", "3D STL visualization" ],
])
%-->

Using [GitHub Actions](https://docs.github.com/en/actions) and [GitHub Pages](https://docs.github.com/en/pages), I'm creating a static documentation website using [mdBook](https://rust-lang.github.io/mdBook/).
To visualize KiCad schematics and 2D board designs I'm exporting them as svg images and display them interactively using [svg-pan-zoom](https://github.com/bumbu/svg-pan-zoom).
KiCad PCBs are also exported in 3D as VRML files and displayed using [three.js](https://threejs.org/).

To generate these files I'm mostly using shell scripts in the project repository.

* `generate_stls.sh` is creating STL files from OpenSCAD sources
* `generate_fab.sh` is creating Gerber files to order PCBs
* `generate_plot.sh` is creating the 2D and 3D files for KiCad projects
* `generate_docs.sh` is creating the static website using the output from the previous scripts

Then the workflows can be kept relatively short, just installing the required dependencies, running the proper script and putting the resulting files where they are needed.
This way the coupling to the proprietary GitHub features is not that thight and can hopefully be ported to other providers with relative ease.

* `cmake.yml` is creating firmware archives (also usable for OTA updates)
* `scad.yml` to create the STL files
* `kicad.yml` to generate board gerber files
* `docs.yml` to create the static documentation pages

The whole workflow is relatively customizable.
So for some projects I'm for example creating special board previews for etching PCBs at home.

I've implemented this workflow in a couple of projects now:

* [OpenAutoLab](https://kauzerei.github.io/openautolab/) ([Repo](https://github.com/kauzerei/openautolab))
* [LARS](https://xythobuz.github.io/lars/) ([Repo](https://github.com/xythobuz/lars))
* [Dispensy](https://drinkrobotics.github.io/dispensy/) ([Repo](https://github.com/drinkrobotics/dispensy))
* [Tritonmischer](https://kauzerei.github.io/tritonmischer/) ([Repo](https://github.com/kauzerei/tritonmischer))

Take a look there for the implementation details.

## Example Implementation

Here are the basics to get you started.

#### 1) mdBook dependency

Fetch the [pre-built mdBook binary](https://github.com/rust-lang/mdBook/releases) and place it in your PATH.

#### 2) mdBook initialization

Add a [docs](https://github.com/xythobuz/lars/tree/master/docs) directory to your project, either by copying it from one of my repos, or creating a new one and adapting the resulting `book.toml` config.

    mdbook init docs

#### 3) svg-pan-zoom dependency

If you want to visualize SVG images for KiCad schematics and boards, add svg-pan-zoom as a subrepo.

    cd docs
    git submodule add https://github.com/bumbu/svg-pan-zoom
    mkdir -p src/js
    cd src/js
    ln -s ../../svg-pan-zoom/dist/svg-pan-zoom.js svg-pan-zoom.js
    ln -s ../../svg-pan-zoom/dist/svg-pan-zoom.min.js svg-pan-zoom.min.js

#### 4) Generating docs

Add the `docs/generate_docs.sh` script and adapt the config and calls to other script at the beginning, as needed for your project:

<!-- https://clay-atlas.com/us/blog/2021/06/30/html-en-copy-text-button/ -->
<script>
function copyEvent(id) {
    var str = document.getElementById(id);
    window.getSelection().selectAllChildren(str);
    document.execCommand("Copy")
}
</script>

[Here](https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/docs/generate_docs.sh) is an example `generate_docs.sh` file.
<button type="button" onclick="copyEvent('generatedocs')" class="clip-btn">Copy 'generate_docs.sh' to clipboard</button>

<pre id="generatedocs" class="sh_sh">
<!--%
include_url("https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/docs/generate_docs.sh")
%-->
</pre>

#### 5) Auto-generating and publishing docs

Add the `.github/workflows/docs.yml` script:

[Here](https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/.github/workflows/docs.yml) is an example `docs.yml` file.
<button type="button" onclick="copyEvent('docsyml')" class="clip-btn">Copy 'docs.yml' to clipboard</button>

<pre id="docsyml" class="sh_yaml">
<!--%
include_url("https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/.github/workflows/docs.yml")
%-->
</pre>

And don't forget to set the GitHub Pages source in the repo settings to GitHub Actions:

<!--%
lightgallery([
    [ "img/github_pages_actions.png", "What to change in the GitHub repo settings" ],
])
%-->

#### 6) STL 3D visualization

If you want to visualize 3D print files, do the same with `3dprint/generate_stls.sh` and `.github/workflows/scad.yml`:

[Here](https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/3dprint/generate_stls.sh) is an example `generate_stls.sh` file.
<button type="button" onclick="copyEvent('generatestls')" class="clip-btn">Copy 'generate_stls.sh' to clipboard</button>

<pre id="generatestls" class="sh_sh">
<!--%
include_url("https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/3dprint/generate_stls.sh")
%-->
</pre>

[Here](https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/.github/workflows/scad.yml) is an example `scad.yml` file.
<button type="button" onclick="copyEvent('scadyml')" class="clip-btn">Copy 'scad.yml' to clipboard</button>

<pre id="scadyml" class="sh_yaml">
<!--%
include_url("https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/.github/workflows/scad.yml")
%-->
</pre>

And then add something like this to the mdBook sources where you want the visualization to appear:

    \{{#include inc_enclosure_bottom.stl.md}}

    [Direct link to this file](./stl/enclosure_bottom.stl).

#### 7) PCB gerber files

If you want to generate gerber files from PCBs, do something similar with `pcb/generate_fab.sh` and `.github/workflows/kicad.yml`:

[Here](https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/pcb2/generate_fab.sh) is an example `generate_fab.sh` file.
<button type="button" onclick="copyEvent('generatefab')" class="clip-btn">Copy 'generate_fab.sh' to clipboard</button>

<pre id="generatefab" class="sh_sh">
<!--%
include_url("https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/pcb2/generate_fab.sh")
%-->
</pre>

[Here](https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/.github/workflows/kicad.yml) is an example `kicad.yml` file.
<button type="button" onclick="copyEvent('kicadyml')" class="clip-btn">Copy 'kicad.yml' to clipboard</button>

<pre id="kicadyml" class="sh_yaml">
<!--%
include_url("https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/.github/workflows/kicad.yml")
%-->
</pre>

#### 8) PCB visualization

If you want to visualize KiCad schematics and PCBs in 2D and 3D, add `pcb/generate_plot.sh`:

[Here](https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/pcb2/generate_plot.sh) is an example `generate_plot.sh` file.
<button type="button" onclick="copyEvent('generateplot')" class="clip-btn">Copy 'generate_plot.sh' to clipboard</button>

<pre id="generateplot" class="sh_sh">
<!--%
include_url("https://git.xythobuz.de/thomas/drumkit/raw/commit/314bf218ca5e958d6ffa825d92d702cb5431abf6/pcb2/generate_plot.sh")
%-->
</pre>

Then include this where you want the 2D schematic visualization to appear:

    You can also view the [schematics as PDF](./plot/lars2.kicad_sch.pdf).

    \{{#include inc_lars2.kicad_sch.md}}

And this where you want to visualize the 2D PCB layout:

    You can also view the [2D PCB layout as PDF](./plot/lars2.kicad_pcb.pdf).

    <script src="js/svg-pan-zoom.js" charset="UTF-8"></script>
    <div style="background-color: white; border: 1px solid black;">
        <embed type="image/svg+xml" src="./plot/lars2.kicad_pcb.svg" id="pz_drumkit0" style="width: 100%;"/>
        <script>
            document.getElementById('pz_drumkit0').addEventListener('load', function(){
                svgPanZoom(document.getElementById('pz_drumkit0'), {controlIconsEnabled: true, minZoom: 1.0});
            })
        </script>
    </div>

    [Direct link to this file](./plot/lars2.kicad_pcb.svg).

And add this where you want to visualize the 3D PCB layout:

    \{{#include inc_lars2.kicad_pcb.md}}

That should more or less be all that's required.

Of course, adapt paths as needed to match your project layout.
And test locally by calling the scripts manually on your machine:

    ./pcb/generate_plot.sh
    ./3dprint/generate_stls.sh

    ./docs/generate_docs.sh serve

Hope this helps.
