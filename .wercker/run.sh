#!/bin/bash

set -eux -o pipefail

for v in 3.6 3.7 3.8; do
  ./scripts/clean.sh
  /usr/local/python-$v/bin/python setup.py bdist_wheel install test
  /usr/local/python-$v/bin/python scripts/publish.py --target=gemfury
done

