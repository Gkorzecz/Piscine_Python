import matplotlib.pyplot as plt
import numpy as np


def ft_invert(image: np.ndarray):
    """Inverts the color of the image received."""
    # !WARNING! this does NOT create a new image is you dont use .copy()
    inverted_image = image.copy()
    rgb_invert_dict = {}
    height = inverted_image.shape[0]
    width = inverted_image.shape[1]
    channels = inverted_image.shape[2]

    for i in range(256):
        rgb_invert_dict[i] = 255 - i

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                value = inverted_image[y, x, c]
                inverted_image[y, x, c] = rgb_invert_dict[value]

    plt.imshow(inverted_image)
    plt.show()


def ft_blue(image: np.ndarray):
    """Display the blue channel of an RGB image"""
    # !WARNING! this does NOT create a new image is you dont use .copy()
    blue_image = image.copy()
    height = blue_image.shape[0]
    width = blue_image.shape[1]

    for y in range(height):
        for x in range(width):
            blue_image[y, x, 0] = 0
            blue_image[y, x, 1] = 0

    plt.imshow(blue_image)
    plt.show()


def ft_red(image: np.ndarray):
    """Display the red channel of an RGB image"""
    # !WARNING! this does NOT create a new image is you dont use .copy()
    red_image = image.copy()
    height = red_image.shape[0]
    width = red_image.shape[1]

    for y in range(height):
        for x in range(width):
            red_image[y, x, 1] = 0
            red_image[y, x, 2] = 0

    plt.imshow(red_image)
    plt.show()


def ft_green(image: np.ndarray):
    """Display the red channel of an RGB image"""
    # !WARNING! this does NOT create a new image is you dont use .copy()
    green_image = image.copy()
    height = green_image.shape[0]
    width = green_image.shape[1]

    for y in range(height):
        for x in range(width):
            green_image[y, x, 0] = 0
            green_image[y, x, 2] = 0

    plt.imshow(green_image)
    plt.show()


def ft_grey(image: np.ndarray):
    """Display shade of grey of an RGB image."""
    grey_image = image.copy()
    height = grey_image.shape[0]
    width = grey_image.shape[1]

    for y in range(height):
        for x in range(width):
            # using the '+' operator not authorized
            # grey_value = int((red + green + blue) / 3)
            grey_value = grey_image[y, x].mean()
            # directly assign the three channel value the same thing
            grey_image[y, x] = grey_value

    plt.imshow(grey_image)
    plt.show()
