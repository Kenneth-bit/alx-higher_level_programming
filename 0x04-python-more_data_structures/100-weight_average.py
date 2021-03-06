#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        total_score = 0
        total_weight = 0
        for tuple in range(len(my_list)):
            values = my_list[tuple]
            score, weight = values
            total_weight += weight
            product = weight * score
            total_score += product
        w_average = total_score / total_weight
        return w_average


weight_average([(1, 2), (2, 1), (3, 10), (4, 2)])
