#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    resulting_matrix = []
    for value in matrix:
        new_matrix = []
        for number in value:
            new_matrix.append(number**2)
        resulting_matrix.append(new_matrix)
    return resulting_matrix
