#!/bin/bash

set -eux -o pipefail

git submodule update --init --recursive

apt install unzip -y

for v in 3.5 3.6 3.7; do
  /usr/local/python-$v/bin/python -m pip install auditwheel
  /usr/local/python-$v/bin/python -m pip install -r requirements-dev.txt
done
