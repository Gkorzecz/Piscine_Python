import numpy as np


def parsing(family: list, start: int, end: int) -> bool:
    """Verify argument from function slice_me"""
    if type(family) is not list:
        print("Not a list")
        return False

    if type(start) is not int or type(end) is not int:
        print("Start or End not an int")
        return False

    if not family:
        print("List is empty")
        return False

    for elem in family:
        if type(elem) is not list or not elem:
            print("list invalid (type or empty)")
            return False
        for item in elem:
            if type(item) not in (int, float) or not item:
                print("item of list invalid (type or empty)")
                return False

    family_lenght = len(family[0])
    for elem in family:
        if len(elem) != family_lenght:
            print("Different list size")
            return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """Give a new array sliced from start to end"""
    try:
        assert parsing(family, start, end), "invalid arguments"
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        sliced_arr = arr[start:end]
        print(f"My new shape is {sliced_arr.shape}")
        return sliced_arr.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []


def main():
    print("Subject test :")
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print("__________________________________________________________________")
    print()

    print("Empty list :")
    family = []
    print(slice_me(family, 0, 2))
    print("__________________________________________________________________")
    print()

    print("Empty element / Invalid element:")
    family = [[], []]
    family_1 = [["banana", "kiwi"], [2, 3]]
    print(slice_me(family, 0, 2))
    print(slice_me(family_1, 0, 2))
    print("__________________________________________________________________")
    print()

    print("Different lenght :")
    family = [[2, 3], [1]]
    print(slice_me(family, 0, 2))
    print("__________________________________________________________________")
    print()

    print("Valid list")
    family = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print(slice_me(family, 0, 2))
    print("__________________________________________________________________")


if __name__ == "__main__":
    main()
