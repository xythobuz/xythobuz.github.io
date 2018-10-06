#!/bin/bash

rm -rf output
mkdir output

./poole.py --build

cp -r static/* output/

./poole.py --serve
