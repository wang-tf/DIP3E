#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from PIL import Image
import numpy as np


def local_fuzzy(image, m, n):
    imagearray = np.array(image)
    shape = np.zeros((imagearray.shape[0]+m-1, imagearray.shape[1]+n-1))
    shape[((m-1)/2):-((m-1)/2)][((n-1)/2):-((n-1)/2)] = imagearray
    result = np.zeros(imagearray.shape)
    print(imagearray.shape)
    for i in range(imagearray.shape[0]):
        for j in range(imagearray.shape[1]):
            xmin = i - int((m - 1) / 2)
            ymin = j - int((n - 1) / 2)
            xmax = i + int((m - 1) / 2)
            ymax = j + int((m - 1) / 2)
            # if xmin < 0 and ymin < 0:
            #     number = (m + ) * n - ((0 - xmin) * (0 - ymin) + (0 - xmin) * j + (0 - ymin) * i)
            # elif xmin < 0 and ymin > 0:
            #     number = m * n - ((0 - xmin) * (0 - ymin) + (0 - xmin) * j + (0 - ymin) * i)
            result[i][j] = np.sum(shape[i:i+m][j:j+n]) / (m * n)

    result = Image.fromarray(result)
    return result


def main():
    with Image.open('./images/Fig0235(c)(kidney_original).tif') as image:
        m = 41
        n = 41
        output = local_fuzzy(image, m, n)
        output.show()


if __name__ == '__main__':
    main()
