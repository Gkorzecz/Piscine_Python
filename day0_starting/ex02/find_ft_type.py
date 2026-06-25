def all_thing_is_obj(object: any) -> int:

    x = type(object)

    if (x == list):
        print("List :", x)
    elif (x == tuple):
        print("Tuple :", x)
    elif (x == set):
        print("Set :", x)
    elif (x == dict):
        print("Dict :", x)
    elif (x == str):
        print (object, "is in the kitchen :", x)
    else:
        print("Type not found")
        
    return 42

