# -*- encoding: utf-8 -*-

import pytest
from emojilib import generate


def test_generate_kwargs_text():
    kwargs = { 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(text='a', **kwargs), bytes)

    with pytest.raises(TypeError):
        generate(text=None, **kwargs)
    with pytest.raises(TypeError):
        generate(text=0, **kwargs)
    with pytest.raises(ValueError):
        generate(text='', **kwargs)


def test_generate_kwargs_width():
    kwargs = { 'text': 'a', 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(width=128, **kwargs), bytes)

    with pytest.raises(TypeError):
        generate(width=None, **kwargs)
    with pytest.raises(TypeError):
        generate(width='', **kwargs)
    with pytest.raises(ValueError):
        generate(width=-1, **kwargs)
    with pytest.raises(ValueError):
        generate(width=0, **kwargs)


def test_generate_kwargs_height():
    kwargs = { 'text': 'a', 'width': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(height=128, **kwargs), bytes)

    with pytest.raises(TypeError):
        generate(height=None, **kwargs)
    with pytest.raises(TypeError):
        generate(height='', **kwargs)
    with pytest.raises(ValueError):
        generate(height=-1, **kwargs)
    with pytest.raises(ValueError):
        generate(height=0, **kwargs)


def test_generate_kwargs_color():
    kwargs = { 'text': "a", 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(color='FFFFFFFF', **kwargs), bytes)
    assert isinstance(generate(color='#FFFFFFFF', **kwargs), bytes)


def test_generate_kwargs_background_color():
    kwargs = { 'text': "a", 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(background_color='FFFFFFFF', **kwargs), bytes)
    assert isinstance(generate(background_color='#FFFFFFFF', **kwargs), bytes)


def test_generate_kwargs_align():
    kwargs = { 'text': "a", 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(align='left', **kwargs), bytes)
    assert isinstance(generate(align='Left', **kwargs), bytes)
    assert isinstance(generate(align='LEFT', **kwargs), bytes)
    assert isinstance(generate(align='center', **kwargs), bytes)
    assert isinstance(generate(align='right', **kwargs), bytes)

    with pytest.raises(TypeError):
        generate(align=None, **kwargs)
    with pytest.raises(TypeError):
        generate(align=1, **kwargs)
    with pytest.raises(ValueError):
        generate(align='', **kwargs)
    with pytest.raises(ValueError):
        generate(align='unknown', **kwargs)


def test_generate_kwargs_size_fixed():
    kwargs = { 'text': 'a', 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(size_fixed=None, **kwargs), bytes)
    assert isinstance(generate(size_fixed=True, **kwargs), bytes)
    assert isinstance(generate(size_fixed=1, **kwargs), bytes)
    assert isinstance(generate(size_fixed='a', **kwargs), bytes)
    assert isinstance(generate(size_fixed=False, **kwargs), bytes)
    assert isinstance(generate(size_fixed=0, **kwargs), bytes)
    assert isinstance(generate(size_fixed='', **kwargs), bytes)


def test_generate_kwargs_disable_stretch():
    kwargs = { 'text': 'a', 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(disable_stretch=None, **kwargs), bytes)
    assert isinstance(generate(disable_stretch=True, **kwargs), bytes)
    assert isinstance(generate(disable_stretch=1, **kwargs), bytes)
    assert isinstance(generate(disable_stretch='a', **kwargs), bytes)
    assert isinstance(generate(disable_stretch=False, **kwargs), bytes)
    assert isinstance(generate(disable_stretch=0, **kwargs), bytes)
    assert isinstance(generate(disable_stretch='', **kwargs), bytes)


def test_generate_kwargs_typeface_file():
    kwargs = { 'text': 'a', 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(typeface_file='/XXXXXXXXXXX/X/XXX.ttf', **kwargs), bytes)

    with pytest.raises(TypeError):
        generate(typeface_file=None, **kwargs)
    with pytest.raises(TypeError):
        generate(typeface_file=1, **kwargs)
    with pytest.raises(ValueError):
        generate(typeface_file='', **kwargs)


def test_generate_kwargs_format():
    kwargs = { 'text': 'a', 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(format='png', **kwargs), bytes)
    assert isinstance(generate(format='Png', **kwargs), bytes)
    assert isinstance(generate(format='PNG', **kwargs), bytes)
    assert isinstance(generate(format='webp', **kwargs), bytes)
    assert isinstance(generate(format='Webp', **kwargs), bytes)
    assert isinstance(generate(format='WEBP', **kwargs), bytes)

    with pytest.raises(TypeError):
        generate(format=None, **kwargs)
    with pytest.raises(TypeError):
        generate(format=1, **kwargs)
    with pytest.raises(ValueError):
        generate(format='', **kwargs)
    with pytest.raises(ValueError):
        generate(format='unknown', **kwargs)


def test_generate_kwargs_quality():
    kwargs = { 'text': 'a', 'width': 16, 'height': 16 }

    assert isinstance(generate(**kwargs), bytes)
    assert isinstance(generate(quality=0, **kwargs), bytes)
    assert isinstance(generate(quality=1, **kwargs), bytes)
    assert isinstance(generate(quality=99, **kwargs), bytes)
    assert isinstance(generate(quality=100, **kwargs), bytes)

    with pytest.raises(TypeError):
        generate(quality=None, **kwargs)
    with pytest.raises(TypeError):
        generate(quality='', **kwargs)
    with pytest.raises(ValueError):
        generate(quality=-1, **kwargs)
    with pytest.raises(ValueError):
        generate(quality=101, **kwargs)
