# emojilib
[![Build Status](https://travis-ci.org/emoji-gen/libemoji-py.svg?branch=master)](https://travis-ci.org/emoji-gen/libemoji-py) [![wercker status](https://app.wercker.com/status/f267cf98d7b5bb0b9de645f7ef53667b/s/master "wercker status")](https://app.wercker.com/project/byKey/f267cf98d7b5bb0b9de645f7ef53667b)

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
import emojilib

data = emoji.generate(text="絵文\n字。", width=128, height=128)

```

## Development
### Test

```
$ python setup.py test
```

## License
MIT &copy; Emoji Generator
