#!/bin/bash

set -eux

PATH=/usr/local/opt/gnu-getopt/bin:$PATH

# 3.5
which retry
retry -- ~/local/python-3.5/bin/python setup.py bdist_wheel install test
retry -- ~/local/python-3.5/bin/python ./scripts/publish.py
./scripts/clean.sh

# 3.6
retry -- ~/local/python-3.6/bin/python setup.py bdist_wheel install test
retry -- ~/local/python-3.6/bin/python ./scripts/publish.py
./scripts/clean.sh

# 3.7
retry -- ~/local/python-3.7/bin/python setup.py bdist_wheel install test
retry -- ~/local/python-3.7/bin/python ./scripts/publish.py
