import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    image = ft_load("animal.jpeg")

    if image is None:
        return

    print(image)

    try:
        zoomed = image[200:600, 300:700, 0:1]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        plt.imshow(zoomed, cmap='gray')
        plt.show()

    except Exception as error:
        print(f"Error while zooming image: {error}")

if __name__ == "__main__":
    main()
