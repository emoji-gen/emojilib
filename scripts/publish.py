#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import subprocess
from importlib import machinery
from pathlib import Path

import click
from git import Repo

GEMFURY_AS = 'emoji-gen'
GEMFURY_API_TOKEN = os.getenv('GEMFURY_API_TOKEN', '')
PYPI_USERNAME = os.getenv('PYPI_USERNAME', '')
PYPI_PASSWORD = os.getenv('PYPI_PASSWORD', '')
PACKAGE_NAME = 'emojilib'


def find_branch():
    if 'WERCKER_GIT_BRANCH' in os.environ:
        return os.environ['WERCKER_GIT_BRANCH']

    if 'TRAVIS_BRANCH' in os.environ:
        return os.environ['TRAVIS_BRANCH']

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
    process = subprocess.run(['fury', 'list',
        '--as=' + GEMFURY_AS, '--api-token=' + GEMFURY_API_TOKEN],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    packages = process.stdout.decode('utf-8')
    return packages


def find_gemfary_versions():
    process = subprocess.run(['fury', 'versions', PACKAGE_NAME,
        '--as=' + GEMFURY_AS, '--api-token=' + GEMFURY_API_TOKEN],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    versions = process.stdout.decode('utf-8')
    return versions


def find_wheel_path(version):
    paths = Path(__file__) \
        .resolve().parents[1].joinpath('dist') \
        .glob('*-{}-*.whl'.format(version))
    return str(list(paths)[0])


def push_to_gemfary(wheel_path):
    subprocess.run(['fury', 'push', wheel_path,
        '--as=' + GEMFURY_AS, '--api-token=' + GEMFURY_API_TOKEN], check=True)


def push_to_pypi(wheel_path, repository):
    repository_urls = {
        'pypi': 'https://upload.pypi.org/legacy/',
        'pypitest': 'https://test.pypi.org/legacy/',
    }
    subprocess.run(['twine', 'upload', '--repository-url', repository_urls[repository],
        '--username', PYPI_USERNAME, '--password', PYPI_PASSWORD, wheel_path], check=True)


@click.command()
@click.option(
    '--target',
    type=click.Choice(['gemfury', 'pypi', 'pypitest']),
    default='gemfury'
)
def publish(target):
    print('Target: ' + target)

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

    if target != 'gemfury':
        push_to_pypi(wheel_path, target)
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
            print('WARN: {} is already released'.format(release_version))

    push_to_gemfary(wheel_path)


if __name__ == '__main__':
    publish()
