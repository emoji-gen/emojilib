#!/bin/bash

set -eux

# 3.5
~/local/python-3.5/bin/python setup.py bdist_wheel install test
~/local/python-3.5/bin/python ./scripts/publish.py
./scripts/clean.sh

# 3.6
~/local/python-3.6/bin/python setup.py bdist_wheel install test
~/local/python-3.6/bin/python ./scripts/publish.py
./scripts/clean.sh

# 3.7
~/local/python-3.7/bin/python setup.py bdist_wheel install test
~/local/python-3.7/bin/python ./scripts/publish.py
