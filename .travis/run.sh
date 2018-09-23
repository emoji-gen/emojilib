#!/bin/bash

set -eu -o pipefail

PATH=/usr/local/opt/gnu-getopt/bin:$PATH

for v in 3.5 3.6 3.7; do
  ./scripts/clean.sh
  retry -- ~/local/python-$v/bin/python setup.py bdist_wheel install test
  retry -- ~/local/python-$v/bin/python ./scripts/publish.py --target=gemfury
  PATH=~/local/python-$v/bin:$PATH \
    retry -- ~/local/python-$v/bin/python ./scripts/publish.py --target=pypi
done
