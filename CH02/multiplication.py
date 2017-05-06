#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from PIL import Image
import numpy as np


def multiplication(image_a, bash):
    bash = (1.0 / 255) * np.array(bash)
    bash = np.round(bash)
    bash = bash.astype('uint8')  # if not change the type of bash , it will be error
    print(bash)
    result = np.array(image_a) * bash
    print(bash.dtype)
    result = Image.fromarray(result, 'L')
    return result


def main():
    with Image.open('./images/Fig0230(a)(dental_xray).tif') as image_a, \
            Image.open('./images/Fig0230(b)(dental_xray_mask).tif') as image_b:
        output = multiplication(image_a, image_b)

        output.show()


if __name__ == '__main__':
    main()
