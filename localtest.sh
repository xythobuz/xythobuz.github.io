#!/bin/bash

set -e

echo "Cleaning"
rm -rf output
mkdir output

echo "Building"
./poole.py --build

echo "Minifying"
./minify.py static/js
#./minify.py static/js/sh
./minify.py --extension .css static/css

echo "Copying"
cp -r static/* output/

echo "Serving"
./poole.py --serve
