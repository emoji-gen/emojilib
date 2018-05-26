#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from setuptools import setup, Extension

VERSION = '0.1.4'


extra_objects = [
    'lib/libemoji.a',
]
extra_compile_args = [
    '-std=c11',
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
        'dl',
        'fontconfig',
        'freetype',
        'GL',
        'GLU',
    ])


def main():
    module = Extension(
        'emojilib',
        sources=['src/emojilib.c'],
        include_dirs=['include'],
        extra_objects=extra_objects,
        libraries=libraries,
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        language='c11'
    )

    setup(
        name='emojilib',
        version=VERSION,
        description='Ultimate Emoji Generator library using Skia and Python C Extension',
        url='https://github.com/emoji-gen/emojilib',
        author='Emoji Generator',
        author_email='pinemz+emoji@gmail.com',
        license='MIT License',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        ext_modules=[module]
    )


if __name__ == '__main__':
    main()
