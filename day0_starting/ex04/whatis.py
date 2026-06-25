import sys

# thanks geeksforgeeks.org :
# number of argument give by : len(sys.argv), sys.argv[0] is program name
argc = len(sys.argv)

# use of sys.exit() insteand of defining a __main__

if argc == 1:
    sys.exit(0)

try:
    assert argc <= 2, "more than one argument is provided"
except AssertionError as e:
    print(f"AssertionError: {e}")
    sys.exit(1)

# little going around the subject here, you can't assert that a string is an int if argv[1] can't already be converted to an int (raise an error)
try:
    nb = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)


if (nb % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
