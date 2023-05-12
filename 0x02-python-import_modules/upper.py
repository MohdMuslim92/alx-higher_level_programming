import string


def print_upper_letters(index=0):
    print(string.ascii_uppercase[index], end="")
    if index < 25:
        print_upper_letters(index + 1)
