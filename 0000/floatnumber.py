#! python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
"""图片原点坐标为左上角，现在要确定图片的右上角"""
"""http://yxnt.github.io/2016/05/15/Pillow-Python3.5/"""
"""http://blog.csdn.net/justheretobe/article/details/50612618"""



# im = Image.open("cat.png")
# print(im.format, im.size, im.mode)


# def draw():
#     with Image.open('cat.png').convert('RGBA') as im:  # 打开
#         new = Image.new(im.mode, im.size)
#         font = ImageFont.truetype('Arial/Arial.ttf', 66)
#         d = ImageDraw.Draw(new)
#         d.ellipse((575, 50, 675, 150), 'red')
#         d.text((605, 55), '1', font=font, fill=(255, 255, 255))
#
#         out = Image.alpha_composite(im, new)
#         out.save('new.png')
#         out.show()
#
# draw()


# with Image.open('cat.png') as im:
#     im_to_draw = im.copy()
#     draw = ImageDraw.Draw(im_to_draw)
#     font = ImageFont.truetype('Arial/Arial.ttf', 40)
#
#     text = '1'
#     position_x, position_y = (1348, 20)
#     color = (255, 0, 0)
#     draw.text((position_x, position_y), text, color, font=font)
#     im_to_draw.save('im_draw_font.png')
#     im_to_draw.show()


def cat():
    with Image.open('cat.png').convert('RGBA') as im:
        im_to_draw = im.copy()  # 创建新图片
        font = ImageFont.truetype('Arial/Arial.ttf', 66)  # 设置新字体
        draw = ImageDraw.Draw(im_to_draw)  # 初始化画图实例
        draw.ellipse((1200, 20, 1300, 120), fill='red', outline='red')  # 对应坐标分别为x1,y1, x2, y2,要画个圆，
        # x2-x1要等于y2-y1,然后注意坐标不能超过im.size，想要圆处于图片的右上角，这只要关注一组坐标就行了，比如说只关注x1,y1,
        # 由于原点在左上角(0, 0),所以x1往右移动，y1增加往下移动
        draw.text((1230, 32), '1', font=font, fill=(255, 255, 255))  # 要将数字写在圆的中间，则x,y坐标要在x1,x2,y1,y2中间，
        # 然后慢慢调整

        out = Image.alpha_composite(im, im_to_draw)  # 组合两个图片
        out.save('perfect.png')
        out.show()

cat()