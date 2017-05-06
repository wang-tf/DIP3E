#!/usr/bin/env pytho3
# _*_ coding:utf-8 _*_

from PIL import Image
from PIL import ImageStat
import numpy as np


def complementary(image):
    bash = 255 + np.zeros(np.array(image).shape)
    result = bash - np.array(image)
    result = Image.fromarray(result)
    return result


def union(image):
    imagearray = np.array(image)
    shape = imagearray.shape
    bash = (3 * ImageStat.Stat(image).mean[0]) * np.ones(shape)
    bash.astype('uint8')
    for i in range(shape[0]):
        for j in range(shape[1]):
            imagearray[i][j] = max(imagearray[i][j], bash[i][j])
    result = Image.fromarray(imagearray)
    return result


def main():
    with Image.open('./images/Fig0232(a)(partial_body_scan).tif') as image:
        output1 = complementary(image)
        output2 = union(image)
        output1.show()
        output2.show()


if __name__ == '__main__':
    main()
