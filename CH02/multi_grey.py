#!/usr/bin/env python2
# _*_ coding:utf-8 _*_

from PIL import Image
import numpy as np
import matplotlib as plt


def multi_grey_scale(image, scale):
    newimage = ((scale - 1) / 255) * np.array(image)
    newimage = (255 / (scale - 1)) * np.round(newimage)
    newimage = np.round(newimage)
    newimage = Image.fromarray(newimage)
    newimage = newimage.convert('L')  # 输入图像的模式为‘Ｌ’
    # newimage.show()
    print(newimage)
    newimage.save(str(scale) + '.tif', 'tiff')


def main():
    scales = {128.0, 64.0, 32.0, 16.0, 8.0, 4.0, 2.0}
    with Image.open('./images/Fig0221(a)(ctskull-256).tif') as image:
        print(image)
        for scale in scales:
            multi_grey_scale(image, scale)
        print('done')


if __name__ == '__main__':
    main()
