# -*- encoding: utf-8 -*-

import json
import re
import sys
import tomllib

def main():
    if len(sys.argv) < 2:
        sys.exit('Please specify the path to pyproject.toml as a command-line argument.')

    pyproject_path = sys.argv[1]
    with open(pyproject_path, 'rb') as f:
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
