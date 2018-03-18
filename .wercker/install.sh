#!/bin/bash

set -eux

git submodule update --init --recursive

/usr/local/python-3.5/bin/python  -m pip install -r requirements-dev.txt
/usr/local/python-3.6/bin/python  -m pip install -r requirements-dev.txt

gem install gemfury --no-document
