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

git clone --depth 1 https://github.com/pyenv/pyenv ~/.pyenv
PYENV_ROOT="$HOME/.pyenv"
PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# install python
pyenv install 3.6.4
pyenv global 3.6.4
pyenv rehash

# install virtualenv
python -m pip install --user virtualenv
python -m virtualenv .venv

# setup virtualenv
VIRTUAL_ENV_DISABLE_PROMPT=true
source .venv/bin/activate

# install requirements
pip install -r requirements-dev.txt
gem install gemfury --no-document
