#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from setuptools import Extension, setup
from Cython.Build import cythonize


extra_objects = [
    'lib/libemoji.a',
]
extra_compile_args = [
    '-std=c++20',
    '-Wall',
    '-Wextra',
]
extra_link_args = []
libraries = []

if sys.platform.startswith('darwin'):
    extra_link_args.extend([
        '-framework', 'CoreFoundation',
        '-framework', 'CoreGraphics',
        '-framework', 'CoreText',
        '-framework', 'CoreServices',
    ])
elif sys.platform.startswith('linux'):
    libraries.extend([
        'GL',
        'GLU',
        'dl',
        'fontconfig',
        'freetype',
        'z',
    ])


def main():
    extension = Extension(
        'emojilib',
        sources=['src/emojilib.pyx'],
        include_dirs=['include'],
        extra_objects=extra_objects,
        libraries=libraries,
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        language='c++'
    )
    setup(ext_modules=cythonize([extension]))


if __name__ == '__main__':
    main()
