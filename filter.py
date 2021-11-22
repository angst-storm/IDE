# import sys
from PIL import Image
import numpy as np


def median_gray(arr, step):
    """
        Находит самое близкое к среднему значению массива arr число, кратное шагу step.
        :param arr: array
        :param step: int
        :return: int
        >>> median_gray([0, 50, 100], 50)
        50
        >>> median_gray([0, 1, 2], 50)
        0
        >>> median_gray([0, 50, 250], 50)
        100
        >>> median_gray([40, 28, 61], 1)
        43
    """
    return int(np.mean(arr) // step) * step


def gray_pixelation(image, size, gradations):
    step = int(255 // (gradations - 1))
    arr = np.array(image)
    for row in range(0, len(arr), size):
        for column in range(0, len(arr[1]), size):
            arr[row:row + size, column:column + size] = \
                median_gray(arr[row:row + size, column:column + size], step)
    return Image.fromarray(arr)


if __name__ == "__main__":
    # gray_pixelation(Image.open(sys.argv[1]), 10, 5).save(sys.argv[2])
    gray_pixelation(
        Image.open(input("Имя исходного изображения: ")),
        int(input("Размер пикселя: ")),
        int(input("Число градаций серого: "))
    ).save(
        input("Имя результата: ")
    )
