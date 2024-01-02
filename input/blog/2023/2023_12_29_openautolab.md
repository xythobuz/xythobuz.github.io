title: Blog
post: 'OpenAutoLab' by Kauzerei
description: Open-Source automatic film development machine
date: 2023-12-29
update: 2024-01-02
comments: false
github: https://github.com/kauzerei/openautolab
---

My good friend [Kauzerei](https://github.com/kauzerei) has built [the automatic film development machine OpenAutoLab](https://github.com/kauzerei/openautolab).

<!--%
lightgallery([
    [ "https://www.youtube.com/watch?v=qe7pgEp7S68", "OpenAutoLab demo video" ],
    [ "img/openautolab_front.png", "OpenAutoLab without heating option" ],
    [ "img/openautolab_37c3.jpg", "OpenAutoLab with RGB LEDs at 37C3" ],
])
%-->

Please also take a look at [the OpenAutoLab documentation](https://kauzerei.github.io/openautolab/) for detailed build and usage instructions.

## Background

I haven't really participated in the construction of this machine in any way.
But we went to 37C3 together, where I fully saw the machine in action for the first time.
While socializing we noticed that it is (or was) really hard to find the project by googling.
Neither 'openautolab', 'kauzerei', 'github openautolab kauzerei', or any other combination of these words and quotation marks, no results at all came up.

Therefore I decided to do some "SEO" in the hopes of making it easier for people remembering the name to find the project.
I also wanted to play around a bit more with GitHub Actions, or CI in general, and GitHub Pages.
So I came up with [the OpenAutoLab documentation](https://kauzerei.github.io/openautolab/).
The job was actually pretty easy, because the hard work of writing most of the documentation was already done.
I just had to find a suitable way of converting these markdown files to html, and host them on GitHub Pages, preferably automated.
The result is [this GitHub Actions workflow](https://github.com/kauzerei/openautolab/blob/main/.github/workflows/deploy.yml) using [mdBook](https://rust-lang.github.io/mdBook/).

While thinking about making it easier for "normal users" to use this project, I decided to also test out making a web flashing utility.
The main board of OpenAutoLab contains an Arduino Nano, so it can be updated via WebSerial using a [compatible browser](https://developer.mozilla.org/en-US/docs/Web/API/Web_Serial_API#browser_compatibility) (only Chromium based ones, unfortunately).
To do this I used [avrgirl-arduino](https://github.com/sudevkrishnan/avrgirl-arduino) for the update process, and [zip.js](https://gildas-lormeau.github.io/zip.js/), and wrote some JavaScript to fetch binaries from GitHub releases or GitHub actions.
The result it [this web flashing utility](https://kauzerei.github.io/openautolab/web_update.html).

Of course I also had to add a [workflow to build the firmware hex](https://github.com/kauzerei/openautolab/blob/main/.github/workflows/compile.yml) on each commit push and upload the artifact for new GitHub releases / tags.
And I did the same for [generating the STL files from the OpenSCAD sources](https://github.com/kauzerei/openautolab/blob/main/.github/workflows/scad.yml).

![Firmware](https://github.com/kauzerei/openautolab/actions/workflows/compile.yml/badge.svg)
![STLs](https://github.com/kauzerei/openautolab/actions/workflows/scad.yml/badge.svg)
![Documentation](https://github.com/kauzerei/openautolab/actions/workflows/deploy.yml/badge.svg)

I'm quite happy with the results.
So this was my small share of hacking on 37C3.
