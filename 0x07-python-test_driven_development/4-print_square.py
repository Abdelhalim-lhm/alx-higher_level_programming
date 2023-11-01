#!/usr/bin/python3
''' print_square module '''


def print_square(size):
    '''  function that prints a square with the character # '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.filetest("tests/4-print_square.txt")
