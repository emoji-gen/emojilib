# emojilib &nbsp;[![Build Status](https://travis-ci.org/emoji-gen/emojilib.svg?branch=master)](https://travis-ci.org/emoji-gen/emojilib) [![wercker status](https://app.wercker.com/status/486fa62cf2efbf47c595632b1e902e58/s/master "wercker status")](https://app.wercker.com/project/byKey/486fa62cf2efbf47c595632b1e902e58)

:books: Ultimate Emoji Generator library for Python

## System requirements

- Python 3.5.x or later
- C11 Compiler

## Official supported platforms

- macOS 10.12 Sierra
- Debian 9 Stretch

## Getting started

```
$ pip install emojilib --extra-index-url https://repo.fury.io/emoji-gen/
```

## Example

```python
import emojilib

def main():
    data = emojilib.generate(text="絵文\n字。", width=128, height=128)
    // TODO

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
### Test requirements

- Git LFS

### Test

```
$ git lfs pull
$ pip install -r requirements-dev.txt
$ python setup.py build install test
```

### Create wheel package

```
$ pip install wheel --upgrade
$ python setup.py bdist_wheel
```

## License
MIT &copy; Emoji Generator
