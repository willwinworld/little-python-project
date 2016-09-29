#! python3
# -*- coding: utf-8 -*-
"""http://python.jobbole.com/84905/"""
import string
import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter


numbers = ''.join(map(str, range(0, 10)))
letters = string.ascii_letters
init_chars = ''.join((letters, numbers))
text = ''.join(random.sample(init_chars, 4))

IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255, 255, 255)
Image_Font = 'arial.ttf'
LINE_NUM = (1, 2)


def random_color():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def create_identifying_code(strs, width=400, height=200, chance=2):
    im = Image.new(IMAGE_MODE, (width, height), IMAGE_BG_COLOR)
    draw = ImageDraw.Draw(im)
    # 绘制背景噪声
    for w in range(width):
        for h in range(height):
            if chance < random.randint(1, 100):
                draw.point((w, h), fill=random_color())

    # 绘制背景干扰线
    line_num = random.randint(*LINE_NUM)
    for _ in range(line_num):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=random_color())

    font = ImageFont.truetype(Image_Font, 80)  # 设置字体
    font_width, font_height = font.getsize(strs)
    strs_len = len(strs)
    x = (width - font_width) / 2
    y = (height - font_height) / 2
    # 逐个绘制文字
    for i in strs:
        draw.text((x, y), i, random_color(), font)
        x += font_width / strs_len  # 每个字的x坐标进行位移
    # 模糊
    im = im.filter(ImageFilter.BLUR)
    im.save('identifying_code_pic.jpg')

if __name__ == '__main__':
    create_identifying_code(text)

