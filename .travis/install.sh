#!/bin/bash

set -eux

PYTHON_35_VERSION=3.5.5
PYTHON_36_VERSION=3.6.4

# install lfs
brew install git-lfs
git lfs install
git lfs pull

# install python
mkdir -p ~/local
git clone https://github.com/tagomoris/xbuild.git ~/local/xbuild
~/local/xbuild/python-install -f $PYTHON_35_VERSION ~/local/python-3.5
~/local/xbuild/python-install -f $PYTHON_36_VERSION ~/local/python-3.6

# install requirements
~/local/python-3.5/bin/pip3 install -r requirements-dev.txt
~/local/python-3.6/bin/pip3 install -r requirements-dev.txt
~/local/python-3.5/bin/pip3 install --upgrade wheel
~/local/python-3.6/bin/pip3 install --upgrade wheel
gem install gemfury --no-document
