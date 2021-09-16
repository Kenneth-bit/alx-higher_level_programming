#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new2 = []
        for j in i:
            new2.append(j**2)
        new.append(new2)
    return new
