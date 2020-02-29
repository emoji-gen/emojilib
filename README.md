# emojilib
[![PyPI version](https://badge.fury.io/py/emojilib.svg)](https://badge.fury.io/py/emojilib)
[![Build Status](https://travis-ci.org/emoji-gen/emojilib.svg?branch=master)](https://travis-ci.org/emoji-gen/emojilib)
[![wercker status](https://app.wercker.com/status/486fa62cf2efbf47c595632b1e902e58/s/master "wercker status")](https://app.wercker.com/project/byKey/486fa62cf2efbf47c595632b1e902e58)
[![Requirements Status](https://requires.io/github/emoji-gen/emojilib/requirements.svg?branch=master)](https://requires.io/github/emoji-gen/emojilib/requirements/?branch=master)

:books: Ultimate Emoji Generator library for Python
<br><br>

## System requirements

- Python 3.6, 3.7 or 3.8
- C11 Compiler

### Official supported platforms
We officially support building and running on these platforms below, but you can try it on other platforms.

- macOS 10.14 Mojave
- macOS 10.15 Catalina
- Debian 10 Buster

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
### Dependencies

```
$ pip install -r requirements-dev.txt
```

### Example

```
$ python setup.py install
$ python ./example/example.py
```

### Test

```
$ python setup.py build install test
```

### Create wheel package

```
$ pip install wheel --upgrade
$ python setup.py bdist_wheel
```

## See also
- [emojilib (Gemfury)](https://gemfury.com/emoji-gen/python:emojilib)
- [emojilib (PyPI)](https://pypi.org/project/emojilib/)

## License
MIT &copy; [Emoji Generator](https://emoji-gen.ninja)
