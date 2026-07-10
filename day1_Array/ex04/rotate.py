from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

# it would be as easy as this with .transpose() of numpy
# def main():

#     image = ft_load("animal.jpeg")

#     if image is None:
#         return

#     try:
#         # you can't do a simple tranpose : last channel can't move
#         # 0 -> 1, 1 -> 0 and 2 -> 2
#         transposed_image = np.transpose(image, (1, 0, 2))
#         plt.imshow(transposed_image, cmap='gray')
#         plt.show()
#     except Exception as error:
#         print(f"Error while zooming image: {error}")


def ft_transpose(image):
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    # don't forget to assign the dtype of the image
    # uint8 in original 0-255, because zeros() gives you floats 0.0
    transposed = np.zeros((width, height, channels), dtype=image.dtype)

    # switch order of loops x <-> y
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                transposed[x][y][c] = image[y][x][c]

    return transposed


def main():
    image = ft_load("animal.jpeg")

    if image is None:
        return

    try:
        zoomed_image = image[200:600, 300:700, 0:1]
        shape = zoomed_image.shape
        print(f"The shape of image is: {shape} or {shape[0:2]}")
        print(zoomed_image)

        transposed_image = ft_transpose(zoomed_image)
        transposed_shape = transposed_image.shape
        print(f"New shape after Transpose: {transposed_shape[0:2]}")
        print(transposed_image)

        plt.imshow(transposed_image, cmap="grey")
        plt.show()

    except Exception as error:
        print(f"Error while transposing image: {error}")


if __name__ == "__main__":
    main()
