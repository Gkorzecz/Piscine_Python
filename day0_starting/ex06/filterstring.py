import sys


def main():
    # your tests and your error handling
    """DOCUMENTATION"""

    argc = len(sys.argv)

    try:
        assert argc == 3, "arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(0)

    try:
        nb = str(sys.argv[1])
    except ValueError:
        print("AssertionError: arguments are bad")
        sys.exit(0)

    try:
        nb = int(sys.argv[2])
    except ValueError:
        print("AssertionError: arguments are bad")
        sys.exit(0)

    # the format of the output is clearly a result of split
    words = sys.argv[1].split(" ")

    # list comprehension and lambda
    # note that assigning a variable from a lambda will make flake8 complain
    result = [word for word in words if (lambda x: len(x) > nb)(word)]

    print(result)


if __name__ == "__main__":
    main()
