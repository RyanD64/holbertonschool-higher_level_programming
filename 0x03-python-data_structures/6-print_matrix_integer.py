#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for char in range(len(matrix[row])):
                if char != len(matrix[row]) - 1:
                    final = ' '
                else:
                    final = ''
                print("{:d}".format(matrix[row][char]), end=final)
            print()
