#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    resulting_matrix = []
    for i in matrix:
        new_matrix = []
        for j in i:
            new_matrix.append(j**2)
        resulting_matrix.append(new_matrix)
    return resulting_matrix
