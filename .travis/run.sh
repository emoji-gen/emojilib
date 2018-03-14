#!/bin/bash

set -eux

# setup pyenv
PYENV_ROOT="$HOME/.pyenv"
PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# setup venv
VIRTUAL_ENV_DISABLE_PROMPT=true
source .venv/bin/activate

# build
python setup.py build
cp build/lib.*/emoji.*.so .

# test
python setup.py test
