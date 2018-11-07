#!/bin/bash

set -eux -o pipefail

git submodule update --init --recursive

apt-get update -qq
apt-get -qq install -y --no-install-recommends unzip patchelf

for v in 3.5 3.6 3.7; do
  /usr/local/python-$v/bin/python -m pip install auditwheel
  /usr/local/python-$v/bin/python -m pip install 'wheel==0.31.1'
  /usr/local/python-$v/bin/python -m pip install -r requirements-dev.txt
done
