import numpy as np


def verify_arguments_BMI(height: list[int | float], weight: list[int | float]) -> bool:

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
    if type(bmi) is not list:
        print("Argument is not a list")
        return False
    
    if not bmi:
        print("List is empty")
        return False

    if type(limit) is not int:
        print("Limit is invalid")
        return False
    if limit <= 0:
        print("Limit should be stricly positive")
        return False

    for elem in bmi:
        if type(elem) not in (int, float) or elem <= 0:
            print("List contain invalid element")
            return False
    
    return True
    

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert verify_arguments_BMI(height, weight), "invalid arguments"

        # empty for now
        bmi_array = np.array([])

        # Numpy will "convert" the type of elements, if one float is found -> all float
        height_array = np.array(height)
        weight_array = np.array(weight)
        
        for i in range(len(height)):
            # note that np.append DOESNT append to the list -> create a new, that fool
            bmi_array = np.append(bmi_array, [weight_array[i]] / (height_array[i] * height_array[i]))

        bmi_list = bmi_array.tolist()

        return bmi_list


    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
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
    thislist = [1]
    thatlist = [1]
    print(give_bmi(thislist, thatlist))
    print(apply_limit(give_bmi(thislist, thatlist), 1))

if __name__ == "__main__":
    main()