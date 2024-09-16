#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return (my_list)
    iseven = []
    for i in my_list:
        if i % 2 == 0:
            iseven[i] = True
        else:
            iseven[i] = False
    return (iseven)
