#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    total_score = 0
    total_weight = 0
    for value in my_list:
        total_score += value[0] * value[1]
        total_weight += value[1]
    average = total_score / total_weight
    return (average)
