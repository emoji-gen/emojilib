#!/bin/bash

set -eux

# install pyenv
git clone --depth 1 https://github.com/pyenv/pyenv ~/.pyenv
PYENV_ROOT="$HOME/.pyenv"
PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv install 3.6.4
pyenv global 3.6.4
pyenv rehash

python -m pip install --user virtualenv
python -m virtualenv .venv
source .venv/bin/activate
