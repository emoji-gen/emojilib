#!/bin/bash

set -eu -o pipefail

PATH=/usr/local/opt/gnu-getopt/bin:$PATH

# 3.5
./scripts/clean.sh
retry -- ~/local/python-3.5/bin/python setup.py bdist_wheel install test
retry -- ~/local/python-3.5/bin/python ./scripts/publish.py --target=gemfury
PATH=~/local/python-3.5/bin:$PATH \
  retry -- ~/local/python-3.5/bin/python ./scripts/publish.py --target=pypi

# 3.6
./scripts/clean.sh
retry -- ~/local/python-3.6/bin/python setup.py bdist_wheel install test
retry -- ~/local/python-3.6/bin/python ./scripts/publish.py --target=gemfury
PATH=~/local/python-3.6/bin:$PATH \
  retry -- ~/local/python-3.6/bin/python ./scripts/publish.py --target=pypi

# 3.7
./scripts/clean.sh
retry -- ~/local/python-3.7/bin/python setup.py bdist_wheel install test
retry -- ~/local/python-3.7/bin/python ./scripts/publish.py --target=gemfury
PATH=~/local/python-3.7/bin:$PATH \
  retry -- ~/local/python-3.7/bin/python ./scripts/publish.py --target=pypi
