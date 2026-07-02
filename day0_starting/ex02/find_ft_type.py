def all_thing_is_obj(object: any) -> int:

    # pretty straightforward, the clue is everything should be hardcoded from : "Type not found"
    # also the difference between type(object) and the object himself
    
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

