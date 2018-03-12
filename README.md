# libemoji for Python
[![Build Status](https://travis-ci.org/emoji-gen/libemoji-py.svg?branch=master)](https://travis-ci.org/emoji-gen/libemoji-py)

## System requirements

- macOS or Ubuntu
- Python 3.5.x or later
- C11 Compiler

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
import emoji

data = emoji.generate(text="絵文字。", width=128, height=128)

```

## License
MIT &copy; Emoji Generator
