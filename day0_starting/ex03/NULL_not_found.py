import math

def NULL_not_found(object: any) -> int:
    x = type(object)

    if object is None:
        print("Nothing:", object, x)
        return 0
    elif (x == float and math.isnan(object)):
        print("Cheese:", object, x)
        return 0
    elif (x == int and object == 0):
        print("Zero:", object, x)
        return 0
    elif (x == str and object == ""):
        print ("Empty:", object, x)
        return 0
    elif (x == bool and object == False):
        print ("Fake :", object, x)
        return 0
    else:
        print("Type not found")
        return 1
    print(x)
