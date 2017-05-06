#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from PIL import Image
import numpy as np


def division(image_a, image_b):
    result = np.array(image_a) - np.array(image_b)
    result = Image.fromarray(result, 'L')
    return result


def main():
    with Image.open('./images/Fig0229(a)(tungsten_filament_shaded).tif') as image_a, \
            Image.open('./images/Fig0229(b)(tungsten_sensor_shading).tif') as image_b:
        output = division(image_a, image_b)
        image_a.show()
        output.show()


if __name__ == '__main__':
    main()