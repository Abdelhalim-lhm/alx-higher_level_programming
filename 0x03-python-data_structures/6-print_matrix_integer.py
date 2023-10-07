#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for i in row:
            if i == row[len(row) - 1]:
                print("{:d}".format(i), end ="")
            else:
                print("{:d}".format(i), end = " ")
        print()
