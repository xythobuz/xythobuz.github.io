#!/bin/bash

set -e

echo "Cleaning"
rm -rf output
mkdir output
rm -rf errors_html.log errors_css.log

echo "Building"
./poole.py --build

echo "Minifying"
./minify.py static/js
#./minify.py static/js/sh
./minify.py --extension .css static/css

VNU_EXT="--skip-non-html --also-check-css --format text --stdout"

echo "Validating HTML"
java -jar ~/bin/vnu.jar $VNU_EXT output | tee errors_html.log

echo "Validating CSS"
java -jar ~/bin/vnu.jar $VNU_EXT static/css | tee errors_css.log

echo "Copying"
cp -r static/* output/

echo "Serving"
./poole.py --serve
