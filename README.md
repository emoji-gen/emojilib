# emojilib &nbsp;[![Build Status](https://travis-ci.org/emoji-gen/emojilib.svg?branch=master)](https://travis-ci.org/emoji-gen/emojilib) [![wercker status](https://app.wercker.com/status/290fdb66111b86139911b59a84332720/s/master "wercker status")](https://app.wercker.com/project/byKey/290fdb66111b86139911b59a84332720)

:books: Ultimate Emoji Generator library for Python

## System requirements

- Python 3.5.x or later
- C11 Compiler

## Official supported platforms

- macOS 10.12 Sierra
- Debian 9 Stretch

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

## Example

```python
import pyemoji

data = pyemoji.generate(text="絵文\n字。", width=128, height=128)

```

## Development
### Test

```
$ python setup.py build
$ cp build/lib.*/pyemoji.*.so .
$ python setup.py test
```

### Create wheel package

```
$ pip install wheel --upgrade
$ python setup.py bdist_wheel
```

## License
MIT &copy; Emoji Generator
