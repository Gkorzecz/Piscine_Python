import numpy as np


def ver_arg_BMI(height: list[int | float], weight: list[int | float]) -> bool:
    """Basic 'parser' for the bmi function"""
    # are those argument lists ?
    if type(height) is not list or type(weight) is not list:
        print("Argument is not a list")
        return False

    # are lists the same size ?
    if len(height) != len(weight):
        print("Different lenght list")
        return False

    # are lists not empty ?
    if not height or not weight:
        print("List is empty")
        return False

    # are elements of the list positive int or float ?
    for elem in height:
        if type(elem) not in (int, float) or elem <= 0:
            print("List contain invalid element")
            return False
    for elem in weight:
        if type(elem) not in (int, float) or elem <= 0:
            print("List contain invalid element")
            return False

    # all good
    return True


def verify_arguments_apply_limit(bmi: list[int | float], limit: int) -> bool:
    """Basic 'parser' for verify limit function"""
    if type(bmi) is not list:
        print("Argument is not a list")
        return False

    if not bmi:
        print("List is empty")
        return False

    if type(limit) is not int or limit <= 0:
        print("Limit is invalid")
        return False

    for elem in bmi:
        if type(elem) not in (int, float) or elem <= 0:
            print("List contain invalid element")
            return False

    return True


# def give_bmi(
#    height: list[int | float],
#    weight: list[int | float],
# -> list[int | float]:
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:  # noqa: E501
    """Give the body-mass index from a list"""
    try:
        assert ver_arg_BMI(height, weight), "invalid arguments"

        # empty for now
        bmi_array = np.array([])

        # Numpy will "convert" the type of elements,
        # if one float is found -> all float
        ha = np.array(height)
        wa = np.array(weight)

        for i in range(len(height)):
            # note that np.append DOESNT append to the list -> create a new
            bmi_array = np.append(bmi_array, [wa[i]] / (ha[i] * ha[i]))

        bmi_list = bmi_array.tolist()

        return bmi_list

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Is the BMI above the limit or not"""
    try:
        assert verify_arguments_apply_limit(bmi, limit), "invalid arguments"

        limit_list = []

        for elem in bmi:
            if elem > limit:
                limit_list.append(True)
            else:
                limit_list.append(False)

        return limit_list

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []


def main():

    print('\033[1m' + "Empty List :" + '\033[0m')
    h0 = []
    w0 = []
    b0 = give_bmi(h0, w0)

    print(b0)
    print(apply_limit(b0, 1))
    print("__________________________________________________________________")
    print()

    print('\033[1m' + "One Element List :" + '\033[0m')
    h1 = [1]
    w1 = [1]
    b1 = give_bmi(h1, w1)

    print(b1)
    print(apply_limit(b1, 1))
    print("__________________________________________________________________")
    print()

    print('\033[1m' + "Subject Test :" + '\033[0m')
    h2 = [2.71, 1.15]
    w2 = [165.3, 38.4]
    b2 = give_bmi(h2, w2)

    print(b2)
    print(apply_limit(b2, 26))
    print("__________________________________________________________________")
    print()

    print('\033[1m' + "Valid 11 elem list :" + '\033[0m')
    h3 = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
    w3 = [0.5, 1, 8, 16, 32, 40, 48, 56, 60, 68, 74]
    b3 = give_bmi(h3, w3)

    print(b3)
    print(apply_limit(b3, 1))
    print("__________________________________________________________________")
    print()

    print('\033[1m' + "Not a list :" + '\033[0m')
    h4 = (1)
    w4 = [1]
    b4 = give_bmi(h4, w4)

    print(b4)
    print(apply_limit(b4, 1))
    print("__________________________________________________________________")
    print()

    print('\033[1m' + "Element not int or float :" + '\033[0m')
    h5 = ["banana"]
    w5 = [1]
    b5 = give_bmi(h5, w5)

    print(b5)
    print(apply_limit(b5, 1))
    print("__________________________________________________________________")
    print()

    print('\033[1m' + "Different lenght list :" + '\033[0m')
    h6 = [1, 2]
    w6 = [1]
    b6 = give_bmi(h6, w6)

    print(b6)
    print(apply_limit(b6, 1))
    print("__________________________________________________________________")


if __name__ == "__main__":
    main()
