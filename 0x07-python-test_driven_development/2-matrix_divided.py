#!/usr/bin/python3
''' matrix_divided module '''


def matrix_divided(matrix, div):
    ''' function that divides all elements of a matrix '''
    for row in matrix:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
