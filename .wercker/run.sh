#!/bin/bash

set -eux

# 3.5
./scripts/clean.sh
/usr/local/python-3.5/bin/python setup.py bdist_wheel install test
/usr/local/python-3.5/bin/python scripts/publish.py --target=gemfury
/usr/local/python-3.5/bin/python scripts/publish.py --target=pypi

# 3.6
./scripts/clean.sh
/usr/local/python-3.6/bin/python setup.py bdist_wheel install test
/usr/local/python-3.6/bin/python scripts/publish.py --target=gemfury
/usr/local/python-3.6/bin/python scripts/publish.py --target=pypi

# 3.7
./scripts/clean.sh
/usr/local/python-3.7/bin/python setup.py bdist_wheel install test
/usr/local/python-3.7/bin/python scripts/publish.py --target=gemfury
/usr/local/python-3.7/bin/python scripts/publish.py --target=pypi
