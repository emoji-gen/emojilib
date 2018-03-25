#!/bin/bash

set -eux

~/local/python-3.5/bin/python setup.py bdist_wheel install test
~/local/python-3.5/bin/python ./scripts/publish.py

./scripts/clean.sh

~/local/python-3.6/bin/python setup.py bdist_wheel install test
~/local/python-3.6/bin/python ./scripts/publish.py

