#!/bin/bash

set -eux

PYTHON_35_VERSION=3.5.5
PYTHON_36_VERSION=3.6.5
PYTHON_37_VERSION=3.7.0

# install lfs
brew install git-lfs
git lfs install
git lfs pull

# install retry
curl https://raw.githubusercontent.com/kadwanev/retry/master/retry -o /usr/bin/retry
chmod +x /usr/bin/retry

# install python
mkdir -p ~/local
git clone https://github.com/tagomoris/xbuild.git ~/local/xbuild
~/local/xbuild/python-install -f $PYTHON_35_VERSION ~/local/python-3.5
~/local/xbuild/python-install -f $PYTHON_36_VERSION ~/local/python-3.6
~/local/xbuild/python-install -f $PYTHON_37_VERSION ~/local/python-3.7
~/local/python-3.5/bin/pip3 install --upgrade pip
~/local/python-3.6/bin/pip3 install --upgrade pip
~/local/python-3.7/bin/pip3 install --upgrade pip
~/local/python-3.5/bin/pip3 install --upgrade wheel
~/local/python-3.6/bin/pip3 install --upgrade wheel
~/local/python-3.7/bin/pip3 install --upgrade wheel

# install requirements
~/local/python-3.5/bin/pip3 install -r requirements-dev.txt
~/local/python-3.6/bin/pip3 install -r requirements-dev.txt
~/local/python-3.7/bin/pip3 install -r requirements-dev.txt
gem install gemfury --no-document
