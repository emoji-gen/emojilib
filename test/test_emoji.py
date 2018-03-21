# -*- encoding: utf-8 -*-

import pytest
from emojilib import generate


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
