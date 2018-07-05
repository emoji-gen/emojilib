# emojilib &nbsp;[![Build Status](https://travis-ci.org/emoji-gen/emojilib.svg?branch=master)](https://travis-ci.org/emoji-gen/emojilib) [![wercker status](https://app.wercker.com/status/486fa62cf2efbf47c595632b1e902e58/s/master "wercker status")](https://app.wercker.com/project/byKey/486fa62cf2efbf47c595632b1e902e58) [![Osushi](https://img.shields.io/badge/donate-osushi-EA2F57.svg)](https://osushi.love/intent/post/9ad90add99954e62ac79251606c10eec)

:books: Ultimate Emoji Generator library for Python

## System requirements

- Python 3.5, 3.6 or 3.7
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

    with open('emoji.png') as f:
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
MIT &copy; [Emoji Generator](https://emoji-gen.ninja)
