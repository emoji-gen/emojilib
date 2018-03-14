#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import subprocess

from pygit2 import Repository

GEMFURY_AS = 'emoji-gen'
PACKAGE_NAME = 'libemoji'

def publish():
    repo = Repository('.')
    branch = repo.head.shorthand
    in_release_branch = branch.startswith('release/')

    print('Branch: ' + branch)
    print('In release branch: {}'.format(in_release_branch))

    if not in_release_branch:
        print('Not in release branch')
        return

    subprocess.run(['fury', '-v'], stdout=subprocess.PIPE, check=True)
    process = subprocess.run(
        ['fury', 'list', '--as=' + GEMFURY_AS], stdout=subprocess.PIPE, check=True)
    packages = process.stdout.decode('utf-8')

    if PACKAGE_NAME not in packages:
        print(packages)
        sys.exit('ERROR: `{}` is not found in gemfury'.format(PACKAGE_NAME))

    process = subprocess.run(
        ['fury', 'versions', PACKAGE_NAME, '--as=' + GEMFURY_AS],
        stdout=subprocess.PIPE, check=True)
    versions = process.stdout.decode('utf-8')
    print(versions)


if __name__ == '__main__':
    publish()
