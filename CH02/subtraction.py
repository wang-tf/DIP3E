#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

# 缺少配准

from PIL import Image
import numpy as np


def subtraction(image_a, image_b):
    result = np.array(image_a) - np.array(image_b)
    result = Image.fromarray(result)
    return result


def main():
    with Image.open('./images/Fig0228(a)(angiography_mask_image).tif') as image_a, \
            Image.open('./images/Fig0228(b)(angiography_live_ image).tif') as image_b:
        output = subtraction(image_a, image_b)
        output.show()


if __name__ == '__main__':
    main()
