import unittest

import emoji

class EmojiTest(unittest.TestCase):
    def test_generate_kwargs_color(self):
        kwargs = { 'text': "a", 'width': 16, 'height': 16 }
        self.assertIsInstance(emoji.generate(**kwargs), bytes)
        self.assertIsInstance(emoji.generate(color='FFFFFFFF', **kwargs), bytes)
        self.assertIsInstance(emoji.generate(color='#FFFFFFFF', **kwargs), bytes)


    def test_generate_kwargs_align(self):
        kwargs = { 'text': "a", 'width': 16, 'height': 16 }
        self.assertIsInstance(emoji.generate(**kwargs), bytes)
        self.assertIsInstance(emoji.generate(align='left', **kwargs), bytes)
        self.assertIsInstance(emoji.generate(align='Left', **kwargs), bytes)
        self.assertIsInstance(emoji.generate(align='LEFT', **kwargs), bytes)
        self.assertIsInstance(emoji.generate(align='center', **kwargs), bytes)
        self.assertIsInstance(emoji.generate(align='right', **kwargs), bytes)

        with self.assertRaises(TypeError):
            emoji.generate(align=None)

        with self.assertRaises(TypeError):
            emoji.generate(align=1)

        with self.assertRaises(ValueError):
            emoji.generate(align='')

        with self.assertRaises(ValueError):
            emoji.generate(align='unknown')
