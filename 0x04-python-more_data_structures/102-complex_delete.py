#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return (a_dictionary)
    for k, v in list(a_dictionary.items()):
        if v == value:
            del a_dictionary[k]
    return (a_dictionary)
