import sys


def verify_string(text: str) -> bool:
    for c in text:
        if not c.isalnum() and not c.isspace():
            return False
    return True


def main():
    argc = len(sys.argv)

    try:
        assert argc == 2, "the arguments are bad"
        assert verify_string(sys.argv[1]), "the arguments are bad"

        # all lowercase transformed into uppercase
        # morse don't deal with case, no need to expand the dict
        upper_text = sys.argv[1].upper()

        morse_code = {
            " ": "/",
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
        }

        # we just need to not print space at the end,
        # note that print add a \n by default, change with "end="
        for i in range(len(upper_text)):
            if i != len(upper_text) - 1:
                print(morse_code[upper_text[i]], end=" ")
            else:
                print(morse_code[upper_text[i]])

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(0)


if __name__ == "__main__":
    main()
