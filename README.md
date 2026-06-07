# emojilib
[![PyPI version](https://badge.fury.io/py/emojilib.svg)](https://badge.fury.io/py/emojilib)
[![Build and Publish](https://github.com/emoji-gen/emojilib/actions/workflows/build_and_publish.yml/badge.svg)](https://github.com/emoji-gen/emojilib/actions/workflows/build_and_publish.yml)

:books: Ultimate Emoji Generator library for Python
<br><br>

## System requirements

- Python 3.10 ~ 3.14
- C++20 Compiler

### Official supported platforms
We officially support building and running on these platforms below, but you can try it on other platforms.

- macOS 26 Tahoe (arm64)
- Ubuntu 24.04 (x86\_64)

## Used libraries

- [Cython](http://cython.org/)
- [libemoji](https://github.com/emoji-gen/libemoji) - Ultimate Emoji Generator library for C/C++

## Getting started

```
$ pip install emojilib --extra-index-url https://repo.fury.io/emoji-gen/
```

## Example

```python
import emojilib

def main():
    data = emojilib.generate(text="ab\nc.", width=128, height=128)

    with open('emoji.png', 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    main()
```

## How to build
### 1. Compile libemoji
First, please build externals.
See also [libemoji](https://github.com/emoji-gen/libemoji)'s README.

```
$ git submodule update --init --recursive
$ cd externals/libemoji
$ cmake .
$ make
```

### 2. Setup Python virtualenv
```
$ python -m venv venv
$ . venv/bin/activate
```

### 3. Run build command
```
$ python setup.py build
```

## Development
### Install Dependencies

```
$ pip install --group dev
```

### Test

```
$ pytest
```

### Publish

Update the version in pyproject.toml to the version you want to release.

Then, manually trigger the [build_and_publish.yml](https://github.com/emoji-gen/emojilib/actions/workflows/build_and_publish.yml) workflow via the workflow_dispatch event to create a release.

## See also
- [emojilib (Gemfury)](https://gemfury.com/emoji-gen/python:emojilib)
- [emojilib (PyPI)](https://pypi.org/project/emojilib/)

## License
MIT &copy; [Emoji Generator](https://emoji-gen.ninja)
