def ft_filter(function, iterable) -> iter:
    """filter(function or None, iterable) --> filter object


Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])

# print(filter.__doc__)

# simple example for list comprehension :
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


# MAIN TEST
def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False


def main():
    print("Our function ft_filter :")
    even_numbers = ft_filter(is_even, [1, 2, 3, 4, 18, 222, 15])
    for x in even_numbers:
        print(x)

    print("original filter:")
    even_numbers = filter(is_even, [1, 2, 3, 4, 18, 222, 15])
    for x in even_numbers:
        print(x)

    print("None for ft_filter :")
    even_numbers = ft_filter(None, [1, 2, 3, 4, 18, 222, 15])
    for x in even_numbers:
        print(x)

    print("None for filter:")
    even_numbers = filter(None, [1, 2, 3, 4, 18, 222, 15])
    for x in even_numbers:
        print(x)


if __name__ == "__main__":
    main()
