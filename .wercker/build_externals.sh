#!/bin/bash

set -eux

cd externals/libemoji
cmake .
make
