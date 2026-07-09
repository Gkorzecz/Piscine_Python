import matplotlib.pyplot as plt
import numpy as np


def verify_extension(path: str) -> bool:
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
    try:
        if verify_extension(path) is False:
            return None

        image = plt.imread(path)
        print(f"The shape of image is: {image.shape}")
        return image

    except Exception as error:
        print(f"Error: {error}")
        return None
