# -*- coding: utf-8 -*-
"""
Template for homework exercise 5, question 2
Fundamentals of CS for EE students 2023
"""

import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage.color import rgb2gray


def gaussian_kernel(row, col, mean_v=0, std_v=None, mean_h=0, std_h=None):
    """
    Returns an array that acts as a Gaussian convolution filter with shape (row, col)
    Parameters
    ----------
    row : TYPE int
        DESCRIPTION. Number of rows in filter.
    col : TYPE int
        DESCRIPTION. Number of columns in filter.
    mean_v: TYPE float
        DESCRIPTION. The location of the kernel mean, along the vertical axis.
                        If not specified, is set by default to 0 (center of kernel)
    std_v:TYPE float
            DESCRIPTION. The standard deviation of the kernel, along the vertical axis (axis=0).
                            If not specified, is set by default to 1/2 the size of the vertical axis.
    mean_h: TYPE float
            DESCRIPTION. The location of the kernel mean, along the horizontal axis (axis=1).
                            If not specified, is set by default to 0 (center of kernel).
    std_v:TYPE float
            DESCRIPTION. The standard deviation of the kernel, along the horizontal axis (axis=1).
                            If not specified, is set by default to 1/2 the size of the horizontal axis.

    Returns
    -------
    g_ker: TYPE ndarray
        DESCRIPTION. The Gaussian convolution kernel
    """
    pass


def gaussian_blur(image, g_ker):
    """Applies gaussian blurring to input image using Gaussian kernel g_ker"""
    pass


if __name__ == "__main__":
    image = data.astronaut()
    image_grey = rgb2gray(image)  # converts color images to black-and-white
    plt.imshow(image)
    plt.imshow(image_grey, cmap="gray")
    plt.imsave("q2a.png", image_grey)

    g_ker = gaussian_kernel(100, 50, mean_v=0, std_v=15, mean_h=-0, std_h=10)
    plt.imshow(g_ker, cmap="gray")
    plt.imsave("q2b.png", g_ker)

    image_blur = gaussian_blur(image_grey, g_ker)
    plt.imshow(image_blur, cmap="gray")
    plt.imsave("q2c.png", image_blur)
