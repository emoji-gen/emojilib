#!/bin/bash

set -eux

/usr/local/python-3.5/bin/python setup.py bdist_wheel install test
/usr/local/python-3.5/bin/python scripts/publish.py

./scripts/clean.sh

/usr/local/python-3.6/bin/python setup.py bdist_wheel install test
/usr/local/python-3.6/bin/python scripts/publish.py
