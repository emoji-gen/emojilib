libemoji-py
-----------

## System requirements

- macOS or Ubuntu
- Python 3.5.x or later
- C11 Compiler

## How to build
### 1. Compile libemoji
First, please build [libemoji](https://github.com/emoji-gen/libemoji) and copy `libskia.a` and `libemoji.a` for the lib directory

### 2. Setup Python virtualenv
```
$ python -m venv venv
$ . venv/bin/activate
```

### 3. Run build command
```
$ python setup.py build
```

## License
MIT &copy; Pine Mizune
