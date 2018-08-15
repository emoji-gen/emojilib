#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import emojilib

def main():
    data = emojilib.generate(
        text="絵文\n字。",
        width=128,
        height=128,
        typeface_file='./example/NotoSansMonoCJKjp-Bold.otf'
    )

    with open('./example/emoji.png', 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    main()
