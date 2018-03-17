#!/bin/bash

set -eux

# install pyenv
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
gem gemfury --no-document
