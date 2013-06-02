#!/bin/bash
./poole.py --build
cp -r output/* ../apache/
cp -r static/* ../apache/