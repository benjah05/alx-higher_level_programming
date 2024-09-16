#!/usr/bin/python3
def no_c(my_string):
    no_c_string = ""
    for i in my_string:
        if i not in 'cC':
            no_c_string += i
    return (no_c_string)
