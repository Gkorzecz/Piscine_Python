import matplotlib.pyplot as plt
import numpy as np


def check_rgb_image(image: np.ndarray) -> bool:
    """Check if the shape of the image is correct"""
    if not isinstance(image, np.ndarray):
        print("Error: image is not a NumPy array")
        return False

    if len(image.shape) != 3:
        print("Error: image does not have 3 dimensions")
        return False

    if image.shape[2] != 3:
        print("Error: image does not have 3 RGB channels")
        return False

    return True


def verify_extension(path: str) -> bool:
    """Check for extension in filename, only jpg and jpeg"""
    file_extension = ["jpg", "jpeg"]

    if '.' in path:
        # [-1] = the last element in the list.
        if path.split(".")[-1] in file_extension:
            return True
        else:
            print("Error: wrong extension: only '.jpg' and '.jpeg' authorized")
            return False
    # no '.' in the filename, so no extension.
    else:
        print("Error: invalid filename: no extension")
        return False


def ft_load(path: str) -> np.ndarray:
    """Load image with matplotlib"""
    try:
        if verify_extension(path) is False:
            return None

        image = plt.imread(path)
        if check_rgb_image(image) is False:
            return None

        print(f"The shape of image is: {image.shape}")
        print(image)
        plt.imshow(image)
        plt.show()
        return image

    except Exception as error:
        print(f"Error: {error}")
        return None
