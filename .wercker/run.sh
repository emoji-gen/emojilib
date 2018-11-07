#!/bin/bash

set -eux -o pipefail

for v in 3.5 3.6 3.7; do
  ./scripts/clean.sh
  /usr/local/python-$v/bin/python setup.py bdist_wheel install test
  PATH=/usr/local/python-$v/bin:$PATH \
    /usr/local/python-$v/bin/python scripts/publish.py --target=pypi
  /usr/local/python-$v/bin/python scripts/publish.py --target=gemfury
done

