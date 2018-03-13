# -*- encoding: utf-8 -*-

import pytest
import emoji

def test_generate_kwargs_color():
    kwargs = { 'text': "a", 'width': 16, 'height': 16 }
    assert isinstance(emoji.generate(**kwargs), bytes)
    assert isinstance(emoji.generate(color='FFFFFFFF', **kwargs), bytes)
    assert isinstance(emoji.generate(color='#FFFFFFFF', **kwargs), bytes)


def test_generate_kwargs_align():
    kwargs = { 'text': "a", 'width': 16, 'height': 16 }
    assert isinstance(emoji.generate(**kwargs), bytes)
    assert isinstance(emoji.generate(align='left', **kwargs), bytes)
    assert isinstance(emoji.generate(align='Left', **kwargs), bytes)
    assert isinstance(emoji.generate(align='LEFT', **kwargs), bytes)
    assert isinstance(emoji.generate(align='center', **kwargs), bytes)
    assert isinstance(emoji.generate(align='right', **kwargs), bytes)

    with pytest.raises(TypeError):
        emoji.generate(align=None)

    with pytest.raises(TypeError):
        emoji.generate(align=1)

    with pytest.raises(ValueError):
        emoji.generate(align='')

    with pytest.raises(ValueError):
        emoji.generate(align='unknown')
