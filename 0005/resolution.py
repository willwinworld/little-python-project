#! python3
# -*- coding: utf-8 -*-
from glob import glob
from PIL import Image
"""改变所有图片的分辨率，不大于iphone5的分辨率"""


IPHONE5_WIDTH = 1136
IPHONE5_HEIGHT = 640


# def reset_size(width=IPHONE5_WIDTH, height=IPHONE5_HEIGHT):
#     # for picture in glob('saber'):
#     image = Image.open('cat.png')
#     image_width, image_height = image.size
#     print(image_width, image_height)
#     change_width = float(image_width) / width
#     change_height = float(image_height) / height
#
#     if change_width > 1 or change_height > 1:
#         change = change_width if change_width > change_height else change_height
#         print(change)
#         print(int(width / change), int(height / change))
#         image.resize((int(image_width / change), int(image_height / change)), Image.ANTIALIAS).save('result.png')
#
#
# if __name__ == '__main__':
#     reset_size()


def reset_size(resolution):
    count = 1
    for picture in glob('saber/*'):
        image = Image.open(picture)
        x, y = image.size
        print(x, y)
        change_x = float(x) / resolution[0]
        change_y = float(y) / resolution[1]

        if change_x > 1 or change_y > 1:
            change = change_x if change_x > change_y else change_y
            print(change)
            print(int(resolution[0] / change), int(resolution[1] / change))
            image.resize((int(x / change), int(y / change)), Image.ANTIALIAS).save('res/result_%s.jpg' % count)
            count += 1


if __name__ == '__main__':
    reset_size((1136, 640))

