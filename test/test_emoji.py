# -*- encoding: utf-8 -*-

import pytest
from emojilib import generate

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
        generate(align=None)

    with pytest.raises(TypeError):
        generate(align=1)

    with pytest.raises(ValueError):
        generate(align='')

    with pytest.raises(ValueError):
        generate(align='unknown')
