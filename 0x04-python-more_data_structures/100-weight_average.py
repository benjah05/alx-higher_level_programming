#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    total_score = 0
    total_weight = 0
    for value, weight in my_list:
        total_score += value * weight
        total_weight += weight
    average = total / weight
    return (average)
