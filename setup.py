#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from setuptools import setup, Extension


extra_link_args = []
if sys.platform.startswith('darwin'):
    extra_link_args.extend([
        '-framework', 'CoreFoundation',
        '-framework', 'CoreGraphics',
        '-framework', 'CoreText',
        '-framework', 'CoreServices',
    ])
elif sys.platform.startswith('linux'):
    extra_link_args.extend([
        '-fPIC',
    ])



module = Extension(
    'emoji',
    sources=['src/emoji.c'],
    include_dirs = ['include'],
    library_dirs = ['lib'],
    libraries= ['z', 'skia', 'emoji'],
    extra_compile_args=[
        '-std=c11',
        '-Wall',
        '-Wextra',
    ],
    extra_link_args=extra_link_args,
    language='c11'
)

setup(
    name='libemoji',
    version='0.1.1',
    description = 'Ultimate Emoji Generator library using Skia and Python C Extension',
    url='https://github.com/emoji-gen/libemoji-py',
    author='Emoji Generator',
    author_email='pinemz+emoji@gmail.com',
    classifier=[
        'License :: OSI Approved :: MIT License',
    ],
    test_suite='test.emoji',
    ext_modules=[module]
)
