#!/bin/bash

set -eux -o pipefail

PYTHON_36_VERSION=3.6.10
PYTHON_37_VERSION=3.7.6
PYTHON_38_VERSION=3.8.2

# install lfs
brew install git-lfs
git lfs install
git lfs pull

# install retry
brew install gnu-getopt
sudo curl https://raw.githubusercontent.com/kadwanev/retry/master/retry -o /usr/local/bin/retry
sudo chmod +x /usr/local/bin/retry

# install python
mkdir -p ~/local
git clone https://github.com/tagomoris/xbuild.git ~/local/xbuild
~/local/xbuild/python-install -f $PYTHON_36_VERSION ~/local/python-3.6
~/local/xbuild/python-install -f $PYTHON_37_VERSION ~/local/python-3.7
~/local/xbuild/python-install -f $PYTHON_38_VERSION ~/local/python-3.8

# install requirements
for v in 3.6 3.7 3.8; do
  ~/local/python-$v/bin/pip3 install 'wheel==0.31.1'
  ~/local/python-$v/bin/pip3 install -r requirements-dev.txt
done
gem install gemfury --no-document
