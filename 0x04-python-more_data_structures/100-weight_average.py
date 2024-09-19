#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    total = 1
    total_score = 0
    weight = 0
    for elem in my_list:
        for i in elem:
            total_score *= i
        weight += i
        total += total_score
    average = total / weight
    return (average)
