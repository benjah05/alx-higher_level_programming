#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return ({})
    b_dictionary = dict(sorted(a_dictionary.items()))
    for k, v in b_dictionary.items():
        print("{:s}: {}".format(k, v))
