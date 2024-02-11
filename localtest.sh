#!/bin/bash

echo "Cleaning"
rm -rf output
mkdir output

echo "Building"
./poole.py --build

echo "Copying"
cp -r static/* output/

echo "Serving"
./poole.py --serve
