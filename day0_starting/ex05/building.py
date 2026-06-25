import sys


def main():
    """Program that take 1 argument or user input if none is given,
    count the number of uppercase, lowercase, digit, spaces and punctuation"""

    argc = len(sys.argv)

    try:
        assert argc <= 2, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(0)

    # declare the variable first so we can test if it exist or not,
    # put empty in it.
    user_input = ""
    if argc == 1:
        user_input = input("Enter a string:")

    # put whatever in string
    if (user_input):
        string = user_input
    else:
        string = sys.argv[1]

    Upp, Low, Pct, Spa, Dig, Tot = 0, 0, 0, 0, 0, 0

    # importing string would be a better way
    # (use of .punctuation()) but this is hardcoded.
    # also cleaner would be "if c in string"
    for i in range(len(string)):
        if string[i].isupper():
            Upp = Upp + 1
        elif string[i].islower():
            Low = Low + 1
        elif string[i].isdigit():
            Dig = Dig + 1
        elif string[i].isspace():
            Spa = Spa + 1
        else:
            Pct = Pct + 1
        Tot = Tot + 1

    print(f"The text contains {Tot} characters:")
    print(f"{Upp} upper letters")
    print(f"{Low} lower letters")
    print(f"{Pct} punctuation marks")
    print(f"{Spa} spaces")
    print(f"{Dig} digits")
    # you can see what a function __doc__ is via that :
    # print(main.__doc__)


if __name__ == "__main__":
    main()
