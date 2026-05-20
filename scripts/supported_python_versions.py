#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import re
import tomllib

def main():
    with open('pyproject.toml', 'rb') as f:
        pyproject = tomllib.load(f)

    classifiers  = pyproject['project']['classifiers']
    versions = []
    for classifier in classifiers:
        m = re. fullmatch('Programming Language :: Python :: (\\d\\.\\d+)', classifier)
        if m:
            versions.append(m.group(1))

    sorted_versions = sorted(versions)
    print(json.dumps(sorted_versions, separators=(',', ':')))

if __name__ == '__main__':
    main()
