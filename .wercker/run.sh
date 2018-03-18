#!/bin/bash

set -eux

/usr/local/python-3.5/bin/python setup.py bdist_wheel
cp build/lib.*/pyemoji.*.so .

/usr/local/python-3.6/bin/python setup.py bdist_wheel
cp build/lib.*/pyemoji.*.so .
