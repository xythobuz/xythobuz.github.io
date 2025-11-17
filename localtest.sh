#!/usr/bin/env bash

set -e

echo "Cleaning"
rm -rf output
mkdir output
rm -rf errors_html.log errors_css.log
echo

echo "Building"
./poole.py --build
echo

echo "Minifying"
./minify.py static/js
#./minify.py static/js/sh
./minify.py --extension .css static/css
echo

VNU_EXT="--skip-non-html --also-check-css --format text --stdout"

echo "Validating HTML"
java -jar ~/bin/vnu.jar $VNU_EXT output | tee errors_html.log
echo

echo "Validating CSS"
java -jar ~/bin/vnu.jar $VNU_EXT static/css static/lg static/emu_js | tee errors_css.log
echo

echo "Validating RSS"
./validate_rss.sh
echo

echo "Copying"
cp -r static/* output/
echo

echo "Serving"
./poole.py --serve
