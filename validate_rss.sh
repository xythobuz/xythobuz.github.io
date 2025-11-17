#!/usr/bin/env bash

ORIG=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd ~/Projekte/extern/feedvalidator
source ./venv/bin/activate

python src/demo.py $ORIG/output/rss.xml
exit 0
