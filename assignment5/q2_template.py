# -*- coding: utf-8 -*-
"""
Template for homework exercise 5, question 2
Fundamentals of CS for EE students 2023
"""

import numpy as np
from matplotlib import pyplot as plt
import math as M
from skimage import data
from skimage.color import rgb2gray


def gaussian_kernel(
    row: int,
    col: int,
    mean_v: float = 0,
    std_v: float = None,
    mean_h: float = 0,
    std_h: float = None,
) -> np.ndarray:
    g = gaussian(std_v, std_h, mean_v + int(row / 2), mean_h + int(col / 2))
    out = np.array(list([g(i, j) for j in range(col)] for i in range(row)))
    return out


# an aux function that returns the function of the gaussian kernel according to init conditions
def gaussian(sig_x, sig_y, mu_x, mu_y):
    C = 1 / (sig_x * sig_y * (2 * M.pi)**0.5)
    x_co = lambda x: ((x - mu_x) ** 2) / (2 * sig_x**2)
    y_co = lambda y: ((y - mu_y) ** 2) / (2 * sig_y**2)
    g = lambda x, y: C * M.exp(-(x_co(x) + y_co(y)))
    return g


def gaussian_blur(image: np.ndarray, g_ker: np.ndarray):
    m, n = g_ker.shape
    x, y = image.shape
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            im_slice = np.zeros((m, n))
            exceeds_x = i + m > x
            exceeds_y = j + n > y

            end_x = m if not exceeds_x else x-i
            end_y= n if not exceeds_y else y-j

            im_slice[:end_x,:end_y] = image[i:i+end_x,j:j+end_y]

            g_sum = np.array(g_ker * im_slice)
            image[i, j] = sum(sum(g_sum))
    return image


if __name__ == "__main__":
    image = data.astronaut()
    image_grey = rgb2gray(image)  # converts color images to black-and-white
    plt.imshow(image)
    plt.imshow(image_grey, cmap="gray")
    plt.imsave("q2a.png", image_grey)
    # plt.show()

    g_ker = gaussian_kernel(100, 50, mean_v=0, std_v=15, mean_h=-0, std_h=10)
    plt.imshow(g_ker, cmap="gray")
    plt.imsave("q2b.png", g_ker)
    plt.show()

    image_blur = gaussian_blur(image_grey, g_ker)
    plt.imshow(image_blur, cmap="gray")
    plt.imsave("q2c.png", image_blur)
    plt.show()
