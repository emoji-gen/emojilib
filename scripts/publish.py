#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import subprocess
from importlib import machinery
from pathlib import Path

from git import Repo

GEMFURY_AS = 'emoji-gen'
PACKAGE_NAME = 'libemoji'


def find_branch():
    wercker_branch = os.environ['WERCKER_GIT_BRANCH']
    if wercker_branch:
        return wercker_branch

    repo = Repo('.')
    branch = repo.active_branch
    return branch.name


def find_release_version():
    path = Path(__file__).resolve().parents[1].joinpath('setup.py')
    loader = machinery.SourceFileLoader('emoji_setup', str(path))
    module = loader.load_module()
    return module.VERSION


def find_gemfary_packages():
    subprocess.run(['fury', '-v'], stdout=subprocess.PIPE, check=True)
    process = subprocess.run(
        ['fury', 'list', '--as=' + GEMFURY_AS], stdout=subprocess.PIPE, check=True)
    packages = process.stdout.decode('utf-8')
    return packages


def find_gemfary_versions():
    process = subprocess.run(
        ['fury', 'versions', PACKAGE_NAME, '--as=' + GEMFURY_AS],
        stdout=subprocess.PIPE, check=True)
    versions = process.stdout.decode('utf-8')
    return versions


def find_wheel_path(version):
    paths = Path(__file__) \
        .resolve().parents[1].joinpath('dist') \
        .glob('*-{}-*.whl'.format(version))
    return list(paths)[0]


def push_to_gemfary(wheel_path):
    subprocess.run(['fury', 'push', wheel_path, '--as=' + GEMFURY_AS], check=True)


def publish():
    branch = find_branch()
    print('Branch: ' + branch)

    if not branch:
        print('branch not found')
        return

    in_release_branch = branch.startswith('release/')
    release_version = find_release_version()
    wheel_path = find_wheel_path(release_version)

    print('In release branch: {}'.format(in_release_branch))
    print('Release version: {}'.format(release_version))
    print('Wheel path: {}'.format(wheel_path))

    if not in_release_branch:
        print('Not in release branch')
        return

    if not release_version:
        sys.exit('release version not found')

    if not wheel_path:
        print('wheel path not found')
        return

    packages = find_gemfary_packages()
    print(packages)

    package_created = PACKAGE_NAME in packages
    if not package_created:
        print('WARN: `{}` is not found in gemfury'.format(PACKAGE_NAME))

    if package_created:
        versions = find_gemfary_versions()
        print(versions)

        if release_version in versions:
            print('{} is already released'.format(release_version))
            return

    push_to_gemfary(wheel_path)


if __name__ == '__main__':
    publish()
